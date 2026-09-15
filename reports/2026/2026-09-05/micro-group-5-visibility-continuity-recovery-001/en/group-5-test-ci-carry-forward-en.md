# Group 5 — Test Evidence, CI Matrix, and Carry-Forward Disclosure

## 1. Final test counts (actual, verified)

| Suite | Count | Files |
| --- | --- | --- |
| Domain tests | **277 passed / 277** | 23 |
| Prototype tests | **766 passed / 766** | 120 |

Prototype progression across the Group 5 series: 717 (Group 4 baseline) → 752 after the Group 5 implementation (`ced148f`, +35 tests) → 761 after the browser-QA dead-wire fixes and reviewer synthesis (`a5f0cd7`, `782127b`, +9) → **766** after this session's QA-recovery fixes (`4445da0`, +5: four service-level family-context regressions and one MIC-10 restore-cycle regression). Zero failing, zero skipped, zero flaky tests in the final runs; the domain suite is unchanged at 277 (the Group 5 work is application-layer by design — domain coverage was already complete from Group 4).

Both suites were re-run on merged main (`ad9fc13`) with identical results, and the whole gate chain (typecheck, lint 0/37, format, density, design-guards + stylelint, production build + PWA 96 precache entries) passed on both the push head and the merged head.

## 2. CI matrix (this delivery cycle)

| Workflow | Job | First result | Classification | Remediation | Final result | Run URL |
| --- | --- | --- | --- | --- | --- | --- |
| CI | `checks` (PR #153, pull_request, head `4445da04`) | success | — | none | success | https://github.com/Qays7753/Micro/actions/runs/33947927146 |
| CI | `checks` (push, main `ad9fc13`) | success | — | none | success | https://github.com/Qays7753/Micro/actions/runs/33948024196 |
| Cloudflare Pages | external check-run on PR head | success | — | — | success | PR #153 check-runs |

The workflow (`.github/workflows/ci.yml`) runs one job: `pnpm install --frozen-lockfile --ignore-scripts` → `pnpm audit --audit-level high` → `pnpm lint` → `pnpm check` (typecheck + lint + format + density + guards + domain + prototype + build). Both runs of this cycle passed on the first attempt — no infrastructure flakes (the npm-audit registry outages of PRs #150–#152 did not recur), no retrigger commit, no `--admin`, no protection bypass, no force-push, no test deletion, and no merge over a failed check. The local `pnpm audit --audit-level high` was also run directly and returned no known vulnerabilities.

## 3. Browser QA evidence (fresh production pass, this session)

Arabic RTL, production build served by `vite preview` with a real service worker, at 390×844 and 360×800. 33 screenshots in the session workspace (`download/g5-browser-evidence-final/`), covering: onboarding; seeded financial data; Home «آخر ما حدث» (labels, dates, amounts, deep link); the `/finance/activity` reader (filters, family chips, offline truth line); activity-row deep links to the focused event view; the statement deep layers and honest unknown result; the Markdown report card and the downloaded file's content; the 16-check integrity page with version stamps; a documented reversal with reason and its audit register entry (reason, net effect, original link); the full draft lifecycle (first-keystroke write → reload → explicit restore offer → full restore → final-save clears → discard removes) plus draft writes in all four editors; lock enable → idle veil → wrong PIN → unlock with preserved form values; share preview (customer-safe text, edit, copy + manual fallback); v27 export inspection; tamper rejection; valid-import preview → atomic restore → post-restore health check; offline reload from the SW precache and offline SPA navigation; the PWA dirty-update block with a genuine waiting service worker; and the 360×800 sweep with overflow and console-error checks. Zero console errors, zero page errors, no horizontal overflow, no Arabic-Indic digits, no wrong date formats.

Distinction note: one defect class (invisible storage feedback) reproduced identically in the clean production build — it was a real production defect (F-1), not an HMR artifact, and was fixed and re-verified on a fresh production reload. The three findings fixed this session (F-1, F-2, F-2b) each carry a regression test.

## 4. Group 4 carry-forward items — explicit disposition

| Item | Status | Disposition |
| --- | --- | --- |
| `autoConsume` as a read-only declaration vs distinct per-line value | **Open — assigned to a future group** | The template flag remains an explicit banner; movements stay inside the single atomic delivery confirmation (the documented Group 4 decision, contract 29). Group 5 surfaces consume delivery movements read-only; no change was safe or required for visibility/continuity. |
| Deposit classification numeric-effect line | **Fixed and verified** | OrderDetail's deposit panel gained the numeric effect line (Group 5 carry-forward fix); the classification surface states the effect with amounts. Verified live. |
| Plural/shared-reason input behavior | **Fixed and verified** | The nine plural sites moved to `g5Plurals.ts` with correct Arabic rules; the shared-reason input was split into three distinct reason inputs on AssetDetail (acquisition/contract/disposal). |
| Agreement-time deposit wallet attribution | **Open — assigned to a future group** | Deposit cash at agreement still enters unallocated (the Group 3/4 boundary as-is). The MIC-14 WARN surfaces the review need honestly; no silent wallet guess was added. |

## 5. Group 5-specific findings disclosure

- Activity rows and deep links: all 15 families render and deep-link to their owning surfaces; the inventory movement editor is the one surface reached by type route rather than per-record id (the pre-existing inventory navigation contract, unchanged).
- Draft editors: all four wired editors verified end-to-end (full cycle on DirectSaleEditor; write + persistence verified on the other three, including survival through the lock veil). The FAB quick-entry sheet is intentionally excluded (momentary entry).
- Share/privacy: clipboard writes may be permission-blocked by the platform; the manual fallback is the designed honest path. `navigator.share` depends on device support; copy is the fallback.
- Backup/restore: the v27 digest covers the `data` payload (the exported `counts` are informational and re-derived at import); legacy files without a digest follow the existing validation path. MIC-14's WARN prose rounds the drift to whole dinars while the drift line shows the exact value (intentional).
- Production PWA: no production-only issue remains — the offline reload, dirty-update block, and update card were verified against a real service worker in the production preview; the update card was exercised with a genuine new SW revision.
- Flaky/skipped/failing tests: **none** — the final runs are 277/277 and 766/766 with no skips and no retries.
