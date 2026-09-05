# SA-5 — Adversarial Integration Audit (Zman→Micro Transfer, Group 6 / Task 5-c)

- **Date:** 2026-09-05
- **Micro baseline:** `1242aa6` (`agent/group-6-zman-transfer-audit`, clean tree) — app in `apps/prototype-web/client`, domain in `src/domain`
- **Zman baseline:** `bdd63ab` (read-only reference, `/home/z/my-project/repos/zman-app`)
- **Method statement:** STATIC adversarial code analysis of interaction seams between transferred capabilities and the rest of Micro. No repository file was created or modified. As permitted, I ran **existing** vitest suites read-only (15 test files / 198 tests, all green: `directSaleService`, `projectFinancialService`(+`.redelivery`), `localTransferService.envelope27`, `EventsLayer.familyGuard.dom`, `deliveryReviewService`, `collectionReversalService`, `retainedDepositService`, `IndexedDbLocalStore.delivery`, `projectFinancialService.test`, `statementService.test`, `inventoryMaterialService.test`, `localTransferService.test`, `loanService.test`, `assetService.test`, `fulfillmentService.test`) and `pnpm lint` (0 errors / 37 pre-existing warnings — AR-05 gate intact). All `file:line` citations are at the stated revisions.

## Methodology

Attack each seam end-to-end: construct the adversarial event sequence, trace the write path (UI handler → application service → domain policy → `IndexedDbLocalStore` commit), then trace every read path that aggregates the result (`projectFinancialService`, `statementService`, `financialPulseService`, `walletLedgerService`, `integrityCheckService`). Classify: **SAFE**, **DEFECT (P0/P1/P2/P3)**, or **NEEDS_OWNER_DECISION**. P0 = financial correctness/data loss/security; P1 = missing capability/broken journey/data integrity; P2 = UX/perf/maintainability/data-integrity edge; P3 = enhancement/defense-in-depth.

---

## Scenario 1 — DOUBLE EFFECTS (one economic event → two records/movements)

**Attack:** save → cancel/reverse → retry on every money-writing path; look for a second record, second movement, or second cash effect.

### 1.1 Direct sale: save + cancel + retry (FT-02 mirror idempotency)
- **Trace:** `DirectSaleService.record` reuses by idempotency key (`application/direct-sales/directSaleService.ts:74-78`). `cancel` reuses by revision key (`:182-191`) and refuses a key already used anywhere (`:184-191`); revision-count conflict guard for stale windows (`:180-181`). The FT-02 wallet mirror builds reversals with deterministic identities `id: sale-cancel:${entry.id}` / `operationKey: sale-cancel:${sale.id}:${entry.id}` (`:248-262`), skips already-reversed allocations (`:233-246`), commits them in ONE `commitCashContinuity` call (`:263`), and on failure returns an honest `allocationReversalNotice` instead of failing the cancel (`:220-221`). Domain `cancelDirectSale` is itself documented and appends a `cancel` revision.
- **Test evidence (read bodies):** `directSaleService.test.ts:431-452` asserts allocation+mirror wallet sum = 0 after cancel; `:454-463` asserts repeated cancel → `reused: true` and exactly ONE reversal entry; `:465-483` asserts no-attribution cancel writes zero cash entries. Ran green.
- **Verdict:** **SAFE.**
- **Note (P3, doc-only):** the FT-02 comment (`directSaleService.ts:214-219`) says the value «returns to unallocated», but `readPosition` voids the cancelled sale entirely (`projectFinancialService.ts:355-356` filters to active sales; `:379-387` subtracts only live allocations) — the money leaves recorded cash, and the physical drawer surplus surfaces as a negative wallet balance resolved by owner adjustment. Financially honest; the comment overstates. **Recommended:** align the comment.

### 1.2 Delivery + reversal + re-delivery
- **Trace:** `commitDelivery` refuses a second delivery while an unreversed delivered event exists (`application/fulfillment/deliveryReviewService.ts:313-322`); per-attempt idempotency keys (`:131-139`, `:339-345`) make re-delivery a new delivery, not a replay. Movement identity embeds the delivery event id (`:394`, `:413`) and skips existing operation keys (`:395`). `reverseDelivery` refuses double reversal of the same delivery event (domain `craft-order/policies.ts:824-830`), mirrors only unreversed consumption movements (`deliveryReviewService.ts:586-624`), guards non-negativity (`:616`), and commits atomically via `commitOrderDeliveryReversal` (store refuses duplicates — `IndexedDbLocalStore.delivery.test.ts:195-258`, ran green). Cash collected at delivery is NOT touched by the reversal (explicit contract, `:551-553`).
- **Verdict:** **SAFE.**

### 1.3 Collection reversal (partial + compound)
- **Trace:** domain `reverseOrderCollection` caps cumulative reversals at the source collection (`craft-order/policies.ts:756-765`), refuses cancelled orders (`:751-752`) and over-collection (`:764-765`). The compound service only offers dual reversal (collection + allocation) on full match with a single unambiguous, unreversed, amount-equal allocation (`application/collections/collectionReversalService.ts:111-175`), reuses by root key (`:263-286`), and writes atomically (`commitOrderCollectionReversal`, `:338-342`). G6-F1-2 root-key fix removed the timestamp-key repeat hole.
- **Test evidence:** `collectionReversalService.test.ts` (10 tests) ran green.
- **Verdict:** **SAFE.**

### 1.4 Loan restore / repayment reversal (FT-03 family guard)
- **Trace:** `familyEventOwner` (`components/finance/EventsLayer.tsx:79-105`) replaces reverse/edit/delete/restore buttons for `asset_*`, `loan_*`, and `deposit_retained_*` events with a deep link to the owning record page (both the unreversed state `:356-378` and the reversed/restore state `:380-397`), so the general corrector can no longer desynchronize an event from its family record (MIC-10/11/12 failures). Loan repayment reversal is one-shot per repayment (`src/domain/loan/policies.ts:104-106`); `restore:` deterministic keys let MIC-10 recognize restored acquisitions (`integrityCheckService.ts:705-716`).
- **Test evidence:** `EventsLayer.familyGuard.dom.test.tsx:89-159` asserts asset rows show the owner link and NO general buttons, loan rows likewise, and the link target `?from=` is preserved. Ran green.
- **Verdict:** **SAFE.**

### 1.5 Asset correction
- **Trace:** `correctAcquisition` refuses an already-reversed source (`application/assets/assetService.ts:233-234`) and no-change edits (`:236-240`); writes reversal+replacement+record atomically (`commitAssetAcquisitionCorrection`). Domain `correctLoanRecord` refuses principal below active repayments (`src/domain/loan/policies.ts:131-133`).
- **Verdict:** **SAFE.**

### 1.6 Waste reversal
- **Trace:** `InventoryMaterialService.reverse` is one-shot per movement (`application/inventory/inventoryMaterialService.ts:1163-1168`), mirrors quantity AND value with the original cost knowledge (`:1170-1184`), and asserts the position stays non-negative (`:1185`; domain asserts both quantity and value — `src/domain/inventory-material/policies.ts:227-235`).
- **Verdict:** **SAFE.**

### 1.7 Retained deposit: classification → settlement → re-classification
- **Trace:** settlement happens once (`settleDeposit` guard `craft-order/policies.ts:918-920` — a decided deposit cannot be re-settled; refund and retain are mutually exclusive states). `classify` is refused if an active classification exists (`retainedDepositService.ts:95-96`; domain `:1000-1001`); `reclassify` is the only path after classification (reversal + replacement, atomic `commitDepositClassificationCorrection`) and refuses same-meaning reclassification (`policies.ts:1033`). Period readers exclude globally reversed ids (`projectFinancialService.ts:617-626`), so the re-classified amount never double counts. Re-classification after settlement **is possible by design** (documented correction) — verdict below.
- **Verdict:** **SAFE** (re-classification after settlement is an intended, audited correction; see Scenario 9 for the wallet asymmetry).

---

## Scenario 2 — DUPLICATE SUBMIT (double-tap on every financial commit)

**Attack:** rapid double-tap / programmatic double `click()` on every financial editor; look for (a) in-flight re-entrance guard `if (saving) return`, (b) `disabled` while saving, (c) stable idempotency key that survives re-invocation.

| Editor | `disabled` while saving | In-flight guard | Stable key / service dedupe | Verdict |
|---|---|---|---|---|
| FinancialEventEditor | `:736` | `savedRef` (`:187,478`) + saved-note short-circuit (`:432-436`) | key ref per mount (`:188`); `projectFinancialService.record` reuses (`:861-877`) | SAFE |
| SupplierPurchaseEditor | `:873` | none | key refs (`:68-70`); service reuse (`supplierPurchaseService.ts:105-106,146-147,187-190,274-277`) | SAFE |
| InventoryMovementEditor | `:839,849,883` | none | operationKey reuse in service (`inventoryMaterialService.ts:815-816,934-941,1046-1047,1096-1097`) | SAFE |
| DirectSaleEditor | `:885,898,940,948` | none | key refs (`:101-105`); service reuse (`directSaleService.ts:77,137-146,182-191`) | SAFE |
| DeliveryReview | `:458,469` | none | attempt keys + status guard (`deliveryReviewService.ts:131-139,313-322`) | SAFE |
| Collect | `:257,425` | `doneRef` post-success (`:162`) | `idempotencyKeyRef` (`:63-65`); domain `eventExists` | SAFE |
| CashDistribution / settlement | `:220` | none | `distributeUnallocated` reuse by operationKey (`projectFinancialService.ts:955-962`) | SAFE |
| EventsLayer corrections | `:736` region | `cancel()` no-ops while saving (`:163-168`) | deterministic `reverse:/edit:/delete:/restore:${event.id}` keys (`:181,219,247,269`) | SAFE |
| **AssetEditor** | `:309` | **none** | **none** — `assets.create` mints fresh ids/keys per call (`assetService.ts:165-193`) | **P3** |
| **LoanEditor** | `:197` | **none** | **none** — `loans.create` fresh ids (`loanService.ts:99-123`) | **P3** |
| **RepaymentSheet** | `:112` | **none** | **none** — `recordRepayment` fresh `repaymentId` + per-call key (`loanService.ts:141-149`) | **P3** |

- **Reasoning:** React 18 commits discrete-event state synchronously, so a genuine double-tap sees the disabled button. The residual exposure for the three P3 writers is (i) two clicks dispatched inside one task (programmatic/AT), and (ii) crash-after-commit-before-navigation → reopen → form-draft restore → re-save **with a fresh mount key** (see Scenario 5) — both produce permanent duplicate records (two assets + two `asset_purchase_*` events; two loans; double partial repayment — the domain caps only at outstanding, `loan/policies.ts:73-79`).
- **Recommended action:** add `if (saving) return` to the three handlers and accept a UI-supplied stable idempotency key in `assets.create` / `loans.create` / `recordRepayment` (mirroring `directSaleService.record`). **Verdict: DEFECT P3 (defense-in-depth missing on 3 writers).**

---

## Scenario 3 — PERIOD ATTRIBUTION (delivered in A, reversed in B, re-delivered in B)

**Attack:** does any period reader attribute the re-recognized revenue to the reversed (old) delivery date?

- **Trace:** the FT-01 helper `lastEffectiveDeliveryEvent` (`application/fulfillment/deliveryAttribution.ts:16-26`) pairs each `delivery_reversed` with its exact `reversesEventId` and returns the **last unreversed** delivery. It is consumed by every order-period reader:
  - `projectFinancialService.readRecordedPeriodResult` (`:546-553`) and the second canonical reader (`:722`), 
  - `ownerEntitlementService` (`:502-505`), `recurringWorkService` (`:297-299`), `g5Service` (`:53-55`).
  Re-delivery recomputes `recognizedRevenueMinor` via `transitionOrder` (`craft-order/policies.ts:423-438`), so revenue returns with the new delivery date.
- **Period A** (January): `lastEffectiveDeliveryEvent` → null (only delivery reversed) → revenue 0, finalOrderCount 0. **Period B** (February): last effective delivery in-period → full revenue 5000, finalOrderCount 1.
- **Test evidence (asserted):** `projectFinancialService.redelivery.test.ts:62-89` (unit: returns the unreversed delivery, null after reversal alone, the re-delivery event after re-delivery) and `:91-140` (integration: January `recognizedRevenueMinor: 0` / February `5000`), plus `:142-163` (never-reversed order keeps its period). All ran green.
- **Other readers:** `statementService` delegates the profit block to the same fixed reader (`statementService.ts:151`) and attributes order **cash** collections by each event's own date (`:179-203` — a reversed collection deducts in the reversal's period, G6-F1-3). `financialPulseService` is a point-in-time state summary with no period attribution (`financialPulseService.ts:37-68`) — during the reversed window it honestly shows 0 recognized revenue; after re-delivery it is restored. `walletLedgerService` lists cash entries at their own recorded dates with reversal rows showing effect-not-balance (`walletLedgerService.ts:92-138`).
- **Verdict:** **SAFE (FT-01 correct and regression-locked).**

---

## Scenario 4 — IMPORT/RESTORE ADVERSARIAL (localTransferService)

**Attack matrix (envelope `format/version/schemaVersion` = 27/35 current pair):**

| Attack | Disposition | Evidence |
|---|---|---|
| Unknown schema version / unpaired version+schema | **Rejected** | version pair allowlist `localTransferService.ts:2484-2546` («إصدار الملف غير مدعوم») |
| Tampered data with valid digest mismatch | **Rejected** | sha256 compare `:2554-2565` («بصمة التكامل لا تطابقه») — test `envelope27.test.ts:56-68` |
| Malformed integrity block (unknown algo / non-string digest) | **Rejected** (DP-09) | `:2557-2560` — test `envelope27.test.ts:106-117` |
| Modified counts vs migrated data (integer values) | **Rejected** (DP-01) for current-version files | `:2840-2851` — test `envelope27.test.ts:91-102` |
| Counts keys that are **non-numbers** or stripped entirely | **Silently accepted** | mismatch filter requires `typeof incoming === "number" && Number.isInteger(...)` (`:2843-2846`) — P3 bypass |
| Integrity block **removed entirely** | **Silently accepted** | `:2554` checks only if present (legacy promise, `:2549-2553`); digest is unsigned → recomputable by a deliberate tamperer — tamper-evidence, not tamper-proof (accepted local threat model) — P3 note |
| Duplicated event ids / type+key pairs | **Rejected** | `financialIds`/`financialKeys` dedupe `:1693-1718`; direct-sale id/key/revision-key dedupe `:1553-1573` |
| Events referencing missing parent **orders** (deposit context) | **Rejected** | `:1706-1711` |
| Events referencing missing parent **assets / loans** (`assetContext.assetId`, `loanContext.loanId`) | **SILENTLY ACCEPTED** | `validFinancialEvent` checks shape only (`:532-592`); `validateSnapshot` checks assets→events and loans→events (`:2378-2396`) but **never events→assets/loans** — **P2** |
| Restore preserves deposit/asset/loan context | **Yes** | asset migration keeps `categoryLabel/lifeMonths/depreciationStartOn/disposal/writeOff/contractRevisions` (`:2793-2807`); loan migration keeps `repayments(+reversals)/corrections` (`:2808-2826`); reversal events must carry the same contexts as their sources (`:1739-1741`); new delta columns can't go negative in aggregate (`:1749-1755`) |

- **P2 finding (AI-01) — orphan family events accepted at import:** a hand-tampered or manually merged current-version file can contain `asset_purchase_cash`/`loan_outgoing_cash`/`deposit_retained_*` events whose `assetContext.assetId`/`loanContext.loanId` point at records not in the file. The import validates only shape (`:532-592`) and the reverse direction (`:2383-2395`). Once imported: the event's deltas count in every reader; the FT-03 family guard (`EventsLayer.tsx:79-105`) blocks general correction and links to `/assets/:id` / `/loans/:id` which render "غير متاح محليًا" (`assetService.ts:143` / `loanService.ts:88`); MIC-10/11 iterate over assets/loans and never sweep events with ghost ids (`integrityCheckService.ts:694-750`, `:790-816`). The orphan is therefore **uncorrectable through any UI path**. This is exactly the audit brief's «a correction or restore loses asset, loan, or deposit context» risk, inverted (context without record). **Recommended:** in `validateSnapshot`, require every `assetContext.assetId`/`loanContext.loanId` to exist in `assetIds`/`loanIds` (deposit already does this for orders), and add a reverse-direction orphan sweep to MIC-10/11.
- **Verdict:** **DEFECT P2 (one gap) + 2 P3 bypass notes.** Ran `localTransferService.test.ts` (30) + `envelope27.test.ts` (5) green.

---

## Scenario 5 — DRAFT/CANCEL SEAMS (formDraftService, guards, lock, PWA)

- **Concurrency:** `FormDraftService.save` enforces `expectedUpdatedAt` conflict («نافذة أخرى أحدث», `formDraftService.ts:63-74`); `valuesVersion` mismatched drafts are ignored, not exploded (`:48-50`).
- **Stale draft after correction elsewhere:** drafts are value-only payloads; final writes go through domain guards that re-validate live state — DirectSale correction carries `expectedRevisionCount` (conflict, `directSaleService.ts:132-136`; the collection path passes the live revision count, `collectionService.ts:181`). Supplier purchase edit refuses totals/quantities below live receipts and material re-linking with live receipts (SA-5 F3, `supplierPurchaseService.ts:204-233`). **SAFE.**
- **Draft-from-purchase-bridge:** receipts are inventory movements, not purchase children — reversing a purchase payment never touches them, and the edit guard refuses to strand them (`:193-233`). **SAFE.**
- **Crash-window duplicate (P3, AI-07):** every editor clears the form draft only *after* a successful commit (e.g. `FinancialEventEditor.tsx:478-480`, `DirectSaleEditor.tsx:339-430`, `AssetEditor.tsx:148-150`). A crash between the IDB commit and the draft delete → restore-offer on reopen → re-save with a **fresh per-mount idempotency key** → a second, duplicate record. Combined with Scenario 2's three key-less writers this is the only realistic duplicate-submit route. **Recommended:** persist the draft's idempotency key inside the draft envelope and reuse it on restore.
- **UnsavedChangesGuard ↔ AppLockGate ↔ PWA:** the guard syncs the module-level dirty registry on every registration/unregistration (`UnsavedChangesGuard.tsx:57,66`); the PWA refuses auto-reload while dirty (`pwa/register.ts:51-58`) and the manual "update now" button explains instead of destroying (`PwaRuntimeNotice.tsx:36-47`); `AppLockGate` renders a veil over mounted content with `inert` so unsaved state survives locking (`AppLockGate.tsx:132-203`), and SP-03 requires real input for the heartbeat (`:82-100`). Interplay verified by `UnsavedChangesGuard.dirtyBridge.dom.test.tsx`.
- **Minor (P3, AI-08):** `setDirtyForms(1|0)` is a single global slot (`dirtyRegistry.ts:10-16`) — stacked guards (page + sheet) would overwrite each other's dirty state; token-checked cleanup (`UnsavedChangesGuard.ts:62-68`) limits the damage to the currently registered guard.
- **Verdict:** **SAFE** with 2 P3 notes.

---

## Scenario 6 — CATEGORY/CLASSIFICATION SEAMS

- **Corrections while statements are open:** statements are ad-hoc period reads, no open/close lock. A correction (reverse + replacement in period B) leaves period A's copy of the original under its old label and shows the reversal in B's corrections block (`statementService.ts:279-281` cash-corrections family). Historical restatement matches the reversal model. **SAFE.**
- **Suggested-category dedup:** `deriveExpenseCategorySuggestions` dedupes by exact string and merges seeds (`expenseCategorySuggestions.ts:28-44`); import and input normalize trim + whitespace-collapse only (`:48-51`, `localTransferService.ts:456-459`). No case folding → Latin-script case variants («Fuel»/«fuel») yield duplicate suggestions and duplicate statement groups (P3).
- **Grouping totals drift:** expense groups sum only family (non-reversed) in-period events (`statementService.ts:500-527`) while the period result nets reversal deltas (`projectFinancialService.ts:565-600`). With an in-period correction, Σ(groups) ≠ net period expense by design («وين راح المصروف» is a gross view) but there is no truth line saying so (P3 disclosure).
- **Verdict:** **SAFE** + 2 merged P3 (case-insensitive normalization; a one-line truth note on the groups block).

---

## Scenario 7 — TRACKED/UNTRACKED SEAMS

- **Untracked→tracked mid-life:** `retrackMaterial` resets the opening contract to unconfirmed (`inventoryMaterialService.ts:606-627`); `confirmMaterialOpening` records the delta versus the live position as a documented `opening`/`adjustment` movement with cost knowledge, and asserts non-negativity (`:647-719`). Position stays consistent with history — **SAFE**.
- **Partial receipt then reversal:** `receivePurchase` caps value and quantity by the purchase's active receipts (`:754-777`); `editPurchase` refuses totals/quantities below received and material re-linking with live receipts (F3, `:204-233`); `reverse` mirrors the receipt and **rejects** if the position (quantity OR value, `inventory-material/policies.ts:227-235`) would go negative — i.e., consumption after receipt blocks receipt reversal with an honest message instead of a negative balance. **SAFE.**
- **Untracked extract guard (Group 2 e40da57):** present — `extractRemainder` refuses untracked materials (`inventoryMaterialService.ts:1051-1057`, «SA-5 (F2)»), `waste`/`outbound` and `consume`/`recordShortage`/`consumeWithShortage` all refuse untracked materials (`:821-826, 887-892, 945-950, 1209-1213`); delivery review rows mark untracked as cost-reference-only skip rows (`deliveryReviewService.ts:222-239`). Shortage repeat safety: `consumeWithShortage` reuses the `:shortage` operation key (`:934-941`). **SAFE.** (`inventoryMaterialService.test.ts`, 22 tests, green.)

---

## Scenario 8 — CALCULATOR SEAMS (estimates ↔ catalog)

- **Attack:** save estimate → change catalog cost → reopen estimate → create order.
- **Trace:** `CostEstimate` freezes its own `materialItems` (each with `unitPriceMinor`/`priceDate`), `plannedCostMinor/unitCostMinor/priceFloorMinor/knowledgeState` at save (`costEstimateService.ts:96-123`); `update` is an explicit whole-record revision that recomputes from new inputs (`:125-152`) — it never silently re-reads catalog prices. `preview` is a pure calculation (`:39-79`). Order/draft creation from an estimate copies snapshot values (`sourceEstimateId` carried as a link only, `localTransferService.ts:1619-1625`; `NewDraft`/`EstimateDetail` create drafts with copied items).
- **Verdict:** **SAFE** — historical snapshots are immutable by construction; catalog changes cannot retroactively alter saved estimates.

---

## Scenario 9 — DEPOSIT SEAMS

- **Collect → cancel → refund:** refund requires a cancelled order and an undecided deposit; settlement is once-only and refund/retain are exclusive states (`craft-order/policies.ts:904-945` guard `:918-920`, amount must equal the collected deposit `:923-924`). Statement nets the refund as cash-returned (`statementService.ts:181-203`). **No double-refund path.**
- **Retain → classification → settlement:** one classification at a time; reclassify = audited reversal + replacement; period readers exclude globally reversed ids so nothing double counts (Scenario 1.7). Retained-pending deposits surface as their own position line (`projectFinancialService.ts:395-402`).
- **Gap (P3, AI-03) — wallet asymmetry:** `fulfillmentService.refundDeposit`/`retainDeposit` (`:324-360`) settle the order only; neither mirrors wallet allocations, unlike the analogous direct-sale cancel (FT-02, `directSaleService.ts:225-270`) and collection reversal (G6-F1-2, `collectionReversalService.ts:319-335`). If the owner had allocated the deposit's cash into a wallet (generic distribution), a physical refund leaves the wallet ledger overstated; the mismatch surfaces only through cash counting. (Deposit collection itself records no wallet attribution — `agreementService.ts:133-134` — so this needs a deliberate prior distribution.)
- **Verdict:** **SAFE** core + **P3** asymmetry (decide: mirror order-source allocations on deposit refund, or document that wallet reconciliation is the owner's count-time act).

---

## Scenario 10 — ASSET/LOAN SEAMS

- **Depreciated to end of life → disposal:** `planAssetDepreciation` floors at full-life and per-month caps (domain asset policies); `prepareAssetDisposal` requires terminal readiness; disposal event freezes `bookValueMinor` in `assetContext` (`assetService.ts:369-392`).
- **Correction of an old depreciation entry after disposal:** `reverseDepreciation` checks only "event exists, is depreciation, not already reversed" (`:323-338`) — no asset-status guard. Reversing an old depreciation of a **disposed** asset re-inflates the derived book value while the disposal event (frozen book value, proceeds) stands; `assetBookValueNowMinor` becomes positive for a disposed asset. It is auditable (deltas are explicit) but no surface warns about it (P3: refuse or warn when `asset.status !== "active"`).
- **Loan settled → correction of an old repayment → net effect:** `reverseLoanRepayment` re-activates the repayment (`loan/policies.ts:96-118`); `readLoan` derives outstanding from active repayments (`:54-64`) so the loan re-opens honestly; `correctLoan` guards against revisions already reversed (`loanService.ts:216`), against no-change edits (`:219-222`) and against principals below active repayments (`policies.ts:131-133`). Repayment events are mirrored atomically (`commitLoanRecord`).
- **Partial repayment reversal > remaining?** A reversal *restores* outstanding (it can only un-reverse a repayment that actually happened — `:104-106`); it cannot over-reverse. **SAFE.**
- **Idempotency of corrections:** loan/asset correction keys embed `this.now()` (`loanService.ts:230,239`; `assetService.ts:248,257`) — unique per call. Double-fire protection is read-then-write (`source.correctionType === "reverse"` checks) — a TOCTOU window exists only for two concurrent invocations, which the disabled-during-flight UI prevents (same class as Scenario 2; P3 inherited).
- **Verdict:** **SAFE** core + **P3** (depreciation reversal on disposed assets lacks a status guard).

---

## Scenario 11 — LOCK/PIN SEAMS

- **Brute-force math (online, through the UI):** PIN space 4–8 digits = 111,110,000; PBKDF2-SHA256 **120,000 iterations** per attempt (`localLockService.ts:52-66`) ≈ 50–150 ms in-browser. Enforced backoff: 0/3s/10s/30s after 3/5/8 failures (`:102-107`), early-rejected inside the window without counter inflation (SP-04, `:179-192`); `disable()` shares the same counter/backoff (DP-05, `:244-266`). Steady state 30 s/attempt ⇒ ≈2,880 attempts/day; 4-digit PIN ≈ 3.5 days of continuous attack, 6-digit ≈ 9.5 years. The failed-attempt counter only resets on success — waiting does not reset it. Honest scope: the gate UI itself declares «يحمي من النظرة العابرة فقط» (`AppLockGate.tsx:143-145`); against an attacker who extracts the IndexedDB record, 120k iterations is a GPU-speedable hash for a 4-digit PIN — acceptable for the stated glance-protection threat model.
- **Legacy PIN migration:** single-sha256 legacy records verify on the legacy path and are transparently upgraded to PBKDF2 on first successful unlock (`verifyPin`, `:70-84`) — no lock-out, no weak record left behind.
- **Deep link while locked:** `AppLockGate` re-evaluates on every location change (`:33-60`) and stays locked; `/setup` and `/settings` are exempt recovery routes (`StartupGate.tsx:8`). That exemption IS a bypass of the veil — but every data-leaving action on `/settings` (export, import, reset) is separately gated by `DataActionPinGate` (`Settings.tsx:196-202, 232-238, 263-269, 310-317`, gate component `DataActionPinGate.tsx:29-51` using the same `unlock` counter). Success at the data gate is equivalent to unlocking. No other route exposes financial surfaces while locked (content under the veil is `inert`, `AppLockGate.tsx:201`).
- **Verdict:** **SAFE** (P3 observation only: on a browser tab (non-PWA install), a locked session deep-linked to `/settings` shows non-financial settings content — data actions still require the PIN).

---

## Scenario 12 — REGRESSION WATCH (Agent 1 fixes vs transferred capabilities)

| Fix | Regression test exists? | Actually asserts behavior? | Transfer-masking risk |
|---|---|---|---|
| FT-01 period attribution | `projectFinancialService.redelivery.test.ts` | **Yes** — Jan 0 / Feb 5000 with `finalOrderCount` (`:124-139`); pure attribution unit (`:62-89`). Ran green | None — the test exercises the *transferred* order-delivery flow directly; it strengthens, not masks |
| FT-02 mirror reversal | `directSaleService.test.ts:387-484` | **Yes** — wallet sum 0 (`:448-451`), idempotent identity (`:454-463`), zero entries without attribution (`:465-483`). Ran green | None |
| FT-03 family guard | `EventsLayer.familyGuard.dom.test.tsx:89-159` | **Yes** — no general buttons on asset/loan rows + correct deep link (`:125-139,157-158`) | Masks nothing; note it makes the P2 orphan-event gap (Scenario 4) *worse* by removing the last generic correction route — by design, but the import boundary must therefore reject orphans (recommended action) |
| DP-01 counts | `localTransferService.envelope27.test.ts:91-102` | **Yes** — rejects integer mismatch before preview | Bypass noted (non-integer/missing counts) — test does not cover the bypass (P3) |
| DP-09 malformed integrity | `localTransferService.envelope27.test.ts:106-117` | **Yes** — rejects `{algorithm:"sha512", digest:42}` | Same file lacks the stripped-integrity case (accepted by design for legacy) |
| Density guard 52 pages (AR-04) | `scripts/text-density-count.py` (CI gate via `pnpm check`) — PAGES list at `:552`, missing/unmeasured pages fail (`:800-835`) | Yes (script asserts, not vitest) | None — script-level, financial paths untouched |
| AR-05 lint/format full-app | `package.json:18-20` covers `apps/prototype-web/client/src`; CI `.github/workflows/ci.yml:35-39` runs `pnpm lint` + `pnpm check` | Verified live: `pnpm lint` → 0 errors / 37 warnings | None |

**Conclusion:** all of Agent 1's fixes are regression-locked with meaningful assertions; none of their tests stubs or narrow a transferred capability in a way that could mask a transfer defect. The only residual interaction is the FT-03 × import-boundary one noted above.

---

## Scenario 13 — RELEASE RISK (production build, current branch)

- **Lazy routes:** all 52 `lazy(() => import("@/pages/…"))` entries in `MicroRouter.tsx:12-77` resolve to files that exist in `src/pages/` (verified by directory listing); route order places specific patterns before `:id` catch-alls (`:94-101,137-142`); no dead route targets. `/review` redirects to `/finance` (`:151-153`).
- **Service wiring:** `PrototypeServicesContext` provides all services used by pages (`usePrototypeServices` consumers matched). No unresolved import found by eslint (AR-05 gate, 0 errors).
- **IndexedDB migrations:** `onupgradeneeded` creates every store guardedly (existence checks, `IndexedDbLocalStore.ts:207-388`) and migrates data for `oldVersion < 23/24/25/26/17/…` with guarded cursors and honest upgrade failures (`:389-660`); schema 34→35 adds `formDrafts`/`security` stores only (`:366-374`). Older in-the-wild schema versions (14–34) all open without data loss — the export side accepts their paired file versions back to 6/14 (Scenario 4 allowlist).
- **PWA update flow:** `register.ts` only registers in PROD + secure context (`:30-36`); dirty-form reload protection verified (Scenario 5).
- **Targeted suites:** 15 files / 198 tests green; lint 0 errors. (Full `pnpm check`/build not run here — last AR-05 commit message records a verified production PWA build at this tree.)
- **Verdict:** **SAFE** — no release blocker found in the transferred-feature areas.

---

## Verdict summary table

| # | Scenario | Verdict | Key finding |
|---|---|---|---|
| 1 | Double effects | **SAFE** | All writers idempotent or guarded; FT-02/FT-03 verified by tests |
| 2 | Duplicate submit | **DEFECT P3** | AssetEditor / LoanEditor / RepaymentSheet: no in-flight guard + per-call keys |
| 3 | Period attribution | **SAFE** | FT-01 last-effective-delivery used by every period reader; regression-locked |
| 4 | Import/restore | **DEFECT P2** | Orphan asset/loan-context events accepted → uncorrectable; DP-01/DP-09 otherwise enforced |
| 5 | Draft/cancel seams | **SAFE** (+2 P3) | expectedUpdatedAt + explicit restore; crash-window duplicate; single-slot dirty registry |
| 6 | Category seams | **SAFE** (+2 P3) | No case folding; group-vs-net disclosure line missing |
| 7 | Tracked/untracked | **SAFE** | Untracked extract guard present; value+quantity non-negative invariants |
| 8 | Calculator seams | **SAFE** | Estimate snapshots frozen; catalog changes never retroactive |
| 9 | Deposit seams | **SAFE** (+P3) | Once-only settlement; wallet mirror absent on deposit refund (asymmetric with FT-02) |
| 10 | Asset/loan seams | **SAFE** (+P3) | Depreciation reversal lacks disposed-status guard; no over-reversal possible |
| 11 | Lock/PIN | **SAFE** | 120k-iter PBKDF2 + enforced backoff; recovery routes gated by DataActionPinGate |
| 12 | Regression watch | **PASS** | All 5 fix-tests assert real behavior; density/lint gates live in CI |
| 13 | Release risk | **SAFE** | All lazy imports resolve; migrations cover old schemas; lint 0 errors |

## Findings

**P0 — none.** **P1 — none.**

- **P2-01 (AI-01)** Import accepts family-context events with missing parent records: `localTransferService.ts:532-592` (shape-only validation of `assetContext`/`loanContext`), `:2378-2396` (one-directional asset/loan→event checks; deposit→order is checked at `:1706-1711`). Imported orphans are uncorrectable: FT-03 guard (`EventsLayer.tsx:79-105`) routes to a nonexistent asset/loan page; MIC-10/11 never sweep ghost ids (`integrityCheckService.ts:694-750,790-816`). *Action:* validate `assetContext.assetId`/`loanContext.loanId` against the file's record sets and add a reverse orphan sweep to MIC-10/11.

**P3 (defense-in-depth / honesty polish):**
- **P3-01 (AI-02)** Three financial writers without in-flight guard or stable idempotency keys: `AssetEditor.tsx:125-152`, `LoanEditor.tsx:76-109`, `RepaymentSheet.tsx:33-53` (+ `assetService.ts:161-199`, `loanService.ts:97-165` fresh keys per call).
- **P3-02 (AI-04)** DP-01 counts bypass: non-integer or missing count values skip comparison (`localTransferService.ts:2843-2846`); the digest is unsigned (recomputable by a deliberate tamperer) — tamper-evidence only, per local-file threat model.
- **P3-03 (AI-03)** Deposit refund/retain do not mirror wallet allocations (`fulfillmentService.ts:324-360`) — asymmetric with FT-02 (`directSaleService.ts:225-270`) and G6-F1-2 (`collectionReversalService.ts:319-335`); wallet ledger overstated after a physical refund until cash count.
- **P3-04 (AI-05)** FT-02 code comment claims the value «returns to unallocated» while `readPosition` voids the cancelled sale's cash entirely (`directSaleService.ts:214-219` vs `projectFinancialService.ts:355-387`) — behavior is honest; the comment misleads maintainers.
- **P3-05 (AI-06)** `reverseDepreciation` lacks an asset-status guard (`assetService.ts:323-355`): reversing old depreciation of a disposed/written-off asset re-inflates `assetBookValueNowMinor`.
- **P3-06 (AI-09)** Category labels: no case folding at normalization (`expenseCategorySuggestions.ts:48-51`, `localTransferService.ts:456-459`); statement expense groups are gross while the period result nets corrections — add a truth line (`statementService.ts:500-527` vs `:578-600`).
- **P3-07 (AI-07)** Crash-window duplicate: form drafts cleared only after commit (`FinancialEventEditor.tsx:478-480` et al.); crash between commit and draft delete → restore → re-save with a fresh per-mount key duplicates the record. *Action:* persist the idempotency key in the draft envelope.
- **P3-08 (AI-08)** Dirty registry is a single 0/1 slot (`dirtyRegistry.ts:10-16`); stacked guards overwrite each other's dirty state.

**NEEDS_OWNER_DECISION — none.** (P3-03 deposit-wallet mirroring is the closest call: mirroring would add a hidden cash write; not mirroring relies on cash counting. Owner preference.)

**Overall release verdict:** no P0/P1; the transferred Zman capabilities are integrated with Micro's event-sourced correction model without double-counting, and every Agent 1 fix is regression-locked. The one P2 sits at the import boundary (hand-tampered files only, not the live path) and is a small validator addition.
