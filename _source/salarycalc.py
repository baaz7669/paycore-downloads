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
 ("How do I calculate pay for hourly employees?",
  "With a fixed hourly rate, multiply the rate by the hours worked; hours above the standard monthly hours (for example 208) are paid at your extra-hours rate, such as 125%. If the employee has a monthly salary paid by hours, the hourly rate is the salary divided by the standard hours: fewer hours reduce the salary and extra hours add to it. Choose “Hourly pay” in the calculator above to work it out."),
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
 ("كيف أحسب أجر الموظف بالساعة؟",
  "مع سعر ثابت للساعة، اضرب السعر في ساعات العمل، وتُدفع الساعات التي تزيد على ساعات الشهر القياسية (مثل 208) بنسبة الساعات الإضافية، مثل 125%. وإذا كان للموظف راتب شهري يُحسب بالساعات، فأجر الساعة هو الراتب مقسومًا على الساعات القياسية: الساعات الأقل تُنقص الراتب والساعات الإضافية تزيده. اختر «الأجر بالساعة» في الحاسبة أعلاه لحسابه."),
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
.newpill{font-size:11px;font-weight:800;letter-spacing:.06em;color:#fff;background:#047857;border-radius:999px;padding:2px 7px;margin-inline-start:4px}
[hidden]{display:none!important}
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
  var hr=mode==='hr';
  ['sc-days-f','sc-parts-f','sc-basis-f'].forEach(function(id){$(id).hidden=hr}); $('sc-hr-f').hidden=!hr;
  if(hr){hourly(cur,d,out);return}
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
 function hourly(cur,d,out){
  var m=val('hm'), fixed=m==='fixed';
  $('sc-rate-f').hidden=!fixed; $('sc-msal-f').hidden=fixed;
  var Tt=parseFloat($('sc-std').value), H=parseFloat($('sc-hw').value), P=(parseFloat($('sc-pct').value)||0)/100;
  var R=parseFloat($('sc-rate').value), S=parseFloat($('sc-msal').value);
  if(!(Tt>0)||isNaN(H)||H<0||(fixed?!(R>0):!(S>0))){out.innerHTML='<p class="hint">'+T.hfill+'</p>';return}
  var c=function(v){return cur+' '+fmt(v,d)}, fh=function(v){return v.toLocaleString(T.locale,{maximumFractionDigits:2})}, lines=[], pay;
  var reg=Math.min(H,Tt), ext=Math.max(0,H-Tt);
  if(fixed){
   pay=R*reg+R*ext*P;
   lines.push(T.hreg.replace('{h}',fh(reg)).replace('{r}',c(R)).replace('{x}',c(R*reg)));
   if(ext>0) lines.push(T.hext.replace('{h}',fh(ext)).replace('{r}',c(R)).replace('{p}',Math.round(P*100)).replace('{x}',c(R*ext*P)));
  } else {
   var rate=S/Tt; lines.push(T.hrate.replace('{s}',c(S)).replace('{t}',fh(Tt)).replace('{r}',c(rate)));
   if(H<Tt){var ded=S*(Tt-H)/Tt; pay=S-ded; lines.push(T.hshort.replace('{h}',fh(Tt-H)).replace('{x}',c(ded)));}
   else if(H>Tt){var ex=S*(H-Tt)/Tt*P; pay=S+ex; lines.push(T.hext.replace('{h}',fh(ext)).replace('{r}',c(rate)).replace('{p}',Math.round(P*100)).replace('{x}',c(ex)));}
   else {pay=S; lines.push(T.hfull);}
  }
  out.innerHTML='<div class="lbl">'+T.hest+'</div><div class="big">'+c(pay)+'</div><ul>'+lines.map(function(l){return '<li>'+l+'</li>'}).join('')+'</ul>';
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
 "h": ["Salary part", "Monthly", "Paid"], "total": "Total",
 "hfill": "Enter the hourly rate or monthly salary, the hours worked and the standard monthly hours.",
 "hest": "Pay for the month",
 "hreg": "Regular hours: {h} × {r} = {x}",
 "hext": "Extra hours: {h} × {r} × {p}% = {x}",
 "hrate": "Hourly rate: {s} ÷ {t} hours = {r}",
 "hshort": "Short by {h} hours: deduction {x}",
 "hfull": "Worked exactly the standard hours: full salary"}
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
 "h": ["جزء الراتب", "شهريًا", "المدفوع"], "total": "الإجمالي",
 "hfill": "أدخل سعر الساعة أو الراتب الشهري، وساعات العمل، وساعات الشهر القياسية.",
 "hest": "أجر الشهر",
 "hreg": "الساعات العادية: {h} × {r} = {x}",
 "hext": "الساعات الإضافية: {h} × {r} × {p}% = {x}",
 "hrate": "أجر الساعة: {s} ÷ {t} ساعة = {r}",
 "hshort": "نقص {h} ساعة: خصم {x}",
 "hfull": "عمل الساعات القياسية كاملة: الراتب كاملًا"}

L_EN = {"cur": "Currency", "mode": "What do you want to calculate?", "abs": "Deduction for absent or unpaid days", "work": "Salary for days worked",
        "parts": "Monthly salary", "basis": "Days in a month", "b30": "30 days", "bcal": "Actual days in the month", "bcus": "Working days",
        "month": "Month", "wd": "Working days in the month",
        "presets": "Quick choice", "pfull": "Full salary", "pbasic": "Basic only", "pbh": "Basic + housing",
        "hint": "Unticked parts are paid in full.",
        "disc": "A free estimate. Follow your employment contract, company policy and local labour law; this isn't legal advice.",
        "hr": "Hourly pay", "new": "NEW", "hmeth": "How is this employee paid?", "hfixed": "Fixed rate per hour", "hsal": "Monthly salary by hours worked",
        "hrate": "Hourly rate", "hmsal": "Monthly salary", "hworked": "Hours worked this month",
        "hstd": "Standard hours in the month", "hstdh": "208 is 8 hours × 26 working days. Hours above this count as extra hours.",
        "hpct": "Extra hours paid at (%)", "hpcth": "Use 100 for the same rate. Overtime rates differ by country and contract."}
L_AR = {"cur": "العملة", "mode": "ماذا تريد أن تحسب؟", "abs": "خصم أيام الغياب أو الإجازة بدون أجر", "work": "الراتب عن أيام العمل",
        "parts": "الراتب الشهري", "basis": "عدد أيام الشهر", "b30": "30 يومًا", "bcal": "أيام الشهر الفعلية", "bcus": "أيام العمل",
        "month": "الشهر", "wd": "أيام العمل في الشهر",
        "presets": "اختيار سريع", "pfull": "الراتب الكامل", "pbasic": "الأساسي فقط", "pbh": "الأساسي + السكن",
        "hint": "الأجزاء غير المحددة تُدفع كاملة.",
        "disc": "تقدير مجاني. اتبع عقد العمل وسياسة الشركة وقانون العمل المحلي، وهذه ليست استشارة قانونية.",
        "hr": "الأجر بالساعة", "new": "جديد", "hmeth": "كيف يُدفع أجر هذا الموظف؟", "hfixed": "سعر ثابت للساعة", "hsal": "الراتب الشهري حسب ساعات العمل",
        "hrate": "سعر الساعة", "hmsal": "الراتب الشهري", "hworked": "ساعات العمل هذا الشهر",
        "hstd": "ساعات الشهر القياسية", "hstdh": "208 تعني 8 ساعات × 26 يوم عمل. ما يزيد عليها يُحسب ساعات إضافية.",
        "hpct": "أجر الساعات الإضافية (%)", "hpcth": "استخدم 100 لنفس السعر. تختلف نسب العمل الإضافي حسب الدولة والعقد."}


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
<label><input type="radio" name="m" value="hr"> {L['hr']} <span class="newpill">{L['new']}</span></label>
</div></div>
<div class="row">
<div class="fld"><label for="sc-cur">{L['cur']}</label><select id="sc-cur">{opts}</select></div>
<div class="fld" id="sc-days-f"><label for="sc-days" id="sc-days-l"></label><input type="number" id="sc-days" min="0" step="0.5" inputmode="decimal" placeholder="0"></div>
</div>
<div class="fld" id="sc-parts-f"><label>{L['parts']} · <span id="sc-ck-l"></span></label>
<div class="presets" role="group" aria-label="{L['presets']}"><button type="button" data-p="full">{L['pfull']}</button><button type="button" data-p="basic">{L['pbasic']}</button><button type="button" data-p="bh">{L['pbh']}</button></div>
<div class="comp">{rows}</div><p class="hint">{L['hint']}</p></div>
<div class="fld" id="sc-basis-f"><label id="sc-b-l">{L['basis']}</label>
<div class="seg" role="radiogroup" aria-labelledby="sc-b-l">
<label><input type="radio" name="b" value="30" checked> {L['b30']}</label>
<label><input type="radio" name="b" value="cal"> {L['bcal']}</label>
<label><input type="radio" name="b" value="cus"> {L['bcus']}</label>
</div>
<div id="sc-bm" class="fld" style="margin-top:10px"><label for="sc-month">{L['month']}</label><input type="month" id="sc-month"></div>
<div id="sc-bc" class="fld" style="margin-top:10px"><label for="sc-wd">{L['wd']}</label><input type="number" id="sc-wd" min="1" max="31" step="1" value="26"></div>
</div>
<div id="sc-hr-f" hidden>
<div class="fld"><label id="sc-hm-l">{L['hmeth']}</label>
<div class="seg" role="radiogroup" aria-labelledby="sc-hm-l">
<label><input type="radio" name="hm" value="fixed" checked> {L['hfixed']}</label>
<label><input type="radio" name="hm" value="sal"> {L['hsal']}</label>
</div></div>
<div class="row">
<div class="fld" id="sc-rate-f"><label for="sc-rate">{L['hrate']}</label><input type="number" id="sc-rate" min="0" step="any" inputmode="decimal" placeholder="0"></div>
<div class="fld" id="sc-msal-f" hidden><label for="sc-msal">{L['hmsal']}</label><input type="number" id="sc-msal" min="0" step="any" inputmode="decimal" placeholder="0"></div>
<div class="fld"><label for="sc-hw">{L['hworked']}</label><input type="number" id="sc-hw" min="0" step="0.25" inputmode="decimal" placeholder="0"></div>
</div>
<div class="row">
<div class="fld"><label for="sc-std">{L['hstd']}</label><input type="number" id="sc-std" min="1" step="1" value="208"><p class="hint">{L['hstdh']}</p></div>
<div class="fld"><label for="sc-pct">{L['hpct']}</label><input type="number" id="sc-pct" min="0" step="1" value="125"><p class="hint">{L['hpcth']}</p></div>
</div>
</div>
<div class="res" id="sc-out" aria-live="polite"></div>
<p class="hint">{L['disc']}</p>
</form>"""


EX_EN = [("Full salary, 3 unpaid days", "Basic 400 + housing 150 + transport 50 = OMR 600", "600 ÷ 30 = 20 a day; 20 × 3 = 60", "OMR 540"),
         ("Basic only, 3 unpaid days", "Same salary", "400 ÷ 30 = 13.333 a day; × 3 = 40", "OMR 560"),
         ("Joined on the 11th (20 days worked)", "Full salary OMR 600", "600 ÷ 30 × 20", "OMR 400"),
         ("Hourly, fixed rate, 220 hours", "OMR 2.500 an hour, 208 standard hours, extra at 125%", "208 × 2.5 + 12 × 2.5 × 1.25", "OMR 557.500"),
         ("Hourly, salary by hours, 190 hours", "Salary OMR 520, 208 standard hours", "520 − 520 × 18 ÷ 208", "OMR 475")]
EX_AR = [("الراتب الكامل، 3 أيام بدون أجر", "أساسي 400 + سكن 150 + نقل 50 = 600 ريال عماني", "600 ÷ 30 = 20 يوميًا؛ 20 × 3 = 60", "540 ريالًا"),
         ("الأساسي فقط، 3 أيام بدون أجر", "الراتب نفسه", "400 ÷ 30 = 13.333 يوميًا؛ × 3 = 40", "560 ريالًا"),
         ("التحق يوم 11 (20 يوم عمل)", "راتب كامل 600 ريال", "600 ÷ 30 × 20", "400 ريال"),
         ("بالساعة، سعر ثابت، 220 ساعة", "2.500 ريال للساعة، 208 ساعات قياسية، الإضافي 125%", "208 × 2.5 + 12 × 2.5 × 1.25", "557.500 ريال"),
         ("بالساعة، الراتب حسب الساعات، 190 ساعة", "راتب 520 ريالًا، 208 ساعات قياسية", "520 − 520 × 18 ÷ 208", "475 ريالًا")]

EN_BODY = f"""
<p class="crumbs"><a href="/">Home</a> › Free salary calculator</p>
<h1>Free salary calculator for absences, unpaid leave, days worked and hourly pay</h1>
<p class="updated"><span class="free">FREE</span>No sign-up · Works for any currency</p>
<p class="lead">Work out a daily salary rate, the deduction for absent or unpaid leave days, the pay for an employee who worked only part of the month, or hourly pay with extra hours. Choose whether the calculation uses the full salary, basic salary only, or basic plus selected allowances.</p>
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
<h1>حاسبة الراتب المجانية للغياب والإجازة بدون أجر وأيام العمل والأجر بالساعة</h1>
<p class="updated"><span class="free">مجانية</span>بدون تسجيل · تعمل مع أي عملة</p>
<p class="lead">احسب الأجر اليومي، وخصم أيام الغياب أو الإجازة بدون أجر، أو راتب موظف عمل جزءًا من الشهر فقط، أو الأجر بالساعة مع الساعات الإضافية. اختر إن كان الحساب على الراتب الكامل، أو الأساسي فقط، أو الأساسي مع بدلات تختارها.</p>
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
        ("en", en_url, ar_url, "Free Salary & Hourly Pay Calculator: Absence, Days Worked",
         "Free salary calculator: deductions for absent or unpaid days, pay for days worked, and hourly pay with extra hours. Full salary, basic only or chosen allowances.",
         EN_BODY, "/", "Back to home",
         "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Figtree:wght@400;600;700&display=swap",
         '"Figtree","Segoe UI",system-ui,sans-serif', '"Bricolage Grotesque","Segoe UI",sans-serif',
         '<a href="/">Home</a> · <a href="/gratuity-calculator/">Free gratuity calculator</a> · <a href="/salary-software-guide/">Buyer\'s guide</a> · <a href="/ar/salary-calculator/" hreflang="ar" lang="ar">العربية</a> · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a>',
         "Free salary calculator for absences, unpaid leave, days worked and hourly pay", os.path.join(out_dir, "salary-calculator"), FAQ_EN),
        ("ar", ar_url, en_url, "حاسبة الراتب والأجر بالساعة المجانية: الغياب وأيام العمل | PayCore",
         "حاسبة راتب مجانية: احسب الأجر اليومي وخصم أيام الغياب أو الإجازة بدون أجر أو الراتب عن أيام العمل، على الراتب الكامل أو الأساسي أو بدلات تختارها.",
         AR_BODY, "/ar/", "العودة للرئيسية",
         "https://fonts.googleapis.com/css2?family=Cairo:wght@700;800&family=IBM+Plex+Sans+Arabic:wght@400;600;700&display=swap",
         '"IBM Plex Sans Arabic","Segoe UI",Tahoma,sans-serif', '"Cairo","Segoe UI",Tahoma,sans-serif',
         '<a href="/ar/">الرئيسية</a> · <a href="/ar/gratuity-calculator/">حاسبة مكافأة نهاية الخدمة المجانية</a> · <a href="/ar/salary-software-guide/">دليل اختيار برنامج الرواتب</a> · <a href="/salary-calculator/" hreflang="en" lang="en">English</a> · <a href="/privacy.html">سياسة الخصوصية</a> · <a href="/terms.html">شروط الاستخدام</a>',
         "حاسبة الراتب المجانية للغياب والإجازة بدون أجر وأيام العمل والأجر بالساعة", os.path.join(out_dir, "ar", "salary-calculator"), FAQ_AR),
    ]
    for lang, url, alt, title, desc, body, home, back, fonts, bf, df, links, headline, folder, faq in pages:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(gratuity._page(lang, url, alt, title, desc, body.strip(), home, back, fonts, bf, df, links,
                                    site_url, year, headline, faq, js=JS, extra_css=CSS))
    return en_url, ar_url
