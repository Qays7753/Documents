# AGENT-3 — Contract and Accessibility Audit (Micro Standard v2 Reconciliation, 2026-09)

Agent: Agent 3 — Contract and Accessibility Auditor
Mode: READ-ONLY analysis. No repository file was modified, created, or deleted. Only this report and the worklog append were written.
Baseline audited: `Documents/main @ 864263c190f5d3da6041acfafb0720e85ac6e320`, package `micro-standard-v2/` (31 files = 29 core + 2 metadata; verified against `MANIFEST.json` which still records `file_count: 29` — see Addition 10).

## Files read (mandatory reading completed)

1. `/home/z/my-project/worklog.md` (read first, as instructed).
2. Context pack (`recon-work/wt-context/planning/micro-standard-v2-reconciliation-context-2026-09/`):
   - `OWNER_UNIFIED_DECISION_REGISTER.md` (full — decisions U-01…U-20 and the ten approved additions).
   - `REPORTS_RECONCILIATION.md` (full — Flash primary, 5.3 cross-check; counts carry definitions).
   - `EXECUTION_PROMPT_CONTEXT.md` (full — Agent-3 mandate at §"Five-agent execution model"; ten additions at §B; stop conditions).
   - `REFERENCE_ZAI_FLASH_REPORT.md` §6 (Standard contract inventory, incl. 6.2 palette, 6.5 states, 6.6 accessibility+geometry) and §16 (owner decisions D-01…D-12); §3–§5 and §7 gap rows GAP-10/13/24/32/35/46 skimmed for evidence.
3. Standard package (`recon-work/Documents/micro-standard-v2/`), read fully as instructed: `accessibility.md`, `color-system.md`, `typography.md`, `component-states.md`, `component-contracts.md`, `responsive-geometry.md`, `motion-interaction.md`, `overlay-system.md`, `button-system.md`, `input-system.md`, `content-guidelines.md`, `design-tokens.css`, `design-tokens.json`.
   Supporting evidence also read: `verification-report.md`, `decision-log.md`, `coverage-matrix.json`, `README.md`, `RELEASE.md`, `MANIFEST.json`, `navigation-shell.md`, `iconography.md`, `empty-loading-error-states.md`, `surface-system.md`, `data-display-system.md`, `spacing-radius-elevation.md`, `visual-direction.md`, and `component-gallery.css/.html/.js` (targeted reads: tags, stripes, nav/FAB/safe-area, sheet/snackbar, focus trap, reduced motion).
4. Run state check: `micro-standard-v2-UPDATED/` in the run folder currently contains 31 files **byte-identical** to the baseline (diff-verified). The ten additions have not yet been applied; this audit is a true pre-edit gate.

## Contrast verification (all ratios recomputed, WCAG 2.1 relative luminance)

All 13 recorded pairs in `accessibility.md` reproduce to the digit: warm ink/canvas 17.50; warm ink/surface 18.43; Clay/surface 3.12; Clay/canvas 2.96; #C96442/surface 3.90; error/surface 6.02; info/surface 3.87; status/surface 3.25; success/surface 3.27; boundary/surface 3.65; surface-ring/warm-ink-fill 18.43; ink #141413 on Clay 5.90 (the "Clay icon / identity surface" row = the text-bearing-Create pairing); warm-ink snackbar text 18.43. Verification-report extras confirmed: ordinary-save pair 16.72 (warm ink on #F5F4ED), commit pair 18.43.

New pairs required by the ten additions (semantic hues and inks on the tint surfaces the tint grammar actually produces):

| Foreground | On #FFFFFF surface | On #FAF9F5 canvas | On #F5F4ED ground | On #F0EEE6 recessed |
|---|---|---|---|---|
| info `#2C84DB` | 3.87 ✓(non-text) | 3.67 ✓ | **3.51 ✓** | **3.33 ✓** |
| error `#B53333` | 6.02 ✓(text) | 5.72 ✓(text) | **5.46 ✓(text)** | **5.19 ✓(text)** |
| success `#629987` | 3.27 ✓(non-text) | 3.10 ✓(marginal) | **2.96 ✗ BELOW 3:1** | **2.81 ✗** |
| status `#1490FF` | 3.25 ✓(non-text) | 3.08 ✓(marginal) | **2.95 ✗ BELOW 3:1** | **2.80 ✗** |
| `#C96442` edge | 3.90 ✓ | 3.70 ✓ | 3.54 ✓ | — |
| boundary `#87867F` | 3.65 ✓ | — | 3.31 ✓ | 3.15 ✓ |
| ink-secondary `#4D4C48` (word) | — | 8.16 ✓AA | **7.80 ✓AA** | **7.40 ✓AA** |
| ink-tertiary `#6B6962` (word) | 5.49 ✓AA | 5.22 ✓AA | **4.98 ✓AA** | **4.73 ✓AA** |
| warm ink `#141413` (word) | 18.43 | 17.50 | 16.72 | 15.87 |

**Core finding (the tint-grammar trap):** the recorded tint grammar ("ground `#F5F4ED` + semantic ink") is contrast-valid only for **info** (3.51 on ground) and **error** (5.46 on ground, the sole text-safe semantic). **Success `#629987` (2.96) and status `#1490FF` (2.95) fall below the 3:1 non-text minimum on ground, and further on recessed (2.81/2.80).** They qualify only on white surface (3.27/3.25) and, marginally, on canvas (3.10/3.08). Every addition that places a semantic mark on a tinted chip must therefore restrict success/status hues to surface/canvas backgrounds, or use ink for the mark. Derivatives: scrim `rgba(20,20,19,.45)` over canvas composites ≈ `#92928F` (warm-ink text on it 5.91 — scrim is not a text background and must stay one); translucent header over dark content ≈ `#DAD9D5` with warm-ink text 13.05 ✓; disabled pair `#55524A`/`#F0EEE6` 6.72 ✓ (disabled exempt); white icon on Clay 3.12 (icon-only, non-text pass); `#141413` on Clay 5.90 (text-bearing Create) ✓.

## Verdict table (the ten approved additions)

| # | Addition | Verdict | One-line reason |
|---|---|---|---|
| 1 | Knowledge-state presentation contract | **PASS WITH CONDITIONS** | No new color needed; words must bind to text-safe inks and status/success markers must not sit on ground/recessed tints (<3:1) |
| 2 | Operational-row marker contract | **PASS WITH CONDITIONS** | Contract + gallery already exist (logical inline-start, ≤3px); stripe hue must meet 3:1 against the actual row background |
| 3 | AUX behavior addendum | **PASS WITH CONDITIONS** | Zero new colors (surface ladder + E2 + translucent header); route transition must bind to the existing 200ms token, not a new 260ms value; keyboard-hide must never hide focus/labels; nav needs explicit safe-area clearance |
| 4 | Period-control variants | **PASS WITH CONDITIONS** | No new color; native month input must keep LTR-isolated numeric entry, 44px hit, 13px label, visible focus |
| 5 | Quiet feedback variant | **PASS WITH CONDITIONS** | No new color; success check-marker fails 3:1 on tint quiet surfaces → ink marker on tints; inline completion needs a `role="status"` announcement channel |
| 6 | Overlay vs in-flow guidance | **PASS** | Composition-only; overlays keep focus containment; in-flow must not weaken focus visibility or the destructive confirmation path |
| 7 | Typography floor clarification | **PASS WITH CONDITIONS** | Needed: 13px floor must classify state words and nav labels (gallery `.tag`/`.navlabel` render them at 12px today) and disambiguate the tertiary-13 mono step as non-financial only |
| 8 | Icon and RTL adapter guidance | **PASS** | Mirror rule already contractual and implemented; binds to marker grammar; no library forced; no color impact |
| 9 | Authority ladder | **PASS** | Documentation-only (U-19); must not touch the verification boundary |
| 10 | Verification and manifest corrections | **PASS WITH CONDITIONS** | Make 29+2=31 explicit (GAP-46); preserve the exact not-tested list; re-run checks if gallery conditions land |

**REJECTs: none.** All ten additions are implementable inside the 18-value palette and the verified contracts, provided the conditions below are written into the contracts.

## Detailed per-addition analysis

### 1. Knowledge-state presentation contract — PASS WITH CONDITIONS

**Palette discipline:** no new value required. Words: `#141413` / `#4D4C48` / `#6B6962` (all AA on every approved background — 15.87…18.43, 7.40…8.16, 4.73…5.49). Markers: info `#2C84DB` (≥3.33 everywhere), error `#B53333` (5.19+), status `#1490FF` and success `#629987` only on surface/canvas. Tinted chips reuse ground `#F5F4ED` or white surface; the tint grammar needs **no** new hex.

**Conditions (binding):**
- C1.1 Word ink is always text-safe (`#141413`/`#4D4C48`/`#6B6962`; error `#B53333` permitted as word ink at 5.46/5.19 on tints). Semantic-hue **word text is forbidden** (info 3.51 on ground fails AA text; status 2.95 fails everything).
- C1.2 Status/success markers render on white surface (3.25/3.27) or canvas (3.08/3.10) only — never on ground (2.95/2.96) or recessed (2.80/2.81).
- C1.3 Knowledge `unknown` **binds to the existing unknown presentation** (`component-states.md` row 10; `empty-loading-error-states.md`): neutral ink + question/info marker; never success, never failure. This preserves "unknown ≠ failure".
- C1.4 Distinct non-color markers per state so the tier is readable without color and without ambiguity: e.g., unconfirmed → dashed/dotted-outline marker; incomplete → half-filled shape (mirrors `partial`); needs-review → eye marker (mirrors `reviewed`); estimated → approximation marker (≈), **not** the pending clock (an estimated value is not in-flight; sharing the clock would blur "pending ≠ settled"). Words remain examples (product-owned), per U-05/U-12 — no Micro vocabulary imposed.
- C1.5 Boundary statement required: knowledge states qualify **recorded** data reliability; they do not replace the honest voids (unrecorded → action chip; unavailable → "غير متاح"; measured zero → "0"). "Unconfirmed" ≠ "unrecorded".
- C1.6 An `estimated` financial value still renders as a financial value: ≥15px tabular mono, bidi-isolated; the knowledge word/marker is a qualifier beside it, never a shrink of the value (protects the type floor, Addition 7).
- C1.7 Do **not** copy the current gallery tag shorthand (see Deviation D1 below) into the knowledge-state demo.

**Contrast math:** see table above; the decisive numbers are success/ground 2.96 and status/ground 2.95 vs the 3:1 non-text threshold, and ink-secondary/ground 7.80 vs the 4.5:1 text threshold.

### 2. Operational-row marker contract — PASS WITH CONDITIONS

**Palette discipline:** no new value. The contract already exists (`component-contracts.md` "Operational row slots": optional state slot = one word + marker; optional ≤3px inline-start stripe in the state's semantic color, always paired with the word). Gallery implements it logically: `.row.state-edge::before { inset-inline-start: 0; width: 3px }` with `.stripe-pending` info, `.stripe-failed` error, `.stripe-review` status (`component-gallery.css` L600–608).

**Conditions:**
- C2.1 Stripe hue must clear 3:1 against the **actual row background**: on the white `.rowlist` surface all four hues pass (info 3.87, error 6.02, status 3.25, success 3.27); on canvas rows info 3.67 / error 5.72 / #C96442 3.70 pass, success 3.10 / status 3.08 pass only marginally; on ground/recessed rows success (2.96/2.81) and status (2.95/2.80) **fail** — restrict ground-tinted rows to info/error stripes or ink stripes.
- C2.2 Stripe stays ≤3px and absolutely positioned at the logical inline-start (never physical left/right) — the gallery already complies; the contract text must state `inset-inline-start` explicitly so RTL mirroring is guaranteed, not incidental.
- C2.3 Stripe never the sole signal — the state word + marker must exist inside the row (already stated; keep it verbatim in the amended text).
- C2.4 Geometry: the stripe must not consume hit area or induce horizontal overflow at 320px/200% (absolute positioning, no layout impact — verified pattern); it stays 3px at all text scales.
- C2.5 The `never color alone` rule is satisfied structurally (word + marker + stripe); confirm the amended wording repeats that low-ratio hues never carry meaning alone (`accessibility.md` L23).

### 3. AUX behavior addendum — PASS WITH CONDITIONS

**Palette discipline:** chrome must be built only from the surface ladder (`#FAF9F5`/`#F5F4ED`/`#F0EEE6`/`#FFFFFF`/`#E8E6DC`/`#D1CFC5`), the disclosed translucent header `rgba(250,249,245,0.86)`, and the recorded E2 shadow for the scroll border (`.topbar-scrolled` already demonstrates exactly this trio, `component-gallery.css` L672–676). **No new chrome color, blur value as decoration only, no new shadow tone.** The addendum is a behavior contract, not a route list (route families/classification stay product-owned — U-10, GAP-32/33).

**Conditions:**
- C3.1 Route-transition timing must bind to the **existing** motion token `--motion-normal` (200ms). Micro's observed 260ms route transition must not be imported as a new recorded timing without a recorded-basis update and re-verification; the Flash report's "motion table gains a route row" should land as a 200ms row (opacity/transform only).
- C3.2 Reduced motion: route transitions and keyboard-driven chrome hiding collapse under the `motion-interaction.md` contract — transitions become near-instant (≤ the 0.01s collapse already implemented for both the gallery control and `prefers-reduced-motion`) or opacity-only; arrival state is carried by content, never by the animation.
- C3.3 Keyboard-driven chrome hiding must never hide the focused control, its label, its helper/error text, or the focus indicator; suppressed labels are route-context/header labels only. When chrome returns (keyboard close), focus must not be lost, trapped, or moved without a user action.
- C3.4 Safe-area clearance: bottom navigation clears `env(safe-area-inset-bottom)` (the gallery currently demonstrates clearance only on the FAB, L699, and sheet body, L779 — `.bottomnav` itself has none). The addendum must specify nav clearance and the gallery should demonstrate it.
- C3.5 Scroll-border behavior = translucent header + E2 (existing derivatives); state it as such so no implementer invents a new border color or shadow.
- C3.6 Context-label suppression must not remove the only label of a control; if a route context label is suppressed, the screen title or field labels still identify the screen (word-carrying requirement).
- C3.7 Geometry: chrome hide/show must not cause horizontal overflow or layout shift at 320/360/390/430px and 100/130/200% (reserve the chrome's space or transition transform only).

### 4. Period-control variants — PASS WITH CONDITIONS

**Palette discipline:** none needed. Chip variant keeps the existing chip grammar (36px visual / 44px hit via `::after`, selection = 2px `#C96442` inset edge + bold ink — unchanged selection grammar); native variant keeps the input grammar (white surface, `--vf-border-soft`, warm-ink focus).

**Conditions:**
- C4.1 Native month/date input: numeric entry is LTR-isolated inside RTL composition — `dir="ltr"` + `unicode-bidi: isolate` on the entry control, exactly matching `input-system.md` ("English numerals, tabular figures, bidi isolation, and LTR numeric entry inside RTL composition"). The Arabic label stays RTL outside the isolated control.
- C4.2 44px touch floor on the control/wrapper; label at 13px (`--text-label-size`); visible focus (`:focus-visible` ring; where native internals cannot be styled, the wrapper carries the ring).
- C4.3 Native picker internals are accepted as-is (platform chrome); the Standard's contract scope is the wrapper, label, isolation, geometry, and focus — no attempt to restyle native internals, no new colors to do so.
- C4.4 Time semantics, default period, and ranges remain product-owned (U-08, D-07 default (b)); the Standard records the variant, not a policy.
- C4.5 Geometry: at 320px/200%, a month input + label must not overflow; the chip variant keeps horizontal scroll containment (`.chip-row` pattern).

### 5. Quiet feedback variant — PASS WITH CONDITIONS

**Palette discipline:** none needed. Quiet completion = quiet surface + word + check marker (`button-system.md` "State rules"; `component-states.md` "Quiet completion"). Snackbar stays optional with its verified contract (warm-ink fill, white text 18.43, 5000ms hold, `role=status`, z-500).

**Conditions:**
- C5.1 **Check-marker ink on tint surfaces:** success `#629987` on the Warm-Tint quiet surface = **2.96 < 3:1** — a success-colored check on a `#F5F4ED` button/notice fails non-text contrast. Binding: on tint surfaces the check marker renders in ink (`#141413` 16.72 / `#4D4C48` 7.80); the success hue is permitted for markers only on white surface (3.27). The past-tense word is always text-safe ink.
- C5.2 Inline completion must expose a **non-visual announcement channel** equivalent to the Snackbar's: `role="status"` (or `aria-live="polite"`) on the inline notice — otherwise the "valid alternative to Snackbar" is only visually equivalent. This matches Micro's verified inline regime (110 × `role="status"`).
- C5.3 Word + marker always (never color alone, never surface-return alone) — already contractual; repeat in the variant note.
- C5.4 The Snackbar is neither mandatory nor forbidden by the amended text (U-07: "Snackbar يبقى عقدًا اختياريًا غير مفعل"); the 5000ms hold applies only when a Snackbar is actually used.
- C5.5 Receipt/outcome cards and quiet notices sit on surface/ground with text-safe inks; semantic hues follow the tint rule (info/error on ground; success/status on surface only).

### 6. Overlay vs in-flow guidance — PASS

No palette, geometry, or motion impact. Binding: consequential confirmation and deletion use Dialog/Sheet with the **existing high-consequence anatomy** (consequence word + icon + short explanation + independent confirmation path); continuous explanation and editing stay in-flow. Verified safeguards that must be restated so the guidance cannot weaken them: overlays keep focus containment (gallery JS implements Escape + Tab trap + focus restore, `component-gallery.js` L233–246, L140–141), one active modal surface, shared scrim `rgba(20,20,19,.45)` visible (verification-report item 7), and in-flow blocks keep the dual focus treatment (2px outline on light controls / inset surface ring on filled) — the guidance text should say in-flow is not a license to drop focus visibility or the destructive confirmation step.

### 7. Typography floor clarification — PASS WITH CONDITIONS

**Current wording verified:** `typography.md` label = 13/1.4/500 "field labels, chips"; caption (floor) = 12/1.5/400 "the 12px floor; never for financial facts"; "Financial facts never render below 15px; the 12px caption floor carries metadata only"; amount = 15 mono/600; amount-input = 24 mono/600. No current wording allows 12px **labels** — the scale is already 13px — but two real contradictions exist and the clarification must resolve them:

**Conditions:**
- C7.1 **12px state words in the gallery:** `.tag { font-size: var(--text-caption-size) }` (12px) renders every state word ("Pending", "Posted", "Failed", "Unknown", "Reviewed" — `component-gallery.html` L318–686) at 12px. Under the clarified floor, state words are labels → **`.tag` must move to `--text-label-size` (13px)** in the same wave, or the Standard self-contradicts. There is no literal `font-size:12px` in the gallery; the violation is via the caption token.
- C7.2 **12px nav labels:** `.navlabel` (12px, L720–722) — navigation labels are labels → 13px.
- C7.3 **Tertiary-13 ambiguity:** the numeric ladder ("hero 28, primary 24, secondary 15, tertiary 13") coexists with "financial facts never render below 15px". The clarification must state: **tertiary 13 mono is non-financial numeric metadata only** (counts, dates, IDs); any monetary value, delta, or unit renders at ≥15px (amount 15 / kpi 24 / hero 28 / amount-input 24).
- C7.4 Caption row rewording: "12px only for **non-financial** metadata (timestamps, counts, helper captions); never for state words, labels, field labels, nav labels, units, deltas, or financial facts." Acceptable 12px uses today: `.row-sub` dates, `.helper`, `.frame-bar`, `.demo-note`, `.state-tag` (gallery documentation chrome). `.error-msg` at 12px is contrast-safe (error ink 6.02) but should move to 13px label size as error text is label-like — recommend, not block.
- C7.5 Financial legibility stays: facts/amounts never below 15px; the currency unit `د.أ`/`دأ` renders beside the value (never inside the numeric string) and should not drop to 12px (treat as part of the financial fact; ≥13px, preferably with the value).
- C7.6 Scaling: 13px labels at 200%/320px must not overflow (verified pattern: wrapping rows/chips; keep `word-break` behavior for Arabic).

### 8. Icon and RTL adapter guidance — PASS

`iconography.md` already holds the rule ("Directional icons mirror in RTL; symmetric and object icons do not"); the gallery implements `[dir="rtl"] .mirror { transform: scaleX(-1) }` (L143). Binding guidance: mirror flags apply to directional glyphs only; never mirror numerals or Latin text inside glyphs; semantic icon roles bind to the state-marker grammar (word + marker; hues per the tint rule in this report); the 43-glyph registry stays a contractual reference, no production library forced (U-13 — Lucide with mirror flags is a valid carrier); icon sizes stay 20/24; icons never replace financial wording. No color impact; no conditions beyond restating the tint rule for semantic icon hues.

### 9. Authority ladder — PASS

Documentation-only (U-19): Standard = visual contracts; Micro `--vf-*` mapping = runtime carrier; Micro docs = implementation guidance; domain/application/storage = meaning and persistence. Condition-free **provided** the wording lands in README/MANIFEST/RELEASE without touching the verification boundary, the palette statements, or the action-class tables. It changes no color, no contrast, no geometry.

### 10. Verification and manifest corrections — PASS WITH CONDITIONS

**Conditions:**
- C10.1 `MANIFEST.json` currently says `file_count: 29` while 31 files are on disk (GAP-46). The correction must make the split explicit — e.g., `"file_count": {"core": 29, "metadata": 2, "total": 31}` or equivalent wording — so the count is self-documenting.
- C10.2 Preserve the exact testing limitations verbatim: no physical-device testing, no screen-reader testing, no real-device performance/PWA claims (`verification-report.md` "What was not tested"; `coverage-matrix.json` `requires_separate_testing`). No new claims may appear.
- C10.3 If the gallery conditions land (C7.1/C7.2 tag/nav 13px, C3.4 nav safe-area, D1 tag-word ink fix), the geometry/contrast/reduced-motion checks must be re-run and `verification-report.md`/`coverage-matrix.json` refreshed — the recorded evidence then covers the amended contracts.
- C10.4 Keep the 18-hex audit statement intact ("zero new hex introduced"); the additions add no value, so the statement remains true.

## Cross-cutting checks

**RTL/geometry (320/360/390/430px, 100/130/200%):** edge stripe uses logical `inset-inline-start` (verified) — the contract must mandate it; month input LTR-isolated inside RTL (C4.1); keyboard chrome hiding must not trap or clip content (C3.3/C3.7); safe-area clearance specified for bottom nav (C3.4); knowledge-state chips wrap (inline-flex + wrap patterns exist); no addition introduces fixed widths that could overflow at 320px/200%.

**Reduced motion:** route transitions and keyboard chrome hiding collapse to near-instant/opacity-only under both the gallery control and `prefers-reduced-motion` (existing 0.01ms collapse, `component-gallery.css` L975–989); state/action meaning preserved via words, markers, `aria-busy` — the AUX addendum must cite this contract explicitly (C3.2).

**Focus:** overlays keep focus containment (trap + restore verified in gallery JS); in-flow guidance must not weaken the dual focus treatment; keyboard-driven chrome hiding never hides focus or the active control's labels (C3.3); period native input keeps visible focus (C4.2).

**Non-color redundancy:** all ten carry word + non-color markers structurally. Risk points are (a) the stripe (mitigated: word+marker always in-row), (b) the quiet check (mitigated: past-tense word + announcement channel), (c) knowledge states (mitigated: distinct markers per C1.4). No addition can be read as color-only once the conditions are written in.

**State/decision consistency (dimension 8):** the ten additions do not weaken any verified contract **with the conditions applied**: state matrix unchanged (knowledge tier is a presentation contract, not new matrix rows — U-11 wording "presentation contract فقط"); honest voids preserved (C1.5 boundary); pending ≠ success preserved (nothing touches it; estimated must not borrow the clock marker, C1.4); unknown ≠ failure preserved (C1.3 binding); selection grammar 2px `#C96442` edge unchanged (period chip variant reuses it); one-active-modal and scrim visibility untouched (in-flow guidance reduces overlay use, never stacks them); 18-hex palette untouched (zero new values required by any addition).

## Pre-existing deviations found (fix in the same wave; not caused by the additions)

- **D1 — Semantic-hue word text in gallery tags (contradicts `accessibility.md` L23 and the CSS's own comment):** `.tag-positive`/`.tag-operational`/`.tag-pending`/`.tag-review` set the **word** `color:` to success/info/status on the ground tint (`component-gallery.css` L427–432) → 2.95–3.51:1, failing AA text (4.5). Only `.tag-negative` is text-safe (error 5.46 on ground). The comment at L425–426 claims the opposite intent. Fix: word → `#4D4C48` (7.80) or `#141413`; hue stays on the leading marker icon only. The knowledge-state demo (Addition 1) must not replicate this shorthand (C1.7).
- **D2 — 12px state words and nav labels** (`.tag`, `.navlabel` via `--text-caption-size`) — see C7.1/C7.2.
- **D3 — `.bottomnav` lacks `env(safe-area-inset-bottom)` clearance** (only FAB L699 and sheet L779 have it) — see C3.4.
- **D4 — Tertiary-13 mono ambiguity** vs the ≥15px financial floor — see C7.3.

## Final summary

**PASS: 3** (Additions 6, 8, 9). **PASS WITH CONDITIONS: 7** (Additions 1, 2, 3, 4, 5, 7, 10). **REJECT: 0.** No addition requires a new color value; none relies on color alone once the stated conditions are contractual; none weakens a verified contract.

## Risks

- **R1 (highest):** the tint grammar read literally ("ground + semantic ink") produces sub-3:1 marks for success (2.96) and status (2.95). Without the background restriction written into the contracts (C1.2, C2.1, C5.1), implementers will ship failing marks. Recommend recording the extended contrast table above in `accessibility.md`.
- **R2:** copying the gallery tag shorthand (D1) into the knowledge-state or quiet-feedback demos would institutionalize an AA text failure behind a comment that claims compliance.
- **R3:** landing the 13px label floor without fixing `.tag`/`.navlabel` (D2) leaves the package self-contradictory; the fix is two token swaps in `component-gallery.css`.
- **R4:** importing Micro's 260ms route transition as a new motion value breaks the recorded motion basis; bind to `--motion-normal` (C3.1).
- **R5:** native month-input internals are unstylable; scope the contract to wrapper/isolation/focus or the Standard will make claims it cannot verify (C4.3).
- **R6:** estimated/incomplete values rendered at tertiary-13 would breach the financial floor; the disambiguation (C7.3) must be explicit.
- **R7:** AUX keyboard-hide, if implemented without C3.3, can hide the focused field's label or the focus ring — an accessibility regression the current Micro code does not have; the contract must forbid it.
- **R8:** white text directly on the scrim composite (≈3.12) — scrim is never a text background; keep the one-scrim/overlay-owns-text rule.
