# Mobile Composition & Density Audit — Subagent 2 (Task R4-b)

**Target:** `/home/z/my-project/repos/Documents/zed-ai-runs/20260908T201936Z-g53-252a/visual-foundation-package/`
**Auditor:** Subagent 2 — Mobile Composition and Density Auditor · **Date:** 2026-09-09 · **Mode:** read-only research + report
**Source-pack truth:** `/home/z/my-project/repos/Documents/accounting-visual-foundation-source-pack-v1/` (SOP_VISUAL_ONLY.md, rendered-reference/*.html)

**Verdict in one line:** the package's component language is faithful to the source (rows, surfaces, sheet scaffold, RTL discipline all check out), but it fails repair **C** outright (the filter UI is still a permanent chip row), fails repair **D**'s core KPI requirements (broken sum relationship, no progress bar, 320/360 clipping), and demonstrates only a fraction of repair **E/H**'s Arabic, trailing-action, text-scale and safe-area stress cases.

---

## 1. Methodology

1. **Static composition analysis** of `component-gallery.html` (731 lines), `component-gallery.css` (620), `component-gallery.js` (317), `design-tokens.css` (300): white-space/overflow rules, padding/max-width/margin-auto centering, logical vs physical properties, safe-area usage, zebra/divider rules, grid min-content risk.
2. **Doc cross-read** (data-display-system, surface-system, responsive-geometry, content-guidelines, component-contracts, component-states, typography, navigation-shell, overlay-system, self-critique) to catch doc-vs-implementation contradictions.
3. **Live geometry measurement** with the agent-browser headless CLI (read-only `eval`): `documentElement.scrollWidth` vs `clientWidth` at 320/360/390/430 × LTR/RTL; featured-grid overflow; chip/button/row/topbar/nav heights; FAB vs bottom-nav rects; open-sheet composition; RTL trailing-edge rects; token resolution walk.
4. **Text-scale simulation** via root font-size override (16 / 20.8 / 32 px = 100 / 130 / 200%), with fresh-element probes to bypass the chip `transition: all` caching artifact.
5. **Capture triangulation** with the provided a11y snapshots (`current-{ltr,rtl}-{320,360,390,430}.txt`), `overflow-320-{ltr,rtl}.txt`, `computed-structure.txt` (confirms `rowTitleWhiteSpace: nowrap`, `rowTitleTextOverflow: ellipsis`, `textModes: [normal, large]`), `computed-fonts.txt`, `computed-tokens.txt`.
6. **Source-precedent comparison** against `accounting-mockup.html` and `accounting-mobile-components.html` (Two-Jars featured card, §7.3 chip row, §7.7 rows, §7.5 sheet, FAB/nav geometry).

Key measurements (agent-browser, viewport 320 unless noted):

| Measurement | Result |
|---|---|
| Page `scrollWidth` vs `clientWidth`, all 8 viewport×dir combos | equal — **no horizontal page scroll** |
| `.feat-grid` overflow (scroll−client) | **320: 56px · 360: 16px · 390: 0 · 430: 0**; large-text@320: 69px; sim-130%@390: 47px; sim-200%@390: 189px |
| `.kpi-hero` "1,250,000" @200% | scrollWidth 303 > clientWidth 292 (hero clipped) |
| Tile min-content | 133.16px (32px padding + 101px mono numeral) |
| Chip hit box | **36px** (visual = hit; docs claim 44) |
| Buttons / iconbtns / sheet rows / menu options / nav items / snackbar action | 48 / 44 / 48 / 44 / 48+ / 44 — all pass |
| Open sheet | 286×347, handle 36×5, rows 48px, `max-height: 84%` (of demo frame), **0 Apply/Reset buttons, no pointer/drag handlers** |
| FAB vs bottom nav (navigation demo) | FAB top 4504.2 vs nav top 4505.2 → **FAB overlaps the nav's upper ~55px**; `--fab-offset` (80px) token unused |
| Safe area | `.bottomnav` padding `8px 12px 16px`, `.actionbar` `12px 16px`, `.sheet-body` `0 20px 32` — **no `env()` anywhere**; meta viewport lacks `viewport-fit=cover` |
| RTL rows | tile at inline-start (227–271), amount at logical trailing edge (49–103, flush to inner edge), `dir=ltr` + `unicode-bidi: isolate` ✓ |
| Text modes | `normal`/`large` only; `html[data-text-size=large]{font-size:17px}` ≈ 106% |

---

## 2. Per-family composition review

### Buttons — pass (density ✓, geometry ✓)
Full-width 48px ladder, `pair-row` flex with `flex: 1 1 160px`, state strips with 96px labels; press 0.97/120ms; icon-only 44px round with `aria-label`. No nesting or centering issues. Scales correctly (48→51px @17px root; 48→96px @32px root).

### Inputs — pass with one minor
Label-above rhythm (8px), 48px fields, error below field with icon, `padding-inline` for search icons (RTL-correct), amount input `dir="ltr"` + live grouping. Long-content state scrolls internally (documented). Minor: `.sel-value` truncates single-line with no clamp/full-value path (**S2-15**).

### Chips & tags — **Repair C violation (blocker S2-01) + touch defect (S2-10)**
The frame titled **"Filters — tap to select one"** is a permanent, horizontally scrollable chip row (`overflow-x: auto`, single active chip via JS), i.e. the exact UI repair C forbids. No compact Filter control, no filter sheet, no grouped choices/status-date-type-sort, no Apply/Reset, no staged selections, no active-count indicator; the empty-state "Clear filters" is hard-wired to the chips (S2-14). Status tags (In progress/Ready/Closed/Received/Sent/Moved/Returned) are correctly *not* part of the filter control — they are static 12px pills, per the repair's separation rule. Chip hit box measures 36px vs the 44px claimed by `data-display-system.md:29` and `component-contracts.md:32`.

### Segmented — pass
Pill (ivory track, terracotta thumb, RTL-aware JS placement) + underline with counts; 3 segments each; 40px min buttons; the underline row scrolls horizontally (component-scoped, acceptable; the only other horizontal scroller is the chip row).

### Badges — pass
4/12 padding pills, 12/600 text, icon-or-dot pairing; no interaction implied. Source parity (progress gold, ready accent, closed recessed).

### Cards & KPI — **Repair D failures (blockers S2-02, S2-03; minor S2-11)**
- **Broken sum relationship:** featured hero **1,250,000** vs tiles **620,000 + 230,400 = 850,400**. The source's Two-Jars card (`accounting-mobile-components.html:246-289`, `accounting-mockup.html:109-153`) is internally consistent: **850,400 = 620,000 + 230,400**. The package merged that composition with the *standalone* featured-card demo value 1,250,000 (`mobile-components.html:168`), destroying the "two values that visibly belong to the total" requirement. An adjacent "Total balance 850,400" card adds a second, unrelated total with no grouping header.
- **No progress/relationship bar anywhere** — the required summary-metric composition (total + bar + two summing values) does not exist.
- **320/360 clipping:** `grid-template-columns: 1fr 1fr` cannot shrink below 133px tile min-content; measured overflow 56px @320, 16px @360, clipped silently by `.screen{overflow:hidden}`. `responsive-geometry.md:13,22` claims "138px tiles at 320; verified no wrap" — the formula omits the featured card's own 16px padding, and no `tnum`-based graceful truncation CSS exists (`.tile-num` has no overflow rule).
- Positive: **no white-card-in-white-card** — the featured card uses the recessed ivory fill with white inner tiles, the source-accepted treatment; plain cards are single-surface with E1; the grouped surface uses dividers, not nested cards.

### Rows — **Repair E failures (majors S2-04, S2-05)**
- `.row-title { white-space: nowrap; text-overflow: ellipsis }` = **truncation-only**; the "line-clamp preferred" promised in three docs is never implemented (measured `webkitLineClamp: none`). Repair E requires shrink **and wrap** for Arabic.
- Coverage gaps: exactly **one short Arabic title** (تحويل داخلي); no long Arabic label, no wrapped qualifier line, no trailing action/chevron in any row.
- Positive: rows stretch full width of `.rowlist` (no margin-auto/max-width centering anywhere in rows); leading 44px tile + flexible `min-width:0` text + `flex:none` amount pinned to the logical trailing edge (verified in RTL); mono tabular signed amounts with `dir="ltr"` + `unicode-bidi: isolate`; content-driven height (56px min, grew 76→148px under 200% text); consistent inline edges (screen 16 + row 16 = 32px text edge, matching cards and topbar); one divider rule (1px border-soft above subsequent siblings) applied consistently across rowlist/group-list/menu/sheet-rows; zebra alternation consistent and inherited from source (note S2-20).

### Navigation — FAB defect (major S2-09), rest pass
Top bar 56px (60px rendered incl. padding) flat/scrolled variants, truncating title (acceptable for bars). Bottom nav: 4×64px items, 52×32 active pill, filled active icon — fits 320. **FAB:** anchored `inset-block-end: 20px` inside `.nav-demo-wrap` which *contains* the nav, so the 56px FAB covers the nav's top ~55px (measured), instead of floating `--fab-offset` (80px, defined, unused) above it; doc claims 80px + safe-area. Action bar: 72px with one primary — correct, but no safe-area (S2-07).

### Overlays — scaffold pass, drag missing (major S2-08)
Sheet: 36×5 handle, 20px top radius, E2, focus trap + restore + Escape, 48px action rows, scrolling owned by `.sheet-body` (chrome stable) — good foundation for the repair-C filter sheet. Missing: **drag-to-dismiss entirely** (no pointer handlers; self-critique.md:18 admits), no 94vh expanded snap (only `max-height: 84%` of the demo frame), no Apply/Reset pattern. Dialog: intentionally centered (`margin-inline: auto`, max 360) — legitimate. Snackbar: 16px insets, ink surface, 44px undo action, 5s hold — fine. Scrim 0.4 ink — matches source.

### Empty · loading · error — pass with density notes
Four states distinct (no-data vs no-results vs error vs skeleton); 64px tile + guiding copy + one action each; skeletons promise the real layout (title/line/card/row shapes). Minor: `.frame-tall .screen{min-height:560px}` leaves ~450px unjustified blank at rest in the overlays frame (S2-12); `.empty` mixes `gap: 4px` with per-child margins (S2-13).

### Icons & RTL — pass
24-glyph sheet at 20/24px, stroke 1.8; directional mirroring demonstrated for chevrons (`[dir=rtl] .mirror`), symmetric glyphs unmirrored; icon-only controls labeled.

---

## 3. Viewport matrix (measured)

| Viewport | Dir | Page overflow | Notes |
|---|---|---|---|
| 320 | ltr | **none** | Featured KPI grid clipped internally **56px** (tiles 133px min-content vs 122px track in full-bleed math; 111px in demo). Large-text: 69px. |
| 320 | rtl | **none** | Same clipping; RTL row order/edges verified correct. |
| 360 | ltr | **none** | Featured grid clipped **16px**. |
| 360 | rtl | **none** | Same; a11y tree parity with LTR. |
| 390 | ltr | **none** | Fits with 7px headroom per tile. Sim-130%: 47px overflow; sim-200%: 189px + hero number clipped 11px. |
| 390 | rtl | **none** | Same; segmented thumb RTL-aware. |
| 430 | ltr | **none** | Tiles 160px; nav 4×64 fits. |
| 430 | rtl | **none** | Same; logical properties throughout. |

Text scale: shipped modes = **100% / 106%** (`normal`/`large`, 16→17px). Required **100/130/200** — 130/200 absent (S2-06), though the rem architecture itself scales cleanly (fresh-element probe: chip 36→72px, button 48→96px, rows 76→148px at 32px root, no page overflow).

Safe area: **absent in code** (no `env()`, no `.safe-area-*` usage, no `viewport-fit=cover`) while `responsive-geometry.md:26` claims five safe-area surfaces — doc-vs-implementation contradiction (S2-07).

---

## 4. Findings table

| ID | Area | Severity | Criterion | Summary | Class |
|---|---|---|---|---|---|
| S2-01 | filters | **blocker** | C | Permanent scrollable filter-chip row is the filter UI; no Filter control/sheet/Apply/Reset/staged selections/count indicator | proposed |
| S2-02 | metrics | **blocker** | D | Featured hero 1,250,000 ≠ tiles 620,000+230,400; source had exact sum 850,400; no progress/relationship bar anywhere | corrected |
| S2-03 | metrics | **blocker** | D/H | Featured 2-tile grid clipped 56px @320 / 16px @360 (69px large-text; 47/189px @130/200%); "138px verified" claim false; `.tile-num` has no overflow strategy | corrected |
| S2-04 | rows | major | E | `.row-title` truncation-only (`nowrap`+ellipsis); promised line-clamp never implemented; Arabic cannot wrap | proposed |
| S2-05 | arabic | major | E/H | No long Arabic label, no wrapped qualifier, no trailing action/chevron demos in rows | proposed |
| S2-06 | text-scale | major | H | Only 100%/106% text modes; 130/200 missing from UI, tokens, docs | proposed |
| S2-07 | surfaces | major | C/H | No safe-area in nav/actionbar/sheet/FAB; no `viewport-fit=cover`; docs claim five surfaces | corrected |
| S2-08 | filters | major | C | Sheet has no drag-to-dismiss, no 94vh snap (self-critique admits); overlay contract documents full drag spec | corrected |
| S2-09 | other | major | geometry/nav | FAB demo overlaps bottom nav (~55px) instead of 80px above; `--fab-offset` token unused | corrected |
| S2-10 | touch | major | geometry | Chip hit box = 36px vs claimed 44px; container padding doesn't enlarge the button | corrected |
| S2-11 | metrics | minor | D | Source's conditional footnote row dropped; two unrelated "totals" adjacent with no grouping header | normalized |
| S2-12 | scrolling | minor | D | `.frame-tall .screen{min-height:560px}` — ~450px unjustified blank at rest | normalized |
| S2-13 | surfaces | minor | geometry | `.empty` mixes flex gap + per-child margins; `.kpi-change` margin-top vs `.screen` gap — dual spacing systems | normalized |
| S2-14 | filters | minor | C | "Clear filters" hard-wired to the chip group; will break when C lands | normalized |
| S2-15 | rows | minor | E | `.sel-value` single-line truncation; documented "full value on tap" not implemented | normalized |
| S2-16 | text-scale | note | H | POSITIVE: rem tokens scale cleanly to 130/200% (fresh-element probes); chip `transition: all` animates layout — scope it to colors | inherited |
| S2-17 | rtl | note | E/H | POSITIVE: RTL trailing-edge, bidi isolation, logical properties, LTR/RTL tree parity all verified | inherited |
| S2-18 | scrolling | note | geometry | POSITIVE: no page-level horizontal scroll at any viewport × direction | inherited |
| S2-19 | arabic | note | H | POSITIVE: Arabic font fallback explicitly documented (typography.md:10, README.md:9, verification-report.md:92) | inherited |
| S2-20 | rows | note | E | Divider rule consistent everywhere; zebra+divider double separation inherited from source — decide and document one rule | inherited |

**Totals: 3 blockers · 7 majors · 5 minors · 5 notes.**

---

## 5. Concrete repair recommendations (with source tokens/geometries)

### C — Filter control + bottom sheet (fixes S2-01, S2-08, S2-14)
1. **Filter control:** outline button, `--control-height` 48px, `--radius-control` 12, 20px `#i-filter` icon + "Filter" label; active state = `accent.50` fill + `accent.600` text (reuse the `.ghost-btn[aria-expanded]` treatment already in the header); optional count pill reusing `.count` (12/700 mono, `recessed`→`primary.700` when active).
2. **Filter sheet:** reuse the existing `.sheet` scaffold (handle 36×5 `divider`, `--radius-sheet` 20 top corners, E2, `--z-scrim` 40 / `--z-overlay` 50). Title row 20px/700 + 44px quiet close. Body: grouped 48px `sheet-row` choices (Status: In progress/Ready/Closed…; Date range; Type; Sort) with the menu's selected treatment (`accent.50` + `accent.600` + 20px check at `margin-inline-start: auto`). Footer: sticky, `Reset` (btn-ghost, inline-start) + `Apply` (btn-primary, flex 1); `padding-bottom: calc(32px + env(safe-area-inset-bottom))`.
3. **Behavior:** staged selections in JS; commit on Apply only; Cancel (scrim/Escape/close) discards; parent shows only "N filters active" summary; rewire `data-chip-clear` → `data-filters-clear` (clear staged + applied, update count, snackbar confirm).
4. **Drag-to-dismiss:** pointer events on the handle row — translateY follows pointer, transition suppressed; release: `dy > +130px` → dismiss, `dy < −50px` → expand to the 94vh snap, else settle at 84vh; clamp upward travel at −44px; restore `--motion-sheet` 340ms `cubic-bezier(.16,1,.3,1)` on release (source `BottomSheet.jsx:88-126` geometry).
5. **320 + large text:** sheet body scrolls (`overflow-y: auto` already), Apply/Reset stack vertically below 360px or at 200% text; verify 48px rows and label wrap with `min-width: 0`.

### D — KPI composition (fixes S2-02, S2-03, S2-11)
1. **Restore the source sum:** hero **850,400** with tiles **620,000** ("Reserved", `primary.100` chip + `primary.700` icon) + **230,400** ("Free", `positive.100` chip + `positive.700` icon) — exactly the source Two-Jars values; drop the 1,250,000 hero (it belongs to the standalone featured demo, not this composition).
2. **Add the relationship bar** between hero and tiles: 8px-high track, full card width, `--radius-full`, `--color-recessed` track, fill segment `--color-primary-500` ≈ 73% (620,000/850,400); optional second segment `--color-positive-200`; caption 12px `ink-secondary`: "620,000 reserved · 230,400 free". Grid-aligned to 4px (margin-block 12).
3. **320 safety:** `.feat-grid { grid-template-columns: minmax(0,1fr) minmax(0,1fr) }`, `.tile { min-width: 0 }`, `.tile-num { overflow: hidden; text-overflow: ellipsis; min-width: 0 }` (or `clamp()` numeral size); collapse to one column below 360px; fix the documented formula `(100vw − 2×16 − 12)/2` → subtract the card padding too.
4. **Grouping:** either give the KPI pair a section header or convert card 1 into a change/companion metric; restore the source's conditional footnote row (12px caption + 16px info icon, centered, 12px above the card bottom).
5. Keep the recessed-ivory + white-tile treatment (source-accepted); do **not** introduce white-in-white.

### E — Rows (fixes S2-04, S2-05, S2-15)
1. `.row-title { white-space: normal; overflow-wrap: break-word; -webkit-line-clamp: 2; display: -webkit-box; -webkit-box-orient: vertical; overflow: hidden }` — wrap first, 2-line ceiling; keep `.row-main { min-width: 0; flex: 1 1 auto }` and `.row-amt { flex: none; text-align: end; unicode-bidi: isolate }` so the value stays pinned.
2. Add demo rows: long Arabic title (e.g. «تحويل راتب شهري مع علاوة بدل مواصلات وخصم التأمين»), wrapped qualifier («الدفعة الثانية من أصل أربع دفعات», caption 12 `ink-secondary`), and one row with trailing chevron (`#i-chevron-right`, mirrored in RTL) + one with a 44px trailing icon action coexisting with the amount.
3. `.sel-value`: 2-line clamp or full-label-in-menu; implement "full value on tap" as opening the menu at the option.
4. Keep: full-width rows, 32px inline edge discipline, one divider rule (decide zebra+divider intentionally and document it — S2-20).

### H — Verification surface (fixes S2-06, S2-07, S2-16)
1. Text control → three modes `A / A+ / A++` = 16 / 20.8 / 32px root (`data-text-size` normal/130/200); tokens already scale (verified).
2. `viewport-fit=cover` on the meta; `env(safe-area-inset-bottom)` on `.bottomnav` (16 + inset), `.actionbar` (12 + inset), `.sheet-body` (32 + inset), `.fab` (`--fab-offset` + inset), `env(safe-area-inset-top)` on `.topbar` (8 + inset).
3. Scope `.chip`'s `transition: all` to `background-color, color` (currently animates min-height/font-size and produces stale measurements).
4. FAB demo: anchor to a container that ends above the nav and use `var(--fab-offset)` (80px) + safe-area; anchor to the frame edge (16px), not a padded screen (avoid double inset).

---

## 6. Explicit unresolved list

1. **Filter sheet content model** — the repair brief requires grouped choices (status/date range/type/sort) with staged selections; the source pack contains no filter-sheet precedent (SOP §7.3 is chips), so the exact grouping copy, sort ordering, and count-indicator form are *proposed*, not inherited — needs coordinator sign-off.
2. **130/200% acceptance thresholds** — the rem architecture scales, but final pass/fail at 200% (e.g. whether KPI hero may wrap to two lines or must shrink via `clamp`) is a policy decision not defined by the source.
3. **Zebra + divider coexistence** — inherited from source; whether the repair keeps both or drops dividers on zebra rows is a one-rule decision to make explicit.
4. **On-device safe-area / real-font rendering** — not testable in the desktop headless environment (declared limits in verification-report.md:92-93); my findings cover the code-level absence, not device behavior.
5. **Transition-based measurement artifacts** — `.chip { transition: all }` and any future layout transitions can make headless measurements read mid-transition values; auditors should use fresh-element probes (methodology §3) or wait past `--motion-base`.
