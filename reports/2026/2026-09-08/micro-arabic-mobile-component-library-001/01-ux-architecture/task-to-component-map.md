# Task-to-Component Map — Real Operations → Components

Agent 01 · Task 2-a · RUN_ID `20260908T133450Z-16d11`. Maps the operational tasks of مخبز أبو محمد (Amman) to the component families that serve them. Personas/counterparties and values follow the shared example bank; all amounts are plausible in the 35.00–1,284.50 `د.أ` range, dates are `DD/MM/YYYY`, today is `08/09/2026` (الثلاثاء). Each task lists: trigger, primary component(s), state considerations, and the number/state shown first.

---

## 1. Record a cash sale (تسجيل بيع نقدي)

- **Trigger:** A customer is at the counter and pays cash; أبو محمد has seconds, one hand free.
- **Primary components:** `QuickActionRail` tile `إضافة بيع` (first tile, brand-tint, rightmost in RTL) → `Sheet` (medium) with `Input` family: customer selection (`اختر العميل` or quick walk-in), `Amount` input (`0.00` placeholder, `د.أ` affix), `Segmented` `نقدي | آجل` defaulting to `نقدي`, `Date` defaulting to `اليوم` → `Button` primary `تسجيل البيع` (48px, brand-ink filled).
- **State considerations:** On save: CTA → loading (`جاري الحفظ…`) → quiet completion (check + `تم`) → sheet exits 180ms. Offline: the entry saves locally (`محفوظ على الجهاز` + `يُرسل عند عودة الاتصال`) and never silently pretends to be synced. Duplicate-risk: conflict state `عملية مشابهة موجودة` with `عرض الموجودة` / `تسجيلها مع ذلك`.
- **Number/state shown first:** The sheet opens with the amount field focused and the segmented control already on `نقدي`; after completion the `MetricRow` `مبيعات اليوم` and the `PrimaryValueBlock` `نقد اليوم` update immediately — no count-up animation.

## 2. Record a receivable collection (تحصيل دين)

- **Trigger:** أبو أحمد stops by and pays part of his old balance in cash.
- **Primary components:** `QuickActionRail` `تحصيل دين` → picker `Sheet` (search `Input` + customer `OperationalRow` list) → collection `Sheet` titled `تحصيل من أبو أحمد` with `MetricRow` `المتبقي — 240.00 د.أ`, `Amount` input with quick-fill chip `240.00`, `Button` `تحصيل`.
- **State considerations:** 20-row customer batch, prefetch near the last 5 rows, 3 skeleton rows while fetching; search empty state `لا نتائج مطابقة` + `مسح البحث`; if the balance cannot load offline, show `—` + `غير متاح حاليًا` — never `0` (a fake zero would make أبو محمد waive a real debt). If the full remaining amount is collected, the new balance is a true zero `0.00 د.أ`, rendered at full weight — an achievement, not an absence.
- **Number/state shown first:** The outstanding balance `240.00 د.أ` (after today's earlier 120.00 payment), before any input.

## 3. Add an expense (إضافة مصروف)

- **Trigger:** Fuel for the delivery scooter, a mixer blade, a paid receipt — money out, right now.
- **Primary components:** `QuickActionRail` `إضافة مصروف` → `Sheet` with `Amount`, `Selection` category (`وقود`، `صيانة`، `إيجار`، `أخرى`), `Date` (`اليوم` default), optional `ملاحظة (اختياري)` text input, `Button` `حفظ`.
- **State considerations:** Expenses are recorded as outflows; in `حركة اليوم` the metric renders `مصروفات اليوم — -92.50 د.أ` with the sign as the primary direction signal in neutral ink-strong (color not required). Validation error wording fixes the input: `أدخل مبلغًا أكبر من صفر`.
- **Number/state shown first:** Empty amount field with `0.00` placeholder (empty input, never committed as zero) and category unset (`اختر الفئة`).

## 4. Purchase from supplier — cash or credit (شراء من مؤسسة الشرق)

- **Trigger:** Flour is low; أبو محمد calls مؤسسة الشرق للتجهيزات and takes delivery of `طحين فاخر 10كغ` bags.
- **Primary components:** Threshold `OperationalRow` tap → full purchase `Sheet` titled `شراء من مؤسسة الشرق للتجهيزات` (supplier prefilled), material and quantity inputs (`أكياس` unit), computed total, `Segmented` `دفع الآن | على الحساب`, `Button` `تسجيل الشراء`. Result: `OperationalRow` `مؤسسة الشرق للتجهيزات — شراء آجل — 06/09/2026 — 350.00 د.أ` style entry.
- **State considerations:** `دفع الآن` reduces `نقد اليوم` and shows the entry as cash-out; `على الحساب` increases `ذمم المورّدين` (the `CompactTile` value) without touching cash — the sheet states the consequence before saving in one 13px line. Stock updates the threshold state (`متبقي 4 أكياس` → new quantity, warning cleared).
- **Number/state shown first:** The prefilled supplier and material with an empty quantity; the computed total appears as a `MetricRow` `الإجمالي — 350.00 د.أ` once quantity is entered (immediate, never animated).

## 5. Follow up a delivery company settlement (تسوية شركة التوصيل السريع)

- **Trigger:** شركة التوصيل السريع owes a settlement from last week's deliveries to مطعم النخيل and hasn't transferred it.
- **Primary components:** Warning `OperationalRow` (`شركة التوصيل السريع — بانتظار التحويل — منذ 05/09/2026 — 142.00 د.أ`) → detail `Sheet` `تسوية شركة التوصيل السريع` with the amount, related orders, and two actions: `Button` `تأكيد الاستلام` (completed) and quiet `إرسال التذكير`.
- **State considerations:** Pending is decision-critical: warning clock icon + word `بانتظار التحويل` + since-date, so urgency is readable without color. If the amount is not yet confirmed by the company, it is unknown — `—` + `قيد التحديد`, never `0`. On confirmation, the row flips inline to completed (check + `تم`) and `نقد اليوم` rises by 142.00; the settlement stays in history as an audit trail.
- **Number/state shown first:** The owed amount `142.00 د.أ` with the pending state and `منذ 05/09/2026`.

## 6. Monitor a material stock threshold (متابعة حد المخزون)

- **Trigger:** Flour bags or paper cups are running low; the owner wants to reorder before the weekend rush.
- **Primary components:** Threshold `OperationalRow` (`طحين فاخر 10كغ — متبقي 4 أكياس — الحد 6`) with warning icon and the colored quantity; detail `Sheet` with a `Chart` sparkline of the last 7 days' usage and a quick `Button` `أضف شراء` leading to the purchase flow. `المخزون` destination in `BottomNavigation` hosts the full list of materials.
- **State considerations:** Warning fires at/below the threshold and is signalled by icon + wording `متبقي 4 أكياس` + the warning-colored number (one of the composition's ≤2 colored numbers) — never color alone. Quantities are not money: no `د.أ`, no sign, but the same unknown/unavailable rules apply (`—` if not counted yet).
- **Number/state shown first:** `متبقي 4 أكياس` with the threshold context `الحد 6`.

## 7. Check a customer balance / receivable (رصيد أبو أحمد)

- **Trigger:** أبو أحمد calls; أبو محمد wants the exact remaining debt before agreeing to anything.
- **Primary components:** `الذمم` destination → search `Input` (`ابحث عن عميل أو عملية`) → customer `OperationalRow` list → detail view: `PrimaryValueBlock` `ذمم أبو أحمد` + `MetricGroup` rows (`آخر دفعة — اليوم 12:40`، `أقدم فاتورة — 24/08/2026`، `مجموع المسدّد — 480.00 د.أ`) + `Button` `تحصيل دفعة`.
- **State considerations:** True zero renders `0.00 د.أ` at full weight (debt cleared); offline renders `—` + `غير متاح حاليًا` + `إعادة المحاولة` (retries stop after the first failure); the aging row may use warning only when the oldest invoice is actually overdue — otherwise neutral.
- **Number/state shown first:** The balance `240.00 د.أ` as the screen's primary value.

## 8. Check supplier payable (مستحقات مؤسسة الشرق)

- **Trigger:** The supplier's driver is at the door; how much do we owe them?
- **Primary components:** `CompactTile` `ذمم المورّدين — 640.00 د.أ — مؤسسة الشرق` in the today view, or `المزيد` → `المورّدون` sheet list → supplier detail with `PrimaryValueBlock` `مستحقات مؤسسة الشرق` + `MetricRow`s (`آخر شراء — 06/09/2026`، `آخر دفعة — 07/09/2026`) + `Button` `تسجيل دفعة`.
- **State considerations:** Payable is a stock value — no sign; direction appears only when a payment is recorded (cash out with `-`). If the supplier's statement hasn't synced, `—` + `غير متاح حاليًا`, never an invented `0`.
- **Number/state shown first:** `640.00 د.أ` payable to مؤسسة الشرق للتجهيزات.

## 9. Review today's cash movement (حركة اليوم)

- **Trigger:** A quiet minute between customers; أبو محمد verifies the day so far.
- **Primary components:** `PrimaryValueBlock` `نقد اليوم — 1,284.50 د.أ — حتى 14:20` + `QuickActionRail` + `MetricGroup` `حركة اليوم` (`مبيعات اليوم 465.00`، `تحصيلات ذمم +210.00`، `مصروفات اليوم -92.50`) — this is exactly the test composition.
- **State considerations:** Loading shows the label + 2 skeleton bars and 3 skeleton rows (never a `0` placeholder); a stale cache adds `آخر تحديث 12:40` rather than pretending freshness; the pending 142.00 settlement is intentionally absent from cash (it is still `بانتظار التحويل`) — consistency between states is the trust mechanism. Below the fold, the `CompactTile` pair shows the receivables/payables position (`1,175.00` vs `640.00`).
- **Number/state shown first:** `نقد اليوم 1,284.50 د.أ` at 32px, then the signed flow rows.

## 10. Resolve an operational exception (failed / pending entry)

- **Trigger:** An entry recorded in the basement (no signal) failed to send, or a duplicate was detected.
- **Primary components:** Exception `OperationalRow` variants inside `متابعة اليوم` (or a dedicated follow-up state): failed — danger chip `فشل الإرسال` + inline quiet `Button` `إعادة المحاولة`; conflict — chip `عملية مشابهة موجودة` → comparison `Sheet` showing both entries side by side with `عرض الموجودة` / `تسجيلها مع ذلك`; pending — warning `بانتظار التحويل`.
- **State considerations:** Automatic retries stop after the first failure (SPEC §6.12) — the retry is always a visible, focusable action; the failed entry remains locally saved (`محفوظ على الجهاز`) so no money record is lost; conflict resolution preserves both candidates until the user decides; resolved rows flip to `تم` inline with a 120ms crossfade and stay in history.
- **Number/state shown first:** The failed amount with the `فشل الإرسال` chip and the retry action in the thumb zone.

## 11. Record a payment to a supplier (تسجيل دفعة)

- **Trigger:** أبو محمد hands the supplier's driver 200.00 in cash against the 640.00 payable.
- **Primary components:** `QuickActionRail` `تسجيل دفعة` → picker sheet (supplier list) → payment `Sheet` `تسجيل دفعة لمؤسسة الشرق للتجهيزات` with `MetricRow` `المستحق — 640.00 د.أ`, `Amount` input + quick-fill chip `640.00`, `Segmented` `نقدي | تحويل`, `Button` `تسجيل الدفعة`.
- **State considerations:** Payment is cash-out: the resulting entry carries `-` (direction by sign) while the supplier's payable drops to `440.00 د.أ`; a transfer payment does not touch `نقد اليوم` but flags the entry `بانتظار التأكيد` until the bank confirms — decision-critical pending, info-tinted only if the composition's semantic budget allows, otherwise neutral chip + wording.
- **Number/state shown first:** `المستحق 640.00 د.أ` above the amount input.

## 12. Review planned-vs-actual sales (المخطط مقابل الفعلي)

- **Trigger:** End of week; did the bakery hit the plan before restocking decisions?
- **Primary components:** `Chart` primitive `planned-vs-actual` (actual solid, planned dashed, direct labels `فعلي` / `مخطط`, LTR time axis) + `Chart` `target meter` `هدف الشهر — 1,950.00 من 3,000.00 (65%)` + `Chart` `trend marker` `+12% عن الأسبوع الماضي` beside the weekly total.
- **State considerations:** Series are distinguishable by line style (solid/dashed), never color alone; the partial window states `بيانات من 24/08/2026`; behind-plan status uses warning fill on the meter plus the status in words; every chart has a full text alternative (`role="img"` + sentence).
- **Number/state shown first:** The direct labels `مخطط 2,000.00` / `فعلي 1,275.00 د.أ` — numbers before shape.

---

### Coverage summary

Every task resolves into the locked families: `QuickActionRail` triggers 7 of 12 tasks; `Sheet` hosts every entry flow; `Button` carries every commit; `OperationalRow` carries identity+state lists; `PrimaryValueBlock` anchors every balance view; `MetricGroup`/`MetricRow` carry secondary numbers; `CompactTile` carries the one comparison pair; `State` family covers empty/loading/error/offline/pending/conflict/failed/completed/cancelled/reversed across all flows; `BottomNavigation` + `TopZone`/`Avatar` provide the shell; `Chart` primitives add depth without becoming first-screen furniture. Gaps found by Agents 02–05 should be logged against this map, not solved with new families.
