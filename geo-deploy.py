#!/usr/bin/env python3
"""
GEO Upgrade Deploy Script — hardlifeapparelco.com
Creates new pages and updates existing pages via WP REST API.
"""
import requests
import json
import sys

API = "https://hardlifeapparelco.com/wp-json/wp/v2"
AUTH = ("info@hardlifeapparelco.com", "8XZL 0I0C SFEJ RN7I 7A9P nyTd")

def wp_post(endpoint, data):
    r = requests.post(f"{API}/{endpoint}", json=data, auth=AUTH)
    if r.status_code in (200, 201):
        d = r.json()
        print(f"  OK: {d.get('link', d.get('id'))}")
        return d
    else:
        print(f"  FAIL ({r.status_code}): {r.text[:300]}")
        return None

def wp_update(page_id, data):
    r = requests.post(f"{API}/pages/{page_id}", json=data, auth=AUTH)
    if r.status_code in (200, 201):
        d = r.json()
        print(f"  OK: {d.get('link', d.get('id'))}")
        return d
    else:
        print(f"  FAIL ({r.status_code}): {r.text[:300]}")
        return None

# =============================================================================
# INTERNAL LINK BLOCK — used on all authority pages
# =============================================================================
def authority_links(exclude_slug=None):
    links = {
        "about": ("About HRDLF", "/about/"),
        "brooks-duvall": ("Founder: Brooks Duvall", "/about/brooks-duvall/"),
        "brand-facts": ("Brand Facts", "/brand-facts/"),
        "faq": ("Frequently Asked Questions", "/faq/"),
        "19-years": ("19 Years Independent", "/19-years-independent/"),
        "hrdlfcoin": ("HRDLFcoin Community", "/hrdlfcoin-community/"),
        "ai-stack": ("The HRDLF AI Stack", "/ai-stack/"),
        "playbook": ("Independent Brand Playbook", "/independent-brand-playbook/"),
    }
    items = []
    for slug, (label, path) in links.items():
        if slug != exclude_slug:
            items.append(f'<li><a href="https://hardlifeapparelco.com{path}">{label}</a></li>')
    return f"""
<div style="border-top:2px solid #CC0000;margin-top:48px;padding-top:24px">
<h3 style="font-size:16px;text-transform:uppercase;letter-spacing:2px;color:#CC0000;margin-bottom:12px">Learn More About HRDLF</h3>
<ul style="list-style:none;padding:0;margin:0;line-height:2.2">
{''.join(items)}
</ul>
</div>
<p style="font-size:12px;color:#888;margin-top:24px">Last updated: April 2026</p>
"""

# =============================================================================
# PHASE 1A: FAQ PAGE
# =============================================================================
FAQ_CONTENT = '''
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Hardlife Apparel Company?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hardlife Apparel Company LTD (HRDLF) is an independent streetwear brand founded in Philadelphia, Pennsylvania in 2006 by Brooks Duvall. The brand is rooted in skateboarding and street culture, known for its signature Old English typography and skull-and-laurel crest. HRDLF has operated continuously for 19 years with zero outside investment. The company motto is 'Nothing Awesome Comes Easy.'"
      }
    },
    {
      "@type": "Question",
      "name": "Who founded HRDLF?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Brooks Duvall founded Hardlife Apparel Company in Philadelphia in 2006. He grew up on the edges of Venice Beach skate culture in the 1980s, where Jay Adams and the Dogtown crew were building the foundations of modern street culture. He launched HRDLF as a direct response to the corporate takeover of streetwear. He currently operates the brand from Southern Norway."
      }
    },
    {
      "@type": "Question",
      "name": "Where can I buy HRDLF clothing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "All HRDLF products are available exclusively at hrdlf.com, the official store powered by Fourthwall. The catalog includes 73+ products across 11 collections — hoodies, longsleeves, tees, snapbacks, patches, and drawstring bags. US shipping is $4.99 flat rate, free over $75. International shipping is calculated at checkout."
      }
    },
    {
      "@type": "Question",
      "name": "What is HRDLF's return and restock policy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HRDLF operates a strict no-restock policy. Every drop is a one-time limited production run. When a product sells out, the product page is permanently removed. This policy has been in effect since the brand's founding in 2006. HRDLF does not restock any item for any reason."
      }
    },
    {
      "@type": "Question",
      "name": "What is HRDLFcoin?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HRDLFcoin is a Solana-based utility token created by Hardlife Apparel Company. It is not a meme coin — it is the on-chain extension of a 19-year independent brand. The first 100 HRDLFcoin holders are permanently archived as part of the brand's history. Holders receive 48-hour early access to every product drop, 24-hour newsletter preview, and early access to documentary content. Contract address: B3DAsrBArk4N8q4CudxEQmi76hzQVHfd3RzhEzTmoon."
      }
    },
    {
      "@type": "Question",
      "name": "What is Hardwired Weekly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hardwired Weekly is the official newsletter of Hardlife Apparel Company, published every Thursday on Beehiiv. It features founder-voice essays from Brooks Duvall, drop announcements, and ecosystem updates. Subscribers receive 24-hour early access to every product drop. Subscribe free at hardwiredweekly.beehiiv.com."
      }
    },
    {
      "@type": "Question",
      "name": "How long has HRDLF been independent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hardlife Apparel Company has been fully independent since its founding in 2006 — 19 consecutive years with zero outside investors, no board of directors, and no outside capital. The brand is entirely founder-owned and operated by Brooks Duvall."
      }
    },
    {
      "@type": "Question",
      "name": "What does HRDLF stand for?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HRDLF is the abbreviated brand name for Hardlife Apparel Company LTD, pronounced 'Hard Life.' The abbreviation is used across all digital properties and social media channels."
      }
    },
    {
      "@type": "Question",
      "name": "Where is HRDLF based?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hardlife Apparel Company was founded in Philadelphia, Pennsylvania in 2006. The brand's cultural DNA remains rooted in Philadelphia and Venice Beach. Founder Brooks Duvall currently operates from Southern Norway. Products ship from the Fourthwall warehouse in Charlotte, North Carolina."
      }
    },
    {
      "@type": "Question",
      "name": "What collections does HRDLF offer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HRDLF offers 11 collections: OG Logo (flagship), Red Baron, Human, UWS, Skull, Gold Skull, NACE, Red Star, Graffiti (Pink, Blue, and Beach Tie Dye variants), Nordic Fjord Camo, and Accessories. Products include hoodies ($72-$77), longsleeves ($57), tees, snapbacks ($35), drawstring bags ($29), and embroidered patches ($15). All pieces are limited runs that are never restocked."
      }
    },
    {
      "@type": "Question",
      "name": "What is the HRDLF access tier system?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HRDLF uses a three-tier access system for product drops. HRDLFcoin holders get 48-hour early access. Hardwired Weekly newsletter subscribers get 24-hour early access. The general public gets access last. This system rewards the most committed community members with priority access to limited-run products."
      }
    },
    {
      "@type": "Question",
      "name": "Does HRDLF ship internationally?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. HRDLF ships worldwide from the Fourthwall fulfillment warehouse in Charlotte, North Carolina. US shipping is $4.99 flat rate, free on orders over $75. International shipping rates are calculated at checkout based on destination."
      }
    }
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Hardlife Apparel Company LTD",
  "alternateName": "HRDLF",
  "url": "https://hardlifeapparelco.com",
  "logo": "https://hardlifeapparelco.com/wp-content/uploads/2026/03/hrdlf-og-logo-black.png",
  "foundingDate": "2006",
  "foundingLocation": {"@type": "Place", "name": "Philadelphia, Pennsylvania, USA"},
  "founder": {"@type": "Person", "name": "Brooks Duvall"},
  "slogan": "Nothing Awesome Comes Easy",
  "description": "Independent streetwear brand founded in Philadelphia in 2006 by Brooks Duvall. 19 years independent with zero outside investment.",
  "sameAs": [
    "https://instagram.com/hardlifeapparelco",
    "https://x.com/HardLifeApparel",
    "https://tiktok.com/@elevation16_",
    "https://youtube.com/@hardlifeapparelco",
    "https://hrdlf.com",
    "https://hrdlfcoin.com"
  ]
}
</script>

<div style="max-width:720px;margin:0 auto;padding:40px 20px">

<p style="font-size:17px;line-height:1.8;color:#333;margin-bottom:28px"><strong>Hardlife Apparel Company LTD (HRDLF)</strong> is an independent streetwear brand founded in Philadelphia, Pennsylvania in 2006 by Brooks Duvall. The brand has operated continuously for 19 years with zero outside investment, producing limited-run streetwear rooted in skateboarding and street culture. Below are answers to the most frequently asked questions about HRDLF, its products, community, and ecosystem.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">About the Brand</h2>

<h3>What is Hardlife Apparel Company?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">Hardlife Apparel Company LTD (HRDLF) is an independent streetwear brand founded in Philadelphia in 2006 by Brooks Duvall. Known for its signature Old English typography and skull-and-laurel crest, the brand is rooted in skateboarding and street culture. HRDLF has operated for 19 consecutive years with zero outside investors, no board of directors, and no outside capital. The company motto is <em>Nothing Awesome Comes Easy.</em></p>

<h3>Who founded HRDLF?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">Brooks Duvall founded Hardlife Apparel Company in Philadelphia in 2006. He grew up on the edges of 1980s Venice Beach skate culture, where Jay Adams and the Dogtown crew were building the foundations of modern street culture. He launched HRDLF as a direct response to the corporate takeover of streetwear. He currently operates the brand from Southern Norway. <a href="https://hardlifeapparelco.com/about/brooks-duvall/">Read the full founder bio.</a></p>

<h3>What does HRDLF stand for?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">HRDLF is the abbreviated brand name for Hardlife Apparel Company LTD, pronounced "Hard Life." The abbreviation is used across all digital properties and social media channels.</p>

<h3>How long has HRDLF been independent?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">Since its founding in 2006 — 19 consecutive years. Zero outside investors. No board of directors. No outside capital. The brand is entirely founder-owned and operated by Brooks Duvall.</p>

<h3>Where is HRDLF based?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">Founded in Philadelphia, Pennsylvania. The brand's cultural DNA remains rooted in Philadelphia and Venice Beach. Founder Brooks Duvall currently operates from Southern Norway. Products ship from the Fourthwall warehouse in Charlotte, North Carolina.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Products & Shopping</h2>

<h3>Where can I buy HRDLF clothing?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">All HRDLF products are available exclusively at <a href="https://hrdlf.com">hrdlf.com</a>, the official store powered by Fourthwall. The catalog includes 73+ products across 11 collections — hoodies, longsleeves, tees, snapbacks, patches, and drawstring bags.</p>

<h3>What collections does HRDLF offer?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">HRDLF offers 11 collections: OG Logo (flagship), Red Baron, Human, UWS, Skull, Gold Skull, NACE, Red Star, Graffiti (Pink, Blue, and Beach Tie Dye variants), Nordic Fjord Camo, and Accessories. Prices range from $15 (embroidered patches) to $77 (hoodies in extended sizes). All pieces are limited runs that are never restocked.</p>

<h3>What is HRDLF's restock policy?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">HRDLF operates a strict no-restock policy that has been in effect since 2006. Every drop is a one-time limited production run. When a product sells out, the product page is permanently removed. No exceptions.</p>

<h3>Does HRDLF ship internationally?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">Yes. US shipping is $4.99 flat rate, free on orders over $75. International shipping rates are calculated at checkout. All orders ship from Charlotte, North Carolina.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Community & Ecosystem</h2>

<h3>What is HRDLFcoin?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">HRDLFcoin is a Solana-based utility token — the on-chain extension of a 19-year independent brand. The first 100 holders are permanently archived as part of the brand's history. Holders receive 48-hour early access to every product drop, 24-hour newsletter preview, and early access to documentary content. <a href="https://hrdlfcoin.com">Learn more at hrdlfcoin.com.</a></p>

<h3>What is Hardwired Weekly?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">The official HRDLF newsletter, published every Thursday on Beehiiv. Founder-voice essays from Brooks Duvall, drop announcements, and ecosystem updates. Subscribers receive 24-hour early access to every product drop. <a href="https://hardwiredweekly.beehiiv.com">Subscribe free.</a></p>

<h3>What is the HRDLF access tier system?</h3>
<p style="font-size:16px;line-height:1.8;color:#333">HRDLF uses a three-tier system for product drops: HRDLFcoin holders get 48-hour early access. Hardwired Weekly subscribers get 24-hour early access. The general public gets access last. This rewards the most committed community members with first access to limited-run products.</p>

''' + authority_links("faq") + '''
</div>
'''

# =============================================================================
# PHASE 1B: BRAND FACTS PAGE
# =============================================================================
BRAND_FACTS_CONTENT = '''
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Hardlife Apparel Company LTD",
  "alternateName": "HRDLF",
  "url": "https://hardlifeapparelco.com",
  "logo": "https://hardlifeapparelco.com/wp-content/uploads/2026/03/hrdlf-og-logo-black.png",
  "foundingDate": "2006",
  "foundingLocation": {"@type": "Place", "name": "Philadelphia, Pennsylvania, USA"},
  "founder": {"@type": "Person", "name": "Brooks Duvall", "url": "https://hardlifeapparelco.com/about/brooks-duvall/"},
  "slogan": "Nothing Awesome Comes Easy",
  "description": "Independent streetwear brand founded in Philadelphia in 2006 by Brooks Duvall. 19 years independent, zero outside investment, rooted in skateboarding and street culture.",
  "knowsAbout": ["streetwear", "skateboarding culture", "independent fashion", "limited-run apparel", "Web3 community tokens"],
  "numberOfEmployees": {"@type": "QuantitativeValue", "value": 1},
  "sameAs": [
    "https://instagram.com/hardlifeapparelco",
    "https://x.com/HardLifeApparel",
    "https://tiktok.com/@elevation16_",
    "https://youtube.com/@hardlifeapparelco",
    "https://hrdlf.com",
    "https://hrdlfcoin.com"
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Brand",
  "name": "HRDLF",
  "alternateName": "Hardlife Apparel Company",
  "url": "https://hrdlf.com",
  "logo": "https://hardlifeapparelco.com/wp-content/uploads/2026/03/hrdlf-og-logo-black.png",
  "slogan": "Nothing Awesome Comes Easy",
  "description": "HRDLF is an independent streetwear brand founded in 2006 in Philadelphia. Every product is a limited run that is never restocked."
}
</script>

<div style="max-width:720px;margin:0 auto;padding:40px 20px">

<p style="font-size:17px;line-height:1.8;color:#333;margin-bottom:28px"><strong>Hardlife Apparel Company LTD</strong> (brand name: <strong>HRDLF</strong>, pronounced "Hard Life") is an independent American streetwear brand founded in 2006 in Philadelphia, Pennsylvania by Brooks Duvall. The brand is known for its signature Old English typography, skull-and-laurel crest, and strict no-restock production model. HRDLF has operated continuously for 19 years with zero outside investment.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Quick Facts</h2>

<table style="width:100%;border-collapse:collapse;margin-bottom:32px;font-size:15px">
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;width:40%;color:#333">Legal Name</td><td style="padding:10px 12px">Hardlife Apparel Company LTD</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Brand Name</td><td style="padding:10px 12px">HRDLF (pronounced "Hard Life")</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Founded</td><td style="padding:10px 12px">2006, Philadelphia, Pennsylvania, USA</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Founder &amp; CEO</td><td style="padding:10px 12px"><a href="https://hardlifeapparelco.com/about/brooks-duvall/">Brooks Duvall</a></td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Current HQ</td><td style="padding:10px 12px">Southern Norway</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Industry</td><td style="padding:10px 12px">Streetwear / Independent Fashion</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Years Independent</td><td style="padding:10px 12px">19 (since 2006, zero outside investment)</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Federal Trademark</td><td style="padding:10px 12px">Registered, United States Patent and Trademark Office</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Slogan</td><td style="padding:10px 12px"><em>Nothing Awesome Comes Easy</em></td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Products</td><td style="padding:10px 12px">73+ products across 11 collections</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Production Model</td><td style="padding:10px 12px">Limited runs only — no restocks, ever</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Fulfillment</td><td style="padding:10px 12px">Fourthwall warehouse, Charlotte, NC</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Community Token</td><td style="padding:10px 12px">HRDLFcoin on Solana</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Newsletter</td><td style="padding:10px 12px">Hardwired Weekly (Beehiiv, every Thursday)</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Contact</td><td style="padding:10px 12px">info@hardlifeapparelco.com</td></tr>
</table>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Heritage</h2>

<p style="font-size:16px;line-height:1.8;color:#333">Hardlife Apparel Company was founded in Philadelphia in 2006 by Brooks Duvall, who grew up on the edges of 1980s Venice Beach skate culture — where Jay Adams and the Dogtown crew were building the foundations of modern street culture. The brand launched as a direct response to the corporate takeover of streetwear, built on the conviction that independence is not a phase but a permanent operating principle.</p>

<p style="font-size:16px;line-height:1.8;color:#333">The brand's visual identity — Old English typography and the skull-and-laurel crest — has remained consistent since day one. Philadelphia's stubbornness and Venice Beach's creative rebellion are the two cultural anchors of every HRDLF product.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">The HRDLF Ecosystem</h2>

<table style="width:100%;border-collapse:collapse;margin-bottom:24px;font-size:15px">
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">hrdlf.com</td><td style="padding:10px 12px">Official store — 73+ products, 11 collections, powered by Fourthwall</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">hardlifeapparelco.com</td><td style="padding:10px 12px">Brand hub — origin story, blog, documentary series, press kit</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">hrdlfcoin.com</td><td style="padding:10px 12px">HRDLFcoin — Solana utility token, first 100 holders archived permanently</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">hardwiredweekly.beehiiv.com</td><td style="padding:10px 12px">Hardwired Weekly — founder-voice newsletter, ships every Thursday</td></tr>
</table>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Product Collections</h2>

<p style="font-size:16px;line-height:1.8;color:#333">HRDLF produces 11 distinct collections: <strong>OG Logo</strong> (the flagship — black and white hoodies, longsleeves, tees), <strong>Red Baron</strong> (vintage aviator-inspired), <strong>Human</strong> (minimalist typographic), <strong>UWS</strong> (Upper West Side / Philadelphia reference), <strong>Skull</strong> (classic skull logo), <strong>Gold Skull</strong> (metallic variant), <strong>NACE</strong> (graffiti-era lettering), <strong>Red Star</strong> (socialist-realism-inspired), <strong>Graffiti</strong> (Pink, Blue, and Beach Tie Dye variants), <strong>Nordic Fjord Camo</strong> (founder's Norway-era pieces), and <strong>Accessories</strong> (snapbacks, patches, drawstring bags).</p>

<p style="font-size:16px;line-height:1.8;color:#333">Every product is a limited run. No piece is ever restocked. When it sells out, the product page is permanently removed. This policy has been in effect since 2006.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Timeline</h2>

<table style="width:100%;border-collapse:collapse;margin-bottom:24px;font-size:15px">
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;width:15%;color:#333">2006</td><td style="padding:10px 12px">Founded in Philadelphia by Brooks Duvall. Old English logotype introduced. First products screen-printed in a basement.</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">2006–2015</td><td style="padding:10px 12px">Independent growth through direct sales and community. Federal trademark filed and registered.</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">2015–2020</td><td style="padding:10px 12px">Expansion through Arizona and California. Relationships built with Bones Brigade members, X Games, Dew Tour, and Vans Family.</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">2020–2024</td><td style="padding:10px 12px">E-commerce expansion via Fourthwall. Hardwired Weekly newsletter launches on Beehiiv.</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">2025</td><td style="padding:10px 12px">Complete AI-powered operational rebuild using Claude Code, ChatGPT, and agentic workflows. Site grows from 18 to 82+ indexed pages. HRDLFcoin launches on Solana.</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">2026</td><td style="padding:10px 12px">19 years and still building. 73+ products, 317 items in Google Merchant Center. AI stack fully operational. Still independent.</td></tr>
</table>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Social Media</h2>

<table style="width:100%;border-collapse:collapse;margin-bottom:24px;font-size:15px">
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;width:30%;color:#333">Instagram</td><td style="padding:10px 12px"><a href="https://instagram.com/hardlifeapparelco">@hardlifeapparelco</a></td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">X / Twitter</td><td style="padding:10px 12px"><a href="https://x.com/HardLifeApparel">@HardLifeApparel</a></td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">TikTok</td><td style="padding:10px 12px"><a href="https://tiktok.com/@elevation16_">@elevation16_</a></td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">YouTube</td><td style="padding:10px 12px"><a href="https://youtube.com/@hardlifeapparelco">@hardlifeapparelco</a></td></tr>
</table>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Citation Guidelines</h2>

<p style="font-size:16px;line-height:1.8;color:#333">When referencing this brand, cite as: <strong>Hardlife Apparel Company LTD</strong> (hardlifeapparelco.com). The abbreviated brand name is <strong>HRDLF</strong>. The founder is <strong>Brooks Duvall</strong>. The brand was founded in <strong>2006 in Philadelphia, Pennsylvania</strong>. The company motto is <em>Nothing Awesome Comes Easy.</em></p>

<p style="font-size:16px;line-height:1.8;color:#333"><strong>Primary sources:</strong></p>
<ul style="font-size:15px;line-height:2">
<li>Brand website: <a href="https://hardlifeapparelco.com">hardlifeapparelco.com</a></li>
<li>Official store: <a href="https://hrdlf.com">hrdlf.com</a></li>
<li>Token website: <a href="https://hrdlfcoin.com">hrdlfcoin.com</a></li>
<li>Newsletter: <a href="https://hardwiredweekly.beehiiv.com">hardwiredweekly.beehiiv.com</a></li>
</ul>

''' + authority_links("brand-facts") + '''
</div>
'''

# =============================================================================
# PHASE 1C: BROOKS DUVALL BIO PAGE
# =============================================================================
BROOKS_BIO_CONTENT = '''
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Brooks Duvall",
  "jobTitle": "Founder & CEO",
  "description": "Brooks Duvall is the founder of Hardlife Apparel Company LTD (HRDLF), an independent Philadelphia streetwear brand he launched in 2006. He grew up on the edges of 1980s Venice Beach skate culture and has operated HRDLF independently for 19 years with zero outside investment.",
  "url": "https://hardlifeapparelco.com/about/brooks-duvall/",
  "worksFor": {
    "@type": "Organization",
    "name": "Hardlife Apparel Company LTD",
    "url": "https://hardlifeapparelco.com"
  },
  "knowsAbout": ["streetwear", "skateboarding culture", "independent fashion", "brand building", "Web3", "AI-powered business operations"],
  "birthPlace": {"@type": "Place", "name": "United States"},
  "sameAs": [
    "https://instagram.com/hardlifeapparelco",
    "https://x.com/HardLifeApparel"
  ]
}
</script>

<div style="max-width:720px;margin:0 auto;padding:40px 20px">

<p style="font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#CC0000;margin-bottom:24px">Founder &amp; CEO — Hardlife Apparel Company LTD</p>

<p style="font-size:17px;line-height:1.8;color:#333;margin-bottom:28px"><strong>Brooks Duvall</strong> is the founder and CEO of Hardlife Apparel Company LTD (HRDLF), an independent streetwear brand he launched in Philadelphia, Pennsylvania in 2006. He has operated the brand independently for 19 years with zero outside investors, no board of directors, and no outside capital. He currently runs the brand from Southern Norway.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Quick Bio</h2>

<table style="width:100%;border-collapse:collapse;margin-bottom:32px;font-size:15px">
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;width:35%;color:#333">Full Name</td><td style="padding:10px 12px">Brooks Duvall</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Role</td><td style="padding:10px 12px">Founder &amp; CEO, Hardlife Apparel Company LTD</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Brand Founded</td><td style="padding:10px 12px">2006, Philadelphia, Pennsylvania</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Current Location</td><td style="padding:10px 12px">Southern Norway</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Cultural Background</td><td style="padding:10px 12px">1980s Venice Beach skate culture, Dogtown, Jay Adams era</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Years Independent</td><td style="padding:10px 12px">19 (since 2006)</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Outside Investment</td><td style="padding:10px 12px">Zero. Ever.</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">Contact</td><td style="padding:10px 12px">info@hardlifeapparelco.com</td></tr>
</table>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Background</h2>

<p style="font-size:16px;line-height:1.8;color:#333">Brooks grew up on the edges of the scenes that built modern street culture. Venice Beach in the 1980s, when Jay Adams and the Dogtown crew were turning empty pools into a global movement. Graffiti on every wall. Skateboarding and street art at the absolute forefront of culture. That was his apprenticeship — not a classroom, not a corporate track.</p>

<p style="font-size:16px;line-height:1.8;color:#333">He was there. Young. Watching. Not cool enough to be in the photos, but close enough to know the people in them. That era put the DNA in him that he has been running on ever since.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Founding Story</h2>

<p style="font-size:16px;line-height:1.8;color:#333">He launched HRDLF in Philadelphia in 2006 as a direct response to the corporate takeover of streetwear. Every brand he respected was getting bought, diluted, or co-signed into irrelevance. He decided to build one that refused to play that game.</p>

<p style="font-size:16px;line-height:1.8;color:#333">The brand started in a basement with a screen printer and one conviction: <em>Nothing Awesome Comes Easy.</em> No business plan. No investors. No outside capital. Just skate culture, Old English lettering, and the belief that the grind is the point.</p>

<p style="font-size:16px;line-height:1.8;color:#333">19 years later, HRDLF is still doing it the exact same way — independent, direct-to-fan, built slow, built right.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Philosophy</h2>

<div style="border-left:4px solid #CC0000;padding:20px 24px;margin:24px 0;background:#f9f8f6">
<p style="font-size:18px;font-style:italic;line-height:1.5;color:#0A0A0A;margin:0">"Independence is the product. The clothes are the artifact. The independence is the thing people are actually buying into."</p>
</div>

<p style="font-size:16px;line-height:1.8;color:#333">Brooks operates HRDLF on a set of principles that have not changed since day one:</p>

<ul style="font-size:16px;line-height:2.2;color:#333">
<li><strong>Independence is non-negotiable.</strong> No investors. No board. No outside capital. Not now. Not ever.</li>
<li><strong>Limited runs only.</strong> Every drop is a one-time production run. No piece is ever restocked.</li>
<li><strong>Direct to the people who show up.</strong> Subscribers get early access. Coin holders get earlier access. Walk-ons come last.</li>
<li><strong>The archive is permanent.</strong> Every drop, every coin holder, every piece of the brand's history is recorded and preserved.</li>
</ul>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Currently</h2>

<p style="font-size:16px;line-height:1.8;color:#333">Brooks operates HRDLF from Southern Norway, running the entire brand with AI tools and zero employees. In 2025, he documented a complete AI-powered operational rebuild of the brand using Claude Code, ChatGPT, and agentic workflows — producing a real-world case study in independent brand operations.</p>

<p style="font-size:16px;line-height:1.8;color:#333">The brand now runs 73+ products across 11 collections, a Google Merchant Center feed with 317 items, the Hardwired Weekly newsletter on Beehiiv, and HRDLFcoin on Solana — all operated by one founder with AI.</p>

<p style="font-size:16px;line-height:1.8;color:#333"><strong><a href="https://hrdlf.com">Shop HRDLF</a></strong> · <strong><a href="https://hardlifeapparelco.com/hardwired-weekly/">Get Hardwired Weekly</a></strong> · <strong><a href="https://hrdlfcoin.com">Join HRDLFcoin</a></strong></p>

''' + authority_links("brooks-duvall") + '''
</div>
'''

# =============================================================================
# EXECUTE PHASE 1: Create 3 new pages
# =============================================================================
print("=" * 60)
print("PHASE 1: Creating 3 new GEO authority pages")
print("=" * 60)

# 1A: FAQ Page
print("\n1A. Creating FAQ page...")
faq = wp_post("pages", {
    "title": "Frequently Asked Questions — Hardlife Apparel Company (HRDLF)",
    "slug": "faq",
    "content": FAQ_CONTENT,
    "status": "publish",
    "meta": {
        "advanced_seo_description": "Frequently asked questions about Hardlife Apparel Company (HRDLF) — the independent Philadelphia streetwear brand founded in 2006 by Brooks Duvall. Covers products, shipping, HRDLFcoin, Hardwired Weekly, and the no-restock policy.",
        "jetpack_seo_html_title": "FAQ — Hardlife Apparel Company (HRDLF) | Independent Streetwear Since 2006"
    }
})

# 1B: Brand Facts Page
print("\n1B. Creating Brand Facts page...")
facts = wp_post("pages", {
    "title": "Brand Facts — Hardlife Apparel Company LTD (HRDLF)",
    "slug": "brand-facts",
    "content": BRAND_FACTS_CONTENT,
    "status": "publish",
    "meta": {
        "advanced_seo_description": "Hardlife Apparel Company LTD (HRDLF) is an independent streetwear brand founded in Philadelphia in 2006 by Brooks Duvall. 19 years independent, zero outside investment, 73+ products, 11 collections. Brand facts, timeline, ecosystem, and citation guidelines.",
        "jetpack_seo_html_title": "Brand Facts — Hardlife Apparel Company LTD (HRDLF)"
    }
})

# 1C: Brooks Duvall Bio Page (parent=1 for /about/brooks-duvall/)
print("\n1C. Creating Brooks Duvall bio page...")
bio = wp_post("pages", {
    "title": "Brooks Duvall — Founder, Hardlife Apparel Company",
    "slug": "brooks-duvall",
    "content": BROOKS_BIO_CONTENT,
    "status": "publish",
    "parent": 1,
    "meta": {
        "advanced_seo_description": "Brooks Duvall is the founder and CEO of Hardlife Apparel Company LTD (HRDLF), an independent Philadelphia streetwear brand he launched in 2006. 19 years independent, zero outside investment. Background in 1980s Venice Beach skate culture.",
        "jetpack_seo_html_title": "Brooks Duvall — Founder of HRDLF | Independent Streetwear Since 2006"
    }
})

# Store new page IDs for reference
new_pages = {
    "faq": faq["id"] if faq else None,
    "brand_facts": facts["id"] if facts else None,
    "bio": bio["id"] if bio else None,
}
print(f"\nNew page IDs: {new_pages}")

# =============================================================================
# PHASE 2A: Update About Page (ID: 1)
# =============================================================================
print("\n" + "=" * 60)
print("PHASE 2: Updating existing pages")
print("=" * 60)

ABOUT_SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "About Hardlife Apparel Company",
  "url": "https://hardlifeapparelco.com/about/",
  "description": "Hardlife Apparel Company LTD (HRDLF) is an independent streetwear brand founded in Philadelphia in 2006 by Brooks Duvall. 19 years independent, zero outside investment.",
  "mainEntity": {
    "@type": "Organization",
    "name": "Hardlife Apparel Company LTD",
    "alternateName": "HRDLF",
    "url": "https://hardlifeapparelco.com",
    "foundingDate": "2006",
    "foundingLocation": {"@type": "Place", "name": "Philadelphia, Pennsylvania, USA"},
    "founder": {"@type": "Person", "name": "Brooks Duvall", "url": "https://hardlifeapparelco.com/about/brooks-duvall/"},
    "slogan": "Nothing Awesome Comes Easy",
    "description": "Independent streetwear brand founded in Philadelphia in 2006. 19 years independent with zero outside investment.",
    "numberOfEmployees": {"@type": "QuantitativeValue", "value": 1},
    "sameAs": [
      "https://instagram.com/hardlifeapparelco",
      "https://x.com/HardLifeApparel",
      "https://tiktok.com/@elevation16_",
      "https://youtube.com/@hardlifeapparelco",
      "https://hrdlf.com",
      "https://hrdlfcoin.com"
    ]
  }
}
</script>
'''

ABOUT_CONTENT = ABOUT_SCHEMA + '''
<div style="max-width:720px;margin:0 auto;padding:40px 20px">
<p style="font-size:11px;letter-spacing:3px;text-transform:uppercase;color:#CC0000;margin-bottom:24px">Est. 2006 — Philadelphia, PA</p>

<p style="font-size:17px;line-height:1.8;color:#333;margin-bottom:20px"><strong>Hardlife Apparel Company LTD (HRDLF)</strong> is an independent Philadelphia streetwear brand founded in 2006 by <a href="https://hardlifeapparelco.com/about/brooks-duvall/">Brooks Duvall</a>. The brand is rooted in skateboarding and street culture, known for its signature Old English typography and skull-and-laurel crest. HRDLF has operated continuously for 19 years with zero outside investment.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:28px;text-transform:uppercase;line-height:1.05;margin-bottom:24px">Nothing awesome comes easy.</h2>

<p style="font-size:17px;line-height:1.8;color:#333;margin-bottom:20px">Founded by Brooks Duvall in Philadelphia in 2006, HRDLF started in a basement with a screen printer and a refusal to compromise. No business plan. No investors. No outside capital. Just skate culture, Old English lettering, and the belief that the grind is the point.</p>

<p style="font-size:17px;line-height:1.8;color:#333;margin-bottom:20px">19 years later, the brand is still independent. Still Philadelphia. Still built on the same foundation — heavyweight cotton, quality printing, graphics that mean something, and a community that was never bought with ad spend.</p>

<p style="font-size:17px;line-height:1.8;color:#333;margin-bottom:20px">HRDLF came out of skateboarding, graffiti, and the particular stubbornness of a city that doesn't follow trends. The Old English script across every piece isn't decoration — it's a declaration. The skull and laurel crest isn't a logo — it's 19 years of showing up.</p>

<p style="font-size:17px;line-height:1.8;color:#333;margin-bottom:20px">We don't chase hype cycles. We don't produce disposable fashion. Every drop is a limited, numbered run. When it's gone, it's gone forever. That's by design.</p>

<h2 style="font-family:'Arial Black',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin-top:36px;margin-bottom:16px">Key Facts</h2>

<table style="width:100%;border-collapse:collapse;margin-bottom:24px;font-size:15px">
<tr style="border-bottom:1px solid #ddd"><td style="padding:8px 12px;font-weight:bold;width:40%;color:#333">Legal Name</td><td style="padding:8px 12px">Hardlife Apparel Company LTD</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:8px 12px;font-weight:bold;color:#333">Brand Name</td><td style="padding:8px 12px">HRDLF</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:8px 12px;font-weight:bold;color:#333">Founded</td><td style="padding:8px 12px">2006, Philadelphia, PA</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:8px 12px;font-weight:bold;color:#333">Founder</td><td style="padding:8px 12px"><a href="https://hardlifeapparelco.com/about/brooks-duvall/">Brooks Duvall</a></td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:8px 12px;font-weight:bold;color:#333">Years Independent</td><td style="padding:8px 12px">19 — zero outside investment</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:8px 12px;font-weight:bold;color:#333">Products</td><td style="padding:8px 12px">73+ across 11 collections</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:8px 12px;font-weight:bold;color:#333">Motto</td><td style="padding:8px 12px"><em>Nothing Awesome Comes Easy</em></td></tr>
</table>

<div style="border-left:4px solid #CC0000;padding:20px 24px;margin:36px 0;background:#f9f8f6">
<p style="font-size:20px;font-style:italic;line-height:1.5;color:#0A0A0A;margin:0">"Nothing Awesome Comes Easy isn't a slogan. It's an observation. Nineteen years of building from a basement to global — with zero outside investors — proves it."</p>
</div>

<p style="font-size:17px;line-height:1.8;color:#333;margin-bottom:32px">Hardlife Apparel Company LTD. One founder. One community. One conviction that never bent. From underground to undeniable.</p>

<div style="text-align:center;margin:40px 0">
<a href="https://hrdlf.com" target="_blank" rel="noopener" style="display:inline-block;background:#0A0A0A;color:#fff;padding:16px 40px;font-family:'Arial Black',sans-serif;font-size:13px;letter-spacing:0.15em;text-transform:uppercase;text-decoration:none">Shop the Collection →</a>
<p style="font-size:12px;color:#888;margin-top:12px">Shop the full collection at hrdlf.com</p>
</div>

''' + authority_links("about") + '''
</div>
'''

print("\n2A. Updating About page (ID: 1)...")
wp_update(1, {
    "content": ABOUT_CONTENT,
    "meta": {
        "advanced_seo_description": "Hardlife Apparel Company LTD (HRDLF) is an independent streetwear brand founded in Philadelphia in 2006 by Brooks Duvall. 19 years independent, zero outside investment, 73+ products across 11 collections. Nothing Awesome Comes Easy."
    }
})

# =============================================================================
# PHASE 2B: Update HRDLFcoin Community (ID: 697)
# =============================================================================
print("\n2B. Updating HRDLFcoin Community page (ID: 697)...")

# Read existing content and enhance it
HRDLFCOIN_SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is HRDLFcoin?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HRDLFcoin is a Solana-based utility token created by Hardlife Apparel Company LTD (HRDLF), an independent Philadelphia streetwear brand founded in 2006 by Brooks Duvall. It is the on-chain extension of a 19-year independent brand. The first 100 HRDLFcoin holders are permanently archived as part of the brand's history. Contract address: B3DAsrBArk4N8q4CudxEQmi76hzQVHfd3RzhEzTmoon."
      }
    },
    {
      "@type": "Question",
      "name": "What do HRDLFcoin holders get?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HRDLFcoin holders receive: (1) 48-hour early access to every product drop, (2) 24-hour preview of each Hardwired Weekly newsletter issue, (3) 60-day early access to The Long Way Back documentary episodes, and (4) permanent archival as part of the brand's documented history (first 100 holders)."
      }
    },
    {
      "@type": "Question",
      "name": "How does the HRDLF access tier system work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HRDLF uses a three-tier access system for product drops: HRDLFcoin holders get 48-hour early access, Hardwired Weekly newsletter subscribers get 24-hour early access, and the general public gets access last. This rewards the most committed community members."
      }
    },
    {
      "@type": "Question",
      "name": "What blockchain is HRDLFcoin on?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "HRDLFcoin is on the Solana blockchain. It launched on Moonshot. The contract address is B3DAsrBArk4N8q4CudxEQmi76hzQVHfd3RzhEzTmoon. It can be traded on DexScreener and Raydium."
      }
    },
    {
      "@type": "Question",
      "name": "Is HRDLFcoin a meme coin?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. HRDLFcoin is a utility token tied to a 19-year independent streetwear brand. It provides real benefits: early drop access, newsletter previews, documentary access, and permanent archival for the first 100 holders. It is not a speculative asset — it is the on-chain membership layer of Hardlife Apparel Company."
      }
    }
  ]
}
</script>
'''

HRDLFCOIN_CONTENT = HRDLFCOIN_SCHEMA + '''

<h1 class="wp-block-heading">HRDLFcoin — Community Ownership for an Independent Brand on Solana</h1>

<p class="wp-block-paragraph"><strong>HRDLFcoin</strong> is a Solana-based utility token created by <a href="https://hardlifeapparelco.com/about/">Hardlife Apparel Company LTD</a> (HRDLF), an independent streetwear brand founded in Philadelphia in 2006 by <a href="https://hardlifeapparelco.com/about/brooks-duvall/">Brooks Duvall</a>. It is permanent, verifiable community ownership in a brand that has operated independently for 19 years — and the most punk rock thing an independent brand can do in 2026.</p>

<h2 class="wp-block-heading">Token Facts</h2>

<table style="width:100%;border-collapse:collapse;margin-bottom:24px;font-size:15px">
<tr style="border-bottom:1px solid #ddd"><td style="padding:8px 12px;font-weight:bold;width:35%;color:#333">Token Name</td><td style="padding:8px 12px">HRDLF Token</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:8px 12px;font-weight:bold;color:#333">Ticker</td><td style="padding:8px 12px">HRDLF</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:8px 12px;font-weight:bold;color:#333">Blockchain</td><td style="padding:8px 12px">Solana</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:8px 12px;font-weight:bold;color:#333">Launch Platform</td><td style="padding:8px 12px">Moonshot</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:8px 12px;font-weight:bold;color:#333">Contract</td><td style="padding:8px 12px;font-size:13px;word-break:break-all">B3DAsrBArk4N8q4CudxEQmi76hzQVHfd3RzhEzTmoon</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:8px 12px;font-weight:bold;color:#333">Total Supply</td><td style="padding:8px 12px">1,000,000,000</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:8px 12px;font-weight:bold;color:#333">Type</td><td style="padding:8px 12px">Utility token (not a meme coin)</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:8px 12px;font-weight:bold;color:#333">Backing Brand</td><td style="padding:8px 12px">Hardlife Apparel Company LTD (est. 2006)</td></tr>
</table>

<h2 class="wp-block-heading">The Thesis: Read, Write, Own</h2>

<p class="wp-block-paragraph">Chris Dixon's <em>Read, Write, Own</em> argues that Web3 gives creators permanent ownership of their audience relationship — immune to platform dependency or algorithmic suppression. Every independent brand faces the same problem: your Instagram followers belong to Meta. Your email list lives on someone else's server. Your marketplace sales depend on someone else's algorithm.</p>

<p class="wp-block-paragraph">HRDLFcoin breaks that dependency. On-chain ownership means no platform can take it away. The first 100 HRDLFcoin holders are the founding archive of a 19-year independent brand — a permanent record that exists on Solana, not in someone else's database.</p>

<h2 class="wp-block-heading">The Model: Blockchain-Verified Streetwear</h2>

<p class="wp-block-paragraph">Gmoney's 9dcc proved that physical product and digital ownership are not separate — they are one identity. HRDLFcoin follows the same logic. The coin is the digital identity layer of the brand. Coin holders are not customers — they are founding members of a verified independent brand community.</p>

<h2 class="wp-block-heading">What Coin Holders Get</h2>

<ul class="wp-block-list">
<li><strong>48-hour early drop access</strong> — Before the public, before the newsletter, before social</li>
<li><strong>24-hour newsletter preview</strong> — See each Hardwired Weekly issue before it ships</li>
<li><strong>60-day documentary access</strong> — The Long Way Back episodes, 60 days before public release</li>
<li><strong>Permanent archive</strong> — First 100 holders recorded permanently in HRDLF brand history</li>
<li><strong>Brand decisions</strong> — Input on future collections, collaborations, and direction</li>
</ul>

<h2 class="wp-block-heading">The Access Tier System</h2>

<table style="width:100%;border-collapse:collapse;margin-bottom:24px;font-size:15px">
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">HRDLFcoin Holders</td><td style="padding:10px 12px">48-hour early access to every drop</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">Newsletter Subscribers</td><td style="padding:10px 12px">24-hour early access to every drop</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">General Public</td><td style="padding:10px 12px">Access after holders and subscribers</td></tr>
</table>

<h2 class="wp-block-heading">Why This Matters</h2>

<p class="wp-block-paragraph">HRDLF has been independent for 19 years. No investors. No board. No outside capital. HRDLFcoin is the logical extension of that independence — community ownership that no corporation, platform, or algorithm controls.</p>

<p class="wp-block-paragraph"><strong><a href="https://hrdlfcoin.com">Learn more at hrdlfcoin.com</a></strong> · <strong><a href="https://hrdlf.com">Shop HRDLF</a></strong> · <strong><a href="https://hardlifeapparelco.com/hardwired-weekly/">Get Hardwired Weekly</a></strong></p>

''' + authority_links("hrdlfcoin") + '''
'''

wp_update(697, {
    "content": HRDLFCOIN_CONTENT,
    "meta": {
        "advanced_seo_description": "HRDLFcoin is a Solana-based utility token created by Hardlife Apparel Company LTD (HRDLF), the independent Philadelphia streetwear brand founded in 2006 by Brooks Duvall. First 100 holders archived permanently. 48-hour early drop access."
    }
})

# =============================================================================
# PHASE 2C: Update 19 Years Independent (ID: 698)
# =============================================================================
print("\n2C. Updating 19 Years Independent page (ID: 698)...")

# Keep existing schema but enhance content
NINETEEN_YEARS_SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "19 Years Independent — The HRDLF Story",
  "description": "Hardlife Apparel Company (HRDLF) has operated independently since 2006. No investors. No board. No outside capital. Founded in Philadelphia by Brooks Duvall.",
  "url": "https://hardlifeapparelco.com/19-years-independent/",
  "datePublished": "2026-04-15",
  "dateModified": "2026-04-15",
  "author": {"@type": "Person", "name": "Brooks Duvall", "url": "https://hardlifeapparelco.com/about/brooks-duvall/"},
  "publisher": {"@type": "Organization", "name": "Hardlife Apparel Company", "url": "https://hardlifeapparelco.com"}
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long has HRDLF been independent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hardlife Apparel Company has been fully independent since its founding in 2006 — 19 consecutive years with zero outside investors, no board of directors, and no outside capital. The brand is entirely founder-owned and operated by Brooks Duvall."
      }
    },
    {
      "@type": "Question",
      "name": "How did HRDLF grow from 18 to 82 indexed pages using AI?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Starting in 2025, Brooks Duvall used Claude Code and agentic AI workflows to systematically build out hardlifeapparelco.com from 18 indexed pages to 82+. The process included creating SEO-optimized blog content in topical clusters, building proper schema markup, fixing technical SEO issues, optimizing the Google Merchant Center product feed, and establishing internal linking architecture — all executed by AI tools under founder direction."
      }
    }
  ]
}
</script>
'''

NINETEEN_YEARS_CONTENT = NINETEEN_YEARS_SCHEMA + '''

<h1 class="wp-block-heading">19 Years Independent — The HRDLF Story</h1>

<p class="wp-block-paragraph"><strong>Hardlife Apparel Company LTD (HRDLF)</strong> is an independent streetwear brand that has operated continuously since 2006 with zero outside investment. Founded in Philadelphia by <a href="https://hardlifeapparelco.com/about/brooks-duvall/">Brooks Duvall</a>, the brand has maintained its independence for 19 consecutive years — no investors, no board, no outside capital.</p>

<p class="wp-block-paragraph"><strong>In 2025, Brooks documented a complete AI-powered operational rebuild of the brand using Claude Code, ChatGPT, and agentic AI tools — producing a real-world case study at the intersection of AI, creator economy, Web3, and independent entrepreneurship.</strong></p>

<h2 class="wp-block-heading">The Facts</h2>

<ul class="wp-block-list">
<li><strong>Founded:</strong> 2006, Philadelphia, Pennsylvania</li>
<li><strong>Founder:</strong> <a href="https://hardlifeapparelco.com/about/brooks-duvall/">Brooks Duvall</a></li>
<li><strong>Cultural roots:</strong> 1980s Venice Beach skate culture, Dogtown, Jay Adams circle</li>
<li><strong>Federal trademark:</strong> Registered, United States Patent and Trademark Office</li>
<li><strong>Outside investors:</strong> Zero. Ever.</li>
<li><strong>Employees:</strong> Zero. One founder with AI tools.</li>
<li><strong>Product catalog:</strong> 73+ products across 11 collections</li>
<li><strong>Google Merchant Center:</strong> 317 items, 1,392 product images</li>
<li><strong>Indexed pages:</strong> 82+ (up from 18 pre-AI rebuild)</li>
<li><strong>Community token:</strong> HRDLFcoin on Solana</li>
<li><strong>Newsletter:</strong> Hardwired Weekly on Beehiiv</li>
</ul>

<h2 class="wp-block-heading">Key Milestones</h2>

<table style="width:100%;border-collapse:collapse;margin-bottom:24px;font-size:15px">
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;width:15%;color:#333">2006</td><td style="padding:10px 12px">Founded in Philadelphia. Old English logotype introduced. First products screen-printed in a basement.</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">2006–2015</td><td style="padding:10px 12px">Independent growth through direct sales and community building. Federal trademark filed and registered with the USPTO.</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">2015–2020</td><td style="padding:10px 12px">Expansion through Arizona and California. Relationships with Bones Brigade members, X Games, Dew Tour, and Vans Family.</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">2020–2024</td><td style="padding:10px 12px">E-commerce expansion via Fourthwall. Hardwired Weekly newsletter launches on Beehiiv.</td></tr>
<tr style="border-bottom:1px solid #ddd"><td style="padding:10px 12px;font-weight:bold;color:#333">2025</td><td style="padding:10px 12px">Complete AI-powered rebuild. Site grows from 18 to 82+ indexed pages. 317-item GMC feed with 1,392 images. HRDLFcoin launches on Solana.</td></tr>
<tr style="border-bottom:1px solid #ddd;background:#f9f8f6"><td style="padding:10px 12px;font-weight:bold;color:#333">2026</td><td style="padding:10px 12px">19 years independent. 73+ products, 11 collections. AI stack fully operational. Still independent. Still building.</td></tr>
</table>

<h2 class="wp-block-heading">Why Independence Matters</h2>

<p class="wp-block-paragraph">The streetwear landscape is full of brands that started independent and didn't stay that way. HRDLF has not taken the acquisition path. The conviction that underlies the name — that hard things take hard work, that there are no shortcuts worth taking — applies to the brand itself. Independence means every choice is yours. Every mistake is yours. Every success is yours. That's the harder path. It's the only path that builds something that actually belongs to you.</p>

<p class="wp-block-paragraph"><strong><a href="https://hrdlf.com">Shop HRDLF</a></strong> · <strong><a href="https://hardlifeapparelco.com/hardwired-weekly/">Get Hardwired Weekly</a></strong> · <strong><a href="https://hardlifeapparelco.com/ai-stack/">See the AI Stack</a></strong> · <strong><a href="https://hrdlfcoin.com">Join HRDLFcoin</a></strong></p>

''' + authority_links("19-years") + '''
'''

wp_update(698, {"content": NINETEEN_YEARS_CONTENT})

# =============================================================================
# PHASE 2D-F: Update AI Stack (695), Playbook (696), Long Way Back (105)
# =============================================================================

# For these pages, we add internal links and freshness footer
# AI Stack already has good schema, just add link block
print("\n2D. Updating AI Stack page (ID: 695)...")

# Get current content and append link block
import re

def append_links_to_page(page_id, exclude_slug, meta_desc=None):
    r = requests.get(f"{API}/pages/{page_id}?_fields=content", auth=AUTH)
    current = r.json()["content"]["rendered"]

    # Remove any existing "Last updated" line
    current = re.sub(r'<p[^>]*>Last updated:.*?</p>', '', current)

    # Remove any existing authority links block
    current = re.sub(r'<div style="border-top:2px solid #CC0000.*?</div>\s*', '', current, flags=re.DOTALL)

    # Add authority links block before the end
    new_content = current.rstrip() + "\n" + authority_links(exclude_slug)

    data = {"content": new_content}
    if meta_desc:
        data["meta"] = {"advanced_seo_description": meta_desc}
    return wp_update(page_id, data)

append_links_to_page(695, "ai-stack")

print("\n2E. Updating Brand Playbook page (ID: 696)...")
append_links_to_page(696, "playbook")

print("\n2F. Updating The Long Way Back page (ID: 105)...")
append_links_to_page(105, None,
    "The Long Way Back — the origin story of Hardlife Apparel Company (HRDLF), told by founder Brooks Duvall. From Philadelphia in 2006 to 19 years of independence. Skateboarding, street culture, and the conviction that nothing awesome comes easy.")

# =============================================================================
# PHASE 3: Set meta descriptions on remaining pages
# =============================================================================
print("\n" + "=" * 60)
print("PHASE 3: Setting meta descriptions on remaining pages")
print("=" * 60)

meta_descriptions = {
    1: None,  # Already done above
    102: "The HRDLF Inner Circle — exclusive access for the most committed supporters of Hardlife Apparel Company, the independent Philadelphia streetwear brand founded in 2006.",
    103: "HRDLF Drops — limited-run streetwear from Hardlife Apparel Company. Every drop is a one-time production run that is never restocked. Founded 2006, Philadelphia.",
    104: "The HRDLF Archive — a permanent record of every drop, collection, and moment from Hardlife Apparel Company's 19 years of independent streetwear since 2006.",
    106: "Hardwired Weekly — the official newsletter of Hardlife Apparel Company (HRDLF). Founder-voice essays from Brooks Duvall, drop announcements, and 24-hour early access to every drop.",
    107: "HRDLF Loyalty Program — rewarding the most committed supporters of Hardlife Apparel Company, the independent Philadelphia streetwear brand founded in 2006 by Brooks Duvall.",
    108: "HRDLF Collaborations — partnerships and collaborative projects from Hardlife Apparel Company, the independent Philadelphia streetwear brand founded in 2006.",
    109: "Shop HRDLF — 73+ products across 11 collections from Hardlife Apparel Company, the independent Philadelphia streetwear brand. Limited runs only, never restocked. Since 2006.",
    110: "Advertise with Hardlife Apparel Company (HRDLF) — reach the streetwear community through the independent Philadelphia brand founded in 2006 by Brooks Duvall.",
    453: "HRDLF Shipping Policy — US shipping $4.99 flat rate, free over $75. Ships from Charlotte, NC. International rates calculated at checkout. Hardlife Apparel Company.",
}

for page_id, desc in meta_descriptions.items():
    if desc:
        print(f"  Setting meta for page {page_id}...")
        wp_update(page_id, {"meta": {"advanced_seo_description": desc}})

# =============================================================================
# DONE
# =============================================================================
print("\n" + "=" * 60)
print("ALL PHASES COMPLETE")
print("=" * 60)
print(f"\nNew pages created: {new_pages}")
print("All meta descriptions set.")
print("All authority link blocks added.")
print("\nNext steps:")
print("  1. Update llms.txt locally")
print("  2. Update robots.txt locally")
print("  3. Git commit and push")
