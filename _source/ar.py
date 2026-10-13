"""Arabic landing page (/ar/). Imported by build.py.

Targets Arabic searches such as: برنامج رواتب، برنامج رواتب الموظفين، برنامج مسير رواتب،
برنامج رواتب بدون اشتراك، برنامج رواتب بدون انترنت، مكافأة نهاية الخدمة.
Edit the text below, then run build.py.
"""
import html, json, os, shutil

EMAIL = "info@paycoresalarysystem.com"
WA = "96890959084"
WA_LICENSE = "https://wa.me/96890959084?text=" + "%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D8%A7%D9%84%D8%AD%D8%B5%D9%88%D9%84%20%D8%B9%D9%84%D9%89%20%D8%AA%D8%B1%D8%AE%D9%8A%D8%B5%20PayCore"  # مرحبا، أريد الحصول على ترخيص PayCore
WA_DEMO = "https://wa.me/96890959084?text=" + "%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D8%8C%20%D8%A3%D8%B1%D9%8A%D8%AF%20%D8%AD%D8%AC%D8%B2%20%D8%B9%D8%B1%D8%B6%20%D9%85%D8%AC%D8%A7%D9%86%D9%8A%20%D9%84%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D8%AC%20PayCore"  # مرحبا، أريد حجز عرض مجاني لبرنامج PayCore

TITLE = "برنامج رواتب الموظفين بدون اشتراك شهري | PayCore"
DESC = ("برنامج رواتب للويندوز يعمل بدون إنترنت. شراء لمرة واحدة لعدد غير محدود من الموظفين، "
        "مع قسائم الرواتب والسلف ومكافأة نهاية الخدمة وواجهة عربية كاملة.")

FEATURES = [
 ("سجل الموظفين", "بيانات كل موظف وتاريخ التعيين والقسم وهيكل الراتب، بما في ذلك بدل السكن والنقل وأي بدلات إضافية تحددها."),
 ("مسير الرواتب الشهري", "يحسب العمل الإضافي والمكافآت والإجازات غير المدفوعة والضرائب تلقائيًا. راجع الأرقام واعتمد مسير الشهر في دقائق."),
 ("السلف والقروض", "اصرف السلف والقروض للموظفين ويُخصم القسط تلقائيًا من الراتب كل شهر، مع إمكانية الإيقاف المؤقت أو تسجيل سداد إضافي."),
 ("قسائم الرواتب والتقارير", "قسائم رواتب بصيغة PDF تحمل بيانات شركتك، وتقارير رواتب شهرية مع تصدير إلى Excel للمحاسب أو البنك."),
 ("مكافأة نهاية الخدمة ونظام حماية الأجور", "احسب مكافأة نهاية الخدمة بالنسبة التي تحددها، وحدد مبلغ التحويل البنكي لكل موظف وفق نظام حماية الأجور (WPS)."),
 ("متابعة انتهاء الوثائق", "احفظ السجلات التجارية والإقامات والهويات ووثائق التأمين في مكان واحد، مع تذكيرات على لوحة التحكم قبل انتهاء صلاحيتها."),
]

COMPARE = [
 ("السعر", "ترخيص لمرة واحدة", "اشتراك شهري أو سنوي"),
 ("التكلفة مع زيادة الموظفين", "ثابتة لا تتغير", "تزيد مع كل موظف جديد"),
 ("مكان حفظ البيانات", "جهازك الخاص", "خوادم الشركة المزوّدة"),
 ("الاتصال بالإنترنت", "غير مطلوب", "مطلوب"),
 ("الواجهة العربية", "متوفرة بالكامل", "تختلف حسب المزوّد"),
 ("ميزات مخصصة لشركتك", "متاحة عند الطلب", "نادرًا ما تتوفر"),
]

FAQ = [
 ("هل يوجد برنامج رواتب بدون اشتراك شهري؟", "نعم. PayCore يُباع بترخيص لمرة واحدة، بدون اشتراك وبدون تجديد وبدون أي رسوم لكل موظف."),
 ("هل يعمل برنامج الرواتب بدون إنترنت؟", "نعم. مسير الرواتب والتقارير والنسخ الاحتياطي وتفعيل الترخيص كلها تعمل بدون إنترنت. فقط المساعد الذكي الاختياري يحتاج إلى الإنترنت."),
 ("هل يدعم البرنامج اللغة العربية؟", "نعم. يحتوي PayCore على واجهة عربية كاملة، ويمكنك التبديل بين العربية والإنجليزية في أي وقت."),
 ("هل يحسب البرنامج مكافأة نهاية الخدمة؟", "نعم. يحسب PayCore مكافأة نهاية الخدمة بالنسبة التي تحددها في الإعدادات. ننصحك بمراجعة النسبة بما يتوافق مع نظام العمل في بلدك."),
 ("هل يمكنني تجربة البرنامج قبل الشراء؟", "نعم. نقدم عرضًا مباشرًا مجانيًا عبر مكالمة فيديو. تواصل معنا عبر واتساب أو البريد الإلكتروني لتحديد موعد."),
 ("هل يمكن نقل البرنامج إلى جهاز جديد؟", "نعم. ثبّت PayCore على الجهاز الجديد وفعّله بنفس البريد الإلكتروني ومفتاح الترخيص، ثم استعد بياناتك من النسخة الاحتياطية."),
 ("هل بياناتي آمنة؟", "بيانات الرواتب تبقى على جهازك ولا تُرسل إلينا. الاستثناء الوحيد هو المساعد الذكي الاختياري: عند تفعيله تُرسل سجلات الرواتب إلى Google مع كل سؤال. الدخول محمي برمز PIN، وملفات النسخ الاحتياطي غير مشفرة لذا احفظها في مكان آمن."),
]

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>'
CROSS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M7 7l10 10M17 7 7 17"/></svg>'
DLICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12m0 0 5-5m-5 5-5-5M4 20h16"/></svg>'
MARK = '<span class="mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"><circle cx="9" cy="9" r="5.5"/><circle cx="15" cy="15" r="5.5"/></svg></span>'
ICONS = [
 '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.8-3.6 3.4-5.5 6.5-5.5s5.7 1.9 6.5 5.5M16 4.5a3.5 3.5 0 0 1 0 7M18.5 14.8c1.6.8 2.6 2.5 3 5.2"/>',
 '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h4"/>',
 '<path d="M3 10 12 4l9 6M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
 '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
 '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h4"/>',
 '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
]
GRADS = ["g1", "g2", "g3", "g4", "g5", "g6"]

CSS = """
:root{color-scheme:light;--bg:#f6f8ff;--ink:#0d1a33;--muted:#4b5a74;--line:#dfe6f3;--card:#fff;--blue:#1d4ed8;--mint:#047857;
--grad:linear-gradient(245deg,#2563eb 0%,#0ea5e9 45%,#10b981 100%);
--f-display:"Cairo","Segoe UI",Tahoma,sans-serif;--f-body:"IBM Plex Sans Arabic","Segoe UI",Tahoma,sans-serif;--r:20px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:400 18px/1.8 var(--f-body);overflow-x:hidden}
a{color:var(--blue)}:focus-visible{outline:3px solid var(--blue);outline-offset:3px;border-radius:8px}
.wrap{max-width:1160px;margin:0 auto;padding-inline:20px;position:relative}
h1,h2,h3{font-family:var(--f-display);line-height:1.3;margin:0;text-wrap:balance}
h2{font-size:clamp(28px,4vw,42px);font-weight:800}h3{font-size:20px;font-weight:800}
p{margin:0}.lede{color:var(--muted);font-size:19px;max-width:62ch}
.grad{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.btn{display:inline-flex;align-items:center;gap:10px;padding:14px 24px;border-radius:999px;font:700 17px/1 var(--f-body);text-decoration:none;border:0;cursor:pointer;transition:transform .2s,box-shadow .2s}
.btn svg{width:18px;height:18px}.btn:hover{transform:translateY(-2px)}
.btn-primary{background:var(--grad);color:#fff;box-shadow:0 10px 30px -10px rgba(37,99,235,.55)}
.btn-soft{background:#fff;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line)}
.btn-wa{background:linear-gradient(140deg,#0f9f5a,#22c55e);color:#fff}
.nav{position:sticky;top:0;z-index:20;padding-block:14px}
.nav-in{display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.85);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid var(--line);border-radius:999px;padding:8px 18px 8px 8px}
.brand{display:flex;align-items:center;gap:10px;font:800 21px/1 var(--f-display);color:var(--ink);text-decoration:none}
.mark{width:34px;height:34px;border-radius:10px;background:var(--grad);display:grid;place-items:center}.mark svg{width:19px;height:19px}
.nav ul{display:flex;gap:2px;list-style:none;margin:0 auto 0 0;padding:0}
.nav ul a{color:var(--muted);text-decoration:none;font-weight:600;font-size:16px;padding:8px 12px;border-radius:999px}
.nav ul a:hover{background:#eef3ff;color:var(--blue)}
.nav .btn{padding:10px 18px;font-size:15px}
@media (max-width:820px){.nav ul{display:none}.nav-in{justify-content:space-between}}
.hero{position:relative;padding-block:40px 30px;overflow:hidden}
.hero::before{content:"";position:absolute;inset:-200px -100px auto;height:700px;z-index:-1;background:radial-gradient(500px 400px at 85% 30%,rgba(147,197,253,.55),transparent 70%),radial-gradient(500px 400px at 10% 40%,rgba(110,231,183,.45),transparent 70%),radial-gradient(400px 300px at 50% 0%,rgba(165,243,252,.5),transparent 70%)}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-weight:700;font-size:14px;color:var(--blue);background:#e8efff;border:1px solid #d3e0ff;padding:7px 14px;border-radius:999px}
.hero h1{font-size:clamp(38px,6vw,68px);font-weight:900;margin-top:18px;line-height:1.2}
.hero .lede{margin-top:20px}
.acts{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}
.pills{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.pills span{display:inline-flex;align-items:center;gap:7px;background:#fff;border:1px solid var(--line);padding:7px 14px;border-radius:999px;font-size:15px;font-weight:600}
.pills svg{width:15px;height:15px;color:var(--mint)}
.shot{margin-top:46px;border-radius:18px;background:#fff;padding:10px;box-shadow:0 40px 90px -40px rgba(37,99,235,.45),0 0 0 1px var(--line)}
.shot img{display:block;width:100%;height:auto;border-radius:10px}
section{padding-block:80px}.head{display:grid;gap:14px;margin-bottom:40px;max-width:760px}
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
@media (max-width:900px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:600px){.grid{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:26px;display:grid;gap:10px;align-content:start;transition:transform .3s,box-shadow .3s}
.card:hover{transform:translateY(-5px);box-shadow:0 26px 50px -30px rgba(37,99,235,.45)}
.card p{color:var(--muted);font-size:16.5px}
.ic{width:50px;height:50px;border-radius:14px;display:grid;place-items:center;color:#fff}.ic svg{width:25px;height:25px}
.g1{background:linear-gradient(135deg,#2563eb,#60a5fa)}.g2{background:linear-gradient(135deg,#0ea5e9,#67e8f9)}.g3{background:linear-gradient(135deg,#10b981,#6ee7b7)}
.g4{background:linear-gradient(135deg,#f59e0b,#fcd34d)}.g5{background:linear-gradient(135deg,#6366f1,#a5b4fc)}.g6{background:linear-gradient(135deg,#f43f5e,#fda4af)}
.cmp{background:#fff;border:1px solid var(--line);border-radius:24px;overflow:hidden}
.row{display:grid;grid-template-columns:1.1fr 1fr 1fr;border-top:1px solid var(--line)}.row:first-child{border-top:0}
.row>span{padding:16px 20px;display:flex;align-items:center;gap:10px;min-width:0}
.row .k{font-weight:700}.row .p{background:linear-gradient(180deg,rgba(37,99,235,.06),rgba(16,185,129,.06));font-weight:600}.row .s{color:var(--muted)}
.row i{flex:none;width:26px;height:26px;border-radius:50%;display:grid;place-items:center}.row i svg{width:14px;height:14px}
.row i.y{background:#d1fae5;color:#047857}.row i.n{background:#f1f5f9;color:#64748b}
.hrow>span{font-weight:800;font-family:var(--f-display)}
@media (max-width:700px){.row{grid-template-columns:1fr 1fr}.row .k{grid-column:1/-1;padding-bottom:0;color:var(--muted);font-size:15px}.hrow .k{display:none}.row>span{padding:12px 14px;font-size:16px}}
.checks{list-style:none;padding:0;margin:24px 0 0;display:grid;gap:14px}
.checks li{display:grid;grid-template-columns:30px 1fr;gap:10px;color:var(--muted)}
.checks li i{width:30px;height:30px;border-radius:9px;background:#ecfdf5;color:var(--mint);display:grid;place-items:center}.checks li i svg{width:16px;height:16px}
.checks b{color:var(--ink)}
#download{background:linear-gradient(180deg,#eef4ff,#f6f8ff);border-block:1px solid var(--line)}
.dl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}@media (max-width:760px){.dl{grid-template-columns:1fr}}
.dl .card{gap:12px}.tag{justify-self:start;font-size:13px;font-weight:700;padding:5px 12px;border-radius:999px;background:#e8efff;color:#1d4ed8}
.file{direction:ltr;text-align:right;font-family:Consolas,monospace;font-size:14px;color:var(--muted);word-break:break-all}
.note{margin-top:22px;background:#fffbeb;border:1px solid #fde68a;color:#6b4a0c;border-radius:var(--r);padding:18px 22px;font-size:16px}
.steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}@media (max-width:860px){.steps{grid-template-columns:1fr}}
.n{width:44px;height:44px;border-radius:50%;display:grid;place-items:center;font:800 19px/1 var(--f-display);color:#fff;background:var(--grad)}
.contact{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin-top:30px}@media (max-width:760px){.contact{grid-template-columns:1fr}}
.cc{border-radius:24px;padding:28px;color:#fff;display:grid;gap:10px;align-content:start}
.cc.wa{background:linear-gradient(140deg,#0f9f5a,#22c55e)}.cc.em{background:linear-gradient(140deg,#1d4ed8,#0ea5e9)}
.cc .val{direction:ltr;text-align:right;font:800 clamp(19px,3vw,28px)/1.3 var(--f-display);overflow-wrap:anywhere}
.cc .btn{background:#fff;color:var(--ink);justify-self:start;padding:11px 20px;font-size:16px}
.demo{margin-top:30px;border-radius:24px;padding:2px;background:var(--grad)}
.demo-in{background:#fff;border-radius:22px;padding:30px;display:flex;flex-wrap:wrap;gap:20px;align-items:center;justify-content:space-between}
.demo-in p{color:var(--muted);max-width:60ch;margin-top:6px}
.faq{display:grid;gap:10px;max-width:860px}
.faq details{background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px 20px}
.faq summary{cursor:pointer;font-weight:700;list-style:none;display:flex;justify-content:space-between;gap:16px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";flex:none;width:28px;height:28px;border-radius:50%;background:#eef4ff;color:var(--blue);display:grid;place-items:center;font-weight:700}
.faq details[open] summary::after{content:"−"}
.faq details p{color:var(--muted);margin-top:8px;font-size:16.5px}
.final{border-radius:32px;padding:50px 30px;text-align:center;background:var(--grad);color:#fff;display:grid;gap:14px;justify-items:center}
.final .btn{background:#fff;color:var(--blue)}
footer{padding-block:36px;color:var(--muted);font-size:15px}
footer .wrap{display:flex;flex-wrap:wrap;gap:12px 24px;justify-content:space-between;border-top:1px solid var(--line);padding-top:24px}
footer a{color:var(--ink);font-weight:600;text-decoration:none}
.rv{animation:up .8s cubic-bezier(.2,.8,.2,1) both}
@keyframes up{from{opacity:0;transform:translateY(18px)}}
@media (prefers-reduced-motion: reduce){*{animation:none!important;transition:none!important}html{scroll-behavior:auto}}
"""


def build(out_dir, site_url, dl_base, setup_name, portable_name, shots_dir, year):
    os.makedirs(os.path.join(out_dir, "ar"), exist_ok=True)
    shutil.copy(os.path.join(shots_dir, "ar-dashboard.jpg"), os.path.join(out_dir, "images", "paycore-arabic-payroll-dashboard.jpg"))
    url = site_url + "ar/"
    e = html.escape
    feats = "".join(f'<div class="card"><span class="ic {GRADS[i]}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[i]}</svg></span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(FEATURES))
    rows = "".join(f'<div class="row" role="row"><span class="k" role="rowheader">{e(k)}</span><span class="p" role="cell"><i class="y">{CHECK}</i>{e(p)}</span><span class="s" role="cell"><i class="n">{CROSS}</i>{e(o)}</span></div>' for k, p, o in COMPARE)
    faqs = "".join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>' for i, (q, a) in enumerate(FAQ))
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "SoftwareApplication", "@id": url + "#app", "name": "PayCore Payroll", "url": url, "inLanguage": "ar",
         "description": DESC, "applicationCategory": "BusinessApplication", "applicationSubCategory": "برنامج رواتب",
         "operatingSystem": "Windows 10, Windows 11", "softwareVersion": "1.0.0",
         "downloadUrl": dl_base + setup_name, "screenshot": site_url + "images/paycore-arabic-payroll-dashboard.jpg",
         "publisher": {"@id": site_url + "#org"}, "isAccessibleForFree": False},
        {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": "ar",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]}

    page = f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(TITLE)}</title>
<meta name="description" content="{e(DESC)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ar" href="{url}">
<link rel="alternate" hreflang="en" href="{site_url}">
<link rel="alternate" hreflang="x-default" href="{site_url}">
<meta name="theme-color" content="#2563eb">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="PayCore">
<meta property="og:locale" content="ar_AR">
<meta property="og:title" content="{e(TITLE)}">
<meta property="og:description" content="{e(DESC)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site_url}og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cairo:wght@700;800;900&family=IBM+Plex+Sans+Arabic:wght@400;600;700&display=swap">
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=1)}
</script>
<style>{CSS}</style>
</head>
<body>
<nav class="nav" aria-label="القائمة الرئيسية"><div class="wrap"><div class="nav-in">
<a class="brand" href="./">{MARK}PayCore</a>
<ul>
<li><a href="#features">المزايا</a></li><li><a href="#compare">المقارنة</a></li><li><a href="#download">التحميل</a></li><li><a href="#license">الترخيص</a></li><li><a href="#faq">الأسئلة الشائعة</a></li>
<li><a href="../" hreflang="en" lang="en">English</a></li>
</ul>
<a class="btn btn-primary" href="#download">تحميل</a>
</div></div></nav>

<header class="hero"><div class="wrap">
<div class="rv">
<span class="eyebrow">برنامج رواتب للويندوز يعمل بدون إنترنت</span>
<h1>برنامج رواتب الموظفين <span class="grad">بدون اشتراك شهري</span></h1>
<p class="lede">يحسب PayCore الرواتب والعمل الإضافي والسلف ومكافأة نهاية الخدمة لجميع موظفيك، ويُصدر قسائم الرواتب بخطوة واحدة. اشترِ الترخيص مرة واحدة واستخدمه لعدد غير محدود من الموظفين.</p>
<div class="acts"><a class="btn btn-primary" href="#download">{DLICON}تحميل للويندوز</a><a class="btn btn-soft" href="{WA_DEMO}" target="_blank" rel="noopener">احجز عرضًا مجانيًا</a></div>
<div class="pills"><span>{CHECK}ترخيص لمرة واحدة</span><span>{CHECK}عدد غير محدود من الموظفين</span><span>{CHECK}واجهة عربية كاملة</span></div>
</div>
<div class="shot rv"><img src="../images/paycore-arabic-payroll-dashboard.jpg" alt="لوحة تحكم برنامج الرواتب PayCore باللغة العربية: قاعدة الرواتب الشهرية وعدد الموظفين والسلف والقروض وتوزيع الرواتب حسب الأقسام" width="1200" height="750"></div>
</div></header>

<main>
<section id="features"><div class="wrap">
<div class="head"><h2>كل ما تحتاجه لإدارة <span class="grad">رواتب موظفيك</span></h2>
<p class="lede">من تسجيل أول موظف حتى إصدار آخر قسيمة راتب، يدير PayCore دورة الرواتب الشهرية كاملة للشركات الصغيرة والمتوسطة.</p></div>
<div class="grid">{feats}</div>
<div style="margin-top:56px;max-width:760px">
<h2>بيانات الرواتب <span class="grad">تبقى تحت سيطرتك</span></h2>
<ul class="checks">
<li><i>{CHECK}</i><span><b>يعمل بدون إنترنت.</b> جميع بيانات الرواتب محفوظة على جهازك، بدون حساب سحابي.</span></li>
<li><i>{CHECK}</i><span><b>دخول محمي.</b> قفل برمز PIN يحمي معلومات الرواتب حتى على جهاز مكتب مشترك.</span></li>
<li><i>{CHECK}</i><span><b>نسخ احتياطي واستعادة.</b> احفظ نسخة احتياطية في أي مجلد أو ذاكرة USB واستعدها على أي جهاز. ملفات النسخ غير مشفرة، لذا احفظها في مكان آمن.</span></li>
<li><i>{CHECK}</i><span><b>أي عملة.</b> الريال العماني والدينار الكويتي والبحريني بثلاث خانات عشرية، والدرهم والريال السعودي والقطري وأي عملة أخرى.</span></li>
</ul></div>
</div></section>

<section id="compare" style="padding-top:20px"><div class="wrap">
<div class="head"><h2>شراء لمرة واحدة مقابل <span class="grad">برامج الرواتب بالاشتراك</span></h2>
<p class="lede">برامج الرواتب السحابية تتقاضى رسومًا عن كل موظف كل شهر. هذه مقارنة سريعة.</p></div>
<div class="cmp" role="table" aria-label="مقارنة PayCore مع برامج الرواتب بالاشتراك">
<div class="row hrow" role="row"><span class="k" role="columnheader">الميزة</span><span class="p" role="columnheader">PayCore</span><span class="s" role="columnheader">برامج الاشتراك</span></div>
{rows}
</div></div></section>

<section id="download"><div class="wrap">
<div class="head"><h2>تحميل برنامج PayCore <span class="grad">للويندوز</span></h2>
<p class="lede">اختر ملف التثبيت للاستخدام المعتاد، أو النسخة المحمولة لتشغيل البرنامج من ذاكرة USB بدون تثبيت. يطلب البرنامج مفتاح الترخيص عند تشغيله أول مرة.</p></div>
<div class="dl">
<div class="card"><span class="tag">موصى به</span><h3>ملف التثبيت</h3><p>تثبيت عادي على ويندوز مع اختصار على سطح المكتب وقائمة ابدأ.</p><span class="file">{e(setup_name)} · 123 MB</span><a class="btn btn-primary" href="{dl_base}{setup_name}">{DLICON}تحميل ملف التثبيت</a></div>
<div class="card"><span class="tag" style="background:#ecfdf5;color:#047857">بدون تثبيت</span><h3>النسخة المحمولة</h3><p>ملف واحد يعمل مباشرة بدون تثبيت، مناسب لذاكرة USB وأجهزة المكاتب.</p><span class="file">{e(portable_name)} · 123 MB</span><a class="btn btn-soft" href="{dl_base}{portable_name}">{DLICON}تحميل النسخة المحمولة</a></div>
</div>
<p class="note"><b>متطلبات التشغيل:</b> ويندوز 10 أو 11 (64 بت)، ولا يحتاج إلى إنترنت.<br>عند التشغيل لأول مرة قد يظهر تنبيه «Windows protected your PC» لأن البرنامج غير موقّع بشهادة نشر تجارية. اضغط <b>More info</b> ثم <b>Run anyway</b>. يظهر التنبيه مرة واحدة فقط.</p>
</div></section>

<section id="license"><div class="wrap">
<div class="head"><h2>احصل على <span class="grad">ترخيص PayCore</span></h2>
<p class="lede">تُباع تراخيص PayCore مباشرة من فريقنا. تواصل معنا عبر واتساب أو البريد الإلكتروني، وغالبًا تستلم مفتاح الترخيص في نفس يوم العمل.</p></div>
<div class="steps">
<div class="card"><span class="n">1</span><h3>تواصل مع المبيعات</h3><p>أرسل اسمك واسم شركتك والبريد الإلكتروني الذي سيُسجّل عليه الترخيص.</p></div>
<div class="card"><span class="n">2</span><h3>إتمام الدفع</h3><p>نؤكد لك السعر وطرق الدفع. دفعة واحدة فقط، بدون تجديد أو رسوم لكل موظف.</p></div>
<div class="card"><span class="n">3</span><h3>التفعيل</h3><p>أدخل بريدك الإلكتروني ومفتاح الترخيص في PayCore. التفعيل يعمل بدون إنترنت.</p></div>
</div>
<div class="contact">
<div class="cc wa"><span>واتساب</span><span class="val">+968 9095 9084</span><span>المبيعات والدعم عبر الرسائل فقط، لا تتوفر مكالمات على هذا الرقم.</span><a class="btn" href="{WA_LICENSE}" target="_blank" rel="noopener">تواصل عبر واتساب</a></div>
<div class="cc em"><span>البريد الإلكتروني</span><span class="val">{EMAIL}</span><span>اذكر البريد الإلكتروني الذي تريد تسجيل الترخيص عليه.</span><a class="btn" href="mailto:{EMAIL}">أرسل بريدًا إلكترونيًا</a></div>
</div>
<div class="demo" id="demo"><div class="demo-in"><div><h3>احجز عرضًا مباشرًا مجانيًا</h3><p>شاهد PayCore قبل الشراء. سيعرض لك فريقنا دورة رواتب كاملة عبر مكالمة فيديو، من إضافة الموظفين حتى إصدار قسائم الرواتب، ويجيب عن أسئلتك.</p></div>
<a class="btn btn-wa" href="{WA_DEMO}" target="_blank" rel="noopener">احجز عبر واتساب</a></div></div>
</div></section>

<section id="faq" style="padding-top:20px"><div class="wrap">
<div class="head"><h2>الأسئلة <span class="grad">الشائعة</span></h2></div>
<div class="faq">{faqs}</div>
<div class="final" style="margin-top:70px"><h2>ابدأ مسير رواتبك القادم مع PayCore</h2><p>حمّل البرنامج الآن، أو احجز عرضًا مجانيًا مع فريقنا أولًا.</p>
<div class="acts" style="justify-content:center;margin-top:6px"><a class="btn" href="#download">{DLICON}تحميل للويندوز</a></div></div>
</div></section>
</main>

<footer><div class="wrap">
<span>© {year} PayCore. جميع الحقوق محفوظة.</span>
<span><a href="../" hreflang="en" lang="en">English</a> · <a href="../privacy.html">سياسة الخصوصية (بالإنجليزية)</a> · <a href="../terms.html">شروط الاستخدام (بالإنجليزية)</a> · <a href="https://wa.me/{WA}" target="_blank" rel="noopener">واتساب</a></span>
</div></footer>
</body>
</html>
"""
    with open(os.path.join(out_dir, "ar", "index.html"), "w", encoding="utf-8") as fh:
        fh.write(page)
    return "ar/"
