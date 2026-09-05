# SA-4 — Financial Adaptation Audit (Zman → Micro)

- **Date:** 2026-09-05
- **Task ID:** 5-b (Group 6 / Agent 2, Specialist Agent 4)
- **Revisions:** v1 (initial issue)
- **Read-only statement:** This audit modified **no repository file**. Both baselines were read in place: Zman @ `bdd63ab` (`/home/z/my-project/repos/zman-app`, app in `artifacts/zman-app/`) and Micro @ `1242aa62b3f81e8db263f4220bcefd3c8827d307` (`/home/z/my-project/repos/Micro`, app in `apps/prototype-web/client/`, domain in `src/domain/*/`). The only files written are this report and the worklog append.

---

## 1. Methodology

1. Fixed both baselines (commits above) and read each side's financial constitution first: Zman `artifacts/zman-app/ACCOUNTING_RULES.md` (deposit settlement cycle) + `docs/ACCOUNTING_RULES.md`; Micro `docs/contracts/05-financial-p0-policies.md`, `docs/contracts/25-network-money-representation-contract.md`, `docs/contracts/29-group4-deep-finance-contract.md` (referenced).
2. For each of the 14 capabilities, extracted the **writer path** (what creates/changes money records) and the **reader path** (what the profit/balance numbers are derived from) on both sides, with file:line evidence.
3. Audited Micro against all 14 financial safety rules from the continuation prompt §8, treating Zman behavior as "user value to preserve" and Micro's truth model as the constraint — never the reverse.
4. Where Zman behavior conflicts with a Micro financial contract, the item is classified **NEEDS_OWNER_DECISION** with alternatives, per audit instructions.
5. Cross-verified Agent 1's merged fixes (FT-01, FT-02, DP-01, DP-09) in the current tree rather than trusting the worklog claims.

Path shorthand used below:
- **Z:** `repos/zman-app/artifacts/zman-app/src/`
- **M-domain:** `repos/Micro/src/domain/`
- **M-app:** `repos/Micro/apps/prototype-web/client/src/`

---

## 2. Capability Audits (core)

### C1 — Expense entry semantics

**Zman semantics.** Expense row: category (free text, catalog auto-added), amount, `isCapitalAsset` × `costNature` (fixed/variable), `isInventoryWriteoff` — `Z features/finance/db.ts:108-171`. `createExpense` (`Z features/finance/actions.ts:678-783`) inserts the row plus a `cash_movement` out (744-754) inside one transaction, with idempotency key (701-717) and audit log outside the transaction (767-775). The capital flag only changes P&L bucketing (`operatingExpensesCents` vs `capitalAdditionsCents`, `Z features/finance/pnl.ts:159-173, 271`); the cash movement is identical either way — the money left the box regardless. Category text never creates a movement.

**Micro semantics.** Expense = explicit event kind `operating_expense_cash` / `operating_expense_payable` with a hard-wired effect row in `DELTA_TABLE` (`M-domain financial-event/policies.ts:271-276`): `[-1,0,0,1,0,0,0,0]` (cash↓, expense↑) and `[0,1,0,1,...]` (payable↑). `OperatingExpenseContext` (`M-domain financial-event/types.ts:42-52`) carries `relationship` (project|shared), `behavior` (fixed|variable|mixed|**unknown**), `purpose`, `knowledge` (known|estimated|needs_review), `sharedProjectShare` (basis + allocated/unallocated), and `categoryLabel` — normalized and frozen at creation (`policies.ts:153-197, 142-152`). An unallocated shared expense contributes **0** to the period result until a share is declared (`policies.ts:313-316`), and is surfaced as reason "حصة غير موزعة" (`M-app application/finance/projectFinancialService.ts:644`). The context can never change deltas — the effect is a function of `type` only (`policies.ts:304-329`). Capital spending is not an expense flag but a different kind (`asset_purchase_cash/payable`, `policies.ts:285-287`) chosen at entry with an effect preview (`M-app components/presentation/EventEffectPreview.tsx`).

**Value preserved?** Yes, with a stronger question set. Cash-out + description + grouping label survive (`categoryLabel` end-to-end trace verified by SA-2). `behavior` covers Zman's `costNature` (and adds mixed/unknown); `knowledge` and `sharedProjectShare` are truth questions Zman never asked (Zman has no project/shared concept at all — SA-1 code-verified negative). Micro also adds payable-expense + settlement (Zman expenses are cash-only). Zman's category *catalog management* (rename/merge via `Z features/finance/actions.ts:2607-2790`) has no Micro equivalent — labels are frozen and corrected by reversal+replacement only.

**Micro truth-model compliance:** **PASS.** Classification is provably non-financial (delta keyed by type); "unknown" never renders as 0 (behavior=unknown is legal; unknown cost ⇒ `resultMinor = null`, `projectFinancialService.ts:690-692`; MIC-9 enforces the biconditional `resultIsNull ⟺ unknownDeclared`, `M-app application/finance/integrityCheckService.ts:519-532`).

**Verdict: ADAPT** — same user value, deeper truth questions; category rename/merge is the one lost Zman convenience (finding F-5).

---

### C2 — Purchase / inventory

**Zman semantics.** `createPurchase` (`Z features/finance/actions.ts:136-318`) always books the cash-out (250-260) and, if linked to a tracked catalog item, automatically inserts a `catalog_movement` `in` with `unitCostCents = floor(total/qty)` (262-306; high-precision 6-decimal unit cost on the row, `Z features/finance/db.ts:34-42`). COGS is computed **at sale time** as an immutable weighted average stored on the movement (`Z features/inventory/actions.ts:272-311`), with the A4 residual book-value sweep when stock hits zero (334-336). **Negative stock is allowed** with only a note warning (`inventory/actions.ts:267-270`); **zero-cost opening** movements default to cost 0 (documented as "free inventory", `inventory/db.ts:56-73`).

**Micro semantics.** A supplier purchase "changes cash or supplier payable only — never operating expense or period result" (truth string, `M-app application/suppliers/supplierPurchaseService.ts:95-97`). Inventory entry happens only via an **explicit receiving movement** (`purchase_receipt` requires `purchaseId`, `M-domain inventory-material/policies.ts:137-138`; adds must increase both quantity and value, 129-131). Invariants are enforced at write time: `assertInventoryRemainsNonNegative` (quantity **and** value, `policies.ts:227-235`) with an explicit `InventoryShortage` record as the documented alternative to negative balances (238-241). Opening knowledge is explicit: `quantityState` confirmed/unconfirmed, `costState` known/unknown (`types.ts:15-23`, validation `policies.ts:76-93`); value 0 is legal **only** when tagged `costKnowledge:"unknown"` ("declared ambiguous, not free", `policies.ts:122-127`). Consumption value uses pro-rata `roundHalfUp` with Decision-20's "take the remainder as full waste" fallback (`policies.ts:195-214`). Editing a purchase cannot silently strand receipts: received value/quantity floors and a material-link immutability guard (`supplierPurchaseService.ts:193-233`).

**Micro stricter (good):** non-negative invariant + shortage record; unknown≠zero opening; explicit receiving contract; receipt-aware edit guards; movement values frozen at recording (historical stability).

**Where Micro lost Zman value:** (a) the automatic purchase→inventory linkage and automatic delivery deduction (`deductForDelivery`, `Z features/inventory/actions.ts:196-368`) — in Micro the owner records consumption at delivery review; if skipped, `cogsStatus` degrades to `partial`/`not_available` and the reader falls back to snapshot cost (`derivePeriodCogs`, `projectFinancialService.ts:254-315` — honest, but the "never forget COGS" automation is gone, and MIC-13 only *checks* linkage after the fact, `integrityCheckService.ts:985-989`); (b) 6-decimal purchase unit pricing (Zman `unit_cost_micro_cents`) is impossible in 2-decimal minor units (see C13); (c) negative-stock tolerance replaced by rejection+shortage record (deliberate, stricter).

**Micro truth-model compliance:** **PASS** ("a purchase is not automatically inventory or cost of sale without valid receiving/consumption contract" — contract 28 + `policies.ts:137-143`).

**Verdict: ADAPT** — invariants strictly better; the lost automation is a documented trade (explicit receiving), not a truth violation.

---

### C3 — Waste / write-off

**Zman semantics.** `adjustStock` out with value creates a **shadow expense** `is_inventory_writeoff=true` in the same transaction — non-cash, no `cash_movement` — deducted from `operatingNetCents` (`inventoryWriteOffCents`, `Z features/finance/pnl.ts:224-237, 277`) and from retained profit in the balance (`INV-25`, `Z features/inventory/actions.ts:551-575`). It is immutable — there is no reverse path for a write-off.

**Micro semantics.** Two decoupled, both reasoned paths:
1. **Inventory waste movement** — `type:"waste"` requires a reason and `wasteContext` (`M-domain inventory-material/policies.ts:128-151`); value-only delta (no cash); **reversible** via a mirror `reversal` movement with `reversesMovementId` (`M-app application/inventory/inventoryMaterialService.ts:1154-1185`). The period reader surfaces `generalInventoryWasteMinor` and `unallocatedInventoryCostMinor` as separate declared lines + reasons "هدر عام"/"استهلاك غير موزع" (`projectFinancialService.ts:294-304, 647(cogsReasons)`) — but they are **not subtracted** in `resultMinor` (690-701).
2. **`loss_non_cash` financial event** — manual, reasoned, delta `[0,0,0,1,0,0,0,0]` ("reduces period profit with no cash exit", `policies.ts:282`, `M-app components/presentation/EventEffectPreview.tsx:62`) — this is the path that nets into the recorded result.

**Better?** Reversibility with reason is better correction honesty than Zman's immutable no-reverse (matches the "correction preserves the original and records reason and net effect" rule). **Cash-masquerading risk:** none — waste movements carry no cash delta, and `loss_non_cash` has a zero cash delta by table.

**The conflict:** Zman INV-25 automatically nets waste into profit; Micro contract 05 §3.2.1 defines the recorded result equation (delivered-order revenue − recognized direct cost − operating-expense delta) and deliberately keeps general waste **outside** the number, disclosed as a reason. This is a genuine Zman-vs-Micro-contract conflict → **NEEDS_OWNER_DECISION** (finding F-1). Alternatives: (a) keep disclose-only (current Micro contract — number stays "recorded result", waste visible as reason + `MIC-8`/`MIC-9` surfaces); (b) net general waste and unallocated consumption into `resultMinor` (Zman parity — but changes the meaning of the number and requires a contract amendment, not a code patch); (c) prompt the owner to record `loss_non_cash` when a waste movement with value exists (automation, owner-approved).

**Verdict: ADAPT** (reversibility strictly better) **+ NEEDS_OWNER_DECISION** on netting-vs-disclosure (F-1).

---

### C4 — Orders / deposits

**Zman semantics.** Deposit is a liability: `order.depositCents` backed by a `deposit` cash-in movement (`Z features/orders/db.ts:34-35`; collection in `orders/actions.ts:145-153, 437-476`). Forfeit = **reclassify** the deposit movement `deposit/in → sale/in` + create a `source='manual'` sale for the retained remainder only; no new cash (ACCOUNTING_RULES.md rule 4; `Z features/finance/actions.ts:2097-2186`). Refund = separate `deposit/out` movement, liability reduced (rule 2-3; `refundOrder` 1787+). Reverse-forfeit restores liability without cash (rule 8). Guarded by IC-3/IC-16.

**Micro semantics.** `collectDeposit` raises `depositCollectedMinor`/`collectedMinor` with **no revenue** and a cap at the agreed price (`M-domain craft-order/policies.ts:516-547`). Cancel sets `depositSettlement:"needs_review"` — a valid pending state, not an error (`cancelOrder`, `policies.ts:874-884`). Settlement is three-way: refund (`settleDepositRefund` 947-963 — reduces `collectedMinor`; the cash model nets the collection), retain (`settleDepositRetain` 965-981 — cash stays, `retainedMeaning` pending), and pending (safe default). Retained deposits get an **explicit classification event** — `deposit_retained_revenue` (revenueDelta only) or `deposit_retained_owner` (ownerCapitalDelta only), both with **zero cash delta** (`policies.ts:299-301`) — written atomically with the order (`M-app application/finance/retainedDepositService.ts:84-122`). Reclassification = mirror reversal + replacement, both documented (124-187). Pending retained deposits are surfaced in the position (`pendingRetainedDepositsMinor`, `projectFinancialService.ts:393-402`) and in MIC-14's detail (`integrityCheckService.ts:1004-1021`); MIC-12 guards classification integrity (905-915).

**No double-count, no early revenue:** revenue for a cancelled order exists only via the single classification event per order (`classificationEventId` picks the latest active, duplicates rejected — `retainedDepositService.ts:39-55, 95-96`); a never-delivered order has `recognizedRevenueMinor = 0`; the deposit cash entered once at collection. Verified: no path books revenue before the explicit decision — Zman books forfeit revenue **at forfeit time**, Micro defers to the owner's classification, which is *stricter* than Zman on the "deposit is not revenue until its explicit meaning requires it" rule.

**Value preserved?** Yes — liability-before-settlement, refund, retain, reverse all present; Micro adds the pending state and the owner/revenue meaning split (Zman forfeit is revenue-only; Micro can also declare it owner money).

**Micro truth-model compliance:** **PASS.**

**Verdict: ADAPT** (strictly safer: pending default + explicit meaning split; refunds net the cash ledger instead of Zman's gross in+out pair — see F-6).

---

### C5 — Order→sale conversion

**Zman semantics.** `convertOrderToSale` (`Z features/finance/actions.ts:1441-1638`): sale = full realized revenue (totalPrice + additionalProfit, 1528-1541); the collected deposit movement is **transformed** `deposit→sale` (reclassify, not double-post — 1549-1576); the **remainder is inserted as a cash-in at delivery** (1578-1595) whether or not it was actually collected. (The task brief's "INV-4: sale posts max(0, amount−deposit)" is documentation drift — the sale posts the *full* amount; the netting happens in the cash movements: transformed deposit + remainder = realized. See F-9.)

**Micro semantics.** Delivery (`transitionOrder` → delivered, `M-domain craft-order/policies.ts:385-466`) recognizes `recognizedRevenueMinor = agreedPriceMinor` once (423-438), with `resultStatus` gated on cost knowledge; the remainder stays `receivableMinor` until `collectRemaining` (549-587, requires delivered + amount ≤ remaining) or `registerDebt` (594-620). Period attribution uses the **last effective (non-reversed) delivery event** via `lastEffectiveDeliveryEvent` (`M-app application/fulfillment/deliveryAttribution.ts:16-26`, used at `projectFinancialService.ts:546-553`) — Agent 1's FT-01, verified in tree. Direct sales: revenue recognized at `occurredOn` once (F-005 comment, `projectFinancialService.ts:534-539`); cash = `collectedMinor` only; partial debt → receivable; **cancel** = documented revision + FT-02 mirror reversal of wallet allocations with deterministic keys (`M-app application/direct-sales/directSaleService.ts:168-223, 225-270` — ids `sale-cancel:${entry.id}`, operation keys `sale-cancel:${sale.id}:${entry.id}`, already-reversed filtering) — verified idempotent.

**Revenue-timing honesty, both sides:** Zman recognizes revenue at delivery (honest timing) but **fabricates cash** for the uncollected remainder at the same moment (weaker — SA-2 P1 corroborates). Micro recognizes revenue at delivery (same timing) and never fabricates cash: cash enters only on collection events, receivables are tracked, and a cancelled direct sale's wallet allocations are restored to unallocated by mirror reversal. Both are honest on revenue timing; only Micro is honest on cash.

**Micro truth-model compliance:** **PASS.**

**Verdict: ADAPT** (Micro's split is the compliant direction; do **not** port Zman's remainder-as-cash-in).

---

### C6 — Credit / receivables

**Zman semantics.** Order remainders: cash-in at delivery (see C5 — the weak path). Person debts: `receivable` = loan-out as cash movement `out` (`Z features/finance/actions.ts:3774-3783`), repayments cash `in` capped at remaining (3976-3999) — never profit (source types `receivable`/`receivable_payment` are excluded from `computeOperatingPnl` sums, `pnl.ts:134-200`).

**Micro semantics.** Debt exists only when explicitly registered after delivery (`isRegisteredCustomerDebt`, `M-domain craft-order/policies.ts:589-592`; `registerDebt` requires delivered + remainder > 0, 594-620). `collectRegisteredDebt` reduces the debt, never re-recognizes revenue (625-654). The collection sheet routes writes through the owning service only (`M-app application/collections/collectionService.ts:139-233`) with explicit wallet-or-unallocated destination and an honest failure mode when attribution fails (money stays unallocated + notice, 213-218). Delivery+collection can never fabricate cash: `collectRemaining`/`collectFromSheet` require `status === "delivered"` and cap at `receivableMinor` (`policies.ts:558-564`; `fulfillmentService.ts:219-231`); `transitionOrder` forbids `settled` with remainder unless debt is registered (394-396). Position surfaces `customerReceivablesMinor` (registered debt + direct-sale partial debt, `projectFinancialService.ts:407`).

**Micro truth-model compliance:** **PASS** — the delivery+collection flow cannot mint cash.

**Value preserved / gained:** Micro is strictly stronger than Zman's order-side model (Zman's remainder fabrication is the capability *not* transferred — correctly). Zman's person-debt feature maps to loans (C8).

**Verdict: ADOPT.**

---

### C7 — Assets / depreciation

**Zman semantics.** Read-time computed: `monthlyDepreciationCents = floor(amount/life)` stored on the row (`Z features/depreciation/actions.ts:137-142`), period-aware formula `(min(monthsAtEnd,life) − min(monthsAtStart,life)) × monthly` (`Z features/depreciation/queries.ts:83-127`), last-month sweep charges the remainder so book value hits exactly 0 (D13, `queries.ts:185-205`), never any cash movement (INV-22, `depreciation/db.ts` header). **Retroactive by design:** editing life/start recalculates all history at read time (`depreciation/actions.ts:244-249` comment).

**Micro semantics.** Event-sourced: acquisition (`asset_purchase_cash/payable`, assetDelta +amount, `M-domain financial-event/policies.ts:285-287`), monthly = `floorRatio(amount, life)` (`M-domain asset/policies.ts:133-135`), full-life sweep at `elapsed ≥ life` (163-171), **unknown life / unknown start are legal states** that stop depreciation proposals instead of defaulting to zero (`planAssetDepreciation` readiness, 204-238; surfaced as `hasUnknownLife/hasUnknownStart` in `M-app application/assets/assetService.ts:121-123`). Depreciation is a **proposed read-only number until the owner records an explicit `asset_depreciation` event** (`assetService.ts:284-321`, idempotency key `${assetId}:dep:${asOf}`); reversal is reasoned and single-shot (323-355); acquisition correction = mirror reversal + replacement preserving the original (220-282); disposal freezes book value in the event context (357-400, `policies.ts:261-276`); write-off (402-444). No cash from depreciation ever (`DELTA_TABLE` row `asset_depreciation: [0,0,0,0,0,-1,0,0]`, `policies.ts:289`). Period attribution = the event's `occurredOn` (owner-chosen `asOf`), read at `projectFinancialService.ts:627-629`.

**Compliance:** **PASS** on all four audit points — no cash from depreciation (delta table), correction preserves the original (mirror + reason), period attribution explicit, and **cost snapshots are historically stable** (recorded events are immutable; `reviseAssetContract` changes future proposals only). Note: Zman's retroactive read-time recost *would violate* Micro's no-retroactive-recost rule — it was correctly **not** transferred.

**Value trade:** Zman never forgets depreciation (auto-netted at read); Micro requires per-asset manual recording — the unrecorded proposal is displayed (`unrecordedDepreciationMinor`, `assetService.ts:123`) but does **not** enter the period result or its reasons until recorded (finding F-3).

**Verdict: ADAPT** (explicit events over read-time computation — compliant direction; manual-recording gap disclosed).

---

### C8 — Loans

**Zman semantics.** `receivable` = loan out as cash-out, never an expense (`Z features/finance/db.ts:414-451`); repayment cash-in, never revenue (`actions.ts:4014-4023`); IC-15 cross-checks movements vs records.

**Micro semantics.** Dedicated layer: `loan_outgoing_cash: [-1,0,0,0,0,0,1,0]` (cash↓, loan outstanding↑ — not expense, not withdrawal) and `loan_repayment_cash: [1,0,0,0,0,0,-1,0]` (not revenue) (`M-domain financial-event/policies.ts:294-297`). `loanContext` is mandatory for loan kinds and forbidden elsewhere (259-261). `M-app application/loans/loanService.ts`: create (97-129), repayment (131-165), repayment reversal (167-201, mirror), principal correction = mirror + replacement with a no-op-change rejection guard (203-264). MIC-11 checks loan integrity including orphan/restore semantics (`integrityCheckService.ts:845-915`).

**Micro truth-model compliance:** **PASS** — loan-out is not an expense or owner withdrawal; repayment is not revenue, both by construction in the delta table and guarded by MIC-16's owner-type separation.

**Value preserved:** Yes — same user capability (track money lent out and repayments), plus corrections, contexts, and the outstanding-loan layer in the position (`loansOutstandingMinor`, `projectFinancialService.ts:421`).

**Verdict: ADOPT.**

---

### C9 — Period reading

**Zman semantics.** LOCKED-6: one function `computeOperatingPnl` (`Z features/finance/pnl.ts:122-290`) feeds dashboard, reports and monthly profit; IC-13 cross-checks the three public entry points in two windows (current month + all-time, catching period-scaling bugs) at runtime (`Z features/finance/integrityCheck.ts:1209-1323`).

**Micro semantics.** Canonical reader `readRecordedPeriodResult` (`M-app application/finance/projectFinancialService.ts:455-709`) is the only producer of the period number; `StatementService.read` delegates to it (`statementService.ts:134-152`) and `readFinancialInsights` consumes it (712-714). MIC-1 cross-checks reader vs statement vs insights by JSON equality (`integrityCheckService.ts:165-200`), plus a stamped schema/export version on every report (63-66, 160-161). FT-01's `deliveryAttribution.ts` is used by the reader itself (546-553) — period readers are consistent, as Agent 1 claimed. **Two independent profit numbers?** None found: the only other money-number surfaces are the order-level `profitIndicatorMinor` (explicitly *not* project profit per contract 05 §3.2) and G5 contribution/break-even (a different labeled concept). `resultMinor` is `null` — not 0 — when any direct-sale cost is unknown (690-692), and the status degrades to `incomplete` with machine-listed reasons (639-651).

**Micro truth-model compliance:** **PASS** (single canonical number; null-not-zero; disclosed exclusions).

**Verdict: ADOPT** (LOCKED-6 discipline preserved with an even stricter reader contract).

---

### C10 — Integrity checks (IC-1..16 vs MIC-*)

Zman's 16 read-only checks (`Z features/finance/integrityCheck.ts`, titles at lines 270, 428, 535, 602, 647, 718, 753, 864, 908, 970, 998/1029, 1191, 1315, 1394, 1492, 1598) vs Micro's 13 live checks (`M-app application/finance/integrityCheckService.ts:30-46, 95-146`):

| Zman | Meaning | Micro analog | Status |
|---|---|---|---|
| IC-1 | Equity drift = 0 (balance equation) | By-construction additive layers; MIC-14 warns on negative unallocated cash (`integrityCheckService.ts:996-1032`) | Partial — no single drift=0 equation (see F-4) |
| IC-2 | No orphan cash movements | MIC-4 (event/allocation/source-ref integrity, 433-481) + MIC-8 (movement w/o material/purchase/order, 596-604) | Mapped |
| IC-3 | Deposit consistency | MIC-12 (retained deposit, 905-915) + MIC-14 pending note (1004-1021) | Mapped |
| IC-4 / IC-9 | No deposit double-count in order sales | Structural in Micro (no sale row; revenue once) + MIC-12 once-per-order + MIC-15 key uniqueness | Mapped (by construction) |
| IC-5 | No archived account with non-zero balance | **No analog — Micro wallets cannot be archived** | Lost (corroborates SA-2 P2) |
| IC-6 | Net P&L ↔ balance sheet reconciliation | MIC-1 (period-result consistency) | Partial (by construction otherwise) |
| IC-7 | Money unit / no unexplained negatives | Domain invariants (`assertInventoryRemainsNonNegative`, `assertPositiveMinor`) + MIC-8 | Mapped (write-time, stronger) |
| IC-8 | Cash record ↔ auxiliary tables | MIC-2 (cash & wallet structure, 308-325) + MIC-4 | Mapped |
| IC-10 | Owner tx ↔ cash movement | MIC-16 (owner money separation, 1063-1091) + atomic `commitOwnerMovement` | Mapped (stronger) |
| IC-11 | Opening balance ↔ movements | Wallet `openingStatus` known/unknown + MIC-2 | Mapped (knowledge-typed) |
| IC-12 | Inventory ledger book value | MIC-8 (565-679) | Mapped |
| IC-13 | Profit sources match (LOCKED-6) | MIC-1 | Mapped |
| IC-14 | Capital asset valuation | MIC-10 (741-771) | Mapped |
| IC-15 | Receivable movements ↔ records | MIC-11 (loans) + collection sheet routing | Mapped |
| IC-16 | Forfeit settlement consistency | MIC-12 | Mapped |

Micro reserves MIC-3/5/6 for later groups (documented reservation, `integrityCheckService.ts:7-11, 30-46`) — they are not silently missing.

**Value lost:** IC-5's archived-account-with-balance guard (nothing to guard yet — no archival) and IC-1/IC-6's single equation (replaced by construction + layer sums; the residual risk — a *negative* unallocated — is caught by MIC-14 as WARN). **Value gained:** write-time invariants (Zman checks only after the fact), schema/export stamping, deep links, and knowledge-honesty enforcement (MIC-9) which Zman has no concept of.

**Verdict: ADAPT** (13 live checks, 2 by-construction replacements, 1 genuinely lost).

---

### C11 — Backup / restore

**Zman semantics.** Export-only, partial JSON (accounts, catalog, capital assets, opening balance, last 100 orders) with an explicit "not a restorable copy; no expenses/purchases/sales/cash movements; cannot be imported" disclaimer (`Z components/shared/BackupModal.tsx:28-70, 101-108`).

**Micro semantics.** Envelope v27 (`localExportVersion = 27`, `M-app storage/local/types.ts:44`): sha256 digest over the snapshot + embedded counts + appVersion (`M-app application/transfers/localTransferService.ts:2447-2473`). Import: version-chain gate (2485-2546), **tamper rejection** when digest mismatches (2561-2564), **DP-09** malformed-integrity-block rejection (2554-2560), migration + `validateSnapshot` (2828-2829), **DP-01** embedded-counts validation after migration for current files (2840-2851), verified round-trip export (2881-2894), atomic whole-store `replaceSnapshot` on confirm (2869-2878). **Source links survive:** the snapshot carries cash-continuity entries with `sourceRefId/sourceRefKind/sourceRefLineId` (persisted at `distributeUnallocated`, `projectFinancialService.ts:992-996`), movements with `purchaseId/orderId/saleId`, and events with linked contexts and `correctionOfEventId`; MIC-4 re-validates refs against live records after import. Drafts and the lock secret are deliberately excluded from the snapshot (privacy: the PIN never leaves the device; drafts are transient input, `types.ts:33-36`).

**Micro truth-model compliance:** **PASS** — "all source links and contexts survive export/import/restore" holds for every linked store in the snapshot.

**Verdict: ADOPT** (Micro restores what Zman explicitly could not; tamper/counts/digest all verified in the current tree).

---

### C12 — Drafts / local lock

**Zman semantics.** Server-side auth + `IdleLock` (10-minute visibility-based logout, `Z components/auth/IdleLock.tsx:7-18`); form drafts (ZC-29) are client-side conveniences — no financial event occurs before server-action submit by construction.

**Micro semantics.** `FormDraftService` (contract 36): separate `form-drafts` store **outside** the snapshot, never exported, never a financial event, created only on real input, restored by explicit user action with conflict detection, discarded after final save (`M-app application/drafts/formDraftService.ts:1-14, 43-95`; the financial-event editor draft is inputs-only, `M-app pages/FinancialEventEditor.tsx:123-147`). Local lock (contract 37): PBKDF2-SHA256 120,000 iterations, salted, PIN never stored (`M-app application/security/localLockService.ts:52-66, 129-157`); legacy single-sha256 records are upgraded on first successful unlock (70-84); escalating backoff 3/10/30s actually enforced server-side-of-the-check (102-107, 179-192, 244-258); auto-lock via visibility + last-activity (210-227); disable requires the correct PIN (229-266); destructive data actions additionally gated by `DataActionPinGate` (`M-app components/security/DataActionPinGate.tsx`).

**Micro truth-model compliance:** **PASS** — "a draft creates no financial event before final save" is architectural (drafts live in a store no financial reader touches).

**Privacy parity:** Micro's local lock is *stronger* than Zman's idle logout for a local-first app (slow hash + backoff + PIN-gated destructive actions vs. a 10-minute session logout). Zman's server auth is out of Micro's prototype scope by contract (05 §2).

**Verdict: ADOPT.**

---

### C13 — Money representation (SA-2's finding, verified and detailed)

**Zman semantics.** Integer **fils**, ÷1000, 3 decimals (`Z lib/money.ts:1-2, 15-20, 25-57`); purchases additionally carry 6-decimal micro-cents (`Z features/finance/db.ts:34-42`).

**Micro semantics.** `MoneyMinor` = **qirsh**, ÷100, 2 decimals (`M-domain shared/currency.ts:1-4`; `M-app presentation/formatters.ts:56-58`; parser `M-app application/input/englishNumeric.ts:46-52` — regex `^\d+(\.\d{0,2})?$`, third decimal **rejected**, never silently rounded; contract 25 §2/§4 codifies "1 minor = 1 قرش = 0.01 JOD"). Quantities use milli (÷1000) — a different axis (`numeric.ts:93-100`, `formatters.ts:73-79`).

**Verified in-app consistency:** every ÷1000 in Micro's client applies to quantities or milliseconds (grep-verified across `client/src`); no money path divides by 1000. `MoneyMinor` is a bare `number` with no scale in the type — the unit lives in convention + contract 25 only.

**Risk areas (detailed):**
1. **Cross-app migration (dormant, P1):** no Zman→Micro bridge exists. If one is built naïvely, a Zman value of `1250` (1.250 JOD in fils) read as Micro minor units displays **12.50 JOD — a 10× overstatement**. Any bridge must divide by 10 with an explicit, owner-approved rounding policy. (F-2.)
2. **Ported-formula hazard:** copying Zman money code (`parseJodToFils`, `formatFilsToJod`, `×1000`/`÷1000`) into Micro components silently misplaces value 10×; the inverse (Micro code into Zman) understates 10×. Unit tests with display assertions (`formatters.test.ts`, `cashCountMessages.test.ts:11` "never 1/1000") are the current tripwire.
3. **Precision loss vs Zman:** JOD has 3 official decimals (fils coins circulate). Micro cannot represent sub-qirsh amounts — a 0.125 price is rejected at input (honest refusal, contract 25 §4), where Zman stores 125 fils exactly; Zman's 6-decimal purchase unit costs have no Micro equivalent at all.
4. **Type-level ambiguity:** `MoneyMinor = number` carries no scale; the 10× boundary is invisible to the compiler. A branded type or a unit test enforcing "money never ÷1000" would harden this.

**Micro truth-model compliance:** **PASS internally** (consistent ÷100 everywhere, honest rejection of 3rd decimals). The **boundary** decision (accept 2-decimal money vs Zman's 3-decimal parity; migration rounding) is an owner call.

**Verdict: NEEDS_OWNER_DECISION** — alternatives: (a) keep qirsh (current contract 25; 2 decimals; owner consciously rounds) and mandate an explicit ÷10 conversion if any Zman data is ever migrated; (b) move MoneyMinor to fils (3 decimals) for Zman parity — a contract-25 amendment touching every formatter, parser and test; (c) brand the type (`type MoneyMinor = number & {__qirsh:true}`) to make the unit compiler-visible without changing scale.

---

### C14 — Owner draw / inject

**Zman semantics.** `ownerTransaction` draw/inject + `owner_draw`/`owner_inject` cash movements (`Z features/finance/db.ts:348-383`; `actions.ts:3265-3366`); excluded from profit by construction — `computeOperatingPnl` sums only `sale`/`expense`/`purchase` sources (`pnl.ts:134-200`); IC-10 cross-checks amounts.

**Micro semantics.** `owner_investment_cash: [1,0,1,0,0,0,0,0]` / `owner_withdrawal_cash: [-1,0,-1,0,0,0,0,0]` — owner-capital layer moves with cash, zero expense/revenue (`M-domain financial-event/policies.ts:272-273`). O1 entitlement settlements are guarded against over-draw per record/opening/prior-draw (`M-app application/finance/ownerEntitlementService.ts:790-869`); owner movements commit atomically with their cash entry (870-886); MIC-16 enforces that owner deltas appear only on owner types and that owner types never carry expense/revenue deltas (`integrityCheckService.ts:1063-1091`). **Amanah is a separate layer** (`amanahDeltaMinor`, `policies.ts:278-280`; principle 13, `types.ts:4-9`) with its own MIC-7 read-back and an amanah-over-draw reversal guard (`projectFinancialService.ts:903-914`).

**Micro truth-model compliance:** **PASS** — "owner cash is not amanah cash" and "owner transactions never touch profit" both hold by delta-table construction plus runtime guard.

**Value preserved:** Yes — draw/inject with reason, plus the entitlement/withdrawal editor, opening-balance settlements, and amanah separation, which Zman does not model.

**Verdict: ADOPT.**

---

## 3. Financial-Safety-Rules Compliance Table (Micro, per continuation prompt §8)

| # | Rule | Status | Evidence (Micro) |
|---|---|---|---|
| 1 | unknown is not zero | **PASS** | `resultMinor = null` on unknown cost (`projectFinancialService.ts:690-692`); MIC-9 biconditional (`integrityCheckService.ts:519-532`); unknown-cost movements: value 0 legal only tagged `costKnowledge:"unknown"` (`inventory-material/policies.ts:122-127`); wallet `openingUnknown` display (`walletLedgerService.ts:147`) |
| 2 | classification is not financial effect | **PASS** | `DELTA_TABLE` keyed by type only (`financial-event/policies.ts:271-329`); expenseContext cannot alter deltas; categoryLabel frozen read-only (`types.ts:48-51`); unallocated-shared 0-effect is an explicit, disclosed knowledge decision (`policies.ts:313-316`, reasons at `projectFinancialService.ts:644`) |
| 3 | owner cash is not amanah cash | **PASS** | Separate `ownerCapitalDeltaMinor` vs `amanahDeltaMinor` layers (`types.ts:86-91`); principle 13 (`types.ts:4-9`); MIC-16 + MIC-7; amanah reversal limit guard (`projectFinancialService.ts:903-914`) |
| 4 | deposit = liability until settlement; retained classification explicit | **PASS** | `collectDeposit` no revenue (`craft-order/policies.ts:516-547`); cancel → `needs_review` (874-884); classification event with zero cash delta (`policies.ts:299-301`; `retainedDepositService.ts:84-122`); pending surfaced (`projectFinancialService.ts:393-402`); MIC-12 |
| 5 | loan is not expense or owner withdrawal | **PASS** | `loan_outgoing_cash [-1,0,0,0,0,0,1,0]` (`policies.ts:294-295`); mandatory `loanContext` (259-261); MIC-11; MIC-16 excludes loan kinds from owner types |
| 6 | purchase not automatically inventory/COGS | **PASS** | Supplier truth string (`supplierPurchaseService.ts:95-97`); explicit `purchase_receipt` (`inventory-material/policies.ts:137-138`); MIC-13 consumption linkage; edit guards vs received receipts (`supplierPurchaseService.ts:193-233`) |
| 7 | draft creates no financial event before final save | **PASS** | Drafts in separate non-snapshot store (`formDraftService.ts:1-14`; `storage/local/types.ts:33-36`); editor draft = inputs only (`FinancialEventEditor.tsx:123-147`) |
| 8 | reversal is mirror-only, idempotent | **PASS** | `createFinancialReversal` negates every delta, copies source, records reason (`policies.ts:389-424`); reversal-of-reversal blocked (395-396); already-reversed guards (`projectFinancialService.ts:894-902`); FT-02 deterministic keys (`directSaleService.ts:248-263`) |
| 9 | idempotency key doesn't block legitimate retry after reversal | **PASS** | Attempt-suffixed keys for re-delivery/re-ready after reversal (`fulfillmentService.ts:66-75, 138-146` — D4); value-level key-collision checks return `reused` (e.g. `directSaleService.ts:137-146`). (Zman's single-key table *does* mis-block: `Z finance/actions.ts:1456-1472` returns ok-with-nothing for a re-conversion after `reverseSale` — see F-7; pattern correctly not transferred.) |
| 10 | correction preserves original + reason + net effect | **PASS** | Reversal keeps source note/counterparty/context + `correctionReason` (`policies.ts:397-423`); `editEvent` = reversal + replacement atomically (`projectFinancialService.ts:1016+`); loan/asset corrections mirror+replace (`loanService.ts:203-264`; `assetService.ts:220-282`); `correctionHistoryService` renders net effect |
| 11 | non-cash waste must not masquerade as cash outflow | **PASS** | `loss_non_cash [0,0,0,1,0,0,0,0]` (`policies.ts:282`); waste movements carry value-only deltas (no cash anywhere in inventory layer); MIC-8 zero-value⇔unknown rule (`integrityCheckService.ts:605-609`) |
| 12 | cost snapshot historically stable, no retroactive recost | **PASS** | Recorded events immutable; movement values frozen at recording; `reviseAssetContract`/price revision affect future only (`asset/policies.ts:103-129`; `craft-order/policies.ts:684-708` comment "لا يُمس الماضي"). (Zman's retroactive depreciation was correctly **not** imported.) |
| 13 | no silent negative/positive balance without explicit contract | **PASS** | `assertInventoryRemainsNonNegative` (`inventory-material/policies.ts:227-235`); allocation guards both directions (`projectFinancialService.ts:969-980`); MIC-14 WARN on negative unallocated; collections capped at receivable (`craft-order/policies.ts:562-564`); shortage record = explicit negative alternative (`policies.ts:238-241`) |
| 14 | source links and contexts survive export/import/restore | **PASS** | Snapshot carries sourceRef*/contexts/correction links; import validates structure + digest + counts (`localTransferService.ts:2447-2878`); MIC-4 re-validates refs live; wallet ledger deep links (`walletLedgerService.ts:46-66`) |

**Total: 14/14 PASS, 0 violations, 0 needs-owner-decision at rule level.** (Owner decisions exist at *capability* level: C3 netting, C13 unit/scale — see findings.)

---

## 4. Findings (P0..P3, with harm classification)

- **P0 — none.** No Micro financial-safety rule is violated by any transferred capability.

- **F-1 (P1 — NEEDS_OWNER_DECISION, financial overstatement risk, mitigated).** General inventory waste and unallocated consumption are disclosed (`generalInventoryWasteMinor`, `unallocatedInventoryCostMinor`, reasons "هدر عام"/"استهلاك غير موزع", `projectFinancialService.ts:294-304, 647`) but **not netted** into `resultMinor` (690-701), whereas Zman's INV-25 subtracts write-offs (`Z pnl.ts:277`). Harm: an owner reading only the number overstates profit by the waste amount; mitigation: status degrades to `incomplete` with the reason listed and MIC-9 warns on pending items. Alternatives: keep disclose-only (current contract 05 §3.2.1); amend the contract to net them (Zman parity); or prompt a `loss_non_cash` event when a valued waste movement exists. **Do not patch code before the contract decision.**

- **F-2 (P1 — dormant, catastrophic if triggered).** No Zman→Micro data bridge exists, and the money scale differs 10× (fils ÷1000 vs qirsh ÷100, `Z lib/money.ts:1-2` vs `M-domain shared/currency.ts:1-4`). Harm: any future migration that copies Zman integers into Micro `MoneyMinor` fields overstates every amount 10× (1250 fils → 12.50 JOD). Also: `MoneyMinor` is an unbranded `number`, so the compiler cannot catch the mismatch. Required before any bridge: explicit ÷10 conversion + owner-approved rounding policy + branded-type or test hardening. (Corroborates and details SA-2's P2.)

- **F-3 (P2 — overstatement risk, disclosed elsewhere).** Depreciation must be manually recorded per asset; the unrecorded proposal (`unrecordedDepreciationMinor`, `assetService.ts:123`) is shown on the Assets page but does **not** enter the period result or its reasons until recorded. Harm: profit overstated until the owner acts — unlike Zman's automatic read-time netting. Mitigation: proposal is visible and per-asset; recorded depreciation nets correctly (`projectFinancialService.ts:627-629, 698`).

- **F-4 (P2 — coverage gap).** MIC-3/5/6 are reserved-but-unimplemented; IC-5 (archived account with balance) has no Micro analog because wallets cannot be archived; IC-1/IC-6's single balance equation is replaced by by-construction layers with only MIC-14's negative-unallocated WARN as a runtime net. Harm: a hypothetical future store that breaks additivity would not be caught by an equation check the way Zman catches drift. Mitigation: write-time invariants + MIC-15 key uniqueness.

- **F-5 (P2 — lost Zman convenience).** Zman's expense category catalog management (rename/merge, `Z finance/actions.ts:2607-2790`) has no Micro equivalent — `categoryLabel` is frozen at creation; correction is the only path. Harm: label typos persist as new labels; grouping fragments. (Corroborates SA-2.)

- **F-6 (P2 — audit-shape difference, honest).** Micro's deposit refund nets `collectedMinor` (`craft-order/policies.ts:932`) rather than posting a gross cash-out entry; the cash ledger therefore shows net collections, while Zman keeps gross in+out movements (`Z ACCOUNTING_RULES.md` rule 2). History remains auditable via order events (`deposit_refunded`), but gross-cash audit trails are thinner than Zman's.

- **F-7 (P2 — Zman-side transfer hazard).** Zman's global `idempotency_key` table can incorrectly block a legitimate retry after reversal: a re-conversion after `reverseSale` reusing the same `requestId` returns `ok` with no data (`Z finance/actions.ts:1456-1472` selects the now-soft-deleted sale → undefined) instead of re-converting. Micro's attempt-suffixed keys (`fulfillmentService.ts:138-146`) are the compliant pattern. Transfer guidance: never port Zman's single-key-per-entity pattern.

- **F-8 (P3 — brief drift).** The task brief describes `OperatingExpenseContext.relationship` as project/private/unknown; the actual enum is **project | shared** (`financial-event/types.ts:28`), with "private/personal" spending represented as `owner_withdrawal_cash` and shared-with-declared-share covering the household dimension. No code impact; corrected for the record.

- **F-9 (P3 — brief drift).** The brief's "INV-4: sale posts max(0, amount−deposit)" does not match the code: Zman books the **full** realized revenue as the sale and nets on the cash side (transformed deposit + remainder movement, `Z finance/actions.ts:1528-1595`). Micro's model (revenue = full price at delivery; cash = collections) is equivalent-or-stricter; no action.

- **F-10 (P3 — cosmetic).** MIC-14 and asset-disposal messages round with `Math.round(minor/100)` for display (`integrityCheckService.ts:1013, 1020`), dropping sub-qirsh remainders in message text only (values themselves are integer-exact). No financial effect.

---

## 5. Verdict Summary

| # | Capability | Value preserved? | Truth compliance | Verdict |
|---|---|---|---|---|
| 1 | Expense entry semantics | Y (deeper questions; catalog rename/merge lost) | PASS | **ADAPT** |
| 2 | Purchase/inventory | Partial (auto-linkage/auto-COGS traded for explicit receiving; stricter invariants) | PASS | **ADAPT** |
| 3 | Waste/write-off | Partial (reversible + reasoned; netting vs disclosure differs) | PASS (conflict flagged) | **ADAPT + NEEDS_OWNER_DECISION (F-1)** |
| 4 | Orders/deposits | Y (pending default + meaning split is stricter) | PASS | **ADAPT** |
| 5 | Order→sale conversion | Y (revenue timing equal; cash honesty stronger; FT-02 verified) | PASS | **ADAPT** |
| 6 | Credit/receivables | Y+ (no fabricated cash) | PASS | **ADOPT** |
| 7 | Assets/depreciation | Partial (manual recording; no retroactivity — compliant) | PASS | **ADAPT** |
| 8 | Loans | Y | PASS | **ADOPT** |
| 9 | Period reading | Y (canonical reader + MIC-1; no second profit number) | PASS | **ADOPT** |
| 10 | Integrity checks | Partial (IC-5 lost; IC-1/6 by construction; MIC-3/5/6 reserved) | PASS | **ADAPT** |
| 11 | Backup/restore | Y+ (tamper/counts/atomic restore; links survive) | PASS | **ADOPT** |
| 12 | Drafts/lock | Y+ (no-event drafts; PBKDF2+backoff lock) | PASS | **ADOPT** |
| 13 | Money representation | N at boundary (10× + 2-vs-3 decimals; in-app consistent) | PASS internally | **NEEDS_OWNER_DECISION (F-2)** |
| 14 | Owner draw/inject | Y+ (amanah + entitlement separation) | PASS | **ADOPT** |

**Totals: ADOPT 6 · ADAPT 7 · NEEDS_OWNER_DECISION 1 (plus one embedded decision in C3) · REWORK/REJECT_WITH_REASON/MISSING 0.**

**Safety rules: 14/14 PASS. Findings: P0=0, P1=2, P2=5, P3=3.**

Key transfer rules derived from this audit (for the group synthesis):
1. Never port Zman's read-time retroactive depreciation, remainder-as-cash-in conversion, or single-idempotency-key pattern — all three violate Micro contracts.
2. Any future Zman data migration requires an explicit fils→qirsh (÷10) conversion with an owner-approved rounding policy (F-2).
3. The waste-netting question (F-1) must be settled by contract amendment before any code changes.
