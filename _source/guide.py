"""Buyer's guide pages: how to choose salary software for a small business.

  /salary-software-guide/      (English)
  /ar/salary-software-guide/   (Arabic)

Targets "best salary software", "salary software for small business", "payroll software
comparison" and the Arabic equivalents, without stuffing those phrases into the homepage.
Prices were checked on 2026-10-14; re-check them before changing CHECKED.
Edit the text below, then run build.py.
"""
import html, json, os

CHECKED = "October 2026"
CHECKED_AR = "أكتوبر 2026"
EMAIL = "info@paycoresalarysystem.com"
AED_PER_USD = 3.6725  # AED is pegged to the US dollar

# 20-employee example, using each vendor's published pricing (see SOURCES)
ZOHO_MONTH_AED = 35 + 15 * 7          # Standard, billed annually: AED 35 incl. 5 staff + AED 7 each
ZOHO_YEAR_USD = round(ZOHO_MONTH_AED * 12 / AED_PER_USD)
GREYTHR_MONTH = 50 + 10 * 2           # Essential: $50 incl. 10 staff + $2 each
GUSTO_MONTH = 49 + 20 * 6             # Simple: $49 base + $6 per person (US only)

ROWS = [  # name, how it's priced, cost per year, cost over 3 years
 ("Zoho Payroll (UAE, Standard)", "AED 35/month for 5 employees, then AED 7 per employee", f"about ${ZOHO_YEAR_USD:,}", f"about ${ZOHO_YEAR_USD*3:,}"),
 ("greytHR (Middle East, Essential)", "$50/month for 10 employees, then $2 per employee", f"${GREYTHR_MONTH*12:,}", f"${GREYTHR_MONTH*36:,}"),
 ("Gusto (US only, Simple)", "$49/month plus $6 per employee", f"${GUSTO_MONTH*12:,}", f"${GUSTO_MONTH*36:,}"),
 ("PayCore (Windows, one-time)", "One-time license", "$50 in the first year", "$50"),
]
ROWS_AR = [
 ("Zoho Payroll (الإمارات، الباقة الأساسية)", "35 درهمًا شهريًا لـ 5 موظفين، ثم 7 دراهم لكل موظف", f"حوالي {ZOHO_MONTH_AED*12:,} درهم", f"حوالي {ZOHO_MONTH_AED*36:,} درهم"),
 ("greytHR (الشرق الأوسط، Essential)", "50 دولارًا شهريًا لـ 10 موظفين، ثم دولاران لكل موظف", f"{GREYTHR_MONTH*12:,} دولار", f"{GREYTHR_MONTH*36:,} دولار"),
 ("Gusto (الولايات المتحدة فقط)", "49 دولارًا شهريًا + 6 دولارات لكل موظف", f"{GUSTO_MONTH*12:,} دولار", f"{GUSTO_MONTH*36:,} دولار"),
 ("PayCore (ويندوز، لمرة واحدة)", "ترخيص لمرة واحدة", "50 دولارًا في السنة الأولى", "50 دولارًا"),
]

SOURCES = [
 ("Zoho: Payroll software for small businesses, pricing and options (UAE)", "https://www.zoho.com/en-ae/payroll/academy/payroll-operations/payroll-software-pricing.html"),
 ("greytHR: HR and payroll software pricing for the Middle East", "https://www.greythr.com/middle-east/pricing/"),
 ("CostBench: Gusto pricing", "https://costbench.com/software/hr/gusto"),
]

FAQ_EN = [
 ("What is the best salary software for a small business?",
  "There isn't one best tool for everyone. The best choice is the one that covers your monthly payroll steps, stays affordable as you hire, and keeps your data where you're comfortable. Cloud tools suit teams that need access from several places; a desktop tool like PayCore suits an office that runs payroll on one computer and doesn't want a monthly bill."),
 ("Is there free salary software?",
  "Excel templates are free, and most paid tools offer a free trial or demo. Fully free payroll software is rare and usually limited to very small teams or basic features. Check what happens to your data and price once you pass the free limit."),
 ("Is Excel enough for payroll?",
  "For a handful of staff with fixed salaries, Excel can work. It gets risky once you add overtime, unpaid leave, loans or end-of-service, because every formula is maintained by hand and one broken cell changes someone's pay. Payroll software does those calculations the same way every month and keeps a history."),
 ("What does salary software cost?",
  f"Subscription tools usually charge a monthly base fee plus a fee per employee. For 20 employees, the published prices we checked in {CHECKED} range from roughly ${ZOHO_YEAR_USD:,} to ${GUSTO_MONTH*12:,} a year. One-time desktop software is paid once instead."),
]
FAQ_AR = [
 ("ما هو أفضل برنامج رواتب للشركات الصغيرة؟",
  "لا يوجد برنامج واحد هو الأفضل للجميع. الخيار الأفضل هو الذي يغطي خطوات الرواتب الشهرية في شركتك، ويبقى بتكلفة مناسبة مع زيادة عدد الموظفين، ويحفظ بياناتك في المكان الذي ترتاح له. البرامج السحابية تناسب الفرق التي تحتاج الوصول من عدة أماكن، وبرنامج مكتبي مثل PayCore يناسب مكتبًا يدير الرواتب من جهاز واحد ولا يريد فاتورة شهرية."),
 ("هل يوجد برنامج رواتب مجاني؟",
  "قوالب Excel مجانية، ومعظم البرامج المدفوعة تقدم تجربة أو عرضًا مجانيًا. البرامج المجانية بالكامل نادرة وغالبًا محدودة بعدد قليل من الموظفين أو بمزايا أساسية. تأكد مما يحدث لبياناتك وللسعر عند تجاوز الحد المجاني."),
 ("هل يكفي Excel لإدارة الرواتب؟",
  "لعدد قليل من الموظفين برواتب ثابتة قد يكفي Excel. لكنه يصبح مخاطرة عند إضافة العمل الإضافي والإجازات غير المدفوعة والسلف ومكافأة نهاية الخدمة، لأن كل معادلة تُدار يدويًا وخلية واحدة خاطئة تغيّر راتب موظف. برنامج الرواتب يجري هذه الحسابات بالطريقة نفسها كل شهر ويحتفظ بالسجل."),
 ("كم تكلفة برنامج الرواتب؟",
  f"البرامج بالاشتراك تتقاضى عادة رسومًا شهرية أساسية ورسومًا لكل موظف. لعشرين موظفًا، تتراوح الأسعار المنشورة التي راجعناها في {CHECKED_AR} بين نحو {ZOHO_MONTH_AED*12:,} درهم و{GUSTO_MONTH*12:,} دولار سنويًا. أما البرامج المكتبية بترخيص لمرة واحدة فتُدفع مرة واحدة."),
]

CSS = """
:root{color-scheme:light;--bg:#f6f8ff;--ink:#0d1a33;--muted:#4b5a74;--line:#dfe6f3;--blue:#1d4ed8;--mint:#047857;--grad:linear-gradient(115deg,#2563eb,#0ea5e9 45%,#10b981)}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:400 17.5px/1.75 %BODYFONT%}
a{color:var(--blue)}
:focus-visible{outline:3px solid var(--blue);outline-offset:3px;border-radius:6px}
.wrap{max-width:820px;margin:0 auto;padding-inline:20px}
header{padding-block:20px}
.top{display:flex;justify-content:space-between;align-items:center;gap:16px;background:#fff;border:1px solid var(--line);border-radius:999px;padding:8px 8px 8px 16px}
.brand{display:flex;align-items:center;gap:10px;font:800 20px/1 %DISPFONT%;color:var(--ink);text-decoration:none}
.mark{width:32px;height:32px;border-radius:10px;background:var(--grad);display:grid;place-items:center}
.back{font-weight:700;font-size:15px;text-decoration:none;background:var(--grad);color:#fff;padding:10px 16px;border-radius:999px}
main{background:#fff;border:1px solid var(--line);border-radius:24px;padding:44px;margin-block:20px 40px}
@media (max-width:640px){main{padding:26px 18px}}
.crumbs{font-size:14px;color:var(--muted);margin:0 0 14px}.crumbs a{color:var(--muted)}
h1{font:800 clamp(30px,5.4vw,44px)/1.15 %DISPFONT%;letter-spacing:-.02em;margin:0 0 8px;text-wrap:balance}
.updated{color:var(--muted);font-size:14px;margin:0 0 22px}
.lead{font-size:19.5px;color:var(--muted)}
h2{font:800 25px/1.3 %DISPFONT%;margin:40px 0 10px;text-wrap:balance}
h3{font-size:18px;margin:22px 0 4px}
ul,ol{padding-inline-start:22px} li{margin-block:7px}
.answer{background:#f1f6ff;border:1px solid #d6e3ff;border-radius:16px;padding:18px 20px;margin:24px 0}
.answer b{display:block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--blue);margin-bottom:4px}
.tbl{overflow-x:auto;margin:16px 0;border:1px solid var(--line);border-radius:14px}
table{border-collapse:collapse;width:100%;min-width:560px;font-size:15.5px}
th,td{padding:12px 14px;text-align:start;vertical-align:top;border-bottom:1px solid var(--line)}
thead th{background:#f6f8ff;font-weight:700}
tbody tr:last-child td{border-bottom:0}
tr.us td{background:#f0fdf6}
td.num{font-variant-numeric:tabular-nums;white-space:nowrap}
.note{font-size:14.5px;color:var(--muted)}
.cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:14px}
@media (max-width:700px){.cols{grid-template-columns:1fr}}
.opt{border:1px solid var(--line);border-radius:16px;padding:16px 18px;min-width:0}
.opt h3{margin-top:0}
.opt p{font-size:15.5px;color:var(--muted);margin:6px 0}
.check{list-style:none;padding:0}
.check li{padding-inline-start:30px;position:relative}
.check li::before{content:"✓";position:absolute;inset-inline-start:0;top:0;color:var(--mint);font-weight:800}
.fit{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media (max-width:640px){.fit{grid-template-columns:1fr}}
.fit div{border-radius:16px;padding:16px 18px}
.fit .yes{background:#f0fdf6;border:1px solid #c9f2df}.fit .no{background:#fff7ed;border:1px solid #fde3c4}
.fit h3{margin-top:0}
.faq details{border:1px solid var(--line);border-radius:14px;padding:12px 16px;margin-block:10px}
.faq summary{cursor:pointer;font-weight:700}
.faq p{color:var(--muted);margin:8px 0 2px}
.cta{margin-top:40px;border-radius:20px;padding:26px;background:var(--grad);color:#fff;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between}
.cta p{margin:0;max-width:52ch}.cta strong{font:800 21px/1.3 %DISPFONT%;display:block}
.cta a{background:#fff;color:var(--blue);font-weight:700;text-decoration:none;padding:12px 20px;border-radius:999px}
.sources{font-size:14.5px;color:var(--muted)}
footer{color:var(--muted);font-size:14px;padding-bottom:40px;display:flex;flex-wrap:wrap;gap:10px 24px;justify-content:space-between}
footer a{color:var(--ink);font-weight:600;text-decoration:none}
"""

BEACON = """<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "a6468f1ecc92499d89496f6e15f55399"}'></script><!-- End Cloudflare Web Analytics -->"""
MARK = '<span class="mark" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"><circle cx="9" cy="9" r="5.5"/><circle cx="15" cy="15" r="5.5"/></svg></span>'


def _faq_html(faq):
    return "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in faq)


def _table(rows, heads):
    head = "".join(f"<th scope='col'>{h}</th>" for h in heads)
    body = ""
    for i, (n, how, y1, y3) in enumerate(rows):
        cls = ' class="us"' if i == len(rows) - 1 else ""
        body += f"<tr{cls}><th scope='row'>{html.escape(n)}</th><td>{html.escape(how)}</td><td class='num'>{html.escape(y1)}</td><td class='num'>{html.escape(y3)}</td></tr>"
    return f"<div class='tbl' tabindex='0'><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>"


def _sources(label):
    items = "".join(f'<li><a href="{u}" rel="noopener">{html.escape(t)}</a></li>' for t, u in SOURCES)
    return f'<div class="sources"><h2>{label}</h2><ul>{items}</ul></div>'


EN_BODY = f"""
<p class="crumbs"><a href="/">Home</a> › Salary software guide</p>
<h1>How to choose salary software for a small business</h1>
<p class="updated">Updated {CHECKED} · 6 minute read</p>
<p class="lead">If you're comparing payroll tools or searching for the best salary software, this guide covers what to check, what each type of tool costs, and when each one makes sense. We make PayCore, so we've also been clear about when it isn't the right fit.</p>

<div class="answer"><b>Short answer</b>The best salary software for you covers your monthly payroll steps (salaries, overtime, leave, loans and payslips), stays affordable as you hire, and keeps your data where you're comfortable. Price per employee is the biggest difference between tools over time.</div>

<h2>Your three options</h2>
<div class="cols">
<div class="opt"><h3>Excel</h3><p><b>Cost:</b> free.</p><p>Fine for a few staff on fixed salaries. Overtime, leave and loans mean more formulas, and one broken cell changes someone's pay without anyone noticing.</p></div>
<div class="opt"><h3>Cloud subscription</h3><p><b>Cost:</b> monthly fee plus a charge per employee.</p><p>Works from any computer or phone, often with employee self-service and, in some countries, automatic tax filing. The bill grows with your team, every month.</p></div>
<div class="opt"><h3>Desktop, one-time</h3><p><b>Cost:</b> paid once.</p><p>Installed on your own computer and works offline. No monthly bill and your data stays with you, but it's tied to that computer and usually to Windows.</p></div>
</div>

<h2>Features to check before you buy</h2>
<ul class="check">
<li><b>Salary structure:</b> basic pay plus the allowances you actually use (housing, transport, phone, food).</li>
<li><b>Monthly calculations:</b> overtime, bonuses, unpaid leave and deductions worked out automatically.</li>
<li><b>Loans and advances:</b> installments taken from salary each month, with a way to pause or record early repayment.</li>
<li><b>Payslips and reports:</b> PDF payslips with your company name, plus an Excel export for your accountant or bank.</li>
<li><b>End-of-service and bank rules:</b> gratuity at the rate your country uses, and a fixed bank-transfer amount if you follow a wage protection system (WPS).</li>
<li><b>Currency and language:</b> your currency with the right decimals (OMR, KWD and BHD use three), and Arabic if your team needs it.</li>
<li><b>Your data:</b> where it's stored, how you back it up, and how you get it out if you leave.</li>
<li><b>Support:</b> who answers when payroll is due tomorrow and something looks wrong.</li>
</ul>

<h2>What it really costs: 20 employees</h2>
<p>Subscription prices look small per month, so compare them over the years you'll actually use the software. Here is the published pricing for three popular tools, worked out for a business with 20 employees.</p>
{_table(ROWS, ["Software", "How it's priced", "Per year", "Over 3 years"])}
<p class="note">Prices checked in {CHECKED} from each vendor's published pricing; they change, so check before you buy. Zoho is billed annually in AED and converted at 3.6725 AED per dollar. Subscription tools include things a desktop tool doesn't, such as access from anywhere and, for Gusto, US tax filing. Gusto is only available in the United States.</p>

<h2>Questions to ask any vendor</h2>
<ol>
<li>What will I pay per year if my team doubles?</li>
<li>Can I export all my payroll history if I stop using it?</li>
<li>Does it handle my country's end-of-service and bank transfer rules?</li>
<li>Can I see it run a full month of payroll before I pay?</li>
<li>Who do I contact for support, and how fast do they answer?</li>
</ol>

<h2>Is PayCore right for you?</h2>
<div class="fit">
<div class="yes"><h3>A good fit if</h3><ul><li>You run payroll from one Windows computer</li><li>You don't want a monthly or per-employee bill</li><li>You want your data on your own computer</li><li>You need Arabic, Gulf currencies or end-of-service</li></ul></div>
<div class="no"><h3>Not the right fit if</h3><ul><li>Several people need to work on payroll from different places</li><li>Staff need to view their own payslips online</li><li>You use a Mac</li><li>You need automatic government tax filing</li></ul></div>
</div>

<h2>Common questions</h2>
<div class="faq">{_faq_html(FAQ_EN)}</div>

<div class="cta"><p><strong>See PayCore before you decide</strong>Book a free demo, or download it and contact us for your license.</p><a href="/#download">Go to PayCore</a></div>

{_sources("Sources")}
"""

AR_BODY = f"""
<p class="crumbs"><a href="/ar/">الرئيسية</a> › دليل اختيار برنامج الرواتب</p>
<h1>كيف تختار برنامج الرواتب المناسب لشركتك الصغيرة</h1>
<p class="updated">آخر تحديث: {CHECKED_AR} · قراءة 6 دقائق</p>
<p class="lead">إذا كنت تقارن بين برامج الرواتب أو تبحث عن أفضل برنامج رواتب، يشرح هذا الدليل ما يجب التحقق منه، وتكلفة كل نوع من البرامج، ومتى يناسب كل نوع. نحن من يطوّر PayCore، لذلك ذكرنا بوضوح أيضًا متى لا يكون الخيار المناسب.</p>

<div class="answer"><b>الإجابة المختصرة</b>أفضل برنامج رواتب لك هو الذي يغطي خطوات الرواتب الشهرية (الرواتب والعمل الإضافي والإجازات والسلف وقسائم الرواتب)، ويبقى بتكلفة مناسبة مع زيادة الموظفين، ويحفظ بياناتك حيث ترتاح. السعر لكل موظف هو أكبر فرق بين البرامج على المدى الطويل.</div>

<h2>الخيارات الثلاثة</h2>
<div class="cols">
<div class="opt"><h3>Excel</h3><p><b>التكلفة:</b> مجاني.</p><p>مناسب لعدد قليل من الموظفين برواتب ثابتة. العمل الإضافي والإجازات والسلف تعني معادلات أكثر، وخلية واحدة خاطئة تغيّر راتب موظف دون أن ينتبه أحد.</p></div>
<div class="opt"><h3>برنامج سحابي بالاشتراك</h3><p><b>التكلفة:</b> رسوم شهرية ورسوم لكل موظف.</p><p>يعمل من أي جهاز أو هاتف، وغالبًا مع بوابة للموظفين. لكن الفاتورة تكبر مع فريقك كل شهر.</p></div>
<div class="opt"><h3>برنامج مكتبي لمرة واحدة</h3><p><b>التكلفة:</b> تُدفع مرة واحدة.</p><p>يُثبّت على جهازك ويعمل بدون إنترنت. لا فاتورة شهرية وبياناتك تبقى معك، لكنه مرتبط بذلك الجهاز وغالبًا بنظام ويندوز.</p></div>
</div>

<h2>مزايا يجب التحقق منها قبل الشراء</h2>
<ul class="check">
<li><b>هيكل الراتب:</b> الراتب الأساسي والبدلات التي تستخدمها فعلًا (السكن والنقل والهاتف والطعام).</li>
<li><b>الحسابات الشهرية:</b> العمل الإضافي والمكافآت والإجازات غير المدفوعة والخصومات تُحسب تلقائيًا.</li>
<li><b>السلف والقروض:</b> خصم القسط من الراتب كل شهر، مع إمكانية الإيقاف المؤقت أو تسجيل سداد مبكر.</li>
<li><b>قسائم الرواتب والتقارير:</b> قسائم PDF باسم شركتك، وتصدير Excel للمحاسب أو البنك.</li>
<li><b>نهاية الخدمة وقواعد البنك:</b> مكافأة نهاية الخدمة بالنسبة المعمول بها في بلدك، ومبلغ تحويل ثابت إذا كنت تتبع نظام حماية الأجور (WPS).</li>
<li><b>العملة واللغة:</b> عملتك بالخانات العشرية الصحيحة (الريال العماني والدينار الكويتي والبحريني بثلاث خانات)، والعربية إذا احتاجها فريقك.</li>
<li><b>بياناتك:</b> أين تُحفظ، وكيف تأخذ نسخة احتياطية، وكيف تستخرجها إذا تركت البرنامج.</li>
<li><b>الدعم:</b> من يجيبك عندما يكون موعد الرواتب غدًا ويبدو شيء غير صحيح.</li>
</ul>

<h2>التكلفة الحقيقية لعشرين موظفًا</h2>
<p>أسعار الاشتراك تبدو صغيرة شهريًا، لذا قارنها على عدد السنوات التي ستستخدم فيها البرنامج فعلًا. هذه الأسعار المنشورة لثلاثة برامج معروفة، محسوبة لشركة فيها 20 موظفًا.</p>
{_table(ROWS_AR, ["البرنامج", "طريقة التسعير", "سنويًا", "خلال 3 سنوات"])}
<p class="note">راجعنا الأسعار في {CHECKED_AR} من صفحات الأسعار المنشورة لكل شركة، وقد تتغير، لذا تحقق منها قبل الشراء. البرامج بالاشتراك تتضمن أشياء لا يوفرها البرنامج المكتبي، مثل الوصول من أي مكان، وفي Gusto تقديم الضرائب الأمريكية. Gusto متاح في الولايات المتحدة فقط.</p>

<h2>أسئلة اطرحها على أي شركة برامج</h2>
<ol>
<li>كم سأدفع سنويًا إذا تضاعف عدد موظفيّ؟</li>
<li>هل يمكنني تصدير كل سجل الرواتب إذا توقفت عن استخدام البرنامج؟</li>
<li>هل يدعم قواعد نهاية الخدمة والتحويل البنكي في بلدي؟</li>
<li>هل يمكنني رؤيته يعالج رواتب شهر كامل قبل الدفع؟</li>
<li>بمن أتواصل للدعم، وما سرعة الرد؟</li>
</ol>

<h2>هل PayCore مناسب لك؟</h2>
<div class="fit">
<div class="yes"><h3>مناسب إذا</h3><ul><li>تدير الرواتب من جهاز ويندوز واحد</li><li>لا تريد فاتورة شهرية أو رسومًا لكل موظف</li><li>تريد بياناتك على جهازك الخاص</li><li>تحتاج العربية أو العملات الخليجية أو نهاية الخدمة</li></ul></div>
<div class="no"><h3>غير مناسب إذا</h3><ul><li>يحتاج عدة أشخاص للعمل على الرواتب من أماكن مختلفة</li><li>يحتاج الموظفون لرؤية قسائمهم عبر الإنترنت</li><li>تستخدم جهاز ماك</li><li>تحتاج تقديم الضرائب الحكومية تلقائيًا</li></ul></div>
</div>

<h2>أسئلة شائعة</h2>
<div class="faq">{_faq_html(FAQ_AR)}</div>

<div class="cta"><p><strong>شاهد PayCore قبل أن تقرر</strong>احجز عرضًا مجانيًا، أو حمّل البرنامج وتواصل معنا للحصول على الترخيص.</p><a href="/ar/#download">انتقل إلى PayCore</a></div>

{_sources("المصادر")}
"""


def _page(lang, url, alt_url, title, desc, body, home, back, fonts, bodyfont, dispfont, footer_links, site_url, year, headline):
    css = CSS.replace("%BODYFONT%", bodyfont).replace("%DISPFONT%", dispfont)
    faq = FAQ_EN if lang == "en" else FAQ_AR
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "@id": url + "#article", "headline": headline, "description": desc, "inLanguage": lang,
         "datePublished": "2026-10-14", "dateModified": "2026-10-14", "mainEntityOfPage": url,
         "author": {"@id": site_url + "#org"}, "publisher": {"@id": site_url + "#org"},
         "image": site_url + "og-image.png"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "PayCore", "item": site_url + ("" if lang == "en" else "ar/")},
            {"@type": "ListItem", "position": 2, "name": headline, "item": url}]},
        {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": lang,
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
    other = "ar" if lang == "en" else "en"
    return f"""<!doctype html>
<html lang="{lang}" dir="{'rtl' if lang == 'ar' else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="{lang}" href="{url}">
<link rel="alternate" hreflang="{other}" href="{alt_url}">
<link rel="alternate" hreflang="x-default" href="{url if lang == 'en' else alt_url}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="PayCore">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site_url}og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{fonts}">
<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=1)}
</script>
<style>{css}</style>
</head>
<body>
<header><div class="wrap"><div class="top">
<a class="brand" href="{home}">{MARK}PayCore</a>
<a class="back" href="{home}">{back}</a>
</div></div></header>
<div class="wrap">
<main>{body}</main>
<footer><span>© {year} PayCore.</span><span>{footer_links}</span></footer>
</div>
{BEACON}
</body>
</html>
"""


def build(out_dir, site_url, year):
    en_url = site_url + "salary-software-guide/"
    ar_url = site_url + "ar/salary-software-guide/"
    pages = [
        ("en", en_url, ar_url, "How to Choose Salary Software for a Small Business (2026)",
         "Compare Excel, cloud subscription and one-time payroll software: features to check, real costs for 20 employees, and questions to ask before you buy.",
         EN_BODY, "/", "Back to home",
         "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Figtree:wght@400;600;700&display=swap",
         '"Figtree","Segoe UI",system-ui,sans-serif', '"Bricolage Grotesque","Segoe UI",sans-serif',
         '<a href="/">Home</a> · <a href="/ar/salary-software-guide/" hreflang="ar" lang="ar">العربية</a> · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a>',
         "How to choose salary software for a small business", os.path.join(out_dir, "salary-software-guide")),
        ("ar", ar_url, en_url, "كيف تختار أفضل برنامج رواتب لشركتك الصغيرة (دليل 2026) | PayCore",
         "مقارنة بين Excel وبرامج الرواتب بالاشتراك والبرامج بترخيص لمرة واحدة: المزايا التي يجب التحقق منها، والتكلفة الحقيقية لعشرين موظفًا، وأسئلة قبل الشراء.",
         AR_BODY, "/ar/", "العودة للرئيسية",
         "https://fonts.googleapis.com/css2?family=Cairo:wght@700;800&family=IBM+Plex+Sans+Arabic:wght@400;600;700&display=swap",
         '"IBM Plex Sans Arabic","Segoe UI",Tahoma,sans-serif', '"Cairo","Segoe UI",Tahoma,sans-serif',
         '<a href="/ar/">الرئيسية</a> · <a href="/salary-software-guide/" hreflang="en" lang="en">English</a> · <a href="/privacy.html">سياسة الخصوصية</a> · <a href="/terms.html">شروط الاستخدام</a>',
         "كيف تختار برنامج الرواتب المناسب لشركتك الصغيرة", os.path.join(out_dir, "ar", "salary-software-guide")),
    ]
    for lang, url, alt, title, desc, body, home, back, fonts, bf, df, links, headline, folder in pages:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(_page(lang, url, alt, title, desc, body.strip(), home, back, fonts, bf, df, links, site_url, year, headline))
    return en_url, ar_url
