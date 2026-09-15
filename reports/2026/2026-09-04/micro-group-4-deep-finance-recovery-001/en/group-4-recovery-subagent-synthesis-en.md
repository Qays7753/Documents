# Group 4 — Recovery Sub-Agent Synthesis

Five specialized sub-agents participated in Group 4 across the interrupted implementation session and this recovery session. All were read-only (research/review; no pushes, no code changes). This report consolidates their findings and the parent's disposition of each.

## 1. 4-a — Zman deep-finance investigator (previous session)

Delivered the reference map: capital-asset table and floor-formula depreciation with last-month sweep; receivables as loans with derived-not-stored balance and overpay guard; deposit forfeiture as reclassification (no new cash); delivery deduction with tracked-only whitelist and weighted-average COGS; write-off badges. Produced the transferable-invariant list and the UNSAFE-pattern list (retroactive depreciation cancel on soft-delete, in-place reclassification, no consumption preview, silent negative inventory, no true waste reversal, forfeiture visible as a manual sale). Disposition: invariants adopted and rebuilt with Micro's stronger contracts; every unsafe pattern explicitly avoided (reverse+replace instead of history rewriting; explicit preview; policy-marked shortage).

## 2. 4-b — Transaction-integrity investigator (previous session)

Mapped Micro's plug points: the amanah precedent for new delta columns; the canonical `readRecordedPeriodResult` as the single period product; deposits' pending state (`needs_review`) with no FinancialEvent anywhere; delivery deterministic keys and the 5-store atomic commit; schema 33/25 migration chain; the MIC-8 pattern for new checks; the dom-test harness model; and the call-site discipline (no new `createFinancialEvent` call sites outside the services). Disposition: the implementation followed this map exactly — 9 types, 3 delta columns, 6 atomic commits, MIC-10..13, schema 34/26.

## 3. 4-c — Adversarial reviewer of the implementation (previous session)

Audited the full 7,753-line diff and re-ran the gates locally (domain 277/277, G4 app 46/46, G4 dom 10/10, density OK). Verdict: **no blockers**; core transaction integrity (deltas, reversals, atomicity, canonical reader, guards) sound and test-covered. Found 6 REQUIRED-FIX (secondary reading surfaces, import validation, navigation wiring, unreachable correction, dead MIC-13 logic, hardcoded asOf) + 9 RECOMMEND. Disposition: all 6 REQUIRED-FIX applied in commit dbd5f15 with new tests (statement +2, validator +4, MIC-13 negatives +2, no-change guards +2, dom +1); 4 of the RECOMMEND items fixed in the same commit (window.prompt, reversed-original marking, save-blocking on "consumed immediately", no-change churn guards); the rest documented as conscious decisions or deferred limitations.

## 4. 4-d — Inventory-automation + Arabic RTL UX reviewer (this session)

Verified contract 29 end-to-end on the fixed head: open-saves-nothing, single-atomic-commit deduction, three-layer idempotency, explicit shortage, untracked-never-move, mirrored documented reversal, MIC-13 genuinely enforcing after the rewrite; RTL/digits/keyboard/bdi/offline conventions on all six new surfaces; MicroAppShell unchanged (no sixth seat, no second FAB); 14/14 dom tests green; density caps OK. Verdict: **no blockers**; 2 REQUIRED-FIX polish items (residual `window.prompt` in LoanDetail repayment reversal — the earlier fix had covered AssetDetail only; Arabic-Indic digits in two visible strings) + 6 RECOMMEND. Disposition: both polish items applied in commit 632af0f (inline reason pattern + English digits + real unknown-path guidance); RECOMMEND items recorded as limitations (deposit numeric effect line, formatArabicPlural for 1–2 counts, shared reason input, longUse skippable, G3-inherited initial-dirty, inert-by-design autoConsume flag).

## 5. 4-e — Final adversarial QA + CI-readiness reviewer (this session)

Re-executed the entire gate chain independently at dbd5f15: typecheck ×2 clean; lint 0 errors / exactly 37 warnings; prettier clean; density all OK; token guards + stylelint clean; domain 277/277 (23 files); prototype 717/717 (110 files); build OK (91 precache); audit clean. Security: zero secret/token/console/TODO/hex/network matches in the full diff. Migration: 33→34 / 25→26 pairs, honest `?? []` normalizers, IDB+Memory parity for all new stores and commits, guided import with no invention; hardened validator verified in code and by its 4 negative tests. Regression: zero test files removed, 10 added, 6 gained tests only. Deep-checked all five dbd5f15 fix areas (statement no-double-count, MIC-13 extraction against the real colon-laden key format, editors, no-change guards, CSS) — all correct. Verdict: **READY FOR CI+MERGE**, zero REQUIRED-FIX, 4 non-blocking RECOMMEND (residual prompt — since fixed in 632af0f; dead imports; statement source sign convention; a tautological filter). Disposition: merged on the green run after the prompt finding was fixed.

## 6. Consolidated outcome

- All REQUIRED-FIX findings from every reviewer were applied before the merge; no known defect remains open.
- The parent owns the final correctness of the synthesis: the merge (PR #152 → main 05669a9) happened only after 4-e's READY verdict, the two 4-d polish fixes, a green CI run (33867065062), and the green Cloudflare Pages check.
- Honest residual list (limitations, not defects): documented in the implementation report §5.
