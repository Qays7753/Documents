# 02 — Recovered Work and Financial Contracts

## 1. Nine approved financial contracts — final status

Verified against actual code, persistence, UI, and tests on branch head `8a98835` (merged into `main` as `1601fd9`).

| # | Contract | Status | Key evidence |
| --- | --- | --- | --- |
| C1 | Waste/spoilage — owner chooses profit impact | **Implemented (fixed this run)** | `InventoryMovementEditor` asks the نعم/لا question; waste-only records the event with no profit effect; profit-impact with known cost posts a linked non-cash loss (`loss_non_cash`) with no cash outflow; unknown cost stays «غير محدد بعد» with quantity only; reversal restores exactly once. Tests: `inventoryMaterialService.test.ts` (+175 lines), `group2InventorySurfaces.test.tsx` (+88), domain policy tests. |
| C2 | Edit & reversal — both direct edit (with in-event history) and corrective reversal | **Partial by design — owner decision open (FC-02)** | The approved in-repo decision C1 (correction boundary) forbids silent in-place mutation: Micro implements **atomic reverse-and-replace** (reversal + replacement in one transaction, old values preserved, reason required, double-reversal prevented at domain and store level). The alternative path (b) of the assignment — a literal in-place edit that mutates the original event while keeping history inside it — was **not** implemented because it contradicts the repository's own documented decision; flagged NEEDS_OWNER_DECISION, never guessed (report 05). |
| C3 | Deposit lifecycle | **Implemented (completed this run)** | Sale recognized once at delivery (order 100.00 / deposit 20.00 → sale 100.00, deposit applied once, 80.00 remaining → collect or receivable; no duplicate revenue/receivable). Deposit is liquidity-not-revenue at collection; explicit wallet destination at collection (initial `AgreementEditor` + mid-journey `OrderDetail` panel — the previously unreachable WF-01 path); deposit card shows original/collected/applied/refunded/retained + wallet + state + profit effect; cancellation exposes the four outcomes (refund / pending / project revenue / owner money — owner money is due-to-owner, cash decreases only at withdrawal, never profit). Tests: `G3.dom.test.tsx` (deposit + wallet destination + allocation link), `fulfillmentService.test.ts` (+91), `retainedDepositService.test.ts`. |
| C4 | Credit sale & later collection | **Implemented (verified)** | Sale/receivable recorded once; collection reduces receivable and increases wallet with no new revenue; settlement history labeled («تحصيل دفعة من ورقة التحصيل» — FC-09 fix). Verified in domain deltas and `directSaleService`/`collectionService` tests. |
| C5 | Loans | **Implemented (verified)** | Linked to a person, `loan_outgoing_cash` deltas are neither expense nor owner withdrawal; partial repayments, settlement, correction, reversal, and history work; repayment race protected by `loanCommitGuard` (AV-02). |
| C6 | Negative inventory | **Implemented (completed this run)** | In-flow (consume/waste/adjust-decrease) shortage warning: requested + available + resulting quantity, explicit choice, never a silent negative balance (FC-07/FC-10 — warning text, preview refusal of negative result, shortage panel shows requested + resulting). Untracked materials create no stock movement. |
| C7 | Automatic consumption | **Implemented (verified)** | Tracked+approved materials auto-consume on confirmed delivery; untracked create no movement; insufficient stock → preview + explicit confirmation; idempotent (operation keys), linked to order/delivery; reversal mirrors exactly once. |
| C8 | Cost/unknown values | **Implemented (completed this run)** | Calculator/estimate create no sale/cash/inventory/profit event; unknown cost shows quantity with «قيمة غير محددة بعد» — including in movement rows (FC-08: was a confident 0.00); unknown never coerced to zero; **AV-05**: amounts beyond the safe-integer bound now rejected at domain and import (2^53 loses precision in sums). |
| C9 | Opening balances | **Implemented (verified)** | Unknown stays unknown (`null`), never zero; UI explains the consequence and offers later specification (`CashOpeningLaterEditor`, Setup skip path); import of unknown openings preserves state. |

**Money-precision invariant added (AV-05):** `assertPositiveMinor` (financial-event domain) and `isMoney` (backup import validation) now enforce `Number.isSafeInteger`. A forged backup re-sealed with a valid digest over a 2^53 amount is rejected by structure validation, not by the digest. Tests: domain (reject 2^53, accept MAX_SAFE_INTEGER) + import (re-sealed forgery rejected).

## 2. Adversarial findings — final disposition

| ID | Severity | Finding | Disposition |
| --- | --- | --- | --- |
| AV-01 | P0 | Re-entrant submissions duplicate monetary records (TOCTOU read-then-write in saveDirectSale/saveFinancialEvent/commitCashContinuity; state-only UI guards) | **Fixed** (stopped run, verified here): in-transaction key checks (`writeOneIdempotent`) + re-entry guards on money-writing UI paths; 4 regression tests |
| AV-02 | P1 | Concurrent loan repayments desync loan record vs events | **Fixed** (stopped run, verified): `loanCommitGuard` + revision guard in `commitLoanRecord` |
| AV-03 | P1 | Family-event reversal at service level bricks deposit classification | **Fixed** (stopped run, verified): service-level family guard in `projectFinancialService` |
| AV-04 | P2 | Current-version backup with stripped envelope accepted (digest/counts checks conditional on block presence) | **Fixed this run**: current-version files without integrity or without counts rejected; legacy 26/34 path preserved; 3 regression tests (stripped-integrity, stripped-counts, re-sealed forgery) |
| AV-05 | P2 | Financial-event amounts not safe-integer-bounded; import `isMoney` unbounded | **Fixed this run**: `Number.isSafeInteger` bounds + 2 tests |
| AV-06 | P2 | Cancelled order with non-deposit collections: money stuck, warning covered deposits only | **Fixed this run**: pre-cancel warning with consequence + next action (reverse collection first while order is alive); dom test walks the stuck repro path |
| AV-07 | P3 | needs_review nextAction promises «ألغِ موثقًا» but cancel hidden at that status | Deferred (report 05) — status-machine policy decision |
| AV-08 | P3 | Depreciation reversal after disposal resurrects disposed asset book value | Deferred (report 05) |
| AV-09 | P3 | FinancialEventEditor localStorage draft restore lacks defensive coercion other editors have | Deferred (report 05) |

## 3. Financial-contract auditor findings — final disposition

| ID | Severity | Finding | Disposition |
| --- | --- | --- | --- |
| FC-01 | P1 | Waste never asks profit-impact / waste-only | **Fixed** (stopped run, verified): question, stored meaning, linked non-cash loss, reversal, tests |
| FC-02 | P2 / NEEDS_OWNER_DECISION | Direct-edit path (a) of contract 2 absent by design (decision C1) | **Open owner decision** (report 05) — documented, not guessed |
| FC-03 | P2 | Atomic edit replacement may carry old-period occurredOn with no period warning | **Fixed this run**: explicit cross-month warning in the edit preview + dom test |
| FC-04 | P1 | No owner-selected wallet at deposit collection | **Fixed** (stopped run, verified): wallet choice in `AgreementEditor` + mid-journey panel |
| FC-05 | P2 | Deposit card lacks applied/refunded/retained/wallet/profit-effect | **Fixed** (stopped run, verified): full card in `DepositsLayer` |
| FC-06 | P3 | Deposit refund does not mirror manual wallet attribution | Deferred (report 05) |
| FC-07 | P2 | Waste/adjust-decrease lack in-flow shortage warning; preview computes negative resulting qty | **Fixed** (stopped run, verified): warning + choices; previews refuse negative balance |
| FC-08 | P2 | Movement rows render unknown-cost movements as confident 0.00 | **Fixed** (stopped run, verified): «قيمة غير محددة بعد» |
| FC-09 | P3 | Sheet collection on credit sale recorded as generic edit revision | **Fixed** (stopped run, verified): labeled settlement revision |
| FC-10 | P3 | Shortage panel shows current+requested but not resulting quantity | **Fixed** (stopped run, verified): resulting quantity stated |

## 4. Where the money invariants live (audit anchors)

For future auditors, the load-bearing points verified in this run:

- **Idempotency**: `IndexedDbLocalStore.writeOneIdempotent` (transaction-scoped dedupe) — saveDirectSale / saveFinancialEvent / commitCashContinuity; `MemoryLocalStore` mirrors; UI guards: `Collect`, `DirectSaleEditor`, `FinancialEventEditor`, `QuickActionSheet`, `OrderDetail` deposit panel (ref key).
- **Revenue recognition once**: `craft-order/policies.ts` delivery path; DELTA_TABLE `deposit_retained_*` zeros; `loan_outgoing` delta shape.
- **Double-reversal prevention**: `financial-event/policies.ts` (generic), `inventoryMaterialService` (waste), `deliveryReviewService` (delivery), collection cumulative guards.
- **Envelope integrity**: `localTransferService.prepareImport` — digest check, malformed-block rejection, AV-04 missing-block rejection for current versions, counts comparison (DP-01), orphan-family rejection (AI-01).
- **Money bounds**: `financial-event/policies.ts assertPositiveMinor`, `localTransferService isMoney` (AV-05).
