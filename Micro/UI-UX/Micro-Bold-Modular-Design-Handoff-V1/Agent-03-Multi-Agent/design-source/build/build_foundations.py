#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Micro Bold Modular — Agent-03 Foundation Boards (Phase A).
Self-contained HTML board per direction: thesis, adjectives, palette+contrast
(from measured evidence), typography specimens, surfaces, color-block logic,
icons, controls, status family, hero/signal/QAB specimens, success storyboard,
light/dark. Also writes per-direction rationale.md.
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fixtures as fx
from icons import icon, LOGO

ROOT = "/home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent"
TOKENS = os.path.join(ROOT, "tokens")
EVID = json.load(open(os.path.join(TOKENS, "contrast-evidence.json"), encoding="utf-8"))

DIRS = {
 "c1-warm-bold": {
   "title": "C1 — Warm Bold", "thesis": "أقرب اتجاه للمشاريع المنزلية والحرفية دون ريفية أو حنين: تيراكوتا حي يقود الهوية، كتلاً معيارية مستديرة تحفظ الجدية المالية.",
   "adjectives": "دافئ · جريء · قريب · جدي · حي",
   "mood": "مطبخ منظم صباحًا لا دفتر حسابات قديم؛ طاقة قرار لا طاقة سوق شعبي.",
   "dark_rationale": "ليل دافئ: قاعدة بنية-فحمية عميقة، تيراكوتا أفتح للنظر بلا وهج، حليب فاتح للنص، والأدوار الدلالية معاد قياسها كاملة." },
 "c2-confident-bold": {
   "title": "C2 — Confident Bold", "thesis": "اتجاه تحكم مالي حديث بطاقة ظاهرة وثقة بصرية: أزرق معماري عميق يحمل الثقة والسياق النشط، وتيراكوتا يحمل طاقة الإنشاء والفعل.",
   "adjectives": "واثق · منضبط · معماري · دافئ الجوهر · حاسم",
   "mood": "نظام تشغيل مالي جاد — ليس بنكًا ولا SaaS عامًا: كتل مسطحة وشعرية رقمية صارمة.",
   "dark_rationale": "ليل كحلي: أزرق مشبع مخفوف اللمعان، أسطح أغمق من الليل الحرفي، وتيراكوتا مضيء للفعل." },
 "c3-dynamic-modular": {
   "title": "C3 — Dynamic Modular", "thesis": "أعلى مستوى تعبير مقبول: مناطق لونية قوية تحدد المهمة والحالة، شريط وحدة واحد لكل قسم، ولغة حالة وحركة أوضح — بلا قوس قزح ملاحي.",
   "adjectives": "نشط · معياري · واضح الحالة · جسور · متّصل",
   "mood": "واجهة تتحرك قبل أن يلمسها المستخدم — لكن المال يبقى هادئًا.",
   "dark_rationale": "ليل محايد دافئ مع لوحات وحدات فاتحة معاد تشبعها، وأشرطة الوحدة تبقى مميزة." },
}

def contrast_table(direction, mode):
    rows = EVID["results"][direction][mode]
    out = ["<table class='ct'><tr><th>الزوج</th><th>أمامية</th><th>خلفية</th><th>النسبة</th><th>المطلوب</th><th>النتيجة</th></tr>"]
    for e in rows:
        if e["req"] == 99: continue
        req = f'{e["req"]}:1'
        out.append(f"<tr><td>{e['pair']}</td><td><span class='sw' style='background:{e['fg']}'></span>{e['fg']}</td>"
                   f"<td><span class='sw' style='background:{e['bg']};border:1px solid #999'></span>{e['bg']}</td>"
                   f"<td><b>{e['ratio']}:1</b></td><td>{req}</td><td class='{'pass' if e['pass'] else 'fail'}'>{'PASS' if e['pass'] else 'FAIL'}</td></tr>")
    out.append("</table>")
    return "\n".join(out)

BOARD_CSS = """
* { box-sizing:border-box; margin:0; padding:0; }
body { background:#EFEDE8; padding:28px 16px 70px; }
.board { max-width:960px; margin-inline:auto; display:flex; flex-direction:column; gap:22px; }
.board-head { display:flex; align-items:center; gap:14px; flex-wrap:wrap; }
.board-head h1 { font-size:26px; }
.theme-toggle { min-height:44px; padding:8px 18px; border-radius:12px; border:2px solid var(--ink); background:var(--surface); font-family:inherit; font-weight:700; cursor:pointer; color:var(--ink); }
.board section.blk { background:var(--surface); border:1px solid var(--divider); border-radius:var(--r-card); padding:20px 22px; display:flex; flex-direction:column; gap:14px; }
.board h2.bt { font-size:16px; font-weight:700; color:var(--brand-deep); border-inline-start:5px solid var(--brand); padding-inline-start:10px; }
.board p, .board li { font-size:14.5px; line-height:1.8; }
.thesis { font-size:17px; font-weight:700; }
.meta { color:var(--ink2); }
.swatches { display:grid; grid-template-columns:repeat(auto-fill,minmax(150px,1fr)); gap:10px; }
.swatch { border-radius:14px; padding:10px 12px; font-size:12px; border:1px solid var(--divider); }
.swatch .chip { height:44px; border-radius:10px; margin-bottom:6px; border:1px solid rgba(0,0,0,.12); }
.swatch b { font-size:12.5px; }
.ct { width:100%; border-collapse:collapse; font-size:12.5px; }
.ct th, .ct td { padding:6px 8px; text-align:start; border-bottom:1px solid var(--divider); }
.ct th { color:var(--ink2); font-size:12px; }
.ct .sw { display:inline-block; width:13px; height:13px; border-radius:4px; margin-inline-end:6px; vertical-align:-2px; }
.ct .pass { color:var(--pos); font-weight:700; } .ct .fail { color:var(--neg); font-weight:700; }
.spec-row { display:flex; flex-direction:column; gap:6px; border-bottom:1px dashed var(--divider); padding-block:10px; }
.spec-row .lbl { font-size:12px; color:var(--ink2); font-weight:600; }
.grid2 { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:14px; }
.iconrow { display:flex; gap:14px; flex-wrap:wrap; }
.iconrow .ic { display:flex; flex-direction:column; align-items:center; gap:5px; font-size:11.5px; color:var(--ink2); min-width:64px; }
.iconrow .ic .bx { width:52px; height:52px; border-radius:14px; background:var(--group); display:grid; place-items:center; color:var(--ink); }
"""

def board(direction):
    cfg = DIRS[direction]
    css = open(os.path.join(HERE, "..", "design", f"{direction.split('-')[0]}.css"), encoding="utf-8").read()
    css = css.replace("__FONTS__", "../../prototype/assets/fonts")
    pal = EVID["palettes"][direction]
    swatch_defs = [
        ("brand.fill", "Brand Warm — هوية وطاقة الإنشاء"), ("brand.deep", "Brand Deep — نص الهوية والأزرار الثانوية"),
        ("trust", "Trust Blue — معلومات وسياق نشط"), ("pos", "Positive Green — نتيجة موجبة مكتملة فقط"),
        ("neg", "Negative Red — نتيجة سالبة/خطر"), ("att", "Attention Amber — نقص وانتباه"),
        ("canvas", "Canvas — بيئة الصفحة"), ("surface", "Surface — سطح القراءة"),
        ("group", "Group — تون تجميع"), ("ink", "Ink — نص وأرقام"),
    ]
    swatches = "".join(
        f'''<div class="swatch"><div class="chip" style="background:{pal['light'][k]}"></div>
        <b>{n}</b><br><span class="meta">{pal['light'][k]} · {pal['dark'][k]}</span></div>''' for k, n in swatch_defs)
    icons12 = ["بيع", "مصروف", "طلب", "تحصيل", "الكاش", "الدين", "النتيجة", "التكلفة", "محفظة", "مورد", "موعد", "تسليم"]
    icon_row = "".join(f'<div class="ic"><span class="bx">{icon(i)}</span>{i}</div>' for i in icons12)
    type_specimens = [
        ("hero__result", "رقم الهيرو — 44px/700", f'<p class="hero__result num" style="color:var(--ink)"><bdi dir="ltr">+42.50</bdi> <span style="font-size:20px">{fx.CURRENCY}</span></p>'),
        ("", "عنوان شاشة — 18px/700", '<p style="font-size:18px;font-weight:700">حلويات ليان — مشروعي الآن</p>'),
        ("", "عنوان وحدة — 15px/700", '<p style="font-size:15px;font-weight:700">الاستحقاقات — لي عند العملاء</p>'),
        ("", "متن — 15.5px/400", '<p style="font-size:15.5px">بعد تسجيل المبيعات والمصاريف والتكاليف، تظهر نتيجة مشروعك بشكل كامل وواضح.</p>'),
        ("", "ثانوي — 13px/400", '<p style="font-size:13px;color:var(--ink2)">أم محمد عليها 25.00 د.أ منذ 3 أيام — بانتظار التحصيل</p>'),
    ]
    type_html = "".join(f'<div class="spec-row"><span class="lbl">{lbl}</span>{html}</div>' for _, lbl, html in type_specimens)
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl" data-theme="light" data-direction="{direction}">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Foundation Board — {cfg["title"]} · Micro Bold Modular (Agent-03)</title>
<style>
{css}
{BOARD_CSS}
</style>
</head>
<body>
<div class="board">
<header class="board-head">
  <h1>Foundation Board — {cfg["title"]}</h1>
  <button class="theme-toggle" onclick="var h=document.documentElement;h.setAttribute('data-theme',h.getAttribute('data-theme')==='dark'?'light':'dark')">تبديل نهاري/ليلي</button>
  <span class="meta">Micro Bold Modular · Agent-03 · المرحلة A</span>
</header>

<section class="blk">
  <h2 class="bt">الأطروحة والصفات</h2>
  <p class="thesis">{cfg["thesis"]}</p>
  <p><b>الصفات الخمس:</b> {cfg["adjectives"]}</p>
  <p class="meta"><b>مرجع المزاج (مبدأ لا لقطة):</b> {cfg["mood"]}</p>
</section>

<section class="blk">
  <h2 class="bt">أدوار اللوحة (نهاري · ليلي)</h2>
  <div class="swatches">{swatches}</div>
  <p class="meta">قاعدة الحبر الداكن فوق التعبئات الدافئة إلزامية (قياس مقيس)؛ الأخضر للنتيجة الموجبة المكتملة فقط؛ الأزرق ليس مالًا موجبًا.</p>
</section>

<section class="blk">
  <h2 class="bt">جداول التباين المقيسة — نهاري</h2>
  {contrast_table(direction, "light")}
  <h2 class="bt" style="margin-top:10px">ليلي</h2>
  {contrast_table(direction, "dark")}
  <p class="meta">قياس WCAG 2.x (1.4.3/1.4.11) لكل زوج تشغيلي في الوضعين. لا تقريب نسبة فاشلة إلى ناجحة.</p>
</section>

<section class="blk">
  <h2 class="bt">سلم الطباعة — أمثلة عربية فعلية</h2>
  {type_html}
  <p class="meta">IBM Plex Sans Arabic (محلي woff2) — أرقام لاتينية موحدة العرض افتراضيًا، معزولة bidi. لا تباعد أحرف عربي. الحد الأدنى للنص الحرج 13px.</p>
</section>

<section class="blk">
  <h2 class="bt">الأسطح والعمق (4 مستويات)</h2>
  <div class="grid2">
    <div style="background:var(--canvas);border:1px dashed var(--field-border);border-radius:14px;padding:14px"><b>1 · Canvas</b><p class="meta">بيئة الصفحة — لا يحمل نصًا حرجًا مباشرًا.</p></div>
    <div style="background:var(--group);border-radius:14px;padding:14px"><b>2 · Group</b><p class="meta">تجميع توني مفتوح — مقسّمات للصفوف المتجانسة.</p></div>
    <div style="background:var(--surface);border:1px solid var(--divider);border-radius:14px;padding:14px"><b>3 · Reading</b><p class="meta">قراءة ونماذج — حواف بلا ظل.</p></div>
    <div style="background:var(--surface);border:1px solid var(--divider);border-radius:14px;padding:14px;box-shadow:0 14px 34px rgba(0,0,0,.18)"><b>4 · Overlay</b><p class="meta">الأوراق والحوار — المستوى الوحيد المسموح له ظل.</p></div>
  </div>
</section>

<section class="blk">
  <h2 class="bt">منطق الكتلة اللونية (Color Blocking)</h2>
  <p><b>Fill كامل:</b> الهيرو وزر الفعل الأساسي وحقل المبلغ فقط. <b>Tint:</b> الإشارة والمقاييس وشرائح الحالة. <b>Border:</b> أسطح القراءة والسجلات. <b>الإشارة لا تستخدم Fill أبدًا.</b></p>
  <p class="meta">ميزانية الطاقة: تعبئة مشبعة = 3 نقاط، تينت = 2، لمسة = 1؛ الرئيسية 5-6، المالية 3-4، السجلات 1-2. حقل مهيمن واحد في initial viewport — قوة QAB وزنية (حبر) لا كرومية.</p>
</section>

<section class="blk">
  <h2 class="bt">عائلة الأيقونات (12 مفهومًا مطلوبًا)</h2>
  <div class="iconrow">{icon_row}</div>
  <p class="meta">عائلة واحدة (Lucide-style stroke) — مرآة للاتجاهية فقط، وزن أثقل + حاوية للتبويب النشط والفعل الأساسي.</p>
</section>

<section class="blk">
  <h2 class="bt">التسلسل الهرمي للأزرار والتحكم</h2>
  <div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center">
    <button class="btn btn--primary">{icon("بيع","icon--sm")}سجّل بيعًا</button>
    <button class="btn btn--secondary">حصّل المبلغ</button>
    <button class="btn btn--ghost">راجع الطلبات</button>
    <button class="btn btn--text">تراجع</button>
  </div>
  <p class="meta">عقد اللمس 44–48px · مؤشر تركيز 3px بتباين ≥3:1 مقيس · حالة الضغط فورية.</p>
</section>

<section class="blk">
  <h2 class="bt">عائلة الحالات الحرجة (نص + إشارة ثانية دائمًا)</h2>
  <div style="display:flex;gap:10px;flex-wrap:wrap">
    <span class="state-chip state-chip--pos">{icon("سهم-أعلى","icon--sm")}نتيجة موجبة</span>
    <span class="state-chip state-chip--neg">{icon("سهم-أسفل","icon--sm")}نتيجة سالبة</span>
    <span class="state-chip state-chip--att">{icon("تنبيه","icon--sm")}النتيجة غير مكتملة</span>
    <span class="late-chip">{icon("ساعة","icon--sm")}متأخر يومًا واحدًا</span>
    <span class="stage-chip stage-chip--delivered">{icon("صح","icon--sm")}تم التسليم</span>
    <span class="tag">{icon("تنبيه","icon--sm")}خطأ تحقق</span>
  </div>
  <p class="meta">اللون ليس أبدًا الوسيلة الوحيدة (IX-D05) — أيقونة + نص + وزن/حد لكل حالة.</p>
</section>

<section class="blk">
  <h2 class="bt">نماذج المكوّنات المميزة</h2>
  <div class="grid2">
    <div>
      <p class="meta" style="margin-bottom:6px">Business Status Hero (موجبة — التجهيز A)</p>
      <section class="hero">
        <div class="hero__head"><span class="hero__label">وضع مشروعك اليوم</span>
        <span class="state-chip state-chip--pos">{icon("سهم-أعلى","icon--sm")}نتيجة موجبة</span></div>
        <p class="hero__result num"><bdi dir="ltr">+42.50</bdi> <span style="font-size:20px">{fx.CURRENCY}</span></p>
        <p class="hero__explain">بعد تسجيل المبيعات والمصاريف والتكاليف</p>
      </section>
    </div>
    <div>
      <p class="meta" style="margin-bottom:6px">Business Status Hero (غير مكتملة — التجهيز B، بلا رقم)</p>
      <section class="hero">
        <div class="hero__head"><span class="hero__label">نتيجة مشروعك</span>
        <span class="state-chip state-chip--att">{icon("تنبيه","icon--sm")}النتيجة غير مكتملة</span></div>
        <p class="hero__reason">عمليتا بيع تحتاجان تسجيل التكلفة</p>
        <div class="hero__meter">{''.join(f'<span class="meter__seg{" meter__seg--on" if i<8 else ""}"></span>' for i in range(10))}<span class="meter__count num">8 من 10</span></div>
        <div class="hero__supporting"><span class="s-label">مبيعات اليوم:</span><span class="s-value num"><bdi dir="ltr">120.00</bdi> <span class="cur">د.أ</span></span></div>
      </section>
    </div>
    <div>
      <p class="meta" style="margin-bottom:6px">Micro Signal (تينت فقط — حالة ← سبب ← فعل)</p>
      <section class="signal">
        <span class="signal__icon">{icon("تنبيه")}</span>
        <div class="signal__body">
          <p class="signal__status">عندك مبلغ يحتاج تحصيلًا</p>
          <p class="signal__reason">أم محمد عليها <bdi dir="ltr">25.00</bdi> {fx.CURRENCY} منذ 3 أيام</p>
          <div class="signal__action"><button class="btn btn--secondary btn--sm">حصّل المبلغ</button></div>
        </div>
      </section>
    </div>
    <div>
      <p class="meta" style="margin-bottom:6px">Quick Action Bar (وزن حبري، بيع أساسي)</p>
      {fx_qab()}
    </div>
  </div>
</section>

<section class="blk">
  <h2 class="bt">Success Impact — القصة المتسلسلة</h2>
  <div class="grid2">
    <div class="impact-preview"><p class="impact-preview__title">{icon("النتيجة","icon--sm")}شو رح يصير؟</p>
    <p class="impact-preview__body">رح تزيد المبيعات <bdi dir="ltr">25.00</bdi> {fx.CURRENCY}، وينضاف المبلغ إلى درج المحل.</p></div>
    <div class="success-card">
      <span class="success-card__badge">{icon("صح")}</span>
      <p class="success-card__status">تم تسجيل البيع</p>
      <p class="success-card__amount num"><bdi dir="ltr">25.00</bdi> <span style="font-size:16px">{fx.CURRENCY}</span></p>
      <p class="success-card__dest">أُضيف المبلغ إلى درج المحل</p>
      <div class="success-impact"><span class="success-impact__label">الكاش المسجل الآن</span>
      <span class="success-impact__value num"><bdi dir="ltr">161.00</bdi> <span style="font-size:14px">{fx.CURRENCY}</span></span></div>
      <p class="success-ref">عملية #142 · تراجع</p>
    </div>
  </div>
  <p class="meta">تسلسل إلزامي: رد فعل فوري ← حالة حفظ تمنع التكرار ← تأكيد بالمبلغ والوجهة ← عودة للسياق ← إبراز القيمة المتأثرة. بلا confetti/عدّاد/نبض. الحركة تخضع لـreduced-motion.</p>
</section>

<section class="blk">
  <h2 class="bt">علاقة النهاري والليلي</h2>
  <p>{cfg["dark_rationale"]}</p>
  <p class="meta">ليس انعكاسًا حرفيًا: التشبع مخفوف، الأدوار الدلالية الثمانية مميزة، وكل الأزواج أعيد قياسها (الجدول أعلاه).</p>
</section>
</div>
</body>
</html>'''

def fx_qab():
    items = []
    for l in fx.QAB:
        cls = " qab__btn--primary" if l == "بيع" else (" qab__btn--more" if l == "المزيد" else "")
        items.append(f'<button class="qab__btn{cls}"><span class="qab__icon">{icon(l)}</span><span class="qab__label">{l}</span></button>')
    return f'<section class="qab">{"".join(items)}</section>'

def rationale(direction):
    cfg = DIRS[direction]
    return f'''# Foundation Rationale — {cfg["title"]} (Agent-03)

## الأطروحة
{cfg["thesis"]}

## الصفات الخمس
{cfg["adjectives"]}

## المقارنة الـ16 المطلوبة (ملف 06)
1. **الأطروحة:** أعلاه.
2. **الصفات:** أعلاه.
3. **مراجع المزاج (مبادئ):** {cfg["mood"]}
4. **أدوار اللوحة نهاري/ليلي:** في foundation.html (لوحة الأساس) + tokens/contrast-evidence.json.
5. **جدول التباين:** مقيس فعليًا لكل زوج تشغيلي في الوضعين — كل الأزواج ناجحة (4.5:1 نص عادي، 3:1 نص كبير/أيقونات/حدود).
6. **سلم الطباعة:** IBM Plex Sans Arabic — هيرو 44/700، عنوان شاشة 18/700، عنوان وحدة 15/700، متن 15.5، ثانوي 13 — أرقام tabular معزولة bidi.
7. **الأسطح والعمق:** 4 مستويات (Canvas/Group/Reading/Overlay) — الظل للـOverlay فقط، مقسّمات للصفوف المتجانسة، لا بطاقة داخل بطاقة.
8. **الأيقونات:** عائلة واحدة Lucide-style inline SVG — 12 مفهومًا مطلوبًا، مرآة للاتجاهية فقط، وزن/حاوية للنشط.
9. **Business Status Hero:** حقل مهيمن واحد — موجبة/سالبة برقم، غير مكتملة بلا رقم (سبب + عدّاد + إجراء)، فارغة بتشجيع واضح.
10. **Micro Signal:** تينت/حد فقط — حالة ← سبب ← إجراء واحد.
11. **Quick Action Bar:** 5 عناصر بأيقونة + نص، بيع أساسي بتعبئة، قوة وزنية لا كرومية، لا FAB مزدوج.
12. **Success Impact storyboard:** معاينة أثر قبل الالتزام ← تأكيد بالمبلغ والوجهة ← إبراز الكاش 161.00 ← مرجع بشري #142 ← تراجع.
13. **الشاشات المطلوبة:** مغطاة في prototype/{direction}/ (9 شاشات × حالات).
14. **ثلاث نقاط قوة:** (أ) حقل مهيمن يجيب سؤال الوضع خلال ثوانٍ (ب) انضباط دلالي كامل للألوان (ج) عائلة نتيجة رباعية الحالات غير المكتملة فيها مواطن أول.
15. **ثلاث مخاطر:** (أ) {RISKS[direction][0]} (ب) {RISKS[direction][1]} (ج) {RISKS[direction][2]}
16. **عناصر تحتاج اختبار مستخدم:** قراءة العدّاد كمؤشر تقدم؛ ثقة القيم الافتراضية في النموذج؛ انطباع الجدية مقابل الدفء (C1)، أو "بنك أم لا" (C2)، أو الضجيج المدرك (C3).

## مصادر التنفيذ
- الأرقام والنصوص: 04-CONTENT-AND-DATA-FIXTURES.md حرفيًا (تحقق آلي grep في accessibility/qa-automated-report.md).
- القواعد الملزمة: 05-BOLD-MODULAR-VISUAL-RULES.md — ولا قاعدة واحدة خُففت؛ أُضيفت قيود صرامة أعلى (حصة طاقة، حظر Fill للإشارة، حبر داكن فوق الدافئ).
- القيم المساندة غير المحددة في التجهيزات: مركّبة وموثقة (D-010) وثابتة عبر الاتجاهات.
'''

RISKS = {
 "c1-warm-bold": ["ذوبان الجدية المالية في الدفء (السالبة تبدو لطيفة)", "تقارب الأمبر مع التيراكوتا يربك دلالة النقص", "زحف بيج-على-بيج"],
 "c2-confident-bold": ["الانزلاق نحو أزرق fintech عام", "ذوبان الهوية الدافئة إن قلّ نصيب التيراكوتا", "برود مؤسسي يرفع قلق غير المرخّصين (فرضية)"],
 "c3-dynamic-modular": ["التشظي/قوس قزح إن تهاوت حصة الوحدة الواحدة", "ضجيج مدرك على مستخدم خبرة محدودة", "أثقل عبء grayscale وعمى ألوان"],
}

def main():
    for d in DIRS:
        outdir = os.path.join(ROOT, "foundations", d)
        os.makedirs(outdir, exist_ok=True)
        open(os.path.join(outdir, "foundation.html"), "w", encoding="utf-8").write(board(d))
        open(os.path.join(outdir, "rationale.md"), "w", encoding="utf-8").write(rationale(d))
        print(f"foundation board + rationale → {d}")

if __name__ == "__main__":
    main()
