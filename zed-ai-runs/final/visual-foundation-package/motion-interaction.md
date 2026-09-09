# Motion and Interaction

## Principles

Short, purposeful, honest: 80–240ms, unified easings (enter decelerating, exit accelerating), nothing that delays a final value, nothing decorative. The timing system is the repair run's mandated set (R-01) — it supersedes the source-inherited 120/200/300/340 values, which were also never wired to real transitions in the original package (R-02). Bounce, springs, glow, page-wide slides, parallax, skeleton waves, and count-up numbers remain prohibited — the neutral SOP bans automatic count-up, and this package renders final numeric values immediately while the bar alone moves (R-14). Every transition moves one property; no layout shift is ever acceptable; reduced motion removes spatial movement while preserving every state meaning and outcome.

## Motion tokens (the timing system)

| Token | Value | Use |
|---|---|---|
| `motion.press` | 80ms ease-out | press scale 0.97 |
| `motion.fast` | 120ms | menus, quick fades, border color, snackbar exit |
| `motion.normal` | 200ms | standard transitions, segmented thumbs, snackbar enter, relationship-bar movement, row insertion flash |
| `motion.sheet-in` | 240ms `cubic-bezier(.16,1,.3,1)` | sheet enter |
| `motion.sheet-out` | 180ms ease-in | sheet exit |
| `motion.dialog-in` | 160ms `cubic-bezier(.16,1,.3,1)` | dialog enter (scale 0.96→1 + fade) |
| `motion.dialog-out` | 120ms ease-in | dialog exit |
| `motion.scrim` | 200ms ease-out | scrim fade (in and out) |
| `motion.skeleton` | 1.5s infinite | skeleton pulse (opacity 1↔0.5) |
| `snackbar.duration` | 5000ms | auto-dismiss (+120ms exit) |
| `ease.standard` | `cubic-bezier(0.16, 1, 0.3, 1)` | enter easing for overlays |
| `ease.out` / `ease.in` | enter / exit | easing polarity |

Keyframes inherited verbatim from `tailwind.config.source.js:212–220` (`slideUp`, `slideDown`, `fadeIn`, `scaleIn`, `snackbarIn`, `skeleton`, `ghostOut`) plus `spin` for button loading, `rowIn`/`rowFlash` for local row insertion feedback. Every overlay transition is now actually implemented (R-02) — the sheet, scrim, dialog, snackbar, and menu all transition on real CSS properties with transition-aware hide sequencing (the `[hidden]` guard lands only after the exit duration).

## Interaction grammar

**Press.** Every tappable surface uses `.press` — 80ms transform transition, `:active` scale 0.97. Press is also signaled by color where the control has a pressed step (primary 700→800, accent 600→700, identity FAB 500→600). Press feedback works identically in RTL and at every text scale.

**Focus.** The dual-ring contract (R-05): on light surfaces a 2px `accent.600` ring with 2px offset (4.38–5.08:1 on every legal surface); on dark filled controls (primary/accent/semantic fills, FAB, identity icon buttons, selected chips) an inset 2px `surface` ring at −4px — 5.02–8.24:1 against every fill. Inputs shift their border to `accent.500` **and** show the ring; nothing may set `outline: none` without a replacement (R-04). Focus moves into overlays when they open and returns to the trigger when they close (R-07). The page scroll locks while an overlay is open (R-28).

**Loading.** Buttons enter a loading state: the leading icon swaps for a 20px 2-stroke spinner inside a fixed icon slot — the label persists, the width never shifts, and the control is disabled with `aria-busy` so repeated activation is impossible (the source's double-submit guard, raw SOP §8.5; R-24). Content areas load with skeletons, never spinners (raw SOP §8.1).

**Completion.** The quiet-completion pattern (SOP §9): after a successful action the trigger briefly shows a check glyph in the positive tint (800ms, color-only under reduced motion), then resets, and the snackbar confirms.

**Selection.** Chips and segmented controls move their active state with 200ms tint/thumb/indicator transitions; one active element per single-choice group (multi-choice filter groups toggle independently); selection is always visible without motion; segmented controls move with arrow keys (RTL-aware) and expose radiogroup semantics (R-21/R-25).

**Directional feedback.** A row or control that opens a new context fires a short chevron nudge toward the reading end — 120ms, 3px translate, accent.600 tint, mirrored in RTL (R-10). This is feedback, not navigation: the gallery fires it on tap without leaving the page.

**Overlay choreography.** Scrim fades 200ms; the sheet slides in 240ms / out 180ms with the standard easing; the dialog scales+ fades 160/120; the snackbar slides+ fades 200 in / 120 out; the menu fades+scales 120. Exits always use the exit easing. Every overlay has exactly one obvious close path, and closed overlays are genuinely gone (the `[hidden]` guard, R-03).

**Local list changes.** Row removal collapses only that row (ghostOut 200ms, opacity+height) and Undo restores the real node at its old position (R-13). Insertion prepends with a quiet 600ms positive-tint flash. No page-wide sliding, no cascades.

**Bar movement.** When the summary metric's relationship changes, the bar segments animate width over 200ms while the two supporting numbers swap immediately — the final values never wait for motion (R-14), and the `aria-label` carries the live numbers.

**Filtering.** The Filter control opens a staged sheet: selections are draft state until Apply; Cancel, scrim tap, Escape, and drag-to-dismiss all discard the draft; reopening stages from the last applied state (R-08/R-29). The compact sort dropdown is an immediate single-choice control (the one sanctioned simple context for a dropdown).

## Drag (sheet)

Ported from the source component (`BottomSheet.jsx:88–126`) and now actually interactive (R-06 audit finding): two snap points — collapsed (≤84% height) and expanded (94%); drag up past −50px expands, drag down past +130px collapses (when expanded) or dismisses (when collapsed); upward travel is clamped at −44px while collapsed; the transition is suppressed during the drag (`is-dragging`) and restored on release. The drag works with pointer, touch, and pen; the handle reserves `touch-action: none` so vertical drags on it never scroll the page.

## Feedback stack

After every consequential action: press (80ms) → control state change (loading/quiet-completion) → snackbar confirmation (5s, with a real Undo action where the action is reversible — the source's soft-delete + undo pattern). Haptics accompanied every interaction in the source product (`hapticLight`); this visual-only package records them as a documented interaction note but cannot render them.

## Reduced motion

Two mechanisms: the CSS kill-switch (`prefers-reduced-motion: reduce` → all animations/transitions 0.01ms, `index.css.source:177–185`) and the gallery's manual `data-motion="reduced"` toggle. Under reduced motion: overlays appear instantly at final position, the sheet still drags (user-initiated motion is allowed) but snaps without transition, skeletons are static, press feedback is color-only, the bar jumps to its final width, and row removal is instant. State clarity and outcome proof never depend on movement: fills, icons, text, and DOM state carry the meaning.

## Prohibited

Bounce or elastic overshoot · decorative springs · automatic count-up · page-wide slide transitions · motion that delays showing final values · skeleton waves (pulse is opacity-only) · any animation longer than 400ms in the everyday layer · layout-shifting transitions · motion that runs without a state purpose · drag handlers that hijack vertical page scrolling (the rail explicitly allows `pan-x pan-y`).
