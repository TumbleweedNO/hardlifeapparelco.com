#!/bin/bash
# HARDWIRED WEEKLY — Auto-Draft Generator (NYT Editorial Layout)
# Run every Monday: ./hardwired-weekly-generator.sh
# Or tell Claude Code: "generate this week's Hardwired Weekly"
#
# 1. Pulls last 7 days of posts from hardlifeapparelco.com
# 2. Selects top 3 articles
# 3. Generates NYT-style newsletter HTML
# 4. Saves to ~/hardlifeapparelco.com/hardwired-weekly-drafts/
#
# After running: paste HTML into Beehiiv code editor, review, send Thursday

DRAFT_DIR="$HOME/hardlifeapparelco.com/hardwired-weekly-drafts"
mkdir -p "$DRAFT_DIR"

echo "=== HARDWIRED WEEKLY — DRAFT GENERATOR ==="

python3 << 'PYEOF'
import json, sys, os, datetime, urllib.request

draft_dir = os.path.expanduser('~/hardlifeapparelco.com/hardwired-weekly-drafts')
os.makedirs(draft_dir, exist_ok=True)

existing = [f for f in os.listdir(draft_dir) if f.startswith('issue-') and f.endswith('.html')]
issue_num = len(existing) + 2

today = datetime.date.today()
thursday = today + datetime.timedelta(days=(3 - today.weekday()) % 7)
issue_date = thursday.strftime("%B %d, %Y")
issue_date_short = thursday.strftime("%b. %d, %Y")

# Pull posts from last 7 days
week_ago = (today - datetime.timedelta(days=7)).isoformat()
url = f"https://hardlifeapparelco.com/wp-json/wp/v2/posts?per_page=10&orderby=date&order=desc&after={week_ago}T00:00:00&_fields=title,link,date,excerpt"
resp = urllib.request.urlopen(urllib.request.Request(url))
posts = json.loads(resp.read())

articles = [p for p in posts if 'hardwired' not in p['title']['rendered'].lower()][:3]

if not articles:
    print("WARNING: No new articles found in the last 7 days!")
    sys.exit(1)

# Build article blocks — NYT style
article_blocks = ""
for i, art in enumerate(articles):
    title = art['title']['rendered'].replace('&#8217;', "'").replace('&#8211;', "\u2013").replace('&amp;', '&')
    excerpt = art['excerpt']['rendered'].replace('<p>', '').replace('</p>', '').replace('\n', '').strip()
    link = art['link']
    pub_date = datetime.datetime.fromisoformat(art['date']).strftime("%B %d, %Y")

    border_top = 'border-top: 1px solid #e2e2e2; padding-top: 24px;' if i > 0 else ''

    article_blocks += f"""
<div style="margin-bottom: 28px; {border_top}">
  <p style="font-family: Georgia, 'Times New Roman', serif; font-size: 11px; color: #999; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 6px 0;">{pub_date}</p>
  <h2 style="font-family: Georgia, 'Times New Roman', serif; font-size: 22px; font-weight: 700; line-height: 1.3; margin: 0 0 10px 0; color: #1a1a1a;"><a href="{link}" style="color: #1a1a1a; text-decoration: none;">{title}</a></h2>
  <p style="font-family: Georgia, 'Times New Roman', serif; font-size: 15px; line-height: 1.7; color: #555; margin: 0 0 12px 0;">{excerpt}</p>
  <a href="{link}" style="font-family: -apple-system, Arial, sans-serif; font-size: 12px; font-weight: 600; color: #CC0000; text-decoration: none; letter-spacing: 0.3px;">Continue Reading &#8594;</a>
</div>
"""

subjects = [
    f"{articles[0]['title']['rendered'].replace(chr(8217), chr(39)).replace('&#8217;', chr(39))}",
    f"Hardwired Weekly: {len(articles)} stories this week",
    f"Issue {issue_num:02d} — From the desk of Brooks Duvall"
]

html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin: 0; padding: 0; background: #f9f9f9;">

<div style="max-width: 620px; margin: 0 auto; background: #ffffff; font-family: Georgia, 'Times New Roman', serif;">

  <!-- Masthead -->
  <div style="text-align: center; padding: 40px 32px 0 32px;">
    <p style="font-family: -apple-system, Arial, sans-serif; font-size: 10px; letter-spacing: 3px; text-transform: uppercase; color: #999; margin: 0 0 12px 0;">The Streetwear Intelligence Brief</p>
    <h1 style="font-family: Georgia, 'Times New Roman', serif; font-size: 36px; font-weight: 700; letter-spacing: -0.5px; margin: 0; color: #1a1a1a;">Hardwired Weekly</h1>
    <div style="width: 100%; height: 1px; background: #1a1a1a; margin: 16px 0 4px 0;"></div>
    <div style="display: flex; justify-content: space-between; align-items: center; font-family: -apple-system, Arial, sans-serif; font-size: 11px; color: #999;">
      <span>Issue {issue_num:02d}</span>
      <span>{issue_date}</span>
      <span>Brooks Duvall</span>
    </div>
    <div style="width: 100%; height: 2px; background: #1a1a1a; margin: 4px 0 0 0;"></div>
  </div>

  <!-- Editor's Note -->
  <div style="padding: 32px 32px 0 32px;">
    <p style="font-family: -apple-system, Arial, sans-serif; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; color: #CC0000; margin: 0 0 12px 0;">From the Founder</p>
    <p style="font-family: Georgia, 'Times New Roman', serif; font-size: 16px; line-height: 1.8; color: #333; margin: 0 0 8px 0;">[BROOKS \u2014 Write your opening here. 2-3 sentences. What happened this week. What matters. Keep it direct.]</p>
    <p style="font-family: Georgia, 'Times New Roman', serif; font-size: 14px; color: #999; font-style: italic; margin: 16px 0 0 0;">\u2014 Brooks Duvall, Philadelphia, 2006</p>
  </div>

  <!-- Divider -->
  <div style="padding: 24px 32px;">
    <div style="width: 100%; height: 1px; background: #e2e2e2;"></div>
  </div>

  <!-- This Week's Stories -->
  <div style="padding: 0 32px;">
    <p style="font-family: -apple-system, Arial, sans-serif; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; color: #CC0000; margin: 0 0 20px 0;">This Week</p>
    {article_blocks}
  </div>

  <!-- Drop Alert -->
  <div style="margin: 16px 32px 0 32px; background: #fafaf5; border: 1px solid #e8e5d8; padding: 24px;">
    <p style="font-family: -apple-system, Arial, sans-serif; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; color: #8B7355; margin: 0 0 8px 0;">Upcoming Release</p>
    <h3 style="font-family: Georgia, 'Times New Roman', serif; font-size: 20px; font-weight: 700; color: #1a1a1a; margin: 0 0 8px 0;">Graffiti Beach Collection \u2014 April 2</h3>
    <p style="font-family: Georgia, 'Times New Roman', serif; font-size: 14px; line-height: 1.7; color: #555; margin: 0 0 16px 0;">Venice Beach, 1985. Rainbow gradient graffiti graphic on heavyweight zip-ups. Limited run. Never restocked. Hardwired Weekly subscribers get 48-hour early access before public release.</p>
    <a href="https://hrdlf.com" style="font-family: -apple-system, Arial, sans-serif; font-size: 12px; font-weight: 600; color: #1a1a1a; text-decoration: none; border-bottom: 1px solid #1a1a1a; padding-bottom: 2px;">Shop the Collection &#8594;</a>
  </div>

  <!-- Ecosystem Footer -->
  <div style="padding: 32px 32px 0 32px;">
    <div style="width: 100%; height: 1px; background: #e2e2e2; margin-bottom: 24px;"></div>
    <p style="font-family: -apple-system, Arial, sans-serif; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; color: #999; margin: 0 0 12px 0;">The Ecosystem</p>
    <p style="font-family: Georgia, 'Times New Roman', serif; font-size: 13px; line-height: 2; color: #666;">
      <a href="https://hardlifeapparelco.com" style="color: #333; text-decoration: none; border-bottom: 1px solid #ddd;">hardlifeapparelco.com</a> \u2014 Editorial &amp; Culture<br>
      <a href="https://hrdlf.com" style="color: #333; text-decoration: none; border-bottom: 1px solid #ddd;">hrdlf.com</a> \u2014 Shop Limited Drops<br>
      <a href="https://hrdlfcoin.com" style="color: #333; text-decoration: none; border-bottom: 1px solid #ddd;">hrdlfcoin.com</a> \u2014 Own a Piece of the Brand<br>
      <a href="https://instagram.com/hardlifeapparelco" style="color: #333; text-decoration: none; border-bottom: 1px solid #ddd;">@hardlifeapparelco</a> \u2014 Instagram
    </p>
  </div>

  <!-- Colophon -->
  <div style="text-align: center; padding: 32px; border-top: 2px solid #1a1a1a; margin: 24px 32px 0 32px;">
    <p style="font-family: Georgia, 'Times New Roman', serif; font-size: 12px; color: #999; line-height: 1.6;">Hardlife Apparel Company LTD.<br>Philadelphia, Est. 2006<br><em>Nothing Awesome Comes Easy.</em></p>
  </div>

</div>

</body>
</html>"""

# Save
filename = f"issue-{issue_num:02d}-{today.isoformat()}.html"
filepath = os.path.join(draft_dir, filename)
with open(filepath, 'w') as f:
    f.write(html)

meta_path = os.path.join(draft_dir, f"issue-{issue_num:02d}-meta.txt")
with open(meta_path, 'w') as f:
    f.write(f"HARDWIRED WEEKLY — Issue {issue_num:02d}\n")
    f.write(f"Send date: Thursday, {issue_date}\n")
    f.write(f"Generated: {today.isoformat()}\n\n")
    f.write("SUBJECT LINE OPTIONS:\n")
    for i, s in enumerate(subjects, 1):
        f.write(f"  {i}. {s}\n")
    f.write(f"\nPREVIEW TEXT: This week's editorial from the desk of Brooks Duvall.\n")
    f.write(f"\nARTICLES INCLUDED:\n")
    for art in articles:
        f.write(f"  - {art['title']['rendered']}  ({art['link']})\n")
    f.write(f"\nCROSS-LINKS: hardlifeapparelco.com, hrdlf.com, hrdlfcoin.com, instagram.com/hardlifeapparelco\n")
    f.write(f"\nSTATUS: Ready for review — approve or edit before Thursday send\n")
    f.write(f"\nWORKFLOW:\n")
    f.write(f"  1. Open Beehiiv dashboard -> Create new post\n")
    f.write(f"  2. Switch to HTML/code editor view\n")
    f.write(f"  3. Paste the HTML from {filename}\n")
    f.write(f"  4. Fill in the [BROOKS] opening hook section\n")
    f.write(f"  5. Set subject line (pick from options above)\n")
    f.write(f"  6. Set preview text\n")
    f.write(f"  7. Preview, then schedule for Thursday\n")

print(f"\n  Draft saved: {filepath}")
print(f"  Meta saved:  {meta_path}")
print(f"\n  Subject line options:")
for i, s in enumerate(subjects, 1):
    print(f"    {i}. {s}")
print(f"\n  Articles: {len(articles)}")
for art in articles:
    print(f"    - {art['title']['rendered']}")
print(f"\n  STATUS: Ready for review. Paste into Beehiiv, add your opening hook, send Thursday.")

PYEOF
