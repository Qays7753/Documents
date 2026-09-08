# Micro — Component Contracts

Canonical contracts for every family implemented in `micro-component-visual-library.html`.
"Implemented" means: a visible, interactive instance exists in the lab at the stated
location. Class names reference the extraction-ready `.mc-*` layer; tokens resolve
exclusively through `tokens.css`.

Locations shorthand: **C** = Components view section id, **T** = Test Composition,
**V** = Verification view (live 320/360/390/430 clones of T).

---

## 1 · PrimaryValueBlock — `.mc-primary-value`

| Field | Contract |
|---|---|
| name | PrimaryValueBlock |
| purpose | Show the one number that answers the owner's first question ("كم عندي الآن؟") before anything else. |
| when to use | Once per composition, as the first money statement after the integrated top zone. |
| when not to use | Never inside a card/surface; never twice on one screen; never for secondary metrics (those are MetricRow). |
| anatomy | `label` (15px/400 ink-muted) → `figure` (32px/600 ink-strong, tabular lining, `bdi dir="ltr"` numeric run + 15px/500 unit) → optional `delta` (icon + signed value + 14px context) or optional `state` chip (sunken pill, 14px). |
| content hierarchy | number → label → delta/state. The number is always the largest element on screen. |
| sizes | value 32px/1.15; unit 15px; delta 14px/500 + 14px context; state chip height ~24px. |
| spacing | block padding 4/0/16 (12 to next section); label→figure 4px; figure→delta 6px. |
| radius | none (canvas block). State chip radius-full. |
| surface role | **canvas** — by definition, never a surface. |
| brand role | none (ink-forward). |
| semantic color role | delta positive value in `--positive`; negative variant in `--danger`; at most one colored number here per composition. |
| variants | basic · with-state · with-delta · unavailable (`is-unavailable`: 18px/500 "غير متوفّر", never `0`). |
| states | value-known; unavailable (with 14px reason, e.g. "لم يُربط بعد"). |
| interaction and motion | non-interactive by itself; value updates land instantly (no count-up — motion law). |
| RTL behavior | numeric run isolated `bdi dir="ltr"`; unit renders inline-start-adjacent (left of the number); sentence context RTL. |
| accessibility | `aria-label` on section ("رصيد الصندوق الآن"); tabular figures keep column alignment; contrast ink-strong on canvas 15.9:1. |
| Arabic copy examples | «رصيد الصندوق الآن» / «تحصيلات اليوم» / «رصيد حساب البنك». |
| Micro operational examples | daily cash balance 431.100 د.أ with «+86.250 عن أمس»; collections today; bank balance as unavailable. |
| responsive behavior | identical at 320–430 (single column, no wrap at 200% text scale — verified). |
| known limitations | v1 has no compact variant for embedded contexts (by design — it owns the screen). |
| implemented at | C `mx-value-title`, T top (after top zone), V all frames. |

## 2 · MetricGroup — `.mc-metric-group`

| Field | Contract |
|---|---|
| purpose | Hold 2–5 secondary values that belong to one question (اليوم/الأسبوع) in ONE surface with aligned rows. |
| when to use | Daily/weekly summaries directly under the QuickActionRail. |
| when not to use | Never one card per metric; never >5 rows (split or link out); not for primary value; not for operational history (OperationalRow). |
| anatomy | surface (white, radius 16, padding 4/16/8) → head (14px/500 title + hairline) → 2–5 MetricRows. |
| content hierarchy | rows are peers; label right, value left-aligned column (end), qualifier under label. |
| sizes | see MetricRow; group min-height none (content-driven). |
| spacing | group margin-bottom 24; head padding 12/0/8; rows padding 10/0. |
| radius | 16 (`--radius-lg`). |
| surface role | `surface` (plane 1 — the content plane). |
| brand role | none. |
| semantic color role | per-row via value/qualifier only; ≤2 semantic families per composition. |
| variants | titled · untitled (headless). |
| states | n/a (rows carry states). |
| interaction and motion | rows optionally pressable (whole-row tap → detail) with 8% press veil, 80ms. |
| RTL behavior | grid `label|value` mirrored automatically via logical properties; value column end-aligned. |
| accessibility | `aria-label` = group title; hairline is decorative. |
| Arabic copy | «ملخص اليوم» / «عينة الحالات». |
| Micro examples | مبيعات/مصاريف/تحصيلات/مستحقات اليوم (T); weekly variants (C). |
| responsive | rows never clip; values `white-space: nowrap` — verified at 320/200%. |
| limitations | one MetricGroup per composition (two only with documented reason — not used in T). |
| implemented at | C `mx-metric-title`, T after rail. |

## 3 · MetricRow — `.mc-metric-row`

| Field | Contract |
|---|---|
| purpose | One label + one aligned number (+ optional qualifier) on a single line. |
| when to use | Inside MetricGroup; anywhere a compact secondary figure is needed. |
| when not to use | Not for the primary value; not as a list row (that's OperationalRow). |
| anatomy | `label` (grid area 1) · `value` (area 2, end-aligned, tabular) · optional `qualifier` (area 3 under label). |
| content hierarchy | value visually dominant (15px/500) over label (15px/400); qualifier 14px muted. |
| sizes | 15px label/value; qualifier 14px; unit 14px. |
| spacing | row padding 10/0; row-to-row 2 (via padding) — no hairlines between rows (divider budget). |
| radius | none. |
| surface role | inherits group surface. |
| brand role | none. |
| semantic color role | `is-danger` value (cash-out direction), `is-positive` (favorable), `is-attention` qualifier (icon + warning), `is-unavailable` text value. |
| variants | plain · positive-qualifier · attention-qualifier · colored-value · unavailable. |
| states | value-known · unavailable («غير متوفّر» — never 0). |
| interaction and motion | press veil when row is a button; none when static. |
| RTL behavior | value column at inline-end; qualifier wraps under label with `overflow-wrap`. |
| accessibility | label and value in same row read linearly by SR; sign carried by character (−/+) not color. |
| Arabic copy | «مبيعات اليوم» · «مصاريف اليوم» · «مستحقات متأخرة». |
| Micro examples | «مصاريف اليوم −182.500 د.أ · 3 مصاريف» (T); «صافي الأسبوع — غير متوفّر» (C). |
| responsive | qualifier may wrap to second line at 200% — verified no clipping. |
| limitations | no inline sparkline variant in v1 (charts are separate primitives). |
| implemented at | T metric group, C `mx-metric-title`. |

## 4 · CompactTile — `.mc-compact-tile`

| Field | Contract |
|---|---|
| purpose | A genuine comparison PAIR — two figures the owner must see side by side. |
| when to use | exactly one pair per composition, e.g. نقدي مقابل آجل. |
| when not to use | never as a generic mini-card grid; never 3+ tiles; not for navigation (that's QuickActionRail). |
| anatomy | two tiles: `label` 14px muted → `figure` 18px/600 tabular + 13px unit. |
| content hierarchy | figures equal weight (that is the point of a comparison). |
| sizes | tile flex 1; height content-driven (~64px). |
| spacing | 12 padding; 8 tile gap. |
| radius | 12 (`--radius-md`). |
| surface role | surface, 1px line-soft border. |
| brand role | none. |
| semantic color role | optionally one tile's figure semantic (not used in T — budget). |
| variants | pair only. |
| states | n/a. |
| interaction and motion | static (v1); tap-to-filter is a future adapter. |
| RTL behavior | order follows reading direction; first (نقدي) appears right. |
| accessibility | `role="group"` + aria-label on the pair. |
| Arabic copy | «نقدي اليوم» / «آجل اليوم». |
| Micro examples | 520.000 نقدي مقابل 122.750 آجل اليوم. |
| responsive | tiles split 50/50 at every width. |
| limitations | comparison pair only — the library refuses the dashboard-grid pattern. |
| implemented at | C `mx-tile-title`. |

## 5 · QuickActionRail — `.mc-rail`

| Field | Contract |
|---|---|
| purpose | The 4–5 stable, one-tap capture actions (بيع، تحصيل، مصروف، شراء، دفعة) — first action first. |
| when to use | once per composition, directly under the PrimaryValueBlock. |
| when not to use | not a navigation bar; not a category filter; never vertical; never >5 tiles. |
| anatomy | horizontal `ul.mc-rail-scroll` (RTL scroll, proximity snap) of `li > button.mc-rail-tile` (icon 24 + label 13, 8px gap). |
| content hierarchy | first tile = primary action and the ONLY tinted tile (`brand-tint`). |
| sizes | tile 88×92 EXACT; icon 24; label 13px/500 (spec-pinned exception to the 14px Arabic floor); rail start padding 16; end padding 4; edge fade 24px. |
| spacing | tile gap 8. |
| radius | 12. |
| surface role | tiles are `surface` (the rail itself is canvas); the tinted tile is `brand-tint` — counted as the one brand-family moment. |
| brand role | tile 1 tinted + brand-ink icon/label; all other tiles ink-muted on white. |
| semantic color role | none (actions are neutral; semantics belong to data). |
| variants | tinted-first · plain. |
| states | press (8% veil, 80ms); focus-visible ring. |
| interaction and motion | horizontal scroll + proximity snap (snapport preserves the 16px start padding via `scroll-padding-inline-start`); opens sheets; edge fade toward scroll end. |
| RTL behavior | scrolls right-to-left natively; fade at inline-end; directional icons mirror per registry. |
| accessibility | `nav[aria-label="إجراءات سريعة"]`; buttons 92px tall ≥44px; labels always visible (no icon-only). |
| Arabic copy | «إضافة بيع» «تحصيل دين» «إضافة مصروف» «إضافة شراء» «تسجيل دفعة». |
| Micro examples | exactly those five, lab examples (not a final nav map). |
| responsive | locked geometry; measured next-tile peek: 16px @320 (documented exception), 56/86/30 @360/390/430 (device-true; 14/54/84/28 inside the lab's 2px-bordered frames). |
| limitations | peek at 320 is a documented responsive exception, not a bug. |
| implemented at | T under primary value, C `mx-rail-title`, V all frames (measured). |

## 6 · OperationalRow — `.mc-operational-row`

| Field | Contract |
|---|---|
| purpose | One real operational event (sale, collection, expense, purchase, settlement, threshold) scannable in a line. |
| when to use | repeating lists of today's/period's operations. |
| when not to use | not for aggregates (MetricRow); not for settings; not inside MetricGroup. |
| anatomy | `ic` (40px sunken square, 20px icon) · `main` (title 15/500 + qualifier 14) · `side` (amount 15/500 tabular + unit + time 13, or status chip). |
| content hierarchy | title → amount → qualifier → time/chip. Amount column end-aligned across rows. |
| sizes | row min-height 56; icon container 40; amount nowrap. |
| spacing | 12 gaps; row-to-row 8 inside the single grouped surface. |
| radius | 12 (press veil radius); group 16. |
| surface role | rows live on canvas OR within ONE grouped `surface` (T uses the grouped surface so press veil contrast holds). |
| brand role | none. |
| semantic color role | icon container tinted semantic (`is-positive/danger/warning/info`) + optionally semantic-colored value; ≤2 families per panel. |
| variants | financial (signed amount) · follow-up (status chip, no amount) · static (non-pressable demo) · cancelled (`is-cancelled`: muted value + title, «ملغاة» chip). |
| states | default · pressed · pending chip («بانتظار») · cancelled. |
| interaction and motion | whole-row button; press veil 80ms; opens detail (sheet in product); quiet completion updates appear here instantly. |
| RTL behavior | side column at inline-end; signed amounts isolated `bdi dir="ltr"` (U+2212 minus); mirror-registry icons only. |
| accessibility | row is a `<button>` with full text (title + qualifier + amount + time read linearly); min 56px target. |
| Arabic copy | «شراء من مستودع زهران» · «تحصيل من خالد الحوراني» · «تسوية شركة برق للتوصيل». |
| Micro examples | the four T rows + demo prepend rows («مصروف نقدي −12.500 · الآن») written by the save demos. |
| responsive | qualifier wraps; amount never wraps or clips (verified 320/200%). |
| limitations | long qualifiers wrap to two lines by design (content-driven height). |
| implemented at | T list, C `mx-oprow-title` (two panels), dialog demo row, retry-ops result rows. |

## 7 · Button — `.mc-btn` (+ `.mc-iconbtn`)

| Field | Contract |
|---|---|
| purpose | Commit an action; the primary variant is the ONE filled brand-family action per viewport. |
| when to use | sheets/dialogs footers; compact inline actions; icon-only affordances. |
| when not to use | not for navigation links (quiet variant only); destructive NEVER fires without a dialog confirm. |
| anatomy | label (± 20px icon ± 18px spinner) centered; 48px min-height; radius 12. |
| content hierarchy | one verb-first label ≤2 words. |
| sizes | default 48; `--compact` 44; icon-only 44×44. |
| spacing | padding 0/20 (compact 0/14); 8 gap between icon and label. |
| radius | 12. |
| surface role | primary = filled `brand-ink`; secondary = `surface` + line-strong border; quiet = transparent. |
| brand role | primary fill `brand-ink` + `on-brand` text (6.1:1); the atmosphere color is NEVER a text button. |
| semantic color role | destructive = filled `--danger` + white; completion = positive-tint ground + positive icon + ink text. |
| variants | primary · secondary · quiet/text · destructive · icon-only · compact modifier. |
| states | default · pressed (8% veil, 80ms) · focused (2px brand-ink ring, offset 2) · loading (spinner + «جارٍ…», pointer-events off, size locked) · completed (✓ + «تم…», positive-tint) · disabled (sunken + ink-disabled, sub-AA by intent, non-interactive). |
| interaction and motion | all state swaps 120–200ms standard easing; no bounce; completion persists ≥1.1s before sheet closes. |
| RTL behavior | label centered (direction-neutral); icon-leading order flips with reading direction. |
| accessibility | `aria-disabled` + `tabindex="-1"` for loading/disabled; focus-visible always rings; spinner `aria-hidden` with text label retained. |
| Arabic copy | «حفظ المصروف» · «تأكيد التحصيل» · «إعادة المحاولة» · «نعم، إلغاء الفاتورة». |
| Micro examples | every sheet footer; retry in the error state; dialog actions. |
| responsive | full-width in sheet/dialog footers; auto width in matrices. |
| limitations | no small/16px button variant (44px floor is absolute). |
| implemented at | C `mx-btn-title` (full matrix incl. live cycle), all sheets, dialog, states. |

## 8 · Input — `.mc-field` / `.mc-input`

| Field | Contract |
|---|---|
| purpose | Capture text, money, search, dates, and choices with Arabic-first behavior. |
| when to use | inside sheets and forms; search in lists. |
| when not to use | switch only for immediate settings; not for destructive confirms (dialog). |
| anatomy | `field-label` (14/500) → input shell (48px, line-strong, radius 12) containing control + affixes (unit د.أ / icons / clear). |
| content hierarchy | label above; value dominant; error message below (14px danger + alert icon). |
| sizes | height 48; unit 14; error 14. |
| spacing | field gap 16 (sheet body); affix padding 12. |
| radius | 12. |
| surface role | `surface` shell; disabled = sunken. |
| brand role | focus border `brand-ink` (via :focus-within). |
| semantic color role | error = danger border + danger helper text (never color-only: icon + text carry it). |
| variants | text · amount (dir=ltr, inputmode=decimal, tabular) · search (icon + clear 44px) · date (text, dir=ltr, DD/MM/YYYY, calendar affix) · select (native, chevron) · segmented (44px options) · tab · checkbox (22px box) · switch (48×28, immediate only). |
| states | default · focus (brand-ink border) · error (`is-error` + aria-invalid + describedby) · disabled. |
| interaction and motion | border color 120ms; segmented/thumb 120ms; switch dot 120ms translate. |
| RTL behavior | amount/date controls `dir="ltr"` end-aligned inside RTL shell; unit at inline-end; clear button at inline-end. |
| accessibility | label element wraps control; error wired via `aria-describedby`; checkbox/switch keep native inputs visually-hidden but focusable. |
| Arabic copy | «المبلغ» «الوصف» «التصنيف» «التاريخ» «ابحث عن عميل أو فاتورة…». |
| Micro examples | expense sheet (amount 0.000 placeholder, 3-decimal fils), collect sheet customer select with «عليّه 300.000». |
| responsive | full-width; never clips at 200% (verified). |
| limitations | date is a formatted text field + affix (native pickers vary by platform — adapter decision); no multi-line textarea in v1. |
| implemented at | C `mx-input-title`, `mx-choice-title`, expense/collect/sale/purchase/payment sheets. |

## 9 · State — `.mc-state`

| Field | Contract |
|---|---|
| purpose | Tell the truth about data: empty, loading, failed, pending, conflicted… with an action when one exists. |
| when to use | list containers, sync surfaces, anywhere truth must be shown. |
| when not to use | never as decoration; no toasts as sole proof; no illustration theatre. |
| anatomy | optional 20px icon + `title` (15/500) + `line` (14 muted) + optional action button/chip. |
| content hierarchy | title → one explanatory line → action. |
| sizes | card padding 16; chip 24px height. |
| spacing | 4 internal gaps; 8 to action. |
| radius | 12 card; full chip. |
| surface role | surface card (empty variant: canvas, line-based, no card). |
| brand role | none. |
| semantic color role | icons/chips per family: positive=completed, danger=failed, warning=conflict, info=pending/reversed; offline uses cloud icon (ink). |
| variants | empty (line-based) · loading (3 skeletons, sunken, shimmer 1.2s, zero layout shift) · error+retry · offline-local-save · pending · conflict · failed · completed · cancelled (neutral chip) · reversed (info chip + undo icon). |
| states | each is a state. |
| interaction and motion | retry = one manual attempt after first failure (demo: fail once → retry → skeletons → rows); shimmer disabled under reduced motion. |
| RTL behavior | icons lead at inline-start; skeleton shimmer runs RTL (dedicated keyframes). |
| accessibility | `aria-live` announcements via live region; skeleton list `aria-label="جارٍ التحميل"`. |
| Arabic copy | «لا عمليات بعد لهذا اليوم» · «تعذّر تحميل العمليات» · «محفوظ على الجهاز» · «بانتظار تأكيد التسوية» · «مبلغان مختلفان للفاتورة» · «تم التحصيل». |
| Micro examples | all ten, wired where sensible (retry is live). |
| responsive | single column, no clipping. |
| limitations | conflict resolution UI (choose amount) is represented, not implemented. |
| implemented at | C `mx-state-title` (all ten), retry demo live. |

## 10 · Sheet — `.mc-sheet`

| Field | Contract |
|---|---|
| purpose | Own all data-entry flows (بيع/تحصيل/مصروف/شراء/دفعة) — thumb-reachable, scrimmed, dismissible. |
| when to use | any capture or review flow ≤ a few fields. |
| when not to use | irreversible decisions (dialog); long wizards (future step-sheets). |
| anatomy | grab handle (36×4) → head (title 16/600 + 44px close) → body (fields, scrollable) → foot (primary + quiet, full-width). |
| content hierarchy | title → first field (amount first — the frequent case) → actions. |
| sizes | max-height 86% of phone screen; corner radius 24 top. |
| spacing | body 8/16; foot 8/16/24. |
| radius | 24 top corners. |
| surface role | surface with derived elevation shadow (ink 12%, 24px blur) + 45% scrim — scrim alone does not define the edge (2.96:1). |
| brand role | primary CTA is the one filled brand action; grab handle line-strong. |
| semantic color role | error fields inside sheets; completion state on the CTA. |
| variants | reference (expense: 4 fields) · compact (amount + choice). |
| states | closed (translateY 100%) · opening 240ms standard · open · dragging (transform follows pointer) · closing 180ms exit · reduced-motion = opacity fade only. |
| interaction and motion | open from any trigger; close via ✕, scrim tap, Escape, or drag-past-120px; focus moves to first data field; focus returns to trigger on close; scroll owner locked. |
| RTL behavior | logical paddings; sheet slides vertically (RTL-safe by construction). |
| accessibility | `role="dialog" aria-modal`, labelled title; Tab trapped within; Esc closes; scrim is pointer target with no text. |
| Arabic copy | «إضافة مصروف» · «تحصيل دين» · «تسجيل دفعة». |
| Micro examples | five sheets, all wired: save → loading → «تم…» → metrics/list update instantly → auto-close. |
| responsive | full phone width; fields stack; verified at 320/200%. |
| limitations | no multi-step; drag-dismiss threshold fixed at 120px. |
| implemented at | overlay layer of every phone screen (5 sheets), triggered from T rail + C section. |

## 11 · Dialog — `.mc-dialog`

| Field | Contract |
|---|---|
| purpose | Irreversible/destructive confirmations and decision-critical conflicts — never data entry. |
| when to use | «إلغاء الفاتورة؟», conflict resolution choices. |
| when not to use | forms (sheet); informational notices (inline state). |
| anatomy | title (16/600) + description (14) + actions (destructive filled + quiet تراجع). |
| content hierarchy | question → consequence stated in money terms → actions. |
| sizes | inset 24 from screen edges; centered at 50%. |
| spacing | 24/20/20 padding; 8 action gaps. |
| radius | 16. |
| surface role | surface + shadow + scrim 45% (z 350/400 above sheets). |
| brand role | none (destructive uses danger family). |
| semantic color role | destructive action filled danger; quiet escape. |
| variants | destructive-confirm. |
| states | in 160ms / out 120ms (opacity + 8px rise); reduced-motion fade. |
| interaction and motion | scrim tap / Esc / تراجع cancel; confirm applies state change + live-region announcement. |
| RTL behavior | centered; buttons full-width stacked. |
| accessibility | `role="alertdialog"` + labelled + described; focus lands on confirm; returns to trigger. |
| Arabic copy | «إلغاء فاتورة الشراء؟» «نعم، إلغاء الفاتورة» «تراجع». |
| Micro examples | cancelling the زهران invoice → row flips to «ملغاة» + reversal note. |
| responsive | max content width by 24px insets; verified 320. |
| limitations | two-action max (spec). |
| implemented at | C sheet&dialog section, live confirm. |

## 12 · BottomNavigation + integrated TopZone — `.mc-bottomnav`, `.mc-topzone`

| Field | Contract |
|---|---|
| purpose | The ONLY persistent chrome: four destinations + «المزيد»; the top zone is content, not chrome, with the single Avatar profile entry. |
| when to use | every product screen. |
| when not to use | never a fifth domain label at 320 (labels clip — measured); never a detached top app bar. |
| anatomy | nav: 4 items (indicator 24×3 + icon 20 + label 14/500, ink) edge-to-edge on surface with top hairline. TopZone: 44px avatar (brand-tint, brand-ink initial) + greeting 15/500 + meta 14. |
| content hierarchy | active item: ink-strong + 600 label + brand-atmosphere indicator; others ink-muted. |
| sizes | nav item min 44; total ~68 + safe inset. |
| spacing | nav padding 6/4/8; topzone gap 12, block padding 8/0/16. |
| radius | 0 (edge-to-edge, spec). |
| surface role | surface; avatar brand-tint (identity moment — counts as the brand budget when the rail tile is not used… in T the tinted rail tile is the moment and the avatar is a secondary tinted element at 44px; documented as acceptable because avatar tint is an identity mark, not an action surface). |
| brand role | indicator bar atmosphere; avatar tint. |
| semantic color role | none. |
| variants | live (sticky bottom in scroll) · static (matrix). |
| states | active · inactive · pressed veil. |
| interaction and motion | tap switches active (demo-level); sticky positioning, no transition on the bar itself. |
| RTL behavior | item order follows reading direction (الرئيسية rightmost in RTL); icons never mirror (objects). |
| accessibility | `aria-current="page"`; labels always visible 14px; 44px targets; hairline decorative. |
| Arabic copy | «الرئيسية» «العمليات» «العملاء» «المزيد» / «صباح الخير، أبو النور». |
| Micro examples | T live nav + topzone with «بقالة النور · الاثنين 08/09/2026». |
| responsive | labels fit at 320 (measured during design: 4×≤64px slots); verified no clip. |
| limitations | nav switching is demo-state only (no screen map by spec). |
| implemented at | T (live), C `mx-nav-title` (anatomy). |

## 13 · Chart primitives — `.mc-chart`

| Field | Contract |
|---|---|
| purpose | Small, honest, directly-labelled data pictures: sparkline, planned-vs-actual, target meter, trend marker. |
| when to use | inside metric contexts and review surfaces. |
| when not to use | never as hero decoration; never tooltip-dependent (direct labels only); never color-only series. |
| anatomy | head (title 14 + value 16/600) → SVG (viewBox scaled, non-scaling strokes) → visible text alternative (14 muted) + `role="img"` aria-label. |
| content hierarchy | the number in the head first; the shape second. |
| sizes | sparkline 280×64; comparison 280×120; meter 8px track; labels 12px (digits only). |
| spacing | chart padding 12/16; alt divider hairline. |
| radius | 12 card; full meter. |
| surface role | surface card. |
| brand role | none (ink lines). |
| semantic color role | meter fill `--positive` (goal progress); planned line dashed ink-muted vs actual solid ink-strong (texture, not color, distinguishes). |
| variants | sparkline+direct peak marker («690.000») · planned-vs-actual with two direct labels · target meter (62%, end target tick). |
| states | static (v1). |
| interaction and motion | none (deliberate — no hover reliance). |
| RTL behavior | **time axis stays LTR inside the chart** (oldest left, newest right) while all text remains Arabic RTL; charts never mirror. |
| accessibility | every chart: `role="img"` + full-sentence `aria-label` AND a visible caption line with the same numbers. |
| Arabic copy | «مبيعات 7 أيام» · «مبيعات سبتمبر: مخطط مقابل فعلي» · «هدف تحصيلات سبتمبر». |
| Micro examples | sales week 512.000→642.750 (peak 690.000 يوم 06/09); cumulative actual 1,040.250 vs plan 1,200.000; 1,550.000 من 2,500.000 (62%). |
| responsive | SVG scales width 100%; strokes non-scaling; verified 320. |
| limitations | no interaction, no legend (direct labels replace it at 320 per spec). |
| implemented at | C `mx-chart-title` (three demos + trend marker). |

---

### Cross-family rules (binding)

1. Composition budget: 1 PrimaryValueBlock · 1 rail · 1 MetricGroup · 1 comparison pair · ≤3 visible surfaces · ≤3 dividers · ≤2 semantic families · ≤2 colored numbers · 1 filled brand action · 1 tinted rail tile · one vertical scroll owner.
2. Money: English digits, `bdi dir="ltr"`, U+2212 minus, 3-decimal fils, thousands comma, unit «د.أ» outside the isolated run — never "JOD".
3. Unknown ≠ unavailable ≠ zero ≠ empty; never render unknown as 0.
4. The negative sign is the primary direction signal; color is secondary.
5. Light mode only; no dark tokens, no `.dark`, no `prefers-color-scheme` anywhere.
