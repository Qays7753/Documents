# Data Display System

## Content row (inherited anatomy)

The workhorse of data screens, content-driven with a 56px minimum (grows for Arabic/large text):

| Part | Contract |
|---|---|
| Leading icon tile | 44×44, 12px radius, semantic 50-step tint background, 20px semantic-600 icon (stroke 2) |
| Title | `card-title` 15px/600 ink, single line with truncation (line-clamp preferred over mid-word cuts) |
| Secondary line | 12px `ink-secondary` — dates/times in mono (`tnum`) |
| Type tag | semantic badge (tint + 600-step text + optional icon) |
| Trailing amount | mono `text.amount` 15px/600 in the semantic ink color with explicit `+`/`−` sign, end-aligned, bidi-isolated |
| Separators | 1px `border-soft` between rows; alternate rows on canvas tint |
| Padding | 16px; icon-text gap 12px |

Semantic mapping (raw SOP §1): positive = incoming, negative = outgoing/loss, operational = neutral administrative state, gold = rare return/highlight. Signs and icons always accompany color (raw SOP §0.7): arrow-down-left + `+` for positive, arrow-up-right + `−` for negative, bank glyph for operational, trending-up for gold.

## KPI surfaces

Two inherited patterns. The **KPI card** (white, E1): 13px/500 secondary label, 24px/600 mono number in a state color, 12px change line with trend glyph ("▲ 12% vs yesterday"). The **featured value card** (recessed ivory, E1): 28px/700 mono hero number with 13px label and optional grouped white inner tiles (12px radius, 16px padding, 34px icon chips). Numbers use the state's 600-step color on white; the change line carries both a glyph and a sign, never color alone.

## Status badges

Pill (full radius), 4px/12px padding, 12px/600 text — the geometry unified from four conflicting source recipes (D-16). Pairs (background / text): progress `gold.50` / `gold.700` (corrected 6.80:1) · ready `accent.50` / `accent.600` (4.51:1) · closed `recessed` / `ink-secondary` (4.64:1) · semantic badges use their family 50-tint + 600-step text. Icons: a 12px glyph or 6px dot may lead where space allows — the non-color cue (normalized; source badges were text-only).

## Chips, tags, and filters

Chips: 36px, full radius, 12px horizontal padding, `label` 13px type, horizontally scrollable row with 8px gaps, **one active chip maximum** per group (raw SOP §7.3). Unselected: white + 1px `divider` border + `ink-secondary` text (500). Selected: `primary.700` fill + white text (600), **no border** (D-09 removes the source's redundant 1px border). Hit area padded to 44px.

Tags are read-only 12px/600 semantic pills (4px/12px padding) carrying state meaning, not interaction.

## Number formatting (inherited, enforced)

Amounts are digits only — **no currency symbols** (the source mockup's "850.000 د.أ" is the documented violation, D-22) · thousands separator `,` · minus is `−` (U+2212), plus is `+`, in the state color · dates `DD/MM/YYYY`, times `HH:MM` 24h · mono tabular, end-aligned, bidi-isolated inside Arabic text · never below 12px.

## Edge cases (raw SOP §8.4)

Zero, negative, and very large values all render (huge numbers shrink via the mono scale, never truncate the sign) · one item versus hundreds (rows + numbering/incremental loading documented) · long names use line-clamp, never mid-word truncation · overflow degrades to ellipsis + full value on tap · "no search results" is a distinct empty state from "no data".

## Charts (future-facing, inherited guidance only)

Not part of this package's component set; the source's chart rules are preserved as constraints for whoever builds them: colors from the semantic ramps only (terracotta, teal, steel, gold, green — 5–6 distinct, colorblind-safe, gray-distinguishable), light `border-soft` grid, thin axes, direct labels, no 3D, mono tabular tooltips, empty/loading states required.

## Gallery demonstrations

Rows in all four semantic states with alternating separators; KPI card and featured ivory card; the complete badge set (progress/ready/closed + four semantic); chip row with one selected; a mixed-content composition showing hierarchy restraint (max two semantic families per view).
