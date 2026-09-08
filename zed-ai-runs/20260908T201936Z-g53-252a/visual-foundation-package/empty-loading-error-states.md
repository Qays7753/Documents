# Empty, Loading, and Error States

Every screen ships four mandatory states (raw SOP §8.1): empty, loading (skeletons — never spinners), error/validation, and success. This package adds the two distinguishers the source demands (raw SOP §8.4): **no search results ≠ no data**, plus offline/first-use variants specified but marked product-dependent.

## Empty state (inherited from `EmptyState.jsx`)

| Part | Contract |
|---|---|
| Icon tile | 64×64, 16px radius, `recessed` fill, 24px `ink-secondary` glyph (stroke 1.5) |
| Title | `card-title` 15px/600 ink, one line |
| Body | `body` 15px/1.6 `ink-secondary`, max-width 280px, centered |
| Action | compact primary button (40px, 20px padding) — verb-first ("Add record", "Try again") |
| Layout | centered block, 48px vertical breathing, 16px side padding, `role="status"` |

Copy is neutral and guiding ("Nothing here yet" + "Records you add will appear here"), never apologetic filler. The icon tile uses the neutral recessed surface — semantic colors do not appear in empty states.

## Skeleton loading (inherited)

`recessed` blocks, 12px radius, 1.5s opacity pulse (1↔0.5), laid out in the exact shape of the awaited content: card-shaped blocks for cards, row-shaped strips (44px tile + two lines + trailing amount block) for lists, and full-width title bars for headers. Under reduced motion the skeleton is static. Skeletons never carry text or icons; they are shape promises, and their geometry must match the real content or the load will shift layout (prohibited).

## Error and retry

Two layers: **field errors** (inline, below the field — `negative.500` border + alert icon + 12px message; correctable in place) and **surface errors** (panel-level: a white card with an alert-triangle icon tile in `negative.50`, a title, one explanatory line, and a retry button; retry enters loading with the double-submit guard). Errors never blame the user and always offer the next action. Full-screen failure states use the empty-state geometry with the negative tint on the icon tile.

## Success and completion

Quiet by default: the trigger shows the check-circle completion state (800ms) and a snackbar confirms ("Saved" / "Deleted" + Undo where reversible). There is no confetti, no modal celebration, no full-screen success page — energy comes from hierarchy, not fanfare.

## No-results vs no-data

Two distinct empties: **no data** (nothing exists yet — icon tile + "Add" action) and **no search/filter results** (data exists but the query matched nothing — search icon tile + "Clear filters" action). Rendering the same state for both is a contract violation (raw SOP §8.4).

## First-use and offline (specified, product-dependent)

First-use: empty state + one elevated getting-started card (recessed tile, three-step list, single primary action). Offline: a banner-level info chip (accent pair) rather than a blocking screen, appearing and disappearing with connectivity — geometry specified, behavior documented as the receiver's concern.

## Content-driven edge behavior

Long names line-clamp (never mid-word truncation) · zero, negative, and very large numbers all render with signs · single item vs hundreds (skeleton → rows + incremental loading) · text overflow degrades to ellipsis with full value accessible on tap.

## Gallery demonstrations

Empty (with action), skeleton card + skeleton list, error panel with retry (live loading state on retry), success completion on the button family, and the no-results variant — all in both directions.
