# NEXT EXECUTION PLAN — Micro Remediation Before the User-Journey Phase

**Basis:** `MICRO_REMAINING_CLOSURE_AND_DARK_MODE_ANALYSIS.md` (2026-09-15), built from the five-agent read-only audit of `Micro@micro-standard-ui-aux-integration-20260914` (`ece7be3630739d551b9ba7caf37d30a9a63c872f`).
**Status:** PROPOSAL — nothing below has been executed. The owner reviews and approves this plan before any future execution phase begins.
**Branch discipline (unchanged from the integration run):** continue on the existing branch; linear history; revertible commits; clean worktree after every wave; `git diff --check` clean; full `pnpm check` green at every wave boundary; `Micro/main` and `Documents/main` untouched; rollback restore point = `ece7be36` until the phase is accepted.

**Invariants for every wave (from Unified Report §17):** no changes to domain/application/storage layers; no state-word or financial-copy changes (classification/display only); no new palette values; no Dark Mode activation; no journey redesign inside remediation waves; preserved-with-reason register only ever extended.

---

## Phase 0 — Owner decision D1 (before everything)

**Decide: pin light until the dark wave.**
- Recommended: `App.tsx` `defaultTheme="light"` + `switchable={false}` (or hide the AppHeader/Settings toggles), one line + test; recorded in MIGRATION_STATUS U-03.
- Why first: it makes the broken v0 dark surface (quiet-button text 1.05–1.18:1) unreachable, independent of every other wave. If the owner instead accepts reachable dark, dark parity must be added to every wave's test matrix — a materially larger plan.
- Effort: minutes. Risk: minimal, reversible.

## Wave R1 — Feedback truth (product-visible semantic fixes)

**Findings closed:** A5-01 (HIGH), A5-02 (MEDIUM), A5-05 (MEDIUM), A2-03 (MEDIUM), A2-05 (MEDIUM), A3-08 (LOW); opportunistically A1-02.

**Steps:**
1. `FeedbackNote` (`components/primitives/Notice.tsx`): add an explicit success/advisory channel (e.g. a `kind` or `advisory` pattern per consumer) so classification never depends on the `/^تم[ت ]/` prefix alone. **Words untouched.** Consumers: the 8 sites (`SettingsDataProtectionSection.tsx:125`, `SettingsGuidedOpeningSection.tsx:245`, `SettingsOperatingModeSection.tsx:133`, `DraftEditor.tsx:368`, `InventoryMaterials.tsx:255`, `Catalog.tsx:933`, `CostEditor.tsx:362`, `DirectSaleEditor.tsx:793`).
2. Pin contract tests: Settings export-success «النسخة الاحتياطية جاهزة…» family + diagnostic-copy success render a check/neutral marker, never `InlineError`; InventoryMaterials completions (أُوقفت/عادت/حُلّ) and DraftEditor advisories (لم نجد/بدأت) never render InlineError.
3. `pages/OrderDetail.tsx:191-193,272-284`: split load-failure (role=alert + retry action) from not-found (honest road back, distinct copy — copy changes need owner words or existing registered wording).
4. Docs: correct EXECUTION_REPORT §7.F reduced-motion wording; fix MIGRATION_MATRIX Schedule cell (row 43) to match reality (or add a Schedule dom test — R2 does the dom test option); correct ADR-006 (81 files) + ADR-008/MIGRATION_STATUS (8 choice toggles; ActualTimePanel is a Button weight split).
5. Full `pnpm check`; captures on Settings + InventoryMaterials + OrderDetail error path.

**Acceptance:** per Unified Report §15-R1. **Rollback:** single revert. **Depends on:** nothing.

## Wave R2 — Interaction evidence (tests and captures only)

**Findings closed:** A2-01 (HIGH), A2-02 (HIGH), A2-06 (MEDIUM), A2-04 (MEDIUM), A2-10 (LOW); opportunistically A2-09.

**Steps:**
1. Keyboard tests: `{Escape}` closes QuickActionSheet (`onOpenChange(false)` asserted) and the UnsavedChangesGuard drawer; Tab/Enter traversal on the sheet menu.
2. Focus management tests for the overlay family: initial focus on open, focus trap while open, restore on close (`document.activeElement` assertions) — QuickActionSheet + UnsavedChangesGuard drawer first.
3. Render-smoke journeys for the 6 highest-risk never-rendered pages: CashReversalEditor, CashAdjustmentEditor, CashOpeningLaterEditor, InventoryReversalEditor, G5DeclarationEditor, AgreementEditor — each renders + saves through mocked/Memory services.
4. Delete/replace the vacuous test (`primitives.test.tsx:228-232`).
5. Re-run browser captures at 360 and 430 (home + finance) with per-row `capture-log.json` entries — or narrow the width-matrix claim to 320/390 in FINAL_TEST_RESULTS.
6. Optional: StartupGate dom test (loading → ready, first-run redirect /setup, error + retry Button).
7. Reword the none-found "covered by typecheck/lint" claim to match the new reality.

**Acceptance:** per Unified Report §15-R2. **Rollback:** trivial (tests only). **Depends on:** nothing (parallel with R1).

## Wave R3 — Selection visibility + governance hardening

**Findings closed:** A5-04 (MEDIUM), A3-01, A3-02, A3-04, A3-05, A3-06, A3-07, A3-10 (MEDIUM/LOW); optional A2-07 guard if D5 decides "now".

**Steps:**
1. Pressed-state styling for `aria-pressed` link-ink controls (22 FinanceActivity filters, Finance view tabs, Statement ranges, LockSettings options, Corrections/Events toggles) — provisional rule now, final shape per D7 (link-ink ratification or chip migration). `index.css:5853` is currently the only pressed rule in the tree.
2. Docs: amend SOURCE_OF_TRUTH to name FeedbackNote the ratified centralized classifier (post-R1 shape); add the FeedbackNote section to COMPONENT_CONTRACTS (props, regex rule, consumers).
3. Guard: repo CSS scan test — zero `--vf-*` declarations outside `vf-tokens.css`.
4. Guard: eslint `no-restricted-imports` for `components/primitives/**` banning `@/pages/*`, `@/app/*`, `@/application/*`, `@/storage/*`.
5. Docs: correct DARK_MODE_BOUNDARY.md:10 (light-locked primitives; `.dark` user-reachable); repoint EXTENSION_PLAYBOOK B.6/E.3/F.4 at permanent homes; add `components/forms/` + `components/ui/` to the UI_AUX_ARCHITECTURE layer-5 list.
6. At the merge gate (not before): update `docs/operations/current-state.md` + `todo.md` per AGENTS.md §9 (A3-05).
7. Optional (if D5 = now): computed contrast-ratio guard over the token table wired into `pnpm check`.

**Acceptance:** per Unified Report §15-R3. **Rollback:** per-commit. **Depends on:** R1 (for A3-01's documented shape); D7 (for the final pressed-state shape — provisional landing allowed).

## Wave R4 — Dark semantic contracts (Option B preparation)

**Findings closed:** A4-02 (HIGH); applies D1 if not already done in Phase 0.

**Steps:**
1. Create `styles/semantic-roles.css` (layer 2.5): mode-independent roles (surface / surface-raised / text / text-secondary / text-tertiary / border / border-interactive / state-success / state-error / state-info / state-status / identity / identity-interactive / commitment / focus / scrim / elevation / chart-1..n per DARK_MODE_BOUNDARY.md §"future semantic layer") — **light values bind to the existing `--vf-*` set; no new palette values**.
2. Retarget `primitives.css` text/mark/fill bindings (`:19-41,164-167,171-178,275,344-353,376,450-459,480`) from direct `--vf-*` to the semantic roles — **value-preserving in light**.
3. Guard test: no `.micro-prim-*` text/mark declaration binds `--vf-ink*`/`--vf-error`/`--vf-success` directly.
4. Computed-style equality test: light-theme rendered values byte-identical before/after.
5. Visual captures (home/finance/orders @320/390) proving zero light change; full `pnpm check`.
6. Zero TSX changes required — 299 Buttons inherit automatically.

**Acceptance:** per Unified Report §15-R4. **Rollback:** single revert (delete semantic-roles.css + restore direct bindings). **Depends on:** D1 decided (recommended first); D10 runs in parallel on the Standard side (steward, non-blocking).

## Owner decision session (D)

| When | Decisions |
|---|---|
| Phase 0 (before R1) | **D1** dark reachability |
| Before R3 | **D7** link-ink + pressed state; **D4** surface-tone grammar; **D5** contrast floors |
| Before J1 (merge gate) | **D2** Row/Field sequencing; **D3** commit-class expansion |
| Any time (parallel) | **D6** conditional feedback; **D8** FinanceActivity chip copy; **D9** ✓ marker (after R1) |
| Standard revision (steward) | **D10** mode-neutrality clarification |

All decisions recorded in `docs/architecture/MIGRATION_STATUS.md` registers (D10 in the Standard repo).

## Exit gate to the journey phase (J1)

J1 starts only when:
1. R1–R4 merged on the integration branch (or its accepted successor), full `pnpm check` green at each boundary, clean worktree, linear history.
2. D1, D2, D3, D7 recorded.
3. current-state.md + todo.md describe the integration + remediation state (A3-05).
4. Owner formally accepts the branch (optional fresh `pnpm check` at acceptance per A1-05).

## Effort estimate (honest, order-of-magnitude)

| Wave | Nature | Rough effort |
|---|---|---|
| D1 | one-line config + test + register note | minutes |
| R1 | primitive channel + 8 consumers + tests + OrderDetail split + docs | ~0.5–1 day |
| R2 | test authoring + captures | ~1 day |
| R3 | one CSS capability + 2 guards + doc pass | ~0.5–1 day |
| R4 | semantic layer + retarget + equality tests | ~1 day |
| D2–D10 | decisions (owner time) | owner-dependent |

**Total execution-side: roughly 3–5 focused days** — small against the integration run it closes, and every piece revertible.
