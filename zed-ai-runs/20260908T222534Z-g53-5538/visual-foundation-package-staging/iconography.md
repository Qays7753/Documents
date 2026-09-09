# Iconography

## Style

One icon style, inherited without modification from `reference-components/ui/Icon.jsx`: outlined 24×24 viewBox SVGs, `stroke="currentColor"`, round line caps and joins, default stroke width **1.8**. Usages range from 1.5 (quiet large glyphs: empty-state tile, FAB plus) through 2 (row and chip icons) to 2.2–2.4 (dense 12px badge dots and menu checks). The legal range is **1.5–2.5**; thicker reads as a different style, thinner fails contrast at small sizes.

There are no filled icon variants except the documented navigation pattern: the active bottom-nav item swaps its outline glyph for a filled one (raw SOP §6; D-15). Filled icons are otherwise prohibited; the outline family is the single visual language. No emoji, no arbitrary Unicode symbols, no icon fonts, no remote sprite — the gallery inlines every glyph (Repair F).

## Sizes

| Token | Size | Use |
|---|---|---|
| `icon.sm` | 20px | in-row icons, header action glyphs, input trailing icons, button icon slots |
| `icon.md` | 24px | navigation, FAB, empty-state tile, sheet headers, rail chips |

16px appears once in the source (search clear) and is deprecated — 20px is the floor. Icons inherit text color (`currentColor`) so state changes propagate automatically.

## The operational registry (Repair F)

The sprite carries **43 glyphs**: 34 verbatim from the source's 51-name set plus 9 additions composed in the same grammar. The run's required operational coverage, with the mirror decision recorded per glyph:

| Operation | Glyph | Source | Mirror in RTL |
|---|---|---|---|
| add sale | `pos` (point-of-sale pad) | source (`Icon.jsx:199`) | static |
| collect receivable | `arrow-down-left` | source (قبض, `:211`) | **mirrors** |
| add expense | `arrow-up-right` | source (صرف, `:215`) | **mirrors** |
| add purchase | `bag` (shopping bag) | proposed grammar | static |
| withdrawal | `user-minus` / `bank` | source (`:73`, `:196`) | static |
| invoice | `receipt` | source | static |
| inventory / materials | `inventory` (box) | source (`:184`) | static |
| supplier | `user-minus` / `storefront` | source | static |
| delivery | `truck` | proposed grammar | **mirrors** (forward-facing vehicle) |
| customer | `user` | source (`:148`) | static |
| payment | `wallet` | source (`:61`) | static |
| return | `return` (uturn arrow) | proposed grammar | **mirrors** |
| search | `search` | source | static |
| filter | `filter` | source (`:155`) | static |
| sort | `sort` (lines + arrow) | proposed grammar | static |
| confirm | `check` / `check-circle` | source | static |
| error | `alert` (triangle) | source (`:139`) | static |
| loading | CSS spinner (no glyph) | — | — |
| close | `close` | source | static |
| back / forward / more | `chevron-left` / `chevron-right` / `chevron-down` | source (`:92-101`) | left/right **mirror**; down static |

The four "proposed grammar" glyphs (bag, truck, return, sort) have no source precedent; they are drawn with the source's stroke/cap/join grammar and flagged **proposed** in the registry — a receiving team may substitute source-library equivalents without breaking any contract. The remaining 19 sprite glyphs (home, gear, calendar, list, clipboard, edit, trash, download, upload, lock, eye, bell, info, document, tag, share, trending-up, clock, chart) cover general navigation, feedback, and data states and are all static except `share` (directional arc, mirrors).

The gallery grid labels every glyph with its name and mirror flag, so the registry is visible — not just documented. Row-level usage renders at 20px; grid display at 24px.

## RTL mirroring rules

Mirroring is **selective, never global** (SOP §13). The rule set, derived from the source's own chevron semantics (`Icon.jsx:91–98, 174–177`):

| Icon class | Mirror in RTL? | Members |
|---|---|---|
| Directional chevrons/arrows | **yes** | chevron-left/right, back, forward, row chevrons, arrow-up-right, arrow-down-left, return |
| Forward-facing objects | **yes** | truck (delivery) |
| Directional arcs | **yes** | share |
| Progress/media | no | download, upload, clock, calendar |
| Symmetric/objects | no | home, wallet, receipt, gear, search, plus, close, check, trash, lock, eye, bell, info, pos, bag, inventory, user, bank, storefront, tag, sort, document, chart |

Semantics note from the source: `chevronLeft` is labeled "in RTL = forward" and the `back` icon is the chevron-right shape — in RTL the back affordance points right, in LTR left. Micro-glyphs inside 12px badge dots pair with text labels and do not mirror (the text carries direction). Mirroring applies via the `mirror` class on directional uses — the gallery grid flags them and the row chevrons mirror automatically.

## Placement and alignment

Icons sit in 44px round or 12px-radius square containers when used as standalone actions (header actions, sheet close, FAB); in rows they lead inside a 44×44 tinted tile; in the rail they sit in 48px white chips inside tinted cards; next to text they keep a 4–8px gap and align to the text's optical center. Every icon-only control carries an `aria-label`. Icon color follows the surrounding text role: `ink-secondary` for quiet affordances, semantic 600-steps for state icons, white on filled identity surfaces.

## Prohibitions

No emoji as UI iconography (raw SOP §0.5) · no mixed icon libraries · no filled icons outside active navigation · no sub-20px icons · no two-tone or gradient strokes · no glyphs below the 3:1 non-text contrast minimum (gold icons only on white/canvas where `#B08532` measures 3.36:1 — never on its own tint).
