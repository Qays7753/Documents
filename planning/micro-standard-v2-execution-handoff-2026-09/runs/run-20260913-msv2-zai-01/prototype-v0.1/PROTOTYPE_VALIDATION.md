# PROTOTYPE_VALIDATION

- **Run**: `run-20260913-msv2-zai-01` · Validated in headless Chromium (Playwright) — local browser evidence only.
- **Results file**: `PROTOTYPE_TEST_RESULTS.json` · **Screenshots**: `screenshots/` (19 captures)

## What was tested — and the result

| Check | Method | Result |
|---|---|---|
| All 11 scenes activate | scene chips clicked programmatically | **PASS** (11/11; each `is-active` and renders) |
| Zero JS errors | `pageerror` + `console.error` listeners across the whole session | **PASS** (0) |
| Ordinary-save surface | computed style on the save button | **PASS** — bg `rgb(245,244,237)` (#F5F4ED), ink `rgb(20,20,19)` (#141413) |
| Pressed save edge | `.is-pressed` computed box-shadow after transition settle | **PASS** — inset 2px `rgb(201,100,66)` (#C96442); surface stays Warm Tint |
| Loading behavior | click → `aria-busy`, bg check, duplicate-submit guard | **PASS** — stays on Warm Tint `rgb(245,244,237)`, label persists, re-click blocked |
| Quiet completion | auto-advance after loading | **PASS** — label "تم الحفظ" + check marker (`btn-complete`), then restores "حفظ القيد"; snackbar "تم حفظ القيد" with success marker |
| High-consequence commit | open "إغلاق الفترة؟" dialog | **PASS** — ink fill `rgb(20,20,19)`, pressed `rgb(61,61,58)` (#3D3D3A), consequence copy + independent تراجع/اعتماد path |
| Destructive flow | delete → confirmation dialog | **PASS** — same high-consequence dialog contract |
| Chart states | cycle button ×4 | **PASS** — data → zero(+text alternative) → no-data → loading → data |
| Sheet & dialog & scrim | open, Escape close, scrim color | **PASS** — scrim `rgba(20,20,19,0.45)`; Escape closes; focus returns |
| Segmented thumb/underline | visibility + placement after selection change | **PASS** — thumb visible, tracks the selected option (clay edge) |
| Bottom nav | switch destination | **PASS** — current pill gains clay edge + filled icon |
| Viewports | 320/360/390/430px, busiest scene (rows) | **PASS** — no horizontal overflow at any width (page and phone frame) |
| RTL & numerals | document `dir`, `dir="ltr"` amount slots, tabular mono | **PASS** — `dir=rtl`; amounts use English digits with bidi isolation |
| Reduced motion | control toggle; computed durations | **PASS** — transitions/animations collapse to 0.00001s; labels/markers preserve meaning |
| Token parity | `styles-tokens.css` is a byte-identical copy of the Standard's `design-tokens.css` (Wave C) | **PASS** (copy verified at build time; provenance in file header) |

## Issues found and fixed during validation (prototype composition)

1. `[hidden]` overlays stayed in layout because author `display` values overrode the UA rule — added the `[hidden] { display: none !important; }` guard. The same latent defect existed in the gallery's dialog anchor; the identical guard was added to `component-gallery.css` and recorded as a Wave B amendment.
2. Loading state inherited the disabled surface instead of the Warm Tint (rule order) — reordered so loading keeps the save surface, matching the Standard contract.

## What was NOT tested (explicitly not claimed)

- Physical Samsung-device testing — not performed.
- Screen-reader (AT) testing — not performed; `aria-*` attributes were checked in markup and state attributes only.
- Real Arabic device fonts, PWA behavior, performance on low-end hardware — out of scope for a static review prototype.
- Any product behavior: this prototype contains no data, formulas, routes, writes, or posting logic.

## Limitations

- The prototype demonstrates *presentation* of states and slots; when a state appears in the real product remains a Micro product decision.
- Illustrative numbers (1,500 / 4,780 / −640 …) are placeholders, not financial truth.
- Scene 1's FAB opens the rows-scene sheet (the only sheet wired) — acceptable for visual review; it demonstrates the create surface but not a dedicated create screen.
