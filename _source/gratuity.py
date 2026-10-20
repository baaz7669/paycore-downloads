"""Free end-of-service gratuity calculator pages (Oman, UAE, Saudi Arabia).

  /gratuity-calculator/      (English)
  /ar/gratuity-calculator/   (Arabic)

Targets "gratuity calculator Oman", "end of service calculator", "حساب مكافأة نهاية الخدمة".
Rules checked on 2026-10-19 (see SOURCES). Re-check before changing CHECKED, especially
Oman's savings system start date (latest legal date: 19 July 2027).
Edit the text below, then run build.py.
"""
import html, json, os
import guide

CHECKED = "October 2026"
CHECKED_AR = "أكتوبر 2026"

SOURCES = [
 ("Teamed: Oman end-of-service gratuity and the 9% savings system", "https://www.teamed.global/gulf-employment-law/oman-end-of-service-and-savings-system"),
 ("HLB Hamt: End-of-service gratuity in Oman", "https://hlbhamt.com/insights/end-of-service-gratuity-in-oman/"),
 ("Oman Observer: How employees' gratuity will be calculated in Oman (Ministry of Labour clarification)", "https://www.omanobserver.om/article/1161053/oman/labour/how-employees-gratuity-will-be-calculated-in-oman-for-now"),
 ("Gulf Business: Oman clarifies end-of-service gratuity rules (August 2026)", "https://gulfbusiness.com/en/2026/oman/oman-clarifies-end-of-service-gratuity-rules-in-key-labour-update/"),
 ("Khaleej Times: UAE gratuity calculator and rules", "https://www.khaleejtimes.com/uae/jobs/gratuity-calculator"),
 ("Saudi Ministry of Human Resources: end-of-service award", "https://www.hrsd.gov.sa/en/knowledge-centre/articles/317-0"),
 ("ZenHR: How to calculate end-of-service benefits in Saudi Arabia", "https://blog.zenhr.com/en/how-to-calculate-end-of-service-benefits-esb-in-saudi-arabia-2026-guide"),
]

FAQ_EN = [
 ("How is end-of-service gratuity calculated in Oman?",
  "Under Article 61 of the Oman Labour Law (Royal Decree 53/2023), a non-Omani employee gets at least one month of their last basic wage for each year of service from 1 August 2023, with part years paid in proportion. Service up to 31 July 2023 follows the previous law: 15 days' basic wage for each of the first three years and a month for each later year, as the Ministry of Labour has clarified. Allowances are not included. Omani employees are covered by the Social Protection Fund instead of a gratuity."),
 ("Is Oman replacing gratuity with a savings system?",
  "Yes. The Social Protection Law (Royal Decree 52/2023) will replace gratuity for expatriates with a savings system: the employer pays 9% of the basic wage each month. The Social Protection Fund sets the start date, which must be no later than 19 July 2027. When we checked in October 2026, no start date had been announced. Gratuity earned before the start date is still owed."),
 ("How is gratuity calculated in the UAE?",
  "After one year of continuous service, a private-sector employee gets 21 days of basic salary for each of the first five years and 30 days for each year after that, with part years paid in proportion. The daily wage is the basic monthly salary divided by 30, and the total can't be more than two years' wage. Days of unpaid absence don't count."),
 ("How is the end-of-service award calculated in Saudi Arabia?",
  "Half a month's wage for each of the first five years and a full month's wage for each year after that, based on the last wage, with part years paid in proportion. The wage includes fixed allowances such as housing and transport. If the employee resigns, they get nothing under 2 years, one third for 2 to 5 years, two thirds for 5 to 10 years, and the full award after 10 years."),
 ("Do I get gratuity if I resign?",
  "In Oman and the UAE, resigning doesn't reduce gratuity under the current laws. In Saudi Arabia it does, depending on years of service. Dismissal for serious misconduct can change the result in any country, so check your own case."),
 ("Does PayCore calculate gratuity automatically?",
  "Yes. PayCore keeps each employee's joining date and salary and calculates end-of-service gratuity at the rate you set, alongside monthly payroll, loans and payslips. It's a one-time USD 50 license for unlimited employees."),
]
FAQ_AR = [
 ("كيف تُحسب مكافأة نهاية الخدمة في سلطنة عمان؟",
  "بموجب المادة 61 من قانون العمل العماني (المرسوم السلطاني 53/2023)، يستحق العامل غير العماني أجرًا أساسيًا لشهر واحد على الأقل عن كل سنة خدمة اعتبارًا من 1 أغسطس 2023، بحسب آخر أجر أساسي، وتُحسب أجزاء السنة بنسبتها. أما الخدمة حتى 31 يوليو 2023 فتخضع للقانون السابق: أجر 15 يومًا عن كل سنة من السنوات الثلاث الأولى، وأجر شهر عن كل سنة بعدها، وفق توضيح وزارة العمل. لا تدخل البدلات في الحساب. أما العمانيون فيشملهم صندوق الحماية الاجتماعية بدلًا من المكافأة."),
 ("هل ستستبدل عمان مكافأة نهاية الخدمة بنظام ادخار؟",
  "نعم. قانون الحماية الاجتماعية (المرسوم السلطاني 52/2023) سيستبدل مكافأة نهاية الخدمة للعمال الوافدين بنظام ادخار يدفع فيه صاحب العمل 9% من الأجر الأساسي شهريًا. يحدد صندوق الحماية الاجتماعية تاريخ البدء، على ألا يتجاوز 19 يوليو 2027. عند مراجعتنا في أكتوبر 2026 لم يُعلن تاريخ البدء بعد. والمكافأة المستحقة عن الخدمة قبل تاريخ البدء تبقى حقًا للعامل."),
 ("كيف تُحسب مكافأة نهاية الخدمة في الإمارات؟",
  "بعد إتمام سنة خدمة متصلة، يستحق العامل في القطاع الخاص أجر 21 يومًا من الراتب الأساسي عن كل سنة من السنوات الخمس الأولى، و30 يومًا عن كل سنة بعدها، وتُحسب أجزاء السنة بنسبتها. الأجر اليومي هو الراتب الأساسي الشهري مقسومًا على 30، ولا يزيد المجموع على أجر سنتين. ولا تُحتسب أيام الغياب بدون أجر."),
 ("كيف تُحسب مكافأة نهاية الخدمة في السعودية؟",
  "نصف أجر شهر عن كل سنة من السنوات الخمس الأولى، وأجر شهر كامل عن كل سنة بعدها، على أساس آخر أجر، وتُحسب أجزاء السنة بنسبتها. يشمل الأجر البدلات الثابتة مثل السكن والنقل. وإذا استقال العامل فلا يستحق شيئًا قبل سنتين، ويستحق الثلث من سنتين إلى خمس، والثلثين من خمس إلى عشر، والمكافأة كاملة بعد عشر سنوات."),
 ("هل أستحق المكافأة إذا استقلت؟",
  "في عمان والإمارات لا تقلل الاستقالة المكافأة وفق القوانين الحالية. أما في السعودية فتقل بحسب سنوات الخدمة. وقد يغيّر الفصل بسبب مخالفة جسيمة النتيجة في أي بلد، لذا تحقق من حالتك."),
 ("هل يحسب PayCore مكافأة نهاية الخدمة تلقائيًا؟",
  "نعم. يحفظ PayCore تاريخ التعيين والراتب لكل موظف ويحسب مكافأة نهاية الخدمة بالنسبة التي تحددها، إلى جانب الرواتب الشهرية والسلف وقسائم الرواتب. والترخيص لمرة واحدة بـ 50 دولارًا لعدد غير محدود من الموظفين."),
]

CALC_CSS = """
.calc{border:1px solid var(--line);border-radius:20px;padding:24px;margin:26px 0;background:linear-gradient(180deg,#fbfcff,#f4f8ff)}
.calc .row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media (max-width:640px){.calc{padding:18px 14px}.calc .row{grid-template-columns:1fr}}
.calc label{display:block;font-weight:700;font-size:15px;margin:0 0 6px}
.calc .fld{margin-bottom:14px;min-width:0}
.calc input,.calc select{width:100%;font:inherit;font-size:16px;padding:11px 12px;border:1px solid #c9d5ea;border-radius:12px;background:#fff;color:var(--ink);min-width:0}
.calc input:focus,.calc select:focus{outline:3px solid #bfd3ff;border-color:var(--blue)}
.calc .hint{font-size:13.5px;color:var(--muted);margin:5px 0 0;line-height:1.5}
.seg{display:flex;flex-wrap:wrap;gap:8px}
.seg label{font-weight:600;margin:0;display:flex;align-items:center;gap:8px;border:1px solid #c9d5ea;background:#fff;border-radius:999px;padding:8px 14px;cursor:pointer}
.seg input{width:auto;margin:0}
.seg label:has(input:checked){border-color:var(--blue);background:#eef3ff;color:var(--blue)}
.res{margin-top:6px;border-radius:16px;background:#fff;border:1px solid var(--line);padding:18px 20px}
.res .big{font:800 clamp(28px,6vw,40px)/1.15 %DISPFONT%;color:var(--mint);font-variant-numeric:tabular-nums;margin:2px 0 6px}
.res .lbl{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:700}
.res ul{margin:8px 0 0;padding-inline-start:20px;font-size:15.5px;color:var(--muted)}
.res .warn{color:#9a3412}
.ex td,.ex th{white-space:normal}
.also{margin-top:34px;padding:14px 18px;border-radius:14px;background:#f0fdf6;border:1px solid #c9f2df;font-weight:600}
.free{display:inline-block;vertical-align:middle;font:800 13px/1 sans-serif;letter-spacing:.08em;color:#fff;background:#059669;border-radius:999px;padding:6px 10px;margin-inline-end:10px}
"""

# The calculator reads its words from data attributes so one script serves both languages.
JS = r"""
(function(){
 var f=document.getElementById('gc'); if(!f) return;
 var T=JSON.parse(f.getAttribute('data-t'));
 var $=function(id){return document.getElementById(id)};
 var CUR={om:['OMR',3],ae:['AED',2],sa:['SAR',2]};
 function country(){return f.querySelector('input[name=c]:checked').value}
 function fmt(v,d){return v.toLocaleString(T.locale,{minimumFractionDigits:d,maximumFractionDigits:d})}
 function day(s){var p=s.split('-');return Date.UTC(+p[0],+p[1]-1,+p[2])}
 function sync(){
  var c=country();
  $('gc-sal-l').textContent=T.sal[c]; $('gc-sal-h').textContent=T.salh[c];
  $('gc-why').hidden=(c!=='sa'); $('gc-cur').textContent=CUR[c][0];
  calc();
 }
 function calc(){
  var c=country(), cur=CUR[c][0], d=CUR[c][1], out=$('gc-out');
  var s=$('gc-s').value, e=$('gc-e').value, sal=parseFloat($('gc-sal').value), un=parseFloat($('gc-un').value)||0;
  if(!s||!e||!(sal>0)){out.innerHTML='<p class="hint">'+T.fill+'</p>';return}
  var a=new Date(day(s)), b=new Date(day(e)+864e5);
  if(b<=a){out.innerHTML='<p class="warn">'+T.order+'</p>';return}
  function add(dt,yy,mm){var r=new Date(dt);r.setUTCFullYear(r.getUTCFullYear()+yy,r.getUTCMonth()+mm);return r}
  var yy=b.getUTCFullYear()-a.getUTCFullYear(); if(add(a,yy,0)>b) yy--;
  var mm=0; while(add(a,yy,mm+1)<=b) mm++;
  var dd=Math.round((b-add(a,yy,mm))/864e5);
  var y=yy+Math.round((b-add(a,yy,0))/864e5)/365-Math.max(0,un)/365;
  if(y<=0){out.innerHTML='<p class="warn">'+T.order+'</p>';return}
  var lines=[], amt=0, note='';
  lines.push(T.service.replace('{y}',yy).replace('{m}',mm).replace('{d}',dd).replace('{t}',fmt(y,2))+(un>0?T.minus.replace('{u}',un):''));
  if(c==='om'){
   var C=new Date(Date.UTC(2023,7,1));
   function yrs(p,q){if(q<=p)return 0;var n=q.getUTCFullYear()-p.getUTCFullYear();if(add(p,n,0)>q)n--;return n+Math.round((q-add(p,n,0))/864e5)/365}
   var oy=Math.min(yrs(a,b<C?b:C),y), ny=Math.max(0,y-oy);
   var o1=Math.min(oy,3), o2=Math.max(0,oy-3);
   amt=sal*(o1/2+o2+ny);
   if(oy>0) lines.push(T.omOld.replace('{t}',fmt(oy,2)).replace('{a}',fmt(o1,2)).replace('{b}',fmt(o2,2)).replace('{x}',cur+' '+fmt(sal*(o1/2+o2),d)));
   lines.push(T.om1.replace('{s}',cur+' '+fmt(sal,d)).replace('{t}',fmt(ny,2)).replace('{x}',cur+' '+fmt(sal*ny,d)));
   note=T.omNote;
  } else if(c==='ae'){
   if(y<1){out.innerHTML=res(0,cur,d,lines.concat([T.ae0]));return}
   var dw=sal/30, d1=Math.min(y,5)*21, d2=Math.max(0,y-5)*30;
   amt=dw*(d1+d2);
   lines.push(T.ae1.replace('{w}',cur+' '+fmt(dw,2)).replace('{a}',fmt(d1,1)).replace('{b}',fmt(d2,1)));
   if(amt>sal*24){amt=sal*24;lines.push(T.aeCap)}
  } else {
   var full=Math.min(y,5)*sal/2+Math.max(0,y-5)*sal;
   lines.push(T.sa1.replace('{f}',cur+' '+fmt(full,d)));
   if($('gc-why').querySelector('input:checked').value==='r'){
    var k=y<2?0:(y<=5?1/3:(y<10?2/3:1));
    lines.push(T.saR[k===0?0:k<.5?1:k<1?2:3]); amt=full*k;
   } else amt=full;
  }
  out.innerHTML=res(amt,cur,d,lines)+(note?'<p class="hint">'+note+'</p>':'');
 }
 function res(a,cur,d,lines){
  return '<div class="lbl">'+T.est+'</div><div class="big">'+cur+' '+fmt(a,d)+'</div><ul>'+lines.map(function(l){return '<li>'+l+'</li>'}).join('')+'</ul>';
 }
 f.addEventListener('input',function(ev){ev.target.name==='c'?sync():calc()});
 f.addEventListener('change',function(ev){ev.target.name==='c'?sync():calc()});
 f.addEventListener('submit',function(ev){ev.preventDefault();calc()});
 var t=new Date(); $('gc-e').value=t.toISOString().slice(0,10);
 sync();
})();
"""

T_EN = {
 "locale": "en-US",
 "sal": {"om": "Last basic monthly salary", "ae": "Basic monthly salary", "sa": "Last monthly wage"},
 "salh": {"om": "Basic wage only. Don't include housing, transport or other allowances.",
          "ae": "Basic salary only. Don't include housing, transport or other allowances.",
          "sa": "Basic wage plus fixed allowances such as housing and transport, unless your contract says otherwise."},
 "fill": "Enter the start date, end date and salary to see the gratuity.",
 "order": "The end date must be after the start date.",
 "est": "Estimated gratuity",
 "service": "Service: {y} yr {m} mo {d} days ({t} years)",
 "minus": ", after taking off {u} unpaid days",
 "om1": "From 1 August 2023 (current law): {t} years × {s} (one month of basic wage per year) = {x}",
 "omOld": "Up to 31 July 2023 (previous law): {t} years, at 15 days' basic for the first 3 years ({a}) and a month for later years ({b}) = {x}",
 "omNote": "For non-Omani employees. Omani employees are covered by the Social Protection Fund instead. Oman plans to replace gratuity with a 9% savings system no later than 19 July 2027; gratuity earned before then is still owed.",
 "ae0": "No gratuity before one year of continuous service.",
 "ae1": "Daily wage {w}: {a} days for the first 5 years + {b} days after",
 "aeCap": "Capped at two years' basic salary.",
 "sa1": "Full award: {f} (half a month per year for 5 years, then a month per year)",
 "saR": ["Resigned under 2 years: no award.", "Resigned after 2–5 years: one third of the award.",
         "Resigned after 5–10 years: two thirds of the award.", "Resigned after 10 years or more: full award."],
}
T_AR = {
 "locale": "ar-OM-u-nu-latn",
 "sal": {"om": "آخر راتب أساسي شهري", "ae": "الراتب الأساسي الشهري", "sa": "آخر أجر شهري"},
 "salh": {"om": "الأجر الأساسي فقط، بدون بدل السكن أو النقل أو غيرها.",
          "ae": "الراتب الأساسي فقط، بدون بدل السكن أو النقل أو غيرها.",
          "sa": "الأجر الأساسي مع البدلات الثابتة مثل السكن والنقل، ما لم ينص العقد على غير ذلك."},
 "fill": "أدخل تاريخ البداية وتاريخ النهاية والراتب لعرض المكافأة.",
 "order": "يجب أن يكون تاريخ النهاية بعد تاريخ البداية.",
 "est": "المكافأة التقديرية",
 "service": "مدة الخدمة: السنوات {y} · الأشهر {m} · الأيام {d} ({t} سنة)",
 "minus": "، بعد خصم {u} يوم بدون أجر",
 "om1": "من 1 أغسطس 2023 (القانون الحالي): {t} سنة × {s} (أجر أساسي لشهر عن كل سنة) = {x}",
 "omOld": "حتى 31 يوليو 2023 (القانون السابق): {t} سنة، بأجر 15 يومًا عن أول 3 سنوات ({a}) وأجر شهر عن السنوات التالية ({b}) = {x}",
 "omNote": "للعاملين غير العمانيين. أما العمانيون فيشملهم صندوق الحماية الاجتماعية. وتخطط عمان لاستبدال المكافأة بنظام ادخار بنسبة 9% في موعد أقصاه 19 يوليو 2027، مع بقاء المكافأة المستحقة قبل ذلك.",
 "ae0": "لا مكافأة قبل إتمام سنة خدمة متصلة.",
 "ae1": "الأجر اليومي {w}: {a} يومًا عن أول 5 سنوات + {b} يومًا بعدها",
 "aeCap": "بحد أقصى أجر سنتين من الراتب الأساسي.",
 "sa1": "المكافأة الكاملة: {f} (نصف شهر عن كل سنة لأول 5 سنوات، ثم شهر عن كل سنة)",
 "saR": ["استقالة قبل سنتين: لا مكافأة.", "استقالة بعد 2 إلى 5 سنوات: ثلث المكافأة.",
         "استقالة بعد 5 إلى 10 سنوات: ثلثا المكافأة.", "استقالة بعد 10 سنوات أو أكثر: المكافأة كاملة."],
}


def _form(t, L):
    data = html.escape(json.dumps(t, ensure_ascii=False), quote=True)
    return f"""<form class="calc" id="gc" data-t="{data}" novalidate>
<div class="fld"><label id="gc-c-l">{L['country']}</label>
<div class="seg" role="radiogroup" aria-labelledby="gc-c-l">
<label><input type="radio" name="c" value="om" checked> {L['om']}</label>
<label><input type="radio" name="c" value="ae"> {L['ae']}</label>
<label><input type="radio" name="c" value="sa"> {L['sa']}</label>
</div></div>
<div class="row">
<div class="fld"><label for="gc-s">{L['start']}</label><input type="date" id="gc-s" required></div>
<div class="fld"><label for="gc-e">{L['end']}</label><input type="date" id="gc-e" required></div>
</div>
<div class="row">
<div class="fld"><label for="gc-sal"><span id="gc-sal-l"></span> (<span id="gc-cur"></span>)</label><input type="number" id="gc-sal" min="0" step="any" inputmode="decimal" placeholder="0"><p class="hint" id="gc-sal-h"></p></div>
<div class="fld"><label for="gc-un">{L['unpaid']}</label><input type="number" id="gc-un" min="0" step="1" inputmode="numeric" placeholder="0"><p class="hint">{L['unpaidh']}</p></div>
</div>
<div class="fld" id="gc-why" hidden><label id="gc-why-l">{L['why']}</label>
<div class="seg" role="radiogroup" aria-labelledby="gc-why-l">
<label><input type="radio" name="w" value="t" checked> {L['term']}</label>
<label><input type="radio" name="w" value="r"> {L['resign']}</label>
</div></div>
<div class="res" id="gc-out" aria-live="polite"></div>
<p class="hint">{L['disc']}</p>
</form>"""


L_EN = {"country": "Country", "om": "Oman", "ae": "UAE", "sa": "Saudi Arabia",
        "start": "First working day", "end": "Last working day",
        "unpaid": "Unpaid leave days (optional)", "unpaidh": "Days of unpaid absence are taken off the service period.",
        "why": "How did the job end?", "term": "Contract ended or employer terminated", "resign": "Employee resigned",
        "disc": "An estimate based on the labour law rules below. It's not legal advice; contracts can be more generous, and special cases (such as dismissal for misconduct) are not covered."}
L_AR = {"country": "الدولة", "om": "عمان", "ae": "الإمارات", "sa": "السعودية",
        "start": "أول يوم عمل", "end": "آخر يوم عمل",
        "unpaid": "أيام الإجازة بدون أجر (اختياري)", "unpaidh": "تُخصم أيام الغياب بدون أجر من مدة الخدمة.",
        "why": "كيف انتهى العمل؟", "term": "انتهى العقد أو أنهاه صاحب العمل", "resign": "استقال العامل",
        "disc": "تقدير مبني على قواعد قانون العمل أدناه، وليس استشارة قانونية. قد تكون العقود أكثر سخاءً، ولا يشمل الحالات الخاصة مثل الفصل بسبب مخالفة."}


def _ex_table(rows, heads):
    head = "".join(f"<th scope='col'>{h}</th>" for h in heads)
    body = "".join("<tr>" + "".join(f"<td>{html.escape(c)}</td>" if i else f"<th scope='row'>{html.escape(c)}</th>" for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f"<div class='tbl ex' tabindex='0'><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>"


RULES_EN = [
 ("Oman (non-Omanis)", "One month of last basic wage per year from 1 August 2023; before that, 15 days a year for the first 3 years, then a month", "Part years in proportion; no reduction for resignation", "Labour Law 53/2023, Article 61"),
 ("UAE (private sector)", "21 days of basic per year for 5 years, then 30 days", "Needs 1 year of service; capped at 2 years' wage", "Decree-Law 33/2021, Article 51"),
 ("Saudi Arabia", "Half a month's wage per year for 5 years, then a month", "Reduced if the employee resigns before 10 years", "Labour Law, Articles 84–85"),
]
RULES_AR = [
 ("عمان (غير العمانيين)", "أجر أساسي لشهر عن كل سنة من 1 أغسطس 2023، وقبلها أجر 15 يومًا عن كل سنة لأول 3 سنوات ثم شهر", "أجزاء السنة بنسبتها، ولا تقل بالاستقالة", "قانون العمل 53/2023، المادة 61"),
 ("الإمارات (القطاع الخاص)", "21 يومًا من الأساسي عن كل سنة لأول 5 سنوات، ثم 30 يومًا", "تشترط سنة خدمة، وبحد أقصى أجر سنتين", "المرسوم بقانون 33/2021، المادة 51"),
 ("السعودية", "نصف أجر شهر عن كل سنة لأول 5 سنوات، ثم شهر", "تقل إذا استقال العامل قبل 10 سنوات", "نظام العمل، المادتان 84 و85"),
]
EX_EN = [
 ("Oman, joined after July 2023", "Basic OMR 400, 3 years", "400 × 3", "OMR 1,200"),
 ("Oman, joined before July 2023", "Basic OMR 500, 1 Aug 2021 to 31 Jul 2026", "2 years × 250 (old law) + 3 years × 500", "OMR 2,000"),
 ("UAE", "Basic AED 6,000, 7 years", "200 a day × (105 + 60 days)", "AED 33,000"),
 ("Saudi Arabia", "Wage SAR 8,000, 7 years", "20,000 + 16,000 (two thirds if resigned)", "SAR 36,000 (24,000)"),
]
EX_AR = [
 ("عمان، التحق بعد يوليو 2023", "أساسي 400 ريال، 3 سنوات", "400 × 3", "1,200 ريال عماني"),
 ("عمان، التحق قبل يوليو 2023", "أساسي 500 ريال، من 1 أغسطس 2021 إلى 31 يوليو 2026", "سنتان × 250 (القانون السابق) + 3 سنوات × 500", "2,000 ريال عماني"),
 ("الإمارات", "أساسي 6,000 درهم، 7 سنوات", "200 درهم يوميًا × (105 + 60 يومًا)", "33,000 درهم"),
 ("السعودية", "أجر 8,000 ريال، 7 سنوات", "20,000 + 16,000 (الثلثان عند الاستقالة)", "36,000 ريال (24,000)"),
]


def _sources(label):
    items = "".join(f'<li><a href="{u}" rel="noopener">{html.escape(t)}</a></li>' for t, u in SOURCES)
    return f'<div class="sources"><h2>{label}</h2><ul>{items}</ul></div>'


EN_BODY = f"""
<p class="crumbs"><a href="/">Home</a> › Free gratuity calculator</p>
<h1>Free end-of-service gratuity calculator for Oman, UAE and Saudi Arabia</h1>
<p class="updated"><span class="free">FREE</span>Rules checked {CHECKED} · Free, no sign-up</p>
<p class="lead">Work out an employee's end-of-service gratuity in seconds. Pick the country, enter the dates and salary, and the calculator applies that country's labour law and shows how it got the number.</p>
{_form(T_EN, L_EN)}
<h2>How gratuity works in each country</h2>
{_ex_table(RULES_EN, ["Country", "Rate", "Conditions", "Law"])}
<h2>Worked examples</h2>
{_ex_table(EX_EN, ["Country", "Employee", "Calculation", "Gratuity"])}
<p class="note">Oman: the Ministry of Labour's own example uses this split, with half a month's basic for each year before the new law and a full month after it. UAE daily wage is the basic salary divided by 30: AED 6,000 ÷ 30 = AED 200. Seven years gives 5 × 21 = 105 days plus 2 × 30 = 60 days.</p>
<h2>Oman's change to a savings system</h2>
<p>Oman's Social Protection Law will replace gratuity for expatriate employees with a savings system funded by the employer at 9% of the basic wage each month. The Social Protection Fund decides the start date, which can't be later than 19 July 2027. Until it starts, employers keep paying gratuity under Article 61, and gratuity for service before the start date is still owed.</p>
<h2>Common questions</h2>
<div class="faq">{guide._faq_html(FAQ_EN)}</div>
<p class="also">Also free: <a href="/salary-calculator/">salary calculator for absences, unpaid leave and days worked</a>.</p>
<div class="cta"><p><strong>Calculate gratuity for your whole team</strong>PayCore keeps every employee's joining date and salary, and works out gratuity, payroll, loans and payslips on your own PC. One-time USD 50, unlimited employees.</p><a href="/#download">Get PayCore</a></div>
{_sources("Sources")}
"""

AR_BODY = f"""
<p class="crumbs"><a href="/ar/">الرئيسية</a> › حاسبة مكافأة نهاية الخدمة المجانية</p>
<h1>حاسبة مكافأة نهاية الخدمة المجانية في عمان والإمارات والسعودية</h1>
<p class="updated"><span class="free">مجانية</span>راجعنا القواعد في {CHECKED_AR} · مجانية وبدون تسجيل</p>
<p class="lead">احسب مكافأة نهاية الخدمة لأي موظف في ثوانٍ. اختر الدولة وأدخل التواريخ والراتب، وتطبق الحاسبة قانون العمل في تلك الدولة وتوضح طريقة الحساب.</p>
{_form(T_AR, L_AR)}
<h2>كيف تُحسب المكافأة في كل دولة</h2>
{_ex_table(RULES_AR, ["الدولة", "النسبة", "الشروط", "القانون"])}
<h2>أمثلة محسوبة</h2>
{_ex_table(EX_AR, ["الدولة", "الموظف", "الحساب", "المكافأة"])}
<p class="note">عمان: يستخدم مثال وزارة العمل هذا التقسيم، بنصف أجر أساسي عن كل سنة قبل القانون الجديد وأجر شهر كامل بعده. الأجر اليومي في الإمارات هو الراتب الأساسي مقسومًا على 30: 6,000 ÷ 30 = 200 درهم. سبع سنوات تعطي 5 × 21 = 105 أيام و2 × 30 = 60 يومًا.</p>
<h2>تحوّل عمان إلى نظام الادخار</h2>
<p>سيستبدل قانون الحماية الاجتماعية في عمان مكافأة نهاية الخدمة للعاملين الوافدين بنظام ادخار يموّله صاحب العمل بنسبة 9% من الأجر الأساسي شهريًا. يحدد صندوق الحماية الاجتماعية تاريخ البدء، على ألا يتجاوز 19 يوليو 2027. وإلى أن يبدأ، يستمر أصحاب العمل في دفع المكافأة وفق المادة 61، وتبقى المكافأة عن الخدمة قبل تاريخ البدء حقًا للعامل.</p>
<h2>أسئلة شائعة</h2>
<div class="faq">{guide._faq_html(FAQ_AR)}</div>
<p class="also">أداة مجانية أخرى: <a href="/ar/salary-calculator/">حاسبة الراتب للغياب والإجازة بدون أجر وأيام العمل</a>.</p>
<div class="cta"><p><strong>احسب مكافأة نهاية الخدمة لكل فريقك</strong>يحفظ PayCore تاريخ تعيين وراتب كل موظف، ويحسب المكافأة والرواتب والسلف وقسائم الرواتب على جهازك. 50 دولارًا لمرة واحدة، لعدد غير محدود من الموظفين.</p><a href="/ar/#download">احصل على PayCore</a></div>
{_sources("المصادر")}
"""


def _page(lang, url, alt_url, title, desc, body, home, back, fonts, bodyfont, dispfont, footer_links, site_url, year, headline, faq, js=None, extra_css=""):
    js = JS if js is None else js
    css = (guide.CSS + CALC_CSS + extra_css).replace("%BODYFONT%", bodyfont).replace("%DISPFONT%", dispfont)
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "@id": url + "#calculator", "name": headline, "url": url, "description": desc,
         "inLanguage": lang, "applicationCategory": "BusinessApplication", "operatingSystem": "Any (web browser)",
         "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "publisher": {"@id": site_url + "#org"}},
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
<meta property="og:type" content="website">
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
<a class="brand" href="{home}">{guide.MARK}PayCore</a>
<a class="back" href="{home}">{back}</a>
</div></div></header>
<div class="wrap">
<main>{body}</main>
<footer><span>© {year} PayCore.</span><span>{footer_links}</span></footer>
</div>
<script>{js}</script>
{guide.BEACON}
</body>
</html>
"""


def build(out_dir, site_url, year):
    en_url = site_url + "gratuity-calculator/"
    ar_url = site_url + "ar/gratuity-calculator/"
    pages = [
        ("en", en_url, ar_url, "Free Gratuity Calculator for Oman, UAE & Saudi Arabia (2026) | PayCore",
         "Free end-of-service gratuity calculator for Oman, the UAE and Saudi Arabia. Enter dates and salary to see the amount under each country's labour law, with worked examples.",
         EN_BODY, "/", "Back to home",
         "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Figtree:wght@400;600;700&display=swap",
         '"Figtree","Segoe UI",system-ui,sans-serif', '"Bricolage Grotesque","Segoe UI",sans-serif',
         '<a href="/">Home</a> · <a href="/salary-calculator/">Free salary calculator</a> · <a href="/salary-software-guide/">Buyer\'s guide</a> · <a href="/ar/gratuity-calculator/" hreflang="ar" lang="ar">العربية</a> · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a>',
         "Free end-of-service gratuity calculator", os.path.join(out_dir, "gratuity-calculator"), FAQ_EN),
        ("ar", ar_url, en_url, "حاسبة مكافأة نهاية الخدمة المجانية في عمان والإمارات والسعودية (2026) | PayCore",
         "حاسبة مجانية لمكافأة نهاية الخدمة في عمان والإمارات والسعودية. أدخل التواريخ والراتب لمعرفة المبلغ وفق قانون العمل في كل دولة، مع أمثلة محسوبة.",
         AR_BODY, "/ar/", "العودة للرئيسية",
         "https://fonts.googleapis.com/css2?family=Cairo:wght@700;800&family=IBM+Plex+Sans+Arabic:wght@400;600;700&display=swap",
         '"IBM Plex Sans Arabic","Segoe UI",Tahoma,sans-serif', '"Cairo","Segoe UI",Tahoma,sans-serif',
         '<a href="/ar/">الرئيسية</a> · <a href="/ar/salary-calculator/">حاسبة الراتب المجانية</a> · <a href="/ar/salary-software-guide/">دليل اختيار برنامج الرواتب</a> · <a href="/gratuity-calculator/" hreflang="en" lang="en">English</a> · <a href="/privacy.html">سياسة الخصوصية</a> · <a href="/terms.html">شروط الاستخدام</a>',
         "حاسبة مكافأة نهاية الخدمة المجانية", os.path.join(out_dir, "ar", "gratuity-calculator"), FAQ_AR),
    ]
    for lang, url, alt, title, desc, body, home, back, fonts, bf, df, links, headline, folder, faq in pages:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(_page(lang, url, alt, title, desc, body.strip(), home, back, fonts, bf, df, links, site_url, year, headline, faq))
    return en_url, ar_url
