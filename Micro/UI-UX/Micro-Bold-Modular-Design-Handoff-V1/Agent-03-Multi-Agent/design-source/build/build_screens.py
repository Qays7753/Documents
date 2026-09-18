#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Micro Bold Modular — Agent-03 screen generator.
Generates identical-content HTML screens for C1/C2/C3 (fair comparison)
from fixtures.py; each direction links its own fully isolated CSS.
Run: python3 build_screens.py
"""
import os, sys, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fixtures as fx
from icons import icon, LOGO

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "/home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent"
PROTO = os.path.join(ROOT, "prototype")

DIRS = {
    "c1-warm-bold":       {"name": "C1 — Warm Bold",       "module_default": "home"},
    "c2-confident-bold":  {"name": "C2 — Confident Bold",  "module_default": "home"},
    "c3-dynamic-modular": {"name": "C3 — Dynamic Modular","module_default": "home"},
}
NAV = [("مشروعي الآن", "home", "home.html"), ("العمل", "work", "work.html"),
       ("المالية", "finance", "finance.html"), ("أدواتي", "tools", "tools.html"),
       ("السوق", "market", "market.html")]

def money(v, cls=""):
    c = f' {cls}' if cls else ""
    return f'<span class="num{c}"><bdi dir="ltr">{v}</bdi> <span class="cur">{fx.CURRENCY}</span></span>'

def bdi(v):
    return f'<bdi dir="ltr">{v}</bdi>'

def topzone():
    return f'''<header class="topzone">
  <button class="logo-btn" data-sheet="menu" aria-haspopup="dialog" aria-label="قائمة Micro — الحساب والمشروع والإعدادات">
    {LOGO}<span class="logo-word">Micro</span>
  </button>
  <div class="top-actions">
    <button class="top-chip" data-sheet="delivery">{icon("تسليم", "icon--sm")}<span>النقل والتوصيل</span></button>
    <button class="top-chip" data-sheet="ask">{icon("بحث", "icon--sm")}<span>Ask Micro</span></button>
  </div>
</header>'''

def bottomnav(active):
    tabs = []
    for label, key, href in NAV:
        cur = ' tab--active" aria-current="page' if key == active else ""
        tabs.append(f'<a class="tab{cur}" href="{href}" data-keep><span class="tab__wrap"><span class="tab__icon-wrap">{icon(label)}</span><span class="tab__label">{label}</span></span></a>')
    return f'<nav class="bottomnav" aria-label="التنقل الرئيسي">{"".join(tabs)}</nav>'

def sheets_block(with_qab=False):
    qab_stub = ""
    if with_qab:
        qab_stub = f'''
<div class="backdrop" data-close></div>
<div class="sheet" id="sheet-qab-stub" role="dialog" aria-modal="true" aria-labelledby="qab-stub-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="qab-stub-title">إجراء خارج نطاق النموذج</h2>
  <div class="stub-note">{icon("تنبيه")}<span>نموذج التصميم الحالي يعرض مسار «سجّل بيعًا» كاملًا كنمط للتسجيل. نماذج المصروف والطلب والتحصيل تُصمَّم في مرحلة لاحقة بعد اعتماد الاتجاه.</span></div>
  <div class="btn-row" style="margin-top:14px"><a class="btn btn--secondary" href="#" data-close>حسنًا</a></div>
</div>'''
    else:
        qab_stub = '\n<div class="backdrop" data-close></div>'
    menu_rows = "".join(
        f'''<a class="menu-row" href="tools.html#{key}" data-keep>
  <span class="menu-row__icon">{icon(ic)}</span>
  <span><span class="menu-row__title">{t}</span><br><span class="menu-row__sub">{s}</span></span>
  <span class="menu-row__chev">{icon("سهم-يسار", "icon--sm")}</span>
</a>''' for t, s, key, ic in [
            ("الحساب", "ليان — حلويات ليان", "account", "جهة"),
            ("بيانات المشروع", "الاسم، العملة، الفترة", "project", "محفظة"),
            ("الإعدادات", "اللغة، الوضع الليلي، التنبيهات", "settings", "سجل"),
            ("الحماية", "رمز الحماية (PIN)، الخصوصية", "protection", "درع"),
            ("بياناتي", "نسخة احتياطية — آخر نسخة: أمس", "data", "نسخ")])
    return qab_stub + f'''
<div class="sheet" id="sheet-menu" role="dialog" aria-modal="true" aria-labelledby="menu-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="menu-title">Micro — القائمة</h2>
  {menu_rows}
</div>
<div class="sheet" id="sheet-ask" role="dialog" aria-modal="true" aria-labelledby="ask-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="ask-title">Ask Micro</h2>
  <div class="stub-note">{icon("تنبيه")}<span>هذا الجزء خارج نطاق نموذج التصميم الحالي. Micro نظام مالي وتشغيلي، وليس شخصية محادثة.</span></div>
  <div class="btn-row" style="margin-top:14px"><a class="btn btn--secondary" href="#" data-close>إغلاق</a></div>
</div>
<div class="sheet" id="sheet-delivery" role="dialog" aria-modal="true" aria-labelledby="del-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="del-title">النقل والتوصيل</h2>
  <div class="stub-note">{icon("تنبيه")}<span>هذا الجزء خارج نطاق نموذج التصميم الحالي. حالات التوصيل ممثلة في شاشة العمل والطلب المتأخر.</span></div>
  <div class="btn-row" style="margin-top:14px"><a class="btn btn--secondary" href="#" data-close>إغلاق</a></div>
</div>
<div class="sheet" id="sheet-stub-records" role="dialog" aria-modal="true" aria-labelledby="rec-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="rec-title">السجل التفصيلي</h2>
  <div class="stub-note">{icon("تنبيه")}<span>السجل التفصيلي الكامل خارج نطاق نموذج التصميم. القيم المعروضة هنا من بيانات العرض الثابتة.</span></div>
  <div class="btn-row" style="margin-top:14px"><a class="btn btn--secondary" href="#" data-close>حسنًا</a></div>
</div>
<div class="sheet" id="sheet-collect" role="dialog" aria-modal="true" aria-labelledby="col-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="col-title">حصّل المبلغ</h2>
  <div class="stub-note">{icon("تحصيل")}<span>تحصيل من أم محمد — <bdi dir="ltr">25.00</bdi> د.أ منذ 3 أيام. نموذج تسجيل التحصيل يُصمَّم في مرحلة لاحقة بعد اعتماد الاتجاه؛ مسار «سجّل بيعًا» يعرض نمط التسجيل كاملًا.</span></div>
  <div class="btn-row" style="margin-top:14px"><a class="btn btn--secondary" href="#" data-close>حسنًا</a></div>
</div>
<div class="sheet" id="sheet-share" role="dialog" aria-modal="true" aria-labelledby="shr-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="shr-title">شارك تحديثًا مع الزبونة</h2>
  <div class="stub-note">{icon("مشاركة")}<span>مشاركة حالة الطلب مع سارة الخطيب عبر واتساب — خارج نطاق نموذج التصميم الحالي، ومخطط له ضمن نطاق المنتج.</span></div>
  <div class="btn-row" style="margin-top:14px"><a class="btn btn--secondary" href="#" data-close>حسنًا</a></div>
</div>
<div class="sheet" id="sheet-complete" role="dialog" aria-modal="true" aria-labelledby="cpl-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="cpl-title">أكمل التكلفة</h2>
  <div class="stub-note">{icon("التكلفة")}<span>باقي تسجيل تكلفة عمليتين بيع من أصل 10 عمليات اليوم. التكلفة هي ثمن ما بِعتَه (مواد وتغليف)، وليست مصروفًا عامًا. شاشة الإكمال تُصمَّم بعد اعتماد الاتجاه.</span></div>
  <div class="btn-row" style="margin-top:14px"><a class="btn btn--secondary" href="#" data-close>حسنًا</a></div>
</div>
<div class="sheet" id="sheet-costs" role="dialog" aria-modal="true" aria-labelledby="cst-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="cst-title">راجع التكاليف</h2>
  <div class="stub-note">{icon("التكلفة")}<span>مراجعة تكاليف اليوم (<bdi dir="ltr">108.75</bdi> د.أ أعلى من المعتاد). تفاصيل بنود التكاليف خارج نطاق نموذج التصميم الحالي.</span></div>
  <div class="btn-row" style="margin-top:14px"><a class="btn btn--secondary" href="#" data-close>حسنًا</a></div>
</div>
<div class="sheet" id="sheet-op" role="dialog" aria-modal="true" aria-labelledby="op-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="op-title">عملية <bdi dir="ltr">#142</bdi></h2>
  <div class="stub-note">{icon("سجل")}<span>تفاصيل العملية — بيع <bdi dir="ltr">25.00</bdi> د.أ، أُضيفت إلى درج المحل. السجل التفصيلي الكامل خارج نطاق نموذج التصميم.</span></div>
  <div class="btn-row" style="margin-top:14px"><a class="btn btn--secondary" href="#" data-close>حسنًا</a></div>
</div>
<div class="sheet" id="sheet-order-action" role="dialog" aria-modal="true" aria-labelledby="oa-title">
  <div class="sheet__handle"></div>
  <h2 class="sheet__title" id="oa-title">حدّث حالة الطلب</h2>
  <div class="stub-note">{icon("طلب")}<span>تحديث طلب سارة الخطيب — تجاوز موعد التسليم يومًا. الشاشة الكاملة للطلب متاحة في تبويب العمل.</span></div>
  <div class="btn-row" style="margin-top:14px"><a class="btn btn--primary" href="order.html" data-keep>افتح الطلب</a></div>
</div>'''

def page(direction, title, module, active_tab, body, with_qab_sheets=False, extra=""):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl" data-theme="light" data-direction="{direction}" data-module="{module}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Micro — {DIRS[direction]["name"]}</title>
<link rel="stylesheet" href="screen.css">
{extra}
</head>
<body>
<div class="phone">
{topzone()}
<main class="content" id="main">
{body}
</main>
{bottomnav(active_tab)}
{sheets_block(with_qab_sheets)}
</div>
<script src="screen.js"></script>
</body>
</html>'''

# ---------------- shared components ----------------

def project_context():
    return f'''<div class="project-context">
  <span class="project-name">{fx.PROJECT["name"]}</span>
  <span class="project-period">{fx.PROJECT["period"]}</span>
</div>'''

def qab():
    items = []
    for label in fx.QAB:
        if label == "بيع":
            items.append(f'''<a class="qab__btn qab__btn--primary" href="sale.html" data-keep aria-label="سجّل بيعًا">
  <span class="qab__icon">{icon(label)}</span><span class="qab__label">{label}</span></a>''')
        elif label == "المزيد":
            items.append(f'''<a class="qab__btn qab__btn--more" href="more.html" data-keep aria-label="المزيد من الإجراءات">
  <span class="qab__icon">{icon(label)}</span><span class="qab__label">{label}</span></a>''')
        else:
            items.append(f'''<button class="qab__btn" data-sheet="qab-stub" aria-label="سجّل {label}">
  <span class="qab__icon">{icon(label)}</span><span class="qab__label">{label}</span></button>''')
    return f'<section class="qab" aria-label="إجراءات سريعة">{"".join(items)}</section>'

def hero_A():
    a = fx.A
    return f'''<section class="hero" aria-label="وضع المشروع">
  <div class="hero__head">
    <span class="hero__label">{a["hero_label"]}</span>
    <span class="state-chip state-chip--pos">{icon("سهم-أعلى", "icon--sm")}{a["hero_state"]}</span>
  </div>
  <p class="hero__result num">{bdi(a["hero_result"])} <span style="font-size:1.25rem">{fx.CURRENCY}</span></p>
  <p class="hero__explain">{a["hero_explain"]}</p>
</section>'''

def hero_B():
    b = fx.B
    segs = "".join(f'<span class="meter__seg{" meter__seg--on" if i < b["completion_done"] else ""}"></span>' for i in range(b["completion_total"]))
    return f'''<section class="hero" aria-label="وضع المشروع">
  <div class="hero__head">
    <span class="hero__label">{b["hero_label"]}</span>
    <span class="state-chip state-chip--att">{icon("تنبيه", "icon--sm")}{b["hero_state"]}</span>
  </div>
  <p class="hero__reason">{b["reason"]}</p>
  <div class="hero__meter" role="img" aria-label="اكتمال التكلفة: {b["completion_done"]} من {b["completion_total"]} عمليات">
    {segs}<span class="meter__count num">{b["completion_done"]} من {b["completion_total"]} عمليات مكتملة التكلفة</span>
  </div>
  <div class="hero__supporting">
    <span class="s-label">{b["supporting"]}:</span>
    <span class="s-value num">{money(b["supporting_value"])}</span>
  </div>
  <div class="hero__actions">
    <a class="btn btn--hero" href="#" data-sheet="complete">{icon("التكلفة", "icon--sm")}{b["action"]}</a>
  </div>
</section>'''

def hero_C():
    c = fx.C
    return f'''<section class="hero hero--neg" aria-label="وضع المشروع">
  <div class="hero__head">
    <span class="hero__label">{c["hero_label"]}</span>
    <span class="state-chip state-chip--neg">{icon("سهم-أسفل", "icon--sm")}{c["hero_state"]}</span>
  </div>
  <p class="hero__result num">{bdi(c["hero_result"])} <span style="font-size:1.25rem">{fx.CURRENCY}</span></p>
  <p class="hero__reason" style="font-size:0.9375rem; font-weight:500;">{c["reason"]}</p>
  <div class="hero__mini">
    <span class="m"><span class="m-label">مبيعات اليوم</span><span class="m-value num">{money(c["sales"])}</span></span>
    <span class="m"><span class="m-label">المصاريف والتكاليف</span><span class="m-value num">{money(c["expenses"])}</span></span>
  </div>
  <div class="hero__actions">
    <a class="btn btn--hero" href="#" data-sheet="costs">{icon("التكلفة", "icon--sm")}{c["action"]}</a>
  </div>
</section>'''

def signal(sig):
    return f'''<section class="signal" aria-label="إشارة Micro">
  <span class="signal__icon">{icon("تنبيه")}</span>
  <div class="signal__body">
    <p class="signal__status">{sig["status"]}</p>
    <p class="signal__reason">{sig["reason"]}</p>
    <div class="signal__action">
      <a class="btn btn--secondary btn--sm" href="#" data-sheet="{"collect" if sig is fx.A["signal"] else "order-action"}">{icon("تحصيل", "icon--sm")}{sig["action"]}</a>
    </div>
  </div>
</section>'''

def metric_list(title, icon_name, rows, link=None):
    row_html = "".join(
        f'''<button class="metric-row metric-row--due" data-sheet="stub-records">
  <span class="metric-row__icon">{icon(r.get("icon", icon_name))}</span>
  <span><span class="metric-row__label">{r["label"]}</span>{f'<br><span class="metric-row__hint">{r["hint"]}</span>' if r.get("hint") else ""}</span>
  <span class="metric-row__value">{money(r["value"])}{f'<span class="metric-row__chev">{icon("سهم-يسار", "icon--sm")}</span>' if r.get("chev", True) else ""}</span>
</button>''' for r in rows)
    link_html = f'<a class="section__link" href="{link[1]}" data-keep>{link[0]}</a>' if link else ""
    return f'''<section class="section">
  <h2 class="section__title">{icon(icon_name)}{title}</h2>{link_html}
  <div class="metric-list">{row_html}</div>
</section>'''

def attention_delayed():
    d = fx.D
    return f'''<section class="section">
  <h2 class="section__title">{icon("ساعة")}انتباه العمل</h2>
  <div class="attention-card">
    <div class="attention-card__top">
      <span class="attention-card__title">{d["customer"]} — {d["order"]}</span>
      <span class="late-chip">{icon("تنبيه", "icon--sm")}{d["state"]}</span>
    </div>
    <p class="attention-card__sub">موعد التسليم {bdi(d["delivery_date"])} · المرحلة الحالية: {d["stage"]}</p>
    <div class="attention-card__actions">
      <a class="btn btn--primary btn--sm" href="order.html" data-keep>{d["primary"]}</a>
      <a class="btn btn--ghost btn--sm" href="#" data-sheet="share">{icon("مشاركة", "icon--sm")}{d["secondary"]}</a>
    </div>
  </div>
</section>'''

def attention_collection(amount):
    return f'''<section class="section">
  <h2 class="section__title">{icon("ساعة")}انتباه العمل</h2>
  <div class="attention-card" style="border-inline-start-color: var(--trust)">
    <div class="attention-card__top">
      <span class="attention-card__title">مبالغ بانتظار التحصيل</span>
    </div>
    <p class="attention-card__sub">عندك {money(amount)} عند العملاء</p>
    <div class="attention-card__actions">
      <a class="btn btn--secondary btn--sm" href="finance.html" data-keep>راجع التحصيل</a>
    </div>
  </div>
</section>'''

def recent(rows):
    items = []
    for kind, what, amount, when, tag in rows:
        tag_html = f'<span class="tag">{icon("تنبيه", "icon--sm")}{tag}</span>' if tag else ""
        items.append(f'''<div class="activity-row">
  <span class="activity-row__icon">{icon("بيع" if kind == "بيع" else ("تحصيل" if kind == "تحصيل" else "مصروف"))}</span>
  <span><span class="activity-row__title">{kind} — {what}{tag_html}</span><br><span class="activity-row__time">{when}</span></span>
  <span class="activity-row__value">{money(amount)}</span>
</div>''')
    return f'''<section class="section">
  <h2 class="section__title">{icon("سجل")}آخر النشاطات</h2>
  <div class="metric-list" style="padding: 4px 16px">{"".join(items)}</div>
  <a class="btn btn--text" href="#" data-sheet="stub-records">كل السجل — السجل الكامل خارج نطاق النموذج</a>
</section>'''

# ---------------- screens ----------------

def build_home(direction):
    a, b, c, h = fx.A, fx.B, fx.C, fx.H
    st_pos = f'''{hero_A()}
{signal(a["signal"])}
{qab()}
{metric_list("ملخص اليوم", "الكاش", [
    {"label": "مبيعات اليوم", "value": a["sales"], "icon": "بيع", "hint": "قيم اليوم المسجلة"},
    {"label": "الكاش المسجل", "value": a["cash"], "icon": "الكاش", "hint": "درج المحل"},
])}
{metric_list("الاستحقاقات", "الدين", [
    {"label": "لي عند العملاء", "value": a["due_from"], "icon": "جهة", "hint": "مبالغ بانتظار التحصيل"},
    {"label": "عليّ للموردين", "value": a["due_to"], "icon": "مورد", "hint": "مبالغ عليك دفعها"},
    {"label": "دفعات لاحقة", "value": "50.00", "icon": "موعد", "hint": "مبالغ عند اكتمال الطلبات — طلب سارة الخطيب"},
])}
{attention_delayed()}
{recent(a["recent"])}'''
    st_inc = f'''{hero_B()}
{signal(b["signal"])}
{qab()}
{metric_list("ملخص اليوم", "الكاش", [
    {"label": "الكاش المسجل", "value": b["cash"], "icon": "الكاش", "hint": "درج المحل"},
])}
{metric_list("الاستحقاقات", "الدين", [
    {"label": "لي عند العملاء", "value": b["due_from"], "icon": "جهة", "hint": "مبالغ بانتظار التحصيل"},
    {"label": "عليّ للموردين", "value": b["due_to"], "icon": "مورد", "hint": "مبالغ عليك دفعها"},
])}
{attention_collection(b["due_from"])}
{recent(b["recent"])}'''
    st_neg = f'''{hero_C()}
{signal(c["signal"])}
{qab()}
{metric_list("ملخص اليوم", "الكاش", [
    {"label": "مبيعات اليوم", "value": c["sales"], "icon": "بيع", "hint": "قيم اليوم المسجلة"},
    {"label": "الكاش المسجل", "value": c["cash"], "icon": "الكاش", "hint": "درج المحل"},
])}
{metric_list("الاستحقاقات", "الدين", [
    {"label": "لي عند العملاء", "value": c["due_from"], "icon": "جهة", "hint": "مبالغ بانتظار التحصيل"},
    {"label": "عليّ للموردين", "value": c["due_to"], "icon": "مورد", "hint": "مبالغ عليك دفعها"},
])}
{attention_collection(c["due_from"])}
{recent(c["recent"])}'''
    st_empty = f'''<section class="empty-card" aria-label="لا مبيعات اليوم">
  <span class="empty-card__icon">{icon("بيع")}</span>
  <p class="empty-card__title">{h["title"]}</p>
  <p class="empty-card__desc">{h["description"]}</p>
  <div style="margin-top:16px"><a class="btn btn--primary" href="sale.html" data-keep>{icon("بيع", "icon--sm")}{h["action"]}</a></div>
  <p class="empty-card__note">{h["reassurance"]}</p>
</section>
{qab()}'''
    body = f'''{project_context()}
<section data-screen-state="positive" class="is-active" aria-label="حالة نتيجة موجبة">{st_pos}</section>
<section data-screen-state="incomplete" aria-label="حالة نتيجة غير مكتملة">{st_inc}</section>
<section data-screen-state="negative" aria-label="حالة نتيجة سالبة">{st_neg}</section>
<section data-screen-state="empty" aria-label="حالة يوم بدون مبيعات">{st_empty}</section>'''
    return page(direction, "مشروعي الآن", "home", "home", body, with_qab_sheets=True)

def build_work(direction):
    d = fx.D
    orders = []
    for o in fx.COMPOSED["work_orders"]:
        chip = "late" if o["late"] else ("agreement" if o["stage"] == "اتفاق" else "executing")
        chip_txt = ("متأخر · " + o["stage"]) if o["late"] else o["stage"]
        orders.append(f'''<a class="order-card" href="order.html" data-keep style="text-decoration:none;color:inherit;display:block">
  <div class="order-card__top">
    <span><span class="order-card__name">{o["customer"]}</span><br><span class="order-card__item">{o["item"]}</span></span>
    <span class="stage-chip stage-chip--{chip}">{icon("تنبيه" if o["late"] else "موعد", "icon--sm")}{chip_txt}</span>
  </div>
  <div class="order-steps" style="margin-top:12px">{''.join(f'<span class="ostep{" ostep--current" if s == o["stage"] and not o["late"] else ""}{" ostep--late ostep--current" if s == o["stage"] and o["late"] else ""}"><span class="ostep__dot"></span><span class="ostep__label">{s}</span></span>' for s in fx.ORDER_STAGES)}</div>
</a>''')
    ready = "".join(
        f'''<div class="activity-row"><span class="activity-row__icon">{icon("طلب")}</span>
  <span><span class="activity-row__title">{r["customer"]} — {r["item"]}</span><br><span class="activity-row__time">جاهز للتسليم اليوم</span></span>
  <span class="stage-chip stage-chip--ready">{r["stage"]}</span></div>''' for r in fx.COMPOSED["work_ready"])
    upcoming = "".join(
        f'''<div class="activity-row"><span class="activity-row__icon">{icon("موعد")}</span>
  <span><span class="activity-row__title">{u["label"]}</span><br><span class="activity-row__time">{u["who"]}</span></span>
  <span class="activity-row__value" style="font-size:0.84375rem;color:var(--ink2)">{bdi(u["when"])}</span></div>''' for u in fx.COMPOSED["work_upcoming"])
    completed = "".join(
        f'''<div class="activity-row"><span class="activity-row__icon">{icon("تسليم")}</span>
  <span><span class="activity-row__title">{w["label"]}</span><br><span class="activity-row__time">{w["who"]}</span></span>
  <span class="activity-row__time">{w["when"]}</span></div>''' for w in fx.COMPOSED["work_completed"])
    body = f'''{project_context()}
<div class="search-row">{icon("بحث")}<input type="search" placeholder="ابحث عن طلب أو زبون" aria-label="بحث في العمل"></div>
<section class="section">
  <h2 class="section__title">{icon("تنبيه")}الأولوية الحالية</h2>
  <div class="attention-card">
    <div class="attention-card__top">
      <span class="attention-card__title">{d["customer"]} — {d["order"]}</span>
      <span class="late-chip">{icon("تنبيه", "icon--sm")}{d["state"]}</span>
    </div>
    <p class="attention-card__sub">موعد التسليم {bdi(d["delivery_date"])} · المرحلة: {d["stage"]} · المتبقي {money(d["remaining"])}</p>
    <div class="attention-card__actions">
      <a class="btn btn--primary btn--sm" href="order.html" data-keep>{d["primary"]}</a>
      <a class="btn btn--ghost btn--sm" href="#" data-sheet="share">{icon("مشاركة", "icon--sm")}{d["secondary"]}</a>
    </div>
  </div>
</section>
<section class="section">
  <h2 class="section__title">{icon("طلب")}الطلبات النشطة</h2>
  {''.join(orders)}
</section>
<section class="section">
  <h2 class="section__title">{icon("تسليم")}جاهز للتسليم</h2>
  <div class="metric-list" style="padding: 4px 16px">{ready}</div>
</section>
<section class="section">
  <h2 class="section__title">{icon("موعد")}مواعيد قادمة</h2>
  <div class="metric-list" style="padding: 4px 16px">{upcoming}</div>
</section>
<section class="section">
  <h2 class="section__title">{icon("صح")}أُنجز مؤخرًا</h2>
  <div class="metric-list" style="padding: 4px 16px">{completed}</div>
</section>'''
    return page(direction, "العمل", "work", "work", body)

def build_finance(direction):
    a = fx.A
    body = f'''{project_context()}
<section class="fin-hero">
  <p class="fin-hero__period">{icon("موعد", "icon--sm")}{fx.PROJECT["period"]} · اكتمال البيانات: <strong>10 من 10 عمليات</strong></p>
  <p class="fin-hero__value num"><bdi dir="ltr">+42.50</bdi> <span style="font-size:1rem">{fx.CURRENCY}</span></p>
  <span class="state-chip state-chip--pos">{icon("سهم-أعلى", "icon--sm")}{a["hero_state"]}</span>
</section>
{metric_list("الكاش", "الكاش", [
    {"label": "الكاش المسجل", "value": a["cash"], "icon": "الكاش", "hint": "درج المحل"},
])}
{metric_list("الاستحقاقات", "الدين", [
    {"label": "لي عند العملاء", "value": a["due_from"], "icon": "جهة", "hint": "مبالغ بانتظار التحصيل"},
    {"label": "عليّ للموردين", "value": a["due_to"], "icon": "مورد", "hint": "مبالغ عليك دفعها"},
    {"label": "دفعات لاحقة", "value": "50.00", "icon": "موعد", "hint": "مبالغ عند اكتمال الطلبات — طلب سارة الخطيب"},
])}
<section class="insight-card">
  <span class="signal__icon">{icon("تنبيه")}</span>
  <div>
    <p class="insight-card__status">{a["signal"]["status"]}</p>
    <p class="insight-card__body">أم محمد عليها {bdi("25.00")} {fx.CURRENCY} منذ 3 أيام</p>
    <div style="margin-top:10px"><a class="btn btn--primary btn--sm" href="#" data-sheet="collect">{a["signal"]["action"]}</a></div>
  </div>
</section>
<div class="amount-list">
  <div class="amount-row amount-row--total"><span class="amount-row__label">{icon("النتيجة", "icon--sm")}نتيجة اليوم بعد التكاليف</span><span class="amount-row__value num">{money(a["hero_result"])}</span></div>
</div>
<p style="font-size:0.8125rem;color:var(--ink2);padding-inline:4px">القيم من بيانات العرض الثابتة لليوم. السجل التفصيلي وملخص الفترة خارج نطاق نموذج التصميم.</p>'''
    return page(direction, "المالية", "finance", "finance", body)

def build_tools(direction):
    groups = [
        ("protection", "الحماية", "درع", [
            ("row", "رمز الحماية (PIN)", "مطلوب عند فتح التطبيق", "switch"),
            ("row", "قفل التطبيق", "إغلاق تلقائي بعد دقيقة", "switch"),
            ("stub", "الخصوصية", "ما يُخزن على جهازك فقط", "خصوصية"),
        ]),
        ("data", "بياناتي", "نسخ", [
            ("stub", "نسخة احتياطية", "آخر نسخة: أمس 23:00", "نسخ"),
            ("stub", "تصدير البيانات", "ملف يمكنك الاحتفاظ به", "سجل"),
            ("stub", "استيراد", "من ملف نسخة سابقة", "سهم-أسفل"),
        ]),
        ("tools", "أدوات المشروع", "حاسبة", [
            ("stub", "الآلة الحاسبة", "حسابات سريعة", "حاسبة"),
            ("stub", "تفعيل المخزون", "مغلق حاليًا", "مخزون"),
            ("stub", "الشيكات", "متابعة الشيكات المستحقة", "سجل"),
        ]),
        ("account", "الحساب والمشروع", "جهة", [
            ("stub", "الحساب", "ليان — حلويات ليان", "جهة"),
            ("stub", "بيانات المشروع", "الاسم، العملة، الفترة", "محفظة"),
            ("settings", "الإعدادات", "الوضع الليلي واللغة والتنبيهات", "سجل"),
        ]),
    ]
    html_groups = []
    for anchor, title, ic, rows in groups:
        rows_html = ""
        for r in rows:
            if r[0] == "settings":
                rows_html += f'''<div class="tool-row" id="settings"><span class="tool-row__icon">{icon("قمر")}</span>
  <span><span class="tool-row__title">الوضع الليلي</span><br><span class="tool-row__sub">حسب تفضيلك — يُحفظ على جهازك</span></span>
  <button class="switch" aria-label="تبديل الوضع الليلي"></button></div>'''
            elif r[0] == "row":
                rows_html += f'''<div class="tool-row"><span class="tool-row__icon">{icon("درع")}</span>
  <span><span class="tool-row__title">{r[1]}</span><br><span class="tool-row__sub">{r[2]}</span></span>
  <button class="switch" aria-label="{r[1]}"></button></div>'''
            else:
                rows_html += f'''<button class="tool-row" data-sheet="stub-records"><span class="tool-row__icon">{icon(r[3])}</span>
  <span><span class="tool-row__title">{r[1]}</span><br><span class="tool-row__sub">{r[2]}</span></span>
  <span class="metric-row__chev">{icon("سهم-يسار", "icon--sm")}</span></button>'''
        extra_anchor = '<span id="project"></span>' if anchor == 'account' else ''
        html_groups.append(f'''<section class="tool-group" id="{anchor}">{extra_anchor}
  <h2 class="tool-group__title">{icon(ic)}{title}</h2>
  {rows_html}
</section>''')
    body = f'''{project_context()}
{''.join(html_groups)}
<p style="font-size:0.8125rem;color:var(--ink2);padding-inline:4px"><!-- IA-D03 -->
<p style="font-size:0.8125rem;color:var(--ink2);padding-inline:4px">إعدادات الحماية تبقى ظاهرة حتى لو لم يكتمل إعداد المشروع.</p></p>'''
    return page(direction, "أدواتي", "tools", "tools", body)

def build_market(direction):
    body = f'''{project_context()}
<section class="market-hero">
  {icon("مستقبل", "icon--lg")}
  <p class="market-hero__title">السوق — قريبًا</p>
  <p class="market-hero__sub">مساحة مستقبلية داخل Micro لعرض منتجاتك وخدماتك أمام جمهور أوسع.</p>
  <span class="not-now">{icon("تنبيه", "icon--sm")}غير متاح حاليًا — وعد مستقبلي صادق، لا سوق فعلي بعد</span>
</section>
<section class="section">
  <h2 class="section__title">{icon("سهم-أعلى")}ما سيصبح ممكنًا</h2>
  <div class="metric-list" style="padding: 4px 16px">
    <div class="promise-row"><span class="promise-row__icon">{icon("السوق")}</span><span><span class="promise-row__title">وصول أوسع</span><br><span class="promise-row__body">عرض منتجاتك وخدماتك لجمهور جديد</span></span></div>
    <div class="promise-row"><span class="promise-row__icon">{icon("طلب")}</span><span><span class="promise-row__title">طلبات أوضح</span><br><span class="promise-row__body">طلب يصل مباشرة إلى سجل عملك</span></span></div>
  </div>
</section>
<section class="section">
  <h2 class="section__title">{icon("سهم-أسفل")}ما هو غير متاح الآن</h2>
  <div class="metric-list" style="padding: 4px 16px">
    <div class="promise-row"><span class="promise-row__icon">{icon("إغلاق")}</span><span><span class="promise-row__title">لا يوجد سوق فعلي</span><br><span class="promise-row__body">هذه الشاشة تصميم لحالة مستقبلية فقط ولا تعني إتاحة تشغيلية</span></span></div>
  </div>
</section>
<button class="btn btn--secondary btn--block" id="notify-btn" data-sheet="stub-records">{icon("تنبيه", "icon--sm")}أبلغني عندما يجهز السوق</button>'''
    return page(direction, "السوق", "market", "market", body)

def build_products(direction):
    prows = "".join(
        f'''<div class="prod-row">
  <span class="prod-row__icon">{icon("السوق")}</span>
  <span><span class="activity-row__title">{p["name"]}</span><br><span class="activity-row__time">سعر مرجعي</span></span>
  <span style="margin-inline-start:auto;display:flex;align-items:center;gap:8px">
    <span class="type-chip type-chip--{'product' if p['type'] == 'منتج' else 'service'}">{p["type"]}</span>
    <span class="activity-row__value num">{money(p["price"]) if p["price"][0].isdigit() else p["price"]}</span>
  </span>
</div>''' for p in fx.COMPOSED["products"])
    body = f'''<div class="project-context">
  <span class="project-name">منتجاتي وخدماتي</span>
  <span class="project-period">شاشة سياقية — تُفتح من عدة أماكن</span>
</div>
<div class="search-row">{icon("بحث")}<input type="search" placeholder="ابحث عن منتج أو خدمة" aria-label="بحث في المنتجات"></div>
<div class="choice-row" role="group" aria-label="تصفية">
  <button class="choice choice--on"><span class="choice__dot"></span>الكل</button>
  <button class="choice"><span class="choice__dot"></span>منتجات</button>
  <button class="choice"><span class="choice__dot"></span>خدمات</button>
</div>
<div class="metric-list">
{prows}
</div>
<button class="btn btn--primary btn--block" data-sheet="stub-records">{icon("زائد", "icon--sm")}أضف منتجًا أو خدمة</button>
<!-- IA-D02 -->
<p style="font-size:0.8125rem;color:var(--ink2);padding-inline:4px">قائمة مرجعية لأسعارك — لا تعني تتبع مخزون.</p>'''
    return page(direction, "منتجاتي وخدماتي", "home", "home", body)

def build_order(direction):
    d = fx.D
    steps = ""
    for s in fx.ORDER_STAGES:
        cls = "ostep--done" if fx.ORDER_STAGES.index(s) < fx.ORDER_STAGES.index(d["stage"]) else ""
        if s == d["stage"]:
            cls = "ostep--current ostep--late" if True else "ostep--current"
        steps += f'<span class="ostep {cls}"><span class="ostep__dot"></span><span class="ostep__label">{s}</span></span>'
    body = f'''<div class="project-context">
  <span class="project-name">{d["customer"]}</span>
  <span class="late-chip">{icon("تنبيه", "icon--sm")}{d["state"]}</span>
</div>
<section class="order-card">
  <div class="order-card__top">
    <span><span class="order-card__name">{d["order"]}</span><br>
    <span class="order-card__item">موعد التسليم المتفق عليه: {bdi(d["delivery_date"])}</span></span>
  </div>
  <div class="order-steps" style="margin-top:16px">{steps}</div>
</section>
<div class="amount-list">
  <div class="amount-row"><span class="amount-row__label">{icon("محفظة", "icon--sm")}المبلغ المتفق عليه</span><span class="amount-row__value num">{money(d["agreed"])}</span></div>
  <div class="amount-row"><span class="amount-row__label">{icon("الكاش", "icon--sm")}العربون المدفوع</span><span class="amount-row__value num">{money(d["deposit"])}</span></div>
  <div class="amount-row amount-row--total amount-row--remaining"><span class="amount-row__label">{icon("الدين", "icon--sm")}المتبقي على الزبونة</span><span class="amount-row__value num">{money(d["remaining"])}</span></div>
</div>
<div class="btn-row">
  <button class="btn btn--primary" id="advance-stage">{icon("موعد", "icon--sm")}{d["primary"]}</button>
  <button class="btn btn--ghost" data-sheet="share">{icon("مشاركة", "icon--sm")}{d["secondary"]}</button>
</div>
<p style="font-size:0.8125rem;color:var(--ink2);padding-inline:4px">عرض توضيحي: تحديث الحالة يقدّم المرحلة في سكة الطلبات (اتفاق ← تنفيذ ← جاهز ← تم التسليم).</p>'''
    return page(direction, "طلب متأخر", "work", "work", body)

def build_sale(direction):
    f, g, i, j = fx.F, fx.G, fx.I, fx.J
    form_state = f'''<form id="sale-form" data-screen-state="form" class="is-active" novalidate>
  <div class="project-context">
    <span class="project-name">{f["title"]}</span>
    <a class="btn btn--text" href="home.html" data-keep>{f["secondary"]}</a>
  </div>
  <div class="field amount-field">
    <label class="field__label" for="amount">{f["amount_label"]}</label>
    <input class="field__input" id="amount" name="amount" type="text" inputmode="decimal" value="{f["amount"]}" autocomplete="off" aria-describedby="amount-error">
    <span class="cur-mark">{fx.CURRENCY}</span>
  </div>
  <p class="field-error is-hidden" id="amount-error" role="alert">{icon("تنبيه", "icon--sm")}{i["message"]}</p>
  <div class="field">
    <span class="field__label">حالة الدفع</span>
    <div class="choice-row">
      <button type="button" class="choice choice--on" aria-pressed="true"><span class="choice__dot"></span>{f["payment"]}</button>
      <button type="button" class="choice" aria-pressed="false"><span class="choice__dot"></span>عربون</button>
      <button type="button" class="choice" aria-pressed="false"><span class="choice__dot"></span>على الحساب</button>
    </div>
  </div>
  <div class="field">
    <label class="field__label" for="customer">الزبون</label>
    <input class="field__input" id="customer" name="customer" type="text" value="{f["customer"]}">
  </div>
  <div class="field">
    <label class="field__label" for="destination">وجهة المبلغ</label>
    <input class="field__input" id="destination" name="destination" type="text" value="{f["destination"]}">
  </div>
  <div class="field">
    <label class="field__label" for="date">التاريخ</label>
    <input class="field__input" id="date" name="date" type="text" value="18/09/2026" inputmode="numeric" readonly>
  </div>
  <section class="impact-preview">
    <p class="impact-preview__title">{icon("النتيجة", "icon--sm")}{f["preview_title"]}</p>
    <p class="impact-preview__body">{f["preview"]}</p>
  </section>
  <div class="btn-row">
    <a class="btn btn--primary" href="sale.html?state=success" id="submit-sale" data-keep>{icon("بيع", "icon--sm")}{f["primary"]}</a>
  </div>
</form>'''
    # validation state: same form, deep-linked with state=validation
    validation_state = form_state.replace('data-screen-state="form"', 'data-screen-state="validation"').replace('value="{f["amount"]}"', 'value="0"').replace('id="amount-error"', 'id="amount-error"')
    success_state = f'''<section data-screen-state="success" aria-label="نجاح تسجيل البيع">
  <div class="success-card">
    <span class="success-card__badge">{icon("صح")}</span>
    <p class="success-card__status">{g["status"]}</p>
    <p class="success-card__amount num">{bdi(g["amount"])} <span style="font-size:1rem">{fx.CURRENCY}</span></p>
    <p class="success-card__dest">{g["destination"]}</p>
    <div class="success-impact">
      <span class="success-impact__label">{g["updated_label"]}</span>
      <span class="success-impact__value num">{bdi(g["updated_value"])} <span style="font-size:0.875rem">{fx.CURRENCY}</span></span>
    </div>
    <p class="success-ref">عملية <bdi dir="ltr">#142</bdi></p>
    <div class="btn-row">
      <a class="btn btn--secondary" href="#" data-sheet="op">{g["primary"]}</a>
      <a class="btn btn--text" href="sale.html" data-keep>{g["recovery"]}</a>
    </div>
  </div>
</section>'''
    error_state = f'''<section data-screen-state="system-error" aria-label="خطأ في الحفظ">
  <div class="error-card">
    <p class="error-card__title">{icon("تنبيه")}{j["title"]}</p>
    <p class="error-card__body">{j["description"]}</p>
    <div class="btn-row" style="margin-top:16px">
      <a class="btn btn--primary" href="sale.html?state=success" data-keep>{j["primary"]}</a>
      <a class="btn btn--secondary" href="sale.html" data-keep>{j["secondary"]}</a>
    </div>
  </div>
</section>'''
    body = form_state + "\n" + success_state + "\n" + error_state
    return page(direction, "سجّل بيعًا", "home", "home", body, with_qab_sheets=True)

def build_more(direction):
    quick = "".join(
        f'''<a class="qab__btn{' qab__btn--primary' if l == 'بيع' else ''}" href="sale.html" data-keep>
  <span class="qab__icon">{icon(l)}</span><span class="qab__label">{l}</span></a>''' if l == "بيع" else
        (f'''<button class="qab__btn" data-sheet="qab-stub"><span class="qab__icon">{icon(l)}</span><span class="qab__label">{l}</span></button>''' if l != "المزيد" else "")
        for l in fx.QAB)
    rows = ""
    for t, s, dest in fx.MORE_SHEET:
        if dest == "products":
            rows += f'''<a class="menu-row" href="products.html" data-keep><span class="menu-row__icon">{icon("السوق")}</span><span><span class="menu-row__title">{t}</span><br><span class="menu-row__sub">{s}</span></span><span class="menu-row__chev">{icon("سهم-يسار", "icon--sm")}</span></a>'''
        else:
            rows += f'''<button class="menu-row" data-sheet="stub-records"><span class="menu-row__icon">{icon("سجل")}</span><span><span class="menu-row__title">{t}</span><br><span class="menu-row__sub">{s} — خارج نطاق النموذج</span></span><span class="menu-row__chev">{icon("سهم-يسار", "icon--sm")}</span></button>'''
    body = f'''<div class="project-context">
  <span class="project-name">المزيد</span>
  <span class="project-period">إجراءات وأدوات إضافية</span>
</div>
<section class="qab" aria-label="إجراءات سريعة">{quick}</section>
<section class="sheet" style="position:static;transform:none;box-shadow:none;border-radius:var(--r-card);border:1px solid var(--divider);max-height:none;padding:14px 12px" aria-label="أدوات إضافية">
  {rows}
</section>
<div class="stub-note">{icon("تنبيه")}<span>الأدوات المعروضة كواجهة توضيحية تعتمد نطاق نموذج التصميم. شاشات كاملة متوفرة: مشروعي الآن، العمل، المالية، أدواتي، السوق، منتجاتي وخدماتي، الطلب المتأخر، تسجيل بيع.</span></div>'''
    return page(direction, "المزيد", "home", "home", body, with_qab_sheets=True)

# ---------------- runner ----------------

def main():
    for d in DIRS:
        out = os.path.join(PROTO, d)
        os.makedirs(out, exist_ok=True)
        css_src = open(os.path.join(HERE, "..", "design", f"{d.split('-')[0]}.css"), encoding="utf-8").read()
        css_src = css_src.replace("__FONTS__", "../assets/fonts")
        open(os.path.join(out, "screen.css"), "w", encoding="utf-8").write(css_src)
        shutil.copy(os.path.join(HERE, "..", "design", "screen.js"), os.path.join(out, "screen.js"))
        builders = {"home.html": build_home, "work.html": build_work, "finance.html": build_finance,
                    "tools.html": build_tools, "market.html": build_market, "products.html": build_products,
                    "order.html": build_order, "sale.html": build_sale, "more.html": build_more}
        for fname, fn in builders.items():
            open(os.path.join(out, fname), "w", encoding="utf-8").write(fn(d))
            print(f"wrote {d}/{fname}")

if __name__ == "__main__":
    main()
