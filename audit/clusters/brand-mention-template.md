# BRAND MENTION RECOVERY — Templates + Google Alerts Setup

## Step 1: Set Up Google Alerts

Go to google.com/alerts and create these 5 alerts:

| Alert Query | Frequency | Sources |
|-------------|-----------|---------|
| "Hardlife Apparel" | As-it-happens | Everything |
| "HRDLF" -site:hardlifeapparelco.com -site:hrdlf.com | As-it-happens | Everything |
| "HRDLFcoin" -site:hrdlfcoin.com | As-it-happens | Everything |
| "Brooks Duvall" streetwear | As-it-happens | Everything |
| "Hardlife Apparel Company" | As-it-happens | Everything |

Deliver to: your primary email. Format: RSS or email.

---

## Step 2: Check Existing Unlinked Mentions

Known mentions to check for links (from previous research):

1. **OpenPR press release** — openpr.com/news/4341386 — likely links to hrdlf.com already. Verify.
2. **Reddit mentions** — check r/streetwear, r/streetwearstartup for HRDLF/Hardlife mentions
3. **X/Twitter mentions** — not linkable in the traditional sense, but useful for relationship building
4. **Any blog or forum that mentioned the AI rebuild** — check Google: "hardlife apparel" -site:hardlifeapparelco.com

---

## Step 3: Outreach Email Templates

### Template A — Warm Thank-You (for positive mentions)

```
Subject: Quick thanks + a small favor

Hey [name],

Saw your piece on [topic]. Appreciate the mention of Hardlife Apparel.

If it's not too much trouble, would you be open to adding a link to
hrdlf.com? Helps people find us directly.

Either way — thanks for the write-up.

Brooks
Hardlife Apparel Company
hrdlf.com
```

### Template B — Correction/Update (for outdated or incorrect info)

```
Subject: Quick update on Hardlife Apparel

Hey [name],

Noticed your [article/post] mentions Hardlife Apparel — thanks for
including us.

One quick update: [correction — e.g., "we're based in Philadelphia,
not NYC" or "the brand was founded in 2006, not 2007"]. If you get
a chance to update, that'd be great. Happy to provide any other
details.

Also, if you could link to hardlifeapparelco.com or hrdlf.com,
that helps readers find us directly.

Brooks
Hardlife Apparel Company
hrdlf.com
```

### Template C — Value-Add (for listicles or roundups)

```
Subject: Update for your [streetwear/independent brands] piece

Hey [name],

Saw your roundup on [topic]. Good list.

Quick pitch for an update: Hardlife Apparel (HRDLF) might fit.
Founded 2006 in Philadelphia, still founder-owned, zero investors.
19 years independent. We just launched a Solana community token
(HRDLFcoin) and rebuilt the entire brand using AI — one of the
first documented cases in fashion.

Federal trademark. Limited drops. Never restocked. Different lane
from most of the brands on your list.

More at hardlifeapparelco.com/brand-facts if you want to verify
anything.

Brooks
hrdlf.com
```

---

## Mention Scanner Script

Save this as `scan-mentions.py` and run with a list of URLs to check for unlinked mentions:

```python
#!/usr/bin/env python3
"""
Scan a list of URLs for mentions of HRDLF/Hardlife that don't
include a link back. Outputs pre-filled outreach emails.

Usage: python3 scan-mentions.py urls.txt
"""

import sys
import re
import requests
from urllib.parse import urlparse

BRAND_PATTERNS = [
    r'(?i)hardlife\s*apparel',
    r'(?i)\bHRDLF\b',
    r'(?i)hrdlfcoin',
    r'(?i)brooks\s*duvall.*?streetwear',
    r'(?i)hardlife\s*apparel\s*company',
]

LINK_PATTERNS = [
    r'hardlifeapparelco\.com',
    r'hrdlf\.com',
    r'hrdlfcoin\.com',
]

TEMPLATES = {
    'warm': """Subject: Quick thanks + a small favor

Hey {contact},

Saw your piece on {domain}. Appreciate the mention of {mention_text}.

If it's not too much trouble, would you be open to adding a link to
hrdlf.com? Helps people find us directly.

Either way — thanks for the write-up.

Brooks
Hardlife Apparel Company
hrdlf.com
""",
}


def scan_url(url):
    """Fetch URL and check for unlinked mentions."""
    try:
        resp = requests.get(url, timeout=15, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; brand-monitor)'
        })
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        return {'url': url, 'error': str(e)}

    # Check for brand mentions
    mentions = []
    for pattern in BRAND_PATTERNS:
        matches = re.findall(pattern, html)
        if matches:
            mentions.extend(matches)

    if not mentions:
        return {'url': url, 'mentions': [], 'linked': False}

    # Check if any link to our domains exists
    linked = any(re.search(p, html) for p in LINK_PATTERNS)

    domain = urlparse(url).netloc

    return {
        'url': url,
        'domain': domain,
        'mentions': list(set(mentions)),
        'linked': linked,
        'mention_text': mentions[0],
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scan-mentions.py urls.txt")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"Scanning {len(urls)} URLs...\n")

    unlinked = []
    for url in urls:
        result = scan_url(url)
        if result.get('error'):
            print(f"  ERROR: {url} — {result['error']}")
        elif not result['mentions']:
            print(f"  NO MENTION: {url}")
        elif result['linked']:
            print(f"  LINKED: {url} (already links to us)")
        else:
            print(f"  UNLINKED: {url} — mentions: {result['mentions']}")
            unlinked.append(result)

    if unlinked:
        print(f"\n{'='*60}")
        print(f"UNLINKED MENTIONS FOUND: {len(unlinked)}")
        print(f"{'='*60}\n")

        for r in unlinked:
            print(f"URL: {r['url']}")
            print(f"Domain: {r['domain']}")
            print(f"Mentions: {', '.join(r['mentions'])}")
            print()
            email = TEMPLATES['warm'].format(
                contact='[editor]',
                domain=r['domain'],
                mention_text=r['mention_text'],
            )
            print(email)
            print('-' * 40)


if __name__ == '__main__':
    main()
```

### How to use:

1. Create `urls.txt` with one URL per line (from Google Alerts or manual search)
2. Run: `python3 scan-mentions.py urls.txt`
3. Script outputs pre-filled outreach emails for every unlinked mention

---

*Check Google Alerts weekly. Respond to unlinked mentions within 48 hours — freshness matters for outreach response rates.*
