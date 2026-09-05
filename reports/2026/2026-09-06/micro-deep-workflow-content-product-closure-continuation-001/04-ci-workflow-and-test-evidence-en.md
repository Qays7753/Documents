# 04 — CI, Workflow, and Test Evidence

## 1. Full local validation matrix (branch head `8a98835`, before push)

| Gate | Command | Result |
| --- | --- | --- |
| Typecheck | `pnpm typecheck` (root) + `pnpm prototype:check` | PASS (0 errors) |
| Lint | `pnpm lint` | PASS — 0 errors, 37 warnings (at the repo's documented `--max-warnings 37` ceiling; unchanged from baseline) |
| Format | `pnpm format:check` | PASS (after repairing 4 committed files the stopped run left unformatted) |
| Text density | `pnpm text-density` | PASS — all 52 surfaces within §10 caps; one documented cap raise (Orders 77→79, ratchet note in the script) |
| Design-token + stylelint | `pnpm design-guards` | PASS — no raw hex, values on scale, CSS lint clean |
| Domain tests | `pnpm test` | **23 files / 278 tests PASS** (baseline 277; +1 AV-05 domain test) |
| Prototype tests | `pnpm prototype:test` | **125 files / 818 tests PASS** (baseline 794; +21 recovered from the stopped run + 5 added by this continuation: AV-04 ×2, AV-05 import, AV-06, FC-03; fixture relabels kept the AI-01 suite intact) |
| Production PWA build | `pnpm prototype:build` | PASS — generateSW, 96 precache entries (~2080 KiB), pre-existing >500 kB main-chunk warning unchanged |
| Security audit | `pnpm audit --audit-level high` | PASS — «No known vulnerabilities found» |
| Secret scan | ripgrep over full `6a8c151..8a98835` diff + every changed file | CLEAN — no `github_pat_`/`ghp_` patterns |
| Working tree | `git status --short` | clean at commit time; `core.fileMode=false` neutralized the 663-mode-change environment artifact (no mode churn committed) |

Test-count reconciliation: the stopped run's log claimed 812 at an intermediate point; the verified final count is **818** (the fixture work it stopped inside was never finished, so its claimed number was never reachable — 815 after my fixture repairs and AV-04 tests, +1 AV-05, +1 AV-06, +1 FC-3 = 818).

## 2. Browser QA (production build, real headless Chromium)

Method: `vite build` output served locally; `agent-browser` (Playwright-class headless) at two viewports; interactive journeys, not screenshots-only.

| Check | Evidence |
| --- | --- |
| RTL root | `document.documentElement.dir === "rtl"`; title «Micro — شريك مشروعك» |
| 360×800 | clientWidth 360; `scrollWidth > clientWidth` false (no horizontal overflow); screenshot captured |
| 390×844 | clientWidth 390; no overflow; screenshot captured |
| Navigation invariants | exactly 1 `<nav>`, 1 `.micro-fab`; labels: مشروعي الآن، العمل، سجّل، مالي، أدواتي |
| First-run journey | Foundation setup (قرار البداية): project name → wallet (skip offered with «أسجلها لاحقًا من مالي» — unknown stays unknown) → materials → save; app entered main shell |
| Money path end-to-end | FAB «سجّل» → sheet → quick sale 12.50 JOD → save → receipt dialog («وصل التسجيل») → «افتح السجل» → `/direct-sales/:id` detail: price 12.50, collected 12.50, cost «لا أعرف الآن» (unknown preserved), date displayed 05/09/2026 (DD/MM/YYYY) |
| Unsaved-input guard | closing the sale sheet with a filled amount raised the honest alertdialog («في رقم مكتوب — تسجّله أو تتجاهله؟» → سجّله الآن / تجاهل ما كتبت) |
| Header context (MR-04) | `/direct-sales/:id` header showed «بيع مباشر» — no duplicated brand |
| Offline (PWA) | service worker active (`controller: "active"`); with network offline, reload served the finance page from precache |
| Console/page errors | **zero** at both viewports across all journeys (`agent-browser errors` and `console` empty) |

No real-device claims are made — all evidence above is from headless desktop Chromium at phone viewport sizes.

## 3. CI workflow inspection (before changes)

`.github/workflows/ci.yml` (the only workflow):

- Triggers: `push` to `main`, all `pull_request`
- Permissions: `contents: read` (least privilege)
- pnpm 9.15.9 pinned, Node 22, `cache: pnpm`
- `pnpm install --frozen-lockfile --ignore-scripts`
- `pnpm audit --audit-level high`
- `pnpm lint`; `pnpm check` (typecheck + lint + format + density + design guards + domain + prototype tests + build)

Known real failure mode: the audit step hits transient npm registry outages (`ERR_SOCKET_TIMEOUT` posting to the security-audit endpoint) — documented in the repo's own history (PRs #150/#151/#152 and commit 455bb11: retriggered manually, local audit clean). The earlier Group-6 audit prepared a hardening patch but could not apply it (token lacked Workflows scope then).

## 4. CI hardening applied (this run, with Workflows permission)

Applied the previously proposed patch, plus two repairs discovered during validation:

| Change | Rationale | Honesty check |
| --- | --- | --- |
| Audit bounded retry (3 attempts, 60 s backoff, `::error::` after the third) | registry outages are documented, real, and code-independent | no `continue-on-error`, no step removal — after 3 failures the audit still fails loudly with explicit guidance |
| `concurrency: ci-${{ github.ref }}` + `cancel-in-progress` | superseded runs waste minutes | standard; does not hide results of the latest commit |
| `timeout-minutes: 45` | protects against hung jobs | bounded, generous (typical run ≈ 4 min) |
| Tags `v*` trigger + PWA build artifact per run (30-day retention, `if-no-files-found: error`) | releases become traceable and the build product downloadable | artifact upload is additive; failure to produce it fails the job |
| PR-only `git diff --check` whitespace step | automates the PR checklist rule | additive gate, not a replacement |
| **Full-history checkout (`fetch-depth: 0`)** | first run failed: `origin/main...HEAD: no merge base` under the default shallow checkout | root-cause fix; verified locally then on the re-run |
| Patch fuzz repair | applying the old patch corrupted `branches: [main]` → `branches: ain]` | caught by reading the file + YAML parse before commit |

YAML validated by parser locally; the retry script validated with `bash -n`; local `pnpm audit` run clean before push.

## 5. CI runs — job-by-job record

### Run 33990597565 (branch commit `27d969e`) — FAILURE (infrastructure of the new step)

| Step | Result |
| --- | --- |
| Set up job / Checkout / Setup pnpm / Setup Node / Install dependencies | success |
| **Audit dependencies (bounded retry)** | **success** (first attempt) |
| Lint source and tests | success |
| Verify domain and prototype (`pnpm check`) | success |
| Verify no whitespace errors | **failure** — `fatal: origin/main...HEAD: no merge base` (shallow checkout has no common history to walk) |
| Upload artifact | skipped (job failed) |

Classification: **workflow-definition defect introduced by my own new step**, not a product failure and not a registry issue. All product gates (audit, lint, full check incl. 818 tests + build) were green on this run. Fixed at the root (`fetch-depth: 0`), pushed as `8a98835`.

### Run 33990754485 (branch commit `8a98835`) — SUCCESS (final, on the PR)

| Step | Result |
| --- | --- |
| Set up job | success |
| Checkout (full history) | success |
| Setup pnpm (9.15.9) | success |
| Setup Node (22, cache) | success |
| Install dependencies (frozen lockfile) | success |
| Audit dependencies (bounded retry) | success |
| Lint source and tests | success |
| Verify domain and prototype | success |
| Verify no whitespace errors (PR) | success |
| Upload production PWA build artifact | success |

PR #156 checks: passed. Merge into `main` (merge commit `1601fd9`) executed only after this run completed successfully.

## 6. Delivery mechanics

- Branch pushed: `agent/deep-workflow-content-product-closure` → `origin` (9 commits, 80 files, +2279/−264 vs baseline).
- PR #156 opened with a full description; **merged after checks passed**.
- Token hygiene: push URL set from an untracked file, stripped from config immediately after use; tokens never appear in commits, logs, or reports (scan in §1).
- No force push, no history rewrite, no branch deletion, no protection bypass; recovery refs kept local (branch `recovery/deep-closure-partial-work-2026-09-06` + offline bundles).
