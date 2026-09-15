# Agent 2 — Findings and Remediation

| | |
|---|---|
| Report ID | micro-group-6-parallel-audit-001 / agent-2-zman-transfer-audit |
| Date | 2026-09-05 |
| Baselines | Zman `bdd63ab` (read-only) · Micro branch `agent/group-6-zman-transfer-audit` @ `961051f` (from Agent 1 main `1242aa6`) |
| Severity definitions | P0 financial correctness/security/data loss/release blocker · P1 missing transferred capability/broken core journey/data integrity · P2 discoverability/UX/performance/accessibility/maintainability · P3 optional enhancement |
| Fix policy | fix P0/P1 + unambiguous safe P2; regression test for every fix; financially ambiguous changes become NEEDS_OWNER_DECISION (continuation prompt §10) |

---

## 1. Executive finding counts

| Severity | Found | Fixed on branch (with regression tests) | Open (documented, actionable) |
|---|---|---|---|
| P0 | **0** | — | — |
| P1 | **3** (all classified NEEDS_OWNER_DECISION — financially/strategically ambiguous, must not be coded unilaterally) | 0 | 3 (§4) |
| P2 | **10** | **1** (AI-01, import orphan contexts) | 9 (§5) |
| P3 | **12** | **1** (AI-02, double-submit in-flight guards — defense-in-depth fix) | 11 (§6) |
| **Total** | **25** | **2** | **23** |

No P0/P1 transfer or integration defect remains open as a code fix: the three P1s are owner decisions by nature (a contract amendment, a migration strategy, a reconciliation mapping), each with alternatives laid out. The single unambiguous P2 defect found (AI-01) was fixed, tested, and browser-verified on this branch.

## 2. Fixed on this branch (commit `961051f`)

### AI-01 (P2 — data integrity, import tamper vector) — FIXED + REGRESSION TESTS + BROWSER-VERIFIED

- **Defect:** `validateSnapshot` validated family contexts only by shape; an asset/loan event whose `assetContext.assetId`/`loanContext.loanId` referenced a record absent from the file was accepted (the reverse direction — record→event — was checked at `localTransferService.ts:2378-2396`; the deposit→order direction was checked at `:1706-1711`; asset/loan event→record was not). Imported orphans counted in every ledger and were **uncorrectable**: the FT-03 family guard blocks general correction and deep-links to `/assets/:id`/`/loans/:id` pages that render «غير متاح محليًا»; MIC-10/11 only iterated real records.
- **Fix (layer 1 — import rejection):** `localTransferService.ts` `validateSnapshot` now requires every `assetContext.assetId` ∈ file's `assetIds` and every `loanContext.loanId` ∈ file's `loanIds`, mirroring the deposit check. Legitimate legacy/current files are unaffected (live writes always pair record+event atomically via `commitAssetRecord`/`commitLoanRecord`; exports always embed both arrays).
- **Fix (layer 2 — defense in depth):** MIC-10/11 gained a reverse orphan sweep over live data (`integrityCheckService.ts`) — a ghost-context event now fails the check with `حدث-أصل-بلا-سجل:<eventId>` / `حدث-قرض-بلا-سجل:<eventId>` offenders.
- **Regression tests:** `localTransferService.familyOrphan.test.ts` (4 cases: hand-merged asset orphan rejected; loan orphan rejected; intact hand-merged file still accepted — proving the rejection comes from the orphan check, not the stripped envelope; ghost-context injection with other records intact rejected) + 3 MIC-10/11 ghost cases in `integrityCheckService.test.ts` (asset ghost FAIL, loan ghost FAIL, paired records PASS).
- **Browser verification (live):** a real exported envelope was hand-merged (integrity + counts stripped), its `data.assets` emptied, and imported through the Settings import path — rejected with «الملف ناقص أو لا يطابق بنية Micro المطلوبة. بقيت بيانات هذا الجهاز دون تغيير.»; the live asset remained present after rejection.
- **Harm closed:** uncorrectable ghost ledger entries via tampered/merged files.

### AI-02 (P3 — duplicate-submit window) — FIXED + REGRESSION TESTS + BROWSER-VERIFIED

- **Defect:** `AssetEditor`, `LoanEditor`, `RepaymentSheet` protected saves only with the async `saving` state (button disable after re-render). A same-tick second invocation — notably the UnsavedChangesGuard's programmatic «احفظ واستمر» path while a save is in flight — bypassed the disabled attribute, and the services generate fresh ids/keys per call, so the second call duplicated the record. (The `idempotencyKey` refs in the two editors were dead code — never passed to the service.)
- **Fix:** synchronous `saveInFlightRef` guards (early return + try/finally release) in all three writers; dead refs removed. Mirrors the pattern `FinancialEventEditor` already uses for its service-level key.
- **Regression tests:** guard-path double-invoke tests in `G4Assets.dom.test.tsx` (button save in flight + guard-triggered save → exactly one `create` call) and `G4Loans.dom.test.tsx` (same for `loans.create`; plus a triple-click user-contract test for the repayment sheet). **Negative controls verified:** with the guard temporarily removed, the AssetEditor and LoanEditor tests FAIL (the repayment-sheet contract test passes via the disabled layer — documented honestly in the test comment as locking the user-visible single-write contract, with the ref layer covered by the sibling tests).
- **Browser verification (live):** triple programmatic click on «احفظ الأصل» → exactly one asset; double click on «احفظ القرض» → exactly one loan.

## 3. Findings register (consolidated from SA-1…SA-5, deduplicated and reclassified)

Statuses: FIXED (this branch) · OPEN-P2/P3 (actionable, small) · OWNER (NEEDS_OWNER_DECISION — alternatives documented, no unilateral code) · RECLASSIFIED (was P1 in a specialist report; see notes).

| ID | Sev | Title | Status | Evidence (file:line) | Required action |
|---|---|---|---|---|---|
| AI-01 | P2 | Import accepts orphan family-context events (uncorrectable ghosts) | **FIXED** (`961051f`) | `localTransferService.ts` (validate + new sweep), `integrityCheckService.ts` (MIC-10/11) | merged with owner review |
| AI-02 | P3 | Double-submit window in Asset/Loan/Repayment writers | **FIXED** (`961051f`) | `AssetEditor.tsx`, `LoanEditor.tsx`, `RepaymentSheet.tsx` | merged with owner review |
| F-1 | P1 | Waste/unallocated-consumption disclosed but not netted in `resultMinor` (Zman INV-25 nets) | **OWNER** — contract amendment required | `projectFinancialService.ts:690-701` (disclosure), contract 05 §3.2.1 | choose: keep disclose-only (current) / net into result (Zman parity) / prompt explicit `loss_non_cash` event; **do not code before decision** — financially ambiguous |
| F-2 / P1-1 | P1 | No Zman→Micro migration bridge + 10× money-scale hazard (fils ÷1000 vs minor ÷100; `MoneyMinor` unbranded) | **OWNER** — strategy + hardening | `Z lib/money.ts:1-2` vs `D/shared/currency.ts:1-4`; Zman backup itself partial/non-restorable (`Z BackupModal.tsx:31-71`) | decide fresh-start (current, documented) vs bridge; before any bridge: explicit ÷10 conversion + owner-approved rounding + branded type/test hardening |
| P1-2 | P1 | Credit-sale accounting model mismatch (Zman books uncollected remainder as cash-in at delivery; Micro models receivable) | **OWNER** — reconciliation mapping | `Z finance/actions.ts:1582-1601` vs Micro fulfillment/settlement model | document the mapping for any future onboarding/reconciliation guide; Micro model is the safer one — do not weaken it |
| P1-3 | P1→**RECLASSIFIED** | "Editable templates/snippets not transferred" | **RECLASSIFIED**: snippets = EXCLUDED_BY_OWNER; templates = documented owner rejection (never-build list); residual value → P3 (share-draft customization) | `Z orders/db.ts:144`, `Z snippets/db.ts:4` vs `shareMessageService.ts:16-130` | optional P3: per-kind draft editing (see UXD-01 synergy) |
| AI-01-res | — | (SA-5 residual sub-items folded into AI-01 fix scope) | FIXED | MIC sweep covers reverse direction | — |
| P2-1 / F-2b | P2 | Money-unit 10× semantic boundary between the two products | OPEN (dormant; same root as F-2) | money representations | encode in any future transfer contract; brand `MoneyMinor` eventually |
| P2-2 | P2 | Quantity/cost-basis model difference blocks exact history migration | OPEN (same family as F-2) | Z integer+weighted-avg vs Micro milli+value | part of the migration decision |
| P2-3 / F-5 | P2 | Category rename/merge management absent (label frozen; correction-only) | OPEN-P2 (actionable) | `types.ts:58-61`, `policies.ts:145-151` | either accept free-tag philosophy or add a category-correction flow via `commitFinancialEventReplacement` (needs owner nod) |
| P2-4 | P2 | INV-4 manual-sale↔order linkage has no Micro mapping (ambiguous: direct sale vs order collection) | OPEN-P2 (documentation) | `Z finance/actions.ts:1124-1130` | write the mapping note in the owner onboarding guide |
| P2-6 | P2 | Wallet archival/retirement absent (Zman `archiveAccount` refuses with balance) | OPEN-P2 (actionable, additive) | `D/cash-continuity/types.ts:12-20`; no archive code in `CashWallets.tsx` | add retire-with-nonzero guard if multi-wallet clutter becomes real; safe additive change |
| P2-7 | P2 | Collections cannot be back-dated (late-recorded collection lands in wrong period; no date field in Collect sheet) | OPEN-P2 (actionable, additive) | `fulfillmentService` (now-based events), `projectFinancialService.ts:989`, Collect sheet | add optional occurred-on date + attribution through the canonical reader; requires a small contract note — not speculative UI, but period attribution is financial: implement after a one-line owner confirmation |
| F-3 | P2 | Unrecorded depreciation proposal visible but not netted until recorded (Zman auto-nets read-time) | OPEN-P2 (by design; disclosure exists) | `assetService.ts:123`, `projectFinancialService.ts:627-629,698` | keep (Micro's explicit-recording philosophy) or fold into F-1 contract decision |
| F-4 | P2 | MIC-3/5/6 reserved-unimplemented; no single-balance equation analog of IC-1/IC-6 | OPEN-P2 (structural, accepted) | `integrityCheckService.ts` | document as accepted design (write-time invariants + MIC-14/15); implement only if a drift class ever appears |
| F-6 | P2 | Deposit refund nets `collectedMinor` instead of gross cash-out entry (thinner gross-cash audit trail than Zman) | OPEN-P2 (honest, documented) | `D/craft-order/policies.ts:932` | accepted model difference; note for accountants in onboarding guide |
| F-7 | P2 | Zman's global idempotency key can block legitimate retry after reversal (returns ok with no data) | OPEN — **transfer guidance, not a Micro defect** | `Z finance/actions.ts:1456-1472` | never port this pattern (Micro already uses attempt-suffixed keys); recorded so future transfers avoid it |
| UXD-01 | P2 | `/share/preview` single deep entry + divergent statement-share pattern | OPEN-P2 (UX choice) | `OrderDetail.tsx:1158`, `navigationContract.ts:164` | add statement «شارك» through preview, or record single-context intent in contract 33 |
| UXD-02 | P2 | Owner-withdrawal single-entry discoverability tradeoff (X-05 deliberate) | OPEN-P2 (documented tradeoff) | `OwnerEntitlement.tsx:662` | optional «اسحب لنفسك» affordance in Finance hub |
| P3-1 | P3 | `categoryLabel` max 80 vs Zman 200 (truncation on input) | OPEN-P3 | `FinancialEventEditor.tsx:826` | raise limit if long labels appear in practice |
| P3-2 | P3 | Statement grouping case-sensitive (mixed-case duplicates split groups; rare in Arabic) | OPEN-P3 | `statementService.ts:508` | case-fold grouping key |
| P3-3 | P3 | Purchase-edit expected-quantity guard skipped when cleared to null | OPEN-P3 | `supplierPurchaseService.ts:222` | tighten null handling |
| P3-4 | P3 | Schedule completion idempotency uses first (not last) delivered event | OPEN-P3 (harmless: monotonic) | `scheduleService.ts:206-208` | align with FT-01 convention opportunistically |
| AI-02-res a | P3 | Deposit refund lacks the wallet mirror FT-02 gave to sales | OPEN-P3 (policy) | deposit refund path | mirror-reversal policy decision (small) |
| AI-02-res b | P3 | Crash-window duplicate between service write and navigation (theoretical) | OPEN-P3 (accepted) | — | accepted residual; service-level idempotency keys would need contract change |
| UXD-03 | P3 | Header context label falls back to wordmark on 5 paths (duplication) | OPEN-P3 | `navigation.ts:36-40` | add contextual labels or suppress fallback span |
| UXD-05 | P3 | `/cash/transfer` single entry from wallets only | OPEN-P3 | `CashWallets.tsx:187` | optional Finance-hub quick action |
| UXD-06 | P3 | OrderDetail primary CTA not docked | OPEN-P3 | `OrderDetail.tsx:353-429` | dock the next-step CTA on long pages |
| UXD-07 | P3 | Vestigial `/orders/new` compat shim + fallback entry | OPEN-P3 | `NewDraft.tsx:14-16`, `navigationContract.ts:143` | retire with a note when safe |
| UXD-08 | P3 | ISO fallback in date render (unreachable with valid domain dates) | OPEN-P3 | `Statement.tsx:78` etc. | keep honest fallback; optionally format defensively |
| F-10 | P3 | MIC-14/disposal message display rounding drops sub-qirsh remainders (text only) | OPEN-P3 | `integrityCheckService.ts:1013,1020` | message-only cosmetic |
| SA-5 misc | P3 | DP-01 counts bypass for non-integer/missing values; digest unsigned; FT-02 comment drift; `reverseDepreciation` ignores disposed status; single-slot dirty registry; crash-window draft duplicate | OPEN-P3 batch (documented in SA-5) | various | hardening backlog; none user-visible |

## 4. The three owner decisions (P1, deliberately not coded)

1. **F-1 — waste netting vs disclosure.** Zman subtracts write-offs from profit (`Z pnl.ts:277`); Micro discloses `generalInventoryWasteMinor`/`unallocatedInventoryCostMinor` with status degraded to `incomplete` and reasons listed, without netting (`projectFinancialService.ts:690-701`). Alternatives: (a) keep disclose-only (current contract 05 §3.2.1); (b) amend the contract to net (Zman parity; changes period results for existing owners); (c) prompt an explicit `loss_non_cash` event when a valued waste movement exists (keeps netting owner-explicit). Each alternative changes financial meaning → owner decision before any code.
2. **F-2/P1-1 — migration bridge vs fresh start.** No importer for Zman Postgres data exists; Zman's own backup is partial and non-restorable, so a bridge would need to read a Zman database dump, convert 10× money scale, map quantities (integer+weighted-average → milli+value), map remainder-as-cash-in rows to receivable/collection events, and preserve audit history. Alternatives: (a) fresh start (current, documented); (b) build the bridge with the four hardenings above. Strategically ambiguous → owner decision.
3. **P1-2 — credit-sale reconciliation mapping.** Not a defect (Micro's receivable model is safer), but the two apps will show different period cash for the same business reality; any owner-side comparison or future onboarding documentation needs the explicit mapping table → owner decision on where to document it.

## 5. What was deliberately NOT fixed (and why)

- **P2/P3 UX placement choices (UXD-01/02/03/05/06/07):** placement and copy decisions are product choices; the continuation prompt authorizes fixes only when the intended behavior is unambiguous. All are documented with concrete suggested actions.
- **P2-7 collection back-dating:** additive and valuable, but it changes period attribution — a financial-meaning-adjacent change; implementing it without a contract note would violate the fix policy. Filed with a precise action plan.
- **F-1/F-2/P1-2:** financially ambiguous by definition.
- **Snippets:** excluded by owner instruction; never implemented; recorded as EXCLUDED_BY_OWNER.

## 6. Release-integrity notes

- No tokens, credentials, `.env` files, or sensitive exports were committed; write tokens were used only in local `git remote set-url` configuration.
- No lockfile changes, no gate weakening: lint baseline remains `--max-warnings 37` with the same 37 pre-existing warnings; all gates pass identically before and after the fixes.
- The branch adds 1 new test file and extends 3 existing ones; full suites pass (see test-evidence file).
