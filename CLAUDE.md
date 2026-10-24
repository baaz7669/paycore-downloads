# PayCore Salary System website — handover for Claude Code

This repository is the marketing website **https://paycoresalarysystem.com** for *PayCore Salary System*, an offline Windows payroll app (USD 50 one-time license, unlimited employees, English + Arabic). Hosted on **GitHub Pages** (custom domain via `CNAME`, DNS on Cloudflare). Pushing to `main` publishes the site within 1–2 minutes.

## Who does what (owner's decision)
- **Claude Code (this repo):** website design and development.
- **Claude.ai chat (Project "Payroll application"):** marketing, social posts (Facebook/LinkedIn scheduling), outreach, directory listings, ads. Status notes live in the Project doc `claude/paycore-status.md`.
- **A separate chat:** the PayCore **app** code and builds (exe/appx). **Never edit app code here, and never commit app source or zips** — the app's license secret is in its source.

## Build — never edit the generated HTML in the repo root
All pages are generated. Edit files in `_source/`, then run:

```
pip install pillow   # once
python3 _source/build.py
```

`build.py` writes every live file in the repo root (`index.html`, `ar/`, `gratuity-calculator/`, `salary-calculator/`, `salary-software-guide/`, `privacy.html`, `terms.html`, `404.html`, `sitemap.xml`, `robots.txt`, `llms.txt`, WebP images, IndexNow key file) and `_source/preview.html`. Folders starting with `_` are not published. Commit the source **and** the regenerated output together.

| Source file | Produces / purpose |
|---|---|
| `_source/site-source.html` | English homepage: all text, CSS, animations, JS (hero tilt, reveal-on-scroll with `.rv` / `.pre`, AI box, free-tools section). |
| `_source/build.py` | Main build: SEO head, JSON-LD (Organization, WebSite, SoftwareApplication with `featureList`, FAQPage built from the `<details>` FAQ), sitemap with hreflang, robots, then calls the modules below and injects social buttons into every page. |
| `_source/ar.py` | Arabic homepage `/ar/` (RTL). Text lives in `FEATURES`, `COMPARE`, `FAQ`, `ICONS`, `GRADS`. **The page is a Python f-string: CSS/JS braces must be doubled `{{ }}`.** |
| `_source/guide.py` | Buyer's guide `/salary-software-guide/` and `/ar/salary-software-guide/`; competitor prices checked Oct 2026 (re-check before changing `CHECKED`). Provides the shared `CSS`, `MARK`, `BEACON`, `_faq_html` used by other pages. |
| `_source/gratuity.py` | Free gratuity calculator (EN/AR): Oman, UAE, Saudi Arabia. Its `_page()` is reused by `salarycalc.py`. |
| `_source/salarycalc.py` | Free salary calculator (EN/AR): absence / unpaid-leave deduction, pay for days worked, **hourly pay** (fixed rate, or monthly salary by hours; extra hours at a %). Formulas mirror the app (`calcEmployeeHourlyPay`). |
| `_source/contact_form.py` | Contact form (WhatsApp / email hand-off, nothing stored). |
| `_source/social.py` | LinkedIn / Facebook / WhatsApp buttons (Simple Icons paths). Injected by `build.py` after the other pages are written. |
| `_source/legal.py`, `notfound.py` | Privacy, terms, 404. |
| `_source/llms.txt` | AI-readable summary, copied to the root. Keep it in sync with features and pages. |
| `_source/og-image.html`, `shots/` | Share image source and the app screenshots used on the site. |
| `.github/workflows/indexnow.yml` | On every push, submits all sitemap URLs to IndexNow (Bing, Yandex…). Google indexing is requested manually in Search Console by the owner. |

## Facts and rules for content
- Brand name: always **"PayCore Salary System"** in titles/schema (alternateName PayCore). It must not be confused with the US company **Paycor**. Never add LLC/Ltd.
- Price: **USD 50 one-time, unlimited employees**, no subscription. No free trial — a **free live video demo** instead.
- Contact: WhatsApp **+968 9095 9084** (wa.me/96890959084), **info@paycoresalarysystem.com**.
- Downloads: versionless GitHub release links `releases/latest/download/PayCore-Payroll-Setup.exe` and `PayCore-Payroll-Portable.exe`; recommended route is the **Microsoft Store** (ID 9NMS2FWD82J3, https://apps.microsoft.com/detail/9NMS2FWD82J3). Do not show app version numbers on the site (no `softwareVersion` in schema).
- Do **not** mention Windows/SmartScreen security warnings anywhere.
- The **AI assistant** is optional and uses the customer's own Google Gemini key; whenever it's described, keep the disclosure that questions and payroll records go to Google when it's turned on.
- Social: https://www.facebook.com/paycoresalarysystem and https://www.linkedin.com/company/paycoresalarysystem/ (also in Organization `sameAs`).
- Gratuity rules (sources listed on the page, checked Oct 2026):
  - **Oman** (non-Omanis): service **up to 31 Jul 2023** = previous law (15 days' basic per year for the first 3 years, then a month); **from 1 Aug 2023** = one month's basic per year (Labour Law 53/2023, Art. 61). Ministry example OMR 500 basic, 1 Aug 2021–31 Jul 2026 = OMR 2,000. Expat 9% savings system replaces gratuity once the Social Protection Fund sets a start date (latest 19 Jul 2027) — update the page when announced.
  - **UAE**: 21 days' basic per year for 5 years then 30, 1-year minimum, cap 2 years' wage.
  - **Saudi**: half a month's last wage per year for 5 years then a month; resignation 0 / ⅓ / ⅔ / full at <2 / 2–5 / 5–10 / 10+ years.
- Calculators state they are estimates, not legal advice.

## Things not to touch
- DNS records (MX, TXT, NS) and the owner's other Cloudflare projects.
- `CNAME`, the IndexNow key file `81e5f46776dd0dd067369e919c55b201.txt`, and the Cloudflare Web Analytics beacon token.
- GitHub release assets (the owner uploads the exe files).

## Design system
- Fonts: Bricolage Grotesque (display) + Figtree (body); Arabic: Cairo + IBM Plex Sans Arabic (Google Fonts).
- Brand gradient `#2563eb → #0ea5e9 → #10b981`; ink `#0d1a33`; muted `#4b5a74`; "FREE / NEW" pills `#047857` (kept dark enough for contrast).
- Logo mark: two overlapping circles (see `MARK` in `guide.py`).
- Respect `prefers-reduced-motion`; no horizontal scroll at 360–390 px; every page exists in English and Arabic with reciprocal hreflang.

## Before pushing
1. `python3 _source/build.py`
2. Serve the root (`python3 -m http.server`) and check changed pages in **both languages** at desktop and ~390 px width (no horizontal scroll, no console errors). For calculators, test the worked examples on the page.
3. Optional: Lighthouse — last results: SEO 100, accessibility 100, performance 95–97.
4. Commit and push; check the "pages build and deployment" and IndexNow workflow runs succeed.

## Current state (24 Oct 2026)
- Homepage: features incl. 3 NEW cards (hourly staff payroll, import hours from Excel, leave starting mid-month), compare table, Microsoft Store recommended download, license, animated AI assistant box, "Free payroll calculators" section, FAQ, contact form, social buttons.
- Ideas not done yet: more free tools (e.g. overtime calculator, WPS file checker), Arabic-first landing for Oman, customer reviews section once real reviews exist, demo video embed.
