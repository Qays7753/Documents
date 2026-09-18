# Accessibility & RTL Evidence — Micro Bold Modular V1

All checks below are design-level evidence from the isolated prototype. They are **expert verifications of the concept artifacts**, not assistive-technology audits of a shipping product. The three directions and the refined candidate share one DOM engine, so evidence applies to C1, C2, C3, and C2R unless noted.

## 1. Contrast (WCAG 2.2)

- **Method:** programmatic computation (`scripts/contrast.py`), exact WCAG relative-luminance formula; ratios rounded to two decimals, never rounded into passes.
- **Coverage:** 213 pairs per the shared set (light + dark): body/secondary/tertiary text on canvas/surface/group/tints; state text on state tints; button text on fills; large hero values; icons; tinted-field usage; dark-mode component treatments (active nav, filled chips, logo mark, C2 band, inverted tile).
- **Result: 213/213 PASS** across C1, C2, C3 (light and dark). Full tables: `reports/contrast-evidence.md` + per-direction `tokens.json`.
- Revisions forced by measurement (recorded, not hidden): C3 brand deepened `#D2502A → #C4481E` (4.27 → pass); dark-mode component corrections in all three stylesheets.

## 2. Touch targets

- Primary controls (QAB items, buttons, choices, nav items, menu rows) are ≥44–48px by construction (`min-height` rules); measured via rendered layout.

## 3. Critical state = text + non-color cue

- Every state component renders icon + text (+ shape/progress where relevant). Verified structurally (generator emits icon+label in every chip) and visually.
- **Grayscale/color-blind proof:** critical home screens rendered in grayscale (`exports/grayscale/`) — positive/incomplete/negative remain distinguishable via +/− symbols, check/warning/x icons, and the progress rail. Visual QA confirms no state depends on color alone.

## 4. Visible focus

- `:focus-visible` defined per direction (C2/C2R: 3px brand outline, offset 3px). Proof: keyboard Tab focus captured on the refined sale form (`exports/focus-proof/`) showing the ring on the first focusable control.

## 5. 200% text stress

- Applied via `?scale=text200` (doubles all rem-based text). Measured on home, forms, and success screens for all directions: **no horizontal scrolling** (scrollWidth == viewport width at 390px); tasks remain completable (labels visible, buttons reachable). Proofs: `exports/responsive/*-text200.png`.

## 6. Responsive checkpoints

- 320 / 390 / 430 px rendered for home-positive and sale-success in all three directions (`exports/responsive/`). No horizontal overflow at any width; layouts adapt via fluid flex/grid and the 350px small-screen adjustments (single-column figures, wrapped QAB, icon-only top links).

## 7. RTL integrity

- Documents are `lang="ar" dir="rtl"`; logical properties (`inline-start/end`) throughout the stylesheets.
- **Latin digits isolated:** every amount renders inside an LTR-isolated mono span (`unicode-bidi: isolate`) — mixed runs like «أم محمد عليها 25.00 د.أ منذ 3 أيام» display correctly (verified visually on all critical screens).
- **Non-directional icons never mirrored;** directional icons (logout/back/undo) drawn RTL-correct from the start; expense/collect arrows are vertical (RTL-ambiguous by design).
- `د.أ` unit follows the number consistently; dates use one `DD/MM/YYYY` convention.
- Mixed content demonstrated: Arabic names (أم محمد، سارة الخطيب، حلويات ليان), Latin numerals, currency, `#142`, dates — across home, finance, work, forms, and success screens.

## 8. Bottom-navigation occlusion

- The QAB was measured against the sticky nav at 390×844 for every direction on both home states: QAB bottom 760–762px vs nav top 764–765px → **fully above obstruction**. This directly addresses the confirmed current problem in file 10.
- Form actions verified clear at scroll-rest (26px gap above nav).

## 9. Reduced motion

- `prefers-reduced-motion: reduce` disables all animations/transitions in every direction stylesheet; the Success Impact pulse falls back to a static highlighted border. Proof renders: `exports/reduced-motion/`. The interactive prototype shortens its saving-state delay under the preference.

## 10. Forms, dialogs, and errors

- Labels remain visible after input (labels outside inputs); amount field is visually dominant (mono, 1.5rem).
- Validation error: message explains problem + recovery, field retains value + focus; `aria-describedby` wiring and `role="alert"` present.
- System error dialog: `role="alertdialog"` with labelled title/description, two actions, backdrop dismiss, and the preserved form underneath proves «مدخلاتك ما زالت موجودة».
- Sheets: handle + close affordance + backdrop click-through documented.

## 11. Known limitations (honest record)

- No screen-reader walkthrough (VoiceOver/TalkBack) was performed — focus/ARIA patterns are specified and structurally present but untested with AT.
- Color-vision checks were simulated via grayscale rendering; full CVD simulations (protan/deutan) not run.
- 200% proof uses text scaling only; OS-level font scaling and zoom interactions are implementation-stage concerns.
- The five-second comprehension estimates are expert inspections, not user timings.
