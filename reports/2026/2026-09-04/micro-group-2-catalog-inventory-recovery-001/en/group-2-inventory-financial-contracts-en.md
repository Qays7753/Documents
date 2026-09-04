# Group 2 Inventory and Financial Contracts — Catalog, Selective Tracking, Movements, and Truth Boundaries

**Delivery:** micro-group-2-catalog-inventory-recovery-001 · **Date:** 2026-09-04
**Governing in-repo contract:** `docs/contracts/28-selective-inventory-tracking-contract.md` (Micro @ `1207a5a`)
**Related addenda:** contracts 09 (supplier purchase), 11 (inventory material consumption), 26 (navigation/deep-link vocabulary), 27 (guided financial entry — MIC-8 reservation note)

This report is the normative summary of every inventory/financial contract Group 2 put in force. Decision order throughout: program prompt > live code > reviews. The Micro constitution (cash / payables / receivables / owner money / Amanah / operating result / inventory / estimates stay separate; unknown never silently becomes zero; corrections preserve history; coupled writes atomic + idempotent) is never violated to transfer a Zman behavior.

---

## 1. Entity chain and write boundaries

```
CatalogItem (reference identity, estimate-only)
SupplierPurchase (cash + payables event; materialId?, expectedQuantityMilli?)
   │  explicit action only: «استلم المواد في المخزون»
   ▼
ReceiptMovement (purchase_receipt; capped by purchase total/expected)
InventoryPosition (derived fold: Σ in − Σ out, never negative)
   ├── ConsumptionMovement (consumption; orderId OR reason)
   ├── WasteMovement (waste; reason + context; non-cash)
   ├── AdjustmentMovement (adjustment; increase needs declared value or unknown)
   └── ReversalMovement (reversal; mirrors original, preserves it)
InventoryShortage (open → resolved; never a negative balance)
```

**Write boundary (greppable):** only `InventoryMaterialService` and `guidedOpeningImportService` call `createInventoryMovement` / `commitInventory*`. Group 2 added **zero** new `createFinancialEvent` call sites. Estimates, selections, drafts, and cost calculations can never create inventory or cash effects — this is a tested invariant, not a convention.

## 2. Material identity and the per-item tracking decision

- `Material.tracking?: { status: "tracked" | "untracked"; decidedOn: string | null; reason: string | null }` — optional; absent means legacy tracked (behavior-preserving, no backfill).
- `Material.opening?: { quantityState: "unconfirmed" | "confirmed"; quantityMilli: number | null; costState: "known" | "unknown"; valueMinor: number | null; confirmedOn: string | null; sourceNote: string | null }` — the activation knowledge record.
- The decision is **per material, never a global switch**. An untracked material: may be used in estimates and purchases as a cost input; holds no balance; requires no opening stock; never appears in movement forms; a purchase of it stays a financial/supplier event with an honest hint («للاستلام لاحقًا: فعّل متابعة المادة أولًا»).
- `CatalogItem` remains reference-only (contract 15 intact) — the Zman merged `catalog_component` maps to Micro as two identities: CatalogItem = estimate/reference, Material = inventory/cost-only/tracked. The tracked question lives in the material journey, exactly where Zman's journey put the per-item checkbox, without Zman's silent untrack consequences.
- Movement-form guards: every movement service rejects an untracked material with «المادة غير متتبَّعة — فعّل متابعتها أولًا» (receipt, consume, waste, adjust, extract — the last one added during recovery as SA-5 F2 and now tested).

## 3. Opening/activation knowledge contract

| Opening state | Movement written? | Position display | Cost display |
|---|---|---|---|
| `unconfirmed` (unknown) | none | «غير محدد بعد» — never 0 | «التكلفة غير معروفة» |
| `confirmed`, qty = 0 | none (qty-zero movement forbidden) | «صفر مؤكد» | — |
| `confirmed`, qty > 0, cost known | one `opening` movement (qty, value) | quantity | money value |
| `confirmed`, qty > 0, cost unknown | one `opening` movement (qty, value 0 + `costKnowledge: "unknown"`) | quantity | «التكلفة غير معروفة» |

Activation writes **no cash movement, no financial event, no expense**. Confirmation of a later/legacy unconfirmed opening goes through `confirmMaterialOpening` (deep route `/inventory/material/:id/confirm`): equal-quantity confirmation backfills knowledge; increases become a first movement; decreases are derived adjustments — all preserving the fold and recording date/source («كيف عرفته؟»). Absent `opening` on legacy materials defaults to **known** for derivation (MIC-8 and `quantityKnowledge` both) so legacy data never false-positives the unconfirmed WARN (SA-3 R8).

## 4. Movement contract (common fields and rules)

Every movement carries: `materialId`, `quantityDeltaMilli` (non-zero, sign = direction), `occurredOn` (owner date, Amman), `recordedAt`, `type`, `note`, `reason` where the type demands it, `operationKey` (idempotency), and where applicable `sourceType`/`sourceId` (purchase link), `costKnowledge`, and `reversesMovementId` for reversals.

Deliberate rule changes (documented in contract 28, decision log D-027/028/029):

1. **Consumption**: requires `orderId` **or** `reason` (Zman parity for order-less project consumption without losing the order-linked path). The editor asks «الاستهلاك لطلب محدد أم لعمل المشروع؟».
2. **Value-zero ⟺ unknown**: `valueDeltaMinor === 0` is valid **iff** `costKnowledge === "unknown"`; a known-cost zero-value movement stays forbidden. Reversals mirror the original value and inherit its cost knowledge.
3. **Quantity-zero** remains always forbidden.
4. **Idempotency everywhere**: repeating any write with the same `operationKey` returns the original record with `reused: true` — consume, receive, waste, adjust, extract, shortage-record, and the atomic consume-with-shortage pair (`${key}` + `${key}:shortage`).

## 5. Purchase → receipt bridge (TR-07)

- Purchase side: optional `materialId` + `expectedQuantityMilli` (null = unknown, never 0); edits record `beforeMaterialId` / `beforeExpectedQuantityMilli` in the revision; the edit guard rejects a new total below documented received value («راجع إيصالات الاستلام أولًا») and rejects changing or clearing the material link while receipts stand on it (SA-5 F3) — quantity sums never mix units across materials.
- A purchase **never auto-receipts**: recording it writes the purchase (cash/payables) only; inventory is untouched until the owner acts.
- Bridge action: on the purchase detail, a live received-status card shows «قيمة مستلمة: X من Y د.أ» + «كمية مستلمة: A من B» (when expected is known), lists receipt movements with reverse links, and offers «استلم المواد في المخزون» → `/inventory/movement/receipt?purchase=<id>&from=/suppliers/purchase/<id>`. A fully-received purchase shows «استُلمت قيمة هذا الشراء كاملة.» and **no** CTA (duplicate prevention by state).
- Receipt editor: the `?purchase` deep link selects the purchase, prefills material, remaining quantity, remaining value, note, and date; prefill happens once per purchase and never over owner edits; the cost question («نعم، معلومة» / «لا، غير معروفة بعد — تُسجَّل قيمة صفرية موسومة "غير معروفة"») is explicit. **Prefill never writes** — saving is the only effect (verified by the F1 dom test asserting zero movements while the form is open).
- Caps: cumulative value ≤ `totalMinor` and cumulative quantity ≤ `expectedQuantityMilli` (reversed receipts excluded). Partial receipts are the contract; over-receipt is rejected with honest copy; a second partial receipt is safe and remaining quantities reconcile.
- Deep-link vocabulary: contract 26 gained `purchase` and `material` params (id-shape `^[A-Za-z0-9_-]{1,64}$`) with documented rows and tests; the existing raw `order` param is documented alongside.

## 6. Position and cost read model

`InventoryMaterialOverview` (service-derived) exposes: received/consumed/wasted/adjusted quantities, current fold, `quantityKnowledge` («known» / «unconfirmed»), `costKnowledge` («known» / «partial» / «unknown»), open-shortage count, and source-linked history. Cost model: **Micro's moving-average-within-material kept as-is**, documented against Zman's write-time weighted average (both tested for multiple receipts at different unit costs; Micro stores the derived value on each outbound movement; round-half-up; fold-conserving). Unknown-cost stock consumes at a **marked zero** (never a confident free good); mixed positions are labeled «تكلفة معروفة جزئيًا». `readOrderActualMaterialComparison` carries cost knowledge into the order comparison surface (0-unknown shows a needs-review state, not `0.00` «recorded»).

## 7. Shortage policy (negative-stock contract, D-027)

- Direct over-consumption is **rejected** — the fold never goes negative at write, import, or integrity-check time.
- Offered alternatives when requested quantity > available: (a) «سجّل نقصًا بدل الاستهلاك» — a plain shortage record (material, requested quantity, date, note, optional order link); (b) «استهلك المتاح» — one atomic transaction writing the consumption of what is available **and** the shortage for the rest (idempotent as a pair).
- Shortage records are visible in the material row («نقص مفتوح: N»), disclosed in a collapsed `<details>` with per-record resolve; resolution («سجّل الحل») takes a note and date and keeps the record visible as resolved («حُلّ»); resolution itself is idempotent.
- MIC-8 reports an open shortage as **WARN** (policy-defined, never an unexplained PASS); the state reconciles naturally when the missing receipt arrives.
- Zman's «سيُسمح برصيد سالب عند التسليم» banner behavior was deliberately **not** transferred; the controlled-shortage-record mapping is documented in contract 28 §shortage.

## 8. Waste contract (non-cash write-off)

`هدر مخزون — بلا خروج نقد جديد`. A waste movement: links material and (optionally) waste context (order / work-reference / template / general / unallocated); requires a reason; updates the read model; creates **no** financial event and no cash movement; appears in Finance's period view as «هدر مخزون هذه الفترة» with the standing disclaimer «— غير نقدي: لا يخرج كاش ولا يدخل نتيجة الفترة.»; unknown-cost waste shows «قيمة الهدر غير معروفة بعد» instead of `0.00`; and it is correctable only through the standard reversal path (never silent deletion). The pre-existing all-time row «هدر مخزون (منذ البداية)» was relabeled so the two windows read honestly side by side. `readPeriodWaste` derives from the same `occurredOn` basis as the period reader (renamed from the old heuristic-colliding `wasteSummary…`).

## 9. Untracking, archive, deletion lifecycle

Untracking (`أوقف المتابعة`) is a dialog (not a sheet) stating: current quantity, cost state, «لا يُحذف شيء», that the material leaves movement forms, and that re-tracking returns the fold as «غير محدد بعد» until re-confirmed — the truth-corrected consequence (SA-3 R4; Zman's «يعود الرصيد المحفوظ كما هو» promise was rejected). Cancel is safe and changes nothing. Retrack (`فعّل المتابعة`) is available from the cost-only section. History is never deleted; referenced materials cannot be hard-deleted in a way that breaks history; Undo exists only for safe non-financial actions and never substitutes for a documented correction.

## 10. Migration and export contract

- Versions: schema 31 → 32, export 23 → 24 (single-file bump; legacy 23/31 pair accepted).
- New `inventory-shortages` store (contains-guarded IDB upgrade; three-store atomic `commitInventoryWithShortage`).
- Snapshot enumeration carries shortages in IDB `readSnapshot`/`replaceSnapshot`, `MemoryLocalStore`, and `emptySnapshot` (reset-all) — export, import, and «ابدأ من جديد» all handle shortages lockstep (SA-3 R2, verified by tests).
- Migration normalizations: absent optional fields → `null` (unknown, never zero); `costKnowledge` absent → known; shortages absent → empty; purchase links absent → null. No invented history, no backfill.
- Import validators: `validMaterial` (tracking/opening shapes), `validInventoryMovement` (consumption needs order-or-reason; value-zero iff unknown), `validInventoryShortage` (FK to material; resolution shape), purchase `materialId` FK; fold non-negativity re-checked at import.

## 11. Group 1 integration boundaries

- Guided financial entry, expense classification (`categoryLabel`), allocation, canonical period-result reader, and MIC-1/2/4/7/9 are untouched and regression-green.
- The buy-vs-record distinction is explicit in copy: **buying a material** = cash/payables (purchase record); **operating expense** = Group 1 event; **receiving material** = inventory movement (no cash); **consuming material** = order comparison / period COGS basis (no new cash); **wasting material** = non-cash movement outside the period result; **untracked material in an estimate** = pure reference.
- A category or tracking state never independently alters cash, profit, owner money, Amanah, or payable amounts — verified by the scenario tests asserting zero financial events across all inventory flows.
- MIC-8 slots into the existing integrity registry with no collisions (contract 27's reservation note updated); ToolsIntegrity auto-renders it.

## 12. Zman transfer map (what moved, what didn't)

| Zman behavior | Micro disposition |
|---|---|
| Per-item tracked checkbox in catalog form | **Transferred** — guided per-material question with both paths explained |
| Opening stock on first activation | **Transferred** — with known/unknown/confirmed-zero branches and source note |
| Purchase linked to tracked item, stock-in immediately | **Not transferred** — purchase stays financial; explicit receipt bridge with prefill + caps (TR-07) |
| Partial receipts | **Added beyond Zman** — caps, remaining reconciliation, safe second receipts |
| Weighted-average COGS at write time | **Adapted** — Micro's moving average kept; cost-knowledge states instead of confident zeros |
| Delivery deduction, negative allowed at delivery | **Not transferred** — rejection + atomic shortage-record policy (documented mapping) |
| Waste via manual adjustment → write-off expense row | **Adapted** — non-cash movement + period row; no event, no double counting |
| Untrack soft-deletes all movements, balance collapses with no compensation | **Not transferred** — history preserved; consequences stated; retrack unconfirmed |
| Movement history modal (last 20) | **Transferred** — inspectable history with sources and «مرتدة موثقًا» markers |
| Zero-cost "free stock" warning | **Transferred as explicit state** — «التكلفة غير معروفة» / marked-zero movements |
| Snippets/notes library | **Out of program scope** (owner decision) |
