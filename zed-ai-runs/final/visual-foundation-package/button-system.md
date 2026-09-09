# Button System

## Hierarchy

Exactly one filled identity action per viewport leads the screen; every other action steps down in emphasis (SOP §10). The ladder, with the source's five variants plus the loading, completion, and semantic-filled states:

| Variant | Fill | Text | Border | Emphasis |
|---|---|---|---|---|
| **Primary** | `primary.700 #964E33` | white (6.11) | none | highest — one per viewport |
| **Secondary** | `accent.600 #057B7C` | white (5.08) | none | high — cool-accent actions |
| **Outline** | surface `#FFFFFF` | ink `#1F1E1D` | 1px `divider #DAD5C8` | medium |
| **Ghost** | transparent | `accent.600 #057B7C` | none | low — text actions in context |
| **Destructive** | `negative.600 #B42318` | white (8.24) | none | reserved for destructive intent [corrected R-19] |
| **Positive / Operational filled** | `positive.500` / `operational.600` | white (5.02 / 7.01) | none | semantic quick-actions |
| Disabled | `disabled #B7B2A6` | white | none | inactive, no shadow, no press |

The primary and secondary fills are the package's headline contrast corrections (D-01/D-02): the source paired white with `primary.500` (3.28:1) and `accent.500` (3.24:1); the SOP's own "deep terracotta for text-bearing actions" role supplies the passing steps — same ramps, same identity, one step deeper. The destructive fill moved from the 500 step (`#C9322A`, 5.29) to the 600 step (`#B42318`, 8.24) in the repair run (R-19) — the 600 step is the expense family DEFAULT, the SOP's text/icon step, and the run-pinned "negative main". The 500 step remains a graphic mid-fill for charts and progress arcs.

**`primary.500 #CC785C` is the identity color** — legal and in active use for non-text graphics and **icon-only identity surfaces**: the FAB and the top-bar identity action button (source `Fab.jsx:39 bg-primary`, white glyph at 3.28:1 ≥ 3:1 non-text, R-18). It never carries normal-size white button text.

## Geometry

48px min-height · 12px radius · 600 weight · horizontal padding 24px (compact 20px) · full-width variants span the screen minus margins (16px each side) · icon+label gap 8px · icon slot 20px. Everything is rem-based so text scaling grows the control with its label (48 → 64 at 130% → 108 at 200%).

## The six interaction states (Repair A)

States of **one** button over time — not color variants, not workflow statuses. The gallery shows them together in one strip, labeled, and the loading sample is live (tap twice to feel the guard):

| State | Contract |
|---|---|
| **Default** | per variant table — filled `primary.700`, white text, source geometry |
| **Pressed — hold** | 80ms scale 0.97 **and** one deeper ramp step (primary 700→800; accent 600→700; identity FAB 500→600) — a transient state, never a new permanent terracotta |
| **Focused** | fill unchanged + the dual-ring contract: 2px `accent.600` ring, 2px offset on light surfaces; inset 2px surface ring (−4px) on filled controls — never a background-only change (R-05) |
| **Disabled** | `disabled` fill + white text + no shadow + no press + `cursor: not-allowed`; WCAG-exempt contrast; visually flat and grey-warm, distinct from selected |
| **Loading** | button stays in place; the 20px spinner replaces the leading icon in a fixed slot (zero layout shift); the **label persists** ("Save", not "Saving"); control disabled + `aria-busy` — repeated activation impossible (double-submit guard, raw SOP §8.5; R-24) |
| **Quiet completion** | check glyph + positive-tint feedback for 800ms, then reset (color-only under reduced motion); the snackbar confirms afterwards |

Disabled is the SOP's explicit recipe (`#B7B2A6` + white, raw SOP §7.1). Destructive actions inside sheets use `negative.600` text on surface (quiet destructive row) rather than a filled button, per raw SOP §7.5.

## Content rules

Verb-first labels ("Save", "Confirm", "Try again") · sentence case · never a button without an action · destructive buttons require explicit confirmation or a real undo · icon-only buttons (44px round) carry `aria-label` · the label never truncates — controls are content-driven. One filled primary per viewport is a hard rule: two equal filled buttons in one view is a defect.

## Gallery demonstrations

All variants in default, pressed (hold the sample), focused, disabled, loading, and quiet-completion states; the six-state strip framed as interaction states of one button; the live loading cycle with the duplicate-submit guard; icon+label and icon-only forms; all rendered in LTR and RTL at 100/130/200% text scale.
