#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Micro Bold Modular — Agent 03
Fixed fixtures from 04-CONTENT-AND-DATA-FIXTURES.md (verbatim).
ALL screen content across C1/C2/C3 is generated from this single source
=> fair comparison + fixture integrity by construction.
"""

CURRENCY = "د.أ"
PROJECT = {"name": "حلويات ليان", "period": "اليوم، 18 أيلول"}

# ---- Fixture A — complete positive ----
A = {
    "hero_label": "وضع مشروعك اليوم",
    "hero_state": "نتيجة موجبة",
    "hero_result": "+42.50",
    "hero_explain": "بعد تسجيل المبيعات والمصاريف والتكاليف",
    "sales": "185.00",
    "cash": "136.00",
    "due_from": "49.00",
    "due_to": "22.00",
    "signal": {
        "status": "عندك مبلغ يحتاج تحصيلًا",
        "reason": "أم محمد عليها <bdi dir=\"ltr\">25.00</bdi> " + CURRENCY + " منذ 3 أيام",
        "action": "حصّل المبلغ",
    },
    "recent": [
        ("بيع", "صينية كنافة", "25.00", "منذ 12 دقيقة", ""),
        ("مصروف", "مواد تغليف", "8.50", "منذ ساعة", ""),
        ("تحصيل", "أم محمد", "15.00", "أمس", ""),
    ],
}

# ---- Fixture B — incomplete result ----
B = {
    "hero_label": "نتيجة مشروعك",
    "hero_state": "النتيجة غير مكتملة",
    "reason": "عمليتا بيع تحتاجان تسجيل التكلفة",
    "completion_done": 8, "completion_total": 10,
    "supporting": "مبيعات اليوم",
    "supporting_value": "120.00",
    "action": "أكمل التكلفة",
    "cash": "92.00",
    "due_from": "28.00",
    "due_to": "15.50",
    # composed demo content (D-010) — same across directions
    "signal": {
        "status": "طلب متأخر يحتاج انتباهك",
        "reason": "سارة الخطيب — ضيافة مناسبة — تجاوز موعد التسليم يومًا",
        "action": "حدّث حالة الطلب",
    },
    "recent": [
        ("بيع", "صينية كنافة", "25.00", "منذ 12 دقيقة", "ناقصة التكلفة"),
        ("مصروف", "مواد تغليف", "8.50", "منذ ساعة", ""),
        ("تحصيل", "أم محمد", "15.00", "أمس", ""),
    ],
}

# ---- Fixture C — complete negative ----
C = {
    "hero_label": "نتيجة مشروعك اليوم",
    "hero_state": "نتيجة سالبة",
    "hero_result": "−18.75",
    "reason": "تكلفة المواد أعلى من المعتاد هذا اليوم",
    "sales": "90.00",
    "expenses": "108.75",
    "action": "راجع التكاليف",
    # composed demo content (D-010) — same across directions
    "cash": "70.00",
    "due_from": "20.00",
    "due_to": "18.00",
    "completion_done": 7, "completion_total": 10,
    "signal": {
        "status": "طلب متأخر يحتاج انتباهك",
        "reason": "سارة الخطيب — ضيافة مناسبة — تجاوز موعد التسليم يومًا",
        "action": "حدّث حالة الطلب",
    },
    "recent": [
        ("بيع", "صينية كنافة", "25.00", "منذ 12 دقيقة", ""),
        ("مصروف", "مواد ومستلزمات", "65.00", "منذ ساعة", ""),
        ("مصروف", "مواد تغليف", "8.50", "منذ 3 ساعات", ""),
    ],
}

# ---- Fixture D — delayed order ----
D = {
    "customer": "سارة الخطيب",
    "order": "ضيافة مناسبة — 40 قطعة",
    "agreed": "75.00",
    "deposit": "25.00",
    "remaining": "50.00",
    "delivery_date": "17/09/2026",
    "state": "متأخر يومًا واحدًا",
    "stage": "تنفيذ",
    "primary": "حدّث حالة الطلب",
    "secondary": "شارك تحديثًا مع الزبونة",
    "stages": ["اتفاق", "تنفيذ", "جاهز", "تم التسليم"],
}

# ---- Fixture E — Quick Action Bar ----
QAB = ["بيع", "مصروف", "طلب", "تحصيل", "المزيد"]

# ---- Fixture F — record a sale ----
F = {
    "title": "سجّل بيعًا",
    "amount_label": "مبلغ البيع",
    "amount": "25.00",
    "payment": "مدفوع كاملًا",
    "customer": "أم محمد",
    "destination": "درج المحل",
    "date": "18/09/2026",
    "preview_title": "شو رح يصير؟",
    "preview": "رح تزيد المبيعات <bdi class=\"preview-amount\" dir=\"ltr\">25.00</bdi> " + CURRENCY + "، وينضاف المبلغ إلى درج المحل.",
    "primary": "سجّل البيع",
    "secondary": "إلغاء",
}

# ---- Fixture G — successful sale ----
G = {
    "status": "تم تسجيل البيع",
    "amount": "25.00",
    "destination": "أُضيف المبلغ إلى درج المحل",
    "updated_label": "الكاش المسجل الآن",
    "updated_value": "161.00",
    "reference": "عملية #142",
    "primary": "عرض العملية",
    "recovery": "تراجع",
}

# ---- Fixture H — empty state ----
H = {
    "title": "لسه ما عندك مبيعات اليوم",
    "description": "سجّل أول بيع حتى يبدأ Micro بعرض وضع مشروعك.",
    "action": "سجّل بيعًا",
    "reassurance": "المجهول لا يتحول إلى صفر.",
}

# ---- Fixture I — validation error ----
I = {
    "field": "مبلغ البيع",
    "value": "0",
    "message": "المبلغ لازم يكون أكبر من صفر — اكتب قيمة البيع الفعلية.",
}

# ---- Fixture J — system error ----
J = {
    "title": "ما انحفظت العملية",
    "description": "ما تغيّر أي رقم. جرّب مرة ثانية، ومدخلاتك ما زالت موجودة.",
    "primary": "حاول مرة ثانية",
    "secondary": "ارجع للنموذج",
}

# ---- Order-state model (file 03) ----
ORDER_STAGES = ["اتفاق", "تنفيذ", "جاهز", "تم التسليم"]

# ---- Composed demo content (documented as D-010, identical across directions) ----
COMPOSED = {
    "work_orders": [
        {"customer": "سارة الخطيب", "item": "ضيافة مناسبة — 40 قطعة", "stage": "تنفيذ", "late": True, "amount": "75.00"},
        {"customer": "مقهى الحارة", "item": "تشكيل حلويات أسبوعي", "stage": "اتفاق", "late": False, "amount": "60.00"},
    ],
    "work_ready": [
        {"customer": "أم محمد", "item": "صينية كنافة", "stage": "جاهز", "amount": "25.00"},
    ],
    "work_upcoming": [
        {"label": "تسليم — تشكيل حلويات أسبوعي", "who": "مقهى الحارة", "when": "19/09/2026"},
        {"label": "تحصيل — دفعة متبقية", "who": "سارة الخطيب", "when": "18/09/2026"},
    ],
    "work_completed": [
        {"label": "تم التسليم — صينية كنافة", "who": "أم محمد", "when": "أمس"},
    ],
    "finance_insight": "عندك مبلغ يحتاج تحصيلًا — أم محمد عليها 25.00 د.أ منذ 3 أيام",
    "products": [
        {"name": "صينية كنافة", "type": "منتج", "price": "25.00"},
        {"name": "كعكة مناسبات", "type": "منتج", "price": "35.00"},
        {"name": "تشكيل ضيافة", "type": "خدمة", "price": "حسب الطلب"},
    ],
    "menu": [
        ("الحساب", "ليان — حلويات ليان", "account"),
        ("بيانات المشروع", "الاسم، العملة، الفترة", "project"),
        ("الإعدادات", "اللغة، الوضع الليلي، التنبيهات", "settings"),
        ("الحماية", "رمز الحماية (PIN)، الخصوصية", "protection"),
        ("بياناتي", "نسخة احتياطية — آخر نسخة: أمس", "data"),
    ],
}

MORE_SHEET = [
    ("سجل العمليات", "كل عمليات مشروعك", "finance"),
    ("منتجاتي وخدماتي", "قائمتك المرجعية", "products"),
    ("العملاء والتحصيل", "من عليه مبلغ لك", "finance"),
    ("الموردون والمشتريات", "ما عليك للموردين", "finance"),
]
