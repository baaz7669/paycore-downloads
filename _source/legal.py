"""Privacy policy and terms pages. Imported by build.py.

Edit the text in PAGES below, then run build.py.
"""
import html

UPDATED = "13 October 2026"
EMAIL = "info@paycoresalarysystem.com"
WHATSAPP = "+968 9095 9084"

PAGES = {
 "privacy": {
  "title": "Privacy Policy",
  "desc": "How PayCore handles information on this website, when you contact us, and inside the PayCore payroll app.",
  "body": f"""
<p class="lead">PayCore is payroll software for Windows. This page explains what information we receive, what we don't, and how it is used.</p>

<h2>The short version</h2>
<ul>
<li>The PayCore app stores your payroll data <strong>only on your own computer</strong>. We never receive it.</li>
<li>This website has <strong>no accounts, no cookies and no analytics tracking</strong>.</li>
<li>When you contact us, we use your details only to answer you, issue your license and provide support. We never sell them.</li>
</ul>

<h2>This website</h2>
<p>The website is hosted on GitHub Pages. Like any web host, GitHub may record technical information such as your IP address for security and reliability. See the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub Privacy Statement</a>.</p>
<p>The page loads its fonts from Google Fonts, so your browser connects to Google's servers, which receive your IP address. See the <a href="https://policies.google.com/privacy" rel="noopener">Google Privacy Policy</a>.</p>
<p>The PayCore download files are delivered from GitHub.</p>

<h2>When you contact us</h2>
<p>If you message us on WhatsApp or by email, we receive the details you send, such as your name, company name, email address, phone number and your messages. We use them to:</p>
<ul>
<li>answer your questions and arrange demos,</li>
<li>issue and re-send your license key, which is registered to your email address,</li>
<li>provide support and prepare quotes for custom work.</li>
</ul>
<p>We keep license records for as long as your license is in use, so we can re-send your key if you lose it. You can ask us to delete your details at any time by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>Inside the PayCore app</h2>
<ul>
<li><strong>Payroll data:</strong> Employee records, salaries, loans, payslips and every other record you enter are stored on the computer where PayCore is installed. They are not sent to us or to any cloud service.</li>
<li><strong>Activation:</strong> License activation works offline. Your email and key are checked on your computer.</li>
<li><strong>Backups:</strong> Backup files are created only when you choose to make them, and are saved where you choose. They are not encrypted, so store them securely.</li>
<li><strong>Optional AI assistant:</strong> The AI assistant is off unless you turn it on with your own Google Gemini API key. When it is on, each question you ask is sent to Google together with your PayCore records (employees, salaries, loans, transactions and company details) so it can answer, under <a href="https://ai.google.dev/gemini-api/terms" rel="noopener">Google's Gemini API terms</a>. If you don't turn it on, nothing is sent.</li>
</ul>

<h2>Changes</h2>
<p>If this policy changes, we will update this page and the date below.</p>

<h2>Contact</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or message us on WhatsApp at {WHATSAPP}.</p>
"""},
 "terms": {
  "title": "Terms of Use",
  "desc": "The terms for using PayCore payroll software and your PayCore license.",
  "body": f"""
<p class="lead">These terms apply when you download, activate or use PayCore payroll software. By using PayCore you agree to them.</p>

<h2>Your license</h2>
<ul>
<li>A PayCore license is a <strong>one-time purchase</strong>. There is no subscription and no charge per employee.</li>
<li>Your license key is registered to the email address you give us, and is for use by your own business.</li>
<li>You can reinstall PayCore or move it to a new computer and activate it with the same email and key.</li>
<li>You may not share your license key publicly, resell it, or modify, copy or reverse-engineer the software.</li>
</ul>

<h2>Your payroll responsibilities</h2>
<p>PayCore calculates payroll from the employees, salaries, rates and settings you enter. You are responsible for checking that your payroll, including tax, social insurance, end-of-service gratuity and bank transfer (WPS) amounts, meets the laws that apply to your business. PayCore is a tool, not legal, tax or accounting advice.</p>

<h2>Your data and backups</h2>
<p>Your payroll data stays on your computer and we never have a copy, so we cannot recover it for you. Make regular backups and store them safely.</p>

<h2>Payments and refunds</h2>
<p>Pricing and payment options are confirmed with you before you buy. A free live demo is available so you can see PayCore before purchasing. If PayCore does not run on your computer after purchase, contact us and we will help, or discuss a refund.</p>

<h2>Updates and custom work</h2>
<p>We may release updates to PayCore from time to time. Custom features built for your business are quoted and agreed separately.</p>

<h2>No warranty and limitation of liability</h2>
<p>PayCore is provided "as is". To the extent the law allows, we make no warranties about the software, and our total liability for any claim relating to PayCore is limited to the amount you paid for your license.</p>

<h2>Changes</h2>
<p>We may update these terms. The current version is always on this page, with the date below.</p>

<h2>Contact</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or message us on WhatsApp at {WHATSAPP}.</p>
"""},
}

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | PayCore</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Figtree:wght@400;600;700&display=swap">
<style>
:root{{color-scheme:light;--bg:#f6f8ff;--ink:#0d1a33;--muted:#53627c;--line:#dfe6f3;--blue:#1d4ed8;--grad:linear-gradient(115deg,#2563eb,#0ea5e9 45%,#10b981)}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.7 "Figtree","Segoe UI",system-ui,sans-serif}}
a{{color:var(--blue)}}
.wrap{{max-width:760px;margin:0 auto;padding-inline:20px}}
header{{padding-block:20px}}
.top{{display:flex;justify-content:space-between;align-items:center;gap:16px;background:#fff;border:1px solid var(--line);border-radius:999px;padding:8px 8px 8px 16px}}
.brand{{display:flex;align-items:center;gap:10px;font:800 20px/1 "Bricolage Grotesque","Segoe UI",sans-serif;color:var(--ink);text-decoration:none}}
.mark{{width:32px;height:32px;border-radius:10px;background:var(--grad);display:grid;place-items:center}}
.back{{font-weight:700;font-size:15px;text-decoration:none;background:var(--grad);color:#fff;padding:10px 16px;border-radius:999px}}
main{{background:#fff;border:1px solid var(--line);border-radius:24px;padding:40px;margin-block:20px 40px}}
@media (max-width:600px){{main{{padding:26px 20px}}}}
h1{{font:800 clamp(32px,6vw,44px)/1.1 "Bricolage Grotesque","Segoe UI",sans-serif;letter-spacing:-.03em;margin:0 0 6px}}
.updated{{color:var(--muted);font-size:14px;margin:0 0 24px}}
.lead{{font-size:19px;color:var(--muted)}}
h2{{font:800 22px/1.25 "Bricolage Grotesque","Segoe UI",sans-serif;margin:32px 0 8px}}
ul{{padding-left:22px}} li{{margin-block:6px}}
footer{{color:var(--muted);font-size:14px;padding-bottom:40px;display:flex;flex-wrap:wrap;gap:10px 24px;justify-content:space-between}}
footer a{{color:var(--ink);font-weight:600;text-decoration:none}}
</style>
</head>
<body>
<header><div class="wrap"><div class="top">
<a class="brand" href="./"><span class="mark" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"><circle cx="9" cy="9" r="5.5"/><circle cx="15" cy="15" r="5.5"/></svg></span>PayCore</a>
<a class="back" href="./">Back to home</a>
</div></div></header>
<div class="wrap">
<main>
<h1>{title}</h1>
<p class="updated">Last updated: {updated}</p>
{body}
</main>
<footer><span>© {year} PayCore. All rights reserved.</span><span><a href="./">Home</a> · <a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a></span></footer>
</div>
</body>
</html>
"""


def build(out_dir, site_url, year):
    for slug, p in PAGES.items():
        page = TEMPLATE.format(title=html.escape(p["title"]), desc=html.escape(p["desc"]),
                               url=f"{site_url}{slug}.html", updated=UPDATED, body=p["body"].strip(), year=year)
        with open(f"{out_dir}/{slug}.html", "w", encoding="utf-8") as fh:
            fh.write(page)
    return [f"{slug}.html" for slug in PAGES]
