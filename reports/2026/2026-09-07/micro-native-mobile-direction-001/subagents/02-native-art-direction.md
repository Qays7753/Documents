# 02 — Native Art Direction: Compositional Systems for the Three Candidate Directions

**Delivery:** `micro-native-mobile-direction-001` · **Task ID:** 3-b
**Agent:** Specialist 2 — Senior Art Director & Visual Systems Designer · **Date:** 2026-09-07
**Inputs:** worklog; `en/00` lessons; `en/01` audit; rejected syntheses `-001`/`-002`. Palette, measured contrast pairs, Arabic floors, and money/date formats are fixed; differentiation comes from **composition, surface, shape, density, voice, and rhythm** — never color invention.

---

## 1. What makes a screen read "native premium" vs "web"

Both rejections failed as a *category*, not styling. Reference frame: Apple first-party apps, Material 3 / Google Wallet, Revolut/Monzo/Starling statements, Airbnb, Things 3 — large-title collapse, full-bleed tonal heroes, fixed money columns, hairline registers, ink buttons on edge-to-edge canvases. Their shared properties are countable:

| # | Dimension | Web symptom | Binding native rule |
|---|---|---|---|
| N1 | Surfaces | 4–8 boxed modules | ≤1 grouped surface per screen state; content sits on canvas, separated by hairlines + tonal steps; a box must be one semantic unit *and* must float |
| N2 | Chrome ratio | 30–45% persistent chrome | ≤19% of viewport (≤160px of 844: 64 bar + 64 nav + safe area); the rest scrolls away or lives in a sheet |
| N3 | Row rhythm | mixed paddings per module | one row template per list; tiers {56, 64, 72}px; ±0px variance; dividers inset 16px from the reading edge |
| N4 | Header behavior | static header / load animation | exactly two states (expanded ≤96px / compact 56–64px), scroll-driven, ≤280ms, title never jumps |
| N5 | Canvas | centered column, page background | canvas paints under system bars; 16px fixed margin at 320/360/390/430; no max-width |
| N6 | Elevation | decorative shadows on cards | shadows only on overlaying surfaces (sheets, dialogs, FAB, toasts); ≤2 elevation levels |
| N7 | Corners | radius soup | exactly 3 radii (control / macro / sheet), concentric: sheet outer = control inner + 8 |
| N8 | Color | accent everywhere | ≤10% brand-hue pixels per screen; exactly one high-contrast action fill; neutrals ≥90% |

The rule the rejections violate hardest: **navigation is a stack with a reliable back affordance, and short-lived work happens in sheets — never as page sections.** No screen's meaning may depend on scroll-length. Each seed is specified as *anatomy with behavior*, not page layout.

---

## 2. Seed A — «الخلاصة اليومية» / The Daily Brief

**Composition.** Single-column iOS-editorial. The app bar carries the date as a collapsing large title («الأحد 06/09/2026»), 96px → 56px. The **position block is embedded in the scroll** — typographic ink on paper, edge-to-edge, zero container chrome: 32px cash figure with «لك»/«عليك» as inline secondary figures separated by hairlines. Then a chronological timeline of the day; then an attention strip. On scroll-off the three figures **condense into the compact title bar**.
**Surface & shape.** One surface level + E1 for sheets/dialogs/FAB. Radii 4 / 10 / 16 (markers / buttons / sheet tops); hairlines 1px `#e5dcd6`; timeline rail = 1px vertical hairline on the right (RTL) with 8px hollow nodes; attention marker = 2px `#964e33` right-edge bar.
**Density.** 5 blocks before scroll at 390px (title 96 + position 132 + label 28 + 2 rows + attention ≈ 700px fold); timeline rows 64px, ≤2 lines, one action word; breathing 24–32px between blocks.
**Type.** IBM Plex Sans Arabic; digit runs in IBM Plex Sans with `tabular-nums` — same family DNA. Scale: large title 28/36·600 → compact 17/24·600; hero 32/40·700 tnum; secondary 20/28·600; section label 13/18·600 (weight + color only — **never letter-spacing on Arabic**); body 15/24·400; row amount 16/24·600 tnum; caption 13/20.
**Terracotta.** Atmosphere = warm paper canvas (`#faf7f4`-family) + `#f4e4db` tint on attention rows; accents = section labels `#964e33` (≈5.8:1 on paper, re-measure), focus ring, out-deltas; **one action fill = «سجّل» FAB `#964e33` + white (6.11:1)**. Primary buttons are **neutral ink** (`#221c18` + warm white). Press `#b4613f`, 90ms, never resting.
**Dark.** Not inversion: paper → warm near-black `#1a1613`-family, ink → `#f1e9e3`; the position block *gains* one tonal step to hold hierarchy; labels → `#d59172` (≈6.5–7:1 on dark canvas); ink buttons invert to warm-white fill + `#1c1815`; FAB `#8fd5d6` + `#1c1815`.
**Rhythm.** Irregular whitespace allowed *between* blocks (24/32/48), never *inside* lists.
**Signature.** **The day-title collapse that absorbs the position figures** (Weather/Stocks choreography): *the day is the app bar*.

---

## 3. Seed B — «الدفتر» / The Register

**Composition.** Compact 56px app bar (title 17/24·700 + one search field, max). The **sticky truth bar** (72px): three live tabular figures — «النقد | لك | عليك» — as a working segmented filter; tapping one re-sorts the register beneath to that ledger. Register: date-pinned sections («الخميس 10/09») with day-total rows, then hairline rows — subject on the reading side, amount in the fixed money column. **Zero cards, zero containers.**
**Surface & shape.** One level; the truth bar earns a single tonal step (band `#ffffff` on paper `#faf7f4`), no shadow; E1 only for sheets/dialogs/FAB. Radii 0 / 4 / 12 (rows / chips / sheets). The **2px Terracotta rule under the app bar** is the direction's only ornament — a brand mark, not a layout device.
**Density.** Densest: 128px sticky budget (18% chrome) leaves 8–9 financial rows (64px) or ~10 secondary rows (56px) at 390px; fold = truth bar + date pin + 4–5 rows.
**Type.** **Almarai** (400/700) for Arabic — humanist, the register voice; **IBM Plex Mono** for all money-column digit runs (monospace = guaranteed tabular + decimal alignment). Scale: app title 17/24·700; truth figures 26/32·700 mono; day pin 13/20·700; row subject 15/24·400; row amount 16/24·600 mono; caption 13/20. Money column **88px @320 → 96px @390+** (148px subject budget at 320, per verified arithmetic).
**Terracotta.** Atmosphere = paper canvas + 2px rule + `#f4e4db` selected-day tint; the only colored text is semantic — «لك» `#057b7c`, «عليك» `#964e33` (≥16px·600, ≈4.8–5.8:1 on paper); **one action fill = FAB «سجّل» `#964e33` + white (6.11:1)**, press `#b4613f`.
**Dark.** The ledger lamp: canvas `#191512`, truth bar on raised `#201b17`, warm hairlines `rgba(213,145,114,0.18)` (frames never go cold-gray), mono digits `#f1e9e3`; FAB `#8fd5d6` + `#1c1815`. Light separates by paper-vs-white bands; dark by warm hairlines + one tonal step — not inversion.
**Rhythm.** Mechanical repetition — identical rows, zero extra space; whitespace only at pins and screen edges.
**Signature.** **The truth bar that filters the register** — tap «لك» and the ledger re-sorts live while the figures and the money column never move. Impossible to compose as a web page section.

---

## 4. Seed C — «الصندوق» / The Counter Hub

**Composition.** Position-first, Material-3-flavored. **Full-bleed cash hero on a deep tonal surface** (light: deep warm ink `#221c18`-family, ~216px): label «النقد المتاح» + delta + source-state + 40px bold warm-white figure. Below, **the counter split** (128px): «لك» / «عليك» as two large counters on one raised surface divided by a **single 1px hairline — no gap, no border**. Then the **horizontal day strip** (72px, right→left RTL, snap-paging) + the day agenda paged to the selected day. Hero collapses to a 64px cash strip; day strip sticks.
**Surface & shape.** Two in-flow levels: canvas + tonal macro-surfaces (hero deep, split raised `#ffffff` / dark `#292420`); E1 sheets/dialogs/FAB; separation is **tonal, not shadow**. Radii 8 / 16 / 20 (day pills / buttons / sheet tops), continuous, concentric. Hairlines minimal (split + row separators). Selected day = `#f4e4db` pill + 4px `#cc785c` underline (non-text, on canvas).
**Density.** Block-paged, not row-scrolled: 3 macro-blocks before scroll (216 + 128 + 72 = 416px) + 2–3 agenda rows (72px) at 390px; the agenda pages, so rows-per-screen is a chosen 4–6.
**Type.** **Alexandria** (500/700) — geometric Arabic with real display weight; display 40/48·700 (proportional allowed only for lone hero values); counters 24/32·700; section 16/24·600; body 15/24·400; **all aligned money uses the shared tabular money voice (§7)**.
**Terracotta.** Atmosphere = brand-soft tint blocks (day pill, sheet grabber zone) + the hero's warm deep ink; accents = `#cc785c` underline, deltas (`#057b7c` in / `#964e33` out); **one action fill = sheet primary button `#964e33` + white**; press `#b4613f`. Hero text = warm white on deep ink (~14:1); **text never on `#cc785c`**.
**Dark.** A luminance ladder, not hue flips: hero the deepest plane `#14100e`, display `#f1e9e3`; split `#292420`; tints `#332d27`; `#d59172` the selected-day underline, carrying dark text where a fill is needed (5.26–6.82:1).
**Rhythm.** 16px gutters between macro-blocks; the hairline is the zero-space divider; 8px strip gaps; 12–16px inside blocks.
**Signature.** **The counter split** — two huge figures sharing one hairline on a tonal surface, plus the paging day strip.

---

## 5. Differentiation proof (anatomy, not styling)

| Dimension | A — Daily Brief | B — The Register | C — Counter Hub |
|---|---|---|---|
| Core composition | Editorial scroll narrative | Dense register + sticky filter control | Macro-block hub + horizontal paging |
| Header behavior | Large title collapses, absorbs figures | Compact bar + sticky truth bar | Hero collapses to cash strip; day strip sticks |
| Screen anatomy | Title → position → timeline → attention | Bar → truth bar → date-pinned rows | Hero → split → day strip → paged agenda |
| Primary interaction | Read-then-act rows; push stack | Filter + scan + FAB capture | Tap counters / page days; **sheet-first** |
| Density @390 | 5 blocks, ~6 rows, editorial air | 8–9 rows, 18% chrome | 3 macro-blocks + 4–6 paged rows |
| Containers | 0 (ink on paper) | 0 by construction | 3 full-bleed tonal surfaces, no boxed insets |
| Signature | Title absorbs the day's numbers | Truth bar filters the register | The hairline counter split |

Color is identical across all three; voice, geometry, and anatomy are not.

---

## 6. Anti-drift rules

**A — anti-dashboard / anti-newsletter.** Chronology is not a module grid: one column, no stat cards, no boxed headers; every timeline row carries amount + party + one action word. The position block is edge-to-edge ink (box count 0) — no card wall is possible.
**B — anti-POS / anti-ERP / anti-statement-page.** The register lists *events* (sales, payments, expenses), never SKUs or checkout grids. Rows ≤2 lines, one search field, no toolbar forests — ERP dies there; the truth bar is compact and functional, never a celebratory balance hero — banking drift dies there. It must prove it is **not Calm Ledger reborn**: native-ness comes from interactive anatomy, not a typographic page statement.
**C — anti-wallet / anti-POS / anti-dashboard.** The hero is labeled truth with delta and source-state; no spend affordances, no card number, no «ادفع», no asset tiles — the wallet silhouette dies. The day strip aggregates days, never order tickets; all functions live in sheets — a dashboard needs modules, C has none; macro-surfaces are full-bleed, never boxed insets.

---

## 7. Cross-cutting systems

- **The money voice is a Micro constant shared by all three:** ASCII digits, tabular face (IBM Plex Mono or Plex `tnum`), two decimals, `1,245.50 د.أ` with digits LTR-isolated and «د.أ» in RTL flow, decimal alignment, fixed 88/96px column. Differentiation lives in display figures, never in number discipline.
- **Arabic content at 320px:** 148px subject budget (288 − 88 money − 44 marker − 8 gap); long names («مشغل ليان للأثاث المفروشة») truncate at 2 lines + ellipsis, never 3; button labels ≤24 chars; 9-character display figures (`1,245.50`) at 40px ≈ 200px — fits 288px with the unit stacked.
- **Quiet charts:** ≤2 forms per direction; bars 8–12px, 4px gaps, 1px hairline baseline; no gradients/3D/animation; ink and accent fills only, each ≥3:1 against its *actual* surface; period + unit + source-state + one interpretation sentence; never in a home's first fold.
- **Iconography:** one custom geometric outline family — 24px grid, 1.75–2px stroke, rounded joins; filled only for the active nav seat and happened-states; icons render ink/muted, terracotta only as the active-seat marker; no duotone, no illustration.
- **Logo restraint:** the fixed logo appears in exactly four places — app icon, splash (≤1s), settings header, first-boot helper. Never on home, beside an app-bar title, or as watermark/empty-state/loading decoration.

---

## 8. Ranked verdict and pre-prototype corrections

1. **B — The Register (8.6/10).** Highest native certainty: compact bar + working segmented filter + hairline rows + FAB is the anatomy of the most-trusted native register apps; the money column is structural, not stylistic; smallest drift surface. **Must fix:** truth-bar filter semantics («النقد» = all cash movements, selection + counts); 320px arithmetic proof; distance from Calm Ledger (2px rule, mono money, interactive pin); warmth (paper canvas, `#f4e4db` day tint).
2. **A — Daily Brief (8.2/10).** Strongest identity and iOS-native craft; the collapse-absorbs-figures move is memorable and honest. **Must fix:** timeline rows must carry action (amount + party + verb) or it drifts to a reader app; precise compact-bar figure strip; Plex `tnum` for row digits; digest capped at 5 blocks; one primary per screen.
3. **C — Counter Hub (7.4/10).** Boldest first impression — but the dark full-bleed hero is the exact silhouette of wallet apps (the rejected banking drift), and sheet-first + paging can hide operations behind chrome. **Must fix:** hero label + delta + source-state, zero spend affordances; day-strip selection + agenda paging defined (RTL right→left, snap, sticky); radii capped at 3 values; split = exactly one hairline; 56px row floors inside sheets.

---

## 9. Binding art-direction rulings

- **AD-01** — Native craft floors bind all directions: ≤1 grouped surface per screen state, persistent chrome ≤19% of viewport, ≤2 elevation levels, exactly 3 radii, ≤10% brand-hue pixels, shadows only on overlaying surfaces.
- **AD-02** — Every scrollable screen defines two header states (expanded ≤96px / compact 56–64px), scroll-driven, ≤280ms; static page headers are prohibited.
- **AD-03** — Edge-to-edge canvas with fixed 16px horizontal margin at 320/360/390/430; no centered column, no max-width, no page-background role.
- **AD-04** — One row template per list; tiers {56, 64, 72}px; divider inset 16px from the reading edge; zero variance inside a list.
- **AD-05** — The money voice is a cross-direction constant: ASCII digits, tabular face, two decimals, digit-run LTR isolation with «د.أ» in RTL flow, fixed 88/96px column, decimal alignment.
- **AD-06** — Terracotta discipline per screen: exactly one `#964e33`+white action fill (6.11:1); `#b4613f` press-only (90ms, never resting); `#cc785c` atmosphere/graphics only, never text-bearing in light; `#057b7c` accent text (5.08:1 vs white).
- **AD-07** — Dark themes are luminance-ladder redesigns, not inversions; every pairing re-measured at build; dark action fill = `#8fd5d6` + `#1c1815` label; `#d59172` carries dark terracotta label/underline roles (≈6.5–7:1 on dark canvas).
- **AD-08** — Seed A: the position block is typographic ink-on-paper with hairlines, zero container chrome; its figures condense into the compact title bar on collapse; primary buttons are neutral ink; the FAB is the only Terracotta action.
- **AD-09** — Seed B: zero-card by construction — hierarchy only via app bar, truth bar, date pins, hairlines, and the money column; the truth bar is a working filter (live re-sort), never a display.
- **AD-10** — Seed C: the hero is deep warm ink with warm-white text (~14:1), presenting label + delta + source-state and no spend affordance; the counter split uses exactly one 1px hairline; no text ever on `#cc785c`.
- **AD-11** — Arabic floors: nothing below 13px; body 15px; line-height ≥1.6; rows ≥56px; no letter-spacing on Arabic; button labels ≤24 chars; subject truncation at 2 lines within the 148px budget at 320px.
- **AD-12** — Type systems locked: A = IBM Plex Sans Arabic + Plex `tnum` digits; B = Almarai + IBM Plex Mono money; C = Alexandria display + the shared mono money voice; proportional figures only for lone display values.
- **AD-13** — Charts stay quiet: ≤2 forms per direction, 8–12px bars, 1px baselines, no gradients, ≥3:1 on actual surface, period/unit/source-state/interpretation mandatory, never in a home's first fold.
- **AD-14** — One custom geometric outline icon family (24px grid, 1.75–2px stroke); filled only for the active nav seat and happened-states; terracotta icons only as the active-seat marker.
- **AD-15** — The fixed logo appears only in app icon, splash, settings header, and first-boot helper — four places, never in content screens.
- **AD-16** — Category self-check before any prototype: no module grids, no checkout grids, no wallet-balance affordances, no toolbar forests, no boxed-inset walls; every grouping surface must pass "one semantic unit + must float".

---

*Art direction only; the orchestrator owns the final choice. Contrast values are measured evidence from the brief and prior audits; new pairings must be re-measured at build.*
