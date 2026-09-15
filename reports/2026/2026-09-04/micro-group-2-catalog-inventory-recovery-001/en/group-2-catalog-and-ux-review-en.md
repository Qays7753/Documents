# Group 2 Catalog and UX Review — Material Identity, Guided Journeys, RTL Mobile Behavior, and State Coverage

**Delivery:** micro-group-2-catalog-inventory-recovery-001 · **Date:** 2026-09-04
**Sources:** SA-2 Zman journey analysis (read-only, `zman-app` @ `bdd63ab`), SA-4 Arabic RTL mobile UX review of the Group 2 design contract, the final surfaces merged at Micro `1207a5a`, and live browser QA at 390×844 RTL (0 console errors).

This report records how Group 2's surfaces behave for their owner on a 360–390px one-handed phone: the guided questions asked, the effect previews shown before any save, every required state, the Arabic copy decisions (with the Jordanian-friendly register), the density ledger, and the Zman behaviors that were deliberately reshaped.

---

## 1. Material identity — one question at a time

The Zman catalog form merges identity, tracking, and cost into one screen. Micro keeps the reference catalog separate (contract 15) and moves the inventory identity into a full-screen guided editor (`MaterialEditor`) whose first decision is the tracking question:

```
شو هذه المادة؟ (اسم + وحدة)
→ بدك تتابع كميات هذه المادة؟
   «أيوه، تابع الكمية — يُسجَّل الرصيد، ويُخصم منه عند الاستهلاك والهدر.»
   «لا، للتكلفة فقط — بلا رصيد ولا عدّ.»
→ هل عندك رصيد حالي؟
   «نعم، معلوم — أدخل الكمية الآن.» / «غير محدد بعد» / «صفر مؤكد»
→ التكلفة معروفة ولا تقديرية؟
   «نعم، معلومة» / «لا، غير معروفة بعد — تُسجَّل قيمة صفرية موسومة "غير معروفة" — لا مجانية مفترضة.»
→ التاريخ + «كيف عرفته؟» (gated to confirmed branches)
→ مراجعة الأثر → حفظ
```

UX-law compliance baked into the merged code: the save label is dynamic per branch (no «رصيد البداية» promise on paths that write no movement); date and source fields appear only on confirmed branches; the effect preview is a fixed-min-height block (anti-jitter, Group 1 law) that states the unknown («غير محدد بعد») instead of a confident zero; the untracked path shows a short explanation card («بلا رصيد ولا حركة مخزون») and never asks for a quantity. A later confirmation of an unconfirmed opening uses the deep route `/inventory/material/:id/confirm` — a full editor leg, not a dialog, so the keyboard never fights a modal.

## 2. InventoryMaterials — sections, states, and quiet actions

The surface splits into «مواد متتبَّعة» and «مواد غير متتبَّعة — للتكلفة فقط» (untracked rows: unit, movement count, «بلا رصيد متبع», «فعّل المتابعة»). Tracked rows carry the honest knowledge states: quantity with unit («60 متر»), «غير محدد بعد» with a dash and «أكّد الرصيد», «صفر مؤكد» (keyed to the declared opening, not to the live fold), position cost («التكلفة غير معروفة» / partial / money), and «نقص مفتوح: N» with a collapsed disclosure listing shortage records (requested quantity, note, date via `LocalDateValue`, resolve action «سجّل الحل» with note + date; resolved rows show «حُلّ» and stay visible). Row-level actions: «أخرِج المتبقي» (Decision 20) and «أوقف المتابعة» (consequences dialog). The history section «سجل لا يحذف بصمت» lists movements with dates and notes and marks reversed rows «مرتدة موثقًا» (fixing the pre-existing defect where «تراجع» rendered on already-reversed rows — now hidden on reversed movements).

Movement quick-actions sit in the page header: «استلام شراء» / «استهلاك أو استلام نقص» / «هدر أو ضبط» — all one-handed reachable, each opening the full-screen movement editor.

## 3. The purchase → receipt bridge as an owner journey

On the purchase detail (edit mode), after the truth copy about cost-vs-expense, the received card appears before payments: live «قيمة مستلمة: X من Y د.أ · كمية مستلمة: A من B بوحدة المادة», a disclosure of registered receipt movements, and the CTA «استلم المواد في المخزون» (23 chars — within the 24-char button cap; the SA-4 shortening was adopted over the prompt's longer wording). Fully-received purchases show «استُلمت قيمة هذا الشراء كاملة.» and no CTA. The CTA deep-links to the receipt editor with a safe `from` return; the editor prefills remaining quantity/value once per purchase and never over owner edits, and shows the same received/remaining card so the owner confirms against the truth. Live browser evidence: creating a 20.00 JOD / 50 m purchase, receiving 30 m / 12.00 JOD, and returning to the card reading exactly «12.00 من 20.00 · 30 من 50».

## 4. Movement editor — questions before consequences

The movement editor asks in order: which material (tracked-only list — SA-3 R5; the purchase editor keeps all materials with the honest untracked hint), the consume-target question («لطلب محدد أم لعمل المشروع؟») with reason field on the project path, the cost question on receipt/adjust-increase (recordable unknown), and only then quantity, date, and note. The shortage alternative panel is the **last** block above the sticky save (typing-jitter law): a live one-line warning under the quantity field («الكمية المطلوبة أكبر من المتاحة») grows into the panel offering «استهلك المتاح» + «سجّل نقصًا بدل الاستهلاك» — never a promise that negative balance is allowed. Every mode ends with a fixed-height effect preview stating the exact quantity, value/knowledge, cash implication («بلا خروج نقد جديد» for waste), source, and resulting state, directly above the sticky save.

## 5. Estimate suggestions (Scenario G) — a touch before the keyboard

`MaterialSheet` (the add-material sheet in the cost editor) shows suggestion chips at the top of the sheet body, before any field: name + unit price from the last non-reversed receipt (money via `MoneyValue` bdi), max 6 chips, no `autoFocus` when suggestions exist — one tap fills name/unit/price/confidence (مؤكد from a receipt, تقديري otherwise) before the keyboard ever opens. Copy: «مقترحات من موادك — السعر من آخر استلام». The dom test drives the real CostEditor and proves the tap writes nothing: inventory movements and financial events unchanged.

## 6. Finance period waste row

In the period view, beside the period cost list, the row «هدر مخزون هذه الفترة» renders only when waste exists in the period, shows the known value («2.50») or «قيمة الهدر غير معروفة بعد», and always carries «— غير نقدي: لا يخرج كاش ولا يدخل نتيجة الفترة.». Word order fixed per SA-4 («لا يخرج كاش», not «لا كاش يخرج»). The all-time neighbor row is relabeled «هدر مخزون (منذ البداية)» so the two windows read honestly.

## 7. State coverage (the seventeen required states)

| State | Where it lives |
|---|---|
| Empty catalog | InventoryMaterials empty sections + first-run activation card |
| Untracked material | cost-only section, «بلا رصيد متبع», purchase hint |
| Tracked material | position row + quick actions |
| Activation | page activation card «تفعيل بتاريخ اليوم» (live evidence 01) |
| Unknown opening quantity | «غير محدد بعد» + «أكّد الرصيد» |
| Confirmed zero | «صفر مؤكد» |
| Pending/partial receipt | received card remaining + prefill once |
| Available stock | position with unit |
| Shortage | «نقص مفتوح: N» + disclosure + resolve |
| Unknown cost | «التكلفة غير معروفة» / marked-zero preview |
| Loading | route-level loading states |
| Validation failure | field errors + honest service messages |
| Offline | local-first reads/writes (PWA); reload preserves state |
| Save success | navigation back to source with `from` |
| Save failure | error surfaces without partial writes (atomic) |
| Correction | reversal editors + «مرتدة موثقًا» |
| Archive/reactivation | untrack dialog + «فعّل المتابعة» |

Formatting laws hold everywhere: English digits, `DD/MM/YYYY`, JOD two decimals (inputs and displays), `MoneyValue`/`QuantityValue` bdi isolation for numbers inside Arabic text, `LocalDateValue` for all dates (including shortage resolution — SA-5's raw-ISO fix, verified). No horizontal overflow, keyboard obstruction, bottom-nav collision, unsafe-area overlap, or broken RTL alignment in the live 390×844 run; the five-seat shell and centered FAB are untouched in every screenshot.

## 8. Arabic copy audit (selected verdicts)

- Question register stays colloquial («بدك تتابع كميتها؟», «استلمتها فعلًا ولا لسه؟»); effect/truth copy stays MSA.
- «أيوه، تابع الكمية» — the misspelled standalone «أي» was corrected before merge.
- No accounting jargon in owner labels: «متتبَّعة/غير متتبَّعة» instead of tracked, «الكمية غير معروفة» instead of unknown-quantity, «سجّل الحل» instead of «حُلّ» as a button, «بيان الاستهلاك» for the reason field.
- The untrack dialog's fourth consequence line was truth-corrected to «"غير محدد بعد" حتى تؤكده من جديد» (rejecting Zman's over-promise).
- «صفر مؤكد» is a declared state, never a computed zero.

## 9. Density ledger (measured and locked)

| Surface | At-rest strings | Cap |
|---|---|---|
| MaterialEditor | 39 | 39 |
| InventoryMovementEditor | 54 | 54 |
| SupplierPurchaseEditor | 62 | 62 |
| InventoryMaterials | 56 | 56 |
| Finance | 182 | 182 |
| CostEditor | 58 | 58 |
| ToolsIntegrity | 34 | 34 |

New PAGES entries were added for the previously unmeasured deep editors; the `wasteSummary` variable-name collision with the density counter's "Summary" keeper heuristic was fixed by renaming to `periodWaste`/`readPeriodWaste` (Finance counts honestly at 182 — matching SA-4's prediction exactly).

## 10. Zman UX behaviors — transferred, reshaped, or rejected

**Transferred:** question-order journeys; per-item tracking decision; opening-stock-on-activation; movement history visibility; zero-cost honesty (as explicit unknown state); low-stock visibility (as shortage disclosure); one-tap estimate suggestions.

**Reshaped:** purchase flow (Zman stocks-in immediately with a preview; Micro splits purchase (cash) from receipt (stock) with a prefilled bridge — TR-07); waste (Zman writes an expense row; Micro's is non-cash with a period row); untrack (Zman soft-deletes movements; Micro preserves history with stated consequences).

**Rejected (with reasons):** negative-stock-at-delivery banner («سيُسمح برصيد سالب») — replaced by the shortage policy; untrack copy promising balance restoration; silent untracked skip in delivery (Micro's movement forms simply don't list untracked materials, with the honest hint where they do appear); integer-only quantities (Micro keeps milli-precision).

## 11. Live QA verdict

The 12-screenshot run (supporting folder) walks setup → activation → guided creation → purchase → bridge → partial receipt → position → waste → Finance row → integrity. Zero console errors, zero page errors, correct RTL rendering with isolated LTR numerals, and the five-seat bottom nav intact throughout. The verdict from the browser matches the verdict from the test suite: the surfaces do what their copy promises, and nothing else.
