#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Micro Bold Modular — Agent-03: prototype index + compare + README.
The QA harness renders any screen inside an iframe at 320/390/430 with
theme/state/motion/zoom controls — outside the phone frame so it never
pollutes direction CSS (subagent 5 architecture).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent"
PROTO = os.path.join(ROOT, "prototype")

INDEX = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Micro — نموذج Bold Modular التفاعلي · Agent-03</title>
<style>
:root { --ink:#1F1C19; --ink2:#63594F; --canvas:#F4F3F0; --surface:#fff; --brand:#D96A45; --brand-deep:#A03A1D; --trust:#1F5E8C; --pos:#1E6E42; --divider:#E6E2DA; }
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:"IBM Plex Sans Arabic", Tahoma, sans-serif; background:var(--canvas); color:var(--ink); line-height:1.65; padding:24px 16px 60px; }
.wrap { max-width:1080px; margin-inline:auto; display:flex; flex-direction:column; gap:20px; }
header.top h1 { font-size:24px; }
header.top p { color:var(--ink2); font-size:14.5px; margin-top:4px; max-width:70ch; }
.grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:14px; }
.card { background:var(--surface); border:1px solid var(--divider); border-radius:18px; padding:18px; display:flex; flex-direction:column; gap:8px; text-decoration:none; color:inherit; }
.card:hover { border-color:var(--brand); }
.card h2 { font-size:17px; display:flex; align-items:center; gap:8px; }
.dot { width:14px; height:14px; border-radius:4px; display:inline-block; }
.card p { font-size:13.5px; color:var(--ink2); }
.card .go { color:var(--trust); font-weight:700; font-size:13.5px; margin-top:auto; }
h2.sect { font-size:18px; margin-top:10px; border-inline-start:5px solid var(--brand); padding-inline-start:10px; }
label { font-size:13.5px; font-weight:700; color:var(--ink2); display:block; margin-bottom:6px; }
.row { display:flex; gap:10px; flex-wrap:wrap; align-items:flex-end; }
select, button.ctrl { min-height:44px; border:1.5px solid #8B8478; border-radius:10px; background:#fff; font-family:inherit; font-size:14px; padding:6px 12px; color:var(--ink); cursor:pointer; }
button.ctrl.primary { background:var(--brand); color:#2B130A; font-weight:700; border-color:var(--brand); }
#qa { background:var(--surface); border:1px solid var(--divider); border-radius:18px; padding:16px; display:flex; flex-direction:column; gap:12px; }
#frame-wrap { display:flex; justify-content:center; background:#EDEAE4; border-radius:14px; padding:16px; }
#qa-frame { width:390px; height:780px; border:0; background:#fff; border-radius:22px; box-shadow:0 10px 30px rgba(31,28,25,.15); transition:width .2s; max-width:100%; }
.note { font-size:13px; color:var(--ink2); }
ul.docs { font-size:14px; padding-inline-start:20px; display:flex; flex-direction:column; gap:4px; }
ul.docs a { color:var(--trust); }
.badge { display:inline-block; background:#FBEAE7; color:#B32318; font-size:12px; font-weight:700; padding:2px 10px; border-radius:99px; }
</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <h1>Micro — نموذج Bold Modular التفاعلي <span class="badge">Agent-03 · Multi-Agent</span></h1>
  <p>نموذج تصميمي تفاعلي ثابت (Static) بدون خادم ولا بيانات حقيقية، عربي RTL بالكامل. المسار الثالث المستقل — يُنفّذ بخمسة وكلاء فرعيين + Orchestrator. قابل للتشغيل من أي متصفح حديث بفتح الملفات مباشرة.</p>
</header>

<section>
  <h2 class="sect">الاتجاهات الثلاثة — عرض منفصل</h2>
  <div class="grid">
    <a class="card" href="c1-warm-bold/home.html"><h2><span class="dot" style="background:#D96A45"></span>C1 — Warm Bold</h2><p>تيراكوتا حي يقود، دفء منزلي منضبط، ثقة زرقاء ثانوية.</p><span class="go">افتح الشاشات ←</span></a>
    <a class="card" href="c2-confident-bold/home.html"><h2><span class="dot" style="background:#174E77"></span>C2 — Confident Bold</h2><p>أزرق معماري عميق للثقة والسياق، تيراكوتا لطاقة الإنشاء.</p><span class="go">افتح الشاشات ←</span></a>
    <a class="card" href="c3-dynamic-modular/home.html"><h2><span class="dot" style="background:#6E3B85"></span>C3 — Dynamic Modular</h2><p>مناطق لونية معيارية بشريط وحدة لكل قسم، لغة حالة أجرأ.</p><span class="go">افتح الشاشات ←</span></a>
  </div>
</section>

<section>
  <h2 class="sect">المقارنة والاتجاه الموصى به</h2>
  <div class="grid">
    <a class="card" href="compare/index.html"><h2>⚖️ مقارنة الاتجاهات</h2><p>الشاشة نفسها جنبًا إلى جنب عبر الاتجاهات الثلاثة مع تبديل الحالة.</p><span class="go">افتح المقارنة ←</span></a>
    <a class="card" href="selected-direction/home.html"><h2>⭐ الاتجاه الموصى به (مبدئيًا)</h2><p>الاتجاه المرشّح بعد التقييم الموزون — توصية مهنية معلّقة على اعتماد المالك واختبار المستخدم.</p><span class="go">افتح ←</span></a>
    <a class="card" href="selected-direction/design-system.html"><h2>🧩 نظام التصميم المرشّح</h2><p>Tokens وقواعد مكونات الاتجاه المختار (Candidate Design System).</p><span class="go">افتح ←</span></a>
  </div>
</section>

<section>
  <h2 class="sect">حزمة الفحص — QA Harness</h2>
  <div id="qa">
    <div class="row">
      <div><label for="qa-dir">الاتجاه</label>
        <select id="qa-dir">
          <option value="c1-warm-bold">C1 — Warm Bold</option>
          <option value="c2-confident-bold">C2 — Confident Bold</option>
          <option value="c3-dynamic-modular">C3 — Dynamic Modular</option>
          <option value="selected-direction">الاتجاه الموصى به</option>
        </select></div>
      <div><label for="qa-screen">الشاشة</label>
        <select id="qa-screen">
          <option value="home.html">مشروعي الآن</option>
          <option value="work.html">العمل</option>
          <option value="finance.html">المالية</option>
          <option value="tools.html">أدواتي</option>
          <option value="market.html">السوق</option>
          <option value="products.html">منتجاتي وخدماتي</option>
          <option value="order.html">طلب متأخر</option>
          <option value="sale.html">تسجيل بيع</option>
          <option value="more.html">المزيد</option>
        </select></div>
      <div><label for="qa-state">الحالة</label>
        <select id="qa-state">
          <option value="">(افتراضي)</option>
          <option value="positive">نتيجة موجبة</option>
          <option value="incomplete">نتيجة غير مكتملة</option>
          <option value="negative">نتيجة سالبة</option>
          <option value="empty">يوم فارغ</option>
          <option value="form">نموذج البيع</option>
          <option value="validation">خطأ تحقق</option>
          <option value="success">نجاح الحفظ</option>
          <option value="system-error">خطأ نظام</option>
        </select></div>
      <div><label for="qa-theme">الوضع</label>
        <select id="qa-theme"><option value="light">نهاري</option><option value="dark">ليلي</option></select></div>
      <div><label for="qa-w">العرض</label>
        <select id="qa-w"><option value="320">320px</option><option value="390" selected>390px</option><option value="430">430px</option></select></div>
      <div><label for="qa-zoom">تكبير النص</label>
        <select id="qa-zoom"><option value="100">100%</option><option value="200">200%</option></select></div>
      <div><label for="qa-motion">الحركة</label>
        <select id="qa-motion"><option value="full">كاملة</option><option value="reduce">مخفَّضة</option></select></div>
      <div><label for="qa-sheet">ورقة</label>
        <select id="qa-sheet"><option value="">(بلا)</option><option value="menu">قائمة الشعار</option></select></div>
      <button class="ctrl primary" id="qa-open">تشغيل</button>
    </div>
    <div id="frame-wrap"><iframe id="qa-frame" title="معاينة الشاشة" src="c1-warm-bold/home.html"></iframe></div>
    <p class="note">كل تركيبة (اتجاه + شاشة + حالة + وضع + عرض) رابط عميق قابل للتكرار — الفحص دليل يمكن إعادة إنتاجه. الحزمة خارج إطار الهاتف فلا تلوّث تنسيق الاتجاهات، وكل شاشة تظل قابلة للفتح مباشرة بلا حزمة.</p>
  </div>
</section>

<section>
  <h2 class="sect">التنقل السريع داخل كل اتجاه</h2>
  <div class="grid">
    <a class="card" href="c1-warm-bold/home.html?state=incomplete"><h2>C1 · نتيجة غير مكتملة</h2><p>الحالة الحرجة الأولى.</p></a>
    <a class="card" href="c2-confident-bold/home.html?state=incomplete"><h2>C2 · نتيجة غير مكتملة</h2><p>الحالة الحرجة الأولى.</p></a>
    <a class="card" href="c3-dynamic-modular/home.html?state=incomplete"><h2>C3 · نتيجة غير مكتملة</h2><p>الحالة الحرجة الأولى.</p></a>
    <a class="card" href="c1-warm-bold/sale.html?state=success"><h2>C1 · نجاح البيع والأثر</h2><p>الكاش المسجل الآن 161.00.</p></a>
    <a class="card" href="c2-confident-bold/sale.html?state=success"><h2>C2 · نجاح البيع والأثر</h2><p>الكاش المسجل الآن 161.00.</p></a>
    <a class="card" href="c3-dynamic-modular/sale.html?state=success"><h2>C3 · نجاح البيع والأثر</h2><p>الكاش المسجل الآن 161.00.</p></a>
  </div>
</section>

<section>
  <h2 class="sect">تعليمات التشغيل والحدود</h2>
  <ul class="docs">
    <li>التشغيل الكامل في <a href="README.md">README.md</a> — خطوة واحدة: افتح <code>index.html</code>.</li>
    <li>النطاق: نموذج تصميمي فقط — لا نظام مالي فعلي، لا مصادقة، لا بيانات حقيقية.</li>
    <li>الأجزاء خارج النطاق تفتح ورقة صادقة تصنّف نفسها (Ask Micro، النقل والتوصيل، نماذج غير البيع، السجلات التفصيلية).</li>
    <li>الوضع الليلي داخل أدواتي ← الإعدادات (قرار مقفل IA-D04)، ومتاح أيضًا من حزمة الفحص.</li>
  </ul>
</section>
</div>
<script>
(function(){
  var $ = function(id){ return document.getElementById(id); };
  function build(){
    var p = [];
    var st = $("qa-state").value; if (st) p.push("state="+st);
    var th = $("qa-theme").value; if (th && th !== "light") p.push("theme="+th);
    var zm = $("qa-zoom").value; if (zm === "200") p.push("zoom=200");
    var mo = $("qa-motion").value; if (mo === "reduce") p.push("motion=reduce");
    var sh = $("qa-sheet").value; if (sh) p.push("sheet="+sh);
    var url = $("qa-dir").value + "/" + $("qa-screen").value + (p.length ? "?"+p.join("&") : "");
    return url;
  }
  function apply(){
    $("qa-frame").style.width = $("qa-w").value + "px";
    $("qa-frame").src = build();
  }
  ["qa-dir","qa-screen","qa-state","qa-theme","qa-w","qa-zoom","qa-motion","qa-sheet"].forEach(function(id){
    $(id).addEventListener("change", apply);
  });
  $("qa-open").addEventListener("click", function(){ window.open(build(), "_blank"); });
  apply();
})();
</script>
</body>
</html>'''

COMPARE = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>مقارنة الاتجاهات — Micro Bold Modular</title>
<style>
:root { --ink:#1F1C19; --ink2:#63594F; --canvas:#F4F3F0; --surface:#fff; --brand:#D96A45; --trust:#1F5E8C; --divider:#E6E2DA; }
* { box-sizing:border-box; margin:0; padding:0; }
body { font-family:"IBM Plex Sans Arabic", Tahoma, sans-serif; background:var(--canvas); color:var(--ink); padding:20px 14px 50px; }
.wrap { max-width:1400px; margin-inline:auto; }
h1 { font-size:22px; }
p.sub { color:var(--ink2); font-size:14px; margin:4px 0 16px; }
.row { display:flex; gap:10px; flex-wrap:wrap; align-items:flex-end; margin-bottom:16px; }
label { font-size:13px; font-weight:700; color:var(--ink2); display:block; margin-bottom:4px; }
select { min-height:44px; border:1.5px solid #8B8478; border-radius:10px; background:#fff; font-family:inherit; font-size:14px; padding:4px 10px; }
.frames { display:grid; grid-template-columns:repeat(auto-fit,minmax(340px,1fr)); gap:14px; }
.frame-card { background:var(--surface); border:1px solid var(--divider); border-radius:16px; padding:12px; }
.frame-card h2 { font-size:15px; margin:2px 4px 8px; display:flex; gap:8px; align-items:center; }
.dot { width:13px; height:13px; border-radius:4px; }
.frame-card iframe { width:100%; height:720px; border:0; border-radius:14px; background:#fff; }
@media (max-width:760px){ .frame-card iframe { height:600px; } }
</style>
</head>
<body>
<div class="wrap">
<h1>مقارنة الاتجاهات الثلاثة</h1>
<p class="sub">المحتوى والأرقام والحالات متطابقة عبر الاتجاهات — الاختلاف بصري فقط (عدالة المقارنة، ملف 06). بدّل الحالة والشاشة والوضع لكل الاتجاهات معًا.</p>
<div class="row">
  <div><label for="scr">الشاشة</label>
    <select id="scr">
      <option value="home.html">مشروعي الآن</option>
      <option value="work.html">العمل</option>
      <option value="finance.html">المالية</option>
      <option value="tools.html">أدواتي</option>
      <option value="market.html">السوق</option>
      <option value="products.html">منتجاتي وخدماتي</option>
      <option value="order.html">طلب متأخر</option>
      <option value="sale.html">تسجيل بيع</option>
    </select></div>
  <div><label for="st">الحالة</label>
    <select id="st">
      <option value="">(افتراضي — موجبة)</option>
      <option value="incomplete">غير مكتملة</option>
      <option value="negative">سالبة</option>
      <option value="empty">فارغة</option>
      <option value="form">نموذج بيع</option>
      <option value="validation">خطأ تحقق</option>
      <option value="success">نجاح الحفظ</option>
      <option value="system-error">خطأ نظام</option>
    </select></div>
  <div><label for="th">الوضع</label>
    <select id="th"><option value="light">نهاري</option><option value="dark">ليلي</option></select></div>
  <div><label for="w">العرض</label>
    <select id="w"><option>320</option><option selected>390</option><option>430</option></select></div>
</div>
<div class="frames">
  <div class="frame-card"><h2><span class="dot" style="background:#D96A45"></span>C1 — Warm Bold</h2><iframe id="f1" title="C1"></iframe></div>
  <div class="frame-card"><h2><span class="dot" style="background:#174E77"></span>C2 — Confident Bold</h2><iframe id="f2" title="C2"></iframe></div>
  <div class="frame-card"><h2><span class="dot" style="background:#6E3B85"></span>C3 — Dynamic Modular</h2><iframe id="f3" title="C3"></iframe></div>
</div>
</div>
<script>
(function(){
  function src(dir){
    var p = [];
    if (document.getElementById("st").value) p.push("state="+document.getElementById("st").value);
    if (document.getElementById("th").value === "dark") p.push("theme=dark");
    return dir + "/" + document.getElementById("scr").value + (p.length?"?"+p.join("&"):"");
  }
  function apply(){
    ["f1","f2","f3"].forEach(function(id,i){
      var f = document.getElementById(id);
      f.style.maxWidth = document.getElementById("w").value + "px";
      f.src = src(["c1-warm-bold","c2-confident-bold","c3-dynamic-modular"][i]);
    });
  }
  ["scr","st","th","w"].forEach(function(id){ document.getElementById(id).addEventListener("change", apply); });
  apply();
})();
</script>
</body>
</html>'''

README = """# Micro Bold Modular — النموذج التفاعلي (Agent-03 Multi-Agent)

نموذج تصميمي تفاعلي ثابت (Static HTML/CSS/JS) بدون خادم ولا بيانات حقيقية — عربي RTL بالكامل.

## التشغيل (خطوة واحدة)

افتح `index.html` في أي متصفح حديث مباشرة (نقر مزدوج — يعمل من `file://` دون أي تثبيت أو إنترنت؛ الخطوط والأيقونات مضمّنة محليًا).

أو من الطرفية:

```bash
cd agent-runs/agent-03-multi-agent/prototype
python3 -m http.server 8080   # اختياري — ثم افتح http://localhost:8080
```

## البنية

- `index.html` — مركز التحكم: الاتجاهات الثلاثة، المقارنة، الاتجاه الموصى به، وحزمة الفحص (QA Harness).
- `compare/` — مقارنة الاتجاهات جنبًا إلى جنب (نفس الشاشة/الحالة/الوضع).
- `c1-warm-bold/` / `c2-confident-bold/` / `c3-dynamic-modular/` — تسع شاشات لكل اتجاه + `screen.css` مستقل تمامًا + `screen.js`. **لا تُشارك أي أنماط بين الاتجاهات.**
- `selected-direction/` — الاتجاه الموصى به بعد التطوير + `design-system.html` (نظام التصميم المرشّح).
- `assets/fonts/` — IBM Plex Sans Arabic محليًا (woff2) — أرقام موحدة العرض (tabular) افتراضيًا.

## الشاشات في كل اتجاه

home (4 حالات: موجبة/غير مكتملة/سالبة/فارغة + قائمة الشعار) · work · finance · tools (فيها الوضع الليلي) · market · products · order (طلب متأخر) · sale (نموذج/تحقق/نجاح/خطأ نظام) · more.

## روابط عميقة (كل فحص قابل للتكرار)

```
screen.html?state=positive|incomplete|negative|empty|form|validation|success|system-error
          &theme=light|dark   &zoom=200   &motion=reduce   &sheet=menu
```

أمثلة:
- `c1-warm-bold/home.html?state=incomplete&theme=dark`
- `c3-dynamic-modular/sale.html?state=success`
- `c2-confident-bold/home.html?zoom=200&motion=reduce`

## حدود النموذج (تصنيف صادق)

- نطاق التصميم: مسار «سجّل بيعًا» كامل؛ نماذج مصروف/طلب/تحصيل وسجلات تفصيلية وAsk Micro والنقل والتوصيل خارج النطاق وتفتح ورقة تصنّف نفسها بصدق.
- «عرض العملية» و«كل السجل» تفتح ورقة توضيحية لا شاشة كاملة (خارج النطاق).
- قيم مساندة غير محددة في التجهيزات (حالة C المساندة، عملاء العرض) مركّبة من الـOrchestrator وموثّقة في rationale — لا تمس أي قيمة مقفلة.
- الطلب المتأخر: «حدّث حالة الطلب» يقدّم المرحلة في سكة الطلبات كعرض توضيحي للحالة، ويعود بالتحديث عند إعادة التحميل.

## محاكاة الأعراض والفحص

- **320/390/430px:** من حزمة الفحص في `index.html` أو صفحة المقارنة (iframe معزول).
- **الوضع الليلي:** من أدواتي ← الإعدادات (المسار الرسمي — IA-D04)، أو `?theme=dark` من حزمة الفحص.
- **تكبير 200%:** `?zoom=200` (كل النصوص بـrem).
- **الحركة المخفَّضة:** `?motion=reduce` أو تفعيل prefers-reduced-motion في النظام.
"""

def main():
    open(os.path.join(PROTO, "index.html"), "w", encoding="utf-8").write(INDEX)
    os.makedirs(os.path.join(PROTO, "compare"), exist_ok=True)
    open(os.path.join(PROTO, "compare", "index.html"), "w", encoding="utf-8").write(COMPARE)
    open(os.path.join(PROTO, "README.md"), "w", encoding="utf-8").write(README)
    print("index.html, compare/index.html, README.md written")

if __name__ == "__main__":
    main()
