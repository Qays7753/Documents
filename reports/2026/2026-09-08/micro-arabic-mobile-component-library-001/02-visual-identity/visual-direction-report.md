# Visual Direction Report — «دفء الطابون» · Taboun Warmth

- Run: `20260908T133450Z-16d11` · Agent 02 (Visual Identity) · Task `2-b`
- Companion artifacts: `color-role-map.md` (full token audit), `type-and-spacing-review.md` (type/geometry audit), `visual-swatch-board.html` (visual reference board).
- Scope: ONE direction for the Arabic-first Micro mobile component library. Not a menu of concepts.

---

## 1. Name and character statement

The direction is called **«دفء الطابون» — Taboun Warmth**, after the working clay oven of a Jordanian bakery: the thing that makes أبو محمد's shop warm is not decoration — it is heat that is doing real work.

**Character statement, measured against the neutral comfort benchmark in SPEC §5:** Taboun Warmth is the visual temperature of a working bakery at six in the morning — warm, composed, and already busy. It keeps every comfort the benchmark promises: three comfortable surfaces, meaningful density, strong hierarchy, calm spacing, restrained elevation, a lived-in and trustworthy feel — and it adds the useful heat the benchmark permits but does not spell out. The terracotta `brand-atmosphere` is the fired-clay wall of the oven, visible exactly once per viewport. The semantic green and red are the chalk marks of money actually moving — received on one line, paid on the next — and amber is the shelf threshold that cannot wait. The 32px tabular value is the first thing the owner sees, before any container, before any color. It is warm without becoming a beige monochrome, energetic without becoming noisy, confident because every non-neutral color is an operational fact, and direct because hierarchy is built from size, spacing, and signs before it is ever built from color.

## 2. Warmth from three surfaces and the ink system — no fourth surface

Warmth in this direction is carried by *deltas*, not by painted planes. The three permitted surfaces move in one warm direction only:

- `canvas #FAF9F5` — the room wall: white pushed a few percent toward cream, so the app never reads cold-blue-white.
- `surface #FFFFFF` — the clean counter: pure white cards and grouped surfaces float one warm step above the canvas.
- `sunken #F0EEE6` — the inset board: a flour-warm recess for input fills, chart plot areas, and compact metadata wells inside a surface.

The ink family completes the temperature: `ink-strong #1F1E1D` is a warm near-black (never a blue-black), `ink-muted #6E6A60` and `ink-subtle #767265` are warm greys, and the structure lines `line-soft #EAE6DC` / `line-strong #DED9CB` are beige hairlines, not grey rules. Warmth is therefore ambient — the room is warm — which leaves the *content* free to be the loud thing.

**No fourth surface exists.** `brand-tint #F7EAE4` is not a surface: it appears only as the single tinted QuickActionRail tile. Semantic tints (`positive-tint`, `danger-tint`, `warning-tint`, `info-tint`) are message skins for small chips and state segments — a positive chip is a *sentence about money*, not a place. Nesting is strictly `canvas → surface → sunken` (the permitted two nested levels); `sunken` never contains `sunken`. The `PrimaryValueBlock` sits directly on the canvas — bigger, not boxed — which is precisely why the system never needs another plane to create hierarchy.

## 3. Useful energy — where the life comes from

Energy is budgeted, and every source maps to an operational meaning:

1. **One brand moment per viewport.** The single filled brand-family element is the primary CTA (`brand-ink #964E33` fill, `on-brand` white text, 6.11:1) — e.g. «تسجيل دفعة». Where a composition has no CTA, the brand moment may instead be one `brand-atmosphere` graphic block in an empty state with `ink-strong` text (5.08:1). Never both; never a second fill.
2. **The tinted rail tile.** The first QuickActionRail tile (inline-start, rightmost in RTL) carries `brand-tint` with a `brand-ink` icon (5.21:1 on tint) and `ink-strong` label — the only tinted tile; all other tiles are `surface`.
3. **The positive/danger pair in metrics.** One MetricGroup may color at most two numerical values — one received (+) and one paid (−): `+ 1,284.50` in positive green next to `− 65.00` in danger red. That pair *is* the day's cash story; every other MetricRow value stays `ink-strong`. Sign first, color second (SPEC §6.12).
4. **Tinted state chips.** Small semantic-tint chips with `ink`/`ink-strong` text and a semantic-colored icon + sign: «قبض + 385.00 د.أ» on `positive-tint`, «فاتورة مستحقة» on `warning-tint`, «قيد التسوية» on `info-tint`. Chips carry real Micro copy (مطعم النخيل، مؤسسة الشرق للتجهيزات، شركة التوصيل السريع) — never isolated swatches.

**Color-economy compliance (every SPEC §6.3 rule):**

| Rule | How this direction obeys |
|---|---|
| Max one filled brand-family surface/action per viewport | The CTA (or the empty-state atmosphere block) is the only fill; everything else is surface/canvas. |
| Max two semantic families per composition | The cash pair is positive+danger; exceptions use warning alone; settlement contexts use info alone. Never three families together. |
| Max two colored numerical values | The +/− pair only; all other numbers are ink-strong. |
| Max one tinted QuickActionRail tile | First tile only, brand-ink icon + ink-strong label. |
| Max three visible dividers | Spacing-first: metric rows separate by padding; the three-divider budget goes to header→content, group→list, and inside-list only when spacing cannot do the work. |
| Max two nested surface levels | canvas → surface → sunken only. |
| Full palette across the library, not per composition | All four families appear across the library's components; each composition stays within its budget. |
| Never color an entire card for liveliness | Semantic color lives only on chips, icons, signs, and the two metric values. (A colored start-edge stripe on rows was considered and rejected as decoration-adjacent.) |

## 4. Hierarchy tactics

- **Value first.** Reading order per block: qualifier/label (15px `ink-muted`) → **32px/600/1.15 `ink-strong` value** (tabular-nums lining-nums) → 13px `ink-subtle` qualifier (party, date, doc). The value is the fixation target; it never competes with a card border.
- **Tabular digits everywhere numbers repeat.** `font-variant-numeric: tabular-nums lining-nums` on values, metric rows, chart labels: `1,284.50`, `385.00`, `−65.00` share a ones-column and decimal rail, so Abu Mohammad's eye can scan a column of numbers like a counter tally.
- **Sign-first financial direction.** The +/− sign lives inside the LTR isolate, before the digits; it is never dropped when a value is colored. Unavailable/unknown shows an em-dash plus a label — never `0` (SPEC §6.12).
- **Order of escalation:** size → weight → surface → ink color → semantic color. Semantic color amplifies meaning already carried by sign, label, or icon.
- **Currency.** «د.أ» is a separate Arabic text node beside the isolated number (never inside the isolate), so bidi, shaping, and wrapping stay correct; it may be omitted when context is unambiguous.

## 5. Density and calm spacing

Meaningful density: MetricRows and OperationalRows hold 44–52px content heights (44px touch minimum), 12px internal rhythm, 16px screen edge at all widths. Calm comes from the larger steps: 24px between sibling groups, 32px of air above the PrimaryValueBlock so it reads as the headline of the composition — hierarchy by *air*, not by borders. The spacing scale does the divider work so the ≤3 hairlines stay rare and therefore meaningful. Cards are flat (no shadow); only overlay chrome (Sheet, Dialog) earns a scrim and a soft shadow; inset meaning is carried by `sunken`, never by an embossed shadow. Long Arabic labels wrap to a second line at 320px — heights are content-driven; amounts and dates never truncate.

## 6. What this explicitly is NOT

- **Not a card gallery:** the primary value lives on canvas with no card; metrics share one surface (no card-per-metric); quick actions are a horizontal rail, not a dashboard grid; operational content repeats as rows with real counterparties (مطعم النخيل، مؤسسة الشرق للتجهيزات، شركة التوصيل السريع), not as tiled KPI cards.
- **Not a dashboard:** no admin-KPI tile rows, no desktop density, no detached top bar, no legend chrome; one column, phone-width, thumb-reach CTA.
- **Not a documentation site:** the swatch board is a separate reference artifact; product surfaces never display raw hex, token names, or implementation notes.
- **Not a quiet beige system:** the warm deltas plus one hot brand moment plus one semantic pair keep the screen alive; "neutral comfort" is the floor, not the ceiling.
- **Not a concept board:** every example is an operational Micro fact — طحين فاخر 10كغ under threshold, a 35.00–1,284.50 د.أ range, DD/MM/YYYY dates, English digits.

## 7. RTL-specific visual decisions

- `dir="rtl"` is primary; all spacing/positioning uses logical properties (`inline-start/end`), so mirroring is structural, never hand-flipped per screen.
- Text aligns to the start (right); numeric values are LTR isolates aligned at the row's inline-end so unit columns align vertically across rows. Chart time axes stay LTR inside the chart with Arabic direct labels (SPEC §6.13).
- Icon mirror registry: back/forward/chevrons/directional arrows mirror; semantic and object icons (check, warning, box, truck) never do; no paper-plane send icon.
- The brand moment is placed for the thumb: the filled CTA is bottom, full-width; the tinted rail tile is first (inline-start); the QuickActionRail scrolls right-to-left with proximity snap and its next-item cue peeks at the inline-end.
- Every numeric string (`1,284.50`, `−65.00`, `12.5%`, `30/09/2026`) is wrapped `<bdi dir="ltr">…</bdi>` with «د.أ» as a sibling Arabic node — direction, sign placement, and thousands separators stay deterministic at any zoom or scale.

## 8. Contrast findings and risks handed to Agent 05

All primary reading pairs pass 4.5:1 (ink-strong 14.3–16.6:1; ink 11–12.8:1; ink-muted 4.6–5.4:1; brand-ink 5.2–6.1:1; white-on-brand-ink CTA 6.11:1; press states keep ≥6.6:1). Flags (full tables in `color-role-map.md`): `positive` on `positive-tint` is 4.27:1 — icons/graphics and large (≥24px / 18.66px@600) values only, normal chip text uses ink; `ink-subtle` on `sunken` is 4.14:1 — ink-subtle is restricted to surface/canvas; white on `brand-atmosphere` is 3.28:1 — large text/graphics only, normal text uses `ink-strong`; `ink-disabled` (2.11:1) appears only on genuinely disabled controls (WCAG-incidental, plus a non-color cue); structural hairlines and the surface/canvas step are below 3:1 by design — they never carry meaning alone, and focus rings are 2px `ink-strong`. These are constraints of the fixed palette, documented so Agent 05 can synthesize without re-deriving them.
