# Agent 1 — UX, Performance, Security, and CI Report

Companion to the main report; findings referenced here are detailed in the findings register. Arabic copy is quoted where user-visible.

---

## 1. UX / RTL / Mobile (static inspection; live 360×800 journeys were not re-driven in this audit — see limitations)

### Verified strong
- **RTL correctness:** `dir="rtl"` at html/shell/drawers/dialogs; numeric isolation via `bdi dir="ltr"` + CSS `[dir="ltr"]` with tabular figures; physical left/right only in direction-safe rules; icon mirroring correct (forward = ArrowLeft/ChevronLeft; month-prev = ChevronRight).
- **Accessibility:** global `:focus-visible` outline; focus trap + restore in unsaved-changes guard; `inert` under the lock veil; deep-link focus with scrollIntoView; 289 Arabic aria-labels across 68 files; `viewport-fit=cover` + `env(safe-area-inset-*)` on header/main/nav/sheets/editors; keyboard-open hides chrome without hiding content.
- **Numbers/dates invariant:** single money formatter (Intl en-US, 2 decimals, grouping) and a single date formatter (DD/MM/YYYY numeric); no Arabic-Indic digits in any user-rendered product string; no `<table>` anywhere (row/card lists — no table-direction risk); guard tests assert formatters.
- **Five-seat shell:** structurally and test-enforced (see invariants file).

### Fixed in this audit
- UX-01 (P1) Arabic-Indic PIN digits; UX-02 Tools loading/error/ready machine; UX-03 44×44 chip targets (scale-compliant); the new PIN-gate dialog follows the lock-overlay visual language (alertdialog, Arabic labels, masked input, backoff-aware errors).

### Documented (P3 polish list for the integration step)
- UX-04: ~60 inline `` `${formatMoneyMinor(x)} د.أ` `` renders bypass `MoneyValue`'s LTR isolation and negative styling — values are correct (one formatter); risk is sign display in RTL. Priority subset identified: CorrectionsLayer net effects, EventsLayer previews, Home away-digest.
- UX-05: Finance view toggle is a fake tablist (role="tab" without tabpanel/arrow keys) and each toggle remounts the full page (`<main key={location}>` keyed on the query string) re-running 15 aggregate reads — fix: `aria-pressed` group + key on pathname only.
- UX-06: one `input type="month"` renders locale month names against numeric MM/YYYY labels everywhere else.
- UX-07: ISO (YYYY-MM-DD) fallback leakage in ~7 spots when a stored date is unparseable (`?? lastExport.slice(0,10)` etc.) — standardize the «—» fallback of `LocalDateValue`.
- UX-08: one-tap draft discard in the restore banner (two-step confirm elsewhere).
- UX-09: `role="alert"` vs `role="status"` inconsistency in the quick-action sheet errors.
- UX-10: Catalog renders `toFixed(3)` quantities ("2.000") instead of the canonical trimmed formatter.

## 2. Performance

Baseline measurements (production build): main chunk 590.49 kB / gzip 138.38 kB; PWA precache 96 entries / 2062 KiB; single cached IndexedDB connection (regression-tested); route-level lazy-loading complete (41 routes).

| Hotspot | Evidence | Threshold | Action |
|---|---|---|---|
| Full re-read fan-out on every data change (PERF-01, P1-per-specialist, disposition: DOCUMENTED) | `PrototypeServicesContext.tsx:129-141` bumps dataVersion → Finance effect runs 15 parallel aggregate reads; activity read does `getAll` on 7 stores then slices 120; `listAll` = getAll + in-memory sort | responsive < 200 ms target; measured structurally O(dataset) | service-layer memoization keyed by (dataVersion, range) + IDB index cursors for period reads — architectural; deferred with plan (regression risk in an audit branch exceeds benefit) |
| Settings summary pipeline (PERF-02) | full export + pretty-print + pure-JS SHA-256 + full revalidation per data change | 100–300+ ms at 5 MB | direct store counts — small follow-up |
| Entry chunk composition (PERF-03) | composition root eagerly imports ~40 services + IndexedDbLocalStore (3.1k lines) + localTransferService (2.9k lines incl. all legacy migrations) | < 500 kB chunk (build warns) | dynamic-import transfer/guided-import services; split domain per feature |
| Per-keystroke draft writes (PERF-04) | 2 IDB transactions per keystroke + synchronous localStorage JSON write | typing jank on low-end devices | debounce 300–500 ms; move editor draft to the form-draft store |
| Precache weight (PERF-05) | all lazy chunks + 10 font files ≈ 348 kB precached | offline install cost on 3G | trim/subset fonts; runtime-cache same-origin lazy chunks |
| Uncapped lists (PERF-06) / recompute per read (PERF-07) | Statement/Orders map every row; aggregates re-derived per read | quadratic growth with period length | show-more increments / shared memoized computation |

Positive: single IDB connection with open-count regression test; services are module singletons; StartupGate reads the profile once per session; PWA reload respects dirty forms.

## 3. Security & privacy

### Transmission-vector verdict (production build)
| Vector | Found? |
|---|---|
| fetch / XHR / WebSocket / EventSource / sendBeacon / axios | **No** (only dev-server middleware in `vite.config.ts`, excluded from production via `devOnlyPlugins`; built `dist/public` verified clean) |
| CDN / external fonts / images | **No** — fonts and icons local; manifest icons local |
| Analytics / telemetry | **No** — no gtag/sentry/posthog; a removed analytics tag is documented in `index.html` |
| navigator.share / clipboard | user-gated, text-only, previewed before sending; clipboard `writeText` fallback (no `execCommand`) |
| Service worker | precache-only, same-origin, NavigationRoute → local index |
| CSP | present (`_headers`: `default-src 'self'; script-src 'self'; connect-src 'self'; object-src 'none'`) |

### Secret scan
Clean across tracked files and the working tree (patterns: ghp_, github_pat_, sk-, AKIA, xox*, private keys); no `.env`/`.pem`/`.key` tracked; `.gitignore` covers them; no source maps in the build.

### Lock mechanism (contract 37) — before → after
- PIN never stored/exported; record excluded from snapshot/export/reset — verified and unchanged.
- **Fixed:** PBKDF2-SHA256 (120k iterations) with transparent legacy upgrade (was single SHA-256); enforced escalating backoff in unlock + disable (was cosmetic); input-aware idle heartbeat (was visibility-only); fully opaque veil (was 0.96); masked entry; data-leaving Settings actions PIN-gated (was bypassable via exempted `/settings`).
- **Documented:** data at rest remains unencrypted by design (stated honestly); dev-only collectors must never be enabled in prod; guided-editor/setup drafts in plaintext localStorage (SP-07 — route through the form-draft store).

## 4. Code quality and CI

### Fixed
- AR-05: lint + format gates now cover the whole prototype app (root files and 30 dom-test suites were never linted; the app had no format gate — 165 files had drifted). Post-reformat: all suites green, lint ceiling unchanged (37 — all warnings are pre-existing domain-core items).
- AR-04: density guard measures all 52 routed pages (12 cash/collect/party/ledger surfaces were outside §10.1); listed-but-missing now fails; unlisted routed pages fail until measured.
- AR-02: canonical docs backfilled (current-state §25–§28, traceability, todo, CHANGELOG) for transfer Groups 3–5 and this audit — the PR template's own requirement.

### CI job matrix (single `checks` job, before patch)
checkout → pnpm 9.15.9 (pinned) → Node 22 + cache → `pnpm install --frozen-lockfile --ignore-scripts` → `pnpm audit --audit-level high` → `pnpm lint` → `pnpm check` (typecheck → lint → format → density → design-guards + stylelint → domain tests → prototype tsc → prototype tests → production build + PWA). Least-privilege token; no lifecycle scripts. **Observed on this branch: run 33960263084 success.**

### CI gaps → `proposed-ci-hardening.patch` (token lacked workflow scope)
- tag pushes (`v*`) now run the same checks; production build uploaded as an artifact (`if-no-files-found: error`, 30-day retention);
- `pnpm audit` wrapped in a bounded 3-attempt retry with 60 s waits and an explicit error classification note for the documented registry outages (PRs #150–#152 history: ERR_SOCKET_TIMEOUT — infrastructure, not vulnerabilities; local audit was clean each time);
- `concurrency` group with cancel-in-progress; `timeout-minutes: 45`; PR whitespace check automating the template rule.

### Release governance (owner decisions, documented)
- Zero tags in the repository; version pair mismatch (root 0.1.0 / prototype 1.0.0); CHANGELOG "Unreleased" — release cut, tag scheme, and version sync belong to the owner at the integration step (AR-01 mechanics are ready in the patch).
- Branch protection on `main` could not be verified from the sandbox — verify in repository settings and record it in the repository-policy decision doc (AR-11).
- Adversarial coverage matrix and remaining test debt (cross-session duplicate semantics, future-date guard, PWA reload decision as a pure function, DB-level 33→35 upgrade tests, AppLockGate idle dom suite) are listed in the test-evidence file.
