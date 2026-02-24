# HRDLF Content Hub — hardlifeapparelco.com

## Hardlife Apparel Company LTD — SEO Content Hub
**The Original Since 2006**

This is the SEO-optimized content hub for Hardlife Apparel Company LTD, designed to work alongside the Fourthwall e-commerce store at hrdlf.com as a dual-site architecture.

---

## Site Structure

```
hrdlf-site/
├── index.html              # Homepage (main SEO landing page)
├── about.html              # Brand origin story & timeline
├── 404.html                # Custom 404 page
├── CNAME                   # Custom domain config
├── robots.txt              # Search engine directives
├── sitemap.xml             # XML sitemap for Google
├── blog/
│   └── index.html          # Editorial blog index
├── lookbook/
│   └── index.html          # Collection lookbook gallery
├── press/
│   └── index.html          # Press & media resources
└── assets/
    ├── css/
    │   └── style.css       # Complete design system
    ├── js/
    │   └── main.js         # Animations & interactions
    └── images/
        ├── hrdlf-crew-movement.jpg
        ├── hrdlf-hardlife-hoodie-smoke.jpg
        ├── hrdlf-white-hoodie-street.jpg
        ├── hrdlf-greenhouse-beanie.jpg
        ├── hrdlf-bag-cap-street.jpg
        ├── hrdlf-nothing-awesome-comes-easy.png
        └── hrdlf-unfuck-the-world.jpg
```

---

## Deploy to GitHub Pages (Free Hosting)

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Name it `hardlifeapparelco.com` (or any name you prefer)
3. Set to **Public**
4. Click **Create repository**

### Step 2: Push This Code
```bash
cd hrdlf-site
git init
git add .
git commit -m "Initial launch: HRDLF content hub"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/hardlifeapparelco.com.git
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repo → **Settings** → **Pages**
2. Under "Source", select **Deploy from a branch**
3. Branch: **main**, Folder: **/ (root)**
4. Click **Save**

### Step 4: Connect Custom Domain
1. In **Settings** → **Pages** → **Custom domain**
2. Enter: `hardlifeapparelco.com`
3. Click **Save**
4. Check **Enforce HTTPS**

### Step 5: Update DNS Records
In your domain registrar (wherever hardlifeapparelco.com is registered), add these DNS records:

**A Records** (point to GitHub Pages):
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**CNAME Record** (for www subdomain):
```
www  →  YOUR_USERNAME.github.io
```

DNS propagation takes 15 minutes to 48 hours.

### Step 6: Verify in Google Search Console
1. Go to https://search.google.com/search-console
2. Add property: `https://hardlifeapparelco.com`
3. Verify via DNS TXT record or HTML file
4. Submit sitemap: `https://hardlifeapparelco.com/sitemap.xml`

---

## Adding New Blog Posts

To add a new blog post:
1. Create a new folder in `/blog/` with a keyword-rich slug name
   Example: `/blog/the-origin-story-hardlife-apparel-2006/index.html`
2. Copy the HTML structure from an existing blog post
3. Update the title, meta description, meta keywords, canonical URL, and content
4. Add the article to the blog index page (`/blog/index.html`)
5. Add the URL to `sitemap.xml`
6. Commit and push to GitHub

---

## SEO Features Built In

- Custom meta titles and descriptions on every page
- Open Graph tags for social sharing
- Twitter Card tags
- Schema.org JSON-LD structured data (Organization, WebSite, BreadcrumbList, Blog, AboutPage)
- XML Sitemap
- robots.txt
- Semantic HTML5 structure
- Image alt text on all images
- Canonical URLs
- Mobile-responsive design
- Fast static site (no server-side rendering overhead)

---

## Brand Info

- **Brand:** Hardlife Apparel Company LTD (HRDLF)
- **Founded:** 2006
- **Founder:** Brooks Duvall
- **Store:** https://hrdlf.com
- **Content Hub:** https://hardlifeapparelco.com
- **Instagram:** @hardlifeapparelco
- **TikTok:** @hardlifeapparelco
- **Email:** info@hardlifeapparel.com
