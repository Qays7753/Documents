# Group 4 Contracts — Outgoing Loans and Retained Deposits

Micro deep-finance extension, contract 29 (عقد ٢٩). Baseline `main @ 67d4e41` → final `main @ 05669a9`.

## 1. Outgoing loans — event model

Two of the nine new event types carry the loan lifecycle; both require a mandatory `LoanEventContext { loanId, borrower }`:

| Type | cash | ownerCapital | operatingExpense | loan | meaning |
|---|---|---|---|---|---|
| `loan_outgoing_cash` | −P | 0 | 0 | +P | principal lent out |
| `loan_repayment_cash` | +R | 0 | 0 | −R | repayment received |

Invariants: an outgoing loan is **not** an expense and **not** an owner withdrawal (ownerCapital and operatingExpense deltas are structurally zero); a repayment is **not** revenue (no retainedRevenue delta, no recognized revenue — only the loan balance falls and cash rises). A settled loan remains visible in history (status derived at read: قائم / مسدَّد). Repayment can never exceed the outstanding balance (guard with the exact Arabic message «الدفعة أكبر من المتبقي…»); repeated repayment submissions are idempotent (`${loanId}:repayment:${date}:${amount}` keys, honest reuse).

## 2. Loan record and storage

`LoanRecord` (new store, schema 34): borrower, principal, loan date, purpose note, optional source wallet, `principalEventId`, repayments (each with its event id and optional documented reversal), status, operation key. Outstanding balance, paid total, and status are **derived at read — never stored** (the Zman invariant, rebuilt with Micro's event chain). Four atomic commit transactions in IDB + Memory parity: loan correction, repayment, repayment reversal. Legacy 25/33 files import with `loans: []`.

Corrections:
- **Loan correction** (`correctLoan`): reverse + replace of the principal event atomically, record re-pointed; requires reason; rejects a no-change request; principal cannot be corrected below active repayments; corrections preserve the repayment chain.
- **Repayment reversal**: documented reversal event linked to the repayment; the original stays marked «معكوسة موثقة» with its reason; double reversal refused; cash movement reversed in the same transaction.

## 3. Canonical reading and statement

`readRecordedPeriodResult` gains no revenue/expense term for loans (they are balance-sheet flows). `readPosition` adds the `loanMinor` layer (outstanding loans as an asset of the owner). The cash statement (after fix 1) shows «قروض أعطيتها» in cashOut («قرض لشخص — ليس مصروفًا ولا سحبًا شخصيًا») and «استرداد قروض» in cashIn («رجوع مالك أقرضته — ليس إيرادًا»), each source deep-linked to `/loans/:id`. Loan corrections appear once in the corrections block with family label «قرض أعطيته».

## 4. UX journey

Editor (full-screen): «هل أعطيت هذا المبلغ كقرض؟» framing — borrower («أحمد، محمد، ورشة الجيران» placeholder), amount, date, optional purpose, optional source wallet. Effect preview before save: «لا يُخصم من ربحك — مالك ما زال لك، لكن عند غيره». Detail page: principal, paid, remaining (3-stat summary), repayment history with traceable reversal (inline reason — no browser prompt), documented correction, financial-events layer. Quick repayment via the bottom-sheet RepaymentSheet (the only new sheet; no competing navigation) with over-repayment guard and «سداد كامل المتبقي» chip. Finance tab gains the «القروض» layer with honest counts and pending-deposit visibility.

## 5. Retained deposits — the three explicit outcomes

Finishing the Group 3 pending foundation. When an order with a collected deposit is cancelled, the deposit settlement is «needs_review» — the pending state. Group 4 adds the explicit classification with exactly three outcomes:

1. **Pending decision** (default; cancellation alone never infers meaning) — visible and actionable in OrderDetail («شو بدك تعمل بالعربون المحتفظ به؟» + «أو اتركه معلقًا») and in the Finance loans layer («N عربونًا بانتظار قرارك»), plus a `pendingRetainedDepositsMinor` position layer. The pending state is never raw-data-only.
2. **Owner money** — `deposit_retained_owner` event: ownerCapital +D; cash entered earlier; not revenue, not Amanah.
3. **Project revenue** — `deposit_retained_revenue` event: retainedRevenue +D; recognized once; cash is NOT moved again (the deposit was already collected — no double counting).

Both classification events require `DepositEventContext { orderId }` (the source order). Classification requires a reason. The domain guards single classification per order (one decision, ever); reclassification is a reverse+replace correction (original classification event reversed, replacement recorded, order meaning re-pointed) — the original event and the decision history are preserved.

## 6. Import/export integrity (hardened in this session)

The import validator cross-checks every classification event's `orderId` against the orders present in the file (orphan links rejected); legacy-type events carrying the new deltas are rejected; reversal events must negate all eight delta columns and carry matching contexts; the aggregate retained-revenue sum cannot be negative; deposit records link to real orders through the export round trip.

## 7. Test evidence

Domain: loan policy tests (146-line suite) — deltas, over-repayment guard, settlement visibility, correction chain; craft-order retained-deposit tests — pending default, single classification, reclassify reverse+replace, reason required. App: loanService (7) including correction + no-change guard + below-repayments rejection; retainedDepositService (7) — classification flows, atomic corrections. Dom: G4Loans (3) — editor preview, sheet repayment with guard, reversal; G4RetainedDeposit (3) — pending surface, owner/revenue classification with zero-cash assertion, correction. Statement tests: loan family lines + correction block once (net 0 in-period). Schema34: classification events round-trip with order linkage.
