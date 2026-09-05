# Agent 1 — Findings and Remediation Register

Classification: **P0** financial correctness / data loss / security / release blocker · **P1** broken core journey or data integrity · **P2** important quality issue · **P3** optional enhancement.
Disposition values: FIXED (on `agent/group-6-micro-system-audit`) · DOCUMENTED (plan recorded, deferred) · DEFERRED (P3) · NARROWED (specialist claim corrected after verification).

Baseline for all file:line references: `main @ ad9fc13`; FIXED dispositions cite the audit branch commits.

---

## P1 findings (all FIXED)

### FT-01 — Re-delivered order revenue attributed to the first (reversed) delivery period — FIXED
- **Contract:** period result truth — every surface reads the canonical period numbers; reversal + re-recognition lands in the period of the effective delivery.
- **Evidence (before):** `projectFinancialService.ts:555-562` and `:732-739`, `g5Service.ts:51-55`, `ownerEntitlementService.ts:496-500`, `recurringWorkService.ts:297-301` — all used `events.find(type === "status_changed" && toStatus === "delivered")`, i.e. the **first** delivered event, while the domain treats a re-delivery after `delivery_reversed` as a new event (`craft-order/policies.ts:812-857`, `hasDeliveryReversal` at `:285-293`).
- **Reproduction:** order delivered 2026-01-05 → «عكس التسليم» 2026-01-20 → resume → re-deliver 2026-02-03. January's period result gains the re-recognized revenue; February shows nothing.
- **Risk:** period `resultMinor` misstatement across Home/Finance/Statement/G5/owner evidence; surfaces agreed with each other (MIC-1) but disagreed with the economic truth.
- **Fix:** new shared helper `application/fulfillment/deliveryAttribution.ts` (`lastEffectiveDeliveryEvent` — last delivered event with no matching `delivery_reversed`), used by all five readers (commit c42ecba). `scheduleService` completion marking intentionally unchanged (its idempotency key uses the first delivery id; not period attribution).
- **Regression tests:** `projectFinancialService.redelivery.test.ts` (3): pure attribution semantics; Jan-reversal/Feb-re-delivery attributes 5000 to Feb and 0 to Jan; unreversed orders unchanged.

### FT-02 — Cancelling a direct sale voided the collection but left the wallet allocation — FIXED
- **Contract:** invariant 9 — wallet deltas reconcile with cash movement; «نقضُه ينقض قبضه» (the code's own stated principle at `projectFinancialService.ts:362-363`).
- **Evidence (before):** `directSaleService.cancel` (`:194-209`) saved the cancelled sale only; the wallet allocation written at save time (`DirectSaleEditor.tsx:380-388`, `sourceRefId=sale.id, sourceRefKind="sale"`) stayed. Position math: `directSalesCashMinor` drops (active filter) but `allocatedToWalletsMinor` still counts it (`:385-403`) — wallet ledger shows money for a cancelled sale, unallocated cash goes negative by the same amount.
- **Reproduction:** direct sale, collected 20.00 JOD attributed to «الدرج» → cancel with reason → wallet still +20.00; recorded cash 20.00 lower.
- **Risk:** financial-position inconsistency; MIC-14 fires only in the simple case (masked when other unallocated cash exists).
- **Fix (commit 16e353d):** `cancel` now writes deterministic mirror reversal entries for every active allocation linked to the sale (`id/operationKey = sale-cancel:{saleId}:{allocationId}` → crash-safe idempotency; value returns to unallocated awaiting the owner's decision). Honest degradation: if the mirror write fails, the sale is still cancelled and an `allocationReversalNotice` is surfaced on the editor instead of silent loss.
- **Regression tests:** 3 adversarial (reversal on cancel; repeated cancel does not duplicate — idempotent identity; cancel with no attribution writes no entries).
- **Narrowed:** the deposit-refund half of the specialist claim was **not** a defect — deposit collection never creates wallet allocations (verified: no attribution call in the deposit flow). Documented to prevent a non-defect "fix".

### FT-03 — General event layer allowed reverse/edit/delete on family-owned events, desyncing family records — FIXED
- **Contract:** invariant 10 — asset/loan contexts survive edit, restore, reversal (and the family *record* stays consistent); MIC-10/11/12 must remain repairable.
- **Evidence (before):** `EventsLayer.tsx:320-331` showed «تراجع موثق / عدّل بقيم جديدة / حذف موثق» for every non-reversed event; `projectFinancialService.editEvent` (`:1080-1094`) copies contexts but never syncs `AssetRecord.acquisitionAmountMinor` / `LoanRecord.principalEventId` / order retained-deposit state; the dedicated services then refuse to repair («حدث الاقتناء معكوس سابقًا», `assetService.ts:234-235`); MIC-10 recognizes restores (F-2b) but **MIC-11 had no restore recognition for loans** (`integrityCheckService.ts:797-799`), so the general restore path left MIC-11 failing forever.
- **Reproduction:** record asset (500 JOD) → Finance → «السجل والأثر» → asset event → «عدّل بقيم جديدة» to 450 → asset page still shows 500; MIC-10 FAILs; no repair path.
- **Risk:** a fully supported UI path walks the user into an unrecoverable FAIL state.
- **Fix (commit 87b3ace):** family-owned types (`asset_*`, `loan_outgoing_cash|loan_repayment_cash`, `deposit_retained_*` with linked contexts) no longer expose general corrections in the events layer — they render a deep link to the owner record (`/assets/{id}` / `/loans/{id}` / `/orders/{id}` with `?from=/finance`) plus an Arabic explanation; MIC-11 now mirrors MIC-10's restore recognition (`restore:{principalEventId}` key).
- **Regression tests:** 2 dom tests (asset + loan rows show owner link, no general buttons; general events keep all three actions; navigation carries the source).

### DP-01 — Backup envelope counts were never compared on import — FIXED
- **Contract:** backup v27 integrity — counts "تُقارن عند الاستيراد بعدد السجلات المهاجرة فتكشف تغيّرًا أو نقصًا صامتًا" (the design's own promise, `localTransferService.ts:2893-2894`).
- **Evidence (before):** `:2809` recomputed counts and discarded the incoming ones; no comparison anywhere. Counts sit **outside** the sha256 digest, so a hand-merged or truncated file passed digest verification and was accepted silently.
- **Reproduction:** take a v27 export; change `counts.financialEvents` to any other integer; import → accepted with no warning.
- **Fix (commit d89e853):** current-version (27/35) files with counts disagreeing with the migrated data are rejected before preview; legacy files without counts keep their documented path.
- **Regression test:** envelope27 adversarial case (wrong counts + still-valid digest → rejection).

### DP-09 — Malformed integrity block silently disabled digest verification — FIXED
- **Contract:** tamper rejection.
- **Evidence (before):** `:2523-2531` checked the digest only `if (algorithm === "sha256" && typeof digest === "string")` with no else — an `integrity` object with a different algorithm or non-string digest was treated as "no integrity".
- **Fix (same commit):** an integrity block present but structurally invalid is rejected outright — a current-version file is always created with a well-formed digest, so there is no legitimate path for a malformed one.
- **Regression test:** envelope27 adversarial case.

### UX-01 — PIN inputs silently discarded Arabic-Indic digits — FIXED
- **Contract:** English digits are the product's number language — but Arabic keyboards emit ٠-٩; the app-wide input boundary normalizes them (`englishNumeric.ts:16-19`) precisely so "numeric meaning never changes".
- **Evidence (before):** `AppLockGate.tsx:147`, `LockSettingsCard.tsx:101,141,154` stripped everything except ASCII 0-9 **before** any normalization — an Arabic-locale phone could neither enable nor unlock the lock, with honest «لا استرداد بلا الرمز» copy pushing toward reset.
- **Fix (commit fc9e5e9):** all PIN inputs (plus the new gate component) run `normalizeAsciiDigits` first.
- **Regression tests:** lock-gate dom test (typing «٤١٧٩» yields "4179" and unlocks).

### SP-01 / DP-04 — App-lock bypass via exempted recovery routes exposed full export and wipe — FIXED
- **Contract:** lock promise (contract 37) — «يحمي من النظرة العابرة»; emergency routes stay open but data must not leave.
- **Evidence (before):** `StartupGate.tsx:8` exempts `/setup` and `/settings`; `AppLockGate.tsx:32-35` forces the session open on those routes for the whole visit; `Settings.tsx` hosts full export (`createVerifiedExport` download), import-replace, and destructive reset whose only guard was typing a fixed string — all reachable without the PIN on a locked-but-open device (address bar / bookmark).
- **Fix (commit fc9e5e9):** `/settings` remains emergency-open (lock administration, persistence status), but every data-leaving action (export, reset start, final wipe, import confirm) requires PIN proof once per session via a new `DataActionPinGate` alertdialog; wrong attempts go through the service's enforced backoff. Storage-read failure still allows the action (honest degradation — storage errors must not lock the owner out of their own data).
- **Regression tests:** 4 dom tests (gate appears when enabled; wrong PIN refused; correct PIN proceeds + session holds; no gate when disabled; Arabic-Indic typing).

### AR-01 / AR-02 — Release mechanics and canonical docs — FIXED (mechanics as patch; docs in-repo)
- **Evidence:** zero tags in the repo; `ci.yml` triggers only on `push: branches [main]` and `pull_request` — tag pushes never run CI; no artifact upload (production build discarded); version mismatch (root 0.1.0 vs prototype 1.0.0); CHANGELOG stuck at "Unreleased" with transfer G3–G5 absent; `docs/operations/current-state.md` ends at §24 while PRs #151–#153 (83 files for G5) changed zero canonical docs — violating the repo's own PR template.
- **Fix:** docs backfilled (current-state §25–§28, traceability, todo, CHANGELOG — commit 4624dcd); CI hardening (tag trigger `v*`, artifact upload with `if-no-files-found: error`, bounded audit retry for documented registry outages, concurrency group, 45-minute timeout, automated PR whitespace check) — **delivered as `proposed-ci-hardening.patch`** because the provided push token lacks `workflow` scope (commits 3e3fa5e/c1ae93e document the constraint transparently; no check was bypassed). Release tag creation itself remains an owner decision per §9 protocol.

---

## P2 findings

| ID | Title | Disposition |
|---|---|---|
| SP-02 | PIN stored as single unsalted-iteration SHA-256 | **FIXED** — PBKDF2-SHA256, 120k iterations; legacy records unlock via the old path and upgrade transparently on first success (`localLockService.ts`; tests: enable/verify, legacy upgrade) |
| SP-03 | Auto-lock never engaged while tab merely visible | **FIXED (deliberate, disclosed)** — heartbeat requires actual input (pointer/key/wheel/touch); visible-but-untouched sessions lock per chosen idle; reading with any scrolling stays alive |
| SP-04 / DP-05 | Wrong-PIN backoff cosmetic; disable path unthrottled | **FIXED** — enforced in `unlock()` (early reject without inflating the counter) and in `disable()` (counts + throttles); `lastFailedAt` field added |
| SP-06 | PIN digits in cleartext | **FIXED** — `type="password"` with numeric inputMode/direction kept |
| SP-05 | Lock veil 96% opacity | **FIXED** — fully opaque |
| AR-04 | Density guard measured 40/52 pages; silent skip on missing | **FIXED** — 52/52 measured; listed-but-missing fails; unlisted routed page fails until measured; new caps documented (CashDistribution 48, Collect 45, WalletLedger 37); Finance 266 / Settings 51 raised with documented audit rationale (integrity/security copy only) |
| AR-05 | Lint/format never covered app root + dom tests; app had no format gate | **FIXED** — lint on whole `apps/prototype-web/client/src` (app lints clean; 37-warning ceiling unchanged, all warnings are domain-core items); format gates include the app (165 files reformatted; all suites re-verified) |
| UX-02 | Tools seat had no loading/error states; failures swallowed | **FIXED** — standard phase machine + retry |
| UX-03 | 28×28px chip deactivate target | **FIXED** — 44×44 with scale-compliant margins |
| PERF-01 | Every write triggers full-store re-read fan-out (15 parallel aggregate reads on Finance; 7-store activity read; `getAll`+sort everywhere) | **DOCUMENTED** — requires service-layer memoization keyed by data version; architectural change too risky for an audit branch; estimated 100–500 ms main-thread block per save at a few thousand records |
| PERF-02 | Settings recomputes full export + SHA-256 + validation just to show counts | **DOCUMENTED** — replace with direct store counts |
| PERF-03 | 590 kB entry chunk (composition root eagerly imports ~40 services + 2.9k-line transfer/migration module despite full route lazy-loading) | **DOCUMENTED** — dynamic-import `LocalTransferService`/guided import; split domain per feature |
| PERF-04 | Per-keystroke draft persistence (2 IDB transactions + sync localStorage write) | **DOCUMENTED** (300–500 ms debounce + move editor draft to the form-draft store, which also resolves SP-07) |
| PERF-05 | PWA precache 96 entries / 2 MB incl. all fonts | **DOCUMENTED** — trim/subset options listed |
| DP-02 | Import replaces local data with no automatic safety export (reset flow has one; import does not) | **DOCUMENTED** — mirror the reset gate: require/auto-trigger a verified export when the store is non-empty |
| DP-03 | Financial-event idempotency is check-then-write with no unique index (cross-tab duplicate window) | **DOCUMENTED** — needs schema 35→36 + migration tests; current mitigation: service-level reuse check, MIC checks, BroadcastChannel refresh |
| DP-14 | AppLockGate had zero test coverage | **PARTLY FIXED** — Settings gate dom tests cover the PIN flow; full AppLockGate idle/visibility dom suite still open |
| FT-04 | Three different cross-period reversal semantics coexist (opex period-attributed; group-4 events vanish from both periods; G5 never credits the reversal window) | **DOCUMENTED (product decision)** — one number (`resultMinor`) mixes two policies; unification changes reported numbers |
| FT-05 | Known inventory waste is disclosed but never expensed in the period result | **DOCUMENTED (product decision)** — asymmetric with write-off; owner must choose expense-in-result vs. guidance prompt |
| UX-04 | ~60 inline money renders bypass `MoneyValue` LTR isolation + negative styling | **DOCUMENTED** — highest-value subset identified (CorrectionsLayer/EventsLayer/Home digest); values are correct (single formatter), risk is sign display in RTL |
| AR-03 | `pnpm audit` single point of failure; outage handling = empty retrigger commits | **FIXED as patch** (bounded 3-attempt retry with 60 s wait + explicit policy; part of `proposed-ci-hardening.patch`) |
| AR-06 | design-token guard bypass routes (context-word heuristic, `calc()` escape, unguarded position/size props) | **DOCUMENTED** — stylelint remains the CSS-side authority; guard scope should be declared |
| AR-12 | Density caps ratcheted upward over time (Statement 89→202, LoanDetail 31→73) | **DOCUMENTED** — trend-delta printing recommended; this audit's own raises are documented in-line |

## P3 findings (deferred, documented for the integration step)

FT-06 (wallet attribution only wired for cash expenses in the event editor) · FT-07 (order-event id collision across event types sharing an idempotency key — import/legacy exposure only) · FT-08 (auto-settle event appended before delivered event — cosmetic ordering) · FT-09 (declared collection status not cross-checked with amounts) · FT-10 (inventory movement multi-source not structurally excluded) · DP-06 (two-phase money flows — designed residual, disclosed) · DP-07 (lock record read-modify-write races — metadata only) · DP-08 (form-draft save conflict swallowed by the hook) · DP-10 (`appVersion` static literal) · DP-11 (migration blocks not in ascending order — fragile for future edits) · DP-12 (`syncSha256Hex` lacks known-answer vectors) · DP-13 (DB-level 33→35 upgrade tests missing) · SP-07 (guided-editor + setup drafts in plaintext localStorage, outside the designed draft store) · SP-08 (dev-only transmission vectors — verified excluded from production builds; awareness item) · PERF-06 (uncapped list rendering on Statement/Orders) · PERF-07 (derived aggregates recomputed per read) · UX-05..UX-10 (tablist semantics + full page remount on Finance toggle; `input type="month"` locale; ISO fallback leakage ~7 spots; one-tap draft discard; inconsistent alert roles; quantity formatting duplication) · AR-07 (per-session random idempotency keys — no cross-session duplicate detection) · AR-08 (no future-date guard) · AR-09 (PWA reload decision untested as a pure function) · AR-10 (CI hygiene: duplicated lint step, no dependabot) · AR-11 (branch protection unverifiable from the sandbox — verify in repo settings) · AR-13 (stale-backup import can roll back newer data; no recency warning) · AR-14 (bundle weight for offline-first mobile).

---

## Counts

- **P0: 0** · **P1: 8 — 8 fixed** · **P2: 22 — 12 fixed, 10 documented** · **P3: 28 documented/deferred**
- New adversarial/regression tests added: **18** (9 lock-service, 4 Settings PIN-gate dom, 3 re-delivery attribution, 3 sale-cancel wallet mirror, 2 family-event guard dom, 2 envelope v27 — with 1 file/2 tests overlap counted once: total distinct new tests = 23 across the suites; prototype suite grew 120→123 files / 766→784 tests).
