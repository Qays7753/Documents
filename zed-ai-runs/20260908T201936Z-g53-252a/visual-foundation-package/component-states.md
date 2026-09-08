# Component States

The state matrix for every family in the gallery. "✅" marks states demonstrated live in `component-gallery.html` (see `coverage-matrix.json` for anchor IDs and verification status); every non-demonstrated state is specified in its family contract.

| Family | Default | Pressed / Active | Focused | Disabled | Loading | Error / Destructive | Selected | Other |
|---|---|---|---|---|---|---|---|---|
| Button — primary | ✅ | ✅ (800 fill + 0.97) | ✅ (ring) | ✅ (`#B7B2A6`+white) | ✅ (spinner + guard) | — | — | ✅ quiet-completion (check) |
| Button — secondary | ✅ | ✅ (700 fill) | ✅ | ✅ | ✅ | — | — | — |
| Button — outline | ✅ | ✅ (surface tint) | ✅ | ✅ | — | — | — | — |
| Button — ghost | ✅ | ✅ (tint) | ✅ | ✅ | — | — | — | — |
| Button — destructive | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ confirmation dialog pairing | — | — |
| Button — semantic filled | ✅ | ✅ | ✅ | ✅ | — | — | — | positive / operational |
| Input — text | ✅ | — | ✅ (border + ring) | ✅ | — | ✅ (message + icon) | — | ✅ helper, long content |
| Input — search | ✅ | — | ✅ | — | ✅ (trailing spinner) | — | — | ✅ clear button |
| Input — select | ✅ | ✅ (panel open) | ✅ | — | — | — | ✅ (option row) | ✅ chevron |
| Input — amount | ✅ | — | ✅ | — | — | ✅ (invalid) | — | ✅ live grouping, LTR |
| Input — multiline | ✅ | — | ✅ | ✅ | — | ✅ | — | ✅ grows |
| Chip | ✅ | ✅ | ✅ | ✅ | — | — | ✅ (one max) | ✅ scroll row |
| Tag | ✅ | — | — | — | — | — | — | static |
| Segmented (pill) | ✅ | ✅ (thumb slides) | ✅ | ✅ (whole) | — | — | ✅ (one) | ✅ badge counts |
| Segmented (underline) | ✅ | ✅ | ✅ | ✅ | — | — | ✅ (one) | — |
| Badge | ✅ | — | — | — | — | — | — | 7 pairings |
| Card / KPI | ✅ | — | — | — | ✅ (skeleton) | — | — | ✅ featured ivory |
| Row | ✅ | ✅ (press tint) | ✅ | — | — | ✅ (error row variant) | — | ✅ alternate, long title |
| Top bar | ✅ | — | ✅ (actions) | — | — | — | — | ✅ scrolled E2 state |
| Bottom nav | ✅ | ✅ (pill) | ✅ (ring) | — | — | — | ✅ (one destination) | ✅ 5 items |
| FAB | ✅ | ✅ | ✅ | — | — | — | — | opens sheet |
| Sheet | ✅ (closed→) | ✅ open + expanded snap | ✅ (trap) | — | — | ✅ destructive row | — | ✅ drag handle |
| Dialog | ✅ | ✅ (confirm) | ✅ (trap) | — | — | ✅ destructive confirm | — | — |
| Menu / dropdown | ✅ | ✅ (open panel) | ✅ | — | — | — | ✅ (option) | — |
| Snackbar | ✅ (trigger) | ✅ (action) | ✅ | — | — | ✅ (error variant) | — | ✅ undo, auto-dismiss |
| Empty state | ✅ | — | ✅ (action) | — | — | — | — | icon tile + action |
| Skeleton | ✅ | — | — | — | ✅ (pulse) | — | — | static under reduced motion |
| Error / retry | ✅ | ✅ (retry) | ✅ | — | ✅ (retrying) | ✅ | — | no-results variant |
| Icon | ✅ | — | — | — | — | — | — | ✅ RTL mirror pair |

## Loading semantics

Button loading disables activation for the entire request (no double submits). Content loading is always skeletons — 12px-radius `recessed` blocks pulsing 1.5s (opacity 1↔0.5), static under reduced motion, laid out in the shape of the content they replace. Spinners exist only inside buttons and search fields, never as page-level loaders.

## Selection semantics

One selected element per group: one chip, one segment, one nav destination, one dropdown option. Selection is always visible without motion and without color alone (fill + weight, check glyph, underline, or pill position).

## Error semantics

Errors always pair the negative ramp with an icon and explanatory text at 12px minimum; they never block retry, and destructive confirmations always precede irreversible actions or offer undo.

## Disabled semantics

Disabled means inert: `#B7B2A6` surface, no shadow, no press, no focus, cursor suppressed, and exempt from contrast requirements — but it must still be visually distinguishable from selected states (selected is saturated and carries weight; disabled is flat and grey-warm).
