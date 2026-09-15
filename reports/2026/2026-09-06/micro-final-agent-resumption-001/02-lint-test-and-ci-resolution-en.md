# 02 — Lint, Test, and CI Resolution

## 1. The lint ceiling repair

### 1.1 Precise diagnosis

The approved ceiling is `--max-warnings 37`. The interrupted execution ended at **40 warnings**. Baseline comparison (lint run in a detached worktree at `origin/main` = `1601fd9`, exactly 37 warnings) isolated the **three genuinely new warnings**, all introduced by commit `c502b6b` (FC-06/Conflict E):

1. `src/domain/craft-order/policies.ts:934` — `settleDeposit` complexity (extracted from the deposit-settlement work).
2. `src/domain/craft-order/policies.ts:1121` — `reclassifyRetainedDeposit` complexity.
3. `tests/domain/craft-order.test.ts:1003` — Conflict E describe block exceeding the 60-line function limit.

(Three other apparent "new" warnings were line-number shifts of baseline warnings in `transitionOrder` and the same test file — verified by content-level diff against the baseline warning set, not by count alone.)

### 1.2 The repair (no ceiling change, no rule disable)

- The interrupted run had **already started** refactoring `settleDeposit`/`reclassifyRetainedDeposit` (uncommitted working-tree changes driven by persisted scripts). The resumption verified that refactor was complete and type-safe, then finished the third warning by splitting the Conflict E describe into three blocks (`partial classification and mixed meaning`, `partial classification correction`, `legacy retained deposit reads`) — mirroring the file's existing single-it describe pattern.
- **Result: 0 errors / 37 warnings — exactly at the approved ceiling.**
- No ceiling increase, no `eslint-disable`, no rule configuration change, no generated-file exclusion. `git diff` on `eslint.config.*`: none.

### 1.3 Follow-on integrity fixes discovered by running the full chain

- `pnpm format:check` failed on 5 files (3 of them from the interrupted commits) — normalized with Prettier (formatting only, commit `96d7bac`). This is direct evidence the interrupted run never ran the full validation chain.
- `pnpm text-density` failed on 5 surfaces (Finance 285>277, OrderDetail 179>171, AgreementEditor 62>60, Collect 48>46, DraftEditor 48>47) — all restored within caps (commit `c50a2b6`):
  - **Finance:** per-event correction actions, previews, and the WF-04 expense-classification form moved behind one collapsed named disclosure «تصحيح هذه العملية» — the same §10.2 rule-1 pattern the owner already approved for OrderDetail's «تصحيحات موثقة على الطلب». Nothing deleted; **cap lowered 277→257 as a documented ratchet gain** in `scripts/text-density-count.py`.
  - **OrderDetail:** removed aria-labels/placeholder literals whose accessible names already exist via wrapping labels (two DOM-test queries updated to the implicit names — label normalization, not assertion weakening); dead ternary inside the cancelled-only settlement panel and the mixed-meaning prose rendered as static JSX per project convention.
  - **Collect:** unified `عميل/زبون بلا اسم` and the two unnamed-debt qualifiers into single canonical strings.
  - **DraftEditor / AgreementEditor:** optional hints shortened to the already-counted «اختياري»; one redundant placeholder dropped.

## 2. Full validation chain — actual final counts

Run on the final branch head `bfc41f9` after all repairs (and re-run end-to-end as the exact CI gate `pnpm check`):

| Gate | Result | Actual count / evidence |
| --- | --- | --- |
| `typecheck` (root) | PASS | 0 errors |
| `prototype:check` (app tsc) | PASS | 0 errors |
| `lint` | PASS | 0 errors / **37 warnings** (ceiling 37) |
| `format:check` | PASS | all files conform |
| `text-density` | PASS | all surfaces within caps; Finance 257/257 (cap lowered), OrderDetail 171/171, Collect 46/46, DraftEditor 47/47, AgreementEditor 60/60 |
| `design-guards` | PASS | no raw hex, all values on scale; stylelint clean |
| Domain tests | PASS | **23 files / 285 tests** (baseline 278 → +7 from Conflict B/E/C/D work) |
| Prototype + DOM tests | PASS | **125 files / 835 tests** (baseline 818 → +17 from AV-08/AV-09/WF-04/FC-06/AV-07/Conflict B) |
| Targeted G2/G5/group2 | PASS | 28/28 (`G2.dom.test.tsx` 7, `G5Activity.dom.test.tsx` 3, `group2InventorySurfaces.test.tsx` 18) |
| `prototype:build` | PASS | PWA generateSW, 96 precache entries (2102.68 KiB); main chunk 613.10 kB / gzip 144.98 kB (pre-existing >500 kB warning, unchanged) |
| `pnpm audit --audit-level high` | PASS | no known vulnerabilities |
| Secret scan of the tree | PASS | no `github_pat_`/`ghp_` patterns in any tracked file |

## 3. CI resolution

- **PR #158** run `34027069962`: `checks` job **success** — every step green (install frozen-lockfile, bounded audit retry, lint at 37, full `pnpm check`, artifact upload).
- **`main` after merge** (`4af025d`): run `34027176232` — status recorded in `06-final-qa-and-merge-evidence-en.md`.
- No gate was weakened, no check bypassed, no CI configuration modified in this cycle (the workflow file is untouched by this branch).

## 4. Test-count honesty

Historical counts (945 total at PR #156) were **not copied**. The actual final counts are 285 domain + 835 prototype = **1120 tests**, plus 28 targeted re-runs of the G2/G5/group2 suites. The delta from baseline is fully explained by the recovered commits' new tests (documented in 01 §1.3).
