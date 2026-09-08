# Iconography

## Style

One icon style, inherited without modification from `reference-components/ui/Icon.jsx`: outlined 24×24 viewBox SVGs, `stroke="currentColor"`, round line caps and joins (`strokeLinecap="round"`, `strokeLinejoin="round"`), default stroke width **1.8**. Usages range from 1.5 (quiet large icons: empty-state glyph, FAB plus, info notes) through 2 (row icons) to 2.5 (dense header actions). The system fixes the legal range at **1.5–2.5**; anything thicker reads as a different style, anything thinner fails contrast at small sizes.

There are no filled icon variants except the documented navigation pattern: the active bottom-nav item swaps its outline glyph for a filled one (raw SOP §6: bottom nav active = color + filled icon; `BottomNav.jsx` renders `item.icon(false)` even when active — a defect corrected in this package, D-15). Filled icons are otherwise prohibited; the outline family is the single visual language.

## Sizes

| Token | Size | Use |
|---|---|---|
| `icon.sm` | 20px | in-row icons, header action glyphs, input trailing icons |
| `icon.md` | 24px | navigation, FAB, empty-state glyph, sheet headers |

16px appears once in the source (search clear button, `PageHeader.jsx:158`) and is deprecated — 20px is the floor for legible iconography. Icons inherit text color (`currentColor`) so state changes propagate automatically.

## The gallery set

The gallery implements 26 icons representative of the source's 51-name set, as an inline SVG sprite (no network, no icon font): plus, home, receipt, clipboard, gear, search, calendar, list, wallet, arrow-down-left, arrow-up-right, trash, edit, close, check, check-circle, chevron-left, chevron-right, chevron-down, share, download, upload, lock, eye, bell, info, alert-triangle. Every glyph is drawn with round caps/joins and the 1.8 default stroke, matching the source paths where reused.

## RTL mirroring rules

Mirroring is **selective, never global** (SOP §13: do not flip every SVG). The rule set, derived from the source's own chevron semantics (`Icon.jsx:91–98, 174–177`):

| Icon class | Mirror in RTL? | Examples |
|---|---|---|
| Directional chevrons/arrows | **yes** | chevron-left/right, back, arrow-up-right, arrow-down-left, share |
| Progress/media | no | download, upload, clock, calendar |
| Symmetric/objects | no | home, wallet, receipt, gear, search, plus, close, check, trash, lock, eye, bell, info |

Semantics note from the source: `chevronLeft` is labeled "in RTL = forward" and the `back` icon is the chevron-right shape — in RTL the back affordance points right, in LTR it points left. The gallery demonstrates both directions with the mirrored set applied.

## Placement and alignment

Icons sit in 44px round or 12px-radius square containers when used as standalone actions (header actions, sheet close, FAB); in rows they lead inside a 44×44 `radius.control` tinted tile; next to text they keep a 4px (`space.1`) gap and align to the text's optical center, never the cap height. Every icon-only control carries an `aria-label`. Icon color follows the surrounding text role: `ink-secondary` for quiet affordances, semantic 600-steps for state icons, white on filled identity surfaces.

## Prohibitions

No emoji as UI iconography (raw SOP §0.5); no mixed icon libraries; no filled icons outside active navigation; no sub-20px icons; no two-tone or gradient strokes; no icons below the 3:1 non-text contrast minimum (gold icons are permitted only on white/canvas where `#B08532` measures 3.36:1 — never on its own tint).
