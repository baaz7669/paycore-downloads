"""Build the PayCore website from site-source.html.

Run from anywhere:  python3 _source/build.py

Outputs:
  _source/preview.html -> single-file preview (images embedded)
  repository root      -> the live site files GitHub Pages serves
"""
import base64, html, json, os, re, shutil, sys

SITE_URL = "https://paycoresalarysystem.com/"   # change here if you move to your own domain
DL = "https://github.com/baaz7669/paycore-downloads/releases/latest/download/"
import datetime
TODAY = datetime.date.today().isoformat()
ROOT = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(ROOT, "shots")

src = open(os.path.join(ROOT, "site-source.html"), encoding="utf-8").read()
sys.path.insert(0, ROOT)
import contact_form
src = src.replace("<!--CONTACT_FORM-->", contact_form.html("en") + "\n" + contact_form.JS) \
         .replace("/* about */", contact_form.CSS + "\n/* about */", 1)

# ---------- artifact preview ----------
art = src
for key, name in [("__DASHBOARD__", "dashboard"), ("__PAYROLL__", "payroll")]:
    b64 = base64.b64encode(open(f"{SHOTS}/{name}.jpg", "rb").read()).decode()
    art = art.replace(key, "data:image/jpeg;base64," + b64)
open(os.path.join(ROOT, "preview.html"), "w", encoding="utf-8").write(art)

# ---------- dist ----------
dist = os.path.dirname(ROOT)  # repository root
os.makedirs(os.path.join(dist, "images"), exist_ok=True)
shutil.copy(f"{SHOTS}/dashboard.jpg", os.path.join(dist, "images", "paycore-payroll-dashboard.jpg"))
shutil.copy(f"{SHOTS}/payroll.jpg", os.path.join(dist, "images", "paycore-monthly-payroll-run.jpg"))
# WebP copies for the pages themselves (smaller); the .jpg files stay for schema, sitemap and sharing
from PIL import Image
for src_name, out_name in [("dashboard", "paycore-payroll-dashboard"), ("payroll", "paycore-monthly-payroll-run"),
                           ("ar-dashboard", "paycore-arabic-payroll-dashboard")]:
    Image.open(f"{SHOTS}/{src_name}.jpg").save(os.path.join(dist, "images", out_name + ".webp"), "WEBP", quality=80, method=6)

page = src.replace("__DASHBOARD__", "images/paycore-payroll-dashboard.webp") \
          .replace("__PAYROLL__", "images/paycore-monthly-payroll-run.webp")

# split off the preview's own title/description; the real head is written below
page = re.sub(r"^<title>.*?</title>\s*", "", page, count=1, flags=re.S)
page = re.sub(r'^<meta name="description"[^>]*>\s*', "", page, count=1)
head_part, body_part = page.split("</style>", 1)

TITLE = "Payroll & Salary Management Software for Windows | PayCore"
DESC = ("Payroll and salary management software for Windows. $50 one-time license, no monthly fees, "
        "unlimited employees. Works offline.")
OG_TITLE = "PayCore: payroll software without the monthly bill"

# FAQ schema built from the page's own FAQ, so the two never disagree
faqs = re.findall(r"<details[^>]*><summary>(.*?)</summary><p>(.*?)</p></details>", body_part, flags=re.S)
def plain(t): return html.unescape(re.sub(r"<[^>]+>", "", t)).strip()

schema = {
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "Organization", "@id": SITE_URL + "#org", "name": "PayCore", "url": SITE_URL,
     "logo": SITE_URL + "apple-touch-icon.png", "email": "info@paycoresalarysystem.com",
     "sameAs": ["https://www.linkedin.com/company/paycoresalarysystem/", "https://apps.microsoft.com/detail/9NMS2FWD82J3"],
     "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "email": "info@paycoresalarysystem.com",
                      "telephone": "+968-9095-9084", "availableLanguage": ["English", "Arabic"]}},
    {"@type": "WebSite", "@id": SITE_URL + "#website", "url": SITE_URL, "name": "PayCore Payroll",
     "inLanguage": "en", "publisher": {"@id": SITE_URL + "#org"}},
    {"@type": "SoftwareApplication", "@id": SITE_URL + "#app",
     "name": "PayCore Payroll",
     "publisher": {"@id": SITE_URL + "#org"},
     "description": DESC,
     "url": SITE_URL,
     "applicationCategory": "BusinessApplication",
     "applicationSubCategory": "Payroll software",
     "operatingSystem": "Windows 10, Windows 11",
     "softwareVersion": "1.0.1",
     "fileSize": "123MB",
     "downloadUrl": DL + "PayCore-Payroll-Setup.exe",
     "installUrl": "https://apps.microsoft.com/detail/9NMS2FWD82J3",
     "inLanguage": ["en", "ar"],
     "screenshot": [SITE_URL + "images/paycore-payroll-dashboard.jpg",
                    SITE_URL + "images/paycore-monthly-payroll-run.jpg"],
     "image": SITE_URL + "og-image.png",
     "featureList": [
        "Monthly payroll processing with overtime, bonuses, unpaid leave and tax",
        "Employee loans and salary advances with automatic installment deduction",
        "PDF payslips, payroll reports and Excel/CSV exports",
        "End-of-service gratuity settlement",
        "WPS bank-transfer rules per employee",
        "Transaction ledger",
        "Document expiry tracker",
        "Optional AI assistant (own Google Gemini key): payroll questions, pre-approval anomaly check, report summaries, letter drafting",
        "Works fully offline with PIN lock and local backup",
        "English and Arabic interface; any currency including OMR, KWD, BHD, AED, SAR and QAR"],
     "isAccessibleForFree": False,
     "offers": {"@type": "Offer", "price": "50", "priceCurrency": "USD",
                "availability": "https://schema.org/InStock", "url": SITE_URL + "#license"}},
    {"@type": "FAQPage", "@id": SITE_URL + "#faq",
     "mainEntity": [{"@type": "Question", "name": plain(q),
                     "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faqs]}
  ]
}

seo_head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(TITLE)}</title>
<meta name="description" content="{html.escape(DESC)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{SITE_URL}">
<link rel="alternate" hreflang="en" href="{SITE_URL}">
<link rel="alternate" hreflang="ar" href="{SITE_URL}ar/">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}">
<meta name="theme-color" content="#2563eb">
<meta name="application-name" content="PayCore Payroll">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">

<meta property="og:type" content="website">
<meta property="og:site_name" content="PayCore Payroll">
<meta property="og:title" content="{html.escape(OG_TITLE)}">
<meta property="og:description" content="{html.escape(DESC)}">
<meta property="og:url" content="{SITE_URL}">
<meta property="og:image" content="{SITE_URL}og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="PayCore Payroll: offline payroll software for Windows with a one-time license">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(OG_TITLE)}">
<meta name="twitter:description" content="{html.escape(DESC)}">
<meta name="twitter:image" content="{SITE_URL}og-image.png">

<link rel="preload" as="image" href="images/paycore-payroll-dashboard.webp" type="image/webp">
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=1)}
</script>
"""

out = seo_head + head_part + "</style>\n</head>\n<body>\n" + body_part.strip() + "\n</body>\n</html>\n"
open(os.path.join(dist, "index.html"), "w", encoding="utf-8").write(out)

sys.path.insert(0, ROOT)
import legal
extra = legal.build(dist, SITE_URL, TODAY[:4])
import ar
ar_path = ar.build(dist, SITE_URL, DL, "PayCore-Payroll-Setup.exe", "PayCore-Payroll-Portable.exe", SHOTS, TODAY[:4])
ALT = (f'    <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}"/>\n'
       f'    <xhtml:link rel="alternate" hreflang="ar" href="{SITE_URL}{ar_path}"/>\n'
       f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE_URL}"/>\n')
import notfound
notfound.build(dist)
import guide
g_en, g_ar = guide.build(dist, SITE_URL, TODAY[:4])
G_ALT = (f'    <xhtml:link rel="alternate" hreflang="en" href="{g_en}"/>\n'
         f'    <xhtml:link rel="alternate" hreflang="ar" href="{g_ar}"/>\n'
         f'    <xhtml:link rel="alternate" hreflang="x-default" href="{g_en}"/>\n')
guide_urls = "".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n{G_ALT}  </url>\n" for u in (g_en, g_ar))
import gratuity
c_en, c_ar = gratuity.build(dist, SITE_URL, TODAY[:4])
C_ALT = G_ALT.replace(g_en, c_en).replace(g_ar, c_ar)
guide_urls += "".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n{C_ALT}  </url>\n" for u in (c_en, c_ar))
import salarycalc
s_en, s_ar = salarycalc.build(dist, SITE_URL, TODAY[:4])
S_ALT = G_ALT.replace(g_en, s_en).replace(g_ar, s_ar)
guide_urls += "".join(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n{S_ALT}  </url>\n" for u in (s_en, s_ar))
extra_urls = "".join(f"  <url>\n    <loc>{SITE_URL}{p}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>\n" for p in extra)

# AI-readable summary (llms.txt) and the IndexNow key file used by .github/workflows/indexnow.yml
shutil.copy(os.path.join(ROOT, "llms.txt"), os.path.join(dist, "llms.txt"))
INDEXNOW_KEY = "81e5f46776dd0dd067369e919c55b201"
open(os.path.join(dist, INDEXNOW_KEY + ".txt"), "w").write(INDEXNOW_KEY)

open(os.path.join(dist, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n")
open(os.path.join(dist, "sitemap.xml"), "w").write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{SITE_URL}</loc>
{ALT}    <lastmod>{TODAY}</lastmod>
    <image:image><image:loc>{SITE_URL}images/paycore-payroll-dashboard.jpg</image:loc></image:image>
    <image:image><image:loc>{SITE_URL}images/paycore-monthly-payroll-run.jpg</image:loc></image:image>
  </url>
  <url>
    <loc>{SITE_URL}{ar_path}</loc>
    <lastmod>{TODAY}</lastmod>
{ALT}    <image:image><image:loc>{SITE_URL}images/paycore-arabic-payroll-dashboard.jpg</image:loc></image:image>
  </url>
{guide_urls}{extra_urls}</urlset>
""")
open(os.path.join(dist, "favicon.svg"), "w").write(
 '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
 '<stop offset="0" stop-color="#2563eb"/><stop offset=".55" stop-color="#0ea5e9"/><stop offset="1" stop-color="#10b981"/></linearGradient></defs>'
 '<rect width="64" height="64" rx="16" fill="url(#g)"/><g fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round">'
 '<circle cx="25" cy="25" r="13"/><circle cx="39" cy="39" r="13"/></g></svg>\n')
print("built", len(faqs), "FAQs into schema")
