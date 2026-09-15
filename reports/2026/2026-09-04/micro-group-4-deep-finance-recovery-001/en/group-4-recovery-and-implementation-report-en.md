# Group 4 Recovery and Implementation Report — Deep Finance (Assets, Loans, Retained Deposits, Inventory Automation)

Program: Zman→Micro capability transfer (six groups) — Group 4, recovery session.
Baseline: Micro `main @ 67d4e41` (Groups 1–3 merged via PRs #149–#151).
Final: Micro `main @ 05669a9` (PR #152 merged; local == remote; clean tree; CI green).
Date: 2026-09-04. Branch: `agent/group4-deep-finance` (f20f513 → dbd5f15 → 632af0f → 455bb11).

## 1. Recovery gate — what the previous run left behind

The assignment began as a resumption: the previous Group 4 agent stopped after the implementation commit was pushed but before verification, merge, and delivery. The recovery gate discovered the exact stopping point before any edit:

- Remote Micro `main`: `67d4e41` (Group 3 merge). Local HEAD: `f20f513` on `agent/group4-deep-finance`, clean tree, already pushed; PR #152 open at that head.
- The implementation commit `f20f513` (74 files, +7,753/−54) contained the full Group 4 scope: 9 new financial-event types, 3 optional delta columns, asset/loan/craft-order/catalog domain modules, 6 atomic IndexedDB+Memory commit transactions, asset/loan/retained-deposit services, canonical reader extensions, MIC-10..13 integrity checks, schema 34 / export 26 with migration, 6 new pages plus RepaymentSheet and Finance layers, and 27 domain + 56 app/dom tests.
- Sub-agent research and adversarial review from the interrupted session were preserved in the worklog: 4-a (Zman deep-finance map), 4-b (Micro integration map), 4-c (adversarial review of f20f513 — verdict "no blockers", 6 REQUIRED-FIX, 9 RECOMMEND).
- CI run 33861709388 on f20f513 had failed at the "Verify domain and prototype" step; the audit and lint steps had passed. The failure was reproduced locally: `prettier --check` on `tests/domain/craft-order.test.ts` (one blank-line violation) — a real source-format failure, not infrastructure.
- Stale branches from the pre-2026-09-03 program era (`agent/group4-final-acceptance`, `agent/group5-*`, `agent/group6-*`, `agent/close-everything`) were identified as a different lineage (based on PR #145, before the current Group 1–3 transfer program) and left untouched; PR #141 (task/direct-sale, same old era) was left untouched as out of scope.

No work was discarded, reset, or rebuilt. The recovery map was written to the worklog before any edit, and all subsequent work was applied on top of the preserved implementation.

## 2. Work preserved, newly implemented, and corrected

**Preserved verbatim** (previous session, commit f20f513): the entire deep-finance core — financial-event domain (9 types with mandatory linked contexts), asset domain (acquisition / straight-line depreciation with last-month sweep / disposal / write-off / contract revision), loan domain (principal, repayments with documented reversal, over-repayment guard), retained-deposit classification (pending default, owner-money/revenue, reverse+replace correction), delivery automation contract D4 (atomic single-confirm consumption), storage schema 34/export 26 with honest 25/33 migration, canonical period reader (4 new result terms + 3 position layers), MIC-10..13, and the six Arabic surfaces.

**Corrected** (this session, commit dbd5f15 — the six REQUIRED-FIX findings of the adversarial review 4-c, plus four RECOMMEND):

1. Cash statement hid the four new cash-moving families. `statementService` now surfaces asset purchases paid, asset disposal proceeds, loans given, and loan repayments received in cashOut/cashIn with explicit not-expense / not-withdrawal / not-revenue qualifiers, deep-linked sources to `/assets/:id` and `/loans/:id`, and corrections-block coverage for all four types.
2. The import validator ignored the new delta columns on legacy-type events. It now rejects legacy types carrying non-zero asset/loan/revenue deltas, cross-checks every deposit-classification event's `orderId` against the orders actually present in the file, requires reversal events to negate all eight delta columns and carry matching contexts, and enforces amanah-style aggregate non-negativity for the asset, loan, and retained-revenue columns.
3. Deep-link return paths were missing. `canonicalReturnFor` resolves `/assets/:id` → `/assets` and `/loans/:id` → `/loans`; both editors now navigate to detail carrying `?from`.
4. The asset acquisition correction (`correctAcquisition`) was implemented and tested but unreachable from any surface. AssetDetail gained the "صحّح قيمة أو طريقة الاقتناء" card with effect preview, required reason, and no-change guard.
5. MIC-13's link extraction was wrong (`split(":")[2]` returned the order id because the delivery-event id itself contains colons, so the link check never matched anything) and its first mirror branch was dead code. It was rewritten: extraction between the deterministic `${orderId}:deliver:` prefix and the last colon; mirror check actually enforced for reversed deliveries; scoping to consumption movements only.
6. Depreciation `asOf` was hardcoded to today, breaking the contract's owner-chosen date. AssetDetail now exposes "سجّل حتى تاريخ" (defaults to today).

RECOMMEND fixes in the same commit: `window.prompt` for depreciation reversal replaced with an inline documented-reason form; reversed originals marked in the asset history (`data-reversed`, "عُكِس لاحقًا"); AssetEditor blocks saving an asset the owner just classified as "consumed immediately" (guiding to the expense path instead); no-change correction guards in `correctLoan` and `correctAcquisition`.

**Polished** (commit 632af0f — the two REQUIRED-FIX findings of review 4-d): the residual `window.prompt` in LoanDetail's repayment reversal replaced with the same inline-reason pattern; Arabic-Indic digits removed from the two visible strings (life-months validation, correction placeholder) and the validation message now describes the real unknown path (leave the field empty).

## 3. Verification

All gates ran locally at the final pre-merge head (632af0f) and were independently re-run by sub-agent 4-e; the domain suite was re-run again on merged main:

- Typecheck: root and prototype clean.
- Lint: 0 errors, exactly 37 warnings (the repository's frozen baseline).
- Format: `prettier --check src tests` clean (the CI root cause fixed).
- Text density: all surfaces within caps (Statement ratcheted 89→101 and AssetDetail 36→41 with documented owner-decision notes in `text-density-count.py`).
- Design token guards + stylelint: clean.
- Domain tests: 277/277 in 23 files (re-run green on merged main 05669a9).
- Prototype tests: 717/717 in 110 files.
- Production build: PWA success (91 precache entries).
- Local dependency audit: no known vulnerabilities.
- Regression reconciliation (4-e): zero test files removed; 10 added; 6 existing files gained tests only; no count decreased anywhere.
- Security scans (4-e): zero token/secret/key matches in the full diff; no console.log, TODO/FIXME, hex literals, or network calls added; financial-event writers confined to the service layer.

## 4. Zman adopt / do-not-copy

Adopted from Zman (journeys and invariants, rebuilt with Micro's stronger contracts): the asset question journey ("هذا الشيء للاستخدام لفترة طويلة أم مصروف ينتهي الآن؟"), read-time computed non-cash depreciation layered over the cash ledger, loans as an asset with derived-not-stored outstanding balance, deposit retention as reclassification rather than new cash, per-movement immutable unit cost with book-value sweep. Not copied (Zman's unsafe patterns, flagged by 4-a): history-rewriting in-place reclassification (Micro uses reverse+replace), retroactive soft-delete restatement, silent negative inventory, and the missing pre-confirm consumption preview.

## 5. Limitations (genuine, unresolved)

- The `autoConsumeOnDelivery` template flag remains a read-only declaration (banner) rather than differentiating row defaults — a documented conscious decision per contract 29 (movements stay inside the single atomic confirmation); noted for a future group.
- OrderDetail's deposit-classification panel describes effects qualitatively; the numeric "هذا التغيير سيؤثر على الرصيد كالتالي…" line pattern is not yet applied there (the amount is shown in the header).
- Ad-hoc plurals ("N قرضًا قائمًا") in some new list surfaces do not use `formatArabicPlural` for counts 1–2.
- AssetDetail's three correction forms share one `reason` input (typing in one pre-fills the others).
- The delivery-review initial-dirty false positive (G3-inherited) remains.
- Agreement-deposit wallet attribution remains deferred to unallocated (Group 3 limitation, unchanged).
