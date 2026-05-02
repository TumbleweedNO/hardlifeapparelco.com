#!/usr/bin/env python3
"""
publish_to_wp.py — Automated WordPress publishing for HRDLFcoin blog series.

Usage:
  python3 publish_to_wp.py --dry-run    # Preview what would be published
  python3 publish_to_wp.py              # Publish for real

Requires: requests, python-frontmatter, markdown2
Install:  pip3 install requests python-frontmatter markdown2
"""

import os
import sys
import json
import re
import argparse
import requests
import frontmatter
import markdown2
from datetime import datetime
from pathlib import Path

# ─── CONFIG ───
API = "https://hardlifeapparelco.com/wp-json/wp/v2"
WP_USER = os.environ.get("WP_USER", "info@hardlifeapparelco.com")
WP_PASS = os.environ.get("WP_APP_PASSWORD", "8XZL 0I0C SFEJ RN7I 7A9P nyTd")
AUTH = (WP_USER, WP_PASS)

POSTS_DIR = Path(__file__).parent
IMAGES_DIR = POSTS_DIR / "featured-images"
LOG_FILE = POSTS_DIR / "publishing-log.md"

# Publishing order (file stems)
PUBLISH_ORDER = [
    "02-hrdlfcoin-hub",
    "01-why-solana",
    "03-token-utility",
    "04-19-years-on-chain",
    "05-ai-blockchain-convergence",
]


def verify_api():
    """Verify WP API access."""
    r = requests.get(f"{API}/posts?per_page=1", auth=AUTH, timeout=15)
    if r.status_code == 200:
        print("[OK] WP API access verified")
        return True
    else:
        print(f"[FAIL] WP API returned {r.status_code}: {r.text[:200]}")
        return False


def get_or_create_category(name):
    """Find or create a category by name, return its ID."""
    r = requests.get(f"{API}/categories?search={name}", auth=AUTH, timeout=15)
    for cat in r.json():
        if cat["name"].lower() == name.lower():
            return cat["id"]
    # Create it
    r = requests.post(f"{API}/categories", auth=AUTH,
                      json={"name": name}, timeout=15)
    if r.status_code == 201:
        return r.json()["id"]
    raise Exception(f"Could not create category '{name}': {r.text[:200]}")


def get_or_create_tag(name):
    """Find or create a tag by name, return its ID."""
    r = requests.get(f"{API}/tags?search={name}", auth=AUTH, timeout=15)
    for tag in r.json():
        if tag["name"].lower() == name.lower():
            return tag["id"]
    # Create it
    r = requests.post(f"{API}/tags", auth=AUTH,
                      json={"name": name}, timeout=15)
    if r.status_code == 201:
        return r.json()["id"]
    raise Exception(f"Could not create tag '{name}': {r.text[:200]}")


def upload_featured_image(slug):
    """Upload featured image if it exists, return media ID or None."""
    for ext in [".png", ".jpg", ".jpeg", ".webp"]:
        img_path = IMAGES_DIR / f"{slug}{ext}"
        if img_path.exists():
            mime_types = {
                ".png": "image/png",
                ".jpg": "image/jpeg",
                ".jpeg": "image/jpeg",
                ".webp": "image/webp",
            }
            headers = {
                "Content-Disposition": f'attachment; filename="{img_path.name}"',
                "Content-Type": mime_types[ext],
            }
            with open(img_path, "rb") as f:
                r = requests.post(f"{API}/media", auth=AUTH,
                                  headers=headers, data=f.read(), timeout=60)
            if r.status_code == 201:
                media_id = r.json()["id"]
                print(f"  [OK] Uploaded {img_path.name} → media ID {media_id}")
                return media_id
            else:
                print(f"  [WARN] Upload failed for {img_path.name}: {r.status_code}")
                return None
    return None


def md_to_gutenberg(md_body):
    """Convert markdown body to Gutenberg-compatible HTML blocks."""
    lines = md_body.strip().split("\n")
    blocks = []
    in_list = False
    list_items = []
    in_paragraph = False
    para_lines = []

    def flush_paragraph():
        nonlocal in_paragraph, para_lines
        if para_lines:
            text = " ".join(para_lines)
            # Check if it's an image prompt or just styling text — skip if wrapped in <!--
            if text.strip().startswith("<!--"):
                blocks.append(text.strip())
            else:
                blocks.append(f"<!-- wp:paragraph -->\n<p>{text}</p>\n<!-- /wp:paragraph -->")
            para_lines = []
            in_paragraph = False

    def flush_list():
        nonlocal in_list, list_items
        if list_items:
            items_html = "\n".join(f"<li>{item}</li>" for item in list_items)
            blocks.append(f"<!-- wp:list -->\n<ul>\n{items_html}\n</ul>\n<!-- /wp:list -->")
            list_items = []
            in_list = False

    for line in lines:
        stripped = line.strip()

        # Skip existing Gutenberg comments (they're already in the source)
        if stripped.startswith("<!-- wp:") or stripped.startswith("<!-- /wp:"):
            flush_paragraph()
            flush_list()
            blocks.append(stripped)
            continue

        # Headings
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if heading_match:
            flush_paragraph()
            flush_list()
            level = len(heading_match.group(1))
            text = heading_match.group(2)
            blocks.append(
                f'<!-- wp:heading {{"level":{level}}} -->\n'
                f'<h{level} class="wp-block-heading">{text}</h{level}>\n'
                f'<!-- /wp:heading -->'
            )
            continue

        # Horizontal rule
        if stripped == "---":
            flush_paragraph()
            flush_list()
            blocks.append("<!-- wp:separator -->\n<hr class=\"wp-block-separator\"/>\n<!-- /wp:separator -->")
            continue

        # List items
        list_match = re.match(r'^[-*]\s+(.+)$', stripped)
        if list_match:
            flush_paragraph()
            if not in_list:
                in_list = True
            list_items.append(convert_inline_md(list_match.group(1)))
            continue
        elif in_list and stripped == "":
            flush_list()
            continue
        elif in_list and not list_match:
            flush_list()

        # Empty line = paragraph break
        if stripped == "":
            flush_paragraph()
            continue

        # Regular text — accumulate into paragraph
        in_paragraph = True
        para_lines.append(convert_inline_md(stripped))

    flush_paragraph()
    flush_list()

    return "\n\n".join(blocks)


def convert_inline_md(text):
    """Convert inline markdown (bold, italic, links) to HTML."""
    # Links: [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # Bold: **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic: *text*
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text


def build_faq_schema(post_content):
    """Extract FAQ Q&As from post content and build FAQPage JSON-LD."""
    # Find FAQ section — look for patterns like **Question?**\nAnswer
    faq_pattern = re.findall(
        r'\*\*(.+?\?)\*\*\s*\n(.+?)(?=\n\*\*|\n## |\Z)',
        post_content, re.DOTALL
    )

    if not faq_pattern:
        return ""

    entities = []
    for question, answer in faq_pattern:
        answer_clean = answer.strip()
        # Remove markdown formatting from answer
        answer_clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', answer_clean)
        answer_clean = re.sub(r'\*\*(.+?)\*\*', r'\1', answer_clean)
        answer_clean = re.sub(r'\*(.+?)\*', r'\1', answer_clean)
        answer_clean = answer_clean.replace("\n", " ").strip()

        entities.append({
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": answer_clean
            }
        })

    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }

    return (
        '\n<!-- wp:html -->\n'
        '<script type="application/ld+json">\n'
        f'{json.dumps(schema, indent=2)}\n'
        '</script>\n'
        '<!-- /wp:html -->'
    )


def build_article_schema(title, slug, description, author, date_str):
    """Build Article JSON-LD schema."""
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "author": {
            "@type": "Person",
            "name": author,
            "url": "https://hardlifeapparelco.com/about/brooks-duvall/"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Hardlife Apparel Company LTD",
            "url": "https://hardlifeapparelco.com"
        },
        "datePublished": date_str,
        "dateModified": date_str,
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://hardlifeapparelco.com/{slug}/"
        }
    }

    return (
        '\n<!-- wp:html -->\n'
        '<script type="application/ld+json">\n'
        f'{json.dumps(schema, indent=2)}\n'
        '</script>\n'
        '<!-- /wp:html -->'
    )


def build_breadcrumb_schema(title, url):
    """Build BreadcrumbList JSON-LD schema."""
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home",
             "item": "https://hardlifeapparelco.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog",
             "item": "https://hardlifeapparelco.com/blog/"},
            {"@type": "ListItem", "position": 3, "name": title,
             "item": url}
        ]
    }

    return (
        '\n<!-- wp:html -->\n'
        '<script type="application/ld+json">\n'
        f'{json.dumps(schema, indent=2)}\n'
        '</script>\n'
        '<!-- /wp:html -->'
    )


def process_post(filepath, dry_run=False):
    """Process a single markdown post file and publish to WordPress."""
    post = frontmatter.load(filepath)
    meta = post.metadata
    body = post.content

    title = meta["title"]
    slug = meta["slug"]
    description = meta["meta_description"]
    author = meta.get("author", "Brooks Duvall")
    category_name = meta.get("category", "HRDLFcoin")
    tags = meta.get("tags", [])
    publish_date = meta["publish_date"]
    focus_kw = meta.get("focus_keyword", "")

    print(f"\n{'='*60}")
    print(f"POST: {title}")
    print(f"SLUG: {slug}")
    print(f"DATE: {publish_date}")
    print(f"{'='*60}")

    # Convert body to Gutenberg blocks
    content = md_to_gutenberg(body)

    # Add FAQ schema
    faq_schema = build_faq_schema(body)
    if faq_schema:
        content += faq_schema
        print("  [OK] FAQPage schema added")

    # Add Article schema
    article_schema = build_article_schema(
        title, slug, description, author, publish_date
    )
    content += article_schema
    print("  [OK] Article schema added")

    # Add Breadcrumb schema (URL will be date-based, but use slug for now)
    breadcrumb_schema = build_breadcrumb_schema(
        title, f"https://hardlifeapparelco.com/{slug}/"
    )
    content += breadcrumb_schema
    print("  [OK] BreadcrumbList schema added")

    if dry_run:
        print(f"  [DRY RUN] Would publish as 'future' scheduled for {publish_date}")
        print(f"  [DRY RUN] Category: {category_name}")
        print(f"  [DRY RUN] Tags: {', '.join(tags)}")
        print(f"  [DRY RUN] Meta description: {description[:80]}...")
        print(f"  [DRY RUN] Focus keyword: {focus_kw}")

        # Check for featured image
        file_stem = filepath.stem
        has_image = any(
            (IMAGES_DIR / f"{file_stem}{ext}").exists()
            for ext in [".png", ".jpg", ".jpeg", ".webp"]
        )
        print(f"  [DRY RUN] Featured image: {'FOUND' if has_image else 'NOT FOUND (will publish without)'}")

        return {
            "title": title,
            "slug": slug,
            "date": publish_date,
            "post_id": "DRY-RUN",
            "image_status": "Found" if has_image else "Missing",
            "seo_status": "Ready"
        }

    # ─── LIVE PUBLISH ───

    # Get/create category
    cat_id = get_or_create_category(category_name)
    print(f"  [OK] Category '{category_name}' → ID {cat_id}")

    # Get/create tags
    tag_ids = []
    for tag_name in tags:
        tag_id = get_or_create_tag(tag_name)
        tag_ids.append(tag_id)
    print(f"  [OK] Tags resolved: {len(tag_ids)} tags")

    # Upload featured image
    file_stem = filepath.stem
    media_id = upload_featured_image(file_stem)

    # Create the post
    post_data = {
        "title": title,
        "slug": slug,
        "content": content,
        "excerpt": description,
        "status": "future",
        "date": publish_date,
        "categories": [cat_id],
        "tags": tag_ids,
        "meta": {
            "advanced_seo_description": description,
        }
    }

    if media_id:
        post_data["featured_media"] = media_id

    r = requests.post(f"{API}/posts", auth=AUTH, json=post_data, timeout=30)

    if r.status_code == 201:
        post_id = r.json()["id"]
        link = r.json()["link"]
        print(f"  [OK] Published → ID {post_id}, {link}")

        # Try to set Yoast/Jetpack SEO fields
        seo_status = "Excerpt set"
        try:
            r_meta = requests.post(f"{API}/posts/{post_id}", auth=AUTH, json={
                "meta": {
                    "advanced_seo_description": description,
                    "jetpack_seo_html_title": title,
                }
            }, timeout=15)
            if r_meta.status_code == 200:
                seo_status = "Jetpack SEO set"
                print(f"  [OK] Jetpack SEO meta set")
            else:
                print(f"  [WARN] Jetpack SEO meta failed ({r_meta.status_code}), excerpt used as fallback")
        except Exception as e:
            print(f"  [WARN] SEO meta error: {e}")

        return {
            "title": title,
            "slug": slug,
            "date": publish_date,
            "post_id": post_id,
            "image_status": "Uploaded" if media_id else "Missing",
            "seo_status": seo_status
        }
    else:
        print(f"  [FAIL] Post creation failed: {r.status_code}")
        print(f"  {r.text[:300]}")
        return {
            "title": title,
            "slug": slug,
            "date": publish_date,
            "post_id": f"FAILED ({r.status_code})",
            "image_status": "N/A",
            "seo_status": "N/A"
        }


def write_log(results):
    """Write publishing log to markdown file."""
    log = "# HRDLFcoin Blog Series — Publishing Log\n\n"
    log += f"**Published:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    log += "| Post | Slug | Scheduled Date | WP Post ID | Featured Image | SEO Status |\n"
    log += "|------|------|---------------|------------|----------------|------------|\n"

    for r in results:
        log += (
            f"| {r['title'][:45]}... | "
            f"`{r['slug']}` | "
            f"{r['date'][:10]} | "
            f"{r['post_id']} | "
            f"{r['image_status']} | "
            f"{r['seo_status']} |\n"
        )

    warnings = [r for r in results if r["image_status"] == "Missing"]
    if warnings:
        log += "\n## Warnings\n\n"
        for w in warnings:
            log += f"- **{w['slug']}**: No featured image found. Generate from prompt in `featured-images/{w['slug']}-prompt.txt` and re-run.\n"

    log += "\n## Next Steps\n\n"
    log += "1. Generate featured images from prompts in `featured-images/`\n"
    log += "2. Drop PNGs as `featured-images/[file-stem].png`\n"
    log += "3. Re-run `publish_to_wp.py` to upload images (script will update existing posts)\n"
    log += "4. After hub post publishes, review internal link suggestions for older posts\n"

    with open(LOG_FILE, "w") as f:
        f.write(log)

    print(f"\n[OK] Publishing log written to {LOG_FILE}")


def main():
    parser = argparse.ArgumentParser(description="Publish HRDLFcoin blog series to WordPress")
    parser.add_argument("--dry-run", action="store_true", help="Preview without publishing")
    args = parser.parse_args()

    print("=" * 60)
    print("HRDLFcoin Blog Series Publisher")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE PUBLISH'}")
    print("=" * 60)

    if not verify_api():
        sys.exit(1)

    results = []
    for stem in PUBLISH_ORDER:
        filepath = POSTS_DIR / f"{stem}.md"
        if not filepath.exists():
            print(f"\n[WARN] File not found: {filepath}")
            continue
        result = process_post(filepath, dry_run=args.dry_run)
        results.append(result)

    # Summary table
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"{'Title':<50} {'Date':<12} {'ID':<8} {'Image':<10} {'SEO':<15}")
    print("-" * 95)
    for r in results:
        print(f"{r['title'][:48]:<50} {r['date'][:10]:<12} {str(r['post_id']):<8} {r['image_status']:<10} {r['seo_status']:<15}")

    write_log(results)

    if not args.dry_run:
        print("\n[INFO] Posts scheduled. Internal link suggestions for older posts will be shown separately.")
        print("[INFO] Run with --dry-run first to preview changes to older posts.")


if __name__ == "__main__":
    main()
