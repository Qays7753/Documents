# Content and Data Fixtures

Use these exact fixtures across C1, C2, and C3. Minor punctuation corrections are allowed; meaning, amounts, labels, and hierarchy are fixed.

## Shared project context

- Project: حلويات ليان
- Period: اليوم، 18 أيلول
- Currency format: `185.00 د.أ`
- Numbers: Latin digits with tabular alignment.
- Direction: Arabic RTL; isolate numeric runs.

## Fixture A — Complete positive result

### Business Status Hero

- Label: وضع مشروعك اليوم
- State: نتيجة موجبة
- Result: `+42.50 د.أ`
- Explanation: بعد تسجيل المبيعات والمصاريف والتكاليف
- Sales: `185.00 د.أ`
- Cash recorded: `136.00 د.أ`
- Due from customers: `49.00 د.أ`
- Due to suppliers: `22.00 د.أ`

### Micro Signal

- Status: عندك مبلغ يحتاج تحصيلًا
- Reason: أم محمد عليها `25.00 د.أ` منذ 3 أيام
- Action: حصّل المبلغ

### Recent activity

1. بيع — صينية كنافة — `25.00 د.أ` — منذ 12 دقيقة
2. مصروف — مواد تغليف — `8.50 د.أ` — منذ ساعة
3. تحصيل — أم محمد — `15.00 د.أ` — أمس

## Fixture B — Incomplete result

### Business Status Hero

- Label: نتيجة مشروعك
- State: النتيجة غير مكتملة
- Supporting value: مبيعات اليوم `120.00 د.أ`
- Reason: عمليتا بيع تحتاجان تسجيل التكلفة
- Completion: 8 من 10 عمليات مكتملة التكلفة
- Action: أكمل التكلفة

### Supporting figures

- Cash recorded: `92.00 د.أ`
- Due from customers: `28.00 د.أ`
- Due to suppliers: `15.50 د.أ`

## Fixture C — Complete negative result

### Business Status Hero

- Label: نتيجة مشروعك اليوم
- State: نتيجة سالبة
- Result: `−18.75 د.أ`
- Reason: تكلفة المواد أعلى من المعتاد هذا اليوم
- Sales: `90.00 د.أ`
- Expenses and costs: `108.75 د.أ`
- Action: راجع التكاليف

Do not use accusatory copy such as “مشروعك يخسر”.

## Fixture D — Delayed order

- Customer: سارة الخطيب
- Order: ضيافة مناسبة — 40 قطعة
- Agreed amount: `75.00 د.أ`
- Paid deposit: `25.00 د.أ`
- Remaining: `50.00 د.أ`
- Delivery date: 17/09/2026
- State: متأخر يومًا واحدًا
- Current stage: تنفيذ
- Primary action: حدّث حالة الطلب
- Secondary action: شارك تحديثًا مع الزبونة

## Fixture E — Quick Action Bar

- بيع
- مصروف
- طلب
- تحصيل
- المزيد

Each action uses icon plus visible label. Order remains stable across directions.

## Fixture F — Record a sale

- Title: سجّل بيعًا
- Amount label: مبلغ البيع
- Amount: `25.00`
- Payment state: مدفوع كاملًا
- Customer: أم محمد
- Destination: درج المحل
- Date: 18/09/2026
- Impact preview title: شو رح يصير؟
- Impact preview: رح تزيد المبيعات `25.00 د.أ`، وينضاف المبلغ إلى درج المحل.
- Primary button: سجّل البيع
- Secondary action: إلغاء

## Fixture G — Successful sale

- Status: تم تسجيل البيع
- Amount: `25.00 د.أ`
- Destination: أُضيف المبلغ إلى درج المحل
- Updated figure: الكاش المسجل الآن `161.00 د.أ`
- Human reference: عملية #142
- Primary action: عرض العملية
- Optional recovery: تراجع

Success must visually connect the saved operation to the updated cash or sales figure.

## Fixture H — Empty state

- Title: لسه ما عندك مبيعات اليوم
- Description: سجّل أول بيع حتى يبدأ Micro بعرض وضع مشروعك.
- Action: سجّل بيعًا
- Supporting reassurance: المجهول لا يتحول إلى صفر.

## Fixture I — Validation error

- Field: مبلغ البيع
- Invalid value: `0`
- Message: المبلغ لازم يكون أكبر من صفر — اكتب قيمة البيع الفعلية.
- Preserve entered context and focus the field.

## Fixture J — System error

- Title: ما انحفظت العملية
- Description: ما تغيّر أي رقم. جرّب مرة ثانية، ومدخلاتك ما زالت موجودة.
- Primary action: حاول مرة ثانية
- Secondary action: ارجع للنموذج

## Language rules

- Use plain Arabic with selective familiar Jordanian phrasing.
- Use “نتيجة” until completeness permits “ربح”.
- Use “لي عند العملاء” and “عليّ للموردين”.
- Use “الكاش” where it matches the product voice; do not introduce accounting jargon.
- Do not introduce untranslated UI English such as `Order ID`, `FAIL`, or `agreement recorded locally`.
- Dates use one consistent `DD/MM/YYYY` presentation in operational records.

