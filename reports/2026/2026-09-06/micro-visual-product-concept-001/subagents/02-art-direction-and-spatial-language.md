# 02 — Art Direction & Spatial Language

Delivery: `micro-visual-product-concept-001` · Stage 1 · Sub-agent 2 of 5 · 2026-09-06
Role: art direction, shape, surface, composition. Inputs: brief-fixed constraints (authority 1), Stage 0 intake (`en/00`), lessons (`en/01`). Contrast figures marked ≈ are computed here and flagged for independent re-verification by sub-agent 4.

## 1. Fixed ground (restated for scope only)

- Palette values are immutable. Measured roles: `#cc785c` = atmosphere only (white text ≈3.28:1 — never); `#b4613f` = press states only (≈4.42:1, not a resting pass); `#964e33` = the one high-contrast action ink (white ≈6.07:1) when hierarchy justifies.
- Platform truths: five-seat shell «مشروعي الآن | العمل | سجّل | مالي | أدواتي»; honest unknowns «قيمة غير محددة بعد»; «1,245.50 د.أ»; DD/MM/YYYY; 24-char Arabic button cap; effect-preview before irreversible actions; no Jordanian decorative identity; logo never repeated or shape-ornamented.
- Anti-reference: no card walls, no showcase controls, no generic stat-tile dashboards, no depth without meaning.

**Doctrine D0 — words never sit on mid-tone fills.** Terracotta/teal mid-tones carry icons, bars, spines, and borders — never white text. Words live on canvas, band, or soft tint in ink / `#964e33` / `#057b7c`. Depth is tonal first; shadows exist only at the overlay layer.

## 2. Shared platform constants (hold across all hypotheses)

### 2.1 Spacing rhythm
Base unit **4px**; scale 2 / 4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64.

| Token | 320 | 360 | 390 | 430 |
|---|---|---|---|---|
| Screen gutter | 16 | 16 | 20 | 20 |
| Band inner padding | 12 | 12 | 16 | 16 |
| Section gap | 20 | 20 | 24 | 24 |
| Row horizontal padding | 12 | 12 | 16 | 16 |
| Top chrome / bottom shell | 52 / 64+safe | 52 / 64+safe | 52 / 76 | 52 / 76 |

Min touch target 44×44 everywhere. Motion: 160–220ms ease-out; reduced-motion kills directional digit movement (tap alternative remains, per NumericSurface).

### 2.2 Typography
One stack for all roles: `"IBM Plex Sans Arabic", "Noto Sans Arabic", "Segoe UI", Tahoma, system-ui, sans-serif` — Plex covers Arabic + Latin + Western digits with true tabular figures (`font-variant-numeric: tabular-nums; font-feature-settings:"tnum" 1`); Tahoma preserves Arabic metrics on old Android webviews. Weights {400, 500, 600}; no letter-spacing on Arabic ever; Arabic-Indic digits are not used for amounts (evidence: «1,245.50 د.أ»).

| Role | Size/weight | Line-height | Rules |
|---|---|---|---|
| Hero numeral | 32/600 | 1.2 | tnum, exactly one per screen |
| Section numeral | 22/600 | 1.25 | tnum |
| Row amount | 15/600 | 1.3 | tnum, fixed 88px start-aligned column |
| Row title | 15/500 | 1.55 | no truncation of supplier/customer names <20 chars |
| Body | 15/400 | 1.7 | Arabic body target 1.6–1.8 |
| Meta/caption/chip | 13/500–600 | 1.5 | carries state copy |
| Button | 15/600 | 1.4 | ≤24 chars, height ≥48 |
| Tab bar | 11/600 | 1.3 | five seats, RTL order |

### 2.3 Financial-number composition
- Scale: hero 32 / section 22 / row 15 / badge 13 px, all 600, all tabular. Amounts never wrap; «د.أ» renders at 0.72× size in muted ink, NBSP-glued, placed after the digits in logical order (visually left of them in RTL), never starts a line.
- Grouping: Western digits, `,` thousands, `.` decimals, exactly 2 decimals for JOD («20.00 د.أ»); grouping retained ≥10,000; trailing `.00` kept — precision honesty.
- Deltas: signed tabular 13/600 in semantic ink on soft chips (success `#1f7a4d` on `#e2f2e9`; danger `#b23a31` on `#f7e3e1`); sign required, never color-only; unknown delta renders «قيمة غير محددة بعد» in a 1px dashed chip (ink 24%) — never `0.00`, never `+0.00`.

### 2.4 Neutral tokens (proposed; fixed brand/accent palette untouched)

| Token | Light | Dark | Reasoning |
|---|---|---|---|
| canvas | `#f8f4f0` | `#201b17` | warm paper / warm dark; ink ≈14.5:1 light, ≈13.8:1 dark |
| band | `#ffffff` | `#292420` | reading surface; dark ladder rises with elevation (not inversion) |
| soft slab | `#f4e4db` (fixed) | `#332d27` (fixed brand-soft) | truth-block tint; in dark it doubles as raised slab |
| sunken | `#f3ece6` | `#191512` | inputs/wells, below band |
| hairline | `rgba(43,32,26,.12)` | `rgba(239,230,223,.10)` | warm ink line; solid fallbacks `#e9ded5` / `#3d362f` |
| ink | `#2b201a` | `#efe6df` | terracotta-adjacent brown-black / warm off-white |
| muted | `#6b5d54` (≈5.8:1) | `#b3a69c` (≈7.2:1) | secondary text, both pass AA |
| success | `#1f7a4d` / `#e2f2e9` | `#57b585` | green kept clear of the teal accent hue |
| danger | `#b23a31` / `#f7e3e1` | `#e0796f` | redder than terracotta — never collides with brand |
| warning | `#a86a12` / `#f9eedb` | `#d9a44a` | warm amber |
| scrim | `rgba(43,32,26,.44)` | `rgba(0,0,0,.55)` | overlays |

Dark-token notes: accent-text `#8fd5d6` ≈8.2:1 and brand-primary `#d59172` ≈5.2:1 on `#332d27` — both serve as ink/spine in dark; neither is ever a white-text fill.

### 2.5 Elevation, depth, grouping
- **E0 «صفحة / page»** — canvas + bands, zero shadow.
- **E1 «لوح / plate»** — soft-tint slab, zero shadow; tone does the work.
- **E2 «ورقة / sheet»** — bottom sheets, effect-preview boxes, menus: `0 8px 28px rgba(43,32,26,0.20)` light / `0 8px 28px rgba(0,0,0,0.50)` dark; 20px top corners. Shadows exist nowhere else.
- **Card decision rule:** a card exists only for an object with a name («طلب #٤١٢»), ≥2 owner actions, and a lifecycle state; otherwise it is a band row. Max 2 cards per viewport.
- **Logo-to-principle translation (shared):** terracotta appears only as structure — a start-edge spine on the single truth block, brand-soft tints behind financial position, the active-seat underline, and icon ink `#964e33` on soft plates. Never fills under white text, never logo-shaped ornaments. Craft = concentric nested corners + hairline discipline; warmth = warm neutrals; reliability = one rigid vertical money column.

## 3. Hypotheses

### H1 — «السجل الدافئ» / The Warm Ledger
Thesis: the screen is one continuous ledger; truth blocks are full-width bands; money owns a column; terracotta is a spine.

| Axis | Rule |
|---|---|
| Radius | scale 4 / 8 / 12 (band) / 16; chips pill. Nesting: `R_child = max(4, R_parent − 4)` |
| Hairline | 1px at .12 inside bands, .08 between bands; borders replace shadows at E0/E1 |
| Surfaces | canvas `#f8f4f0`; bands `#ffffff` edge-to-edge; hero truth block `#f4e4db` (E1); sunken `#f3ece6`; no shadows below E2 |
| Grouping | full-width bands, one per owner question (position → what changed → who owes → today); band header 34px; list row 52px |
| Density | at 390×844 (716px content): hero 128 + 3 headers 102 + padding ≈ 8 rows above fold. Hard cap: **1 hero + 3 bands**; band ≤6 rows |
| Type deltas | default roles (§2.2); hero block: outer R20, padding 8, inner plates R12 (concentric) |
| Spine | 3px `#cc785c` on the start (right) edge of the hero block only; 2px active-seat underline; money column 88px with 8% hairline on its left |
| Dark | canvas `#201b17`, band `#292420`, hero `#332d27`, spine `#d59172`, hairline `rgba(239,230,223,.10)` |

### H2 — «الحرفة الهادئة» / Quiet Craft
Thesis: fewer, chunkier slabs with carved concentric corners; atmosphere-forward, deliberately low density.

| Axis | Rule |
|---|---|
| Radius | slabs 20, controls 12, chips pill; concentric nesting `R_child = R_parent − padding` (20−16=4) |
| Surfaces | canvas `#f8f4f0`; slabs `#ffffff` inset 16px; hero slab `#f4e4db`; sunken `#f3ece6`; shadowless except E2 `0 12px 32px rgba(43,32,26,0.20)` |
| Grouping/density | 1 hero + max 2 bands above fold; row 60px; ≈6 rows/viewport; emptiness guard: trailing whitespace >25% → next question band pulls up |
| Type deltas | hero numeral 34/600; body line-height 1.75 |
| Spine | 4px `#cc785c` top keystone on hero slab («sawn edge»); soft icon plates |
| Dark | canvas `#1d1916`; slabs `#292420`; hero `#332d27` with `#d59172` keystone |

### H3 — «التيار المالي» / The Financial Stream
Thesis: every event is a chronological row on a right-edge terracotta rail; composition = time, not containers.

| Axis | Rule |
|---|---|
| Radius | rows square to the rail; containers 10; nesting 10→6 |
| Surfaces | canvas only + sticky day-headers `#f4e4db` (36px); 1px hairline rows; shadowless |
| Rail | 2px `rgba(204,120,92,.35)` on the right edge; 6px node dots: terracotta = money events, `#079fa0` = operational events |
| Density | row 48px; 10–11 rows/viewport; max 1 sticky header visible |
| Type deltas | row title 14/500 lh 1.5; meta 12/500 |
| Dark | canvas `#1e1a16`; day-header `#332d27`; rail `rgba(213,145,114,.35)` |
| Failure mode | «أدواتي» and inventory have no chronology — the stream must fake structure |

### H4 — «المنضدة» / The Counter
Thesis: a persistent brand-soft plateau header holds the financial position while content scrolls beneath.

| Axis | Rule |
|---|---|
| Surfaces | sticky plateau `#f4e4db` 168px; content bands `#ffffff` on canvas; E2 sheet is the only shadow |
| Radius | 16 plateau bottom corners; 8 controls; nesting 16→8 |
| Density | row 52px; 7 rows/viewport; plateau consumes 168+52px of chrome |
| Type deltas | plateau numeral 28/600 |
| Dark | plateau `#332d27`; canvas `#201b17` |
| Failure mode | on 568px-tall devices <50% of viewport remains for content; sticky + RTL safe-area edge cases |

## 4. Comparison

| Criterion | H1 Ledger | H2 Quiet Craft | H3 Stream | H4 Counter |
|---|---|---|---|---|
| Calm-trust | **5** — ledger order is inherently calm | 5 | 3 — stream implies unfinished motion | 4 |
| Differentiation | 4 | 4 | **5** — time-composition rare in finance | 3 |
| Operational density | **5** | 2 — starves «سجّل»/«مالي» lists | 5 | 3 |
| RTL fit | **5** — spine + money column on start edge | 4 | 4 — rail right is natural, nodes clutter | 3 |
| 320px resilience | **5** — bands reflow, no double gutters | 3 — inset slabs lose 32px+padding | 4 | 2 |
| CSS implementability | **5** — `border-inline-start`, no sticky tricks | 5 | 4 — sticky headers + rail alignment | 3 |

## 5. Recommendation

**Adopt H1 «السجل الدافئ» / The Warm Ledger** as the Micro visual language, borrowing exactly two elements: H2's concentric corner rule for the hero truth block (outer R20, padding 8, inner plates R12) and H3's node-dot vocabulary inside the «عمل» timeline screen only.

**Decisive reason:** H1 is the only hypothesis whose composition *is* the product's mental model — the owner reads her business top-to-bottom like a ledger — so calm-trust and operational density stop being a trade-off; every rival buys one at the other's expense.

| Risk | Mitigation |
|---|---|
| Band sameness → generic settings-list feel | tonal trio (canvas/band/soft) + terracotta spine on hero only + rigid money column; band headers carry question copy, not labels |
| 1px hairline rendering across DPRs | rgba hairline with solid fallback `#e9ded5`; 0.5dp floor; sub-agent 4 verifies |
| Density creep → crowding | hard caps: 1 hero + 3 bands, band ≤6 rows, row ≥52px; honors finance density cap precedent (257) |
| Dark warm surfaces muddying | luminance ladder `#201b17` < `#292420` < `#332d27`; ink tokens verified ≥5:1; teal text tokens used only as ink |
| `9,999,999.99` at 320px | money column min 88px, tnum, NBSP-glued «د.أ»; overflow uses grouped short form with full value on tap |

## 6. Handoff notes to sibling sub-agents

- **Sub-agent 3 (components):** §2 constants + the winning H1 rules in §3 are the component substrate; effect-preview boxes are E2 sheets; five-seat shell keeps the 2px active-seat underline.
- **Sub-agent 4 (color audit):** re-verify the ≈ figures — `#964e33` on `#f4e4db` ≈4.9, `#057b7c` on `#e3f5f5` ≈4.5, `#d59172` on `#332d27` ≈5.2, `#8fd5d6` on `#332d27` ≈8.2.
- **Sub-agent 5 (anti-reference audit):** test H1 screens against the §1 avoid-list (card wall, showcase controls, generic tiles, meaningless depth) before synthesis.
