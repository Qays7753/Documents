# Group 4 — Reconciliation and Test Evidence

Micro deep-finance extension. Baseline `main @ 67d4e41` → final `main @ 05669a9` (PR #152). All gates below ran at the final pre-merge head (632af0f), were independently re-executed by sub-agent 4-e, and the domain suite was re-run on merged main.

## 1. Reconciliation checks (MIC — PASS / WARN / FAIL, read-only, never auto-repair)

Group 4 extends the IntegrityCheckService with four checks (10..13) in the established MIC pattern — sequential reads, offender ids, deep links, no writes:

| Check | Domain | Failure means |
|---|---|---|
| MIC-10 | Assets | acquisition vs cash/payable linkage, disposal/write-off event references, over-depreciation beyond schedule |
| MIC-11 | Loans | principal event linkage, repayment reversal mirror, over-repayment, loan/record consistency |
| MIC-12 | Retained deposits | classification event vs order state, single classification, revenue not double-counted, pending visibility |
| MIC-13 | Delivery consumption | every consumption movement's deterministic key resolves to a real delivered event; every reversed delivery has its movement mirrors (rewritten this session — see the inventory report) |

The aggregate import-time guards complement these: amanah/asset/loan/retainedRevenue delta sums can never import negative; deposit classification events must reference existing orders; reversals must negate all eight columns.

## 2. Acceptance-scenario coverage map (the 24 required scenarios)

| # | Scenario | Evidence |
|---|---|---|
| 1 | Asset purchase, immediate payment | assetService create + G4Assets dom (cash −60.00, assetDelta +60.00, opex 0) |
| 2 | Asset purchase payable | domain asset tests (payable +A, cash 0) |
| 3 | Operating expense not treated as asset | FinancialEventEditor type separation + editor longUse="no" block with expense guidance |
| 4 | Known / unknown useful life | G4Assets dom (life 24 saves; life 0 rejected) + unknown-life list honesty («عمره مجهول») |
| 5 | Delayed depreciation start | domain: day-aware fullMonthsElapsed from a start after purchase |
| 6 | Depreciation correction | AssetDetail inline reversal + reverseDepreciation service test + history mark |
| 7 | Disposal and write-off | domain two-amount disposal + write-off; dom detail surfaces with announced economics |
| 8 | Outgoing loan + partial/full repayment | loanService + G4Loans dom (sheet, full-remaining chip) |
| 9 | Loan correction without profit distortion | correctLoan reverse+replace; no expense/revenue deltas; below-repayments guard |
| 10 | Retained deposit left pending after cancellation | craft-order cancelOrder → needs_review; OrderDetail pending surface + Finance layer count |
| 11 | Retained deposit classified as owner money | G4RetainedDeposit dom (ownerCapital +D, cash 0) |
| 12 | Retained deposit classified as project revenue | dom (retainedRevenue +D, recognized once, no second cash) |
| 13 | Reversal/correction of deposit classification | reverse+replace with 3 events asserted in dom test |
| 14 | Delivery with tracked components and explicit preview | G3Delivery dom + DeliveryReview per-row preview |
| 15 | Repeated delivery attempt without duplicate movement | deterministic keys + store dedupe (service + IDB tests) |
| 16 | Untracked components without quantity movement | suggestedAction skip + non-skip rejection (service guard) |
| 17 | Shortage and controlled negative policy | shortage rows + non-negative guard + live warning |
| 18 | Delivery-linked reversal | reverseDelivery mirror + review unlock; MIC-13 negative fixture |
| 19 | Non-cash waste and correction | contract 28 suites (in the 717 run) + asset write-off separate meaning |
| 20 | Reconciliation PASS/WARN/FAIL fixtures | integrity suite 17/17 incl. two negative MIC-13 fixtures |
| 21 | Legacy export/import + current round trip | schema34 suite 8/8 (25/33 acceptance, 26/34 round trip, 4 validator negatives) |
| 22 | Offline, reload, interrupted save, duplicate tap, recovery | atomic IDB transactions + idempotency keys (IDB group4 5/5, delivery reuse tests) |
| 23 | RTL 360–390px browser QA | 4-d RTL/digits/keyboard/bdi audit across all six new surfaces; conventions verified |
| 24 | Full Groups 1–3 regression suites | 277/277 + 717/717 include every prior suite; 0 test files removed |

## 3. Final gate table

| Gate | Result |
|---|---|
| Root typecheck | clean |
| Prototype typecheck | clean |
| Lint | 0 errors / exactly 37 warnings (frozen baseline) |
| Prettier check | clean (CI root cause fixed) |
| Text density | all surfaces within caps (Statement 101, AssetDetail 41 — ratcheted with owner-decision notes) |
| Design token guards + stylelint | clean |
| Domain tests | **277/277 (23 files)** — re-run green on merged main 05669a9 |
| Prototype tests | **717/717 (110 files)** |
| Production build | PWA success (91 precache entries) |
| Local dependency audit | no known vulnerabilities |
| Security scans | 0 secrets / 0 console.log / 0 TODO / 0 hex / 0 network calls in the diff |
| CI (GitHub Actions) | run 33867065062 SUCCESS (all steps + Cloudflare Pages) |

## 4. New test inventory (Group 4 totals)

- Domain (root): 27 new tests — asset (new file), loan (new file), financial-event +9 types/deltas/context guards, craft-order retained-deposit classification + reclassification, catalog template flag, public-surface barrel additions.
- App: G4 suites at f20f513 — assetService 9, loanService 6, retainedDepositService 7, schema34 4, IndexedDb group4 5, integrity MIC 15; plus this session — statement +2, schema34 +4, integrity +2, no-change guards +2.
- Dom: G4Assets 5 (incl. acquisition-correction surface), G4Loans 3, G4RetainedDeposit 3; G3Delivery re-run green.
- Totals moved: domain 246→277; prototype 660→717; regression reconciliation: 0 files removed, 10 added, 6 gained tests only, no count decreased anywhere.

## 5. Sub-agent verification

Five specialized reviewers participated across the two sessions: 4-a (Zman deep-finance investigation), 4-b (Micro transaction-integrity integration map), 4-c (adversarial review of the implementation — 6 REQUIRED-FIX, all applied), 4-d (inventory automation + Arabic RTL UX — no blockers, 2 polish items applied), 4-e (final adversarial QA — verdict READY FOR CI+MERGE with the full gate table re-executed independently). Full logs are in the sub-agent synthesis report and the shared worklog.
