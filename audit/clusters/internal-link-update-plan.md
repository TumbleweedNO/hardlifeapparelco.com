# INTERNAL LINK UPDATE PLAN

Every change below is a proposed PATCH to an existing WP post. **DO NOT auto-execute.** Review each diff and approve before committing.

Format: Post ID | Slug | Link to add | Where in the post | Anchor text

---

## CLUSTER 1 LINKS (→ /ai-rebuild/ pillar)

| Post ID | Slug | Add Link To | Placement | Anchor Text |
|---------|------|-------------|-----------|-------------|
| 727 | what-is-hardlife-apparel | /ai-rebuild/ | In paragraph about the 2025 rebuild | "rebuilt the entire brand with AI" |
| 727 | what-is-hardlife-apparel | /brand-facts/ | Near "federal trademark" mention | "verified brand facts" |
| 738 | step-by-step-guide-launching-skate-brand-2026 | /ai-rebuild/ | In section about tools/technology | "See the full AI rebuild case study" |
| 738 | step-by-step-guide-launching-skate-brand-2026 | /free-toolkit/ | Near any mention of tools or resources | "free AI toolkit" |
| 895 | streetwear-marketing-workflow | /ai-rebuild/ | In intro or methodology section | "AI-powered brand rebuild" |
| 895 | streetwear-marketing-workflow | /ai-stack/ | Near tools discussion | "the full AI stack" |
| 908 | build-authentic-hype-editorial-storytelling | /ai-rebuild/ | In section about content creation | "rebuilt with AI tools" |

---

## CLUSTER 2 LINKS (→ HRDLFcoin hub post ID 843)

| Post ID | Slug | Add Link To | Placement | Anchor Text |
|---------|------|-------------|-----------|-------------|
| 579 | cracking-hype-cycle-trends-tech | /hrdlfcoin-first-streetwear-solana-token/ | Near any tech/innovation discussion | "HRDLFcoin on Solana" |
| 579 | cracking-hype-cycle-trends-tech | hrdlfcoin.com | Same section | "hrdlfcoin.com" |

Note: The 4 HRDLFcoin series posts (845, 847, 849, 851) were built with internal links already. Verify they all link to hub post 843.

---

## CLUSTER 3 LINKS (→ indie pillar — AFTER it's published)

These links should be added AFTER the "Complete Guide to Independent Streetwear Brands" pillar is published:

| Post ID | Slug | Add Link To | Placement | Anchor Text |
|---------|------|-------------|-----------|-------------|
| 204 | underground-streetwear-brands-you-need-to-know | [indie pillar URL] | In intro paragraph | "complete guide to independent streetwear" |
| 654 | streetwear-label-list-top-independent-brands-2026 | [indie pillar URL] | In intro paragraph | "our full independent streetwear guide" |
| 590 | why-choose-independent-brands-authenticity-style | [indie pillar URL] | In intro or first section | "independent streetwear brands" |
| 378 | what-makes-independent-streetwear-brands-last | [indie pillar URL] | In intro paragraph | "the complete guide" |
| 378 | what-makes-independent-streetwear-brands-last | /19-years-independent/ | Near longevity argument | "19 years independent" |
| 201 | philadelphia-streetwear-scene | [indie pillar URL] | In intro paragraph | "independent streetwear brands guide" |
| 202 | old-english-typography-street-culture | [indie pillar URL] | In intro or HRDLF mention | "independent streetwear guide" |
| 11 | the-origin-story-hardlife-apparel-2006 | [indie pillar URL] | Near brand philosophy section | "independent streetwear" |
| 11 | the-origin-story-hardlife-apparel-2006 | /brand-facts/ | Near founding facts | "brand facts" |
| 865 | streetwear-vs-fast-fashion | [indie pillar URL] | In section comparing independent vs mass | "independent streetwear brands" |
| 754 | top-must-follow-skate-brands | [indie pillar URL] | In intro or conclusion | "independent streetwear guide" |
| 342 | what-makes-brand-authentic | [indie pillar URL] | In authenticity discussion | "independent streetwear brands" |
| 911 | why-local-brands-fuel-streetwear-culture | [indie pillar URL] | In intro paragraph | "independent streetwear" |
| 398 | what-does-it-mean-to-be-core | [indie pillar URL] | In skate culture discussion | "independent streetwear guide" |

---

## CROSS-CLUSTER BRIDGE LINKS

| Post ID | Slug | Add Link To | Placement | Anchor Text |
|---------|------|-------------|-----------|-------------|
| 851 | ai-blockchain-streetwear-rebuild | /ai-rebuild/ | Already exists — VERIFY | "AI rebuild" |
| 851 | ai-blockchain-streetwear-rebuild | HRDLFcoin hub (843) | Already exists — VERIFY | "HRDLFcoin" |
| 849 | 19-year-brand-on-chain | [indie pillar URL] | In heritage section | "independent streetwear" |
| 865 | streetwear-vs-fast-fashion | /ai-rebuild/ | In section about brand alternatives | "rebuilt with AI" |

---

## AUTHORITY PAGE LINKS (add to high-traffic posts)

Add links to authority pages from the top 10 most-trafficked posts (check GSC for actual traffic data — these are estimates based on keyword potential):

| Post ID | Slug | Add Link To | Anchor Text |
|---------|------|-------------|-------------|
| 204 | underground-streetwear-brands | /about/ | "About HRDLF" |
| 654 | streetwear-label-list | /about/brooks-duvall/ | "Brooks Duvall" |
| 758 | heavyweight-cotton-tee-guide | hrdlf.com (product link) | "shop HRDLF tees" |
| 201 | philadelphia-streetwear-scene | /about/ | "About Hardlife Apparel" |
| 843 | hrdlfcoin-hub | /about/brooks-duvall/ | "founder Brooks Duvall" |

---

## EXECUTION STEPS

1. I will fetch each post's current content via `GET /wp/v2/posts/{id}?context=edit`
2. Show you a text diff of the proposed change (old paragraph → new paragraph with link added)
3. You approve or modify
4. I PATCH only the approved changes
5. After all patches: re-verify via live site that links render correctly

**Estimated scope:** ~25 link additions across ~20 posts. One-time operation, ~30 minutes with approval cycle.

---

*No changes will be made without explicit per-post approval.*
