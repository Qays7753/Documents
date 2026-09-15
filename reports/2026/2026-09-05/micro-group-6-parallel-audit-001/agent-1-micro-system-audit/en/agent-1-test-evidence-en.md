# Agent 1 — Test Evidence

All numbers below are fresh runs on the audit branch `agent/group-6-micro-system-audit` @ `c1ae93e` (baseline `main @ ad9fc13`). Commands were run exactly as CI runs them.

---

## 1. Final gate table (audit branch)

| Gate | Command | Baseline result | Audit-branch result |
|---|---|---|---|
| Typecheck (domain) | `pnpm typecheck` | PASS | **PASS** |
| Typecheck (prototype) | `pnpm prototype:check` | PASS | **PASS** |
| Lint | `pnpm lint` | PASS 0 errors / 37 warnings | **PASS 0 errors / 37 warnings** (scope widened to the whole app; ceiling unchanged) |
| Format | `pnpm format:check` | PASS (src+tests only) | **PASS (src + tests + app — 165 app files newly gated & formatted)** |
| Text density | `pnpm text-density` | PASS, 40/52 pages | **PASS, 52/52 pages; missing/unlisted pages fail the check** |
| Design guards | `pnpm design-guards` | PASS | **PASS** (no raw hex, values on scale, stylelint clean) |
| Domain tests | `pnpm test` | 23 files / 277 tests | **23 files / 277 tests PASS** |
| Prototype tests | `pnpm prototype:test` | 120 files / 766 tests | **123 files / 784 tests PASS** (+3 files / +18 tests, all new) |
| Production build | `pnpm prototype:build` | PASS, PWA 96 entries | **PASS — PWA generateSW, 96 precache entries (2062 KiB), sw.js + workbox emitted** |
| Full chain | `pnpm check` | PASS | **PASS (exit 0)** |
| Secret scan | git grep patterns + tracked-file scan | clean | **clean** |
| Worktree | `git status --short` | empty | **empty** |

## 2. New tests added by this audit (18 new tests in 3 new files + 3 extended files)

| Test file | Tests | Covers |
|---|---|---|
| `application/security/localLockService.test.ts` (extended) | +4 (9 total) | PBKDF2 enable/verify; legacy single-hash record unlocks and upgrades transparently; enforced backoff inside window (no counter inflation) + counting resumes outside; disable path throttles and counts |
| `Settings.lockGate.dom.test.tsx` (new) | 4 | export gated when lock enabled; wrong PIN refused with error; correct PIN runs the action and verification holds for the session; Arabic-Indic PIN digits keep meaning; no gate when lock disabled |
| `application/finance/projectFinancialService.redelivery.test.ts` (new) | 3 | `lastEffectiveDeliveryEvent` semantics (unreversed → null after reversal → second delivery); Jan-reversal/Feb-re-delivery attributes revenue to February and zero to January; unreversed orders keep their period |
| `application/direct-sales/directSaleService.test.ts` (extended) | +3 | cancel reverses the wallet allocation (mirror with reason + reversesEntryId; wallet sum returns to zero); repeated cancel is idempotent (single reversal); cancel without attribution writes no entries |
| `EventsLayer.familyGuard.dom.test.tsx` (new) | 2 | asset event row shows owner deep link and hides general reverse/edit/delete (navigation carries `?from`); loan event row likewise; general expense events keep all three actions |
| `application/transfers/localTransferService.envelope27.test.ts` (extended) | +2 | current-version file with counts disagreeing with data is rejected (digest stays valid — counts are outside it); malformed integrity block is rejected instead of silently skipping verification |

## 3. Adversarial coverage matrix (10 negative paths × coverage)

| # | Negative path | Coverage before audit | Coverage now |
|---|---|---|---|
| 1 | Double submit (idempotency) | service-level (type+key) + DB-unique key on sales | unchanged (strong) — cross-session duplicate semantics documented (AR-07, P3) |
| 2 | Double reversal | domain + app + storage + import | unchanged (strong) |
| 3 | Malformed values | shared numeric guards + import validators | unchanged (strong) |
| 4 | Invalid IDs / dangling links | broad (reversal, assets, integrity, import) | unchanged (strong) |
| 5 | Missing contexts | required-forbidden context guards | unchanged (strong) |
| 6 | Interrupted saves (partial writes) | atomic transactions + orphan-free tests | unchanged (strong); FT-02 adds crash-safe idempotent mirror keys |
| 7 | Duplicate imports | replace semantics + guided-opening refusal | **+ counts mismatch rejection (DP-01)** |
| 8 | Boundary quantities | quota caps from active receipts | unchanged (strong) |
| 9 | Out-of-order / future events | period membership tests | future-date guard documented (AR-08, P3) |
| 10 | Concurrent edits / two tabs | IDB serialization + versionchange tests + draft staleness | unchanged (strong) — cross-tab data-level race on financial-event idempotency documented (DP-03) |

## 4. Fresh-data invariant scenarios executed

See the financial-invariants file §"Adversarial scenarios executed" — 19 scenarios including double submit, double reversal, reversal-after-re-delivery, cancel-after-wallet-attribution, family-event general correction, PIN brute force, legacy lock upgrade, Arabic-Indic PIN, locked-device export bypass attempt, tampered backup, hand-merged backup (counts), corrupted integrity block, malformed values, invalid IDs, interrupted saves, duplicate import, boundary quantities, concurrent reversal, future dates.

## 5. CI evidence

- Baseline `main` run: 33948024196 — success (before any change).
- Audit branch run: **33960263084 — success** (triggered by PR #154; the workflow file itself is unchanged on the branch — see the patch note).
- PR: https://github.com/Qays7753/Micro/pull/154 (open for review, deliberately **not merged**).

## 6. Groups 1–5 regression evidence

All 58 test files added by PRs #149–#153 exist in the audit worktree and run in the suites above (domain 277/277, prototype 784/784 — the same suites, grown only by this audit's additions; no test was removed, weakened, or skipped). Migration/export/import/backup suites (envelope27, schema29–34, legacy pairs, guided opening, IDB migration chains v1/7/8/11/13/16/24/25, cursor-error abort, versionchange close-and-retry) all pass unchanged.

## 7. Known residual test debt (documented)

- DB-level upgrade tests for 33→34 and 34→35 and the O1 `<23` backfill (DP-13).
- AppLockGate idle/visibility/heartbeat dom suite beyond the PIN flow (DP-14 — partially covered via the Settings gate tests).
- `syncSha256Hex` known-answer (FIPS 180-4) vectors (DP-12).
- PWA reload decision extracted as a pure function with a test (AR-09).
- Cross-session financial-event duplicate semantics test (AR-07) and future-date editor warning test (AR-08).
