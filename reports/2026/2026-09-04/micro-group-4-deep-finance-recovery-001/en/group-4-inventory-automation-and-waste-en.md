# Group 4 Contracts — Delivery-Linked Inventory Automation and Waste

Micro deep-finance extension, contract 29 (عقد ٢٩) on top of the Group 3 delivery transaction (contract D4). Baseline `main @ 67d4e41` → final `main @ 05669a9`.

## 1. The automation contract

Automatic deduction may occur only after configured conditions and is **one deterministic atomic operation** — never a hidden side effect:

- **Opening the delivery review page saves nothing.** `buildReview` reads orders, materials, movements, and templates; it computes a declaration only. The G3 delivery dom test asserts zero inventory movements after opening the review and using the calculator.
- **Saving a draft or creating an estimate deducts nothing** (separate stores; the calculator-suggestion test asserts the movement list is unchanged).
- **The single confirmed delivery commit is the only writer.** `commitDelivery` validates (delivered-reuse guard, per-material duplicate-row rejection, untracked-must-skip rejection, quantity > 0, price change requires a reason, collect ≤ receivable) and then writes exclusively through `commitOrderDelivery` — one IndexedDB readwrite transaction over five stores (order, consumption movements, shortage rows, cash allocation, wallets) — all-or-nothing, mirrored exactly in Memory.
- **The template flag is a declaration, not a trigger.** `autoConsumeOnDelivery` (catalog template, true-only normalization) surfaces as an explicit banner: «خصم تلقائي مفعّل لهذا المنتج: الاقتراحات جاهزة ضمن تأكيد التسليم الواحد — بلا خطوة إضافية وبلا أثر عند فتح الصفحة». Tracked rows always show per-row quantity and decision controls; the owner can adjust or skip each row before the one confirmation. This is a documented conscious design (reviewed by 4-c/4-d): the flag does not differentiate row defaults because the movements must remain inside the single explicit confirmation.

## 2. Idempotency — three layers

1. Service guard: a delivered/settled order returns honest reuse instead of a second commit.
2. Deterministic keys: the consumption movement operation key is `${orderId}:deliver:${deliveryEvent.id}:${materialId}` where the delivery event id is itself deterministic (`${orderId}:${deliverKey}`); re-delivery after a reversal gets attempt-suffixed keys, so every attempt has its own key space.
3. Store-level: the last-delivery-key comparison plus operation-key dedupe inside both stores mean a retry (double tap, reload after interruption) either reuses honestly or completes only the missing deterministic keys — never a duplicate movement.

## 3. Shortage and negative policy

Shortage is explicit and never silently negative: when requested > available, the suggested action becomes «استهلاك المتاح + توثيق النقص» or «نقص فقط»; a shortage row is written to its own store (requested − available = shortage invariant); `assertInventoryRemainsNonNegative` guards every write; the live per-row warning «المادة X: المطلوب أكبر من المتاح — سيُسجَّل النقص صراحةً ولا يصير الرصيد سالبًا» shows before confirmation. Partial/adjusted consumption is supported (per-row editable quantity, capped by availability with Math.min).

## 4. Untracked components

Catalog template components that are not linked to a tracked material are shown as «غير متتبَّعة — مرجع تكلفة فقط، لا حركة كمية»; their suggested action is `skip` and the service rejects any non-skip action for them — untracked components never produce quantity movements.

## 5. Reversal

Reversing a delivery is a documented correction: each unreversed delivery consumption movement is mirrored by a reversal movement (`${operationKey}:reversal`, `reversesMovementId`, negated quantity and value, carried cost knowledge, mandatory reason); double reversal is refused; collected cash is untouched (reversing a collection has its own path); the order moves to «يحتاج مراجعة» with the resume-or-cancel decision explicit. MIC-13 (rewritten in this session) now genuinely enforces the linkage: extraction of the delivery-event id between the deterministic prefix and the last colon (handling colon-bearing event ids — the original implementation extracted the order id and never matched), consumption-only + exact-prefix scoping (cash movements `${orderId}:deliver-cash:` excluded), and the mirror check for reversed deliveries actually enforced. Two negative tests prove it catches a ghost link and a missing mirror.

## 6. Waste and write-off — separate meanings preserved

Waste (Group 2 contract 28) remains a material-level movement: linked to material and source, non-cash in itself, `wasteContext` kinds, derived period read (`readPeriodWaste`: unreversed, occurredOn window, unknown-cost flag), no duplicate operating expense, reversible by mirror. Asset write-off (Group 4) is a separate event-based book loss of a long-use asset's remaining value — `asset_writeoff` with `operatingExpenseDeltaMinor = 0`. The delta table gives **all nine new event types a zero operating-expense delta**, so no deep-finance path can double-count an operating expense; any double-entry-like presentation is a linked, auditable, reversible derived read model (the canonical period reader), never a silent second ledger.

## 7. Test evidence

G3Delivery dom suite (3) re-run green on the Group 4 head — the automation behavior is unchanged by Group 4 (the review's explicit regression condition). G4 delivery-linked surfaces: preview before confirm, repeated attempt without duplicate movement (deterministic keys + store dedupe), untracked without movement, shortage and controlled policy, delivery-linked reversal (dom + service). MIC-13 negative fixtures (2). Inventory domain guards (value-zero ⇔ unknown cost, consumption requires order/sale/reason, reversal requires original reference) unchanged and covered by the Group 2 suites included in the 717-test prototype run.
