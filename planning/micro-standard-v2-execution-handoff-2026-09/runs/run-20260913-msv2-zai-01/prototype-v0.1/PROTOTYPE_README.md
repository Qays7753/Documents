# PROTOTYPE_README — Micro Standard v2 Prototype v0.1

- **Run**: `run-20260913-msv2-zai-01` · **Branch**: `micro-standard-v2-execution-20260913`
- **Purpose**: an independent, interactive, approximate visual review of every visual change implemented in the Standard during this run. It is **not** a product, not a source of truth, and not transferable into Micro.

## How to open

Open `index.html` directly in any modern browser (double-click, or serve the folder statically). Everything is local: no network, no fonts CDN, no frameworks, no build step.

| File | Role |
|---|---|
| `index.html` | the prototype — 11 scenes in one RTL page with a scene switcher and controls |
| `styles-tokens.css` | **verbatim copy** of `micro-standard-v2/design-tokens.css` (Wave C state) so the prototype consumes the exact final tokens |
| `prototype.css` | composition styles mirroring `component-gallery.css` patterns |
| `app.js` | local demonstration interactions only |
| `screenshots/` | key scene captures (headless Chromium) |
| `PROTOTYPE_COVERAGE.md` | maps each scene to the Standard file/contract it demonstrates |
| `PROTOTYPE_VALIDATION.md` | what was tested, results, and limitations |

## Controls (above the phone frame)

- **العرض (viewport)**: 320 / 360 / 390 / 430px frame widths.
- **الحركة (motion)**: عادية / مخففة (reduced) — collapses transitions/animations while preserving meaning, matching the Standard's reduced-motion contract.

## The 11 scenes

1. **الرئيسية وFAB** — quiet-today block, anchored cash value with currency unit, identity FAB (`#D97757`) in its own gutter opening the create sheet.
2. **حفظ عادي** — form with ordinary-save button: Warm Tint surface + dark ink, live loading demo (duplicate-submit guard), pressed state with the `#C96442` edge, quiet completion, success snackbar with check marker.
3. **اعتماد كبير وحذف** — filled warm-ink commit ("إغلاق الفترة") with consequence wording and independent confirm/cancel; destructive delete flow through the same high-consequence dialog; pressed state moving to `#3D3D3A`.
4. **قيمة مالية** — value zone slots (label / value / د.أ unit / period chip / delta) and the three honest voids: action chip ("سجّله"), the word "غير متاح", and a measured zero with its label.
5. **صف تشغيلي** — operational rows with ≤3px state edge stripes, state tags (word + marker), stable trailing amount slots, overflow sheet with a destructive row.
6. **تحديد وعناصر** — segmented control (clay-edge thumb), underline variant with counts, chips where selected = edge + bold ink (never black fills).
7. **الحالات** — success / error / pending / unknown / reviewed tiles, each word + marker + semantic hue on the marker.
8. **رسم بياني** — question-led Arabic bar chart with period chip and four cycled states: data (one Info highlight + text alternative), measured zeros (visible 2px baseline marks), no data (word + icon), loading (skeleton).
9. **أوراق وحوارات** — bottom sheet (drag handle, save via ordinary-save class), centered dialog, shared scrim, Escape/focus handling.
10. **التنقل** — four official destinations, current-destination clay edge pill, FAB gutter demo.
11. **إتمام هادئ** — the full save lifecycle (press → loading → "تم الحفظ" + marker → return) with a step-by-step legend.

## Boundary

No product logic, routes, writes, formulas, real data sources, or remote assets. All numbers and labels are illustrative. Issues seen here are recorded as **prototype composition issues** first; they never automatically change the Standard.
