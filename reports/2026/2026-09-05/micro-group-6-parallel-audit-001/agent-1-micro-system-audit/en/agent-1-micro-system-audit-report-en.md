# Agent 1 — Micro System Audit Report (System Integrity, Quality, Performance, Security, Release)

**Track:** Group 6 parallel audit, track A (system integrity) · **Date:** 2026-09-05 · **Language of record:** English (product language is Arabic RTL; findings quote Arabic copy where user-visible).
**Baseline:** Micro `main @ ad9fc13` (PR #153 = Group 5 merge present; Groups 1–5 all merged via PRs #149–#153; CI green run 33948024196).
**Branch:** `agent/group-6-micro-system-audit` @ `c1ae93e` — isolated, pushed, PR #154 opened for review, **not merged**.
**Parallel track:** Agent 2 runs the Zman→Micro transfer reconciliation audit. Per protocol, Agent 2's branch and report folders were not inspected, modified, or merged. Only general observations relevant to system integrity were recorded (see §8).

---

## 1. Mission and mandate

Micro was audited as a high-value financial product held to a professional release standard, not a casual prototype. The mandate: inspect actual code and behavior (not prior claims), discover, classify, fix, test, and document defects; fix all P0/P1 on the isolated branch; fix safe P2 findings or document them; defer P3 items transparently; never merge to `main` while the parallel audit runs.

## 2. Method

1. **Baseline gate (fresh, actual counts — historical numbers not trusted):** clone, fetch all refs, record remote `main` SHA, all branches, PRs, recent CI runs, and working-tree state; create a recovery snapshot (local branch `recovery/group-6-audit-baseline-2026-09-05` + offline bundle kept outside the repository); then typecheck, lint, format, text-density, design-guards, domain tests, prototype tests, production PWA build.
2. **Five read-only specialist audits run in parallel** (Explore agents, no file modifications): Financial Truth, Data/Persistence, UX/RTL/Mobile, Security/Performance, Adversarial Release. Each returned a structured findings register with file:line evidence.
3. **Synthesis and verification:** every P1 finding was re-verified against the actual code by Agent 1 before fixing (two specialist claims were narrowed after verification — see §6).
4. **Fixes with adversarial/regression tests**, committed in logical units, full gate chain re-run after each batch.
5. **Final gates + push + PR + report.**

## 3. Baseline gate results (actual, before any change)

| Gate | Result |
|---|---|
| `pnpm typecheck` (root + prototype) | PASS (0 errors) |
| `pnpm lint` | PASS — 0 errors / 37 warnings (exactly at the `--max-warnings 37` ceiling) |
| `pnpm format:check` | PASS (scope: `src tests` only — see AR-05) |
| `pnpm text-density` | PASS — but only 40 of 52 routed pages measured (AR-04) |
| `pnpm design-guards` | PASS (no raw hex, values on scale) |
| Domain tests | 23 files / 277 tests PASS |
| Prototype tests | 120 files / 766 tests PASS |
| Production build + PWA | PASS — generateSW, 96 precache entries, 2053 KiB; main chunk 590 kB (gzip 138 kB) with the known >500 kB warning |
| Working tree / secrets | clean / none |

## 4. Verdict

**No P0 findings.** The domain core is unusually well-guarded: integer-minor money math, an 8-column delta table keeping cash/payables/owner-capital/expense/amanah/assets/loans/revenue strictly distinct, mirrored reversals, frozen cost snapshots, atomic multi-store IndexedDB commits with in-transaction identity checks, and an import pipeline that distrusts the file entirely. All ten product invariants hold on the primary write paths (evidence in the financial-invariants companion file).

The residual risk concentrated in **correction journeys at the application layer** and in **release governance**:

- period attribution after a reversed-then-re-delivered order (FT-01),
- a voided collection that left its wallet allocation in place (FT-02),
- the general event editor bypassing family-owned corrections (FT-03),
- envelope counts/integrity validation gaps (DP-01/DP-09),
- lock-surface weaknesses (SP-01..06, UX-01),
- and stale canonical docs + missing release mechanics (AR-01/AR-02).

All eight P1 findings were fixed on the branch with tests. Of the P2 set, the safe subset was fixed (AR-04 density truthfulness, AR-05 lint/format scope, UX-02 Tools states, UX-03 touch target, SP-02 PBKDF2, SP-03 input-aware idle, SP-04 enforced backoff, SP-05 opaque veil, SP-06 masked entry, DP-05 disable-path throttling); the architectural remainder is documented with remediation plans (chiefly PERF-01 full-dataset re-read fan-out, PERF-03 bundle composition, DP-03 cross-tab uniqueness index).

## 5. Status map (complete / partial / failing / unverified)

| Area | Status | Notes |
|---|---|---|
| Financial domain core (14 modules) | Complete + verified | all invariants hold; 277 domain tests |
| Persistence (IndexedDB, schema 35, migrations) | Complete + verified | atomic commits; upgrade-cursor abort test exists; 33→35 DB-level upgrade tests still missing (DP-13, P3) |
| Export/import/backup v27 | Complete + verified; **hardened** | counts comparison + malformed-integrity rejection added (DP-01/DP-09) |
| Visibility/reporting surfaces | Complete; one P1 fixed (FT-01) | canonical readers now share `lastEffectiveDeliveryEvent` |
| Drafts / lock / PWA / offline | Complete; **hardened** | PIN gate for data-leaving actions; PBKDF2; enforced backoff; input-aware idle |
| UX/RTL/density | Strong; gaps fixed or documented | 52/52 pages now measured; Tools states added; chip target 44px; remaining P3 polish documented |
| Performance | Partial (documented) | single IDB connection verified; PERF-01/02/03/05 documented with plans — architectural, deferred as risky-in-audit-scope |
| Security/privacy | Complete + verified | clean secret scan; no production transmission vectors; dev-only collectors excluded from prod; CSP verified |
| CI / release mechanics | Partial | branch CI green; tag/artifact/retry hardening delivered as a patch (token lacks workflow scope); zero tags on repo — release cut remains an owner decision |
| Canonical docs | **Backfilled** | current-state §25–§28, traceability, todo, CHANGELOG now cover transfer G3–G5 + this audit |
| Real-device QA / Pilot | Unverified (out of sandbox) | honestly declared in todo.md before this audit; unchanged |

## 6. Specialist claims re-verified and narrowed

1. **FT-02 deposit-refund half:** the specialist claimed `refundDeposit` also leaves wallet allocations behind. Verified against code: deposit collection **never creates wallet allocations** (no attribution call in the deposit flow — `agreementService` has none, and `collectionService` attribution applies to `collection_recorded` events). Therefore the refund path cannot desync a wallet ledger; the direct-sale cancel half was the real defect and was fixed. Documented so the integration step does not "fix" a non-defect.
2. **SP-03 idle semantics:** the Settings copy says lock-on-hide ("يُقفل … من إخفاء التطبيق"), so visibility-based locking was a *documented* design, not a silent defect. Nevertheless "الخمول" (idle) semantics were implemented more faithfully: the heartbeat now requires actual input, and a visible-but-untouched desktop tab locks after the chosen threshold. Behavior change is deliberate and disclosed.

## 7. Fixes delivered (10 commits, `fc9e5e9..c1ae93e`)

| Commit | Finding | Summary |
|---|---|---|
| fc9e5e9 | SP-01..06, DP-04/05, UX-01 | lock surface hardening incl. Settings data-action PIN gate |
| c42ecba | FT-01 | last effective (unreversed) delivery attribution in 5 readers |
| 16e353d | FT-02 | direct-sale cancel mirrors wallet-allocation reversals (idempotent) |
| 87b3ace | FT-03 | family-owned events corrected only via owner records; MIC-11 loan-restore recognition |
| d89e853 | DP-01/DP-09 | import counts validation + malformed integrity rejection |
| 4624dcd + 3e3fa5e + c1ae93e | AR-01/AR-02/AR-03 | docs backfill for transfer G3–5; CI hardening converted to a proposed patch after push-scope discovery |
| 0d45bb4 | AR-04, UX-02, UX-03 | density guard 52/52 + missing-page failure; Tools loading/error states; 44px chip target |
| a864e0b | AR-05 | lint + format gates cover the whole app (165 files reformatted) |

## 8. General observations on Agent 2's scope (system-integrity relevance only)

- The capability-transfer lineage (Zman→Micro) is the source of the currently merged Groups 1–5; their merge history (PRs #149–#153) is intact and reachable from `main` — required for any later reconciliation.
- One stale open PR (#141, `task/direct-sale`) predates the transfer program and is unrelated to approved work; disposition belongs to the integration step, not this audit.
- The npm-registry audit outages observed during PRs #150–#152 were infrastructure, not vulnerabilities (local audit clean each time); the bounded-retry policy is part of the proposed CI patch.

## 9. Limitations

- **No real browser/device QA in this run** beyond jsdom DOM tests: the audit is static + unit/dom-level; live 360×800 RTL journeys were not re-driven here (the repo's own live-QA claims from Group 5 were treated as historical, not trusted). The dom tests added cover the new behaviors.
- **PERF-01/PERF-03/PERF-05 not fixed** (architectural performance work: service-layer memoization keyed by data version, entry-chunk composition, precache trimming). Fixing them inside an audit branch would carry regression risk exceeding the benefit; each has a concrete remediation plan in the UX/perf companion file.
- **CI workflow unchanged on the branch** — the provided push token lacks `workflow` scope; the hardening is delivered as `proposed-ci-hardening.patch` for the owner to apply with a properly scoped token. Nothing was bypassed.
- **DP-03 (unique idempotency index for financial events) deferred** — requires a schema migration (35→36) plus migration tests; a crash window remains covered by the reuse check + MIC checks, and the risk is documented.
- **Product-decision findings (FT-04 cross-period reversal policy unification, FT-05 waste expensing) documented, not decided** — they change reported numbers and belong to the owner.

## 10. Disposition

- Branch `agent/group-6-micro-system-audit` @ `c1ae93e` pushed; PR #154 open for review; **not merged** while Agent 2 runs.
- `git status --short` empty on the branch; no stashes; no worktrees; temporary artifacts (offline bundle, patch copy) live outside the repository or inside the report folder by design.
- The next step belongs to the owner: controlled integration of Agent 1 + Agent 2 branches, final CI on `main`, release tag decision, and only then cleanup of merged branches after proof of reachability.
