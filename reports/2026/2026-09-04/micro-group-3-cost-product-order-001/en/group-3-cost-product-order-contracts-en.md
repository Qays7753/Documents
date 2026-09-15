# Group 3 — Cost/Product/Order Contracts (English)

## A. Cost calculator and order cost (§5.1–§5.3)
- **Free exploration**: `/tools/calculator` remains a zero-effect thinking tool (no order, no draft, no inventory movement, no cash event — enforced by dom tests asserting empty stores after save).
- **Saved reference**: CostEstimate (own store) — re-computed on open to verify stability; deleting is always allowed (a thinking tool, not a financial record).
- **Order-specific snapshot**: `CostSnapshot` frozen (deep-frozen input; append-only `costSnapshots[]` history; revision forces needs_review; forbidden post-delivery). Later catalog/material cost edits never rewrite historical snapshots — domain test asserts frozen values under external mutation.
- **Identity link**: `MaterialCostItem.materialId?: string | null` — carries the inventory material identity INTO the snapshot while VALUES stay as entered (identity for delivery consumption proposals; never a live price).
- **Knowledge honesty**: estimate shows known/estimated/unknown/excluded components; excluded = named-but-unpriced items listed explicitly ("غير محدد بعد" not zero); suggestion confidence from last non-reversed receipt (`known`) vs name-only (`estimated`).

## B. Product/service definition (§5.2)
- `CatalogItem` kinds product/service + `CatalogTemplate` (one active, revision chain):
  - `components[]`: id, name, quantityMilli, unitId, note, **materialId (optional)** — material link validated to exist (service); tracked/untracked derived live and displayed honestly; absent = free input.
  - `extras`: timeMinutes|null, hourlyRateMinor|null, packagingMinor, deliveryMinor, wasteMinor, safetyBufferMinor — mirrors CostSnapshotInput optional costs 1:1 so template→snapshot flows map without translation.
  - Classification per §5.2: tracked material / untracked material (cost-only) / free-manual input / labor (extras time) / packaging / delivery / waste / safety margin (extras fields).
  - Templates remain zero-effect planning references ("لم يتغير المخزون أو السعر").
- No second catalog/unit model — Group 2's catalog, measurement units, and material contracts reused.

## C. Order lifecycle (§5.4–§5.5)
- States (unchanged): draft → provisional_agreement → confirmed → in_progress → ready → delivered → settled (+ postponed/needs_review/cancelled). Draft/agreement/confirmed/preparing create NO revenue and NO inventory consumption (revenue recognized only at delivered; consumption only via explicit delivery confirmation).
- Order creation asks minimum first (name, customer, price, quantity, minimal cost snapshot allowed — knowledge "incomplete" is honest), details progressive.
- **Delivery completion contract (§5.7–§5.8)**: one intent = one delivery; atomic (`commitOrderDelivery`); idempotent (attempt-suffixed keys `${id}:deliver`, `${id}:deliver-price-N`, `${id}:deliver-collect-N`, `${id}:deliver-consumed-N`; movement keys `${id}:deliver:${deliveryEventId}:${materialId}`); double-tap/reload/retry safe (eventExists + store-level last-delivery-key reuse detection + operation-key filtering).
- Visible completion states: not-yet-completed / completed / partially settled / fully settled / corrected (status + settlementStatus + events timeline).

## D. Deposits and settlement (§5.9–§5.10)
- Deposit states all supported: received, remaining, additional collection, refund (explicit), applied within collected at settlement, cancelled→needs_review (visible pending decision), retained (explicit decision, never auto-revenue).
- Settlement never creates a second sale: collection paths (`collectRemaining`, `collectRegisteredDebt`, Collect sheet) write cash/remainder only — revenue was recognized once at delivery.
- Price/cost review at delivery: agreed vs final price delta (mandatory reason, `price_revised` event preserves from/to), snapshot cost + knowledge state, deposit/collected/remaining — all in the review surface before confirmation.

## E. Inventory integration (§5.11)
- Group 2 contracts reused exclusively: consumption requires orderId OR saleId OR reason; shortage = structured row (D-027) never negative balance; reversal movements mirror quantity/value/costKnowledge.
- Delivery consumption proposal: only tracked linked materials; per-row action/quantity editable; untracked/free never move; no deduction for estimates or drafts.
- Direct-sale linkage: optional `?sale=` deep link; active sales only; movement carries `saleId` (pattern of purchaseId/orderId).

## F. Cancellation, correction, reversal (§5.12)
- Cancel draft/confirmed/post-deposit: existing `cancelOrder` (deposit → needs_review + explicit refund/retain).
- Cancel after delivery: delivery reversal (documented correction) → needs_review → resume OR cancel.
- Correcting price: `reviseAgreedPrice` (from/to preserved; reopens remainder; debt-aware settlement derivation).
- Correcting collected amount: `reverseOrderCollection` (+ compound wallet-allocation reversal).
- Correcting inventory movement: Group 2 reversal contract; delivery reversals auto-mirror all delivery-linked consumption.
- Reversing a completed sale: `reverseDelivery` — original events preserved, revenue/cost neutralized, movements mirrored, cash untouched; re-delivery is a new documented delivery.

## G. Data/migration (§7)
- Schema 33 / export 25; previous pairs 24/32 and 23/31 accepted; normalizers null-honest (no invented links, numbers, or states); export/import round trip preserves materialId, extras, saleId, snapshots, deposits, corrections (schema33 test).
- Entity chain verified end-to-end: Catalog/Material → Product definition → Cost estimate/snapshot → Order → Deposit/Collection → Delivery review → Sale completion → Inventory movement → Settlement → Correction/Reversal.
