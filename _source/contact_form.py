"""Contact form shared by the English homepage and the Arabic page.

The form has no server: the main button opens WhatsApp with the visitor's details typed into
a message to PayCore; the second button opens their email app with the same details.
Imported by build.py (English, injected at <!--CONTACT_FORM-->) and ar.py (Arabic).
"""

WA_NUMBER = "96890959084"
EMAIL = "info@paycoresalarysystem.com"

CSS = """
/* contact form */
.cform{background:#fff;border:1px solid var(--line);border-radius:24px;padding:32px;display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:32px;align-items:start}
@media (max-width:860px){.cform{grid-template-columns:1fr;padding:24px 20px}}
.cform h2{margin:0}
.cform .intro p{color:var(--muted);margin-top:12px}
.cform form{display:grid;grid-template-columns:1fr 1fr;gap:14px 16px}
@media (max-width:560px){.cform form{grid-template-columns:1fr}}
.cform .full{grid-column:1/-1}
.cform label{display:grid;gap:6px;font-weight:600;font-size:15px;min-width:0}
.cform label span.opt{font-weight:400;color:var(--muted);font-size:13px}
.cform input,.cform select,.cform textarea{font:inherit;font-size:16px;color:var(--ink);background:#f8faff;border:1.5px solid var(--line);border-radius:12px;padding:12px 14px;width:100%;transition:border-color .2s,box-shadow .2s}
.cform textarea{min-height:110px;resize:vertical}
.cform input:focus,.cform select:focus,.cform textarea:focus{outline:none;border-color:#2563eb;box-shadow:0 0 0 4px rgba(37,99,235,.15);background:#fff}
.cform .acts{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.cform .send-wa{display:inline-flex;align-items:center;gap:10px;border:0;cursor:pointer;font-family:inherit;font-weight:700;font-size:16px;line-height:1;color:#fff;background:linear-gradient(140deg,#0f9f5a,#22c55e);padding:15px 24px;border-radius:999px;box-shadow:0 10px 26px -10px rgba(22,163,74,.6);transition:transform .2s}
.cform .send-wa:hover{transform:translateY(-2px)}
.cform .send-wa svg{width:20px;height:20px}
.cform .send-em{border:1.5px solid var(--line);background:#fff;color:var(--ink);cursor:pointer;font-family:inherit;font-weight:600;font-size:15px;line-height:1;padding:13px 18px;border-radius:999px}
.cform .cf-note{font-size:13.5px;color:var(--muted);margin:0;background:none;border:0;padding:0}
.cform .cf-err{color:#b91c1c;font-size:14px;margin:0}
.cform .lbl{display:block}
.cform input[dir=ltr]{text-align:start}
[dir=rtl] .cform input[dir=ltr]{text-align:right}
"""

WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.2-.2-.5-.3Z"/></svg>'

TEXT = {
    "en": {
        "title": 'Send us a <span class="grad-text">message</span>',
        "intro": "Tell us a little about your business and what you need. The quickest way is WhatsApp: the button opens a chat with your details already written, so you only press send.",
        "name": "Your name", "company": "Company", "contact": "Email or phone", "staff": "Number of employees",
        "need": "I'm interested in", "msg": "Message", "optional": "(optional)",
        "needs": ["Buying a license", "A free demo", "Custom features", "Something else"],
        "staffs": ["1–10", "11–50", "51–200", "More than 200"],
        "choose": "Choose…",
        "wa": "Send on WhatsApp", "em": "Send by email",
        "note": "Nothing is stored on this website. Your message goes straight to our WhatsApp or email.",
        "err": "Please add your name and choose what you're interested in.",
        "hello": "Hello PayCore,", "subject": "PayCore enquiry",
        "labels": ["Name", "Company", "Contact", "Employees", "Interested in", "Message"],
    },
    "ar": {
        "title": 'أرسل لنا <span class="grad">رسالة</span>',
        "intro": "أخبرنا قليلًا عن شركتك وما تحتاجه. أسرع طريقة هي واتساب: يفتح الزر محادثة فيها بياناتك مكتوبة مسبقًا، وما عليك إلا الضغط على إرسال.",
        "name": "الاسم", "company": "الشركة", "contact": "البريد الإلكتروني أو الهاتف", "staff": "عدد الموظفين",
        "need": "أرغب في", "msg": "الرسالة", "optional": "(اختياري)",
        "needs": ["شراء ترخيص", "عرض مجاني", "ميزات مخصصة", "شيء آخر"],
        "staffs": ["1–10", "11–50", "51–200", "أكثر من 200"],
        "choose": "اختر…",
        "wa": "أرسل عبر واتساب", "em": "أرسل بالبريد الإلكتروني",
        "note": "لا يُحفظ أي شيء على هذا الموقع. تصل رسالتك مباشرة إلى واتساب أو بريدنا الإلكتروني.",
        "err": "يرجى كتابة اسمك واختيار ما ترغب فيه.",
        "hello": "مرحبًا PayCore،", "subject": "استفسار عن PayCore",
        "labels": ["الاسم", "الشركة", "التواصل", "عدد الموظفين", "أرغب في", "الرسالة"],
    },
}


def html(lang):
    t = TEXT[lang]
    o = t["optional"]
    needs = "".join(f"<option>{n}</option>" for n in t["needs"])
    staffs = "".join(f"<option>{s}</option>" for s in t["staffs"])
    rv = ' rv' if lang == "en" else ''
    return f"""<div class="cform{rv}" id="contact">
  <div class="intro"><h2>{t['title']}</h2><p>{t['intro']}</p></div>
  <form id="cform" novalidate data-wa="{WA_NUMBER}" data-email="{EMAIL}" data-hello="{t['hello']}" data-subject="{t['subject']}" data-labels="{'|'.join(t['labels'])}">
    <label><span class="lbl">{t['name']}</span><input id="cf-name" name="name" autocomplete="name" required></label>
    <label><span class="lbl">{t['company']} <span class="opt">{o}</span></span><input id="cf-company" name="company" autocomplete="organization"></label>
    <label><span class="lbl">{t['contact']} <span class="opt">{o}</span></span><input id="cf-contact" name="contact" autocomplete="email" dir="ltr"></label>
    <label><span class="lbl">{t['staff']} <span class="opt">{o}</span></span><select id="cf-staff" name="staff"><option value="">{t['choose']}</option>{staffs}</select></label>
    <label class="full"><span class="lbl">{t['need']}</span><select id="cf-need" name="need" required><option value="">{t['choose']}</option>{needs}</select></label>
    <label class="full"><span class="lbl">{t['msg']} <span class="opt">{o}</span></span><textarea id="cf-msg" name="message"></textarea></label>
    <p class="cf-err full" id="cf-err" role="alert" hidden>{t['err']}</p>
    <div class="acts full">
      <button class="send-wa" type="submit" value="wa">{WA_ICON}{t['wa']}</button>
      <button class="send-em" type="submit" value="email">{t['em']}</button>
    </div>
    <p class="cf-note full">{t['note']}</p>
  </form>
</div>"""


JS = """<script>
(function () {
  var f = document.getElementById('cform');
  if (!f) return;
  f.addEventListener('input', function () { document.getElementById('cf-err').hidden = true; });
  f.addEventListener('change', function () { document.getElementById('cf-err').hidden = true; });
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var via = (e.submitter && e.submitter.value) || 'wa';
    var v = function (id) { var el = document.getElementById(id); return el ? el.value.trim() : ''; };
    var name = v('cf-name'), need = v('cf-need'), err = document.getElementById('cf-err');
    if (!name || !need) { err.hidden = false; (name ? document.getElementById('cf-need') : document.getElementById('cf-name')).focus(); return; }
    err.hidden = true;
    var L = f.getAttribute('data-labels').split('|');
    var vals = [name, v('cf-company'), v('cf-contact'), v('cf-staff'), need, v('cf-msg')];
    var lines = [f.getAttribute('data-hello'), ''];
    for (var i = 0; i < L.length; i++) { if (vals[i]) lines.push(L[i] + ': ' + vals[i]); }
    var text = lines.join('\\n');
    if (via === 'email') {
      window.location.href = 'mailto:' + f.getAttribute('data-email') + '?subject=' +
        encodeURIComponent(f.getAttribute('data-subject') + ' – ' + name) + '&body=' + encodeURIComponent(text);
    } else {
      var url = 'https://wa.me/' + f.getAttribute('data-wa') + '?text=' + encodeURIComponent(text);
      var w = window.open(url, '_blank', 'noopener');
      if (!w) window.location.href = url;
    }
  });
})();
</script>"""
