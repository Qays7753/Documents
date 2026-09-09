# Data Display System

## Content row (repaired grid, R-10)

The workhorse of data screens, content-driven with a 56px minimum (grows for Arabic and large text). The repair replaced truncation-only titles with a safe wrapping grid:

| Part | Contract |
|---|---|
| Grid | `flex`: leading 44×44 tile (flex-none) · `minmax(0, 1fr)` text column · trailing area (flex-none) — the row stretches the full content width of its parent, never centered by `max-width` |
| Leading icon tile | 44×44, 12px radius, semantic 50-step tint, 20px semantic-600 icon (stroke 2); directional glyphs mirror in RTL |
| Title | `card-title` 15px/600 ink — **wraps and 2-line clamps** (`-webkit-line-clamp: 2`), never nowrap-ellipsis; long Arabic titles wrap safely without pushing the trailing value off-screen |
| Secondary line | 12px `ink-secondary` flex row: optional status tag + mono date/time (`tnum`, bidi-isolated) or wrapped qualifier |
| Status tag | small semantic pill under the title, **inside the row context** — icon + text, never color alone (Repair B) |
| Trailing area | mono amount (explicit sign, end-aligned, bidi-isolated) + optional 44px chevron action |
| Trailing action | 44px hit, 20px chevron mirrored in RTL; fires a 120ms directional nudge + accent tint when the row opens a new context |
| Separators | **one rule**: 1px `border-soft`, inset to the text column start (72px = 16 padding + 44 tile + 12 gap) — applied identically in every list |
| Alternation | zebra rows on canvas tint (inherited source pattern, kept with the inset divider) |
| Padding | 16px; icon-text gap 12px |
| Local changes | removal collapses the row only (200ms); insertion flashes a quiet 600ms positive tint; Undo restores the node (R-13) |

Semantic mapping (raw SOP §1): positive = incoming, negative = outgoing/loss, operational = neutral administrative state, gold = rare return/highlight. Signs and icons always accompany color (raw SOP §0.7): arrow-down-left + `+` for positive, arrow-up-right + `−` for negative, bank glyph for operational, trending-up for gold.

## Metric surfaces (repaired, R-09)

Three patterns, chosen by whether the parts genuinely belong to the total:

1. **Direct primary value** (no genuine comparison): white E1 card — 13px/500 label, 24px/600 mono number, optional 12px change line with trend glyph. Nothing else; no decorative islands.
2. **Summary metric composition** (the parts sum to the total): white E1 card — label + period, 28px/700 mono total, an 8px full-radius **relationship bar** on a recessed track (two segments: operational.600 + positive.500), and exactly two supporting values (icon chip + name + mono value) that visibly sum to the total. Content-driven height, one surface, **no white-card-in-white-card** — grouping comes from the bar and 12px gaps. Below 360px the supporting values stack to one column. When the relationship changes, the bar segments move over 200ms while the numbers land immediately (never a count-up, R-14).
3. **Grouped surface**: label rows with 44px minimum and 1px `border-soft` dividers inside one card — spacing and dividers establish grouping, not nested surfaces.

The retired pattern: the ivory featured card with two white inner tiles — its numbers did not sum to its hero total and its grid clipped at 320px (S2-02/S2-03). The source's "distinguished value card" (ivory + recess) remains legal for a single hero value, but not for fake comparisons.

## Status badges (in context, Repair B)

Pill (full radius), 4px/12px padding (compact 2px/10px in rows), 12px/600 text. Pairs: progress `gold.50`/`gold.700` (6.80:1) · ready `accent.50`/`accent.600` (4.51:1) · closed `recessed`/`ink-secondary` (4.64:1) · semantic families use their 50-tint + 600-step. Every badge leads with a 12px icon or dot — never text-only, never color-only. **Statuses are context, not chrome**: they render inside rows, inside the filter sheet, and inside dialogs; a permanent wall of status pills is the documented anti-pattern (removed, R-22). The complete pairing reference lives in the gallery's evidence panel. The ready/moved tint similarity (1.04:1) is a known, documented limit — mitigated by mandatory distinct icons and text.

## Filtering (Repair C)

One compact Filter control (36px visual/44px hit, icon + label + count badge) in the list header; the small sort dropdown beside it is the single sanctioned compact single-choice control. Tapping Filter opens the staged bottom sheet (see `overlay-system.md`). After Apply, the parent keeps only the active summary line ("In progress · this month") and the count badge; the live list filters (status, type, date range) and re-orders (sort); zero matches swaps the list for the no-results empty state with a Clear-filters action. Status labels (`In progress`, `Ready`, `Closed`, `Received`, `Sent`, `Moved`, `Returned`) live inside rows and inside the sheet — never as the filter control itself.

## Chips

36px visual, 44px hit area (`::after` inset −4px, R-26), full radius, 12px horizontal padding, `label` 13px type. Unselected: white + 1px `divider` border + `ink-secondary`/500. Selected: `primary.700` fill + white/600, **no border** (D-09). Multi-choice groups toggle independently (`aria-pressed`); single-choice groups keep one active (`radiogroup`/`radio`). Chips are selection controls inside sheets, menus, and segmented contexts — never the page-level filter UI.

## Number formatting (inherited, enforced)

Amounts are digits only — **no currency symbols** · thousands separator `,` · minus is `−` (U+2212), plus is `+`, in the state color · dates `DD/MM/YYYY`, times `HH:MM` 24h · mono tabular, end-aligned, bidi-isolated inside Arabic text (`unicode-bidi: isolate` on `.num`, `dir="ltr"` spans) · never below 12px.

## Edge cases (raw SOP §8.4)

Zero, negative, and very large values all render (huge numbers shrink via the mono scale, never truncate the sign) · one item versus hundreds · long names **wrap and 2-line clamp** — mid-word truncation is prohibited (raw SOP §8.4; the original package's nowrap-ellipsis rows were the documented violation, corrected in R-10) · overflow degrades to clamp with the full value accessible on tap · "no search results" is a distinct empty state from "no data" — and the filtering family renders that distinction live.

## Charts (future-facing, inherited guidance only)

Not part of this package's component set; the source's chart rules are preserved as constraints: colors from the semantic ramps only (5–6 distinct, colorblind-safe, gray-distinguishable), light `border-soft` grid, thin axes, direct labels, no 3D, mono tabular tooltips, empty/loading states required.

## Gallery demonstrations

The filterable list (seven rows, live filtering/sorting, staged sheet, count badge, summary, no-results swap); the row grid (short Latin, long wrapping Arabic, wrapped qualifier, trailing chevron actions, bidi amounts); the local-change list (insert/remove/undo); the direct primary value; the summary metric composition with simulate-update; the grouped surface; chips in their sheet and reference contexts.
