# Button System

## Hierarchy

Exactly one filled identity action per viewport leads the screen; every other action steps down in emphasis (SOP §10). The ladder, with the source's five variants plus the loading, completion, and semantic-filled states:

| Variant | Fill | Text | Border | Emphasis |
|---|---|---|---|---|
| **Primary** | `primary.700 #964E33` | white (6.11) | none | highest — one per viewport |
| **Secondary** | `accent.600 #057B7C` | white (5.08) | none | high — cool-accent actions |
| **Outline** | surface `#FFFFFF` | ink `#1F1E1D` | 1px `divider #DAD5C8` | medium |
| **Ghost** | transparent | `accent.600 #057B7C` | none | low — text actions in context |
| **Destructive** | `negative.500 #C9322A` | white (5.29) | none | reserved for destructive intent |
| **Positive / Operational filled** | `positive.500` / `operational.600` | white (5.02 / 7.01) | none | semantic quick-actions |
| Disabled | `disabled #B7B2A6` | white | none | inactive, no shadow, no press |

The primary and secondary fills are the package's two headline contrast corrections (D-01/D-02): the source paired white with `primary.500` (3.28:1) and `accent.500` (3.24:1); the SOP's own "deep terracotta for text-bearing actions" role supplies the passing steps — same ramps, same identity, one step deeper. The `primary.500` identity color remains fully in use for non-text graphics (brand marks, icons, selected glyphs, theme-color).

## Geometry

48px min-height · 12px radius · 600 weight · horizontal padding 24px (compact 20px) · full-width variants span the screen minus margins (16px each side) · icon+label gap 8px · icon 20px. Everything is rem-based so large-text mode grows the control with its label.

## States

| State | Contract |
|---|---|
| Default | per variant table |
| Pressed | scale 0.97 (120ms) **and** one step deeper fill: primary 700→800, accent 600→700, others darken one ramp step |
| Focused | 2px `accent.600` ring, 2px offset (unified system ring) |
| Disabled | `disabled` fill + white text + no shadow + `cursor: not-allowed`; press suppressed; WCAG-exempt contrast |
| Loading | spinner (20px, 2px stroke, currentColor) replaces the icon slot, label persists, control disabled — prevents duplicate activation (double-submit guard) |
| Quiet completion | check-circle glyph + positive-tint feedback for 800ms, then reset (color-only under reduced motion) |

Disabled is the SOP's explicit recipe (`#B7B2A6` + white, raw SOP §7.1) — the rendered references' `opacity-50` shortcut is deprecated (D-10). Destructive actions inside sheets use `negative.600` text on surface (quiet destructive row) rather than a filled button, per raw SOP §7.5.

## Content rules

Verb-first labels ("Save", "Confirm", "Try again") · sentence case · never a button without an action · destructive buttons require explicit confirmation or undo snackbar · icon-only buttons (44px round) carry `aria-label` · the label never truncates — controls are content-driven. One filled primary per viewport is a hard rule: two equal filled buttons in one view is a defect.

## Gallery demonstrations

All variants in default, pressed (toggleable via touch/active), focused, disabled, loading, and quiet-completion states; full-width and compact widths; icon+label combinations; the double-submit guard demonstrated on the loading example; all rendered in LTR and RTL.
