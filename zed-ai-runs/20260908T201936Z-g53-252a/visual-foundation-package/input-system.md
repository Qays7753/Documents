# Input System

## Anatomy

Label (13px / 500 / ink-secondary, 8px above) → field → helper or error message (12px, 4px below). The field: 48px min-height, white surface, 1px `border-soft` border, 12px radius, 12px padding, `card-title` type, placeholder `disabled #B7B2A6` (raw SOP §7.2). All geometry rem-based for large-text growth.

## Field variants

| Variant | Contract |
|---|---|
| **Text** | the base field above; icon slot leading/trailing (20px, ink-secondary) |
| **Search** | same geometry, leading search icon, trailing clear (44px hit area, 20px close glyph), `type="search"`; in the header it lives as the icon-expand pattern (44px round button expands into the field, collapses on empty-blur) |
| **Select** | closed state looks like a text field + trailing chevron-down showing the current value; opens a 12px-radius E2 panel of 44px options; the selected option is `accent.600` text + check icon + `accent.50` background (raw SOP §7.4) |
| **Amount** | 24px/700 mono tabular, centered, `dir="ltr"`, `inputMode="decimal"`, live thousands grouping while typing, placeholder `0`, no currency symbols, rejects invalid input visibly (error state) |
| **Multiline (textarea)** | base field, content-driven height, 1.6 line height, 16px internal padding, resize suppressed on mobile |

## States

| State | Contract |
|---|---|
| Default | 1px `border-soft` |
| Focused | border `accent.500 #079FA0` (150ms color transition) **plus** the unified `:focus-visible` ring (2px accent.600, offset 2) — the border-only focus is corrected (D-07) |
| Error | border `negative.500`, message below in `negative.600` 12px with alert-triangle icon 16px→20px; never color alone — icon + text always |
| Disabled | `recessed` field fill, `disabled` text and border, no focus, cursor suppressed |
| Read-only | surface fill, ink text, no border color change on focus, dashed underline optional |
| Long content | fields scroll horizontally internally or wrap (textarea); never truncate mid-word in labels |
| Loading (search) | trailing spinner replaces clear icon during query execution |

## Label and message rules

Labels sit above the field, 8px gap, never inside as floating placeholders (the source's pattern). Helper text is 12px ink-secondary; error text replaces it and is announced (`aria-describedby`). Required fields are marked with the label, not a color-only asterisk. Placeholders are examples, never instructions that disappear.

## Content-driven rules

Fields grow vertically for large text (rem-based height with min-height, not fixed). Arabic labels wrap to two lines gracefully; the 8px label gap and 4px message gap hold. Multiline fields auto-grow in a sheet context rather than scrolling internally where the platform allows.

## RTL/bidi

Labels align to the reading direction; icons swap leading/trailing automatically via logical properties; amount fields force `dir="ltr"` so numerals never reorder; search clear sits on the trailing (logical) side. Error icons lead the message in both directions.

## Gallery demonstrations

Text, search, select (with its open panel state), amount, and multiline fields in default, focused, error, disabled, and long-content states; label + helper + error anatomy; the header icon-expand search pattern in the navigation family.
