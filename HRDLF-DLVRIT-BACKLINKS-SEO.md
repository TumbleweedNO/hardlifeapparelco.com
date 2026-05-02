# HRDLF — dlvr.it Setup + Backlink Strategy + SEO Fixes
### Compiled: March 24, 2026

---

## PART 1 — dlvr.it SETUP

### Status: MANUAL SETUP REQUIRED
dlvr.it dashboard configuration cannot be automated. Follow these exact steps.

### Step 1: Create Feed Source
1. Log into dlvr.it
2. Go to **Sources → Add Source**
3. Feed URL: `https://hardlifeapparelco.com/feed`
4. Check interval: **Every 30 minutes**
5. Enable: Post title, post excerpt, featured image, link to article

### Step 2: Connect Social Destinations

| Platform | Account | Post Format |
|----------|---------|-------------|
| **X/Twitter** | @HardLifeApparel | Title + 150 chars excerpt + direct URL + featured image |
| **Facebook** | Hardlife Apparel Co. Page | Title + 150 chars excerpt + direct URL + featured image |
| **Instagram** | @hardlifeapparelco | Title + 150 chars excerpt + "Link in bio → hardlifeapparelco.com" + featured image |
| **Threads** | via Instagram connection | Title + 150 chars excerpt + "Link in bio → hardlifeapparelco.com" |
| **TikTok** | @hardlifeapparelco (if active) | Title + 150 chars excerpt + featured image |

### Step 3: Posting Rules Per Destination

**X/Twitter & Facebook:**
```
{title}

{excerpt:150}

{url}
```

**Instagram & Threads:**
```
{title}

{excerpt:150}

Link in bio → hardlifeapparelco.com

#HRDLF #Streetwear #Philadelphia #SkateStyle
```

### Step 4: Test
1. Publish a test post on hardlifeapparelco.com
2. Wait 30 minutes (or trigger manual check in dlvr.it)
3. Confirm distribution to all connected platforms
4. Verify featured image renders on each platform

### Step 5: Disable Zapier Buffer Step
Once dlvr.it is confirmed working:
1. Go to Zapier → Zaps → "HRDLF Blog → Social Auto-Post"
2. Disable or delete the Buffer step
3. This eliminates the duplicate posting conflict that was causing X/Twitter failures

---

## PART 2 — BACKLINK STRATEGY

### Current State
- **Google Search Console:** 7 pages indexed, avg position 10.8, zero external backlinks
- **Top query:** "hardlife clothing" — getting impressions but low CTR
- **Problem:** No external sites link to hardlifeapparelco.com

---

### TIER 1 — QUICK WINS (Done or Ready)

| Action | Status | Details |
|--------|--------|---------|
| Beehiiv newsletter backlinks | **NEEDS FIX** | Only 1 issue exists ("The coin wasn't the idea") — has ZERO links to hardlifeapparelco.com. Edit in Beehiiv to add links to at least 2 articles. |
| hrdlf.com → hardlifeapparelco.com cross-link | **NEEDS FIX** | Fourthwall store has NO cross-links to brand site. Follow guide at `hrdlf-com-fourthwall-seo-guide.md` — add header nav + footer links. |
| hrdlfcoin.com → hardlifeapparelco.com | **DONE** | 15+ cross-links already in place across nav, footer, announcement bar, and content sections. |
| Social profile website links | **VERIFY MANUALLY** | Check Instagram, X, TikTok, Facebook bios for hardlifeapparelco.com link. Also verify correct handle: @hardlifeapparelco vs @hardlifeapparel (inconsistency found in codebase). |

### TIER 2 — OUTREACH (Emails Drafted, Ready to Send)

All outreach emails saved to `~/hardlifeapparelco.com/backlink-outreach/`

#### Skate Media (10 Targets)
| # | Target | Contact | Priority | File |
|---|--------|---------|----------|------|
| 1 | **Skate Jawn** (Philly) | skatejawn@gmail.com | HIGHEST | `01-skate-jawn-philly.md` |
| 2 | **Jenkem Magazine** | info@jenkemmag.com | HIGH | `02-jenkem-magazine.md` |
| 3 | **Quartersnacks** | info@quartersnacks.com | HIGH | `03-quartersnacks.md` |
| 4 | The Berrics | Contact form + @theberrics DMs | MEDIUM | `08-general-skate-media.md` |
| 5 | Transworld Skateboarding | Editorial contact form | MEDIUM | `08-general-skate-media.md` |
| 6 | Free Skate Mag | info@freeskatemag.com | MEDIUM | `08-general-skate-media.md` |
| 7 | Pushing Boarders | info@pushingboarders.com | MEDIUM | `08-general-skate-media.md` |
| 8 | Slam City Skates Blog | Website contact form | LOW | `08-general-skate-media.md` |
| 9 | Hypebeast | tips@hypebeast.com | TIER 3 | `08-general-skate-media.md` |
| 10 | Highsnobiety | tips@highsnobiety.com | TIER 3 | `08-general-skate-media.md` |

#### Philadelphia Press (7 Targets)
| # | Target | Contact | Priority | File |
|---|--------|---------|----------|------|
| 1 | **Billy Penn (WHYY)** | tips@billypenn.com | HIGH | `04-billy-penn-whyy.md` |
| 2 | **Philadelphia Inquirer** | business@inquirer.com | HIGH | `05-philadelphia-inquirer.md` |
| 3 | **Technical.ly Philly** | philly@technical.ly | HIGH | `06-technical-ly-philly.md` |
| 4 | **Philadelphia Magazine** | editors@phillymag.com | HIGH | `07-philadelphia-magazine.md` |
| 5 | Broad Street Review | editor@broadstreetreview.com | MEDIUM | `09-philly-press-template.md` |
| 6 | Philadelphia Weekly | editorial@philadelphiaweekly.com | MEDIUM | `09-philly-press-template.md` |
| 7 | PhillyVoice | tips@phillyvoice.com | MEDIUM | `09-philly-press-template.md` |

#### Community / Reddit Strategy
| Platform | Strategy | Rules |
|----------|----------|-------|
| **r/streetwearstartup** | START HERE — post brand story, engage with other brands | Self-promotion allowed |
| **r/philadelphia** | "AMA-style" post: "I started a streetwear brand in Philly in 2006" | Support local sentiment strong |
| **r/streetwear** | Build comment history for 2-4 weeks before any brand content | Strict self-promo rules |
| **r/skateboarding** | Only post skate content (clips of skaters wearing HRDLF gear) | No brand posts allowed |
| Discord | Join streetwear startup servers, share knowledge from 20 years | Relationship-building first |

#### Journalist Platforms (HARO Replacements)
HARO is dead (shut down 2024). Use these instead:
| Platform | URL | Status |
|----------|-----|--------|
| **Qwoted** | qwoted.com | ACTIVE — sign up as source |
| **Featured.com** (fka Terkel) | featured.com | ACTIVE |
| **Source of Sources** | sourceofsources.com | ACTIVE — HARO replacement |
| **Quoted** | quoted.press | ACTIVE |

**Keywords to monitor:** streetwear, independent fashion, Philadelphia business, cryptocurrency fashion, skateboarding culture, small business survival, brand longevity

### TIER 3 — ONGOING (90 days+)

- Respond to Qwoted/Featured/SOS queries daily (10 min/day)
- Reddit community participation (3-4 comments/week)
- Co-brand partner links — require each partner to link to hardlifeapparelco.com
- Monitor skate media for feature/collab opportunities weekly

### Recommended Send Order
1. **This week:** Skate Jawn + Billy Penn + sign up for Qwoted/Featured/SOS
2. **Week 2:** Jenkem + Quartersnacks + Technical.ly + r/streetwearstartup post
3. **Week 3:** Philadelphia Inquirer + Phillymag + begin Reddit engagement
4. **Week 4+:** Berrics/Transworld/Hypebeast (after landing 2-3 smaller features)

---

## PART 3 — CTR IMPROVEMENT (Title Tags + Meta Descriptions)

### Status: DEPLOYED — hrdlf-seo.php v2.0 live

All title tags and meta descriptions rewritten using `[Keyword] — [Differentiator] | HRDLF` formula.

| Page | Old Title | New Title |
|------|-----------|-----------|
| Homepage | HRDLF — Philadelphia Independent Streetwear Since 2006 | *(unchanged — already optimized)* |
| About | About – HRDLF | **About Hardlife Apparel Co. — Independent Since 2006 \| HRDLF** |
| Drops | Drops – HRDLF | **Drops — Limited Streetwear Releases, Never Restocked \| HRDLF** |
| Archive | The Archive – HRDLF | **The Archive — HRDLF Brand Timeline & Founding Members** |
| Hardwired Weekly | Hardwired Weekly – HRDLF | **Hardwired Weekly — Free Streetwear Newsletter Every Thursday \| HRDLF** |
| Inner Circle | Inner Circle – HRDLF | **Inner Circle — Exclusive Streetwear Membership Tiers \| HRDLF** |
| Long Way Back | The Long Way Back – HRDLF | **The Long Way Back — HRDLF Documentary Series \| 6 Episodes** |
| Shop | Shop – HRDLF | **Shop HRDLF — Premium Streetwear, Limited Runs, Never Restocked** |
| Collabs | Collaborations – HRDLF | **Collaborations — HRDLF x Philadelphia Artists & Underground Brands** |
| Loyalty | Loyalty Program – HRDLF | **Loyalty Program — Earn Real Rewards for Staying Subscribed \| HRDLF** |
| Advertise | Advertise – HRDLF | **Advertise With HRDLF — Reach Streetwear Buyers & Skate Culture** |
| Blog posts | [Title] – HRDLF | **[Title] \| HRDLF** *(pipe separator, cleaner)* |

### New Meta Descriptions (all under 155 chars, hook + CTA)
| Page | Meta Description |
|------|-----------------|
| Homepage | Philadelphia independent streetwear brand est. 2006. 19 years of grit, skate culture roots, and zero outside investors... |
| About | Philadelphia streetwear brand built on skate culture, zero investors, and 19 years of showing up. The origin story of HRDLF. |
| Drops | HRDLF drops every first Thursday. Limited quantities. Never restocked. Subscribers get 48hr early access. |
| Archive | The permanent record of every collection, founding member, and coin holder since 2006. Your name. Permanently. |
| Hardwired Weekly | Drop access, brand updates, and the story behind HRDLF. Free every Thursday. Subscribers get 48hr early access. |
| Inner Circle | Three tiers of HRDLF membership. Early drops, exclusive colorways, physical rewards, and your name in The Archive. |
| Long Way Back | 19 years, no investors, Philadelphia. The documentary series about Hardlife Apparel Co. Subscribers see episodes 30 days early. |
| Shop | Claim HRDLF limited drops. Every piece is a numbered run. Once it's gone, it's gone forever. |
| Collabs | HRDLF collaborates with Philly artists, underground skate brands, and Web3 projects. Limited co-branded drops. |
| Loyalty | Stay subscribed to Hardwired Weekly and earn physical rewards. 6 months: patch. 12 months: Archive listing. |
| Advertise | Reach independent streetwear buyers and HRDLFcoin holders through Hardwired Weekly. Lead Sponsor from $750/issue. |

### Google Search Console Re-Index
After title tags update, request re-indexing for these URLs:
```
https://hardlifeapparelco.com/
https://hardlifeapparelco.com/about/
https://hardlifeapparelco.com/drops/
https://hardlifeapparelco.com/archive/
https://hardlifeapparelco.com/hardwired-weekly/
https://hardlifeapparelco.com/inner-circle/
https://hardlifeapparelco.com/the-long-way-back/
https://hardlifeapparelco.com/products/
https://hardlifeapparelco.com/collabs/
https://hardlifeapparelco.com/loyalty/
https://hardlifeapparelco.com/advertise/
```
**Manual step:** Go to Google Search Console → URL Inspection → paste each URL → Request Indexing

---

## PART 4 — INTERNAL LINKING AUDIT

### Status: DEPLOYED — 6 posts fixed

Added "Keep Reading" sections with 3 internal links each to all posts that were missing them.

| Post | Before | After |
|------|--------|-------|
| Philadelphia's Streetwear Scene | 0 links | 3 links |
| Old English Typography | 0 links | 3 links |
| Streetwear vs. Fast Fashion | 0 links | 3 links |
| 10 Underground Brands | 1 link | 4 links |
| The Origin Story | 0 links | 3 links |
| Hardwired Weekly: The Coin | 0 links | 3 links |

The 8 newer blog posts (March 17+) already had 8-10 internal links each — no changes needed.

### Schema.org Updates (v2.0)
- Added `hrdlfcoin.com` to `sameAs` array
- Added Instagram and X/Twitter social profiles to `sameAs`
- Version bump from 1.2 → 2.0

---

## CROSS-LINK AUDIT SUMMARY

| Property | Links to hardlifeapparelco.com | Status |
|----------|-------------------------------|--------|
| **hrdlfcoin.com** | 15+ links (nav, footer, content, schema) | EXCELLENT |
| **hrdlf.com** (Fourthwall) | 0 links | **NEEDS FIX — follow Fourthwall SEO guide** |
| **Beehiiv newsletter** | 0 links in 1 published issue | **NEEDS FIX — add links when editing** |
| **hardlifeapparelco.com** | Links to hrdlf.com (nav, footer) + hrdlfcoin.com (footer) | GOOD |

### Instagram Handle Inconsistency Found
Two different handles used across properties:
- `@hardlifeapparelco` — used on older site versions
- `@hardlifeapparel` — used on current deployed site + hrdlfcoin.com

**Action:** Verify which is the correct/active Instagram account and fix all references.

---

## DONE vs. MANUAL ACTION ITEMS

### DONE (Programmatic)
- [x] Title tags rewritten for all 11 pages — **deployed** (hrdlf-seo.php v2.0)
- [x] Meta descriptions rewritten for all 11 pages — **deployed**
- [x] Schema.org updated with social profiles — **deployed**
- [x] Internal links added to 6 blog posts — **deployed** (hrdlf-internal-links.php)
- [x] 9 outreach emails drafted — saved to `backlink-outreach/`
- [x] Backlink targets researched (10 skate + 7 press + communities)
- [x] Cross-link audit completed across all properties
- [x] Beehiiv newsletter audit completed
- [x] Internal linking audit completed

### MANUAL ACTION REQUIRED
- [ ] **dlvr.it setup** — log in, create feed, connect 5 platforms, test post
- [ ] **Disable Zapier Buffer step** — after dlvr.it is confirmed working
- [ ] **hrdlf.com Fourthwall cross-links** — add nav + footer links to hardlifeapparelco.com
- [ ] **Beehiiv issue edit** — add hardlifeapparelco.com links to "The coin wasn't the idea" issue
- [ ] **Verify Instagram handle** — @hardlifeapparelco or @hardlifeapparel?
- [ ] **Social profile bios** — ensure hardlifeapparelco.com is the website URL on all platforms
- [ ] **Send outreach emails** — start with Skate Jawn + Billy Penn this week
- [ ] **Sign up for Qwoted, Featured.com, Source of Sources** — journalist response platforms
- [ ] **Google Search Console re-indexing** — request re-index for all 11 pages
- [ ] **r/streetwearstartup post** — brand story / 20 years post
- [ ] **r/philadelphia AMA** — "I started a streetwear brand in Philly in 2006 — AMA"

---

## FILES CREATED/MODIFIED

| File | Action |
|------|--------|
| `/htdocs/wp-content/mu-plugins/hrdlf-seo.php` | Updated v1.2 → v2.0 (title tags + meta rewrites) |
| `/htdocs/wp-content/mu-plugins/hrdlf-internal-links.php` | New — one-shot internal link injection |
| `~/hardlifeapparelco.com/backlink-outreach/01-skate-jawn-philly.md` | Outreach email |
| `~/hardlifeapparelco.com/backlink-outreach/02-jenkem-magazine.md` | Outreach email |
| `~/hardlifeapparelco.com/backlink-outreach/03-quartersnacks.md` | Outreach email |
| `~/hardlifeapparelco.com/backlink-outreach/04-billy-penn-whyy.md` | Outreach email |
| `~/hardlifeapparelco.com/backlink-outreach/05-philadelphia-inquirer.md` | Outreach email |
| `~/hardlifeapparelco.com/backlink-outreach/06-technical-ly-philly.md` | Outreach email |
| `~/hardlifeapparelco.com/backlink-outreach/07-philadelphia-magazine.md` | Outreach email |
| `~/hardlifeapparelco.com/backlink-outreach/08-general-skate-media.md` | Template for 7 targets |
| `~/hardlifeapparelco.com/backlink-outreach/09-philly-press-template.md` | Template for 3 targets |
| `~/hardlifeapparelco.com/HRDLF-DLVRIT-BACKLINKS-SEO.md` | This document |
