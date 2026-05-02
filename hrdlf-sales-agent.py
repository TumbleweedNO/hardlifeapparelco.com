#!/usr/bin/env python3
"""
HRDLF Sales Agent
Agentic email system for Hardlife Apparel Co.
Sends intelligent, psychologically-crafted product emails via Resend API.
Reads subscriber list from Beehiiv API for segmentation.

Usage:
    python3 hrdlf-sales-agent.py              # Live send
    python3 hrdlf-sales-agent.py --dry-run    # Preview without sending
    python3 hrdlf-sales-agent.py --force      # Bypass weekly rate limit
    python3 hrdlf-sales-agent.py --segment    # Show subscriber segments only
"""

import os
import sys
import csv
import json
import random
import hashlib
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# ─── Configuration ───────────────────────────────────────────────────────────

# Beehiiv — subscriber data (read-only)
BEEHIIV_API_KEY = "ENEJ4uO7jOPSOXnGAewgA9YwoQlvl22T944t5kZIruFYAVDtYBMCPhcbL8tKUrKl"
BEEHIIV_PUB_ID = "pub_72b88199-d2c3-40c8-92d6-5a2444f6094b"
BEEHIIV_BASE = "https://api.beehiiv.com/v2"

# Resend — email delivery
RESEND_API_KEY = "re_G2PewoBJ_PCHiWWBQiuJ6LoNDLfpeeoX3"
RESEND_BASE = "https://api.resend.com"
# Before domain verification, only sends to 19hrdlf@gmail.com
# After verifying hardlifeapparelco.com in Resend, change FROM_EMAIL and set DOMAIN_VERIFIED = True
FROM_EMAIL = "HRDLF <noreply@hardlifeapparelco.com>"
DOMAIN_VERIFIED = True

SCRIPT_DIR = Path(__file__).parent.resolve()
LOG_FILE = SCRIPT_DIR / "hrdlf-sales-log.csv"
PURCHASE_LOG = SCRIPT_DIR / "hrdlf-purchases.csv"
STATE_FILE = SCRIPT_DIR / ".hrdlf-agent-state.json"

MAX_EMAILS_PER_WEEK = 1
PURCHASE_COOLDOWN_DAYS = 14

# ─── Product Catalog (73 products, 11 collections) ──────────────────────────
# Synced from Fourthwall API (size=100) — 2026-03-22

CATALOG = {
    # ── OG Logo (5) ──────────────────────────────────────────────────────────
    "og-white-tee": {
        "name": "OG Logo Tee — White",
        "price": "$48",
        "url": "https://hrdlf.com/products/og-logo-tee-white",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/e7efc37e-7778-4c4f-9032-20f9646be5f7.jpeg",
        "collection": "og",
        "type": "tee",
    },
    "og-black-tee": {
        "name": "OG Logo Tee — Black",
        "price": "$48",
        "url": "https://hrdlf.com/products/og-logo-tee-black",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/a50a3368-df7a-4958-a30e-1c4856651d98.jpeg",
        "collection": "og",
        "type": "tee",
    },
    "og-blue-tee": {
        "name": "OG Logo — Blue Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/og-logo-blue-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/f90dfbff-344f-44f6-8525-faea31ebb49d.jpeg",
        "collection": "og",
        "type": "tee",
    },
    "og-black-ls": {
        "name": "OG Logo — Black Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/og-logo-black-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/22f873c5-d170-48d7-8b42-680a961badd2.jpeg",
        "collection": "og",
        "type": "longsleeve",
    },
    "og-white-ls": {
        "name": "OG Logo — White Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/og-logo-white-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/04bc9d41-33dc-46d8-b436-a31382358e18.jpeg",
        "collection": "og",
        "type": "longsleeve",
    },
    "og-black-hoodie": {
        "name": "OG Logo — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/og-logo-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/05a69b26-4e7b-409c-a87e-9e9691900e5d.jpeg",
        "collection": "og",
        "type": "hoodie",
    },
    "og-white-hoodie": {
        "name": "OG Logo — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/og-logo-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/b707020d-1fa5-4011-91b9-c3de9320d1ca.jpeg",
        "collection": "og",
        "type": "hoodie",
    },
    # ── OG Logo Red Baron (6) ────────────────────────────────────────────────
    "rb-white-tee": {
        "name": "OG Logo Red Baron — White Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/og-logo-red-barron-white-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/bcda9a17-e6cd-4c14-8a58-21e3fc5565ff.jpeg",
        "collection": "redbaron",
        "type": "tee",
    },
    "rb-black-tee": {
        "name": "OG Logo Red Baron — Black Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/og-logo-red-baron-black-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/c164d6d7-c22b-44e1-a884-ddf88f646cc0.jpeg",
        "collection": "redbaron",
        "type": "tee",
    },
    "rb-black-ls": {
        "name": "OG Logo Red Baron — Black Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/og-logo-red-baron-black-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/c637ba0b-27e6-4283-bf8e-1b0ac49d7282.jpeg",
        "collection": "redbaron",
        "type": "longsleeve",
    },
    "rb-white-ls": {
        "name": "OG Logo Red Baron — White Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/oo-logo-red-baron-white-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/a9d6ee62-530e-408f-92ae-dd1d3af83c46.jpeg",
        "collection": "redbaron",
        "type": "longsleeve",
    },
    "rb-black-hoodie": {
        "name": "OG Logo Red Baron — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/og-logo-red-baron-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/09870b18-2a29-4648-b524-ccf286c1c6be.jpeg",
        "collection": "redbaron",
        "type": "hoodie",
    },
    "rb-white-hoodie": {
        "name": "OG Logo Red Baron — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/og-logo-red-baron-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/0e3113ba-c882-4fe1-a568-e4e71528b3dd.jpeg",
        "collection": "redbaron",
        "type": "hoodie",
    },
    # ── Human Beings (7) ─────────────────────────────────────────────────────
    "hb-black-tee": {
        "name": "Human Beings — Black Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/human-beings-black-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/fac1b0b9-ed1c-4138-8e09-dd157140ab49.jpeg",
        "collection": "human",
        "type": "tee",
    },
    "hb-white-tee": {
        "name": "Human Beings — White Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/human-beings-white-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/45db4e8c-5609-4d96-801c-49a50f34eb0c.jpeg",
        "collection": "human",
        "type": "tee",
    },
    "hb-white-ls": {
        "name": "Human Beings — White Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/human-beings-white-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/27396002-2e42-470a-900d-d39016032c33.jpeg",
        "collection": "human",
        "type": "longsleeve",
    },
    "hb-black-ls": {
        "name": "Human Beings — Black Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/human-beings-black-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/ae29ff37-360c-49b8-a36f-e850849270a3.jpeg",
        "collection": "human",
        "type": "longsleeve",
    },
    "hb-black-hoodie": {
        "name": "Human Beings — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/human-beings-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/d5eb1008-3cac-41be-87e3-10ac184b2ddc.jpeg",
        "collection": "human",
        "type": "hoodie",
    },
    "hb-white-hoodie": {
        "name": "Human Beings — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/human-beings-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/057f0377-0984-491d-83ff-189ca74d328f.jpeg",
        "collection": "human",
        "type": "hoodie",
    },
    # ── United We Stand (6) ──────────────────────────────────────────────────
    "uws-black-tee": {
        "name": "United We Stand — Black Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/united-we-stand-black-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/3f36f404-b985-4bf9-9db3-76f10be2d3f0.jpeg",
        "collection": "uws",
        "type": "tee",
    },
    "uws-white-tee": {
        "name": "United We Stand — White Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/united-we-stand-white-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/dfab18f5-ac2f-41e7-baa5-676e2c4ea6be.jpeg",
        "collection": "uws",
        "type": "tee",
    },
    "uws-black-ls": {
        "name": "United We Stand — Black Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/united-we-stand-black-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/8c368efe-fc0a-4bc0-95eb-9bea1bed3f5f.jpeg",
        "collection": "uws",
        "type": "longsleeve",
    },
    "uws-white-ls": {
        "name": "United We Stand — White Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/united-we-stand-white-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/27241d33-2146-4a5a-9c8e-c08f5b6b7e35.jpeg",
        "collection": "uws",
        "type": "longsleeve",
    },
    "uws-black-hoodie": {
        "name": "United We Stand — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/united-we-stand-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/17cc78b9-559d-49b8-b6ae-d2e2bbb75ea6.jpeg",
        "collection": "uws",
        "type": "hoodie",
    },
    "uws-white-hoodie": {
        "name": "United We Stand — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/united-we-stand-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/e94af90b-f91f-4083-b472-e88e530c259b.jpeg",
        "collection": "uws",
        "type": "hoodie",
    },
    # ── HRDLF Skull (9) ─────────────────────────────────────────────────────
    "skull-black-tee": {
        "name": "HRDLF Skull — Black Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/hrdlf-skull-black-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/124c69b3-737a-4892-8a9c-a980987133d5.jpeg",
        "collection": "skull",
        "type": "tee",
    },
    "skull-white-tee": {
        "name": "HRDLF Skull — White Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/hrdlf-skull-white-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/e09966b5-deec-4a2d-bad8-dc607228a0d2.jpeg",
        "collection": "skull",
        "type": "tee",
    },
    "skull-blue-tee": {
        "name": "HRDLF Orange Skull — Blue Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/hrdlf-orange-skull-blue-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/258a87db-c30f-44ea-b326-b18f40378f7e.jpeg",
        "collection": "skull",
        "type": "tee",
    },
    "skull-black-ls": {
        "name": "HRDLF Skull — Black Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/hrdlf-skull-black-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/1a7f365d-df2e-46a6-bc74-35123e9208aa.jpeg",
        "collection": "skull",
        "type": "longsleeve",
    },
    "skull-white-ls": {
        "name": "HRDLF Skull — White Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/hrdlf-skull-white-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/e7a1f94e-77b6-491c-8676-913c89c396eb.jpeg",
        "collection": "skull",
        "type": "longsleeve",
    },
    "skull-blue-ls": {
        "name": "HRDLF Orange Skull — Blue Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/hrdlf-orange-skull-blue-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/97e38ba3-8c29-442d-9dd6-f5e4d2bc3c9b.jpeg",
        "collection": "skull",
        "type": "longsleeve",
    },
    "skull-black-hoodie": {
        "name": "HRDLF Skull — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/hrdlf-skull-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/df9a1931-ebd3-41e6-859f-5a0c8087d88b.jpeg",
        "collection": "skull",
        "type": "hoodie",
    },
    "skull-white-hoodie": {
        "name": "HRDLF Skull — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/hrdlf-skull-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/3f3e5ac1-c83b-4338-b99e-bbebe19563c6.jpeg",
        "collection": "skull",
        "type": "hoodie",
    },
    "skull-blue-hoodie": {
        "name": "Orange HRDLF Skull — Blue Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/orange-hrdlf-skull-blue-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/6b146d86-a8a2-402c-b3e6-832ac9dcaf70.jpeg",
        "collection": "skull",
        "type": "hoodie",
    },
    # ── Limited Gold Print Skull (3) ─────────────────────────────────────────
    "gold-skull-red-hoodie": {
        "name": "Limited Gold Print HRDLF Skull — Red Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/limited-gold-print-hrdlf-skull-red-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/6f21f577-0d81-40a8-bc6f-d89eb8e2e7f2.jpeg",
        "collection": "goldskull",
        "type": "hoodie",
    },
    "gold-skull-white-hoodie": {
        "name": "Limited Gold Print HRDLF Skull — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/limited-gold-print-hrdlf-skull-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/3704b75a-90e9-473d-a055-92a68fbffffd.jpeg",
        "collection": "goldskull",
        "type": "hoodie",
    },
    "gold-skull-black-hoodie": {
        "name": "Limited Gold Print HRDLF Skull — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/limited-gold-print-hrdlf-skull-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/9fafb894-6dca-4a94-aa43-84a6826d744b.jpeg",
        "collection": "goldskull",
        "type": "hoodie",
    },
    # ── Nothing Awesome Comes Easy (6) ───────────────────────────────────────
    "nace-black-tee": {
        "name": "Nothing Awesome Comes Easy — Black Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/nothing-awesome-comes-easy-black-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/b5e4316e-3a2c-43fc-838c-a27d457cfdd6.jpeg",
        "collection": "nace",
        "type": "tee",
    },
    "nace-white-tee": {
        "name": "Nothing Awesome Comes Easy — White Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/nothing-awesome-comes-easy-white-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/1688c100-9c42-4d0a-a2f4-588416854af0.jpeg",
        "collection": "nace",
        "type": "tee",
    },
    "nace-black-ls": {
        "name": "Nothing Awesome Comes Easy — Black Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/nothing-awesome-comes-easy-black-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/8b268b60-67b1-4fc0-ae7c-b2431af94dcf.jpeg",
        "collection": "nace",
        "type": "longsleeve",
    },
    "nace-white-ls": {
        "name": "Nothing Awesome Comes Easy — White Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/nothing-awesome-comes-easy-white-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/a77115da-ffb4-48a6-a653-80aab82b29a9.jpeg",
        "collection": "nace",
        "type": "longsleeve",
    },
    "nace-black-hoodie": {
        "name": "Nothing Awesome Comes Easy — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/nothing-awesome-comes-easy-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/0990fccd-6844-45ed-964a-ff28402f683e.jpeg",
        "collection": "nace",
        "type": "hoodie",
    },
    "nace-white-hoodie": {
        "name": "Nothing Awesome Comes Easy — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/nothing-awesome-comes-easy-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/b5f19138-59b9-4994-93b5-4c8a0d6f05ad.jpeg",
        "collection": "nace",
        "type": "hoodie",
    },
    # ── Red Star (6) ─────────────────────────────────────────────────────────
    "redstar-black-tee": {
        "name": "Red Star — Black Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/red-star-black-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/dafc094b-d9c8-4343-96c5-6f6065d2d181.jpeg",
        "collection": "redstar",
        "type": "tee",
    },
    "redstar-white-tee": {
        "name": "Red Star — White Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/red-star-white-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/7bd066f6-f3d5-417e-ac01-0dd58eac7443.jpeg",
        "collection": "redstar",
        "type": "tee",
    },
    "redstar-black-ls": {
        "name": "Red Star — Black Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/red-star-black-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/de06d936-0fd5-48d3-92ab-b3b365b18036.jpeg",
        "collection": "redstar",
        "type": "longsleeve",
    },
    "redstar-white-ls": {
        "name": "Red Star — White Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/red-star-white-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/e84aea0c-bac4-401c-b8c2-52619cd26362.jpeg",
        "collection": "redstar",
        "type": "longsleeve",
    },
    "redstar-black-hoodie": {
        "name": "Red Star — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/red-star-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/d293c366-d3a6-4976-854c-ceb2b5178c03.jpeg",
        "collection": "redstar",
        "type": "hoodie",
    },
    "redstar-white-hoodie": {
        "name": "Red Star — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/red-star-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/9bb98525-926e-4480-90af-2703dca49614.jpeg",
        "collection": "redstar",
        "type": "hoodie",
    },
    # ── Graffiti (10) ────────────────────────────────────────────────────────
    "graf-black-tee": {
        "name": "Graffiti — Black Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/graffiti-black-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/4a97bf03-9830-4eed-b365-cceb73ec05ea.jpeg",
        "collection": "graffiti",
        "type": "tee",
    },
    "graf-white-tee": {
        "name": "Graffiti — White Tee",
        "price": "$48",
        "url": "https://hrdlf.com/products/graffiti-white-tee",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/df92b634-42c9-406c-b927-f0b2182749e9.jpeg",
        "collection": "graffiti",
        "type": "tee",
    },
    "graf-black-ls": {
        "name": "Graffiti — Black Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/graffiti-black-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/4af25749-77e4-4940-b6b7-a570ce173383.jpeg",
        "collection": "graffiti",
        "type": "longsleeve",
    },
    "graf-white-ls": {
        "name": "Graffiti — White Longsleeve",
        "price": "$57",
        "url": "https://hrdlf.com/products/graffiti-white-longsleeve",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/3e1f5201-1a80-4144-96ae-977f1ec509c4.jpeg",
        "collection": "graffiti",
        "type": "longsleeve",
    },
    "graf-black-hoodie": {
        "name": "Graffiti — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/graffiti-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/63f151fa-1931-4070-a592-04eed8ea80eb.jpeg",
        "collection": "graffiti",
        "type": "hoodie",
    },
    "graf-white-hoodie": {
        "name": "Graffiti — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/graffiti-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/c29cd297-b4f4-49e8-9477-52653a7263ef.jpeg",
        "collection": "graffiti",
        "type": "hoodie",
    },
    "graf-pink-black-hoodie": {
        "name": "Pink Graffiti — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/pink-graffiti-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/64fd516a-e396-4555-8c2c-4a46e3b86402.jpeg",
        "collection": "graffiti",
        "type": "hoodie",
    },
    "graf-pink-white-hoodie": {
        "name": "Pink Graffiti — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/pink-graffiti-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/e20998c9-fa4d-48c8-b469-64b6e0b9cdc8.jpeg",
        "collection": "graffiti",
        "type": "hoodie",
    },
    "graf-blue-black-hoodie": {
        "name": "Blue Graffiti — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/blue-graffiti-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/1697468d-af5e-4143-b872-2c7dee12fdec.jpeg",
        "collection": "graffiti",
        "type": "hoodie",
    },
    "graf-blue-white-hoodie": {
        "name": "Blue Graffiti — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/blue-graffiti-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/4624dec0-6030-4ce8-883d-d22f7d89d8e1.jpeg",
        "collection": "graffiti",
        "type": "hoodie",
    },
    "graf-green-black-hoodie": {
        "name": "Green Graffiti — Black Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/green-graffiti-black-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/cb3ed6d0-ab0c-4043-85ac-f06909d23969.jpeg",
        "collection": "graffiti",
        "type": "hoodie",
    },
    "graf-green-white-hoodie": {
        "name": "Green Graffiti — White Hoodie",
        "price": "$75",
        "url": "https://hrdlf.com/products/green-graffiti-white-hoodie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/898ba63d-a8a7-4654-8710-4631bba4fbfd.jpeg",
        "collection": "graffiti",
        "type": "hoodie",
    },
    # ── Nordic Fjord Camo (3) ────────────────────────────────────────────────
    "fjord-backpack": {
        "name": "HRDLF Nordic Fjord Camo Backpack",
        "price": "$60",
        "url": "https://hrdlf.com/products/hrdlf-nordic-fjord-camo-backpack",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/cebd948b-aa33-48d9-a13c-e64b036c8b09.jpeg",
        "collection": "fjord",
        "type": "accessory",
    },
    "fjord-tote": {
        "name": "HRDLF Nordic Fjord Camo Tote Bag",
        "price": "$52",
        "url": "https://hrdlf.com/products/hrdlf-nordic-fjord-camo-tote-bag",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/9f7d1aa0-7716-41ff-b92e-ebaea1820e63.jpeg",
        "collection": "fjord",
        "type": "accessory",
    },
    "fjord-drawstring": {
        "name": "HRDLF Nordic Fjord Camo Drawstring Bag",
        "price": "$29",
        "url": "https://hrdlf.com/products/hrdlf-nordic-fjord-camo-drawstring-bag",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/832d3fb1-4a13-451c-b1d6-b2a6ef9f7c76.jpeg",
        "collection": "fjord",
        "type": "accessory",
    },
    "fjord-duffle": {
        "name": "HRDLF Nordic Fjord Camo Duffle Bag",
        "price": "$95",
        "url": "https://hrdlf.com/products/hrdlf-nordic-fjord-camo-duffle-bag",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/99ccf8be-9743-42b8-ab77-85bcfcac6c1c.jpeg",
        "collection": "fjord",
        "type": "accessory",
    },
    # ── Accessories (9) ──────────────────────────────────────────────────────
    "patch": {
        "name": "HRDLF Embroidered Patch",
        "price": "$15",
        "url": "https://hrdlf.com/products/hrdlf-embroidered-patch",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/1de95e07-e4f6-4301-8ad9-01c5293f24b1.jpeg",
        "collection": "accessories",
        "type": "accessory",
    },
    "mug": {
        "name": "HRDLF Black Mug",
        "price": "$15",
        "url": "https://hrdlf.com/products/hrdlf-black-mug",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/aee72781-0581-4390-befd-28e0076d4ec5.jpeg",
        "collection": "accessories",
        "type": "accessory",
    },
    "beanie-gray": {
        "name": "HRDLF Gray Beanie",
        "price": "$25",
        "url": "https://hrdlf.com/products/hrdlf-gray-beanie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/26c4366f-d394-4a7e-9530-3c78e5f1e23d.jpeg",
        "collection": "accessories",
        "type": "accessory",
    },
    "beanie-black": {
        "name": "HRDLF Black Beanie",
        "price": "$25",
        "url": "https://hrdlf.com/products/hrdlf-black-beanie",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/f4723b73-22d5-48bf-beb4-9aef4b96bd1d.jpeg",
        "collection": "accessories",
        "type": "accessory",
    },
    "snap-red": {
        "name": "HRDLF — Red Snapback",
        "price": "$35",
        "url": "https://hrdlf.com/products/hrdlf-red-snapback",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/8fe10efc-267f-47fe-b36e-981f52fdde4b.jpeg",
        "collection": "accessories",
        "type": "accessory",
    },
    "snap-green": {
        "name": "HRDLF — Green Snapback",
        "price": "$35",
        "url": "https://hrdlf.com/products/hrdlf-green-snapback",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/3b4fd0c8-c7b1-41a8-9717-73d5f862462b.jpeg",
        "collection": "accessories",
        "type": "accessory",
    },
    "snap-black": {
        "name": "HRDLF — Black Snapback",
        "price": "$35",
        "url": "https://hrdlf.com/products/hrdlf-black-snapback",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/48260b35-7701-4668-b050-8d8168ec507a.jpeg",
        "collection": "accessories",
        "type": "accessory",
    },
    "trucker": {
        "name": "HRDLF Camo Trucker Hat",
        "price": "$35",
        "url": "https://hrdlf.com/products/hrdlf-camo-trucker-hat",
        "img": "https://cdn.fourthwall.com/offer/sh_edd038df-9387-435f-a5ed-83f673666a43/d4c1ea7e-5ec1-4e7d-9663-ca3858b7a8c0.jpeg",
        "collection": "accessories",
        "type": "accessory",
    },
}

# ─── Beehiiv API Helpers ─────────────────────────────────────────────────────

def beehiiv_request(endpoint, method="GET", data=None):
    """Make authenticated request to Beehiiv API."""
    url = f"{BEEHIIV_BASE}{endpoint}"
    headers = {
        "Authorization": f"Bearer {BEEHIIV_API_KEY}",
        "Content-Type": "application/json",
    }
    body = json.dumps(data).encode() if data else None
    req = Request(url, data=body, headers=headers, method=method)
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        error_body = e.read().decode() if e.fp else ""
        print(f"  API ERROR {e.code}: {error_body}")
        return None


def get_subscribers():
    """Pull all active subscribers with stats."""
    subs = []
    cursor = None
    while True:
        endpoint = f"/publications/{BEEHIIV_PUB_ID}/subscriptions?limit=100&status=active&expand=stats"
        if cursor:
            endpoint += f"&cursor={cursor}"
        resp = beehiiv_request(endpoint)
        if not resp:
            break
        subs.extend(resp.get("data", []))
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")
    return subs


def segment_subscribers(subscribers):
    """Segment subscribers into new, warm, cold."""
    now = datetime.now(timezone.utc)
    seven_days_ago = now - timedelta(days=7)
    thirty_days_ago = now - timedelta(days=30)

    segments = {"new": [], "warm": [], "cold": []}

    for sub in subscribers:
        created = datetime.fromtimestamp(sub["created"], tz=timezone.utc)
        stats = sub.get("stats", {}) or {}
        opens = stats.get("total_unique_opened", 0) or 0

        if created >= seven_days_ago:
            segments["new"].append(sub)
        elif opens > 0:
            segments["warm"].append(sub)
        else:
            segments["cold"].append(sub)

    return segments


# ─── Product Selection ───────────────────────────────────────────────────────

def select_product(email_type, day_seed=None):
    """Select one product contextually based on email type and day rotation."""
    if day_seed is None:
        day_seed = int(datetime.now().strftime("%j"))  # day of year

    if email_type == "welcome":
        # Welcome emails feature signature hoodies
        keys = ["nace-black-hoodie", "og-black-hoodie", "skull-black-hoodie",
                "hb-black-hoodie", "gold-skull-black-hoodie"]
    elif email_type == "drop":
        # Drop announcements rotate through hoodies and longsleeves
        keys = [k for k, v in CATALOG.items() if v["type"] in ("hoodie", "longsleeve")]
    elif email_type == "reengagement":
        # Re-engagement features accessible price points (tees + accessories)
        keys = [k for k, v in CATALOG.items() if v["type"] in ("tee", "accessory")]
    elif email_type == "product_spotlight":
        # Spotlight rotates through all collections
        collections = ["nace", "og", "redbaron", "human", "uws", "skull",
                       "goldskull", "redstar", "graffiti", "fjord", "accessories"]
        col = collections[day_seed % len(collections)]
        keys = [k for k, v in CATALOG.items() if v["collection"] == col]
    else:
        keys = ["nace-black-hoodie"]

    if not keys:
        keys = ["nace-black-hoodie"]

    chosen_key = keys[day_seed % len(keys)]
    product = CATALOG[chosen_key].copy()
    product["key"] = chosen_key
    return product


# ─── Email Templates (Brooks' Voice) ────────────────────────────────────────

def generate_email(email_type, product):
    """Generate email content in Brooks' voice. Max 150 words. No fluff."""

    p_name = product["name"]
    p_price = product["price"]
    p_url = product["url"]
    p_collection = product["collection"]

    p_img = product.get("img", "")

    # Product block HTML (editorial, not e-commerce)
    product_block = f"""
<div style="background:#0A0A0A;border-top:3px solid #C41E1E;padding:24px;margin:24px 0;">
  <p style="font-size:9px;letter-spacing:3px;color:#555;text-transform:uppercase;margin:0 0 12px;">FROM THE COLLECTION</p>
  <div style="text-align:center;margin:0 0 16px;">
    <a href="{p_url}"><img src="{p_img}" alt="{p_name}" width="300" style="display:block;margin:0 auto;width:300px;border:0;" /></a>
  </div>
  <p style="font-size:14px;font-weight:800;text-transform:uppercase;color:#fff;margin:0 0 6px;">{p_name}</p>
  <p style="font-size:14px;color:#ccc;margin:0 0 4px;">{p_price}</p>
  <p style="font-size:11px;font-style:italic;color:#666;margin:0 0 12px;">Limited run. No restocks.</p>
  <a href="{p_url}" style="font-size:11px;color:#ffffff;text-decoration:underline;">&mdash; available at hrdlf.com</a>
</div>"""

    templates = {
        "welcome": {
            "subject": f"This is HRDLF",
            "body": f"""<p style="color:#ccc;font-size:14px;line-height:1.7;">
Started this brand in Philadelphia in 2006. Skate parks and screen printing. Twenty years later we're still here and everything we make means something.

This is not a hype brand. We don't do sales. We don't do restocks. When a piece is gone, it's gone.

You're on the list now. Every Thursday you get Hardwired Weekly — the drop schedule, the story behind what we're building, and first access before anything goes public.

Welcome to the hard life.
</p>
{product_block}
<p style="color:#666;font-size:13px;">— HRDLF</p>""",
        },
        "drop": {
            "subject": f"New piece just dropped",
            "body": f"""<p style="color:#ccc;font-size:14px;line-height:1.7;">
The {p_name.split("—")[0].strip() if "—" in p_name else p_name} just went live on hrdlf.com.

You're seeing this before the public site updates. That's the point of being on this list.

Same rules as always: limited run, no restocks, no exceptions. When the count hits zero it's done.
</p>
{product_block}
<p style="color:#666;font-size:13px;">— HRDLF</p>""",
        },
        "reengagement": {
            "subject": f"Still here",
            "body": f"""<p style="color:#ccc;font-size:14px;line-height:1.7;">
Haven't seen you around. No pitch — just checking in.

We've been building. New pieces in the collection. The brand keeps moving whether you're watching or not.

If you're still about it, the link's below. If not, no hard feelings.
</p>
{product_block}
<p style="color:#666;font-size:13px;">— HRDLF</p>""",
        },
        "product_spotlight": {
            "subject": f"{p_name.split('—')[0].strip() if '—' in p_name else p_name}",
            "body": f"""<p style="color:#ccc;font-size:14px;line-height:1.7;">
Every piece in the collection exists for a reason. This one came from the same place everything else does — the culture, the city, the refusal to make something forgettable.

Not going to oversell it. You either see it or you don't.
</p>
{product_block}
<p style="color:#666;font-size:13px;">— HRDLF</p>""",
        },
    }

    template = templates.get(email_type, templates["product_spotlight"])
    return template


# ─── Rate Limiting & State ───────────────────────────────────────────────────

def load_state():
    """Load agent state from disk."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"last_send": None, "sends_this_week": 0, "week_start": None, "last_product": None}


def save_state(state):
    """Persist agent state."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def can_send(state, force=False):
    """Check if we're within rate limits."""
    if force:
        return True, "forced"

    now = datetime.now(timezone.utc)
    week_start_str = state.get("week_start")

    if week_start_str:
        week_start = datetime.fromisoformat(week_start_str)
        # Reset weekly counter if new week
        if (now - week_start).days >= 7:
            state["sends_this_week"] = 0
            state["week_start"] = now.isoformat()
    else:
        state["week_start"] = now.isoformat()

    if state.get("sends_this_week", 0) >= MAX_EMAILS_PER_WEEK:
        return False, f"rate limited ({state['sends_this_week']}/{MAX_EMAILS_PER_WEEK} this week)"

    return True, "clear"


def get_recent_purchasers():
    """Load emails of recent purchasers from CSV."""
    if not PURCHASE_LOG.exists():
        return set()

    cutoff = datetime.now(timezone.utc) - timedelta(days=PURCHASE_COOLDOWN_DAYS)
    recent = set()

    with open(PURCHASE_LOG, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                purchase_date = datetime.fromisoformat(row["date"])
                if purchase_date >= cutoff:
                    recent.add(row["email"].lower())
            except (KeyError, ValueError):
                continue

    return recent


def log_send(email_type, product_key, subject, subscriber_count, status):
    """Append send record to CSV log."""
    file_exists = LOG_FILE.exists()

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "email_type", "product", "subject", "subscribers", "status"])
        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            email_type,
            product_key,
            subject,
            subscriber_count,
            status,
        ])


# ─── Email Type Selection Logic ──────────────────────────────────────────────

def determine_email_type(segments):
    """Decide which email type to send based on subscriber composition."""
    # Priority order:
    # 1. If new subscribers exist → welcome
    # 2. If cold subscribers exist → re-engagement
    # 3. If warm subscribers exist → rotate between drop and product_spotlight
    # 4. Default → product_spotlight

    if segments["new"]:
        return "welcome"

    if segments["cold"] and len(segments["cold"]) >= len(segments["warm"]):
        return "reengagement"

    day_of_week = datetime.now().weekday()
    if day_of_week in (1, 4):  # Tuesday, Friday
        return "drop"

    return "product_spotlight"


# ─── Send via Resend ─────────────────────────────────────────────────────────

def resend_request(endpoint, data):
    """Make authenticated request to Resend API."""
    url = f"{RESEND_BASE}{endpoint}"
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "HRDLF-Sales-Agent/1.0",
        "Accept": "application/json",
    }
    body = json.dumps(data).encode()
    req = Request(url, data=body, headers=headers, method="POST")
    try:
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        error_body = e.read().decode() if e.fp else ""
        print(f"    Resend API ERROR {e.code}: {error_body}")
        return None
    except Exception as e:
        print(f"    Resend request error: {e}")
        return None


def build_html(body_html):
    """Wrap email body in HRDLF template."""
    return f"""
<div style="background:#060606;padding:40px 20px;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;">
  <div style="max-width:560px;margin:0 auto;">
    <p style="font-size:9px;letter-spacing:3px;color:#999999;text-transform:uppercase;margin:0 0 24px;">HARDLIFE APPAREL CO.</p>
    {body_html}
    <div style="margin-top:32px;padding-top:16px;border-top:1px solid #1a1a1a;">
      <p style="font-size:10px;color:#333;">
        Hardlife Apparel Company LTD | Est. 2006 Philadelphia | <a href="https://hrdlf.com" style="color:#444;">hrdlf.com</a>
      </p>
    </div>
  </div>
</div>"""


def send_email(email_content, subscribers, dry_run=False):
    """Send email to each subscriber individually via Resend."""
    subject = email_content["subject"]
    full_html = build_html(email_content["body"])

    if dry_run:
        return {"status": "dry_run", "subject": subject, "would_send_to": len(subscribers)}

    # Collect recipient emails
    emails = [s.get("email") for s in subscribers if s.get("email")]

    # Before domain verification, Resend only allows sending to the account owner
    if not DOMAIN_VERIFIED:
        owner_email = "19hrdlf@gmail.com"
        print(f"    Domain not verified — sending to owner ({owner_email}) only")
        emails = [owner_email]

    sent_count = 0
    failed_count = 0
    email_ids = []

    for recipient in emails:
        result = resend_request("/emails", {
            "from": FROM_EMAIL,
            "to": recipient,
            "subject": subject,
            "html": full_html,
        })

        if result and result.get("id"):
            sent_count += 1
            email_ids.append(result["id"])
            print(f"    Sent to {recipient} (id: {result['id']})")
        else:
            failed_count += 1
            print(f"    Failed: {recipient}")

    status = "sent" if sent_count > 0 else "failed"
    return {
        "status": status,
        "subject": subject,
        "sent": sent_count,
        "failed": failed_count,
        "email_ids": email_ids,
    }


# ─── Main Agent Loop ─────────────────────────────────────────────────────────

def run(dry_run=False, force=False, segment_only=False):
    """Main agent execution."""
    print("=" * 60)
    print("HRDLF SALES AGENT")
    print(f"Run: {datetime.now(timezone.utc).isoformat()}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}{' (FORCED)' if force else ''}")
    print("=" * 60)

    # 1. Pull subscribers
    print("\n[1] Pulling subscribers from Beehiiv...")
    subscribers = get_subscribers()
    print(f"    Total active: {len(subscribers)}")

    if not subscribers:
        print("    No subscribers found. Exiting.")
        log_send("none", "none", "none", 0, "no_subscribers")
        return

    # 2. Segment
    print("\n[2] Segmenting subscribers...")
    segments = segment_subscribers(subscribers)
    print(f"    NEW  (last 7 days):    {len(segments['new'])}")
    print(f"    WARM (opened in 30d):  {len(segments['warm'])}")
    print(f"    COLD (no opens 30d+):  {len(segments['cold'])}")

    for seg_name, seg_list in segments.items():
        for sub in seg_list:
            email = sub.get("email", "")
            stats = sub.get("stats", {}) or {}
            opens = stats.get("total_unique_opened", 0)
            print(f"      [{seg_name.upper()}] {email} (opens: {opens})")

    if segment_only:
        print("\n-- Segment report only. Exiting. --")
        return

    # 3. Filter out recent purchasers
    recent_purchasers = get_recent_purchasers()
    if recent_purchasers:
        print(f"\n[3] Filtering {len(recent_purchasers)} recent purchasers (14-day cooldown)")
    else:
        print("\n[3] No recent purchasers to filter")

    eligible_count = len([s for s in subscribers if s.get("email", "").lower() not in recent_purchasers])
    print(f"    Eligible subscribers: {eligible_count}")

    if eligible_count == 0:
        print("    All subscribers in purchase cooldown. Exiting.")
        log_send("none", "none", "none", 0, "all_in_cooldown")
        return

    # 4. Check rate limits
    print("\n[4] Checking rate limits...")
    state = load_state()
    allowed, reason = can_send(state, force=force)
    print(f"    Status: {'CLEAR' if allowed else 'BLOCKED'} ({reason})")
    print(f"    Sends this week: {state.get('sends_this_week', 0)}/{MAX_EMAILS_PER_WEEK}")

    if not allowed:
        print("    Rate limited. Exiting.")
        log_send("none", "none", "none", 0, f"rate_limited:{reason}")
        return

    # 5. Determine email type
    print("\n[5] Selecting email type...")
    email_type = determine_email_type(segments)
    print(f"    Type: {email_type}")

    # 6. Select product
    print("\n[6] Selecting product...")
    day_seed = int(datetime.now().strftime("%j"))
    # Avoid repeating last product
    last_product = state.get("last_product")
    product = select_product(email_type, day_seed)
    if product["key"] == last_product:
        product = select_product(email_type, day_seed + 1)
    print(f"    Product: {product['name']}")
    print(f"    Price: {product['price']}")
    print(f"    URL: {product['url']}")

    # 7. Generate email
    print("\n[7] Generating email content...")
    email_content = generate_email(email_type, product)
    print(f"    Subject: {email_content['subject']}")
    print(f"    Type: {email_type}")

    # Preview body text (strip HTML for console)
    import re
    plain = re.sub(r"<[^>]+>", "", email_content["body"])
    plain = re.sub(r"\s+", " ", plain).strip()
    word_count = len(plain.split())
    print(f"    Word count: {word_count}")

    if word_count > 150:
        print(f"    WARNING: Exceeds 150 word limit ({word_count} words)")

    # 8. Filter eligible subscribers (remove recent purchasers)
    eligible_subs = [s for s in subscribers if s.get("email", "").lower() not in recent_purchasers]

    print(f"\n[8] {'Previewing' if dry_run else 'Sending'} to {len(eligible_subs)} subscribers via Resend...")
    result = send_email(email_content, eligible_subs, dry_run=dry_run)
    print(f"    Result: {result['status']}")

    if result.get("sent"):
        print(f"    Delivered: {result['sent']}")
    if result.get("failed"):
        print(f"    Failed: {result['failed']}")

    # 9. Update state and log
    status = result["status"]
    if status == "sent":
        state["last_send"] = datetime.now(timezone.utc).isoformat()
        state["sends_this_week"] = state.get("sends_this_week", 0) + 1
        state["last_product"] = product["key"]
        save_state(state)

    log_send(email_type, product["key"], email_content["subject"], eligible_count, status)

    print(f"\n[9] Logged to {LOG_FILE}")
    print("=" * 60)
    print("DONE")
    print("=" * 60)


# ─── CLI ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HRDLF Sales Agent")
    parser.add_argument("--dry-run", action="store_true", help="Preview without sending")
    parser.add_argument("--force", action="store_true", help="Bypass weekly rate limit")
    parser.add_argument("--segment", action="store_true", help="Show subscriber segments only")
    args = parser.parse_args()

    run(dry_run=args.dry_run, force=args.force, segment_only=args.segment)
