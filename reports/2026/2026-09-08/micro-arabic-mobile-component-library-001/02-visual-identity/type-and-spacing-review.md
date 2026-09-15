# Type & Spacing Review — «دفء الطابون» · Taboun Warmth

- Run: `20260908T133450Z-16d11` · Agent 02 (Visual Identity) · Task `2-b`
- Audits SPEC §6.4 (typography), §6.5 (spacing/geometry/touch), §6.1 (digits/dates/bidi) and defines implementation rules for Agents 03–05.

## 1. Typeface audit

**Primary: IBM Plex Sans Arabic**, weights **400 / 500 / 600** — chosen by SPEC, confirmed here:

- It is a true Arabic-first family (designed with Arabic as a first-class script, not a Latin face with an Arabic bolt-on), so stroke weight and rhythm feel native at 15px, and the Latin/digit design matches the English digits required for financial values.
- It carries proportional **and tabular lining figures** (`font-feature-settings`/`font-variant-numeric` `tnum`/`lnum`), which this product depends on for column-aligned amounts.
- No display, mono, or decorative face is used anywhere in the product voice (SPEC §6.4). A mono face is allowed only for small technical/audit values in documentation — not used in the swatch board or any product surface.
- Weights map to roles: 400 = labels/qualifiers/body; 500 = medium emphasis (chip labels, rail labels, secondary values, currency node); 600 = the primary value and titles. No 700 — the jump from 400→600 is the emphasis gesture; 500 exists precisely so 600 stays rare and therefore loud.

**Fallback stack (in order):** `IBM Plex Sans Arabic` → `Noto Sans Arabic` → `system-ui, sans-serif`. Rationale: Noto Sans Arabic is metrically close enough at 15px/32px to avoid reflow surprises when the webfont is unavailable (offline first open); the system sans covers the rest. The stack must be declared once as a token (`--font-family`) and never re-declared per component. Fallback metrics were not network-verified in this run (local IBM Plex Sans Arabic was installed by the coordinator for verification screenshots); Agent 03 should confirm final font loading order and `font-display: swap`.

## 2. Type roles

| Role | Spec | px / weight / line-height | Ink (default) | Usage |
|---|---|---|---|---|
| Main numeric value | §6.4 | **32px / 600 / 1.15** | `ink-strong` | PrimaryValueBlock amount; `tabular-nums lining-nums`; LTR isolate |
| Label | §6.4 | **15px / 400 / 1.55** | `ink-muted` (promoted to `ink` when actionable) | Labels above values, row labels, body sentences |
| Qualifier / compact metadata | §6.4 | **13px / 400 / 1.4** | `ink-subtle` (surface/canvas only — see §3) | Dates, party names under values, doc references, rail labels (§6.8) |
| Arabic reading text minimum | §6.4 | **≥14px** | — | All user-facing Arabic prose |

- **Line-height discipline:** 1.15 exists so the 32px value reads as one tight figure; 1.55 lets a long Arabic label (e.g. «تحصيل دين من مطعم النخيل») wrap to two lines at 320px without colliding with the value. Never compress Arabic line-height below 1.3 for multi-line text.
- **Currency node:** «د.أ» is a separate Arabic text node beside the number — recommended **20px / 500 / `ink`** next to a 32px value (0.625rem-scale ratio), omitted entirely when context makes it unambiguous (SPEC §6.1).
- **The 13px vs 14px tension (flag for Agent 05):** SPEC §6.4 sets qualifiers at 13px *and* an Arabic minimum of 14px; SPEC §6.8 sets the QuickActionRail label at 13px. Resolution adopted here: **13px is reserved for (a) compact numeric/Latin metadata (dates, IDs, amounts-in-qualifiers) and (b) the spec-mandated rail labels; all reading Arabic in user-facing UI is ≥14px.** Where a 13px Arabic qualifier is unavoidable, it is single-line, `ink-subtle` on surface/canvas only, and 500 weight if it is a rail label. This is a documented interpretation, not a silent choice.

## 3. Numeric policy (digits, signs, tabular alignment)

- **English digits `0–9` only** in all financial values and dates; dates as `DD/MM/YYYY` (e.g. `30/09/2026`). No Arabic-Indic digits anywhere in values.
- **`font-variant-numeric: tabular-nums lining-nums`** on every numeric context: primary values, MetricRow values, chart labels, sheet totals. Result: `1,284.50`, `385.00`, `−65.00` share a fixed-width digit grid, so ones-units and decimals align vertically across rows (demonstrated in `visual-swatch-board.html` §5).
- **Sign-first direction (SPEC §6.12):** the `+`/`−` sign is placed before the digits *inside the LTR isolate*, so it is the leftmost glyph of the number — the primary financial-direction signal. Color (positive/danger) is always secondary and never replaces the sign. Use ASCII `-` for the minus (tabular-safe in Plex Sans Arabic); do not rely on U+2212 unless the shipped subset is verified.
- **Unknown ≠ zero:** unknown/unavailable shows an em-dash `—` plus a label («غير متوفر» / «بانتظار التسوية»), never `0` and never a faded number.
- **Alignment rule:** in RTL rows, labels start at inline-start (right); the value column is LTR-isolated and column-aligned at inline-end, so the ones-digit rail is a vertical scanning line down the composition.

## 4. rem-based component typography (scaling 100/130/200%)

**Rule: root is exactly 16px; every component text token is `rem`; lab/documentation chrome is `px`.**

```css
html { font-size: 16px; }              /* never scaled by media queries */
/* component text tokens (rem) */
--text-value:     2rem;                /* 32px → 64px at 200% */
--text-label:     0.9375rem;           /* 15px */
--text-qualifier: 0.8125rem;           /* 13px */
--text-currency:  1.25rem;             /* 20px */
/* lab chrome (px) — swatch frames, preview bezels, section rules */
.lab-frame { border-width: 1px; padding: 16px; }
```

Why this split:

- Phone OS/browser **text-size settings** (and Firefox "zoom text only") scale the default root font size, so `rem`-based component text grows: at 130% the 32px value becomes ~41.6px; at 200% it becomes 64px, and the 15px label becomes 30px. Component text therefore honors the user's scale request.
- **Lab chrome stays fixed** so the reference board's frames, strips, and measurement demos do not inflate and destroy the artifact's own geometry when text scale is applied.
- Consequences Agents 03–05 must design for: value + label + currency wrap onto 2–3 lines at 200% (content-driven heights, no fixed or aspect-ratio heights — SPEC §6.5); MetricRow min-height stays a *minimum* (44px) while rows grow; the `ch`-based number columns grow with the font; touch targets never shrink. Minimum readable Arabic at 200% is no concern (everything doubles), at 100% the 14px floor governs.
- Do **not** scale the root with viewport media queries (that would couple text size to device width and fight the user's own setting); `px`-locked component text is forbidden.

## 5. Bidi strategy for values

```html
<!-- full amount: number isolated LTR, currency a separate Arabic node -->
<span class="m-val">
  <span class="num"><bdi dir="ltr">-65.00</bdi></span><span class="cur">د.أ</span>
</span>

<!-- date / percent / identifier -->
<bdi dir="ltr">30/09/2026</bdi>
<bdi dir="ltr">12.5%</bdi>
<bdi dir="ltr">#INV-0384</bdi>
```

- `<bdi dir="ltr">` (or `<span dir="ltr" unicode-bidi="isolate">`) wraps the numeric string only; «د.أ» stays outside as Arabic text so shaping, ordering, and wrapping are correct at any scale.
- In RTL flow the isolated number is placed first (inline-start/right of the value cluster) and the currency node follows (to its left): reading order is «label → number → currency», the natural Arabic convention.
- `.num` gets a fixed `ch`-based `min-width` + right alignment so the ones-digit rail aligns across rows (§3).
- Chart time axes remain LTR inside the chart while their labels are Arabic RTL (SPEC §6.13); mixed strings («منذ 3 أيام», `DD/MM/YYYY`) never mix scripts inside one isolate.

## 6. Spacing scale usage map (`2, 4, 8, 12, 16, 24, 32, 40px`)

| Step | Used for |
|---|---|
| 2 | micro-nudges: icon optical centering, sign-to-digit tracking inside chips |
| 4 | inline icon↔text gaps in qualifiers; checkbox↔label; chip internal vertical padding |
| 8 | MetricRow label↔value breathing; QuickActionRail tile gap; icon-to-label gap (§6.8); adjacent-target minimum gap |
| 12 | chip horizontal padding; compact row internal padding; sheet header padding |
| 16 | **screen edge at all widths** (§6.5); card/surface padding; rail padding; group-to-list separation; touch-target slack around 44px rows |
| 24 | between sibling groups (rail → MetricGroup); section separation inside one surface |
| 32 | air above PrimaryValueBlock (headline moment); before bottom action zone |
| 40 | top-of-screen breathing under the integrated top zone; end-of-list clearance above bottom navigation |

Rules: no off-scale values (no 10/20/28); spacing does hierarchy work so hairlines stay rare (≤3 dividers per composition); 8px minimum gap between adjacent touch targets; 44px minimum target height, 48px for primary actions; heights are content-driven — never fixed or aspect-ratio.

## 7. Radius usage map (`6, 12, 16, 24, full`) + BottomNavigation = 0

| Radius | Components | Why |
|---|---|---|
| 6 | chips, small state badges, checkboxes, segmented-control thumbs | small elements stay crisp; avoids pill-creep |
| 12 | inputs, buttons (incl. primary CTA), CompactTile, QuickActionRail tiles, MetricGroup surfaces | the default "counter object" radius — one step from sharp, clearly not a pill |
| 16 | Dialog, grouped inset wells (sunken blocks) | overlays read one level softer than controls |
| 24 | Sheet top corners, large empty-state blocks | the softest moment belongs to overlays and state moments, never to controls |
| full | Avatar, switch track/thumb, circular icon-only buttons, loading spinner | only truly circular elements |
| **0** | **BottomNavigation** | it is edge-to-edge persistent chrome, not a floating control — it must meet the screen edges and the canvas as architecture (SPEC §6.5/§6.7) |

"Do not make every control a pill": `full` is reserved for genuinely circular elements; no rounded-full buttons, no pill tags.

## 8. Elevation restraint rules

1. **Static surfaces are flat.** Cards, MetricGroups, tiles: fill (`surface`) + at most a `line-soft`/`line-strong` hairline. No shadows, no layered translucency, no glass.
2. **Sunken is the inset gesture.** Input fills and plot areas on surfaces use `sunken`; this replaces any "pressed-in" shadow language.
3. **Only overlay chrome may lift:** Sheet, Dialog, and menus float above the `scrim` and may use one soft shadow derived from `#1F1E1D` at low alpha (8–12% — the same ink-alpha family as `press-overlay`/`scrim`; Agent 03 must tokenize it, e.g. `--shadow-overlay`, and nothing else may use a shadow).
4. **Press is overlay, not elevation:** pressed states use `press-overlay` (#1F1E1D @ 8%) at 80ms; no scale/shadow combos.
5. **Focus is a ring, not a glow:** 2px `ink-strong` ring with 2px offset, ≥3:1 against adjacent surfaces (16.6:1 on white).
6. **At most two visual planes in play per composition** (canvas → surface → sunken); a scrim plane appears only while an overlay is open.

## 9. Findings for Agent 05

- `ink-subtle` at 13px fails on `sunken` (4.14:1) — qualifiers inside wells use `ink-muted` at 14px+.
- The 13px qualifier / 14px Arabic-minimum tension (§2) needs a ruling in the final decision log; this review's resolution is written above.
- `rem` tokenization (§4) is the load-bearing decision for 100/130/200% text scaling — Agent 04 should verify it against real browser font-size settings, not only zoom.
- Long-Label spot checks to run: «تحصيل دين من مطعم النخيل» (label, 320px wrap), «تسجيل دفعة لمؤسسة الشرق للتجهيزات» (CTA), «طحين فاخر 10كغ — تحت الحد» (exception row).
