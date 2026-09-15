# Group 3 — Sale/Deposit/Settlement Contracts (English)

## 1. Revenue recognition — exactly once
- Order revenue is recognized ONLY at the delivered transition (`recognizedRevenueMinor = agreedPriceMinor`), re-affirmed by `price_revised` if the price changes. Retry, double-tap, reload, and collect-at-delivery never create a second recognition (service tests assert 6,000 revenue with deposit + collection, not 7,000).
- Direct sale: one record per intent (unique idempotencyKey index on the direct-sales store); revenue, collection status, and optional cost live on the sale; corrections via documented revisions (edit/cancel/price-cut) preserving before-values.

## 2. Deposit truth (عربون)
- A deposit is a collection against a future sale — part of `collectedMinor`, never auto-profit. Recognized revenue stays 0 on cancelled orders regardless of retained deposits.
- On cancellation: `depositSettlement = "needs_review"` (visible pending decision in the deposit overview), resolved ONLY by explicit refund (`cancelled_refunded`) or retain (`cancelled_retained`) with mandatory reason. Retained amounts stay visible pending decisions — never silently classified as revenue, owner money, or Amanah.
- Applied at settlement: deposit is part of collected; receivable = price − collected. No second revenue, no double count.

## 3. Settlement without a second sale
- `collectRemaining` (delivered orders) and `collectRegisteredDebt` (registered debt) write cash + remainder only. Registering debt (`registerDebt`) settles the order with an explicit debt status; collecting it later never reopens the order and never creates revenue.
- All collection surfaces from orders route through the CollectionService/Collect sheet pattern: one documented collection + optional wallet attribution via `distributeUnallocated` (sourceRefKind "order", sourceRefLineId = the collection event), or the delivery-time atomic allocation entry (sourceRefLineId = the delivery event).

## 4. Cash/receivable separation
- Cash enters `registeredCollectionsMinor` → unallocated pool → optional wallet allocation. Receivables are tracked as order remainder / registered debt / direct-sale outstanding (each visible in its source of truth). Amanah, owner money, payables — untouched by these paths (integrity check MIC suite covers the invariants).

## 5. Delivery reversal economics
- Neutralizes recognized revenue/cost to honest unknown (0 + `review_required`, not fake zeros — the order visibly needs review); mirrors every delivery-linked consumption movement (inventory returns); collected cash untouched (explicit in the UI preview: "عكس قبضة له مساره الخاص"); re-delivery after re-execution is a NEW documented delivery (new attempt-suffixed keys; net effect = one live delivery's revenue).
- Period truth: reversed orders drop out of `finals` (resultStatus ≠ final) so revenue/COGS exclude them; movements are mirrored so positions return; original events preserved for audit.

## 6. Double-counting risks reviewed and closed (SA-3/SA-5)
- Deposit counted twice → impossible (single collectedMinor path; tests).
- Settlement creating a second sale → impossible (collection paths touch cash/remainder only).
- Retry duplicating revenue/collection/movements → deterministic keys + store-level reuse detection + eventExists guards (service + IDB tests).
- Changed product cost rewriting a historical order → frozen snapshots (domain test).
- Stock deduction without evidence/confirmation → consumption only through explicit delivery confirmation or explicit manual/sale-linked paths.
- Hidden negative stock → shortage rows with per-row preview (D-027).

## 7. Known limitations (documented, not silent)
- Agreement-time deposit collection has no wallet destination (money lands in unallocated — honest, allocatable later).
- Sale-linked consumption does not feed period COGS this group (positions truthful; order-linked COGS unchanged).
