# 07 — Scenarios, Exceptions, and Role Simulation

Fourteen verification narratives (including the canonical 100/20/80 JOD deposit scenario and
the five financial boundaries) simulated against the current implementation.

| ID | Title | Status |
| --- | --- | --- |
| SCN-01 | Deposit is not revenue (100 / 20 / 80 JOD) | IMPLEMENTED |
| SCN-02 | Cancel with deposit — full consequences preview | IMPLEMENTED |
| SCN-03 | Collection is never profit | IMPLEMENTED |
| SCN-04 | Unknown cost never becomes zero | IMPLEMENTED |
| SCN-05 | Negative inventory impossible | IMPLEMENTED |
| SCN-06 | Waste with and without profit impact | IMPLEMENTED |
| SCN-07 | Asset depreciated to zero still in use | IMPLEMENTED |
| SCN-08 | Tampered backup file rejected | IMPLEMENTED |
| SCN-09 | Double-tap and concurrent window | IMPLEMENTED |
| SCN-10 | Lock protects data-exit actions | IMPLEMENTED |
| SCN-11 | Delivery reversal and re-delivery attribution | IMPLEMENTED |
| SCN-12 | Expense reclassification after save | IMPLEMENTED |
| SCN-13 | Offline day of work | IMPLEMENTED |
| SCN-14 | Unallocated shared expense honesty | IMPLEMENTED |

## Details

### SCN-01 — Deposit is not revenue (100 / 20 / 80 JOD)

**Narrative:** Owner agrees a 100 JOD order, collects a 20 JOD deposit before delivery, then delivers and collects the remaining 80 JOD.

**Expected (verified):** Position before delivery: cash +20, receivables unchanged for the deposit, revenue 0. At delivery: revenue recognized ONCE as 100 (deposit applied once inside the sale, not a second sale); profit = 100 − cost when final. After collecting 80: cash 100, settled.

**Evidence:** src/domain/craft-order/policies.ts:425-441, 518-597; application/finance/projectFinancialService.ts (readPosition/period result); docs/decisions/final-continuation-conflict-resolutions-v1.md (C/D)

### SCN-02 — Cancel with deposit — full consequences preview

**Narrative:** Order with 20 JOD deposit cancelled before delivery; owner chooses partial refund 5, retains 15, classifies 10 as owner money and 5 as project revenue.

**Expected (verified):** Refund 5 → cash −5 and deposit allocation reversed by 5; retain 15 keeps cash; classification: owner capital +10, retained revenue +5 (once); settlement only final when nothing pending; every step previewed before commit.

**Evidence:** fulfillmentService.refundDeposit/buildDepositAllocationReversals; retainedDepositService.classify (partial); G4RetainedDeposit.dom.test.tsx

### SCN-03 — Collection is never profit

**Narrative:** Owner collects 50 of a 120 sale and reads 'profit'.

**Expected (verified):** Collection raises cash only; profit is computed from recognized revenue minus cost at delivery/sale-date; Home/Finance never label collections as profit.

**Evidence:** projectFinancialService.readPosition; financial-operating-model-v1.md; contract 01

### SCN-04 — Unknown cost never becomes zero

**Narrative:** Direct sale recorded with cost unknown; owner reads the period result.

**Expected (verified):** Sale profit shows «غير متاح» (null), and the period result line is null — not zero, not fake profit.

**Evidence:** direct-sale policies (costMinor null ⇒ profit null); projectFinancialService.ts:707-718 (resultMinor null); unavailable-values-known-zero-acceptance-v1.md

### SCN-05 — Negative inventory impossible

**Narrative:** Owner tries to consume 5 kg when only 3 kg are recorded.

**Expected (verified):** Direct write rejected; owner chooses record-shortage or consume-available+shortage; an open shortage record appears with badge; never a negative balance.

**Evidence:** assertInventoryRemainsNonNegative; createInventoryShortage; contract 28 S6/D-027

### SCN-06 — Waste with and without profit impact

**Narrative:** Two waste events: one flagged profit-impact with known cost, one without.

**Expected (verified):** First writes movement + loss_non_cash event atomically (appears as operating expense line «هالك بلا خروج نقد»); second is disclosure-only (general waste value line, outside resultMinor).

**Evidence:** inventoryMaterialService.ts:1285-1320; inventoryMaterialService.test.ts:1184-1299

### SCN-07 — Asset depreciated to zero still in use

**Narrative:** Asset fully scheduled; owner keeps using it and later tries to reverse an old depreciation after disposal.

**Expected (verified):** Book value 0, status stays active; disposal is a separate later event; reversing depreciation after disposal/write-off is rejected (AV-08) — no resurrection of voided value.

**Evidence:** asset policies.ts:247 (fully depreciated); assetService active-only corrections; Conflict G/AV-08

### SCN-08 — Tampered backup file rejected

**Narrative:** Owner imports a current-version file with stripped integrity block, and a file whose digest does not match.

**Expected (verified):** Both rejected before any preview; device data untouched; Arabic tamper messages (AV-04).

**Evidence:** localTransferService.ts:2566-2584; localTransferService.envelope27.test.ts

### SCN-09 — Double-tap and concurrent window

**Narrative:** Owner double-taps 'record sale'; in another tab, the same sale is edited.

**Expected (verified):** One record (reused flag); the second window gets an honest stale-conflict message; no duplicated money.

**Evidence:** reentrancyGuards.test.ts; expectedRevisionCount in directSaleService.update

### SCN-10 — Lock protects data-exit actions

**Narrative:** Device locked; owner opens /settings (emergency route) and tries to export.

**Expected (verified):** Settings opens without unlock, but export/import/reset require one PIN proof in the session; wrong PIN hits the shared backoff counter.

**Evidence:** Settings.tsx:71-90; DataActionPinGate.tsx; Settings.lockGate.dom.test.tsx

### SCN-11 — Delivery reversal and re-delivery attribution

**Narrative:** Delivery recorded in July; reversed in August; re-delivered in August.

**Expected (verified):** Revenue voided at reversal (needs_review); re-delivery uses a new attempt key; July period no longer counts the order; August counts it once via last effective delivery (FT-01).

**Evidence:** projectFinancialService.redelivery.test.ts; deliveryAttribution.ts

### SCN-12 — Expense reclassification after save

**Narrative:** Expense saved under 'بنزين' then corrected to 'توصيل' with behavior change.

**Expected (verified):** Atomic reverse+replace; original keeps 'بنزين'; statement groups the replacement under 'توصيل'; deltas unchanged (category is zero-delta).

**Evidence:** projectFinancialService.category.test.ts; editEvent:1077-1103

### SCN-13 — Offline day of work

**Narrative:** Owner records sales, expenses, and a delivery fully offline, then reloads.

**Expected (verified):** All writes succeed (IndexedDB); offline card states no sync/cloud; SW offline reload works from precache; zero console errors.

**Evidence:** pwa/PwaRuntimeNotice.tsx:91-104; vite.config.ts (navigateFallback); browser QA evidence in worklog (360×800/390×844)

### SCN-14 — Unallocated shared expense honesty

**Narrative:** Electricity bill 60 JOD recorded as shared, share deferred.

**Expected (verified):** Event saved (unallocated), contributes 0 to operating expense in the period result until a share is declared; surfaces as sharedUnallocatedExpenseMinor with reason «حصة غير موزعة».

**Evidence:** policies.ts:317-320 (deltas guard); contract 14; expandExpenseRecordIntent defer mode


## Exception handling patterns (cross-cutting)

- **Atomicity everywhere**: every multi-record change is one transaction; failures write nothing.
- **Honest refusals**: forbidden operations get Arabic reasons naming the current state
  (e.g. «لا يمكن إلغاء الطلب وهو في حالة «تم التسليم».»).
- **Reversal instead of deletion**: history is preserved; reversals are single-use and never
  reversible themselves.
- **Idempotent retries**: same key → same record (`reused: true`), never duplicated money.
- **Concurrency honesty**: expectedRevisionCount / loanCommitGuard produce stale-conflict
  messages instead of overwrites.
- **Offline honesty**: the runtime notice states there is no sync or cloud copy in this version;
  PWA updates wait for owner approval and never reload over dirty forms.
