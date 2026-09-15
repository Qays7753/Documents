# SA-4 — Financial, Data & Domain Integrity Analysis (Zman → Micro Transfer Contracts)

- **Task ID:** SA-4 (Financial, Data, and Domain Integrity Analyst, sub-agent of Zman→Micro gap analysis)
- **Date:** 2026-09-03
- **Repos analyzed (read-only clones):**
  - Zman: `/home/z/my-project/repos/zman`, `main` @ `bdd63ab` — financial code under `artifacts/zman-app/src/features/{finance,inventory,orders,catalog,depreciation,audit,reports}`; rules in `artifacts/zman-app/docs/ACCOUNTING_RULES.md`; money = integer fils (1 JOD = 1000 fils).
  - Micro: `/home/z/my-project/repos/micro`, `main` @ `4db6a5f` — domain `src/domain/` (12 modules), app services `apps/prototype-web/client/src/application/`, storage `apps/prototype-web/client/src/storage/local/` (IndexedDB, schema 30 / export 22, 26 object stores). Money = JOD minor units (2 decimals), `MoneyMinor`.
- **Methodology:** evidence-first. Every mechanism below was re-verified directly in code on both sides (not inherited from Round-1 reports); Round-1 reports (`01-zman-capability-map.md`, `02-micro-gap-comparison.md`) were read first for the candidate set (ZC-01..ZC-24, MG-01..MG-21). Inferences are labeled `INFERENCE`. Neither product repo was modified.
- **Mission:** trace the financial/data mechanics of each transfer-candidate Zman capability, then define the Micro-side financial/data transfer contract — or reject with a documented Micro financial-truth violation.

---

## 1. Zman financial architecture summary

### 1.1 Core philosophy — cash-basis ledger + exactly three read-time non-cash adjustments

`cash_movement` is the single source of truth for cash (INV-1, `docs/ACCOUNTING_RULES.md` §0/§1). Every write action in `src/features/finance/actions.ts` opens a Postgres transaction, inserts the source row(s) + the coupled `cash_movement` row(s) + an `idempotency_key` row, commits, then writes an append-only `audit_log` row **outside** the transaction (defensive; never throws — `src/features/audit/actions.ts:logAction`). Soft-delete is the only delete (INV-5); all aggregates filter `deleted_at IS NULL` (INV-6).

Three read-time non-cash adjustments modify profit without touching the ledger:
1. **COGS** — Σ(out movements `source_type='order_delivery'` × stored unit cost) (`finance/pnl.ts:209-222`)
2. **Inventory write-off** — Σ(`expense.is_inventory_writeoff=true`) read directly from the expense table, not the ledger (`finance/pnl.ts:224-237`)
3. **Depreciation** — computed at read from `capital_asset` (`depreciation/queries.ts:getDepreciationForPeriodCents`)

### 1.2 LOCKED-6 — the single profit function

`computeOperatingPnl({startDate?, endDate, tx})` (`src/features/finance/pnl.ts:122-290`) is the only profit definition:

```
operatingNetCents = salesCents − operatingExpensesCents − operatingPurchasesCents
                    − cogsCents − inventoryWriteOffCents − monthlyDepreciationCents
```

Six parallel queries; expenses/purchases conditionally split operating vs capital (`is_capital_asset`) and tracked purchases (`is_tracked_inventory`) are excluded from operating purchases (capitalized as inventory, INV-23). All three display surfaces (dashboard summary, reports P&L, monthly profit panel) call it. **IC-13** (`finance/integrityCheck.ts:1240-1323`) re-derives the number from three independent display paths for two periods (current Amman month + all-time) and FAILs on any drift — verified: it compares `getFinancialSummary` vs `computeCashBasisPnl("month")` vs `getMonthlyProfit(6)[0]`, then all-time, drift = max absolute difference.

### 1.3 The balance-sheet equation (IC-1)

`reports/actions.ts:getFinancialPosition` (verified lines 778-943):
- `totalAssets = cash + bank + inventoryValue + receivables` (line 778)
- `totalLiabilities = active order deposits` — **held deposits are the only liability** (lines 781-793)
- `retainedProfitCents = salesCashIn − deposits − operatingCashOut − cogsToDate − writeOffToDate` (lines 913-918; cash-basis, deliberately **excludes depreciation**)
- `totalEquity = opening + injections − drawings + retained − capitalAdditions` (line 923)
- `equityDriftCents = assets − liabilities − equity` must be 0 (lines 927-929); IC-1 delegates to this drift so the check and the `balanced` flag can never disagree (`integrityCheck.ts:256-264`).

Deposits held for undelivered orders are liabilities, never income — the same principle as Micro's Amanah.

### 1.4 Inventory — selective per-item tracking, capitalized purchases, immutable COGS

`ACCOUNTING_RULES.md` §9 (INV-20..25, read in full, lines 166-230):
- `catalog_component.tracked` (default false): untracked items never create movements; purchases are purely operating (deduct profit in purchase month).
- Tracked purchases: `purchase.is_tracked_inventory=true` auto-set in `createPurchase` (`finance/actions.ts:200-217`), excluded from operating P&L, capitalized as inventory; cash still leaves (`actions.ts:244-260`); movement `in` with `unitCostCents=floor(total/qty)` and **exact** `totalValueCents=total` (`actions.ts:262-287`).
- COGS on delivery: `inventory/actions.ts:deductForDelivery` (196-368) — weighted average `Σ(in_qty × unit_cost)/Σ(in_qty)` computed at sale time and **stored immutably on the out movement**; A4 "last out sweeps residual book value" (lines 313-336) avoids 1-fils residuals; negative stock is allowed and noted (lines 267-270); deduction runs only inside `convertOrderToSale`'s transaction (INV-21).
- Write-off: `adjustStock` out with value>0 inserts movement + shadow `expense` row (`is_inventory_writeoff=true`) in one transaction, **no cash movement** (INV-25, `inventory/actions.ts:551-575`). Write-off rows are guarded from edit/delete in UI; no reverse-writeoff exists (known gap م-5).

### 1.5 Corrections philosophy

- **Re-derive** on edit (`updatePurchase`/`updateSale`/`updateExpense` re-derive coupled movements).
- **Reclassify-not-double-post**: conversion reclassifies the deposit cash movement (`sourceType deposit→sale`) instead of posting new cash (`finance/actions.ts:1549-1595`).
- **Explicit inverse actions**: `reverseSale` (1650), `reverseDepositForfeiture` (2238).
- Order→sale chain (all verified in code):
  - `convertOrderToSale` (1441-1638): row lock, guards (price>0, not cancelled, deposit ≤ realized, no active sale — F-32 allows re-convert after sale deletion), idempotency key, sale = FULL realized (price + additionalProfit), deposit movement reclassified, remainder movement computed **from the collected movement amount** (not `order.depositCents` — avoids re-booking refunded parts), `deductForDelivery` inside the same transaction **before** status→delivered.
  - `forfeitDeposit` (2020-2232): cancelled order's remaining deposit becomes a `source='manual'` sale row + the deposit movement is reclassified to that sale; deposit zeroed; **no new cash movement**; reversible by `reverseDepositForfeiture`. Guarded by IC-16.
- Historical data: cut-over policy — old months are never rewritten; only capital assets deserve retro-correction (CLAUDE.md §7).

### 1.6 Idempotency (Zman model)

Server Actions + `idempotency_key` table (requestId PK, action, targetId). Checked and inserted inside each transaction (`createExpense` 701-717, `createPurchase` 158-176, `convertOrderToSale` 1455-1526). Forms add an `inFlight` ref double-submit guard (`SmartFinanceForm.tsx:254,488`). `requestId: crypto.randomUUID()` is generated **inside the submit handler** (`SmartFinanceForm.tsx:537,615,697,749`) → the key is per-attempt, not per-intent: a retry after an ambiguous network failure generates a new key and can duplicate (mitigated by rate limiting and DB constraints; labeled a real residual risk — see FI-10).

---

## 2. Micro financial architecture summary

### 2.1 Write path and the five-delta event model

Enforced path: React page → Application service → Domain (`src/domain`) → `PrototypeLocalStore` → IndexedDB (verified `storage/local/types.ts:264-405`, `IndexedDbLocalStore.ts`). No page touches IndexedDB directly.

`src/domain/financial-event/types.ts:7-15` — exactly 8 event types; `policies.ts:186-198` maps each to a **declared five-delta effect** `[cash, payable, ownerCapital, operatingExpense, amanah]`:

| type | cash | payable | ownerCapital | opExpense | amanah |
|---|---|---|---|---|---|
| owner_investment_cash | +1 | 0 | +1 | 0 | 0 |
| owner_withdrawal_cash | −1 | 0 | −1 | 0 | 0 |
| operating_expense_cash | −1 | 0 | 0 | +1 | 0 |
| operating_expense_payable | 0 | +1 | 0 | +1 | 0 |
| payable_settlement_cash | −1 | −1 | 0 | 0 | 0 |
| amanah_held_cash | +1 | 0 | 0 | 0 | +1 |
| amanah_released_cash | −1 | 0 | 0 | 0 | −1 |
| loss_non_cash | 0 | 0 | 0 | +1 | 0 |

**Amanah can never appear as profit by construction** — it lives in its own delta column, never in `operatingExpenseDelta` (`policies.ts:192-197`, principle 13 comment). Shared unallocated expenses contribute **0** to operating expense until a declared share exists (`policies.ts:206-209`) — missing ≠ zero.

### 2.2 Corrections — documented, atomic, reversible, idempotent

- Reversals are new records with negative deltas + `correctionType:"reverse"`, `correctionOfEventId`, mandatory reason, and their own idempotency key (`policies.ts:271-300`); a reversal is itself never reversible (`policies.ts:277-278`).
- Storage commits are **atomic multi-record transactions**: `commitFinancialEventCorrection` (reversal attached to source), `commitFinancialEventReplacement` (reversal + replacement together — "لا يبقى أثر معلّق بينهما", `storage/local/types.ts:305-314`), `commitOrderCollectionReversal` (order + matching cash allocation in one transaction, with in-transaction identity check and `reused` result — `types.ts:280-289`, `IndexedDbLocalStore.ts:740-869`), `commitInventory`, `commitCashContinuity`, `commitOwnerMovement`, `commitShortCashDeclarationReversal`, etc.
- Every sensitive correction flows through `CorrectionPreview` before execution; originals are never deleted (before-values preserved on supplier purchase revisions `supplier-purchase/types.ts:24-35`, direct-sale revisions `direct-sale/types.ts:36-43`).
- Unified read-only corrections history: 11 kinds (`application/finance/correctionHistoryService.ts:10-23`).

### 2.3 Bounded period result ("missing ≠ zero")

`application/finance/projectFinancialService.ts:readRecordedPeriodResult` (433-639):
- Revenue recognized once, at `delivered`/`settled`, **from the order record** (`recognizedRevenueMinor`, `craft-order/policies.ts:406-422`); F-005: later collections never create second revenue (comment 502-503).
- Only orders with `resultStatus === "final"` enter the sum; incomplete ones are **excluded and counted** (`excludedOrderCount`), never zeroed.
- COGS from **evidence**: `derivePeriodCogs` (232-301) uses cost-backed consumption movements linked to final orders; `cogsStatus ∈ recorded|partial|not_available`.
- `resultMinor` is **null** when any direct sale has unknown cost (line 624-631); `status: "incomplete"` with Arabic reasons otherwise `"recorded_only"`. No "final net profit" is ever claimed.

### 2.4 Inventory — opt-in, explicit evidence, non-negative

`inventory-material/policies.ts`: movements carry both `quantityDeltaMilli` and `valueDeltaMinor` (value is declared/derived at write, immutable thereafter); consumption **rejects** negative positions (`assertInventoryRemainsNonNegative` 144-152); consumption value = proportional share of book value via `roundHalfUp` (132-143, decision 20: reject unrepresentable share, "أخرِج المتبقي"); waste requires `wasteContext`; reversal movements carry `reversesMovementId`. Inventory activation is dated and explicit (`InventoryActivation`, decision 9/10 usage in `projectFinancialService.ts:452-461`). Purchases affect cash/payables only (`supplier-purchase/types.ts` header) — purchase ≠ COGS.

### 2.5 Cash continuity and order model

- `cash-continuity/types.ts`: wallets (4 kinds), entry types `opening_balance|cash_adjustment|transfer_out|transfer_in|reversal|allocation`; allocations carry `sourceRef{Id,Kind,LineId}` (sale/expense/collection/order); opening status `known|unknown` — unknown never reads as zero.
- Orders never touch cash directly: collection goes through the record's owning service (`fulfillmentService.ts` domain calls only), then cash allocation via the single `distributeUnallocated` path with one operation key (`collections/collectionService.ts:194-204`); reversal of a collection is the atomic `commitOrderCollectionReversal`.
- Deposits: `collectDeposit` → `deposit_collected` event; cancel → `depositSettlement: "needs_review"` gating; `settleDepositRefund` reduces collected cash; `settleDepositRetain` records the decision (`settlementStatus: "cancelled_retained"`) — **no revenue is created anywhere on retain** (`craft-order/policies.ts:814-855`).

### 2.6 Export/import and idempotency

- Full-store verified export v22 / schema 30; import accepts a chain of older versions (export 6..21, schema 14..29 — verified `localTransferService.ts:1938-1960`), migrates, `validateSnapshot` (relations incl. reversals, partial collections, price_cut, amanah deltas), then **atomic `replaceSnapshot`** (line 2144).
- Idempotency: `idempotencyKey`/`operationKey` on records; unique indexes (`IndexedDbLocalStore.ts:209` sales idempotencyKey unique; declarations/policies/records/balances/movements, lines 289-323); in-transaction reuse checks return `reused: true`; application services add pre-read key-collision detection (`projectFinancialService.ts:805-818`). Editors generate the key **once per form instance** (`FinancialEventEditor.tsx:126` `useRef`) — per-intent, survives in-form retries.

---

## 3. Financial transfer contracts (FI-01..FI-10)

### FI-01 — Expense category vocabulary (lazy catalog, orphan-merge, grouping)

**Zman trace.** `expense.category` is a required denormalized text (≤200) on every expense row (`finance/db.ts:61`). `createExpense` (`actions.ts:678-783`): trims the category, calls `ensureExpenseCategoryInCatalog` (2639-2665) **inside the same transaction** — case/whitespace-insensitive existence check, insert if new, and **failure never blocks the expense save** (catch → console.warn). Category CRUD (`actions.ts:2667-2790`): create/rename/soft-delete on `expense_category_catalog` only — **rename does not rewrite historical expense rows**; delete leaves history untouched. Filter vocabulary = catalog ∪ `SELECT DISTINCT category FROM expense` (orphan-merge; `finance/queries.ts:902`). P&L expense distribution groups by the raw text (`reports/actions.ts:234` `groupBy(expense.category)`), so renames split the distribution across old/new spellings until manual cleanup (duplicate seeded categories م-11 documented). Financial effect of the category label itself: **zero** — money effects come only from `isCapitalAsset`/`costNature`/`isInventoryWriteoff`. Corrections: `updateExpense` re-derives the cash movement; write-off rows are edit/delete-guarded. Duplicate-submission: `idempotency_key` + in-flight lock.

**Micro mapping.** `FinancialEvent.expenseContext` (`financial-event/types.ts:30-36`) has relationship/behavior/purpose/knowledge + sharedProjectShare but **no named category**; period statement splits project/shared/unallocated/legacy (`projectFinancialService.ts:543-581`). Category would be an optional, non-financial label on `OperatingExpenseContext`; the vocabulary can be a **derived read model** (distinct labels over events — the orphan-merge property is inherent to derivation) with optional lazy persistence. It must NOT become an allocation mechanism (G3 contract forbids hidden allocation; `sharedProjectShare` is the only allocation path) and must not affect `resultMinor`, amanah, owner capital, or cash deltas.

```
finding_id: FI-01
capability_name: Expense classification — optional category vocabulary (ZC-02/ZC-01, MG-01)
comparison_classification: MICRO-DIFFERENT (MG-01)
zaman_evidence: artifacts/zman-app/src/features/finance/db.ts (expense + expense_category_catalog); finance/actions.ts:678-783 (createExpense), 2639-2790 (category CRUD + lazy enrollment); finance/queries.ts:902 (orphan-merge); reports/actions.ts:234 (groupBy category)
micro_evidence: src/domain/financial-event/types.ts:30-36 (OperatingExpenseContext); src/domain/financial-event/policies.ts:139-181 (normalizeExpenseContext); apps/prototype-web/client/src/application/finance/projectFinancialService.ts:543-581 (project/shared/unallocated/legacy split); docs/contracts/08-expense-classification-prototype-contract.md
financial_and_data_effect: Zman: category is a write-time text on each expense + a pick-list table; zero effect on cash/profit — purely grouping/filtering; rename leaves history split (no merge tool); write-off category rows immutable. Micro: label would ride the financial event record; grouping is a read-model concern (statement lines); zero effect on the five deltas.
transfer_recommendation: adapt
micro_destination: FinancialEventEditor secondary layer (G22 pattern) → OperatingExpenseContext.categoryLabel; /finance/statement optional per-category lines (derived, read-only)
micro_contract:
  record shape: OperatingExpenseContext += { categoryLabel?: string | null } — ≤80 chars, trimmed, internal whitespace collapsed (Zman lesson: trim-before-compare prevents "راتب مالك"/"راتب المالك" duplicates); stored frozen on the event (part of recorded context, immutable like note).
  vocabulary: derived read model = DISTINCT labels over active operating-expense events (orphan-merge inherent) + optional curated names list (local non-financial store, CostEstimate precedent); NO write-time auto-catalog needed offline (derivation replaces lazy enrollment); if a curated store is added it must never block the save (Zman's never-block rule).
  effects: cash/amanah/receivables/owner/period-result — none (label only). knowledge of the expense unchanged.
  corrections: label is immutable per event. A "merge categories" is NOT a silent tool: relabeling history = per-event atomic replacement (commitFinancialEventReplacement) with reason — only if the owner chooses; default UX offers filter only.
  idempotency: inherits the event's idempotencyKey (payload field, no separate key).
  migration: schema 30→31 (optional field on FinancialEvent.expenseContext), export 22→23; import migration defaults categoryLabel→null for older snapshots (pattern proven: amanahDeltaMinor ?? 0, localTransferService.schema29.test.ts); normalizeExpenseContext gains length/shape assertions; no backfill (legacy null = "غير مصنّف", already surfaced honestly as legacyUnclassifiedExpenseCount).
priority: P1
confidence: high
risks: label drift splitting per-category totals (same as Zman — acceptable, documented); a future "recurring category rules" temptation must stay out (never auto-write expenses); G3 hidden-allocation boundary — category must never influence sharedProjectShare.
open_questions: curated store vs pure derivation (owner decision, MG-01); should statement show per-category lines by default or behind a toggle?
```

### FI-02 — Selective per-item inventory automation (tracked flag, auto-deduct, capitalized COGS)

**Zman trace.** Full chain verified: `catalog_component.tracked` flag → `createPurchase` auto-sets `purchase.is_tracked_inventory` and inserts `catalog_movement(in)` (`finance/actions.ts:200-287`) → excluded from `operatingPurchasesCents` in `computeOperatingPnl` (SQL CASE, `pnl.ts:186-200`) → `convertOrderToSale` calls `deductForDelivery` **inside its transaction** which auto-deducts `component.quantity × order.quantity` for every tracked linked component with weighted-average COGS stored immutably on the out movement (`inventory/actions.ts:196-368`) → `restoreForReverse` soft-deletes those movements on `reverseSale` (`inventory/actions.ts:385-414`). Negative stock allowed (documented); untrack with stock>0 requires confirmation and soft-deletes the movement history. IC-12: FAIL on orphaned movement rows, WARN on negative balances. Opening stock enters at **zero cost** (documented trade-off, CLAUDE.md §7).

**Micro mapping.** Micro's inventory is opt-in and **deliberately explicit**: dated activation; per-material movements recorded by the owner (per-order actual-material panel, `ActualMaterialPanel` + G6 contract); COGS only from cost-backed consumption linked to final orders (`derivePeriodCogs`); purchases affect cash/payables only — they never hit the period result at all, so Zman's "capitalization" exclusion has nothing to port. Optional selection already exists at the sale level (`DirectSale.catalogItemId?`, `direct-sale/types.ts:18-19`) and inventory is never forced (current-state.md Group 3). Micro **rejects negative inventory at write** (`assertInventoryRemainsNonNegative`) and requires honest movement value (non-zero).

Hard conflicts of the automation core with Micro truth rules:
1. Auto-deducting stock from an order's component list creates **inventory effects from cost estimates** (order components/CostSnapshot materials are estimate-grade data with confidence states) — violates "estimates must NOT silently create financial or inventory effects".
2. Delivery-time silent deduction bypasses Micro's **explicit-evidence** boundary (consumption is evidence, G3/G6 contracts).
3. Negative-stock tolerance contradicts Micro's non-negative inventory invariant (a deliberate Micro guarantee).
4. Opening stock at zero cost converts an unknown into zero — violates "missing ≠ zero".

What is already present in Micro (nothing to port): optional/non-forced inventory; immutable value stored on consumption at write time (`consumptionValueMinor` proportional book-value share ≈ Zman's immutable weighted-average, but computed honestly from position and rejecting unrepresentable shares); reversal movements with explicit `reversesMovementId` (stronger than Zman's soft-delete restore). Transferable non-core nicety: non-blocking low-stock reading on the inventory screen (read-only, P2).

```
finding_id: FI-02
capability_name: Selective per-item inventory automation (ZC-07, MG-02)
comparison_classification: MICRO-DIFFERENT (MG-02)
zaman_evidence: catalog/db.ts (tracked flag, migration 0019); finance/actions.ts:200-287 (isTrackedInventory auto-set + movement in + capitalization); finance/pnl.ts:186-200 (tracked purchases excluded); inventory/actions.ts:196-368 (deductForDelivery, immutable weighted-avg COGS, A4 sweep, negative allowed), 385-414 (restoreForReverse), 431-583 (adjustStock); docs/ACCOUNTING_RULES.md §9 INV-20..25
micro_evidence: src/domain/inventory-material/types.ts:18-33; src/domain/inventory-material/policies.ts:64-152 (sign rules, non-negative, consumptionValueMinor, wasteContext); apps/prototype-web/client/src/application/finance/projectFinancialService.ts:224-301 (derivePeriodCogs evidence model); src/domain/direct-sale/types.ts:18-19 (optional binding); docs/decisions/actual-material-cost-per-order-g6-scope.md
financial_and_data_effect: Zman: tracked purchases leave cash but not profit; profit loses COGS at sale via stored immutable unit cost; write-off dual-enters movement+expense without cash; equity stays balanced via inventory asset. Micro: purchases touch cash/payables only; period result loses cost only via recorded consumption evidence; positions non-negative; reversals documented.
transfer_recommendation: reject (automation core) — optional-selection philosophy and immutable-at-write cost already exist in Micro in stricter form
micro_destination: n/a (optional nicety: read-only low-stock indicator on /inventory)
micro_contract: N/A — rejected. Sub-elements explicitly rejected: auto-deduct-on-delivery (estimate-effect + evidence violations), negative-stock tolerance (invariant conflict), zero-cost opening stock (unknown→zero). Sub-element already present: per-item opt-out, immutable written cost, reversal of consumption. Optional non-transfer: low-stock read-only reading.
priority: P0 (boundary decision — Round-1 ranked ZC-07 highest on Zman side; parent must record the non-transfer)
confidence: high
risks: a future "one-tap suggested consumption from the draft's material list" could re-introduce the violation if silent — allowed only as an explicit suggestion requiring a real write action (MG-02 open question preserved).
open_questions: none for the reject; UX-only question of consumption suggestions belongs to Micro design, not Zman transfer.
```

### FI-03 — LOCKED-6 single profit function + runtime cross-check (ZC-09)

**Zman trace.** One function (`computeOperatingPnl`) + IC-13 cross-check of three display sources over two periods; any drift = FAIL; adding a third profit number is forbidden by the D3 naming rule (two declared numbers only: operating after depreciation, and cash-retained before depreciation).

**Micro mapping.** Micro has **two independent result-computing read paths**: `projectFinancialService.readRecordedPeriodResult` (used by Finance period view + insights) and `application/finance/statementService.ts` (statement lines: cash/result/amanah/receivables/payables/owner), plus `homeControlCenterModel` position facts. There is no runtime cross-check that they agree; drift between surfaces is currently guarded only by tests. Copying Zman's *formula* is impossible (Micro's result is bounded, null-on-unknown, and excludes nothing silently) — but the **architecture** (one canonical compute function + a runtime drift check) transfers cleanly and strengthens Micro's "one honest reading" promise without touching the bounded-profit boundary.

```
finding_id: FI-03
capability_name: Single period-result function + runtime cross-check (ZC-09, MG-07)
comparison_classification: MICRO-WEAKER (MG-07)
zaman_evidence: src/features/finance/pnl.ts (whole file, LOCKED-6 header); finance/integrityCheck.ts:1240-1323 (IC-13); CLAUDE.md §2 LOCKED-6; dashboard/queries.ts + reports/actions.ts (callers)
micro_evidence: application/finance/projectFinancialService.ts:433-639 (readRecordedPeriodResult); application/finance/statementService.ts (independent statement computation); application/home/homeControlCenterService.ts (position facts); docs/product/financial-operating-model-v1.md §13 (idempotency + no silent reinterpretation)
financial_and_data_effect: Zman: guarantees one operating number across dashboard/reports/monthly; IC-13 fails on drift. Micro today: two read models can theoretically disagree; no runtime guard; result deliberately bounded (null on unknown) — the boundary itself must be preserved in any adaptation.
transfer_recommendation: adapt
micro_destination: application/finance — designate readRecordedPeriodResult as THE canonical period-result function; statementService result/cash lines consume or cross-check it; add runtime cross-check into the FI-04 integrity suite (MIC-1); domain/application test locking the read surface.
micro_contract:
  record shape: no new records. Add pure function contract: every surface that shows a period number must call ProjectFinancialService (or a thin wrapper) — no inline arithmetic in pages.
  cross-check (runtime, read-only): recompute (a) period result from stores, (b) statement result line, (c) finance period view values; drift > 0 JOD minor → WARN entry in integrity surface with both numbers (never auto-fix; fix path = open the surface's source service).
  effects: none on writes; zero schema/export impact.
  idempotency: n/a (read-only).
  migration: none; guarded by a public-surface test (pattern exists: tests/domain/public-surface.test.ts).
  boundary guard: the cross-check must compare like-for-like knowledge-bounded values; when resultMinor is null, all surfaces must show the same "غير متاح + أسباب" state — absence of a number is itself a value to cross-check (never zero).
priority: P0
confidence: high
risks: statementService computes additional decompositions (amanah held/released, corrections line) — cross-check scope must be limited to the exact fields both models derive; over-strict comparison would cry wolf.
open_questions: whether statementService should be refactored to consume readRecordedPeriodResult directly (cleaner) or kept independent and only cross-checked (redundancy as a feature, Zman's IC-13 philosophy).
```

### FI-04 — Integrity check suite (IC-1..IC-16, user-facing «فحص الآن»)

**Zman trace.** `runFinancialIntegrityCheck` (16 checks, parallel, read-only; PASS/WARN/FAIL with Arabic titles + suggested fixes) exposed via /reports button (`finance/integrityCheck.ts` + `reports/components/IntegrityCheckReportPanel.tsx`). Full enumeration in §4 below.

**Micro mapping.** No user-facing integrity surface. Structural enforcement at write + import-time verification exist (single write path, unique indexes, atomic commits, import relation validation); the owner cannot press "check my numbers". The transfer is the **concept + check-report UX**, with Micro's own invariants — not Zman's checks verbatim (several are meaningless for Micro's model, e.g. equity drift over a balance sheet Micro doesn't construct).

```
finding_id: FI-04
capability_name: User-facing financial integrity self-check (ZC-16, MG-08)
comparison_classification: ZAMAN-ONLY (MG-08)
zaman_evidence: finance/integrityCheck.ts (1608 lines, IC-1..IC-16); reports/components/IntegrityCheckReportPanel.tsx; finance/actions.ts:4127 (runFinancialIntegrityCheckAction)
micro_evidence: no integrity surface; structural equivalents: storage/local/IndexedDbLocalStore.ts (unique indexes, atomic commit* transactions), application/transfers/localTransferService.ts (import relation validation), application/finance/correctionHistoryService.ts (corrections digest), tests/domain/public-surface.test.ts
financial_and_data_effect: Zman: read-only checks with severity + fix suggestions; production evidence 14 PASS / 1 WARN / 0 FAIL. Micro: nothing equivalent visible to the owner today.
transfer_recommendation: adapt
micro_destination: أدواتي (Tools) → new read-only deep page «فحص سلامة مالي» (+ optional link card from مالي); application/finance/integritySelfCheckService.ts — pure reads over existing stores/read models
micro_contract:
  record shape: CheckResult[] = { id: "MIC-<n>", titleAr, status: "PASS"|"WARN"|"FAIL", detailAr, offendingIds?, deepLinks? } — read-only, no new stores, no schema/export change.
  proposed Micro checks (MIC-1..MIC-9): (1) period-result cross-surface consistency (FI-03); (2) cash position consistency — readPosition vs Σ cash-continuity entries vs Σ event cashDeltas; (3) reversal balance — every reversal/correction references an existing, active, not-yet-reversed original, across events/cash/movements/declarations/owner records; (4) allocation sourceRef integrity — sourceRef{Id,Kind,LineId} references existing records (reuse localTransferService validation rules at runtime); (5) collection consistency — order.collectedMinor == Σ active collection events; direct-sale collected == its allocations; (6) deposit settlements pending — cancelled_pending orders with deposit needs_review → WARN (decision pending, not an error); (7) amanah non-negative (F-006 at write; read-back check); (8) inventory — positions non-negative, reversal refs valid, consumption/waste orderId/purchaseId exist (activeInventoryMovements relations); (9) knowledge honesty — final orders' resultStatus vs snapshot knowledgeGaps; direct sales with null cost (informational count).
  fix actions: deep links to the owning record/correction editor only — NO auto-fix writes (fixes must go through the documented correction flows).
  idempotency: n/a (read-only).
  migration: none (outside schema 30/export 22).
priority: P0
confidence: high
risks: check severity wording must not alarm for deliberate states (unknown openings, needs_review deposits are honest states → WARN/info, not FAIL); placement decision (أدواتي "thinking tool" identity vs مالي money truth) is an owner decision (MG-08 open question preserved).
open_questions: exact check list sign-off; placement; whether the digest runs on every Finance open (cheap reads) or only on demand.
```

### FI-05 — Order→sale conversion + deposit reclassification + forfeit-as-revenue (ZC-06)

**Zman trace** (every step code-verified, §1.5): one transaction books revenue exactly once at delivery (sale = full realized; deposit movement **reclassified** to the sale, remainder movement for the delta); stock deduction inside the same transaction; complete inverse chain (`reverseSale`, `refundOrder` with independent out-movement capped at remaining, `forfeitDeposit` reclassifying the deposit to a manual sale **without new cash**, `reverseDepositForfeiture`); guarded by unique partial index (no double conversion), IC-3/4/9/16.

**Micro mapping.** Micro deliberately recognizes revenue **on the order itself** at `delivered`/`settled` (`transitionOrder`) — there is no sale record to convert to; collections are cash-only and never revenue (F-005); the deposit lifecycle is event-logged with `needs_review` gating and explicit refund/retain settlement decisions; reversals are documented records, not soft-deletes/reclassifications. Copying Zman's mechanism would:
1. create a **second revenue path** (order-embedded recognition + converted sale) → double-booking risk, violating the single write-path rule;
2. **mutate an existing cash event** (reclassify `sourceType`/`sourceId` of a past movement) — violates Micro's append-only correction model (originals preserved; corrections are new records);
3. book forfeited deposits as revenue automatically — violating Micro's collection≠profit boundary and its no-guessing rule for retained-deposit accounting (Micro currently records the retain decision without revenue; the classification of retained deposits as income is an **owner decision behind a contract**, not a transfer).

One genuine gap surfaced by the comparison (not a transfer): Micro's retained deposit is currently cash that is neither revenue, nor liability, nor amanah — its accounting home is undefined ("cancelled_retained" documents the decision only). Recommendation: keep the honest deferred state, surface it in the statement (deposits layer exists on Finance), and require an owner decision + specialized contract before any "retained deposit income" event type exists.

```
finding_id: FI-05
capability_name: Order→sale conversion + deposit transform + reversals (ZC-06, MG-05)
comparison_classification: MICRO-SUFFICIENT (MG-05)
zaman_evidence: finance/actions.ts:1441-1638 (convertOrderToSale), 1650-1786 (reverseSale), 1787-2019 (refundOrder), 2020-2232 (forfeitDeposit), 2238-2440 (reverseDepositForfeiture); migrations 0014/0015; ACCOUNTING_RULES INV-3/4/9
micro_evidence: src/domain/craft-order/policies.ts:368-449 (revenue recognized at delivered/settled on the order), 499-530 (collectDeposit), 770-812 (cancel + needs_review), 814-891 (settleDeposit refund/retain — no revenue); application/fulfillment/fulfillmentService.ts (collectFromSheet single path, S2-02 operation keys); application/collections/collectionService.ts:194-204 (allocation via distributeUnallocated); storage/local/types.ts:280-289 (atomic collection reversal); projectFinancialService.ts:502-503 (F-005 revenue-once comment)
financial_and_data_effect: Zman: revenue at conversion, deposit liability → sale via reclassification, remainder cash, forfeiture = manual sale without cash. Micro: revenue on order at delivery; collections are cash-only; deposits settled by explicit decisions; no reclassification ever — corrections are new negative-delta records.
transfer_recommendation: reject
micro_destination: n/a (the retained-deposit accounting question is logged as a Micro-side open decision, not a transfer)
micro_contract: N/A — rejected. Sub-patterns already stronger in Micro: book-once revenue (F-005), full documented inverses (collection_reversed, price_revised, sale edits), atomic coupled corrections, idempotent conversion-free lifecycle. Rejected sub-patterns: cash-event reclassification (append-only violation), auto convert-to-sale (second revenue path), auto forfeit-as-revenue (collection≠profit / no-guessing).
priority: P1
confidence: high
risks: none from rejection; risk only if partially ported (e.g. reclassify-style "fix" tools).
open_questions: owner decision + contract for retained-deposit income classification; statement wording for retained deposits today (should read "عربون محتفظ به — قرار موثق، ليس إيرادًا بعد").
```

### FI-06 — Assets & depreciation (ZC-10)

**Zman trace.** `capital_asset` per (sourceType, sourceId) — idempotent; `monthlyDepreciationCents = floor(amount/life)`; startedAt = purchaseDate (retroactive entry allowed); depreciation counted from month after start; period-scaled formula `(min(months(end),life) − min(months(start),life)) × monthly_dep` with correct `EXTRACT(YEAR)*12+EXTRACT(MONTH)` months (CRITICAL-NOTE-4); last month sweeps the remainder (D13 → NBV exactly 0); **no cash movement ever** (INV-22); P&L deducts period depreciation; balance sheet stays cash-basis (retained excludes depreciation → dual profit labels); opt-in prompt modal; `deleteCapitalAsset` = soft delete stops depreciation, underlying expense/purchase and cash remain; IC-14 (FAIL orphan assets, WARN fully-depreciated).

**Micro mapping.** Nothing implemented; explicitly deferred behind a specialized contract (`docs/decisions/remaining-capabilities-review-v1.md:32` "أصول، إهلاك… مؤجل بعقد متخصص… لا نخمن قواعدها"; :127 "لا يجوز أن تتحول ماكينة أو ثلاجة إلى مصروف طلب كامل"). The existing hook is `loss_non_cash` (one-off non-cash loss). A recurring computed depreciation is expressible as **read-time modeling over an asset register**, exactly like Zman — but Micro's rules add constraints Zman doesn't have: depreciation must surface as a declared non-cash reduction with knowledge state (useful life is an owner estimate → the period result that includes depreciation can never be labeled "final" on that basis alone without the contract deciding so), and it must not silently change historical statements (Zman's retroactive `startedAt` re-derives future reads — acceptable; Micro must state restatement behavior explicitly).

```
finding_id: FI-06
capability_name: Assets & read-time depreciation (ZC-10, MG-10)
comparison_classification: ZAMAN-ONLY (MG-10)
zaman_evidence: depreciation/db.ts (capital_asset); depreciation/actions.ts (addCapitalAsset:59, updateCapitalAsset:282, deleteCapitalAsset:211); depreciation/queries.ts:83-127 (period formula), 160+ (valuation with D13 sweep); pnl.ts:202-206; integrityCheck.ts:1352-1405 (IC-14); ACCOUNTING_RULES §10 (INV-22)
micro_evidence: no asset code; deferral: docs/decisions/remaining-capabilities-review-v1.md:32,127; hook: src/domain/financial-event/types.ts:15 (loss_non_cash) + policies.ts:197 (non-cash loss delta)
financial_and_data_effect: Zman: purchase hits cash once (capital classification excludes it from operating profit); depreciation reduces operating net monthly without cash; equity reconciliation via capitalAdditions line. Micro: purchase would be supplier-purchase/expense; no spreading exists; loss_non_cash is the only non-cash reduction today.
transfer_recommendation: adapt (gated — only after the Micro specialized contract; effectively "reject now, adopt the mechanics later")
micro_destination: future: مالي deep editor + new domain module (asset register) + read-time depreciation service; NOT a financial event per month
micro_contract (sketch for the future contract, per Micro's no-guessing rule):
  record shape: AssetRegister { id, name, purchaseDate, purchaseAmountMinor, usefulLifeMonths, monthlyDepreciationMinor = floor(amount/life), startedAt = purchaseDate, status: active|retired, retirement {date, reason}, idempotencyKey } + purchase linkage (supplier purchase or operating event reference, non-FK soft link like Zman to survive source corrections).
  computation: read-time only (Zman pattern preserved): periodDepreciationMinor over [from,to] via capped months-elapsed formula; last-month sweep; months via exact calendar-month arithmetic (Zman's CRITICAL-NOTE-4 lesson — never date_part month-only).
  effects: cash — none ever; period result — a separate, explicitly labeled non-cash reduction line («إهلاك محسوب — غير نقدي») with its own knowledge state; must NOT fold into operatingExpense events; resultStatus rules unchanged (a period containing computed depreciation is at best "recorded/estimated", never silently "final").
  correction model: revise life/date = documented revision with before-values (append-only, like supplier purchase revisions); retire/stop = documented status change; never rewrite past readings — restatement policy declared in the contract.
  idempotency: idempotencyKey on register writes; read computation deterministic.
  migration: new store(s) → schema major bump (31+), export version bump, import migration (absent store = empty register for older files — trivial), validateSnapshot extension; only after contract approval per remaining-capabilities-review.
priority: P2
confidence: high (mechanics); the Micro contract specifics (persona-fit, Jordanian norms, disposal) are open by design
risks: premature build without contract = exactly the "نخمن قواعدها" violation Micro documents; dual-profit-label confusion if the reduction is styled like an expense.
open_questions: straight-line only? disposal gain/loss handling? minimum capitalization threshold? — all contract-level, listed for the owner.
```

### FI-07 — Non-cash write-off (ZC-18)

**Zman trace.** `adjustStock(out, value>0)` = one transaction: movement out (weighted-avg, A4 sweep) + shadow expense (`category='هدر/تلف مخزون'`, `isInventoryWriteoff=true`, variable, no cash movement); P&L reads it as a dedicated line directly from the expense table; balance sheet deducts from retained + inventory so IC-1 stays 0; write-off rows are **immutable** (no edit/delete in UI, no reverse — known gap م-5).

**Micro mapping.** Present, in a deliberately decoupled and **reversible** form: inventory `waste` movement with `wasteContext` (order / catalog item / template / general / unallocated) + mandatory reason (`inventory-material/policies.ts:68,76-90`), reversible via a `reversal` movement (`reversesMovementId`); and the standalone `loss_non_cash` financial event (cash 0, operatingExpense +1) for non-material losses. The period reading surfaces general waste and unallocated consumption as named lines/reasons (`derivePeriodCogs:272-290`) rather than silently subtracting them from `resultMinor` — an honest boundary choice (they block "clean" status instead of being guessed into the number).

The only element of ZC-18 that must **not** be copied is its immutability (edit/delete-guarded, no reverse): in Micro every sensitive effect must remain traceably correctable — Micro's existing design is the compliant one. One integrity-check note: Micro has two paths for material loss (waste movement vs loss_non_cash event) with no cross-linkage; recording both for the same physical loss could double-report in the reading layer (waste is displayed; loss_non_cash is subtracted) — flagged for the FI-04 suite as a soft warning candidate (cannot be auto-detected without a linkage field; documented as open question).

```
finding_id: FI-07
capability_name: Non-cash write-off (ZC-18, MG-02-adjacent)
comparison_classification: MICRO-SUFFICIENT (false-gap warning #9 in SA-2)
zaman_evidence: inventory/actions.ts:431-583 (adjustStock dual-entry, INV-25); finance/pnl.ts:224-237 (write-off line); migration 0025; CLAUDE.md م-5 (no reversal — known gap)
micro_evidence: src/domain/inventory-material/types.ts:10-17 (waste + wasteContext); policies.ts:76-90 (waste rules + reason); src/domain/financial-event/policies.ts:197 (loss_non_cash deltas); projectFinancialService.ts:272-290 (waste surfaced as line/reasons)
financial_and_data_effect: Zman: movement + shadow expense atomically; reduces profit + inventory; no cash; irreversible. Micro: waste movement reduces inventory position (reversible via reversal movement); loss_non_cash event reduces recorded operating result without cash; general waste surfaces as a reading line that blocks clean status rather than entering the number.
transfer_recommendation: direct — concept already present in Micro; the Zman implementation's irreversibility must NOT be copied (would violate Micro's traceable-corrections rule)
micro_destination: n/a (existing waste movement + loss_non_cash)
micro_contract: N/A — nothing to port. Guardrail note for future editors: never make waste/loss records immutable-only; keep reversal paths.
priority: P2
confidence: high
risks: double-reporting in the reading layer if a user records both a waste movement and a loss_non_cash event for the same physical loss (no linkage field today).
open_questions: optional wasteContext linkage to a loss event id (would enable the double-count warning in FI-04); whether general waste should ever subtract from resultMinor is an owner decision (today: displayed + blocks clean status).
```

### FI-08 — Report export / balance-sheet artifact (ZC-15)

**Zman trace.** /reports builds 6 Markdown reports (pnl, expenses-by-category, sales sources, orders funnel, products, balance_sheet) with per-section download (UTF-8 BOM blob, `downloadReport`); balance sheet = the §1.3 equation (assets = cash+bank+inventory+receivables; liabilities = held deposits only; equity with capitalAdditions subtraction; drift must be 0; advanced reconciliation section).

**Micro mapping.** On-screen statement only (`/finance/statement`: Sunday→Saturday week default, quick ranges, custom; every line links to sources; restatement note; corrections line — `statementService`). No downloadable artifact (MG-13). Micro's components can compose an honest position summary (cash wallets + unallocated, amanah, receivables from orders/sales debts, payables, owner capital/entitlement) **without** claiming an accounting-equation balance: Micro's model is delta-based, not double-entry; fabricating "equity" or a "balanced" claim would create false comfort and collide with the bounded-profit boundary.

```
finding_id: FI-08
capability_name: Report export artifact (ZC-15, MG-13/MG-07)
comparison_classification: MICRO-WEAKER (MG-13)
zaman_evidence: src/app/(app)/reports/page.tsx; src/features/reports/actions.ts (downloadReport:90, getAllReportData:457, getFinancialPosition:660-943)
micro_evidence: pages/Statement.tsx; application/finance/statementService.ts (period statement with source links); application/finance/projectFinancialService.ts (insights: work-name profitability, coverage, liquidity)
financial_and_data_effect: Zman: pure read → Markdown; P&L export reuses computeCashBasisPnl (LOCKED-6-safe). Micro: same pattern possible — pure read of StatementReading; zero writes; no stores; no schema/export bump.
transfer_recommendation: adapt
micro_destination: مالي (Finance) → /finance/statement export action (+ optional work-name profitability export from insights)
micro_contract:
  record shape: none (read-only). Export action composes Markdown/text from the existing StatementReading + position facts; UTF-8 BOM blob; filename micro-statement-YYYY-MM-DD.md; offline-safe (pure local).
  content rules: every money line carries its knowledge state; resultMinor null exports as «غير متاح — بيانات ناقصة» with reasons (never 0); amanah wording preserved («كاش موجود، ليس مالك ولا ربحك»); corrections digest included (count + net effect or null); NO "صافي الربح النهائي" wording; NO balance-sheet equation/balance claim — a position summary section lists components with the qualifier «قراءة مكوّنات، لا ميزانية محاسبية».
  idempotency: n/a (read + blob download).
  migration: none — stays outside schema 30 / export 22.
priority: P1
confidence: high
risks: wording drift violating the bounded-profit boundary (highest-signal risk); hand-editing exports mistaken for records (header must state generated-at + period + "قراءة من السجل المحلي").
open_questions: Markdown vs plain text vs future PDF (documents pipeline); whether insights export is included in v1 (recommend: statement only first, per one-slice rule).
```

### FI-09 — Receivables as asset-not-expense / loans out (ZC-11)

**Zman trace.** `receivable` + `receivable_payment` tables; loan = cash out (sourceType `receivable`) + receivable row; payment = cash in (`receivable_payment`); remaining computed read-time (never stored); **never enters P&L** (separate tables); balance-sheet asset; IC-15 reconciles ledger vs tables; owner wording: «لا يُخصم من ربحك — مالك ما زال لك، لكن عند غيرك».

**Micro mapping.** For **business debts** the principle is fully enforced: order `debt` settlement status + direct-sale `partial_debt` + parties ledger; collect flows with correct source; debt ≠ cash boundary (current-state.md §4). For **loans made from project cash** (Zman's "دَين لشخص" mode): Micro has **no event type** — `owner_withdrawal_cash` would wrongly reduce owner capital; `operating_expense_*` would wrongly reduce profit; `amanah_*` is the mirror (money held for others, owed by me — not money owed to me). A loan-out would need a sixth delta dimension (receivableDelta) — a schema-level event-type decision. Micro's no-new-financial-slices rule (current-state.md §5) means this must not be added as part of a Zman transfer; it requires an independent scope decision + contract if the persona needs it.

```
finding_id: FI-09
capability_name: Receivables/loans as asset-not-expense (ZC-11, MG-17-adjacent)
comparison_classification: MICRO-SUFFICIENT for business debts (MG-17); ZAMAN-ONLY for cash loans made
zaman_evidence: finance/db.ts:68-69 (receivable, receivable_payment); finance/actions.ts:3710-4125 (create/delete receivable + payments); integrityCheck.ts:1420-1489 (IC-15); PROMPT_RECEIVABLES.md
micro_evidence: craft-order SettlementStatus debt; direct-sale partial_debt (direct-sale/types.ts:33); application/parties/partyLedgerService.ts (per-party net); Collect.tsx single collection sheet; financial-event types (no loan-out type); current-state.md §4 debt ≠ cash; §5 no new slices
financial_and_data_effect: Zman: loan = cash out, asset up, profit untouched; payment reverses both; IC-15 guards. Micro: business debt already honest (asset-like reading via parties ledger, never profit); cash loans out currently unrepresentable.
transfer_recommendation: reject (now) — the truth principle is already Micro's; the loan-out slice needs a new event type + delta dimension, i.e. an independent contract, not a transfer
micro_destination: n/a now; future (if owner decides): FinancialEventType "loan_out_cash" + receivableDeltaMinor dimension, parties-ledger reading, reversal via existing correction model
micro_contract: N/A — rejected now. If ever built: mirror-image of amanah (cash −1, receivable +1, profit/owner untouched), repayment = cash +1 / receivable −1 with linkage, reversal through documented corrections, schema + export major bump with `?? 0` legacy default (amanahDelta precedent).
priority: P2
confidence: high (classification); medium (persona need for loan-out — INFERENCE: home-business owners do lend cash, Zman's owner did)
risks: recording a loan as owner_withdrawal or expense today corrupts owner capital / profit truth — worth a FinancialEventEditor hint (wording only, no new type).
open_questions: does the Pilot persona need loan tracking? (owner decision; note QuickActionSheet's «عربون أو تحصيل» covers collections, not loans).
```

### FI-10 — Duplicate-event / idempotency model comparison

**Zman.** Server actions: `idempotency_key` table (requestId PK) checked + inserted inside the write transaction; `SELECT ... FOR UPDATE` row locks; per-IP rate limiting (`checkRateLimit`, "تجاوزت الحد المسموح"); form-level `inFlight` ref; delete-with-undo 5s; audit **after** commit (a crash between commit and audit = missing audit row, accepted). **Key generated per submit attempt** (`crypto.randomUUID()` inside the handler, `SmartFinanceForm.tsx:537,615,697,749`) — protects double-click, not retry-after-ambiguous-failure: a user who re-submits after a timeout can create a duplicate expense/purchase (server-side DB constraints and unique partial index on converted sales stop only the worst classes). `INFERENCE`: Zman has no user-facing "did my last write land?" reconciliation beyond list refresh.

**Micro.** Local-first: no network retry storms by construction. Records carry `idempotencyKey`/`operationKey`; unique indexes (`IndexedDbLocalStore.ts:209` etc.); atomic multi-store `commit*` transactions with in-transaction reuse checks returning `reused:true`; application services do pre-read key-collision detection with Arabic errors (`projectFinancialService.ts:805-818`); editors generate the key **once per form instance** (`FinancialEventEditor.tsx:126` useRef) so in-form retries reuse the key; fulfillment paths accept caller-supplied root keys so retries after interruption don't double-collect (S2-02, `fulfillmentService.ts:131-135,163-175`). IndexedDB transactions are atomic and serialized — reload during a write either completes or rolls back; cross-tab consistency via BroadcastChannel; import is atomic replace.

**Comparison verdict:** Micro's model is structurally stronger for its environment (per-intent keys + unique indexes + atomic local transactions vs Zman's per-attempt keys + network failure window). No transfer needed; two Zman lessons worth recording: (a) per-intent (not per-attempt) idempotency keys — Micro already does this, keep it as a review rule; (b) rate limiting is an online-only concern, not portable.

```
finding_id: FI-10
capability_name: Duplicate-event / idempotency risk model (cross-cutting, candidates set item 10)
comparison_classification: n/a (analysis; MICRO-SUFFICIENT with noted residual risks)
zaman_evidence: finance/actions.ts (idempotency_key in-tx pattern: 158-176, 701-717, 1441-1526); SmartFinanceForm.tsx:254,488,537 (inFlight + per-attempt UUID); lib/ratelimit.ts; audit outside tx (actions.ts:300-308)
micro_evidence: IndexedDbLocalStore.ts:209,239-323 (unique idempotency/operation indexes), 740-869 (in-tx reuse + atomic coupled reversal); projectFinancialService.ts:791-875 (pre-read collision + reuse semantics); FinancialEventEditor.tsx:126 (per-intent key); fulfillmentService.ts:131-135 (S2-02 retry-safe keys); pwa/register.ts (offline-first)
financial_and_data_effect: Zman: server transactions + idempotency keys + row locks; residual duplicate window on retry-after-timeout (per-attempt key). Micro: per-intent keys + unique indexes + atomic local transactions + reuse results; residual risks: (1) multi-tab simultaneous same-key writes → second write fails on unique index (honest error, no duplicate); (2) UI double-tap on slow devices before state update → same-key second commit returns reused/unique-violation; both safe.
transfer_recommendation: direct — no transfer required; adopt Zman's per-intent-key rule as a Micro review invariant (already satisfied)
micro_destination: n/a
micro_contract: N/A — guardrails only: keep per-intent key generation (useRef) in every new editor; keep unique indexes on every new keyed store; keep atomic commit* for every coupled write; error copy for unique-violation must be Arabic and actionable («مفتاح العملية مستخدم…»).
priority: P2
confidence: high
risks: new surfaces (e.g. FI-01 category store) forgetting unique index or per-intent keys; multi-tab writes surfacing raw IndexedDB errors instead of Arabic messages.
open_questions: none material.
```

---

## 4. Integrity check suite mapping (IC-1..IC-16 → Micro)

Legend: **structural** = Micro enforces by construction at write time; **import-time** = verified by `localTransferService` import validation; **needed** = new read-only runtime check (FI-04 suite); **N/A** = meaningless in Micro's model today.

| IC | Zman invariant (title, severity) | Micro status | Micro equivalent / needed check |
|---|---|---|---|
| IC-1 | Equity drift = assets − liabilities − equity = 0 («توازن الميزانية», FAIL) | N/A as equation; **needed** as cross-read-model | Micro has no accounting equation; the analogous risk is read models disagreeing. MIC-1/MIC-2: recompute position + period result from stores and compare across surfaces (Home facts / Finance position / Statement). |
| IC-2 | No orphan cash movements (movement without live source row; FAIL) | **import-time** + **needed** | sourceRef{Id,Kind,LineId} on allocations is optional (no FK). MIC-4: allocation sourceRefs reference existing records; reuse import-verifier relations at runtime. |
| IC-3 | Deposit liability ↔ exactly one live deposit-in movement (FAIL) | **structural (partial)** + **needed** | Deposit collection is an event-logged order operation (no ledger pair). MIC-5/MIC-6: collectedMinor == Σ active collection events; cancelled_pending deposit decisions surfaced as WARN. |
| IC-4 | No deposit double-count in order sales (FAIL) | **structural** | F-005 revenue-once at `delivered` on the order; unique event keys; collectRemaining caps at receivable. Check optional: delivered order recognized values == agreed price after revisions. |
| IC-5 | No archived account with non-zero balance (FAIL) | **N/A** | Micro wallets have no archive/delete path (wallets are created; entries append). No check needed until archiving exists. |
| IC-6 | Cash-basis P&L == retained + deposits liability (FAIL) | **needed** | No retained-profit construct; analogous = statement result/cash lines vs canonical period result + position. Part of MIC-1/MIC-2. |
| IC-7 | Money-unit consistency; no unexplained negative account balances (WARN) | **structural (inventory)** + **needed (cash)** | Inventory non-negative is enforced at write (`assertInventoryRemainsNonNegative`); import validates. Wallet balances can technically go negative via adjustments → MIC-7-adjacent WARN check (negative wallet balances listed). |
| IC-8 | Cash ledger ↔ source tables reconciliation, write-offs excluded (FAIL) | **needed** | MIC-5: order/sale collections vs cash allocations with sourceRef line totals; direct-sale collected vs its allocations. |
| IC-9 | Sale amount == order realized revenue (FAIL) | **structural** | `transitionOrder` sets recognizedRevenue = agreedPrice (revisions preserve history); domain-enforced. Optional consistency read in MIC-5. |
| IC-10 | Owner transaction amount == cash movement (FAIL) | **structural** | `commitOwnerMovement` writes owner movement + cash entry atomically (`IndexedDbLocalStore.ts:1867-1947`). Optional: summarizeFinancialEvents ownerCapital vs owner movements store. |
| IC-11 | Opening balance row ↔ opening cash movements (FAIL) | **structural (stronger)** | Opening known/unknown per wallet; unknown never zero; opening-later completion is a documented event (D-004); guided import validates. Check candidate: wallets still `unknown` after N entries → info/WARN. |
| IC-12 | Inventory ledger: no orphaned movements (FAIL); negative balances (WARN); real book value | **structural** + **needed (refs)** | Non-negative enforced at write; reversal movements documented. MIC-8: reversal refs valid & single-use; consumption/waste orderId/purchaseId exist (activeInventoryMovements relations). |
| IC-13 | LOCKED-6: all profit surfaces match, month + all-time (FAIL) | **needed (top gap)** | No runtime equivalent; multiple read models exist. MIC-1 (FI-03): period result cross-surface drift = FAIL. |
| IC-14 | Capital asset valuation; orphans FAIL; fully-depreciated WARN | **N/A (now)** | No assets (deferred behind contract, FI-06). Future MIC for the asset register if built. |
| IC-15 | Receivables ledger ↔ tables (FAIL) | **needed (adapted)** | Business debts: parties ledger is a derived read model — MIC-5/IC-15-analog: per-party net recomputation == source records; collection events sum == order collected. |
| IC-16 | Deposit forfeit settlement completeness (FAIL) | **structural (different)** | Micro never auto-forfeits; cancel sets needs_review and waits for an explicit decision — the "incomplete settlement" state Zman detects is prevented by gating. MIC-6 keeps lingering `cancelled_pending` visible as WARN. |

**Headline:** of 16 Zman checks, Micro **structurally enforces 7 at write time** (IC-3 partial, IC-4, IC-7-inventory, IC-9, IC-10, IC-12-core, IC-16 via gating) and covers relation integrity **at import time**; **7 require new read-only runtime checks** (IC-1, IC-2, IC-6, IC-8, IC-13, IC-15 + the cash-negative half of IC-7) — all map into the proposed MIC-1..MIC-9 suite (FI-04); **2 are structurally N/A today** (IC-5 no archiving; IC-14 no assets).

---

## 5. Rejected transfers — financial-truth reasons

1. **FI-02 — auto-deduct inventory on delivery (ZC-07 core).** Would create inventory effects from order cost **estimates** (violates: "estimates must not silently create financial or inventory effects"); bypasses Micro's consumption-evidence boundary; negative-stock tolerance breaks Micro's non-negative inventory invariant; zero-cost opening stock converts unknowns into zeros. Optional selection and immutable written cost already exist in Micro.
2. **FI-05 — order→sale conversion, deposit reclassification, forfeit-as-revenue (ZC-06).** Cash-event **reclassification** violates Micro's append-only correction model (originals preserved, corrections are new records); a converted-sale record would create a **second revenue path** next to order-embedded recognition (double-booking risk; single-write-path violation); automatic forfeit-as-revenue violates collection≠profit and the no-guessing rule for retained-deposit accounting.
3. **FI-09 — loan-out receivables slice (ZC-11, now).** No Micro event type carries it; forcing it through `owner_withdrawal` or `operating_expense` would corrupt owner capital or profit truth; a sixth delta dimension is an independent contract decision, not a transfer.
4. **Sub-rejection (FI-07): ZC-18's immutable write-off.** No-reverse, edit/delete-guarded records would violate Micro's traceable-corrections rule. Micro's reversible waste/loss design is retained.
5. **Sub-rejection (FI-02): untrack-with-soft-delete of movement history.** Destructive history suppression conflicts with Micro's append-only movement ledger (reversals instead of deletes).

Not re-litigated here (already rejected in Round 1 with financial-truth agreement): dashboard panels (MG-15), auth/idle-lock (MG-16/21), WhatsApp automation (MG-19).

---

## 6. Migration & compatibility register

| Finding | Schema impact | Export/import impact | Backfill | Lockstep updates required |
|---|---|---|---|---|
| FI-01 category label | `expenseContext.categoryLabel?` → schema **30→31** | export **22→23**; import accepts 22/30 and older → default `null` (precedent: `amanahDeltaMinor ?? 0` migration + schema29 round-trip test) | none — legacy null = unclassified, already surfaced (`legacyUnclassifiedExpenseCount`) | `normalizeExpenseContext` assertions; `validateSnapshot`; public-surface test; new UI test |
| FI-03 single result function | none | none | none | statementService/Finance tests; optional refactor PR |
| FI-04 integrity suite | none (read-only service + page) | none | none | one-slice PR per Micro's group rule (contract first) |
| FI-08 statement export | none (stays outside schema/export versions) | none | none | wording review vs bounded-profit boundary |
| FI-06 assets (gated future) | new store(s) + domain module → major schema bump | export bump + migration (absent store = empty register) | optional historical asset entry | specialized contract first (remaining-capabilities-review), disposal/restatement policy |
| FI-09 loan-out (gated future) | new FinancialEventType + `receivableDeltaMinor` sixth dimension | export bump; legacy events default 0 | none | delta table, summarizeFinancialEvents, statement lines, import validation |
| FI-07 / FI-10 | none | none | none | guardrail notes only |

Compatibility constraints honored by all accepted contracts: single write path (UI → application service → domain → store); atomic coupled corrections via `commit*`; per-intent idempotency keys; migration accepts older export versions; no silent rewrite of history; estimates never create effects; missing never zero.

---

## 7. Evidence index

**Zman (`artifacts/zman-app/` unless noted):**
- `src/features/finance/pnl.ts` — LOCKED-6 computeOperatingPnl (full read)
- `src/features/finance/integrityCheck.ts` — IC-1..IC-16 (read: 1-140, 255-394, 444-573, 665-769, 1240-1405, 1500-1608 + grep enumeration)
- `src/features/finance/actions.ts` — createPurchase 136-316, createExpense 678-783, convertOrderToSale 1441-1638, reverseSale 1650+, forfeitDeposit 2020-2232, category CRUD 2560-2790 (read)
- `src/features/finance/queries.ts` — getExpenseCategories 736, getDistinctExpenseCategories 902, receivables 741+
- `src/features/inventory/actions.ts` — addCatalogMovement, deductForDelivery 196-368, restoreForReverse 385-414, adjustStock 431-583 (read)
- `src/features/depreciation/queries.ts` — getDepreciationForPeriodCents 83-127, valuation 129-160 (read)
- `src/features/reports/actions.ts` — getFinancialPosition (grep + 778-943), report grouping 234-341
- `src/features/finance/components/SmartFinanceForm.tsx` — inFlight 254/488, per-attempt UUID 537/615/697/749 (grep)
- `docs/ACCOUNTING_RULES.md` — §0/§1 (from SA-1), §9 INV-20..25 read in full (166-230), §10 header
- Migrations 0005/0014/0019/0020/0023/0024/0025/0027 (names verified via SA-1; roles cited from ACCOUNTING_RULES)

**Micro:**
- `src/domain/financial-event/types.ts` + `policies.ts` (full reads — delta table, corrections, shared-share rules)
- `src/domain/craft-order/types.ts` (full) + `policies.ts` (368-482, 783-892: transitions, recognition, deposit settlement; grep index)
- `src/domain/inventory-material/types.ts` + `policies.ts` (full reads)
- `src/domain/cash-continuity/types.ts` (full read)
- `src/domain/direct-sale/types.ts`, `src/domain/supplier-purchase/types.ts` (full reads)
- `apps/prototype-web/client/src/storage/local/types.ts` — LocalStoreSnapshot, PrototypeLocalStore commit methods, schema 30/export 22 (222-405)
- `apps/prototype-web/client/src/storage/local/IndexedDbLocalStore.ts` — 26 object stores, unique idempotency indexes, atomic commit* transactions (grep + 740-869 refs)
- `apps/prototype-web/client/src/application/finance/projectFinancialService.ts` — derivePeriodCogs 232-301, readRecordedPeriodResult 433-639, reverse 791-875, distributeUnallocated 878+
- `apps/prototype-web/client/src/application/finance/correctionHistoryService.ts` (1-70)
- `apps/prototype-web/client/src/application/finance/statementService.ts` (grep refs)
- `apps/prototype-web/client/src/application/fulfillment/fulfillmentService.ts` (full read)
- `apps/prototype-web/client/src/application/collections/collectionService.ts` (grep refs)
- `apps/prototype-web/client/src/application/transfers/localTransferService.ts` — version chain 1938-1960, atomic replace 2131-2144 (grep + reads)
- `apps/prototype-web/client/src/pages/FinancialEventEditor.tsx` — per-intent key (grep, line 126)
- `docs/operations/current-state.md`, `docs/product/financial-operating-model-v1.md`, `docs/decisions/remaining-capabilities-review-v1.md` (grep-verified citations)

**Round-1 reports consumed:** `subagents/01-zman-capability-map.md` (ZC-01..ZC-24), `subagents/02-micro-gap-comparison.md` (MG-01..MG-21) — both under `/home/z/my-project/documents-repo/reports/2026/2026-09-03/zaman-to-micro-gap-analysis-001/`.

---

*End of SA-4 report. Built entirely from read-only inspection of zman-app @ bdd63ab and Micro @ 4db6a5f. Both product repos untouched; only this report file and the worklog entry were written.*
