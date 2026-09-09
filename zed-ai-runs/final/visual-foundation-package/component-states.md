# Component States

The state matrix for every family in the gallery. "✅" marks states demonstrated live in `component-gallery.html` (see `coverage-matrix.json` for anchor IDs and verification status); every non-demonstrated state is specified in its family contract. The repair run rebuilt this matrix against the actual DOM — every ✅ below maps to a verifiable selector (R-31).

| Family | Default | Pressed / Active | Focused | Disabled | Loading | Error / Destructive | Selected | Other |
|---|---|---|---|---|---|---|---|---|
| Button — primary | ✅ | ✅ (800 fill + 0.97 @80ms) | ✅ (dual ring) | ✅ (`#B7B2A6`+white) | ✅ (spinner-in-slot + guard + aria-busy) | — | — | ✅ quiet-completion (check + tint) |
| Button — secondary | ✅ | ✅ (700 fill) | ✅ | ✅ | — | — | — | — |
| Button — outline / ghost | ✅ | ✅ | ✅ | ✅ | — | — | — | — |
| Button — destructive | ✅ | ✅ | ✅ | ✅ | — | ✅ negative.600 fill | — | — |
| Button — semantic filled | ✅ | ✅ | ✅ | ✅ | — | — | — | positive / operational |
| Input — text | ✅ | — | ✅ (ring visible — R-04) | ✅ | — | ✅ (message + icon) | — | ✅ helper, long content |
| Input — search | ✅ | — | ✅ | — | — | — | — | ✅ clear button + refocus |
| Input — select / menu | ✅ | ✅ (panel 120ms) | ✅ | — | — | — | ✅ (option + check 4.51) | ✅ Escape/outside close, focus return |
| Input — amount | ✅ | — | ✅ | — | — | ✅ (aria-invalid) | — | ✅ live grouping, LTR |
| Input — recovery loop | ✅ | — | ✅ | — | ✅ (guarded save) | ✅ (error at the control, input preserved) | — | ✅ completion cycle |
| Filter control | ✅ | ✅ | ✅ | — | — | — | ✅ (count badge) | ✅ aria-expanded |
| Filter sheet | ✅ (closed) | ✅ open 240 / expanded snap | ✅ (trap + restore) | — | — | — | ✅ staged chips (pressed/checked) | ✅ drag-to-dismiss, Apply/Reset/Cancel |
| Chip | ✅ | ✅ | ✅ | ✅ | — | — | ✅ (multi + single groups) | ✅ 44px hit |
| Segmented (pill) | ✅ | ✅ (thumb slides 200ms) | ✅ | ✅ (whole) | — | — | ✅ (one, arrows) | ✅ badge counts, radiogroup |
| Segmented (underline) | ✅ | ✅ (indicator slides) | ✅ | ✅ | — | — | ✅ (one, arrows) | ✅ tablist semantics |
| Metric — direct value | ✅ | — | — | — | ✅ (skeleton) | — | — | ✅ change line |
| Metric — summary | ✅ | ✅ (update cycle) | — | — | — | — | — | ✅ bar moves 200ms, numbers immediate |
| Row | ✅ | ✅ (chevron nudge) | ✅ | — | — | ✅ (semantic tiles) | — | ✅ wrap+clamp, alt, status tag, bidi |
| Row — local changes | ✅ | ✅ (add flash / remove collapse) | ✅ | — | — | — | — | ✅ real undo restores node |
| Rail card | ✅ | ✅ (0.97) | ✅ (ring) | — | — | — | — | ✅ snap, drag, peek cue, pan-x+pan-y |
| Top bar | ✅ | — | ✅ (actions) | — | — | — | — | ✅ scrolled E2 veil |
| Bottom nav | ✅ | ✅ (pill) | ✅ | — | — | — | ✅ (one + aria-current) | ✅ 4 destinations, 24px icons |
| FAB | ✅ | ✅ (600 fill + 0.97) | ✅ (inset ring) | — | — | — | — | ✅ identity.500, opens sheet |
| Sheet | ✅ (closed) | ✅ open 240 + expanded snap | ✅ (trap) | — | — | ✅ destructive row | — | ✅ drag handle, real motion |
| Dialog | ✅ (closed) | ✅ (confirm) | ✅ (trap) | — | — | ✅ destructive confirm pairing | — | ✅ centered anchor, 160/120 |
| Menu / dropdown | ✅ | ✅ (open 120ms) | ✅ | — | — | — | ✅ (option) | ✅ outside/Escape close |
| Snackbar | ✅ (hidden) | ✅ (action 44px) | ✅ | — | — | ✅ (error variant spec) | — | ✅ 5s timer, real undo, 200/120 |
| Empty state | ✅ | — | ✅ (action) | — | — | — | — | ✅ icon tile + action |
| No-results | ✅ | — | ✅ (clear action) | — | — | — | — | ✅ wired to live filter state |
| Skeleton | ✅ | — | — | — | ✅ (pulse) | — | — | ✅ static under reduced motion |
| Error / retry | ✅ | ✅ (retry guarded) | ✅ | — | ✅ (retrying) | ✅ | — | — |
| Icon | ✅ | — | — | — | — | — | — | ✅ 43-glyph registry + mirror flags |

## Loading semantics

Button loading disables activation for the entire request (no double submits) while the label persists and the spinner occupies the fixed icon slot (R-24). Content loading is always skeletons — 12px-radius `recessed` blocks pulsing 1.5s (opacity 1↔0.5, never a wave), static under reduced motion, laid out in the shape of the content they replace. Spinners exist only inside buttons and search fields, never as page-level loaders.

## Selection semantics

One selected element per single-choice group: one chip, one segment, one nav destination, one dropdown option; multi-choice groups (filter status/type) toggle independently via `aria-pressed`. Selection is always visible without motion and without color alone (fill + weight, check glyph, underline, or thumb position), and always exposed programmatically (R-21).

## Error semantics

Errors always pair the negative ramp with an icon and explanatory text at 12px minimum; they never block retry; they render **at the failing control** and preserve the user's input (R-15); destructive confirmations always precede irreversible actions or offer a real undo.

## Disabled semantics

Disabled means inert: `#B7B2A6` surface, no shadow, no press, no focus, cursor suppressed, and exempt from contrast requirements — but visually distinguishable from selected states (selected is saturated and carries weight; disabled is flat and grey-warm).
