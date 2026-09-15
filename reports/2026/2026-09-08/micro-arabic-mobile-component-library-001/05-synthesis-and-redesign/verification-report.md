# Verification Report — Micro Component Visual Library

Run `20260908T133450Z-16d11` · Headless Chromium (agent-browser 0.35.0) at 1400×1000/1080 · IBM Plex Sans Arabic installed locally for faithful rendering · every value below is measured, with the local path of its screenshot evidence.

## 1. Viewport × direction × text scale (RTL default)

| Test | Condition | Observed result | Status |
|---|---|---|---|
| VP-01 | Composition 320×568 RTL | No horizontal scroll (scrollWidth ≤ clientWidth); order unchanged; first follow-up row above the fold with documented 320-only rhythm compression | Pass (J) |
| VP-02 | Composition 360×640 RTL | No overflow; peek 56px | Pass (J) |
| VP-03 | Composition 390×844 RTL | No overflow; peek 86px | Pass (J) |
| VP-04 | Composition 430×932 RTL | No overflow; peek 30px | Pass (J) |
| VP-05 | 320 fold | First warning row (شركة التوصيل السريع — بانتظار التحويل) reachable before the fold after container-query compression (32→24-class steps, all from the scale) | Pass (J) |
| VP-06 | Screen edge | 16px/16px measured (inline-start/inline-end) via `.metric-group` box on every frame | Pass (J) |
| DI-01 | LTR geometry check | `#vf-ltr` mirrors via logical properties; nav order flips; numbers stay LTR isolates; chart time axis LTR; no overflow | Pass (J + H) |
| DI-02 | Physical left/right | CSS scan: no physical left/right declarations in component CSS | Pass (scan) |
| DI-03 | Icon mirror registry | Only chevrons carry `.icon-mirror`; semantic icons unmirrored (DOM audit A6); no send/plane glyph exists | Pass (J) |
| TS-01 | 100% (root 16px) | Type roles at 32/15/13 + 14px Arabic floor; tabular-nums on value (computed: `lining-nums tabular-nums`) | Pass (J) |
| TS-02 | 130% (root 20.8px) | Text grows, no clipping | Pass (J) |
| TS-03 | 200% (root 32px) | No overflow RTL or LTR; rail tile grows in height only (width 88/gap 8/padding 16 unchanged) | Pass (J) |
| TS-04 | Long labels at 200% | تحصيل دين، تسجيل دفعة، طحين فاخر 10كغ wrap, none truncate | Pass (H) |
| TS-05 | Nav labels at 320 | All five fit; المبيعات auto-shortens to مبيعات by measured swap (not faked) | Pass (J) |
| MO-01 | Motion durations | Computed: sheet 0.24s, dialog 0.16s, scrim 0.2s (probe elements) | Pass (J) |
| MO-02 | Reduced motion | `data-motion="reduced"`: sheet opens in place (transform = identity); spinner static; skeletons static; state meaning preserved | Pass (J + H) |
| MO-03 | Values never animate | Completion sets textContent directly (1,284.50 → 1,649.50 in one step) | Pass (J) |
| MO-04 | No bounce/spring | Easings from `--mc-ease-*`, none overshoot | Pass (scan) |
| MO-05 | Press overlay | 8% ink at 80ms via shared `.pressable` on tiles, buttons, rows, nav seats, avatar | Pass (M) |

## 2. QuickActionRail measurements (JS `getBoundingClientRect`)

| Width | Measured peek | Expected | Status |
|---|---|---|---|
| 320px | **16px** | 16px (documented exception) | Pass |
| 360px | **56px** | ≥28px | Pass |
| 390px | **86px** | ≥28px | Pass |
| 430px | **30px** | ≥28px | Pass |

Geometry locked at all widths: tile 88×92(min), gap 8, padding 16, label 13px. Two engineering fixes were required to reach exactness and are logged in the decision log (#5, #6): `scroll-padding-inline: 16px` (Chrome's initial snap had consumed the start padding) and replacing the frame's 1px border with a shadow ring (border shifted coordinates by 1px).

## 3. In-lab audit engine (runs on load + on demand)

All nine checks pass: no horizontal overflow; 16px edges; **minimum touch target 44px** (after raising the avatar to a 44×44 hit area and the metric-group header action); no Latin currency code in the UI; currency outside LTR isolates; no unresolved placeholders; mirror registry clean; motion durations from tokens; tabular figures on the primary value; nav labels fit. Results are exposed as `window.MicroAudit` and rendered into the Verification view table.

## 4. Interaction contracts (exercised)

| Contract | Sequence | Result |
|---|---|---|
| Sheet entry | Tile إضافة بيع → sheet 240ms, scrim 200ms, focus lands on amount input | Pass |
| Loading → completion | CTA → «جاري الحفظ…» 1200ms → «تم تسجيل البيع» dwell 1600ms → close 180ms → cash 1,284.50→1,649.50, sales 465.00→830.00 immediately | Pass |
| Validation | Clear amount → submit → «أدخل مبلغًا أكبر من صفر» with danger border, focus returned to field | Pass |
| Dirty guard | Edit amount → Escape → «تجاهل التغييرات؟» dialog (no silent discard) → «متابعة التعديل» keeps sheet | Pass |
| Focus return | Close sheet via إلغاء → focus returns to the invoking tile (تحصيل دين) | Pass |
| Destructive dialog | Escape ignored (still open); حذف → «تم الحذف — أُضيف قيد عكسي بقيمة 35.00 د.أ» notice; إلغاء tabbable and initially focused | Pass |
| Retry recovery | Failed/error notices → «إعادة المحاولة» → loading → completed («تم الإرسال»/«تم التحميل»); single explicit retry, no auto-retry loop | Pass |
| Selection | Segmented نقدي/آجل, tabs اليوم/الأسبوع/الشهر, switch, checkbox, nav seats all toggle with aria state | Pass |
| Search clear | Typing reveals the 44px clear action; clearing refocuses the input | Pass |
| Reduced motion | Toggle → sheet appears in place (identity transform) | Pass |
| Grayscale | Toggle → statuses and chart series still distinguishable | Pass |

## 5. Screenshot evidence (local paths)

`zed-ai-runs/20260908T133450Z-16d11/05-synthesis-and-redesign/screenshots/`

01-foundation-full · 02-library-full · 03-composition-390-rtl · 04-sheet-open · 05-sheet-completion · 06-dirty-guard-dialog · 07-delete-dialog · 08-composition-390-ltr · 09-composition-200-scale · 10-composition-grayscale · 11-sheet-reduced-motion · 12-verification-frames · 13-vf-320-rtl · 14-vf-390-ltr · 15-charts-grayscale

Vision-model QA passes: composition (Arabic shaping correct, no tofu/clipping, RTL correct), sheet (all elements present, scrim correct), 320 frame (no clipping, peek visible, nav labels fit), library full page (PASS), grayscale charts (planned/actual distinguishable by dash pattern + direct labels). VLM misreads of small Arabic currency marks were cross-checked in the DOM (د.أ confirmed).

## 6. Lab constraints

| Check | Result |
|---|---|
| Opens offline via file:// with zero JS errors (fonts fall back gracefully) | Pass |
| No `{{...}}` placeholders | Pass (scan + audit) |
| Light Mode only — no dark tokens/switching | Pass (scan) |
| No fake system UI inside frames | Pass |
| No raw hex / rejected colors / implementation notes inside the phone composition | Pass (scan + design) |
| Views switch Foundation / Library / Composition / Verification; audit separated from showcase | Pass |
| Composition budget (1 PrimaryValueBlock, 1 rail, 1 MetricGroup, 3 surfaces, 2 families, 2 colored numbers, 1 vertical scroll owner) | Pass (constructed + reviewed) |

## 7. Fixes applied during verification (engineering honesty)

1. Audit initially measured hidden frames (display:none → zero rects) — re-scoped to laid-out frames + re-run on view activation.
2. Chrome's initial scroll-snap consumed the rail's start padding — fixed with `scroll-padding-inline`.
3. Frame border corrupted 1px-exact measurements — replaced with a shadow ring.
4. Avatar hit area 32px — rebuilt as 44×44 hit with 32px visual circle.
5. Metric-group header action 21px — raised to a 44px hit area with compensating negative margin.
6. Deleted-notice lookup searched the wrong ancestor — fixed selector.
7. Currency-audit label contained the literal it was checking for (self-poisoning) — label reworded.

All fixes are part of the shipped build; the numbers in this report were produced by the fixed build.
