# Coverage Matrix — Required Family/State → HTML Location → Status

Run `20260908T133450Z-16d11` · "Implemented" means rendered and inspectable in `final/micro-component-visual-library.html` at the stated location. Verification codes: **J** JS-measured · **H** headless screenshot · **M** manual/interactive test. Anything not implemented is explicitly marked **documented-only**.

## 1. Foundation (`#view-foundation`)

| Item | Location | Status |
|---|---|---|
| Brand tokens (atmosphere, tint, ink, on-brand + press overlay) | أسرة العلامة section | Implemented (H: 01) |
| Surfaces (canvas/surface/sunken) | أسطح المنتج section | Implemented (H: 01) |
| Ink & structure (7 inks, 2 lines, scrim) | الحبر والبنية section | Implemented (H: 01) |
| Semantic families (4 base+tint pairs) | الأسر الدلالية section | Implemented (H: 01) |
| Type specimens (32/15/14/13 + tabular demo) | الطباعة section | Implemented (J: computed styles) |
| Spacing scale 2–40 · Radius 6–24/full | المسافات والأركان | Implemented (H: 01) |
| Motion durations + easings table | الحركة section | Implemented (J: computed 0.24/0.16/0.2s) |
| RTL mirror registry (mirrored vs not) | سجل انعكاس الأيقونات | Implemented (J: audit A6) |

## 2. Component Library (`#view-library`)

| Family | Variant / State | Location | Status |
|---|---|---|---|
| PrimaryValueBlock | default / with-state / unavailable | specimen `default`, `with-state`, `unavailable` | Implemented (H: 02) |
| MetricGroup | one surface, aligned rows, dividers ≤3 | `tones` specimen | Implemented (H: 02) |
| MetricRow | positive / danger(danger) / warning / unavailable / qualifier | same | Implemented (H: 02) |
| CompactTile | comparison pair (مستحق لك/عن عليك) | `comparison-pair` specimen | Implemented (H: 02) |
| CompactTile | `--tinted` hook | CSS only | **Documented-only** — the tint pattern is exhibited by the rail tile |
| QuickActionRail | 5 actions, tinted first, snap, edge fade, scroll | `rail` specimen (live scroll) | Implemented (M + J peeks) |
| OperationalRow | supplier-purchase / delivery-settlement / collection / stock-threshold / expense | five specimens | Implemented (H: 02) |
| Button | primary (interactive flow `#btn-flow-demo`) | `variants` specimen | Implemented (M) |
| Button | secondary / quiet / destructive / destructive-quiet / icon-only ×2 | `variants` specimen | Implemented (H: 02) |
| Button | loading (frozen + interactive) / disabled / focused / pressed / quiet completion | `states` specimen | Implemented (H: 02, M) |
| Input | text / amount (د.أ affix, dir ltr, inputmode decimal) / search + clear / date / select | `fields` specimen | Implemented (H: 02, M) |
| Input | segmented / tabs / checkbox / switch | `controls` specimen | Implemented (M) |
| Input | error (static + triggerable in sheet) / filled / disabled | `controls` specimen + sheet | Implemented (M) |
| State | empty (with action) / loading (3 skeletons) / error + retry / offline / pending | `operational` specimen | Implemented (H: 02) |
| State | conflict / failed + retry / completed / cancelled / reversed | `resolution` specimen | Implemented (H: 02) |
| State | interactive retry (×2) | `[data-retry-demo]` buttons | Implemented (M) |
| Sheet | quick-entry (5 adapted flows) + More sheet | `overlays` mini-stage + composition rail | Implemented (M) |
| Dialog | dirty-guard (alertdialog) / destructive delete (modal) | `overlays` mini-stage + sheet flow | Implemented (M) |
| BottomNavigation | 5 seats, active indicator, auto-short labels | `shell` specimen + composition | Implemented (J, M) |
| Top zone + Avatar | integrated, avatar → profile/settings sheet | `shell` specimen + composition | Implemented (M) |
| Chart | sparkline / planned-vs-actual / target meter / trend marker + text alternatives | four `chart-figure` specimens | Implemented (H: 02, 15) |

## 3. Test Composition (`#view-composition`, template `#tpl-composition`)

| Requirement | Status |
|---|---|
| Exactly one PrimaryValueBlock on canvas | Implemented (H: 03) |
| One QuickActionRail, 5 actions, إضافة بيع first | Implemented (J peeks, M) |
| One MetricGroup (3 rows, 2 dividers) | Implemented (H: 03) |
| One comparison pair | Implemented (H: 03) |
| ≤3 surfaces / 2 semantic families / 2 colored numbers / no repeated key value / one vertical scroll owner | Implemented (constructed + reviewed; see self-critique §4) |
| Full interaction contract: sheet → loading → completion → immediate value update; dirty guard; focus return | Implemented (M: measured value changes) |

## 4. Verification (`#view-verification`)

| Item | Location | Status |
|---|---|---|
| Device previews 320×568 / 360×640 / 390×844 / 430×932 (RTL) | `#vf-320…#vf-430` | Implemented (J, H: 12, 13) |
| Geometry-only LTR clone | `#vf-ltr` | Implemented (J, H: 14) |
| Text scale 100/130/200 (root font) | scale control | Implemented (J) |
| Reduced motion toggle (+ auto from `prefers-reduced-motion`) | motion control | Implemented (J, H: 11) |
| Grayscale color-independence check | gray control | Implemented (H: 10, 15) |
| Live peek measurement table | `#peek-results` | Implemented (J: 16/56/86/30) |
| In-lab audit engine (9 checks) | `#audit-results`, `window.MicroAudit` | Implemented (J: all pass) |

## 5. Explicitly not implemented (documented-only)

| Item | Where documented | Why |
|---|---|---|
| 28px value fallback for >9-character values | component contracts (PrimaryValueBlock) | No such value occurs; composition stays 32px |
| 20-row batched list with prefetch-at-5 | component contracts + SPEC §6.12 | The lab proves the 3-skeleton loading state; a full batched list is data behavior, and the composition is intentionally small (SPEC §11) |
| Real screen-reader session | self-critigue §6 | Live regions/roles/labels are wired and DOM-verified; no NVDA/VoiceOver in this environment |
| Physical drag-to-dismiss gesture test | verification report §7 | Implemented with pointer events + reduced-motion tap threshold; exercised via Escape/scrim equivalents |
| Tailwind v4 theme + React adapters | `03-design-system-engineering/` | Optional integration adapters, documented for the later integration phase |
| Full offline save→send flow | state family exhibits | States shown individually (offline/failed/completed); a sync engine is out of scope for a visual library |
