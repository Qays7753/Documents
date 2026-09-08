# Motion and Interaction

## Principles

Short, purposeful, honest: 120–400ms, unified easings (enter decelerating, exit accelerating), nothing that delays a final value, nothing decorative. The band comes from raw SOP §8.2 (150–300ms for UI transitions, with press faster at ~120ms and the sheet's 340ms as the one documented exception). Bounce, springs, page-wide slides, parallax, and count-up numbers are prohibited — the neutral SOP explicitly bans automatic count-up, resolving the raw SOP's contradictory mention (D-24). Every transition moves one property; no layout shift is ever acceptable.

## Motion tokens

| Token | Value | Use |
|---|---|---|
| `motion.press` | 120ms ease-out | press scale 0.97 |
| `motion.fast` | 200ms | scrim fade, border color, header shadow appearance |
| `motion.base` | 300ms | segmented thumb, snackbar enter/exit, nav color change, ghost-card collapse |
| `motion.sheet` | 340ms `cubic-bezier(.16,1,.3,1)` | sheet slide + height snap |
| `motion.skeleton` | 1.5s infinite | skeleton pulse (opacity 1↔0.5) |
| `snackbar.duration` | 5000ms | auto-dismiss (+250ms exit delay) |
| `ease.standard` | `cubic-bezier(0.16, 1, 0.3, 1)` | enter easing for overlays |
| `ease.out` / `ease.in` | enter / exit | easing polarity (corrected: source used ease-out on exits) |

Keyframes inherited verbatim from `tailwind.config.source.js:212–220`: `slideUp`, `slideDown`, `fadeIn`, `scaleIn`, `snackbarIn`, `skeleton`, `ghostOut`; plus a `spin` for button loading.

## Interaction grammar

**Press.** Every tappable surface uses `.press` — 120ms transform transition, `:active` scale 0.97 (`index.css.source:51–52`). Press is also signaled by color where the control has a pressed step (primary 700→800, accent 600→700). Press feedback works identically in RTL and large text.

**Focus.** The unified `:focus-visible` ring (2px accent.600, offset 2) — see `accessibility.md`. Focus moves into overlays when they open and returns to the trigger when they close.

**Loading.** Buttons enter a loading state: label dims, a 20px 2-stroke spinner (currentColor) rotates, the control is disabled to prevent duplicate activation (the source's double-submit guard, raw SOP §8.5). Content areas load with skeletons, never spinners (raw SOP §8.1).

**Completion.** The quiet-completion pattern (SOP §9): after a successful action the trigger briefly shows a check-circle glyph in the positive tint (800ms, color-only under reduced motion), then resets and the snackbar confirms.

**Selection.** Chips and segmented controls move their active state with a 200–300ms tint/thumb transition; one active element per group; selection is always visible without motion.

**Overlay choreography.** Scrim fades 200ms; sheet slides 340ms with the standard easing; dialog scales in 200ms (`scaleIn` 0.95→1); snackbar slides+fade 300ms. Exits reverse: snackbar 300ms down+fade, sheet 340ms down, dialog 200ms fade+scale. Every overlay has exactly one obvious close path.

## Drag (sheet)

The source sheet is draggable: two snap points (collapsed 84vh, expanded 94vh), handle drag-up past −50px expands, drag-down past +130px collapses or closes, and the collapsed state clamps upward travel at −44px (`BottomSheet.jsx:88–126`). Transition is suppressed during the drag and restored (`.3s` transform) on release. This package preserves the geometry and motion exactly.

## Reduced motion

Two mechanisms, both inherited or normalized: the CSS kill-switch (`prefers-reduced-motion: reduce` → all animations/transitions 0.01ms, `index.css.source:177–185`) and the gallery's manual `data-motion="reduced"` toggle. Under reduced motion: overlays appear instantly at final position, skeletons are static, press feedback is color-only, and nothing oscillates. State clarity never depends on movement.

## Feedback stack

After every consequential action: press (120ms) → control state change (loading/quiet-completion) → snackbar confirmation (5s, with undo action where the action is reversible — the source's soft-delete + undo pattern). Haptics accompanied every interaction in the source product (`hapticLight`); this visual-only package records them as a documented interaction note but cannot render them.

## Prohibited

Bounce or elastic overshoot · decorative springs · automatic count-up · page-wide slide transitions · motion that delays showing final values · any animation longer than 400ms in the everyday layer · layout-shifting transitions · motion that runs without a state purpose.
