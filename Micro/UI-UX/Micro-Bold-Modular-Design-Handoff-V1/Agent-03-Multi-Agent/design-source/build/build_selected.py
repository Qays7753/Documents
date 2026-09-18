#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Micro Bold Modular — Agent-03: SELECTED DIRECTION builder.
Provisional winner (C1 Warm Bold, rubric 84.2%) refined with documented
borrowings: finance discipline (C2), progress boldness + signal edge (C3).
Outputs: prototype/selected-direction/{9 screens, screen.css, screen.js,
design-system.html} + selected-direction/ rationale docs.
"""
import os, sys, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_screens as bs
from icons import icon
import fixtures as fx

ROOT = "/home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent"
PROTO = os.path.join(ROOT, "prototype")
OUT = os.path.join(PROTO, "selected-direction")
SEL_DIR = os.path.join(ROOT, "selected-direction")

bs.DIRS["selected-direction"] = {"name": "C1 Warm Bold — الموصى به (مبدئيًا)", "module_default": "home"}

REFINEMENTS = """
/* ============================================================
   SELECTED DIRECTION — C1 Warm Bold + documented borrowings
   (rubric-evaluation.md §خامسًا). C1 identity preserved.
   ============================================================ */
/* Borrowing 1 — from C2: finance numeric discipline */
.fin-hero { border: 1px solid var(--divider); border-inline-start: 4px solid var(--trust); border-radius: 14px; }
[data-module="finance"] .metric-list { border-radius: 14px; }
/* Borrowing 2 — from C3: progress language boldness */
.meter__seg { height: 12px; width: 20px; border-radius: 6px; }
.ostep__dot { width: 16px; height: 16px; }
.ostep::before { top: 10px; height: 3.5px; }
/* Borrowing 3 — from C3: signal edge stripe (scanability) */
.signal { position: relative; border-inline-start: 4px solid var(--att); }
.signal__icon { border-radius: 14px; }
/* Negative hero: C1's own round-3 treatment (corrected attribution — D-402) */
"""

def build_screens():
    os.makedirs(OUT, exist_ok=True)
    css = open(os.path.join(HERE, "..", "design", "c1.css"), encoding="utf-8").read()
    css = css.replace("__FONTS__", "../assets/fonts") + REFINEMENTS
    open(os.path.join(OUT, "screen.css"), "w", encoding="utf-8").write(css)
    shutil.copy(os.path.join(HERE, "..", "design", "screen.js"), os.path.join(OUT, "screen.js"))
    builders = {"home.html": bs.build_home, "work.html": bs.build_work, "finance.html": bs.build_finance,
                "tools.html": bs.build_tools, "market.html": bs.build_market, "products.html": bs.build_products,
                "order.html": bs.build_order, "sale.html": bs.build_sale, "more.html": bs.build_more}
    for fname, fn in builders.items():
        open(os.path.join(OUT, fname), "w", encoding="utf-8").write(fn("selected-direction"))
        print(f"wrote selected-direction/{fname}")

DESIGN_SYSTEM = """<!DOCTYPE html>
<html lang="ar" dir="rtl" data-theme="light" data-direction="selected-direction" data-module="home">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>نظام التصميم المرشّح — Micro · Agent-03</title>
<link rel="stylesheet" href="screen.css">
<style>
* { box-sizing:border-box; margin:0; padding:0; }
body { background:#EFEDE8; padding:26px 16px 70px; }
.ds { max-width:900px; margin-inline:auto; display:flex; flex-direction:column; gap:20px; }
.ds-head { display:flex; align-items:center; gap:14px; flex-wrap:wrap; }
.ds-head h1 { font-size:24px; }
.tgl { min-height:44px; padding:8px 18px; border-radius:14px; border:2px solid var(--ink); background:var(--surface); font-family:inherit; font-weight:700; cursor:pointer; color:var(--ink); }
.ds section.b { background:var(--surface); border:1px solid var(--divider); border-radius:20px; padding:20px 22px; display:flex; flex-direction:column; gap:14px; }
.ds h2 { font-size:16px; font-weight:700; color:var(--brand-deep); border-inline-start:5px solid var(--brand); padding-inline-start:10px; }
.ds p, .ds li { font-size:14px; line-height:1.8; }
.tokgrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(160px,1fr)); gap:10px; }
.tok { border:1px solid var(--divider); border-radius:14px; padding:10px; font-size:12px; }
.tok .chip { height:42px; border-radius:10px; margin-bottom:6px; border:1px solid rgba(0,0,0,.12); }
.tok b { font-size:12px; }
.g2 { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:14px; }
code { background:var(--group); padding:1px 6px; border-radius:6px; font-size:12.5px; }
table { width:100%; border-collapse:collapse; font-size:13px; }
th, td { padding:7px 9px; border-bottom:1px solid var(--divider); text-align:start; }
th { color:var(--ink2); font-size:12px; }
</style>
</head>
<body>
<div class="ds">
<header class="ds-head">
  <h1>نظام التصميم المرشّح — Micro Bold Modular</h1>
  <button class="tgl" onclick="var h=document.documentElement;h.setAttribute('data-theme',h.getAttribute('data-theme')==='dark'?'light':'dark')">نهاري / ليلي</button>
  <span style="font-size:13px;color:var(--ink2)">C1 Warm Bold + استعارات موثقة · Agent-03 · توصية معلّقة على الاعتماد والاختبار</span>
</header>

<section class="b">
<h2>الأطروحة</h2>
<p><b>Warm Bold Micro:</b> تيراكوتا حي يقود الهوية والفعل، كتل معيارية دافئة مستديرة تحفظ الجدية المالية، أزرق ثقة منضبط للملاحة والسياق، عائلة نتيجة رباعية الحالات «الناقص فيها مواطن أول».</p>
<p>الاستعارات الموثقة: انضباط المالية (من C2)، بروز لغة التقدم + شريط حافة الإشارة (من C3)، معالجة سالبة جادة (محسّنة في الجولة 3).</p>
</section>

<section class="b">
<h2>Tokens — اللون (Semantic Core)</h2>
<div class="tokgrid">
<div class="tok"><div class="chip" style="background:var(--brand)"></div><b>brand.fill</b><br>هوية + إنشاء<br><code>#D96A45</code></div>
<div class="tok"><div class="chip" style="background:var(--brand-deep)"></div><b>brand.deep</b><br>نص هوية + تركيز<br><code>#A03A1D</code></div>
<div class="tok"><div class="chip" style="background:var(--on-brand); border:1px solid var(--brand)"></div><b>onBrand</b><br>نص فوق الدافئ<br><code>#2B130A</code></div>
<div class="tok"><div class="chip" style="background:var(--trust)"></div><b>trust</b><br>ملاحة + معلومات<br><code>#1F5E8C</code></div>
<div class="tok"><div class="chip" style="background:var(--pos)"></div><b>positive</b><br>نتيجة موجبة فقط<br><code>#1E6E42</code></div>
<div class="tok"><div class="chip" style="background:var(--neg)"></div><b>negative</b><br>نتيجة سالبة/خطر<br><code>#B32318</code></div>
<div class="tok"><div class="chip" style="background:var(--att)"></div><b>attention</b><br>نقص + انتباه<br><code>#8A5300</code></div>
<div class="tok"><div class="chip" style="background:var(--pos-tint); border:1px solid var(--pos)"></div><b>pos.tint</b><br>أرضية الحالة<br><code>#E6F2EA</code></div>
<div class="tok"><div class="chip" style="background:var(--neg-tint); border:1px solid var(--neg)"></div><b>neg.tint</b><br><code>#FBEAE7</code></div>
<div class="tok"><div class="chip" style="background:var(--att-tint); border:1px solid var(--att)"></div><b>att.tint</b><br><code>#FAEEDA</code></div>
<div class="tok"><div class="chip" style="background:var(--canvas); border:1px solid var(--divider)"></div><b>canvas</b><br><code>#FAF6F1</code></div>
<div class="tok"><div class="chip" style="background:var(--surface); border:1px solid var(--divider)"></div><b>surface</b><br><code>#FFFFFF</code></div>
<div class="tok"><div class="chip" style="background:var(--group); border:1px solid var(--divider)"></div><b>group</b><br><code>#F4ECE3</code></div>
<div class="tok"><div class="chip" style="background:var(--ink)"></div><b>ink</b><br><code>#231A14</code></div>
</div>
<p style="font-size:12.5px;color:var(--ink2)">الوضع الليلي معادل كامل في screen.css (تخفيض تشبع + إعادة قياس كل الأزواج — tokens/contrast-evidence.json). القواعد: الأخضر للنتيجة الموجبة المكتملة فقط · الأزرق ليس مالًا موجبًا · الحبر الداكن فوق كل تعبئة دافئة · لا Fill للإشارة.</p>
</section>

<section class="b">
<h2>Tokens — الطباعة والمسافة والشكل والحركة</h2>
<table>
<tr><th>Token</th><th>القيمة</th><th>الاستخدام</th></tr>
<tr><td><code>type.hero</code></td><td>44px / 700 (2.75rem)</td><td>رقم النتيجة في الهيرو — tabular</td></tr>
<tr><td><code>type.title</code></td><td>18px / 700</td><td>عنوان شاشة/اسم مشروع</td></tr>
<tr><td><code>type.section</code></td><td>15px / 700 + أيقونة</td><td>عنوان وحدة</td></tr>
<tr><td><code>type.body</code></td><td>15.5px / 400</td><td>متن</td></tr>
<tr><td><code>type.secondary</code></td><td>13px / 400</td><td>ثانوي — الحد الأدنى للنص التفسيري الحرج</td></tr>
<tr><td><code>type.label</code></td><td>12px / 500-700 + أيقونة</td><td>ملصقات الملاحة والمراحل (ليست نصًا تفسيريًا)</td></tr>
<tr><td><code>space.unit</code></td><td>4px (سلم 4)</td><td>كل الفراغات</td></tr>
<tr><td><code>radius.card / control / chip</code></td><td>20px / 14px / pill</td><td>بطاقات / تحكمات / رقاقات</td></tr>
<tr><td><code>control.min</code></td><td>44–48px</td><td>عقد اللمس للتحكمات الأساسية</td></tr>
<tr><td><code>motion.save</code></td><td>1.6s ease-out مرة واحدة</td><td>إبراز Success Impact — يسقط عند reduced-motion</td></tr>
<tr><td><code>motion.sheet</code></td><td>0.28s cubic-bezier(.2,.8,.25,1)</td><td>الأوراق — يسقط عند reduced-motion</td></tr>
</table>
<p style="font-size:12.5px;color:var(--ink2)">IBM Plex Sans Arabic محلي (4 أوزان، ~300KB) — أرقام لاتينية موحدة العرض افتراضيًا (tabular مقيسة في الخط) معزولة <code>&lt;bdi dir="ltr"&gt;</code>. الخط كله rem — تكبير 200% يضخم فعليًا.</p>
</section>

<section class="b">
<h2>قواعد المكوّنات (فوق النواة)</h2>
<div class="g2">
<div>
<p class="lbl" style="font-size:12px;color:var(--ink2);margin-bottom:6px">Business Status Hero — 4 حالات</p>
<section class="hero" style="margin-bottom:10px">
  <div class="hero__head"><span class="hero__label">وضع مشروعك اليوم</span><span class="state-chip state-chip--pos">__UP__نتيجة موجبة</span></div>
  <p class="hero__result num"><bdi dir="ltr">+42.50</bdi> <span style="font-size:1.25rem">د.أ</span></p>
  <p class="hero__explain">بعد تسجيل المبيعات والمصاريف والتكاليف</p>
</section>
<section class="hero hero--neg">
  <div class="hero__head"><span class="hero__label">نتيجة مشروعك اليوم</span><span class="state-chip state-chip--neg">__DOWN__نتيجة سالبة</span></div>
  <p class="hero__result num"><bdi dir="ltr">−18.75</bdi> <span style="font-size:1.25rem">د.أ</span></p>
</section>
<p style="font-size:12px;color:var(--ink2)">قاعدة: موجبة/سالبة برقم · غير مكتملة بلا رقم (سبب + عدّاد + إجراء) · فارغة بتشجيع. السالب: سطح فاتح + إطار أحمر (جدية بلا اتهام).</p>
</div>
<div>
<p class="lbl" style="font-size:12px;color:var(--ink2);margin-bottom:6px">Micro Signal + Quick Action Bar</p>
<section class="signal">
  <span class="signal__icon">__ALERT__</span>
  <div class="signal__body">
    <p class="signal__status">عندك مبلغ يحتاج تحصيلًا</p>
    <p class="signal__reason">أم محمد عليها <bdi dir="ltr">25.00</bdi> د.أ منذ 3 أيام</p>
    <div class="signal__action"><button class="btn btn--secondary btn--sm">حصّل المبلغ</button></div>
  </div>
</section>
<section class="qab" style="margin-top:10px">
  <button class="qab__btn qab__btn--primary"><span class="qab__icon">__SELL__</span><span class="qab__label">بيع</span></button>
  <button class="qab__btn"><span class="qab__icon">__EXP__</span><span class="qab__label">مصروف</span></button>
  <button class="qab__btn"><span class="qab__icon">__ORDER__</span><span class="qab__label">طلب</span></button>
  <button class="qab__btn"><span class="qab__icon">__COLLECT__</span><span class="qab__label">تحصيل</span></button>
  <button class="qab__btn qab__btn--more"><span class="qab__icon">__MORE__</span><span class="qab__label">المزيد</span></button>
</section>
<p style="font-size:12px;color:var(--ink2)">الإشارة: تينت + حافة 4px (استعارة C3) — لا Fill. QAB: قوة وزنية (حبر)، بيع بتعبئة، 5 عناصر بأيقونة+نص، لا FAB مزدوج.</p>
</div>
</div>
</section>

<section class="b">
<h2>عائلة الحالة (نص + إشارة ثانية دائمًا)</h2>
<div style="display:flex;gap:10px;flex-wrap:wrap">
<span class="state-chip state-chip--pos">__UP__نتيجة موجبة</span>
<span class="state-chip state-chip--neg">__DOWN__نتيجة سالبة</span>
<span class="state-chip state-chip--att">__ALERT__النتيجة غير مكتملة</span>
<span class="late-chip">__CLOCK__متأخر يومًا واحدًا</span>
<span class="stage-chip stage-chip--delivered">__CHECK__تم التسليم</span>
<span class="tag">__ALERT__ناقصة التكلفة</span>
</div>
<p style="font-size:12.5px;color:var(--ink2)">IX-D05: اللون ليس الوسيلة الوحيدة — أيقونة/شكل/وزن مع كل حالة. جداول التباين المقيسة في <code>tokens/selected-contrast.md</code>.</p>
</section>

<section class="b">
<h2>Success Impact (التوقيع الحركي المرشّح)</h2>
<div class="g2">
<div class="impact-preview"><p class="impact-preview__title">__RESULT__شو رح يصير؟</p>
<p class="impact-preview__body">رح تزيد المبيعات <bdi class="preview-amount" dir="ltr">25.00</bdi> د.أ، وينضاف المبلغ إلى درج المحل.</p></div>
<div class="success-card">
  <span class="success-card__badge">__CHECK2__</span>
  <p class="success-card__status">تم تسجيل البيع</p>
  <p class="success-card__amount num"><bdi dir="ltr">25.00</bdi> <span style="font-size:1rem">د.أ</span></p>
  <p class="success-card__dest">أُضيف المبلغ إلى درج المحل</p>
  <div class="success-impact"><span class="success-impact__label">الكاش المسجل الآن</span>
  <span class="success-impact__value num"><bdi dir="ltr">161.00</bdi> <span style="font-size:0.875rem">د.أ</span></span></div>
  <p class="success-ref">عملية <bdi dir="ltr">#142</bdi> · تراجع</p>
</div>
</div>
<p style="font-size:12.5px;color:var(--ink2)">التسلسل: رد فعل ← حفظ يمنع التكرار ← تأكيد (مبلغ+وجهة) ← إبراز القيمة المحدثة ← مرجع بشري. النجاح = ثقة نظامية (حبر + تينت Trust) — الأخضر حصري للنتيجة. الحركة تسقط تحت prefers-reduced-motion ويبقى الإبراز الثابت.</p>
</section>

<section class="b">
<h2>قواعد الطاقة والأسطح</h2>
<ul style="padding-inline-start:18px">
<li><b>ميزانية الطاقة:</b> تعبئة مشبعة=3 · تينت=2 · لمسة=1. الرئيسية/العمل 5–6 · المالية 3–4 · أدواتي 2–3 · السجلات 1–2. حقل مهيمن واحد في initial viewport.</li>
<li><b>الأسطح (4):</b> Canvas → Group (تون) → Reading (حواف) → Overlay (الظل الوحيد). مقسّمات للصفوف المتجانسة. لا بطاقة داخل بطاقة.</li>
<li><b>Fill كامل فقط:</b> الهيرو، زر الفعل الأساسي، حقل المبلغ. الإشارة تينت+حافة حصرًا.</li>
<li><b>الأيقونات:</b> عائلة واحدة (Lucide-style stroke 2) · مرآة للاتجاهية فقط · نشط = وزن+حاوية.</li>
<li><b>اللمس:</b> 44–48px للأساسي (QAB/ملاحة/حفظ/إشارة) · ≥24px (WCAG 2.5.8) للثانوي الموثق.</li>
</ul>
</section>
</div>
</body>
</html>"""

def build_ds_page():
    html = (DESIGN_SYSTEM
            .replace("__UP__", icon("سهم-أعلى", "icon--sm"))
            .replace("__DOWN__", icon("سهم-أسفل", "icon--sm"))
            .replace("__ALERT__", icon("تنبيه", "icon--sm"))
            .replace("__CLOCK__", icon("ساعة", "icon--sm"))
            .replace("__CHECK__", icon("صح", "icon--sm"))
            .replace("__CHECK2__", icon("صح"))
            .replace("__SELL__", icon("بيع"))
            .replace("__EXP__", icon("مصروف"))
            .replace("__ORDER__", icon("طلب"))
            .replace("__COLLECT__", icon("تحصيل"))
            .replace("__MORE__", icon("المزيد"))
            .replace("__RESULT__", icon("النتيجة", "icon--sm")))
    open(os.path.join(OUT, "design-system.html"), "w", encoding="utf-8").write(html)
    print("wrote selected-direction/design-system.html")

RATIONALE = """# الاتجاه الموصى به (مبدئيًا) — C1 Warm Bold + استعارات موثقة
**الصفة:** توصية مهنية من الـOrchestrator — **معلّقة على اعتماد المالك واختبار المستخدم الحقيقي** (لا ادعاء اعتماد).

## لماذا فاز (الملخص التنفيذي للروبريك)
- المرتبة الأولى بالتقييم الموزون: **84.2%** مقابل 82.8% (C3) و80.3% (C2) — بلا فشل في أي بوابة رفض إلزامية (تقرير reports/rubric-evaluation.md).
- أقوى توافق مع المستخدم الأساسي المقفل (UX-D01: خبرة مالية/رقمية محدودة): أعلى درجات محدودي الخبرة (4.5) والراحة المطولة (4.5) — المحور النفسي الذي يخفض الخوف من الأرقام (فرضية H3 موثقة للاختبار).
- عنقود الفهم/الاكتشاف/السيطرة (44% وزنًا) أعلى مجموعًا: الوضوح الدافئ لا يفرض فك شفرة نظام بصري قبل الإجابة.

## الاستعارات المنفذة (موثقة — ليست خليطًا)
1. من C2: انضباط المالية (fin-hero بحافة trust 4px، أسطح أهدأ في المالية).
2. من C3: بروز لغة التقدم (مقاطع العدّاد 12px، نقاط السكة أمتن).
3. من C3: شريط حافة 4px للإشارة (مسح أسرع) مع بقاء التينت.
4. معالجة السالب الجادة (سطح فاتح + إطار أحمر + رقم أحمر) — محسّنة في الجولة 3.

## ما بقي من C2 وC3 محفوظًا كاملاً
- الشاشات الكاملة للاتجاهين (بجودة متساوية) في prototype/c2-confident-bold/ وprototype/c3-dynamic-modular/ مع أدلتهما — قرار المالك قد يخالف توصيتي، والخياران جاهزان.

## المخاطر المتبقية (موثقة للاختبار)
- تقارب الأمبر/التيراكوتا: مخفف بالشكل+النص، يبقى فرضية تمييز.
- جوار جمالي «توصيل طعام»: مخفف بالانضباط والسالب الجاد.
- «التيراكوتا يشعر أردنيًا»: فرضية صريحة (الملف 10) — لا تُقدَّم كحقيقة.

## مصادر التنفيذ
- prototype/selected-direction/ — 9 شاشات + screen.css (C1 + طبقة الاستعارات) + design-system.html.
- tokens/contrast-evidence.json — كل أزواج الاتجاه المختار مقيسة Light+Dark (PASS).
"""

def main():
    build_screens()
    build_ds_page()
    os.makedirs(SEL_DIR, exist_ok=True)
    open(os.path.join(SEL_DIR, "rationale.md"), "w", encoding="utf-8").write(RATIONALE)
    # selected-direction contrast evidence copy
    import shutil
    src = os.path.join(ROOT, "tokens", "c1-warm-bold-contrast.md")
    shutil.copy(src, os.path.join(ROOT, "tokens", "selected-contrast.md"))
    print("selected-direction rationale + contrast copy written")

if __name__ == "__main__":
    main()
