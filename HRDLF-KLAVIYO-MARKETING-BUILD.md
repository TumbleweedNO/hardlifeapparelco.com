# HRDLF KLAVIYO FULL BUILD
### Graffiti Beach Tie Dye Hoodie Drop — April 2nd, 2026
### Updated: March 23, 2026 — Klaviyo API Build Complete

---

## BUILD STATUS — LIVE ASSETS IN KLAVIYO

### Templates (6 created)
| Template | Klaviyo ID | Type |
|----------|-----------|------|
| Drop Email 1: Subscriber Early Access | `UCpEBc` | Drop Sequence |
| Drop Email 2: Drop Day Reminder | `XAenZx` | Drop Sequence |
| Drop Email 3: Last Chance | `TnmzmW` | Drop Sequence |
| Post-Purchase 1: Brand Story | `WXdknU` | Post-Purchase |
| Post-Purchase 2: Cross-Sell | `S8ju8G` | Post-Purchase |
| Post-Purchase 3: Community Invite | `Rvirw5` | Post-Purchase |

### Campaigns (3 created — all DRAFT)
| Campaign | Klaviyo ID | Scheduled | Target |
|----------|-----------|-----------|--------|
| Email 1: Subscriber Early Access | `01KME9PXARHYQGQGMGFS19NHPK` | Apr 1, 11:59 PM ET | HRDLF Newsletter (SP8eUj) |
| Email 2: Drop Day Reminder | `01KME9QKNSX6E53T6VVCZVKS9X` | Apr 2, 9:00 AM ET | HRDLF Newsletter (SP8eUj) |
| Email 3: Last Chance | `01KME9R70FF93JSPMVG09B0QGF` | Apr 5, 1:00 PM ET | HRDLF Newsletter (SP8eUj) |

### Flows (1 created — DRAFT)
| Flow | Klaviyo ID | Trigger | Status |
|------|-----------|---------|--------|
| HRDLF Post-Purchase Flow | `TFGkCh` | Active on Site (placeholder) | Draft |

**Post-Purchase Flow Actions:**
1. 4-hour delay → Brand Story email (WXdknU)
2. 5-day delay → Cross-Sell email (S8ju8G)
3. 10-day delay → Community Invite email (Rvirw5)

### Segments (1 created)
| Segment | Klaviyo ID | Definition |
|---------|-----------|------------|
| HRDLF Newsletter Subscribers | `TBbAiS` | Members of SP8eUj list |

### Existing Assets (pre-audit)
| Asset | Klaviyo ID | Status |
|-------|-----------|--------|
| Email Welcome Series with Discount | `WjrZQt` (flow) | LIVE |
| HRDLF Newsletter | `SP8eUj` (list) | Active, 3 profiles |
| SMS List | `VprW2V` (list) | Active |
| Preview List | `X7ezc2` (list) | Active |

---

## ACTION REQUIRED — BEFORE GOING LIVE

### 1. Disable Fourthwall Abandoned Cart Emails (30 seconds)
- Log into **hrdlf.com** Fourthwall dashboard
- **Settings → Emails** → Set abandoned cart to **OFF**
- Leave order confirmation and shipping ON (transactional)

### 2. Fix Fourthwall → Klaviyo Order Sync
The Fourthwall integration is syncing profiles but **NOT pushing order events**. No `Placed Order`, `Started Checkout`, or `Ordered Product` metrics exist in Klaviyo yet. This means:
- The post-purchase flow trigger is set to "Active on Site" as a **placeholder**
- Once order events flow in, change the trigger to `Placed Order` in the Klaviyo dashboard
- To verify: Klaviyo → Analytics → Metrics → look for "Placed Order"
- If missing after 48 hours: disconnect and reconnect the Fourthwall integration, or contact Fourthwall support

### 3. Review & Schedule Campaigns
All 3 drop campaigns are in **DRAFT** status. Before going live:
- Review each email in Klaviyo's preview/test send
- Confirm send times match your intent
- **Campaign 3 (Last Chance)** is set to Apr 5 — adjust based on when you want to close the drop

### 4. Set Post-Purchase Flow to LIVE
Once the `Placed Order` metric exists:
- Go to Flows → HRDLF Post-Purchase Flow
- Change trigger from "Active on Site" to "Placed Order"
- Set flow status to **Live**

---

## STEP 0 — CONFLICT RESOLUTION (DO THIS FIRST)

### STATUS: ACTION REQUIRED — Manual Dashboard Step

**Fourthwall abandoned cart emails are ON.** This MUST be disabled before any Klaviyo abandoned cart flow goes live, or every cart abandoner gets double-emailed.

#### Instructions (30 seconds):
1. Log into **hrdlf.com** Fourthwall dashboard
2. Go to **Settings → Emails** (or Settings → Checkout → Abandoned Checkout Reminders)
3. Set abandoned cart emails to **OFF**
4. Save

#### Fourthwall Default Email Audit:
| Email Type | Fourthwall Status | Action |
|------------|------------------|--------|
| Order confirmation | ON (keep) | **Leave ON** — transactional, legally required |
| Shipping notification | ON (keep) | **Leave ON** — tied to carrier scan, transactional |
| Abandoned cart | **ON (DISABLE)** | **Turn OFF** — Klaviyo will own this |
| Out of stock notice | ON (keep) | Leave ON — order-specific, transactional |

**Confirm this is done before proceeding to any Klaviyo flow build.**

---

## STEP 1 — KLAVIYO ACCOUNT AUDIT

### STATUS: COMPLETE — Audited via API on March 23, 2026

**API Key:** `pk_d3b3a30d67d05cc46676a34ddd2a522266`

#### Audit Results:
| Asset | Count | Details |
|-------|-------|---------|
| Flows | 1 | Welcome Series (WjrZQt) — LIVE since Jan 17 |
| Campaigns | 0 | None sent before this build |
| Lists | 3 | HRDLF Newsletter (SP8eUj), SMS (VprW2V), Preview (X7ezc2) |
| Segments | 0 | None before this build |
| Templates | 0 | None before this build |
| Profiles | 3 | info@, 19hrdlf@, 111173elin@ |
| Metrics | 31 | All Klaviyo-native. NO Fourthwall order metrics |
| SMS | Enabled | SMS List exists, metrics tracked |

#### Fourthwall Integration Gap:
Expected Fourthwall metrics NOT present: `Placed Order`, `Ordered Product`, `Started Checkout`, `Viewed Product`. Only `Active on Site` (API source) exists. This must be resolved before post-purchase flows can go live.

---

## STEP 2 — GRAFFITI BEACH DROP SEQUENCE (3 Emails)

### Product Details (from Fourthwall API)
- **Name:** Graffiti Beach Tie Dye Hoodie (Zip Up)
- **Colors:** Black, White
- **Price:** $75 (2XL: $77)
- **Sizes:** S, M, L, XL, 2XL
- **Stock:** UNLIMITED (print-on-demand via Independent Trading Co.)
- **URL (Black):** `https://hrdlf.com/products/graffiti-beach-tie-dye-black-zip-up`
- **URL (White):** `https://hrdlf.com/products/graffiti-beach-tie-dye-white-zip-up`
- **Story:** 1980s Venice Beach tribute — graffiti lettering, rainbow gradient, the era that launched skate/street culture globally

### Klaviyo Configuration
- **Type:** Campaign (manual send, not automated flow — drops are event-driven)
- **Send list:** All active email subscribers
- **Email 2 filter:** Exclude anyone who placed an order containing "Graffiti Beach" after Email 1 sent
- **Email 3 trigger:** Manual send when you decide stock is running low (Fourthwall's "UNLIMITED" stock type means no automatic inventory trigger — you control the scarcity signal)

> **Note on "150 units":** The Fourthwall API shows stock type as UNLIMITED (print-on-demand). If you want to enforce a limited run of 150, you'll need to manually delist the product after 150 orders. The email copy below uses "limited run" language without citing a specific number — adjust if you set a hard cap.

---

### EMAIL 1: SUBSCRIBER EARLY ACCESS
**Send:** April 1st, 11:59 PM ET

#### Subject Line Variants (A/B/C Test in Klaviyo)
| Variant | Subject | Angle |
|---------|---------|-------|
| **A** | `You're in first. Graffiti Beach drops now.` | Urgency + exclusivity |
| **B** | `Venice Beach, 1985. This hoodie is that era.` | Culture/story |
| **C** | `Brooks here. The Graffiti Beach is ready.` | Founder-direct |

#### Preview Text
`Subscriber-only access. 24 hours before the public drop.`

#### Klaviyo Template HTML (Paste into Klaviyo HTML editor)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Graffiti Beach — Subscriber Early Access</title>
</head>
<body style="margin:0;padding:0;background:#000000;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#000000;">
<tr><td align="center" style="padding:20px;">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">

<!-- Header -->
<tr><td style="padding:24px 0 20px;text-align:center;">
  <p style="font-size:11px;font-weight:800;letter-spacing:4px;color:#999999;text-transform:uppercase;margin:0;">HARDLIFE APPAREL CO.</p>
</td></tr>

<!-- Hero Image -->
<tr><td style="padding:0;">
  <a href="https://hrdlf.com/products/graffiti-beach-tie-dye-black-zip-up">
    <img src="https://imgproxy.fourthwall.com/XNhv_OTG5rN9sfNtJgLyQLTz20Nzq1mmHTClsP-erjE/sm:1/enc/bv4g7w0TdW2IbFqO/34hhU0OeeE42ye4Z/lsvE1DSTYFcdJXK9/PKOgyckKFA8KSz1Y/FB_Jy_ZE3nM6-DP-/oQtGrb0JMl0jCz8T/JTKUJvU4PiawL1SN/UMUiXEOsTqkIjyFS/3fPpm3Z7a8X5JO9n/lKTlRv85XS74a0vb/eWeQ6ipPAeVE2vaK/lPLdcR0Zde0TE5AP/vUvEYDDphhhyuSuJ/TLVT-w" alt="Graffiti Beach Tie Dye Hoodie" width="600" style="display:block;width:100%;max-width:600px;border:0;" />
  </a>
</td></tr>

<!-- Body -->
<tr><td style="padding:32px 24px;">
  <p style="font-size:16px;color:#ffffff;line-height:1.7;margin:0 0 20px;">You're on this list for a reason.</p>

  <p style="font-size:16px;color:#ffffff;line-height:1.7;margin:0 0 20px;">The Graffiti Beach Hoodie drops to the public tomorrow at 10 AM.<br>You're getting in right now.</p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 24px;">This is HRDLF's most visually striking piece — a direct tribute to 1980s Venice Beach, California, where graffiti, skateboarding, and street art were at the absolute forefront of culture. "Hard Life Apparel" rendered in bold graffiti lettering with a full rainbow gradient — purple bleeding into red, into orange, into gold, into green — outlined in black. This is what the walls of Venice Beach looked like in that era.</p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 24px;">Premium heavyweight zip-up. Independent Trading Co. base. Printed in a limited run. When it's gone, the page comes down — same policy we've held for 19 years.</p>

  <!-- Product Details -->
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0A0A0A;border-top:3px solid #C41E1E;margin:0 0 24px;">
  <tr><td style="padding:20px;">
    <p style="font-size:14px;font-weight:800;color:#ffffff;text-transform:uppercase;letter-spacing:1px;margin:0 0 6px;">GRAFFITI BEACH TIE DYE HOODIE</p>
    <p style="font-size:14px;color:#cccccc;margin:0 0 4px;">$75 &nbsp;&middot;&nbsp; Black or White &nbsp;&middot;&nbsp; S–2XL</p>
    <p style="font-size:11px;font-style:italic;color:#666666;margin:0;">Limited run. No restocks. No exceptions.</p>
  </td></tr>
  </table>

  <!-- CTA -->
  <table width="100%" cellpadding="0" cellspacing="0">
  <tr><td align="center" style="padding:8px 0 32px;">
    <a href="https://hrdlf.com/products/graffiti-beach-tie-dye-black-zip-up" style="display:inline-block;background:#C41E1E;color:#ffffff;font-size:14px;font-weight:800;text-transform:uppercase;letter-spacing:2px;padding:16px 48px;text-decoration:none;">GET YOURS BEFORE EVERYONE ELSE &rarr;</a>
  </td></tr>
  </table>

  <p style="font-size:14px;color:#ffffff;line-height:1.7;margin:0 0 20px;">This is how it works at HRDLF. The people who showed up first get in first. You showed up.</p>

  <!-- Signature -->
  <p style="font-size:14px;color:#999999;margin:32px 0 0;">— Brooks<br>
  <span style="font-size:11px;color:#666666;">Hardlife Apparel Company<br>Philadelphia, 2006</span></p>
</td></tr>

<!-- Footer -->
<tr><td style="padding:24px;border-top:1px solid #222222;">
  <p style="font-size:10px;color:#444444;text-align:center;margin:0;">You're receiving this because you subscribed. Early access on every drop — always.</p>
</td></tr>

</table>
</td></tr>
</table>
</body>
</html>
```

---

### EMAIL 2: DROP DAY REMINDER
**Send:** April 2nd, 9:00 AM ET
**Klaviyo filter:** Exclude subscribers who placed an order since Email 1 send time

#### Subject Line
`The Graffiti Beach Hoodie is live. Public drop.`

#### Preview Text
`Your subscriber window is closing. Public access starts now.`

#### Klaviyo Template HTML

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background:#000000;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#000000;">
<tr><td align="center" style="padding:20px;">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">

<tr><td style="padding:24px 0 20px;text-align:center;">
  <p style="font-size:11px;font-weight:800;letter-spacing:4px;color:#999999;text-transform:uppercase;margin:0;">HARDLIFE APPAREL CO.</p>
</td></tr>

<tr><td style="padding:0;">
  <a href="https://hrdlf.com/products/graffiti-beach-tie-dye-black-zip-up">
    <img src="https://imgproxy.fourthwall.com/XNhv_OTG5rN9sfNtJgLyQLTz20Nzq1mmHTClsP-erjE/sm:1/enc/bv4g7w0TdW2IbFqO/34hhU0OeeE42ye4Z/lsvE1DSTYFcdJXK9/PKOgyckKFA8KSz1Y/FB_Jy_ZE3nM6-DP-/oQtGrb0JMl0jCz8T/JTKUJvU4PiawL1SN/UMUiXEOsTqkIjyFS/3fPpm3Z7a8X5JO9n/lKTlRv85XS74a0vb/eWeQ6ipPAeVE2vaK/lPLdcR0Zde0TE5AP/vUvEYDDphhhyuSuJ/TLVT-w" alt="Graffiti Beach Hoodie" width="600" style="display:block;width:100%;max-width:600px;border:0;" />
  </a>
</td></tr>

<tr><td style="padding:32px 24px;">
  <p style="font-size:16px;color:#ffffff;line-height:1.7;margin:0 0 20px;">It's live.</p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 20px;">The Graffiti Beach Hoodie went to subscribers at midnight. It goes to the world right now. Once the public hits the page, inventory moves faster. You know how this works.</p>

  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0A0A0A;border-top:3px solid #C41E1E;margin:0 0 24px;">
  <tr><td style="padding:20px;">
    <p style="font-size:14px;font-weight:800;color:#ffffff;text-transform:uppercase;margin:0 0 6px;">GRAFFITI BEACH TIE DYE HOODIE — $75</p>
    <p style="font-size:11px;font-style:italic;color:#666666;margin:0;">Limited run. When it's gone, the page comes down.</p>
  </td></tr>
  </table>

  <table width="100%" cellpadding="0" cellspacing="0">
  <tr><td align="center" style="padding:8px 0 24px;">
    <a href="https://hrdlf.com/products/graffiti-beach-tie-dye-black-zip-up" style="display:inline-block;background:#C41E1E;color:#ffffff;font-size:14px;font-weight:800;text-transform:uppercase;letter-spacing:2px;padding:16px 48px;text-decoration:none;">CLAIM YOURS &rarr;</a>
  </td></tr>
  </table>

  <p style="font-size:12px;color:#666666;text-align:center;margin:0;">
    <a href="https://hrdlf.com/products/graffiti-beach-tie-dye-white-zip-up" style="color:#999999;text-decoration:underline;">Also available in white &rarr;</a>
  </p>

  <p style="font-size:14px;color:#555555;margin:32px 0 0;">— HRDLF</p>
</td></tr>

<tr><td style="padding:24px;border-top:1px solid #222222;">
  <p style="font-size:10px;color:#444444;text-align:center;margin:0;">Subscriber-only list. Early access on every drop.</p>
</td></tr>

</table>
</td></tr>
</table>
</body>
</html>
```

**Word count:** 89 words (under 150 target)

---

### EMAIL 3: LOW STOCK / LAST CHANCE
**Send:** Manual trigger when you decide the drop is nearly done
**Klaviyo filter:** Exclude anyone who already purchased Graffiti Beach

> **Flow configuration note:** Since Fourthwall stock is UNLIMITED (print-on-demand), there's no automatic inventory webhook. Send this manually when you're ready to close the drop — or set a date (e.g., April 5th) as the "last call" to create a real deadline.

#### Subject Line
`Almost gone. Not coming back.`

#### Preview Text
`This is the last email about this drop. You're in or you're not.`

#### Klaviyo Template HTML

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background:#000000;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#000000;">
<tr><td align="center" style="padding:20px;">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">

<tr><td style="padding:24px 0 20px;text-align:center;">
  <p style="font-size:11px;font-weight:800;letter-spacing:4px;color:#999999;text-transform:uppercase;margin:0;">HARDLIFE APPAREL CO.</p>
</td></tr>

<tr><td style="padding:32px 24px;">
  <p style="font-size:20px;font-weight:800;color:#ffffff;text-transform:uppercase;letter-spacing:1px;margin:0 0 24px;">Last call.</p>

  <p style="font-size:16px;color:#ffffff;line-height:1.7;margin:0 0 20px;">Straight with you: the Graffiti Beach Hoodie is coming down.</p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 24px;">When it sells out, it sells out. That's been the rule since 2006. We don't do restocks. We don't do second runs. Every piece we make is the only run of that piece.</p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 24px;">This is the last email you'll get about this drop. Either you're in, or you'll see it on someone else.</p>

  <table width="100%" cellpadding="0" cellspacing="0">
  <tr><td align="center" style="padding:16px 0 8px;">
    <a href="https://hrdlf.com/products/graffiti-beach-tie-dye-black-zip-up" style="display:inline-block;background:#C41E1E;color:#ffffff;font-size:16px;font-weight:800;text-transform:uppercase;letter-spacing:2px;padding:20px 56px;text-decoration:none;">GET THE LAST ONES &rarr;</a>
  </td></tr>
  <tr><td align="center" style="padding:8px 0 24px;">
    <a href="https://hrdlf.com/products/graffiti-beach-tie-dye-white-zip-up" style="font-size:12px;color:#999999;text-decoration:underline;">White version &rarr;</a>
  </td></tr>
  </table>

  <p style="font-size:14px;color:#555555;margin:32px 0 0;">— HRDLF<br>
  <span style="font-size:11px;color:#444444;">Philadelphia. 2006. Still here.</span></p>
</td></tr>

<tr><td style="padding:24px;border-top:1px solid #222222;">
  <p style="font-size:10px;color:#444444;text-align:center;margin:0;">Final notice for this drop. No further emails about this product.</p>
</td></tr>

</table>
</td></tr>
</table>
</body>
</html>
```

---

## STEP 3 — POST-PURCHASE FLOW (3 Emails)

### Klaviyo Flow Configuration
| Setting | Value |
|---------|-------|
| **Trigger** | `Placed Order` (Fourthwall event) |
| **Filter** | Order value > $0 (excludes test orders) |
| **Conditional split** | First-time buyer vs. repeat buyer |
| **First-timers** | Get all 3 emails |
| **Repeat buyers** | Skip Email 1 (brand story), get Emails 2-3 only |
| **Exit condition** | Customer places another order → exits flow |

---

### POST-PURCHASE EMAIL 1: THE BRAND STORY
**Timing:** 4 hours after `Placed Order` event
**Why 4 hours:** Fourthwall sends order confirmation immediately. This arrives after the receipt but while purchase excitement is peak.

#### Subject Line
`You're part of something now.`

#### Preview Text
`19 years. No investors. No shortcuts. Here's what HRDLF actually is.`

#### Klaviyo Template HTML

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background:#000000;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#000000;">
<tr><td align="center" style="padding:20px;">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">

<tr><td style="padding:24px 0 20px;text-align:center;">
  <p style="font-size:11px;font-weight:800;letter-spacing:4px;color:#999999;text-transform:uppercase;margin:0;">HARDLIFE APPAREL CO.</p>
</td></tr>

<tr><td style="padding:32px 24px;">
  <p style="font-size:16px;color:#ffffff;line-height:1.7;margin:0 0 20px;">Your order is confirmed. Fourthwall already sent you the receipt. This is something different.</p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 20px;">You just bought into an independent brand that's been running since 2006 without outside investors, without corporate backing, without compromising the product to make the numbers work. That's 19 years of showing up the same way.</p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 20px;">HRDLF started in Philadelphia. Skate culture. Street culture. The idea that nothing awesome comes easy — and that the things worth having are the things you earned.</p>

  <p style="font-size:14px;color:#ffffff;line-height:1.7;margin:0 0 8px;">Every piece in the HRDLF catalog is:</p>
  <p style="font-size:14px;color:#cccccc;line-height:2;margin:0 0 24px;padding-left:12px;">
    &rarr; Premium heavyweight construction<br>
    &rarr; Screenprinted in limited runs<br>
    &rarr; Never restocked once sold out<br>
    &rarr; Made for people who actually wear it
  </p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 24px;">What you just bought isn't just a hoodie or a tee. It's a piece of a brand that refuses to operate like everyone else.</p>

  <p style="font-size:16px;color:#ffffff;line-height:1.7;margin:0 0 24px;">Welcome to HRDLF.</p>

  <table width="100%" cellpadding="0" cellspacing="0">
  <tr><td align="center" style="padding:8px 0 32px;">
    <a href="https://hardlifeapparelco.com/about" style="display:inline-block;border:2px solid #ffffff;color:#ffffff;font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:2px;padding:14px 40px;text-decoration:none;">READ THE ORIGIN STORY &rarr;</a>
  </td></tr>
  </table>

  <!-- Social Links -->
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0A0A0A;padding:20px;margin:0 0 24px;">
  <tr><td style="padding:20px;">
    <p style="font-size:9px;letter-spacing:3px;color:#555555;text-transform:uppercase;margin:0 0 12px;">STAY CONNECTED</p>
    <p style="font-size:13px;color:#999999;line-height:2;margin:0;">
      <a href="https://instagram.com/hardlifeapparelco" style="color:#999999;text-decoration:none;">Instagram: @hardlifeapparelco</a><br>
      <a href="https://x.com/HardLifeApparel" style="color:#999999;text-decoration:none;">X: @HardLifeApparel</a><br>
      <a href="https://hardlifeapparelco.com/hardwired-weekly/" style="color:#999999;text-decoration:none;">Hardwired Weekly &rarr; Free every Thursday</a>
    </p>
  </td></tr>
  </table>

  <p style="font-size:14px;color:#999999;margin:0;">— Brooks<br>
  <span style="font-size:11px;color:#666666;">Founder, Hardlife Apparel Company<br>Philadelphia, 2006</span></p>
</td></tr>

<tr><td style="padding:24px;border-top:1px solid #222222;">
  <p style="font-size:10px;color:#444444;text-align:center;margin:0;">You're receiving this because you made a purchase at hrdlf.com.</p>
</td></tr>

</table>
</td></tr>
</table>
</body>
</html>
```

---

### POST-PURCHASE EMAIL 2: RELATED PRODUCTS
**Timing:** 5 days after `Placed Order`

#### Klaviyo Flow Configuration
- **Time delay:** 5 days after trigger
- **Dynamic product block:** Use Klaviyo's "Product Recommendations" block
- **Logic:** Same collection first, then best-sellers they haven't purchased
- **Fallback products** (if dynamic block unavailable, hardcode these):

| If They Bought | Show These |
|---------------|-----------|
| Any hoodie | Matching longsleeve + tee from same collection |
| Any tee | Hoodie from same collection |
| Any accessory | OG Logo Black Hoodie + NACE Black Hoodie |
| Graffiti Beach | Pink Graffiti Hoodie + Blue Graffiti Hoodie + Graffiti Tee |

#### Subject Line
`Made to go with what you got.`

#### Preview Text
`Same collection. Same quality. Same limited run.`

#### Klaviyo Template HTML

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background:#000000;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#000000;">
<tr><td align="center" style="padding:20px;">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">

<tr><td style="padding:24px 0 20px;text-align:center;">
  <p style="font-size:11px;font-weight:800;letter-spacing:4px;color:#999999;text-transform:uppercase;margin:0;">HARDLIFE APPAREL CO.</p>
</td></tr>

<tr><td style="padding:32px 24px;">
  <p style="font-size:16px;color:#ffffff;line-height:1.7;margin:0 0 20px;">By now you've got your order — or it's close.</p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 24px;">Here's what goes with it. Same collection DNA, same heavyweight quality, same limited-run production.</p>

  <p style="font-size:9px;letter-spacing:3px;color:#555555;text-transform:uppercase;margin:0 0 16px;">FROM THE COLLECTION</p>

  <!-- Product 1: Pink Graffiti Hoodie -->
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0A0A0A;border-top:3px solid #C41E1E;margin:0 0 16px;">
  <tr>
    <td style="width:120px;padding:16px;">
      <a href="https://hrdlf.com/products/pink-graffiti-black-hoodie"><img src="https://imgproxy.fourthwall.com/a03GIc3_VlD1OTiFnQYYbOo-oG8ddLIbLldinxW_kI8/sm:1/enc/e7ugobPUQYKsUPJB/QmQSrQjCrZpnHElL/GTJipmypCLQH4_lf/XVbIGyxRxQKWpG0H/Bm05uvdATyjtoLfa/J_cSzuYDzja9VN_y/_xQ3e8uNkK9qw5fa/koccHtFuajs3Kdoe/7QIEvIxJFqpJiu3j/j50_95kLiEWisrUw/J8bux6yJXeL9VeqC/YkhekzveqixgE34j/Xd26vLMP11eizcCC/z0VfzQ" alt="Pink Graffiti Hoodie" width="100" style="display:block;width:100px;border:0;" /></a>
    </td>
    <td style="padding:16px;">
      <p style="font-size:14px;font-weight:800;color:#ffffff;text-transform:uppercase;margin:0 0 4px;">Pink Graffiti — Black Hoodie</p>
      <p style="font-size:14px;color:#cccccc;margin:0 0 4px;">$75</p>
      <a href="https://hrdlf.com/products/pink-graffiti-black-hoodie" style="font-size:11px;color:#999999;text-decoration:underline;">View &rarr;</a>
    </td>
  </tr>
  </table>

  <!-- Product 2: Blue Graffiti Hoodie -->
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0A0A0A;border-top:3px solid #C41E1E;margin:0 0 16px;">
  <tr>
    <td style="width:120px;padding:16px;">
      <a href="https://hrdlf.com/products/blue-graffiti-black-hoodie"><img src="https://imgproxy.fourthwall.com/pR7VQ2TSC9TxgI0Afg1n-2rQwksN0UrfEeoPGhPeEXo/sm:1/enc/GZeM0EY6ozdipdII/ZEUVYA8_enuG6lNf/8LqrHvqjZ_A-Wr9S/QvxAF5gGzQnmaG95/R5nwmQCbHfLwaaxr/fz1L9-AMwfkG-wPf/0MIasAQtlEgLdrcf/4MzhtUGGCWibHLkz/E-C7Hsl3swKEdeGH/qVTK8DtB9slYHQkA/bqCFYHnMg4SqplLg/TH6TEsU02tHPJ3hE/xSQaGHEoCaLsPUrZ/I3nbFQ" alt="Blue Graffiti Hoodie" width="100" style="display:block;width:100px;border:0;" /></a>
    </td>
    <td style="padding:16px;">
      <p style="font-size:14px;font-weight:800;color:#ffffff;text-transform:uppercase;margin:0 0 4px;">Blue Graffiti — Black Hoodie</p>
      <p style="font-size:14px;color:#cccccc;margin:0 0 4px;">$75</p>
      <a href="https://hrdlf.com/products/blue-graffiti-black-hoodie" style="font-size:11px;color:#999999;text-decoration:underline;">View &rarr;</a>
    </td>
  </tr>
  </table>

  <!-- Product 3: Graffiti Tee -->
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0A0A0A;border-top:3px solid #C41E1E;margin:0 0 24px;">
  <tr>
    <td style="width:120px;padding:16px;">
      <a href="https://hrdlf.com/products/graffiti-black-tee"><img src="https://cdn.fourthwall.com/customizations/sh_edd038df-9387-435f-a5ed-83f673666a43/529efcda-b45c-43d4-98db-a1a434262e38.webp" alt="Graffiti Tee" width="100" style="display:block;width:100px;border:0;" /></a>
    </td>
    <td style="padding:16px;">
      <p style="font-size:14px;font-weight:800;color:#ffffff;text-transform:uppercase;margin:0 0 4px;">Graffiti — Black Tee</p>
      <p style="font-size:14px;color:#cccccc;margin:0 0 4px;">$48</p>
      <a href="https://hrdlf.com/products/graffiti-black-tee" style="font-size:11px;color:#999999;text-decoration:underline;">View &rarr;</a>
    </td>
  </tr>
  </table>

  <table width="100%" cellpadding="0" cellspacing="0">
  <tr><td align="center" style="padding:0 0 24px;">
    <a href="https://hrdlf.com" style="display:inline-block;border:2px solid #ffffff;color:#ffffff;font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:2px;padding:14px 40px;text-decoration:none;">SHOP THE FULL COLLECTION &rarr;</a>
  </td></tr>
  </table>

  <p style="font-size:14px;color:#555555;margin:0;">— HRDLF</p>
</td></tr>

<tr><td style="padding:24px;border-top:1px solid #222222;">
  <p style="font-size:10px;color:#444444;text-align:center;margin:0;">Recommended based on your recent purchase at hrdlf.com.</p>
</td></tr>

</table>
</td></tr>
</table>
</body>
</html>
```

---

### POST-PURCHASE EMAIL 3: COMMUNITY INVITE
**Timing:** 10 days after `Placed Order`

#### Subject Line
`One more thing.`

#### Preview Text
`The brand runs deeper than the product.`

#### Klaviyo Template HTML

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin:0;padding:0;background:#000000;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#000000;">
<tr><td align="center" style="padding:20px;">
<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;">

<tr><td style="padding:24px 0 20px;text-align:center;">
  <p style="font-size:11px;font-weight:800;letter-spacing:4px;color:#999999;text-transform:uppercase;margin:0;">HARDLIFE APPAREL CO.</p>
</td></tr>

<tr><td style="padding:32px 24px;">
  <p style="font-size:16px;color:#ffffff;line-height:1.7;margin:0 0 20px;">You bought the piece. Here's the rest of it.</p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 24px;">HRDLF isn't just an apparel brand. It's an ecosystem:</p>

  <!-- Hardwired Weekly -->
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0A0A0A;margin:0 0 12px;">
  <tr><td style="padding:20px;border-left:3px solid #C41E1E;">
    <p style="font-size:14px;font-weight:800;color:#ffffff;margin:0 0 6px;">HARDWIRED WEEKLY</p>
    <p style="font-size:13px;color:#999999;line-height:1.6;margin:0 0 8px;">Free newsletter every Thursday. Drop access. Brand updates. The story behind the brand.</p>
    <a href="https://hardlifeapparelco.com/hardwired-weekly/" style="font-size:12px;color:#ffffff;text-decoration:underline;">Subscribe free &rarr;</a>
  </td></tr>
  </table>

  <!-- The Archive -->
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0A0A0A;margin:0 0 12px;">
  <tr><td style="padding:20px;border-left:3px solid #C41E1E;">
    <p style="font-size:14px;font-weight:800;color:#ffffff;margin:0 0 6px;">THE ARCHIVE</p>
    <p style="font-size:13px;color:#999999;line-height:1.6;margin:0 0 8px;">The full history. Every collection. The people who built this.</p>
    <a href="https://hardlifeapparelco.com/archive/" style="font-size:12px;color:#ffffff;text-decoration:underline;">Explore &rarr;</a>
  </td></tr>
  </table>

  <!-- HRDLFcoin -->
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0A0A0A;margin:0 0 12px;">
  <tr><td style="padding:20px;border-left:3px solid #C41E1E;">
    <p style="font-size:14px;font-weight:800;color:#ffffff;margin:0 0 6px;">HRDLFCOIN</p>
    <p style="font-size:13px;color:#999999;line-height:1.6;margin:0 0 8px;">The brand on the Solana blockchain. First 100 coin holders go in The Archive permanently.</p>
    <a href="https://hrdlfcoin.com" style="font-size:12px;color:#ffffff;text-decoration:underline;">Learn more &rarr;</a>
  </td></tr>
  </table>

  <!-- Social -->
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#0A0A0A;margin:0 0 24px;">
  <tr><td style="padding:20px;border-left:3px solid #C41E1E;">
    <p style="font-size:14px;font-weight:800;color:#ffffff;margin:0 0 6px;">FOLLOW</p>
    <p style="font-size:13px;color:#999999;line-height:1.8;margin:0;">
      <a href="https://instagram.com/hardlifeapparelco" style="color:#999999;text-decoration:none;">Instagram: @hardlifeapparelco</a><br>
      <a href="https://x.com/HardLifeApparel" style="color:#999999;text-decoration:none;">X: @HardLifeApparel</a>
    </p>
  </td></tr>
  </table>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 24px;">This is the last email in this sequence. You won't hear from us unless there's something worth saying.</p>

  <p style="font-size:14px;color:#cccccc;line-height:1.7;margin:0 0 24px;">If you want first access on every drop, the newsletter is the move. Subscribers get 24-hour early access on every release.</p>

  <table width="100%" cellpadding="0" cellspacing="0">
  <tr><td align="center" style="padding:0 0 24px;">
    <a href="https://hardlifeapparelco.com/hardwired-weekly/" style="display:inline-block;background:#C41E1E;color:#ffffff;font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:2px;padding:14px 40px;text-decoration:none;">GET HARDWIRED &rarr;</a>
  </td></tr>
  </table>

  <p style="font-size:14px;color:#555555;margin:0;">— HRDLF<br>
  <span style="font-size:11px;color:#444444;">Philadelphia. 2006. Still here.</span></p>
</td></tr>

<tr><td style="padding:24px;border-top:1px solid #222222;">
  <p style="font-size:10px;color:#444444;text-align:center;margin:0;">Final post-purchase email. No further automated messages.</p>
</td></tr>

</table>
</td></tr>
</table>
</body>
</html>
```

---

## STEP 4 — SOCIAL COPY

### Instagram Captions

**1. Story-Driven**
```
Venice Beach, 1985.

Graffiti on every wall. Skaters in the empty pools.
The art form that launched a global culture.

The Graffiti Beach Hoodie is HRDLF's most direct tribute
to that era. Rainbow gradient graffiti lettering on premium
heavyweight. A zip-up that starts conversations.

$75. Limited run. No restock.
hrdlf.com — link in bio.

#HRDLF #HardlifeApparel #GraffitiBeach #VeniceBeach
#StreetWear #LimitedDrop #IndependentBrand #Philadelphia
```

**2. Urgency-Driven**
```
Subscriber early access: midnight tonight.
Public drop: April 2nd, 10 AM.

The Graffiti Beach Hoodie.
Limited run. No restock. Since 2006, that's the rule.

Subscribe at hardlifeapparelco.com/hardwired-weekly
for 24-hour early access on every drop.

Shop: hrdlf.com

#HRDLF #GraffitiBeach #LimitedDrop #StreetWear
#NothingAwesomeComesEasy
```

**3. Product-Focused**
```
GRAFFITI BEACH TIE DYE HOODIE

→ Premium heavyweight zip-up
→ Independent Trading Co. base
→ Full rainbow gradient graffiti graphic
→ Available in Black and White
→ S through 2XL
→ $75

The tribute piece. The conversation starter.
The one people stop you for.

hrdlf.com — link in bio.

#HRDLF #HardlifeApparel #Streetwear #Hoodie
#GraffitiBeach #SkateStyle #LimitedRun
```

### X/Twitter Posts (Under 280 Characters)

**1.**
```
Graffiti Beach Hoodie. April 2nd. Limited run.
Subscribers got in at midnight. Everyone else: hrdlf.com
```
(117 chars)

**2.**
```
Venice Beach 1985 → Philadelphia 2026.
The Graffiti Beach Hoodie is live. $75. No restock.
hrdlf.com
```
(104 chars)

**3.**
```
19 years. Same rule. When it's gone, the page comes down.
Graffiti Beach Hoodie → hrdlf.com
```
(93 chars)

### Carousel Post (7 Slides)

```
THE GRAFFITI BEACH HOODIE — THE FULL STORY

Slide 1:
VENICE BEACH. 1985.

Slide 2:
Graffiti on every wall. Skaters in the empty pools.
The era that launched everything we know about street culture.

Slide 3:
The Graffiti Beach Hoodie is HRDLF's most direct tribute
to that moment. "Hard Life Apparel" in bold graffiti
lettering with a full rainbow gradient.

Slide 4:
Premium heavyweight zip-up.
Independent Trading Co. base.
Black or White. S–2XL. $75.

Slide 5:
Limited run. No restock. No second chance.
That's been the policy since 2006.
No exceptions. Not for this. Not for anything.

Slide 6:
Subscribers get 24-hour early access.
Midnight, April 1st. Public drop April 2nd, 10 AM.
hardlifeapparelco.com/hardwired-weekly

Slide 7:
Philadelphia. 2006. Still here.
SHOP NOW → hrdlf.com

---

Caption:
The Graffiti Beach Hoodie. HRDLF's most visually striking piece
and a direct tribute to the Venice Beach era that changed
everything about street culture. Premium heavyweight, full
rainbow gradient graffiti graphic, limited production run.

Subscribers get in first — midnight April 1st.
Public drop April 2nd at 10 AM.

Subscribe free: hardlifeapparelco.com/hardwired-weekly
Shop: hrdlf.com

#HRDLF #HardlifeApparel #GraffitiBeach #VeniceBeach #StreetWear
#LimitedDrop #IndependentBrand #Philadelphia #SkateStyle
#NothingAwesomeComesEasy
```

---

## STEP 5 — SUBJECT LINE SWIPE FILE

### 10 Reusable Formulas for HRDLF Drops

**1. THE BARE ANNOUNCEMENT**
`[Product]. [Date].`
→ `Graffiti Beach Hoodie. April 2nd.`
→ Generic: `[Collection] Drop. [Day].`
Why: No selling. Just information. Mimics how drops are talked about in culture.

**2. THE INSIDER ACCESS**
`You're getting this [time] early.`
→ `You're getting this 24 hours early.`
→ Generic: `Subscribers get in first. Again.`
Expected: 45%+ open rate (exclusivity + curiosity)

**3. THE FINITE STATEMENT**
`[Quantity context]. That's it.`
→ `Limited run. When it's gone, the page comes down.`
→ Generic: `One production run. No restock. No exceptions.`
Why: Specificity creates urgency. Vague scarcity doesn't.

**4. THE POLICY REMINDER**
`Same rule since 2006. [Rule].`
→ `Same rule since 2006. No restocks.`
→ Generic: `19 years. Same policy. Once it sells out, it's gone.`
Why: Heritage + consistency = trust. The rule predates the reader.

**5. THE LAST CHANCE**
`Almost gone. Not coming back.`
→ Exactly as written — reuse verbatim.
→ Generic: `Last ones. Then the page comes down.`
Expected: 50%+ open rate (loss aversion)

**6. THE CURIOSITY GAP**
`We almost didn't [action].`
→ `We almost didn't release this one.`
→ Generic: `This wasn't supposed to drop yet.`
Why: Creates an open loop that can only be resolved by opening.

**7. THE FOUNDER DIRECT**
`Brooks: [Short statement].`
→ `Brooks: The Graffiti Beach is ready.`
→ Generic: `Brooks: This one's different.`
Why: Personal sender + colon signals a real message, not a blast.

**8. THE SOLD-OUT PROOF**
`[Last item] sold out in [time]. This one's next.`
→ `The last hoodie sold out in 3 days. This one's next.`
→ Generic: `[Previous drop] went fast. Here's what's coming.`
Why: Social proof from last drop creates urgency for this one.

**9. THE IDENTITY PLAY**
`For people who [identity statement].`
→ `For people who don't wait for permission.`
→ Generic: `For the ones who showed up first.`
Why: Opening becomes an act of identity, not consumption.

**10. THE NO-SELL SELL**
`No pitch. Just showing you what we made.`
→ `No pitch. Just the Graffiti Beach Hoodie.`
→ Generic: `Here's what we've been working on.`
Why: Anti-marketing framing disarms resistance. Authenticity as strategy.

---

## FLOW SUMMARY — QUICK REFERENCE

### Drop Sequence (Campaign — Manual Send)
| Email | When | Subject | Filter |
|-------|------|---------|--------|
| 1. Early Access | Apr 1, 11:59 PM | A/B/C test 3 variants | All subscribers |
| 2. Drop Day | Apr 2, 9:00 AM | `The Graffiti Beach Hoodie is live.` | Exclude purchasers |
| 3. Last Chance | Manual (you decide) | `Almost gone. Not coming back.` | Exclude purchasers |

### Post-Purchase Flow (Automated)
| Email | Delay | Subject | Notes |
|-------|-------|---------|-------|
| 1. Brand Story | 4 hours | `You're part of something now.` | First-timers only |
| 2. Cross-Sell | 5 days | `Made to go with what you got.` | All buyers |
| 3. Community | 10 days | `One more thing.` | All buyers, final email |

### Action Items Before Launch
- [x] ~~Provide Klaviyo Private API Key~~ — Done (pk_d3b3...)
- [x] ~~Create email templates~~ — 6 templates live in Klaviyo
- [x] ~~Create drop campaigns~~ — 3 campaigns in draft
- [x] ~~Create post-purchase flow~~ — Flow created (TFGkCh), draft
- [ ] **Disable Fourthwall abandoned cart emails** — Manual dashboard step
- [ ] **Fix Fourthwall → Klaviyo order sync** — No Placed Order metric yet
- [ ] **Confirm Graffiti Beach product URLs are live** on hrdlf.com
- [ ] **Decide: hard cap on units (150?) or unlimited with timed "last call"**
- [ ] **Review & approve all 3 campaigns** in Klaviyo dashboard
- [ ] **Change post-purchase flow trigger** to Placed Order (once metric exists)
- [ ] **Set post-purchase flow to LIVE** after trigger is corrected

---

*All templates, campaigns, and flows are live in Klaviyo via API. Campaigns are in DRAFT — review in the Klaviyo dashboard and schedule when ready. Social copy is ready to schedule in Buffer or post directly.*
