"""Free salary calculator for absences, unpaid leave and days worked.

  /salary-calculator/      (English)
  /ar/salary-calculator/   (Arabic)

Targets "salary per day calculator", "unpaid leave deduction calculator", "absent salary deduction",
"pro rata salary calculator", "حساب الراتب اليومي", "حساب خصم الغياب".
Uses gratuity._page for the page shell. Edit the text below, then run build.py.
"""
import html, json, os
import gratuity

FAQ_EN = [
 ("How do I calculate salary per day?",
  "Divide the monthly salary by the number of days your company uses: 30 days is the most common choice in the Gulf, while some companies use the actual days in the month or only working days (for example 26). Pick the method your contract or HR policy says, and use it the same way every month."),
 ("How is a deduction for absence or unpaid leave calculated?",
  "Daily rate × number of absent or unpaid days. For example, a full salary of OMR 600 on a 30-day basis is OMR 20 a day, so 3 unpaid days is a deduction of OMR 60."),
 ("Should the deduction be from basic salary or full salary?",
  "It depends on the employment contract, company policy and local labour law. Many employers deduct from the full salary (basic plus allowances) for unpaid days, while others deduct from basic only. This calculator lets you choose which parts of the salary are affected, so you can follow your own rule."),
 ("How do I calculate salary for someone who joined or left mid-month?",
  "Choose “Days worked”, enter the number of days the employee worked that month, and the calculator pays the chosen salary parts for those days only. Parts you leave unticked are paid in full."),
 ("Does PayCore do this automatically?",
  "Yes. PayCore tracks leave, attendance and overtime and works out unpaid-leave deductions in the monthly payroll for every employee, then produces payslips and the bank transfer list. It's a one-time USD 50 license for unlimited employees."),
]
FAQ_AR = [
 ("كيف أحسب الراتب اليومي؟",
  "اقسم الراتب الشهري على عدد الأيام الذي تعتمده شركتك: 30 يومًا هو الأكثر استخدامًا في الخليج، وبعض الشركات تستخدم عدد أيام الشهر الفعلي أو أيام العمل فقط (مثل 26 يومًا). اختر الطريقة التي ينص عليها العقد أو سياسة الشركة، واستخدمها بالطريقة نفسها كل شهر."),
 ("كيف يُحسب خصم الغياب أو الإجازة بدون أجر؟",
  "الأجر اليومي × عدد أيام الغياب أو الإجازة بدون أجر. مثلًا راتب كامل 600 ريال عماني على أساس 30 يومًا يساوي 20 ريالًا يوميًا، فيكون خصم 3 أيام 60 ريالًا."),
 ("هل يكون الخصم من الراتب الأساسي أم من الراتب الكامل؟",
  "يعتمد ذلك على عقد العمل وسياسة الشركة وقانون العمل المحلي. كثير من أصحاب العمل يخصمون من الراتب الكامل (الأساسي مع البدلات) عن الأيام بدون أجر، وآخرون يخصمون من الأساسي فقط. تتيح لك هذه الحاسبة اختيار أجزاء الراتب التي يشملها الحساب لتطبق قاعدتك."),
 ("كيف أحسب راتب موظف التحق أو غادر في منتصف الشهر؟",
  "اختر «أيام العمل»، وأدخل عدد الأيام التي عملها الموظف في ذلك الشهر، فتحسب الحاسبة أجزاء الراتب المختارة عن تلك الأيام فقط. أما الأجزاء غير المحددة فتُدفع كاملة."),
 ("هل يقوم PayCore بذلك تلقائيًا؟",
  "نعم. يتابع PayCore الإجازات والحضور والعمل الإضافي ويحسب خصم الإجازات بدون أجر ضمن الرواتب الشهرية لكل موظف، ثم يُصدر قسائم الرواتب وكشف التحويل البنكي. والترخيص لمرة واحدة بـ 50 دولارًا لعدد غير محدود من الموظفين."),
]

CSS = """
.comp{display:grid;grid-template-columns:auto 1fr;gap:10px 12px;align-items:center}
.comp .ck{display:flex;align-items:center;gap:8px;font-weight:600;margin:0;white-space:nowrap}
.comp .ck input{width:18px;height:18px}
.presets{display:flex;flex-wrap:wrap;gap:8px;margin:2px 0 14px}
.presets button{font:inherit;font-size:14.5px;font-weight:700;border:1px solid #c9d5ea;background:#fff;color:var(--ink);border-radius:999px;padding:7px 13px;cursor:pointer}
.presets button.on{border-color:var(--mint);background:#ecfdf5;color:var(--mint)}
.res table{min-width:0;font-size:15px;margin-top:10px}
.res td,.res th{padding:8px 10px}
.res td.num{text-align:end}
#sc-bm{display:none}#sc-bc{display:none}
"""

JS = r"""
(function(){
 var f=document.getElementById('sc'); if(!f) return;
 var T=JSON.parse(f.getAttribute('data-t'));
 var $=function(id){return document.getElementById(id)};
 var DEC={OMR:3,KWD:3,BHD:3};
 var K=['basic','housing','transport','other'];
 function val(r){var e=f.querySelector('input[name='+r+']:checked');return e?e.value:''}
 function fmt(v,d){return v.toLocaleString(T.locale,{minimumFractionDigits:d,maximumFractionDigits:d})}
 function preset(p){
  K.forEach(function(k){$('sc-ck-'+k).checked=(p==='full')||(k==='basic')||(p==='bh'&&k==='housing')});
  calc();
 }
 function marks(){
  var on=K.filter(function(k){return $('sc-ck-'+k).checked}).join(',');
  var map={'basic,housing,transport,other':'full','basic':'basic','basic,housing':'bh'};
  f.querySelectorAll('.presets button').forEach(function(b){b.classList.toggle('on',map[on]===b.getAttribute('data-p'))});
 }
 function calc(){
  marks();
  var cur=$('sc-cur').value, d=DEC[cur]===undefined?2:DEC[cur], out=$('sc-out'), mode=val('m'), basis=val('b');
  $('sc-bm').style.display=basis==='cal'?'block':'none'; $('sc-bc').style.display=basis==='cus'?'block':'none';
  $('sc-days-l').textContent=T.daysL[mode]; $('sc-ck-l').textContent=T.ckL[mode];
  var div=30;
  if(basis==='cal'){var m=$('sc-month').value; if(m){var p=m.split('-');div=new Date(Date.UTC(+p[0],+p[1],0)).getUTCDate()}}
  if(basis==='cus'){div=parseFloat($('sc-wd').value)||0}
  var parts=K.map(function(k){return {k:k,v:parseFloat($('sc-'+k).value)||0,on:$('sc-ck-'+k).checked}});
  var total=parts.reduce(function(a,p){return a+p.v},0), days=parseFloat($('sc-days').value);
  if(!(total>0)||isNaN(days)||!(div>0)){out.innerHTML='<p class="hint">'+T.fill+'</p>';return}
  var warn=days>div?'<p class="warn">'+T.over.replace('{n}',div)+'</p>':'';
  days=Math.min(Math.max(days,0),div);
  var aff=parts.reduce(function(a,p){return a+(p.on?p.v:0)},0), daily=aff/div, rows='', pay=0;
  parts.forEach(function(p){
   if(!p.v) return;
   var paid=p.on?(mode==='abs'?p.v-p.v/div*days:p.v/div*days):p.v; pay+=paid;
   rows+='<tr><th scope="row">'+T.names[p.k]+(p.on?'':' <small>('+T.full+')</small>')+'</th><td class="num">'+fmt(p.v,d)+'</td><td class="num">'+fmt(paid,d)+'</td></tr>';
  });
  var lines=[T.rate.replace('{r}',cur+' '+fmt(daily,d)).replace('{a}',cur+' '+fmt(aff,d)).replace('{n}',div)];
  if(mode==='abs') lines.push(T.ded.replace('{x}',cur+' '+fmt(daily*days,d)).replace('{n}',days));
  else lines.push(T.earn.replace('{n}',days).replace('{x}',cur+' '+fmt(daily*days,d)));
  out.innerHTML=warn+'<div class="lbl">'+T.est+'</div><div class="big">'+cur+' '+fmt(pay,d)+'</div><ul>'+lines.map(function(l){return '<li>'+l+'</li>'}).join('')+'</ul>'
   +'<div class="tbl"><table><thead><tr><th scope="col">'+T.h[0]+'</th><th scope="col">'+T.h[1]+'</th><th scope="col">'+T.h[2]+'</th></tr></thead><tbody>'+rows
   +'<tr><th scope="row">'+T.total+'</th><td class="num"><b>'+fmt(total,d)+'</b></td><td class="num"><b>'+fmt(pay,d)+'</b></td></tr></tbody></table></div>';
 }
 f.addEventListener('input',calc); f.addEventListener('change',calc);
 f.addEventListener('submit',function(e){e.preventDefault();calc()});
 f.querySelectorAll('.presets button').forEach(function(b){b.addEventListener('click',function(){preset(b.getAttribute('data-p'))})});
 $('sc-month').value=new Date().toISOString().slice(0,7);
 calc();
})();
"""

CURS = ["OMR", "AED", "SAR", "QAR", "KWD", "BHD", "USD", "EUR", "GBP", "INR", "PKR"]

T_EN = {"locale": "en-US",
 "daysL": {"abs": "Absent or unpaid leave days", "work": "Days worked this month"},
 "ckL": {"abs": "Deduct from", "work": "Pay these parts for days worked"},
 "fill": "Enter the salary and number of days to see the result.",
 "over": "Days can't be more than the {n} days in your chosen basis, so {n} was used.",
 "est": "Salary for the month", "full": "paid in full",
 "rate": "Daily rate: {r} ({a} ÷ {n} days)",
 "ded": "Deduction: {x} for {n} days",
 "earn": "{n} days worked: {x}",
 "names": {"basic": "Basic salary", "housing": "Housing allowance", "transport": "Transport allowance", "other": "Other allowances"},
 "h": ["Salary part", "Monthly", "Paid"], "total": "Total"}
T_AR = {"locale": "ar-OM-u-nu-latn",
 "daysL": {"abs": "أيام الغياب أو الإجازة بدون أجر", "work": "أيام العمل في هذا الشهر"},
 "ckL": {"abs": "الخصم من", "work": "أجزاء الراتب التي تُحسب بأيام العمل"},
 "fill": "أدخل الراتب وعدد الأيام لعرض النتيجة.",
 "over": "لا يمكن أن تزيد الأيام على {n} يومًا بحسب الأساس المختار، لذا استُخدم {n}.",
 "est": "راتب الشهر", "full": "يُدفع كاملًا",
 "rate": "الأجر اليومي: {r} ({a} ÷ {n} يومًا)",
 "ded": "الخصم: {x} عن {n} يوم",
 "earn": "{n} يوم عمل: {x}",
 "names": {"basic": "الراتب الأساسي", "housing": "بدل السكن", "transport": "بدل النقل", "other": "بدلات أخرى"},
 "h": ["جزء الراتب", "شهريًا", "المدفوع"], "total": "الإجمالي"}

L_EN = {"cur": "Currency", "mode": "What do you want to calculate?", "abs": "Deduction for absent or unpaid days", "work": "Salary for days worked",
        "parts": "Monthly salary", "basis": "Days in a month", "b30": "30 days", "bcal": "Actual days in the month", "bcus": "Working days",
        "month": "Month", "wd": "Working days in the month",
        "presets": "Quick choice", "pfull": "Full salary", "pbasic": "Basic only", "pbh": "Basic + housing",
        "hint": "Unticked parts are paid in full.",
        "disc": "A free estimate. Follow your employment contract, company policy and local labour law; this isn't legal advice."}
L_AR = {"cur": "العملة", "mode": "ماذا تريد أن تحسب؟", "abs": "خصم أيام الغياب أو الإجازة بدون أجر", "work": "الراتب عن أيام العمل",
        "parts": "الراتب الشهري", "basis": "عدد أيام الشهر", "b30": "30 يومًا", "bcal": "أيام الشهر الفعلية", "bcus": "أيام العمل",
        "month": "الشهر", "wd": "أيام العمل في الشهر",
        "presets": "اختيار سريع", "pfull": "الراتب الكامل", "pbasic": "الأساسي فقط", "pbh": "الأساسي + السكن",
        "hint": "الأجزاء غير المحددة تُدفع كاملة.",
        "disc": "تقدير مجاني. اتبع عقد العمل وسياسة الشركة وقانون العمل المحلي، وهذه ليست استشارة قانونية."}


def _form(t, L):
    data = html.escape(json.dumps(t, ensure_ascii=False), quote=True)
    opts = "".join(f'<option{" selected" if c == "OMR" else ""}>{c}</option>' for c in CURS)
    rows = "".join(
        f'<label class="ck" for="sc-ck-{k}"><input type="checkbox" id="sc-ck-{k}"{" checked" if k == "basic" else " checked"}> {t["names"][k]}</label>'
        f'<input type="number" id="sc-{k}" min="0" step="any" inputmode="decimal" placeholder="0" aria-label="{t["names"][k]}">'
        for k in ["basic", "housing", "transport", "other"])
    return f"""<form class="calc" id="sc" data-t="{data}" novalidate>
<div class="fld"><label id="sc-m-l">{L['mode']}</label>
<div class="seg" role="radiogroup" aria-labelledby="sc-m-l">
<label><input type="radio" name="m" value="abs" checked> {L['abs']}</label>
<label><input type="radio" name="m" value="work"> {L['work']}</label>
</div></div>
<div class="row">
<div class="fld"><label for="sc-cur">{L['cur']}</label><select id="sc-cur">{opts}</select></div>
<div class="fld"><label for="sc-days" id="sc-days-l"></label><input type="number" id="sc-days" min="0" step="0.5" inputmode="decimal" placeholder="0"></div>
</div>
<div class="fld"><label>{L['parts']} · <span id="sc-ck-l"></span></label>
<div class="presets" role="group" aria-label="{L['presets']}"><button type="button" data-p="full">{L['pfull']}</button><button type="button" data-p="basic">{L['pbasic']}</button><button type="button" data-p="bh">{L['pbh']}</button></div>
<div class="comp">{rows}</div><p class="hint">{L['hint']}</p></div>
<div class="fld"><label id="sc-b-l">{L['basis']}</label>
<div class="seg" role="radiogroup" aria-labelledby="sc-b-l">
<label><input type="radio" name="b" value="30" checked> {L['b30']}</label>
<label><input type="radio" name="b" value="cal"> {L['bcal']}</label>
<label><input type="radio" name="b" value="cus"> {L['bcus']}</label>
</div>
<div id="sc-bm" class="fld" style="margin-top:10px"><label for="sc-month">{L['month']}</label><input type="month" id="sc-month"></div>
<div id="sc-bc" class="fld" style="margin-top:10px"><label for="sc-wd">{L['wd']}</label><input type="number" id="sc-wd" min="1" max="31" step="1" value="26"></div>
</div>
<div class="res" id="sc-out" aria-live="polite"></div>
<p class="hint">{L['disc']}</p>
</form>"""


EX_EN = [("Full salary, 3 unpaid days", "Basic 400 + housing 150 + transport 50 = OMR 600", "600 ÷ 30 = 20 a day; 20 × 3 = 60", "OMR 540"),
         ("Basic only, 3 unpaid days", "Same salary", "400 ÷ 30 = 13.333 a day; × 3 = 40", "OMR 560"),
         ("Joined on the 11th (20 days worked)", "Full salary OMR 600", "600 ÷ 30 × 20", "OMR 400")]
EX_AR = [("الراتب الكامل، 3 أيام بدون أجر", "أساسي 400 + سكن 150 + نقل 50 = 600 ريال عماني", "600 ÷ 30 = 20 يوميًا؛ 20 × 3 = 60", "540 ريالًا"),
         ("الأساسي فقط، 3 أيام بدون أجر", "الراتب نفسه", "400 ÷ 30 = 13.333 يوميًا؛ × 3 = 40", "560 ريالًا"),
         ("التحق يوم 11 (20 يوم عمل)", "راتب كامل 600 ريال", "600 ÷ 30 × 20", "400 ريال")]

EN_BODY = f"""
<p class="crumbs"><a href="/">Home</a> › Free salary calculator</p>
<h1>Free salary calculator for absences, unpaid leave and days worked</h1>
<p class="updated"><span class="free">FREE</span>No sign-up · Works for any currency</p>
<p class="lead">Work out a daily salary rate, the deduction for absent or unpaid leave days, or the pay for an employee who worked only part of the month. Choose whether the calculation uses the full salary, basic salary only, or basic plus selected allowances.</p>
{_form(T_EN, L_EN)}
<h2>Worked examples</h2>
{gratuity._ex_table(EX_EN, ["Case", "Salary", "Calculation", "Salary for the month"])}
<h2>Full salary or basic salary?</h2>
<p>There isn't one rule for every company. Many employers deduct unpaid days from the full salary, because allowances are paid for the month as a whole; others deduct from basic salary only, or from basic plus housing. Use what your employment contract and company policy say, and apply it the same way to every employee. Tick the salary parts above to match your rule.</p>
<h2>Which day count to use</h2>
<ul class="check"><li><b>30 days:</b> the most common in the Gulf. The daily rate is the same every month.</li><li><b>Actual days in the month:</b> 28 to 31 days, so the daily rate changes each month.</li><li><b>Working days:</b> only days the employee is expected to work, such as 26 for a six-day week.</li></ul>
<h2>Common questions</h2>
<div class="faq">{gratuity.guide._faq_html(FAQ_EN)}</div>
<p class="also">Also free: <a href="/gratuity-calculator/">end-of-service gratuity calculator for Oman, UAE and Saudi Arabia</a>.</p>
<div class="cta"><p><strong>Let PayCore do this every month</strong>PayCore tracks leave and attendance and works out deductions, payroll, loans and payslips for all your staff on your own PC. One-time USD 50, unlimited employees.</p><a href="/#download">Get PayCore</a></div>
"""

AR_BODY = f"""
<p class="crumbs"><a href="/ar/">الرئيسية</a> › حاسبة الراتب المجانية</p>
<h1>حاسبة الراتب المجانية للغياب والإجازة بدون أجر وأيام العمل</h1>
<p class="updated"><span class="free">مجانية</span>بدون تسجيل · تعمل مع أي عملة</p>
<p class="lead">احسب الأجر اليومي، وخصم أيام الغياب أو الإجازة بدون أجر، أو راتب موظف عمل جزءًا من الشهر فقط. اختر إن كان الحساب على الراتب الكامل، أو الأساسي فقط، أو الأساسي مع بدلات تختارها.</p>
{_form(T_AR, L_AR)}
<h2>أمثلة محسوبة</h2>
{gratuity._ex_table(EX_AR, ["الحالة", "الراتب", "الحساب", "راتب الشهر"])}
<h2>الراتب الكامل أم الأساسي؟</h2>
<p>لا توجد قاعدة واحدة لكل الشركات. كثير من أصحاب العمل يخصمون الأيام بدون أجر من الراتب الكامل لأن البدلات تُدفع عن الشهر كله، وآخرون يخصمون من الأساسي فقط أو من الأساسي مع السكن. اتبع ما ينص عليه عقد العمل وسياسة الشركة، وطبّقه بالطريقة نفسها على جميع الموظفين. حدد أجزاء الراتب أعلاه لتطابق قاعدتك.</p>
<h2>أي عدد أيام تستخدم</h2>
<ul class="check"><li><b>30 يومًا:</b> الأكثر استخدامًا في الخليج، والأجر اليومي ثابت كل شهر.</li><li><b>أيام الشهر الفعلية:</b> من 28 إلى 31 يومًا، فيتغير الأجر اليومي كل شهر.</li><li><b>أيام العمل:</b> الأيام التي يُتوقع أن يعمل فيها الموظف فقط، مثل 26 يومًا لأسبوع من ستة أيام.</li></ul>
<h2>أسئلة شائعة</h2>
<div class="faq">{gratuity.guide._faq_html(FAQ_AR)}</div>
<p class="also">أداة مجانية أخرى: <a href="/ar/gratuity-calculator/">حاسبة مكافأة نهاية الخدمة في عمان والإمارات والسعودية</a>.</p>
<div class="cta"><p><strong>دع PayCore يقوم بذلك كل شهر</strong>يتابع PayCore الإجازات والحضور ويحسب الخصومات والرواتب والسلف وقسائم الرواتب لجميع موظفيك على جهازك. 50 دولارًا لمرة واحدة، لعدد غير محدود من الموظفين.</p><a href="/ar/#download">احصل على PayCore</a></div>
"""


def build(out_dir, site_url, year):
    en_url = site_url + "salary-calculator/"
    ar_url = site_url + "ar/salary-calculator/"
    pages = [
        ("en", en_url, ar_url, "Free Salary Calculator: Absence, Unpaid Leave & Days Worked",
         "Free salary calculator: daily rate, deduction for absent or unpaid leave days, or pay for days worked, on full salary, basic only or chosen allowances.",
         EN_BODY, "/", "Back to home",
         "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Figtree:wght@400;600;700&display=swap",
         '"Figtree","Segoe UI",system-ui,sans-serif', '"Bricolage Grotesque","Segoe UI",sans-serif',
         '<a href="/">Home</a> · <a href="/gratuity-calculator/">Free gratuity calculator</a> · <a href="/salary-software-guide/">Buyer\'s guide</a> · <a href="/ar/salary-calculator/" hreflang="ar" lang="ar">العربية</a> · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a>',
         "Free salary calculator for absences, unpaid leave and days worked", os.path.join(out_dir, "salary-calculator"), FAQ_EN),
        ("ar", ar_url, en_url, "حاسبة الراتب المجانية: خصم الغياب والإجازة بدون أجر وأيام العمل | PayCore",
         "حاسبة راتب مجانية: احسب الأجر اليومي وخصم أيام الغياب أو الإجازة بدون أجر أو الراتب عن أيام العمل، على الراتب الكامل أو الأساسي أو بدلات تختارها.",
         AR_BODY, "/ar/", "العودة للرئيسية",
         "https://fonts.googleapis.com/css2?family=Cairo:wght@700;800&family=IBM+Plex+Sans+Arabic:wght@400;600;700&display=swap",
         '"IBM Plex Sans Arabic","Segoe UI",Tahoma,sans-serif', '"Cairo","Segoe UI",Tahoma,sans-serif',
         '<a href="/ar/">الرئيسية</a> · <a href="/ar/gratuity-calculator/">حاسبة مكافأة نهاية الخدمة المجانية</a> · <a href="/ar/salary-software-guide/">دليل اختيار برنامج الرواتب</a> · <a href="/salary-calculator/" hreflang="en" lang="en">English</a> · <a href="/privacy.html">سياسة الخصوصية</a> · <a href="/terms.html">شروط الاستخدام</a>',
         "حاسبة الراتب المجانية للغياب والإجازة بدون أجر وأيام العمل", os.path.join(out_dir, "ar", "salary-calculator"), FAQ_AR),
    ]
    for lang, url, alt, title, desc, body, home, back, fonts, bf, df, links, headline, folder, faq in pages:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(gratuity._page(lang, url, alt, title, desc, body.strip(), home, back, fonts, bf, df, links,
                                    site_url, year, headline, faq, js=JS, extra_css=CSS))
    return en_url, ar_url
