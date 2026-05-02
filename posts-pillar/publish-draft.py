#!/usr/bin/env python3
"""Publish Cluster 3 Pillar Post to WordPress as DRAFT."""

import json
import re
import requests
from markdown_it import MarkdownIt

# --- Config ---
WP_URL = "https://hardlifeapparelco.com/wp-json/wp/v2"
AUTH = ("info@hardlifeapparelco.com", "8XZL 0I0C SFEJ RN7I 7A9P nyTd")

# --- Read and parse markdown ---
with open("cluster-3-pillar.md", "r") as f:
    raw = f.read()

# Strip frontmatter
parts = raw.split("---", 2)
body_md = parts[2].strip() if len(parts) >= 3 else raw

# Split out the JSON-LD HTML block (keep as raw HTML)
json_ld_match = re.search(r'(<!-- wp:html -->.*?<!-- /wp:html -->)', body_md, re.DOTALL)
json_ld_block = json_ld_match.group(1) if json_ld_match else ""

# Remove JSON-LD from markdown body before conversion
if json_ld_block:
    body_md_clean = body_md.replace(json_ld_block, "").strip()
else:
    body_md_clean = body_md

# Convert markdown to HTML
md = MarkdownIt("commonmark", {"html": True}).enable("table")
body_html = md.render(body_md_clean)

# Append JSON-LD block
if json_ld_block:
    body_html += "\n\n" + json_ld_block

# --- Create "Editorial" category ---
print("Creating 'Editorial' category...")
cat_resp = requests.post(
    f"{WP_URL}/categories",
    auth=AUTH,
    json={"name": "Editorial", "slug": "editorial"}
)
if cat_resp.status_code == 201:
    editorial_cat_id = cat_resp.json()["id"]
    print(f"  Created category ID: {editorial_cat_id}")
elif cat_resp.status_code == 400 and "term_exists" in cat_resp.text:
    editorial_cat_id = cat_resp.json().get("data", {}).get("term_id")
    print(f"  Category already exists, ID: {editorial_cat_id}")
else:
    print(f"  Warning: {cat_resp.status_code} — {cat_resp.text[:200]}")
    editorial_cat_id = 1  # fallback to Uncategorized

# --- Create/find tags ---
tag_names = [
    "independent streetwear",
    "indie brands",
    "founder-led",
    "skate culture",
    "philadelphia streetwear",
    "web3 streetwear",
    "2026",
]

tag_ids = []
for tag_name in tag_names:
    # Check if exists
    search_resp = requests.get(
        f"{WP_URL}/tags",
        auth=AUTH,
        params={"search": tag_name, "per_page": 5}
    )
    existing = search_resp.json()
    found = None
    for t in existing:
        if t["name"].lower() == tag_name.lower():
            found = t
            break

    if found:
        tag_ids.append(found["id"])
        print(f"  Tag '{tag_name}' exists: ID {found['id']}")
    else:
        create_resp = requests.post(
            f"{WP_URL}/tags",
            auth=AUTH,
            json={"name": tag_name}
        )
        if create_resp.status_code == 201:
            new_id = create_resp.json()["id"]
            tag_ids.append(new_id)
            print(f"  Tag '{tag_name}' created: ID {new_id}")
        else:
            print(f"  Warning creating tag '{tag_name}': {create_resp.status_code}")

# --- Build payload ---
payload = {
    "title": "Independent Streetwear Brands: The Complete Guide (2026)",
    "slug": "independent-streetwear-brands-2026",
    "content": body_html,
    "status": "draft",
    "categories": [editorial_cat_id],
    "tags": tag_ids,
    "excerpt": "14 independent streetwear brands still founder-owned in 2026 — no investors, no corporate parents. Shop direct from the best indie streetwear labels.",
    "meta": {
        "advanced_seo_description": "14 independent streetwear brands still founder-owned in 2026 — no investors, no corporate parents. Shop direct from the best indie streetwear labels."
    },
}

# --- Print payload summary ---
print("\n" + "=" * 60)
print("WP DRAFT PAYLOAD SUMMARY")
print("=" * 60)
print(f"Title:       {payload['title']}")
print(f"Slug:        {payload['slug']}")
print(f"Status:      {payload['status']}")
print(f"Category:    Editorial (ID: {editorial_cat_id})")
print(f"Tags:        {tag_names}")
print(f"Tag IDs:     {tag_ids}")
print(f"Meta desc:   {payload['meta']['advanced_seo_description'][:80]}...")
print(f"Excerpt:     {payload['excerpt'][:80]}...")
print(f"Content len: {len(body_html)} chars")
print(f"Featured img: independent-streetwear-brands-2026.png (to upload separately)")
print("=" * 60)

# --- POST draft ---
print("\nPublishing draft...")
resp = requests.post(
    f"{WP_URL}/posts",
    auth=AUTH,
    json=payload
)

if resp.status_code == 201:
    post = resp.json()
    post_id = post["id"]
    edit_link = post.get("link", "").replace("?p=", "?p=")
    preview_link = f"https://hardlifeapparelco.com/?p={post_id}&preview=true"

    print(f"\nDRAFT CREATED SUCCESSFULLY")
    print(f"  Post ID:     {post_id}")
    print(f"  Edit URL:    https://hardlifeapparelco.com/wp-admin/post.php?post={post_id}&action=edit")
    print(f"  Preview URL: {preview_link}")
    print(f"  Public URL (when published): https://hardlifeapparelco.com/{payload['slug']}/")

    # Save post ID for later use
    with open("cluster-3-post-id.txt", "w") as f:
        f.write(str(post_id))
else:
    print(f"\nFAILED: {resp.status_code}")
    print(resp.text[:500])
