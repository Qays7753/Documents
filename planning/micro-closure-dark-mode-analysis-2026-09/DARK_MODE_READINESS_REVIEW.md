# Dark Mode Parity & Readiness Review — A4 (Read-Only Closure Analysis)

**Task ID:** A4 · **Agent:** 4 (Dark Mode Parity & Readiness Auditor)
**Date:** 2026-09-15 · **Analyzed tree:** Micro `micro-standard-ui-aux-integration-20260914` @ `ece7be3630739d551b9ba7caf37d30a9a63c872f` (worktree verified clean, read-only)
**Standard consumed:** `documents/micro-standard-v2` (Documents/main @ `f919982c`, 31 files verified on disk)
**Method:** static analysis only — Read/Grep/LS plus read-only `git -C` status checks; WCAG contrast ratios computed offline from declared hex values; **no style computation tools were run against the app, no dark mode was activated, no files inside the clones were modified.**

---

## 1. Executive verdict

1. **The Dark Mode boundary documentation is complete and accurate** (claim 13 verified): `.dark` is a Micro-local legacy block carrying the retired v0 palette, ThemeContext + toggle are preserved, ADR-007 + `DARK_MODE_BOUNDARY.md` define the semantic-layer proposal, and `styles/semantic-roles.css` does **not** exist. As *documentation*, the boundary is closed.
2. **The runtime tells a different story:** the `.dark` theme is **reachable today** — `App.tsx:13` mounts `<ThemeProvider defaultTheme="system" switchable>`, so any device with OS dark preference renders Micro in dark mode on first load, and the AppHeader moon/sun button (`AppHeader.tsx:48-56`) plus the Settings appearance section (`SettingsAppearanceSection.tsx:34-36`) toggle it for everyone else. "NOT activated" is a design-ratification statement, not a runtime state.
3. **If `.dark` is active, the app is PARTIAL-BROKEN.** The shell and legacy feature CSS (≈6,300 lines, all `--color-*` alias-based) re-theme correctly (albeit with retired v0 values). The entire W2 primitive layer binds text-critical roles directly to light-only `--vf-*` contracts, producing: invisible quiet-button text (1.05–1.18:1), an invisible commit-button boundary (1.18:1), invisible Row/Field/EmptyState titles (1.18:1), sub-floor captions/markers (1.81:1), and a sub-floor inline-error ink (2.59:1). Static WCAG math in §3.
4. **Parity inventory (63 roles/components):** 29 PRESENT (≈half of them value-contradictory), 9 PARTIAL, 18 MISSING (7 of those BROKEN-if-activated), 7 NOT-APPLICABLE. Full detail: `DARK_MODE_PARITY_MATRIX.csv`.
5. **Recommendation: Option B** — keep the boundary, close the missing **semantic contracts** (the `semantic-roles.css` layer + re-pointing primitive text bindings) before the next journey phase, and implement the actual dark palette after it — combined with an **immediate owner decision** on the runtime-reachability hole (pin light until the dark wave, or consciously accept the broken dark surface).

---

## 2. Dark boundary inventory (what exists today)

### 2.1 The `.dark` block — `apps/prototype-web/client/src/index.css:107-151`

The block re-declares **37 Micro runtime names**. Complete inventory (name → dark value):

| Group | Re-declared names (dark values) |
|---|---|
| Elevation | `--elevation-1: 0 1px 2px rgba(0,0,0,.12)` · `--elevation-2: 0 6px 20px rgba(0,0,0,.2)` · `--elevation-3: 0 16px 40px rgba(0,0,0,.28)` (the only deliberate non-v0 values) |
| Surfaces | `--color-bg-canvas: #1c1917` · `--color-bg-well: #332d27` · `--color-surface: #27231f` |
| Lines | `--color-border: #51473c` · `--color-divider: #62564b` |
| Text | `--color-text-primary/--color-text-strong: #fff7ed` · `--color-text-secondary: #d6c9ba` |
| Identity | `--color-brand-primary: #d59172` · `--color-brand-pressed: #cc785c` · `--color-brand-text: #8fd5d6` · `--color-brand-soft: #332d27` |
| Accent | `--color-accent-primary: #5ec0c1` · `--color-accent-text: #8fd5d6` · `--color-accent-soft: #332d27` |
| State pairs | success `#7fc49e/#332d27` · danger `#e47975/#332d27` · warning `#e2c268/#332d27` |
| shadcn-level | `--background/--foreground/--card(--foreground)/--popover(--foreground)` → alias refs; `--primary: var(--color-brand-primary)` · `--primary-foreground: var(--color-ink-on-color)` · `--secondary: var(--color-accent-primary)` (teal) · `--secondary-foreground: var(--color-ink-on-color)` · `--muted(-foreground)` · `--accent(-foreground)` · `--destructive: var(--color-danger-text)` · `--destructive-foreground: var(--color-ink-on-color)` · `--border` · `--input` · `--ring: var(--color-accent-text)` |

**Retired v0 palette verified present** (claim 13 exact): canvas `#1c1917` ✓, brand `#d59172` ✓, teal accents `#5ec0c1`/`#8fd5d6` ✓. Additionally `--color-brand-pressed: #cc785c` is on the test suite's own `RETIRED` list (`vf-tokens.test.ts:48-64`) — a retired value in active dark-layer use.

**Registry status of the dark hexes:** of the 14 distinct hex values in the block, **zero** are in `APPROVED_18`, **zero** in `MICRO_KEPT`, one (`#cc785c`) in `RETIRED`, and the remaining 13 belong to **no registry at all** — an unaudited legacy palette that `design-token-guards.py` silently whitelists (it treats `.dark {}` as a token-definition zone, `design-token-guards.py:70-84`).

**Names NOT re-declared under `.dark`** (they keep `:root` values): `--color-ink-on-color` (= `var(--vf-ink)` #141413 — silently light), every `--vf-*` contract (by design, `vf-tokens.css:16-17`), and all geometry/motion tokens (mode-independent).

**Companion dark-only rules** (6 selectors beyond the block): `.dark [data-tone="accent"|"warning"]` structural borders (`index.css:386-391`), `.dark .micro-truth-banner` border (`:392-394`; **0 TSX consumers** — dead rule), `.dark .micro-priority-texture` opacity (`:395-397`), `.dark .micro-review-pattern` blend-mode flip (`:592-595`). These prove the block was once a working theme with deliberate dark adaptations (the §4-item-17 comment at `index.css:384` documents the "all soft colors collapse to #332d27, separation is structural" rule).

**W6 interaction:** five dead token mirrors (`--space-7`, `--motion-in-out`, `--color-text-tertiary`, `--color-withdrawal-text/bg`) were removed from `:root` **and** their `.dark` mirrors (`W5_W6_W7_REPORTS.md:31`) — consistent with DARK_MODE_BOUNDARY.md's "only three verified-dead token mirrors were removed" (three color mirrors).

### 2.2 Theme mechanism — how `.dark` is applied and what re-renders

- `contexts/ThemeContext.tsx` — `ThemeProvider({ defaultTheme = "system", switchable = false })`. **App.tsx:13 passes `defaultTheme="system" switchable`.**
- Resolution: `resolveTheme("system")` reads `matchMedia("(prefers-color-scheme: dark)")` (`ThemeContext.tsx:20-23`) — **OS-dark devices start in dark**; saved preference (Application/LocalStore via `preferenceService`) overrides after load; `system` preference live-follows OS changes (`:38-46`).
- Application: `document.documentElement.classList.toggle("dark", …)` + `dataset.theme` + **runtime meta theme-color rewrite** reading computed `--color-bg-canvas` (`:47-59`). CSS custom properties cascade — every element re-resolves **without React re-rendering**; only `useTheme()` consumers (AppHeader, Settings page) re-render.
- Toggle entry points (all live): AppHeader icon button (`AppHeader.tsx:48-56`), Settings appearance row (`SettingsAppearanceSection.tsx:34-36`), persisted via `preferences.save` (`ThemeContext.tsx:60-66`).
- Tests referencing the path: `Settings.lockGate.dom.test.tsx`, `U11.dom.test.tsx` (mock preference services with `"dark"` saves), `preferenceService.test.ts:24-25`, and the **preservation guard** `styles/vf-tokens.test.ts:188-195` asserting the `.dark` block still exists with `#1c1917`.

### 2.3 Governance documents

- `docs/architecture/ADRs/ADR-007-dark-mode-boundary.md` (6 lines): dark remains a separate semantic boundary; activation requires semantic roles inside the isolated boundary, parity tests across all surfaces/states/overlays, a separate owner gate, and its own ADR to supersede.
- `planning/micro-standard-ui-aux-integration-2026-09/DARK_MODE_BOUNDARY.md` (28 lines): current state, the future `styles/semantic-roles.css` proposal with the role list (`surface / surface-raised / text / text-secondary / text-tertiary / border / border-interactive / state-success / state-error / state-info / state-status / identity / identity-interactive / commitment / focus / scrim / elevation / chart-1..n`), and six owner-gate rules (light from `--vf-*`; separate approved dark set; computed-style parity matrix with contrast floors ≥4.5:1 text / ≥3:1 non-text / focus visible; word+non-color redundancy; PWA twins via the ThemeContext rewrite path; additive rollback).
- Register **U-03** (the dark-mode activation gate) is referenced by `SOURCE_OF_TRUTH_MATRIX.md:3,57`, `DARK_MODE_BOUNDARY.md:3`, `CONTEXT_ACKNOWLEDGEMENT.md:53`, `W1_REPORT.md:18`, and ADR-007's context; in `docs/architecture/MIGRATION_STATUS.md` it appears as owner-decision item #1 ("Dark Mode activation wave (boundary documented; separate gate)", `MIGRATION_STATUS.md:33`) and preserved-item "`.dark` legacy block — Dark Mode boundary — not activated (ADR-007)" (`:21`). Note: the literal string "U-03" does not appear in MIGRATION_STATUS.md itself, and "U-03" is overloaded in older quality docs (order-cancellation register) — the dark-mode U-03 lives in the run-folder register.
- `SOURCE_OF_TRUTH_MATRIX.md:57` states the layer rule: *"Primitives that need mode-adaptive surfaces resolve through the Micro alias names (`--color-*`), not raw `--vf-*`."* — the rule whose violation drives most of §3.

---

## 3. Activation safety assessment (static)

**Question:** if `.dark` were toggled on the current tree, what resolves, what keeps light values, what breaks?

### 3.1 What resolves correctly (legacy alias layer)

Everything in `index.css` feature styles that consumes `--color-*` Micro aliases — app chrome (`.micro-app`, header incl. scrolled translucent state `index.css:204-208`, bottom nav `:737-746`, FAB `:793-817`), cards, sheets, dialogs, all `.micro-field` form controls (`:1018-1082`), calendar (`:3326-3485`), financial tables/zebra separators, text hierarchy, state-pair surfaces (truth banners, warning panels). Dark-side text on dark-side surfaces passes comfortably (text-primary 16.47:1 on canvas; text-secondary 9.60:1 on surface; success 6.66:1 / danger 4.72:1 / warning 7.86:1 on `#332d27`). Elevation re-declares to stronger black shadows. The meta theme-color rewrite follows the computed canvas (`#1c1917`).

### 3.2 What keeps LIGHT values (the `--vf-*` direct bindings)

`--vf-*` contracts are declared only on `:root` (`vf-tokens.css:23-167`) and are intentionally not re-bound under `.dark`. Consumers:

- **All of `styles/primitives.css` (W2 layer)** — action-class fills/inks, chip surface, row title/caption/lead inks, field label/input inks, empty-state inks, markers, notice surfaces. This is the documented design for "class-critical bindings" but the binding set extends well beyond action classes into **body text roles**.
- Two `index.css` color outliers: `.micro-fab:hover` → `var(--vf-clay-interactive)` (`index.css:829`, hover-only) and `.micro-dialog-overlay` → `var(--vf-scrim)` (`:673`; a 45% black scrim that plausibly works over dark content but was never validated).
- `.micro-prim-*` consumers: 299 `<Button>` across 81 files (claim 2; spot-check 298 literal + 1 dynamic `action={…}` = 299 ✓), 4 ChoiceRow, 4 StatusChip, 8 EmptyState, 8 FeedbackNote, 3 Notice, 1 InlineError, 2 QuietCompletion, 9 `.micro-prim-row` sites, plus the AUX shell.

Result: **light islands** (white/warm-tint buttons, chips, inputs, notices floating on dark surfaces) — internally readable (e.g. save island ink 16.72:1; secondary 14.73:1; destructive 6.02:1) but visually unthemed — and, worse, **transparent-background text bindings that fail outright**:

### 3.3 Contrast failures if `.dark` is active (static WCAG 2.1 math on declared values)

| # | Surface | Declaration | Ratio | Floor | Effect |
|---|---|---|---|---|---|
| 1 | Quiet button text | `primitives.css:172` `color: var(--vf-ink)` #141413, transparent bg, on dark card/canvas | **1.05–1.18:1** | 4.5 | invisible — 36 correction/reversal entries (MR-03 financial touchpoints) |
| 2 | Commit button boundary | `primitives.css:144` bg `var(--vf-btn-primary-bg)` #141413 vs dark surface #27231f | **1.18:1** | 3.0 | high-consequence action button dissolves into the card (its white label stays 18.43:1) |
| 3 | Row title | `primitives.css:344` `color: var(--vf-ink)` on `.micro-prim-row` in cards | **1.18:1** | 4.5 | data-row titles invisible |
| 4 | Field label | `primitives.css:376` `color: var(--vf-ink)` | **1.18:1** | 4.5 | labels invisible (primitive not yet adopted — latent) |
| 5 | EmptyState title | `primitives.css:450` `color: var(--vf-ink)` | **1.05–1.18:1** | 4.5 | empty-state titles invisible (honest-void word+marker survives semantically, not visually) |
| 6 | Row caption / empty description / money unit | `primitives.css:350/456/480` `var(--vf-ink-secondary)` #4d4c48 | **1.81:1** | 4.5 | unreadable |
| 7 | Knowledge markers (dot/partial/tilde) | `primitives.css:23/28/36` | **1.81:1** | 3.0 | non-color signal marks fade below floor |
| 8 | Ghost button ink | `primitives.css:165` `var(--vf-ink-tertiary)` #6b6962, transparent | **3.18:1** | 4.5 | sub-floor (0 live consumers today — latent) |
| 9 | InlineError text | `primitives.css:275` `color: var(--vf-error)` #b53333, transparent bg | **2.59:1** | 4.5 | in-form error recovery unreadable (FeedbackNote's error channel) |
| 10 | Dark hairline border | `.dark` `--color-border` #51473c vs surface #27231f | **1.72:1** | 3.0 | structural separators sub-floor even in the *adapting* layer |
| 11 | Dark divider | `--color-divider` #62564b vs #27231f (scrolled header hairline `index.css:205`, sheet handle `:845`) | **2.19:1** | 3.0 | sub-floor |

Rows 1–9 all share one root cause: **text/mark roles in the primitive layer bind light-only `--vf-ink*`/`--vf-error` names instead of mode-adaptive aliases** — contradicting the layer rule recorded in `SOURCE_OF_TRUTH_MATRIX.md:57`. Rows 10–11 show even the v0 dark palette's own line tokens are sub-floor against its surfaces.

### 3.4 Contradictions (even where contrast passes)

- **U-02 violated in dark:** light retired teal everywhere (`--color-accent-text: var(--vf-ink)`, `W1_REPORT.md:23`); dark re-imports teal `#8fd5d6`/`#5ec0c1` as interactive ink, focus ring (`--ring`, base outline `index.css:180-184`, field focus `:1076-1077`), nav-active, month-selected edge, brand text/wordmark. Two different interaction-ink identities across themes.
- **D-01 violated in dark:** identity clay differs — FAB uses v0 `#d59172` in dark vs ratified `#d97757` in light; `--color-brand-pressed: #cc785c` is on the `RETIRED` list yet declared.
- **Accidental passes:** `--color-ink-on-color` is not re-declared, so `--primary-foreground`/`--secondary-foreground`/`--destructive-foreground` resolve to light ink #141413 on v0 clay/teal/danger fills — 6.4–8.6:1, passing by coincidence, not by decision. Drawer overlay (`drawer.tsx:29`) derives from the same token.
- **No `color-scheme` property anywhere** (grep: 0 hits) — native select dropdowns, date pickers, scrollbars, autofill render in light UA styling inside a dark page.

### 3.5 Verdict

**PARTIAL-BROKEN (unsafe to activate).** The alias-based shell re-themes; the primitive layer — the layer every one of the 52 migrated routes now renders its actions, rows, chips, feedback, and empty states through — keeps light values, with 9 sub-floor/invisible combinations including the quiet (correction/reversal) and commit (high-consequence) button classes. The block is simultaneously **contradictory** (retired palette, teal identity, dual clay) per its own governance docs. Since the theme is *reachable* (OS-default dark + live toggles), this is not a hypothetical: it is a latent live-surface defect gated only by documentation.

---

## 4. Light contract inventory

- **Standard 18 approved values** (`styles/vf-tokens.css:23-64`): surfaces canvas `#faf9f5` · ground `#f5f4ed` · recessed `#f0eee6` · surface `#ffffff` · tint `#e8e6dc` · soft/border `#d1cfc5` · border-interactive `#87867f`; inks `#141413` · secondary `#4d4c48` · tertiary `#6b6962` · on-dark `#ffffff` · on-tint `#141413` · pressed `#3d3d3a`; disabled surface `#f0eee6` / ink `#55524a`; focus `#141413` (+ field-border-focus `#87867f`); identity clay `#d97757` + interactive `#c96442`; semantic info `#2c84db` · status `#1490ff` · success `#629987` · error `#b53333`.
- **Action contracts** (`vf-tokens.css:55-85`): create (clay + ink, pressed clay-interactive, icon-ink white) · save (ground + ink + 2px clay-interactive pressed edge) · commit (ink fill + white ink, pressed #3d3d3a) · secondary (tint + on-tint, pressed soft) · outline (surface + interactive border + ink) · ghost (tertiary ink) · destructive (error ink + error border on surface).
- **Derivatives:** scrim `rgba(20,20,19,.45)` · header-translucent `rgba(250,249,245,.86)` (declared; not consumed — header uses its own `color-mix`) · warm shadow tone `rgba(60,50,40,x)`.
- **Micro runtime `:root` names** (`index.css:38-105`): 22 `--color-*` roles binding to `--vf-*` (with two Micro-kept text pairs: success `#256b4a/#e4f2ea`, warning `#7a5c20/#f6eccf`; danger pair uses Standard ground grammar), plus shadcn-level `--background/…/--ring` mapping and geometry/motion aliases. Text-tertiary has **no** Micro alias (removed dead in W6); the tier exists only as `--vf-ink-tertiary`.
- **Role coverage on the light side:** canvas/surface/surface-raised ✓ · text primary/secondary ✓ (tertiary tier = `--vf-ink-tertiary`, ghost-only) · border + border-interactive ✓ · focus ✓ (`--vf-focus`, `--vf-field-border-focus`) · disabled ✓ (opacity mechanism + disabled tokens) · selected ✓ (2px clay-interactive edge + weight + dot) · pressed ✓ · error/destructive ✓ · pending ✓ (info mark + clock, stateAdapter) · unknown ✓ (question marker, neutral tone — never failure) · empty/zero ✓ (three honest voids: unrecorded/unavailable/measured-zero) · status chips ✓ (word + marker + tone) · identity/brand + interactive ✓ · commitment ✓ (commit class) · scrim ✓ · elevation ✓ · chart series — none live (U-16 floors recorded) · safe-area/keyboard ✓ (env insets; `data-keyboard-open` chrome hiding) · reduced-motion ✓ (6 blocks).
- **Consumer scale (light, non-test):** `--color-text-secondary` 179 · `--color-border` 119 · `--color-text-primary` 89 · `--color-accent-text` 69 · `--color-warning-text` 62 · `--color-surface` 60 · `--color-accent-primary` 45 · `--color-bg-well` 37 · `--color-accent-soft` 23 · plus `.micro-field` family 411 class refs and `.micro-text-action` 104.

---

## 5. Parity analysis per area

Full row-per-role detail in **`DARK_MODE_PARITY_MATRIX.csv`** (63 rows: id, layer, light evidence, dark status, dark evidence, consumers, gap, severity, classification, notes). Summary:

| Area | Rows | PRESENT | PARTIAL | MISSING | N/A | Key facts |
|---|---|---|---|---|---|---|
| Core surfaces & text (aliases) | 17 | 15 | 0 | 1 (text-tertiary) | 0 | All re-declare under `.dark` — but with retired v0 values; hairlines/dividers sub-3:1 (A4-R04/R05); ink-on-color not re-declared (A4-R18) |
| `--vf-*` Standard contracts | 1 | 0 | 0 | 1 | 0 | By-design light-only until the semantic layer (A4-R21) |
| Interactive (focus/disabled/selected/pressed) | 4 | 1 | 2 | 0 | 1 | Focus present-but-teal (U-02 contradiction); selected/pressed partial (light islands); disabled is opacity → theme-proof |
| Button action classes (8) | 8 | 0 | 0 | 8 | 0 | **All 8 keep light values.** BROKEN: commit (1.18:1 boundary), quiet (1.05–1.18:1 text), ghost (3.18:1, latent). Light-islands: create/save/secondary/outline/destructive. Only the FAB (shell, alias-bound) actually re-themes |
| State semantics (chip/empty/notice/feedback/quiet-completion) | 5 | 0 | 4 | 1 | 0 | Grammar (word+marker+tone) is theme-independent and survives; surfaces don't. EmptyState BROKEN; InlineError channel 2.59:1; StatusChip/QuietCompletion/Notice = readable light islands |
| Data surfaces (rows/tables/sheets/calendar/filters/charts) | 12 | 5 | 2 | 2 | 3 | Feature CSS adapts (aliases); Row primitive BROKEN; Field primitive latent (0 adopters); charts/legends N/A (no live consumers, U-16) |
| AUX (nav/FAB/header/safe-area/keyboard/motion) | 7 | 4 | 0 | 0 | 3 | Shell adapts; nav-active + selected edges turn teal (U-02); FAB re-themes with v0 clay |
| PWA twins | 2 | 1 | 0 | 1 | 0 | Meta theme-color adapts (runtime rewrite works; dark meta pre-baked `#1c1917`); **manifest** `theme_color`/`background_color` static light — not coverable by the rewrite path |
| Cross-cutting (color-scheme / semantic layer / toggle / dark-variant / dark-only rules) | 5 | 3 | 0 | 2 | 1 | Toggle live (reachable); semantic-roles.css absent (proposal only); no `color-scheme`; Tailwind `dark:` registered, 0 usages; 6 dark-only structural rules exist (1 dead) |
| **Total** | **63** | **29** | **9** | **18** | **7** | 7 of the 18 MISSING are BROKEN-if-activated; ~half the PRESENT rows carry retired/contradictory values |

**Not applicable by design:** disabled (opacity), safe areas, keyboard states, reduced motion, charts/legends (no live consumers), Tailwind `dark:` variant (unused).

---

## 6. Standard contract check (micro-standard-v2)

31 files verified on disk (29 core + `MANIFEST.json` + `RELEASE.md`) — matches claim 15.

**Dark-mode/theme guidance: none.** `self-critique.md` states the restraint explicitly, twice: *"What remains deliberately restrained: no new palette, **no dark mode**, no chart library, no product policy"* (`self-critique.md:9`, repeated at `:27`). `visual-direction.md:3` defines the system as "warm, **light**, restrained, and operational". `color-system.md` defines the 12 approved roles + action roles with **light-surface-specific contrast bindings** ("Success `#629987` and Status `#1490FF` meet the 3:1 non-text minimum on the white Surface … on Ground/Recessed they fall below 3:1", `accessibility.md:23`). `accessibility.md:3` phrases focus as "warm ink … on **light** surfaces". The only "dark" mentions are `--vf-ink-on-dark` (white ink token), the gallery's dark-fill spinner track disclosure (`verification-report.md:50`), and historical decision-log records.

**Conclusion: the Standard defers dark mode entirely** — it neither defines dark roles nor forbids them; it is silent-by-restraint. That silence is exactly why ADR-007 keeps dark Micro-local.

**Minimum general contract clarification the Standard would need** (product-agnostic, no Micro vocabulary, no second palette source, no dark values):

1. A **mode-neutrality clause** in `color-system.md`: role *names* are theme-agnostic; the 18 approved values are the **light binding** of those roles; a consuming theme may bind a separately-approved dark set to the same role names without touching the light values (this ratifies the `semantic-roles` mechanism without specifying any dark hex).
2. A **per-surface contrast re-derivation rule**: the marker-hue × surface bindings computed in `accessibility.md` are properties of the *light* surface set; any theme must re-derive and document its own computed bindings against the same floors (text ≥4.5:1, non-text ≥3:1, focus visible).
3. A **UA color-scheme requirement**: a non-light theme must declare `color-scheme` so native controls/scrollbars match.
4. A statement that non-color semantics (word + marker) are theme-independent and therefore testable independently of palette.

Items 1–4 are steward-owned, owner-gated, and contain zero product-specific or Micro-specific content.

---

## 7. Option comparison

| Evidence dimension | **A — implement Dark Mode NOW (complete wave)** | **B — boundary-ready: close semantic contracts now, implement after next journey phase** | **C — remove/deprecate the `.dark` block** |
|---|---|---|---|
| Gap size (from matrix) | Must close 18 MISSING + 9 PARTIAL + re-derive all PRESENT values (29) into an approved dark set: a full palette decision (~18+ roles), `semantic-roles.css`, primitive re-binding, `color-scheme`, PWA manifest twin, parity-test matrix, dark capture suite | Same end-state work, **sequenced**: only the structural part (semantic roles + re-pointing primitive text bindings) lands now; palette/activation deferred | Tiny diff (~45-line block + 6 dark-only rules + `index.html:10` + `vf-tokens.test.ts:188-195` guard + ADR-007 amendment) |
| Journey-phase risk | High: dark wave lands *before* new screens exist — every new screen then needs dark review immediately, coupling two unstable surfaces | **Lowest**: semantic contracts landing *before* the journey phase means new screens consume theme-neutral roles automatically; no light-only hardcoding accrues | Medium: new screens keep binding `--vf-*` text directly (the A4-F02 pattern) — rework accrues exactly as today |
| Rework cost either way | Duplicates work if journey phase changes primitive consumption patterns; Standard silence forces a Micro-local palette that the Standard may later need to absorb (second-source risk) | Minimal waste: structural layer is a prerequisite of *any* future dark implementation, including A or C | Throws away the only working dark adaptations (shell aliases, tone-border rules, texture blends) that a future wave would rebuild; contradicts the registered owner decision "preserved Micro-local" (MIGRATION_STATUS.md:21) unless the owner re-decides |
| `.dark` block safety (§3) | Block is replaced wholesale by the wave — safety moot | Block stays but its *reachability* must be addressed (A4-F01: pin light or accept) — a one-line-ish owner decision, not a wave | Safety achieved by removal — dark toggle becomes a visual no-op (class applies, no CSS effect) |
| Strategy-constraint fit (same primitives/components; separate semantic mapping not duplicated components; no raw scattered dark hex; full state+surface parity; explicit contrast + non-color semantics; independent rollback; owner gate) | Fits only if Standard clarification (§6) lands first — otherwise violates "no second palette source" in spirit; parity matrix + contrast work unavoidable and large | Fits precisely: `semantic-roles.css` **is** the sanctioned separate mapping; additive rollback (DARK_MODE_BOUNDARY rule 6); owner gate (U-03) preserved for the palette step | Fits, but discards the documented boundary the owner already ratified; ADR-007 supersession requires owner action anyway |
| Dependency posture | Requires: owner gate grant (absent), Standard steward input (absent), unaudited-palette ratification (absent) | Requires only: owner nod for contract closure; Standard clarification is *parallel*, not blocking (roles can mirror the documented proposal) | Requires: owner reversal of the "preserved" register + test-guard change |

**Scoring:** A = highest cost/risk now, unblocks nothing the next phase needs; B = medium-small cost now, eliminates the compounding-rework failure mode, preserves the gate; C = smallest cost, but destroys ratified state and does not stop the A4-F02 binding pattern from spreading.

---

## 8. Recommendation — Option B, with an immediate owner decision on reachability

**Recommend Option B.** Rationale:

1. **ADR-007 and register U-03 already encode this sequencing** ("the Light integration must stabilize and pass owner review first"); the owner gate for the dark wave has not been granted. Implementing now (A) would require superseding an accepted ADR mid-cycle.
2. **The Standard is silent on dark** (§6). A dark palette built today would be Micro-local by necessity — creating exactly the second-source-of-truth risk the fixed strategy forbids. The minimum clarification is small, steward-owned, and parallel.
3. **Rework asymmetry:** every day the primitive layer binds text roles to light-only `--vf-*` names, new surfaces inherit the A4-F02 pattern. Closing the *contract* before the next journey phase means journey work lands theme-aware for free; deferring both means the future dark wave must re-audit every new screen. B is the only option that shrinks future work while spending little now.
4. **Rollback independence** is native to B (additive semantic layer; light output byte-identical).

**Mandatory companion decision (cannot wait for the wave):** A4-F01 — the unsafe `.dark` is runtime-reachable (OS-dark default + live toggles). The owner must choose: (a) pin light until the dark wave (e.g. `defaultTheme="light"` / `switchable={false}` — a product decision, not taken here), or (b) explicitly accept the broken dark surface as a known limitation. Doing nothing leaves a live, unreviewed, partly-invisible theme on a production surface, which contradicts ADR-007's own rationale.

### Implementation shape (if Option B is sanctioned)

- **Layer:** presentation only. New `apps/prototype-web/client/src/styles/semantic-roles.css` (layer 2.5: `--role-*` names bound to `--vf-*` for light), imported from `index.css` after `vf-tokens.css`; retarget `styles/primitives.css` text/mark/fill declarations from raw `--vf-ink*`/`--vf-error`/`--vf-success`… to the semantic roles (or the existing `--color-*` aliases) — **value-preserving in light** (computed styles must not change).
- **Owner:** owner (gate/decision) · MICRO_MAINTAINER (execution) · STANDARD_STEWARD (role-name ratification per §6).
- **Affected consumers:** `primitives.css` (all `.micro-prim-*` rules; the 299 Button, 4 ChoiceRow, 4 StatusChip, 8 EmptyState, 8 FeedbackNote, 3 Notice, 1 InlineError, 2 QuietCompletion, 9 Row sites inherit with **zero TSX changes**); optionally `index.css` `:root` aliases. No domain/application/storage changes.
- **Evidence:** this report's §3 table (9 failing bindings with declarations), `SOURCE_OF_TRUTH_MATRIX.md:57` layer rule, `DARK_MODE_BOUNDARY.md:12-24` role list.
- **Tests:** extend `styles/vf-tokens.test.ts` or add `styles/semantic-roles.test.ts` asserting (i) every `.micro-prim-*` text/mark declaration resolves through semantic roles/aliases — no direct `--vf-ink*`/semantic-hue binds in text roles; (ii) light computed values unchanged; (iii) every semantic role resolves in `:root`. The computed-style **parity matrix** (role × surface × state, both themes) remains the dark wave's acceptance gate per DARK_MODE_BOUNDARY rule 3.
- **Rollback boundary:** single-commit revert of `semantic-roles.css` + the `primitives.css` retarget; zero light-layer change by construction.

---

*Deliverables: this report + `DARK_MODE_PARITY_MATRIX.csv` (63-row parity matrix) + `worklog-agent-4.md`. Analysis was static and read-only; nothing inside `/home/z/my-project/analysis-work/micro` or `/home/z/my-project/analysis-work/documents` was created, modified, or executed.*

## 9. Findings (report ends with the findings table)

Classification legend (CONTEXT.md): `CLOSE_BEFORE_NEXT_PHASE` · `SAFE_TO_DEFER` · `OWNER_DECISION_REQUIRED` · `OUT_OF_SCOPE` · `ALREADY_CLOSED_WITH_EVIDENCE`. Severity: `BLOCKER` · `HIGH` · `MEDIUM` · `LOW`.

- **A4-01** — The "not activated" boundary is not runtime-enforced: OS-dark users load the broken theme by default and every user can toggle into it (App.tsx:13 `switchable`; ThemeContext.tsx:20-23/47-59; AppHeader.tsx:48-56; SettingsAppearanceSection.tsx:34-36).
- **A4-02** — Primitive layer binds text-critical roles to light-only `--vf-*` tokens (quiet/ghost inks, Row title/caption, Field label, EmptyState title/description, markers, money unit, InlineError ink — primitives.css:19-41/164-167/171-178/275/344-353/376/450-459/480), contradicting the layer rule in SOURCE_OF_TRUTH_MATRIX.md:57; this is the root cause of the §3 breakage and compounds with every new screen until closed.
- **A4-03** — `.dark` carries an unaudited palette: 13 hexes outside APPROVED_18/MICRO_KEPT/RETIRED registries + `#cc785c` (on the RETIRED list) as `--color-brand-pressed`; teal `#5ec0c1/#8fd5d6` reintroduced as accent/brand-text/ring contradicting U-02; dual clay identity (#d59172 vs ratified #d97757) contradicting D-01.
- **A4-04** — Even the adapting dark layer is sub-floor on structure: border #51473c = 1.72:1 and divider #62564b = 2.19:1 vs dark surface (non-text floor 3:1).
- **A4-05** — PWA manifest twin gap: `theme_color`/`background_color` static `#FAF9F5` (vite.config.ts:262-263); the ThemeContext rewrite path covers meta tags only — DARK_MODE_BOUNDARY.md rule 5's "PWA twins via the existing rewrite path" cannot reach the manifest.
- **A4-06** — No `color-scheme` declaration anywhere: native selects/date pickers/scrollbars/autofill render light inside a dark page.
- **A4-07** — Standard (micro-standard-v2) contains no dark-mode guidance (deliberate restraint; self-critique.md:9/27); the minimum mode-neutrality + per-surface contrast re-derivation + color-scheme clause (§6) is missing and steward-gated.
- **A4-08** — Guard blind spots: `design-token-guards.py:70-84` whitelists the `.dark` zone (unaudited hexes pass silently); `vf-tokens.test.ts:188-195` asserts the block exists (any Option-C removal must update the test); `.dark .micro-truth-banner` (index.css:392) targets a 0-consumer class; `--color-brand-pressed` is a dead mirror in both themes.
- **A4-09** — Claim 13 verified end-to-end: `.dark` untouched legacy with v0 values, re-declares Micro runtime names, ThemeContext + toggle + meta rewrite preserved, ADR-007 + DARK_MODE_BOUNDARY.md complete, `styles/semantic-roles.css` not implemented. The *documentation* half of the boundary is closed with evidence; the *runtime* half is A4-01.
- **A4-10** — Charts/legends: zero live consumers (grep chart|series = 0 in client/src); U-16 floors recorded as first-chart acceptance criteria — correctly out of scope.
- **A4-11** — FeedbackNote's W7 mixed-channel classifier (failure-text-as-success fix) is theme-independent and holds in dark, but its error channel renders through InlineError whose ink fails 2.59:1 on dark surfaces — semantic fix intact, presentation broken.

| ID | Area | Evidence path | Status | Severity | Owner | Affected layer | Action | Dependency | Acceptance criterion |
|---|---|---|---|---|---|---|---|---|---|
| A4-01 | Dark-mode runtime reachability | `apps/prototype-web/client/src/App.tsx:13` + `contexts/ThemeContext.tsx:20-23,47-59` + `components/layout/AppHeader.tsx:48-56` + `components/settings/SettingsAppearanceSection.tsx:34-36` | OWNER_DECISION_REQUIRED | HIGH | OWNER | App shell / contexts | Owner decides: pin light (`defaultTheme="light"` / `switchable={false}`) or formally accept the broken dark surface until the dark wave; record the decision in MIGRATION_STATUS.md U-03 register | None (decision only) | Decision recorded in MIGRATION_STATUS.md; if pinning: OS-dark first load renders light and the toggle is inert/hidden |
| A4-02 | Primitive text roles bound to light-only `--vf-*` | `apps/prototype-web/client/src/styles/primitives.css:19-41,164-167,171-178,275,344-353,376,450-459,480` vs `planning/.../SOURCE_OF_TRUTH_MATRIX.md:57` | CLOSE_BEFORE_NEXT_PHASE | HIGH | MICRO_MAINTAINER (STANDARD_STEWARD for role names) | styles/primitives (layer 3) | Land `styles/semantic-roles.css` + retarget primitive text/mark/fill bindings to semantic roles/aliases (value-preserving in light) before the next journey phase | A4-07 (parallel, non-blocking); owner nod | No `.micro-prim-*` text/mark declaration binds `--vf-ink*`/`--vf-error`/`--vf-success` directly; light computed styles unchanged; guard test green |
| A4-03 | `.dark` unaudited/contradictory palette | `apps/prototype-web/client/src/index.css:107-151` (+ `:386-397,592-595`); registries in `styles/vf-tokens.test.ts:16-64` | SAFE_TO_DEFER | MEDIUM | OWNER | index.css token zone | Replace v0 values with the owner-approved dark set inside the future dark wave (register U-03); no reuse of retired values without ratification (boundary rule 1) | A4-02, U-03 gate | Every dark hex belongs to the approved dark set or a documented derivative; teal/`#cc785c`/dual-clay contradictions resolved |
| A4-04 | Dark structural lines sub-floor | `index.css:114-115` (values) vs surfaces `:112-113`; consumers `:205,845` | SAFE_TO_DEFER | MEDIUM | NEXT_EXECUTION_AGENT (dark wave) | index.css token zone | Re-derive border/divider dark values to ≥3:1 against dark surfaces during the dark wave | U-03 gate | Computed non-text contrast ≥3:1 for separators on all dark surfaces |
| A4-05 | PWA manifest dark twin unreachable by rewrite path | `apps/prototype-web/vite.config.ts:262-263`; `contexts/ThemeContext.tsx:54-58`; `DARK_MODE_BOUNDARY.md:23` (rule 5) | SAFE_TO_DEFER | LOW | NEXT_EXECUTION_AGENT (dark wave) | PWA config | Dark-wave item: decide manifest strategy (static light vs build-time dual manifest); amend boundary rule 5 wording | U-03 gate | Manifest chrome matches the active theme or a documented single-chrome decision is recorded |
| A4-06 | No `color-scheme` for native widgets | grep `color-scheme` and `prefers-color-scheme` in `client/src/**/*.css` = 0 hits | SAFE_TO_DEFER | MEDIUM | NEXT_EXECUTION_AGENT (dark wave) | base layer | Declare `color-scheme: light dark` appropriately with the dark wave | U-03 gate | Native selects/date pickers/scrollbars match the active theme |
| A4-07 | Standard has no dark/theme contract | `documents/micro-standard-v2/self-critique.md:9,27`; `color-system.md`; `accessibility.md:23` | OWNER_DECISION_REQUIRED | LOW | STANDARD_STEWARD | Standard package (documents repo) | Add the minimum mode-neutrality clarification (§6 items 1–4) at the next Standard revision — product-agnostic, no dark values | Owner revision gate | Standard states role names are theme-agnostic, contrast bindings are per-theme re-derivations, and non-light themes require `color-scheme` |
| A4-08 | Dark-layer guard blind spots | `scripts/design-token-guards.py:70-84`; `styles/vf-tokens.test.ts:188-195`; `index.css:392-394`; `index.css:66,120` | SAFE_TO_DEFER | LOW | MICRO_MAINTAINER | guards / index.css | When the dark wave (or an Option-C removal) touches `.dark`: add a dark-value registry check; remove the dead `.micro-truth-banner` dark rule and the dead `--color-brand-pressed` mirror | A4-03 (same wave) | Guards validate dark hexes against the approved dark set; dead rules removed with 0-consumer proof |
| A4-09 | Claim 13 verification (boundary documentation) | `docs/architecture/ADRs/ADR-007-dark-mode-boundary.md`; `planning/.../DARK_MODE_BOUNDARY.md`; `styles/vf-tokens.css:16-17`; absence of `styles/semantic-roles.css` (verified) | ALREADY_CLOSED_WITH_EVIDENCE | LOW | — | docs / run folder | None (record verified); runtime caveat tracked as A4-01 | None | N/A — verified as claimed |
| A4-10 | Charts/legends dark parity | grep `chart`, `Chart`, `series` in `client/src` = 0; `MIGRATION_STATUS.md:37` (item 5, U-16) | OUT_OF_SCOPE | LOW | — | N/A | None — floors already recorded as first-chart acceptance criteria | First chart implementation | First chart ships with theme-aware series roles from the semantic layer |
| A4-11 | FeedbackNote error channel renders sub-floor in dark | `components/primitives/Notice.tsx:77-97` (classifier) + `styles/primitives.css:273-282` (InlineError ink) | SAFE_TO_DEFER | MEDIUM | NEXT_EXECUTION_AGENT (with A4-02) | primitives | Resolved by A4-02's semantic retarget (error ink must resolve per-theme); classifier needs no change | A4-02 | InlineError text ≥4.5:1 on all surfaces in both themes |
