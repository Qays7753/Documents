# AGENT-4 Report — Prototype v1 Coverage Plan (Micro Standard v2 Reconciliation, 2026-09)

**Agent:** Agent 4 — Prototype Coverage Planner.
**Task ID:** AGENT-4.
**Mode:** Read-only analysis. No repository file was modified, created, or deleted by this agent. The only writes produced by this agent are this report file and the worklog append.
**Product of this report:** a precise BUILD SPECIFICATION for Prototype v1 (scenes, coverage, tokens, vocabulary, validation, anti-contamination). The prototype itself is NOT built here.

---

## 0. Files read (mandatory reading, cited)

1. `/home/z/my-project/worklog.md` — read first (run header, SHAs, rules; Task 1 entry only at time of reading).
2. Context pack at `/home/z/my-project/recon-work/wt-context/planning/micro-standard-v2-reconciliation-context-2026-09/`:
   - `OWNER_UNIFIED_DECISION_REGISTER.md` (80 lines; U-01…U-20; the ten contract additions that enter the 29; the no-harm gate).
   - `EXECUTION_PROMPT_CONTEXT.md` (370 lines; five-agent model; Phase 4 Prototype v1 requirements; upload policy; stop conditions).
   - `REFERENCE_ZAI_FLASH_REPORT.md` — §6 Standard contract inventory (§6.2 palette 18 hex + 2 alpha derivatives; §6.3 named action classes; §6.4 component contracts incl. row `row-amt` 15/600 mono end-aligned `dir="ltr"` isolate, divider inset 72px, ≤3px edge stripe, sheet 84→94% 240/180ms, chip 36/44, FAB 56 @ 80px gutter, value zone + 3 honest voids, period chip) and §15 What must be rejected from Prototype v0 (gallery demo vocabulary Received/In progress/Moved/Returned/Ready/Sent/Closed; retired hexes; no dark mode; Terracotta never a data color). Also read: §5 (Micro inventory), §7 (gap matrix), §14 (preserved), §16–§18.
   - `REPORTS_RECONCILIATION.md` (36 lines; Flash report = primary baseline).
   - `README.md` (context pack index).
   - Cross-checked `REFERENCE_ZAI_5_3_REPORT.md` §15 (Prototype v0 rejection) and knowledge-states/GAP-35 lines; `FLASH_DELIVERY_TRANSCRIPT.txt` (GAP-34/35 knowledge states, Wave 5 contents).
3. Standard package at `/home/z/my-project/recon-work/Documents/micro-standard-v2/` (baseline @ Documents/main `864263c`): `design-tokens.css` (full 120-property token block), `component-contracts.md`, `component-states.md`, `button-system.md`, `navigation-shell.md`, `overlay-system.md`, `motion-interaction.md`, `typography.md`, `iconography.md`, `empty-loading-error-states.md`, `accessibility.md`, `responsive-geometry.md`, `color-system.md`, `content-guidelines.md`, plus supporting reads: `surface-system.md`, `input-system.md`, `spacing-radius-elevation.md`, `data-display-system.md`.
4. `component-gallery.html` — skimmed as demo-artifact reference only: first ~120 lines (chrome pattern: viewport/dir/text/motion controls OUTSIDE every phone-like composition) + section structure via headings, and the Rows / Navigation / Overlays / Icons families in detail (lines ~581–973) to learn the demo vocabulary that MUST NOT be copied (see §7.2).
5. Run artifacts discovered and read for alignment: `CONTEXT_ACKNOWLEDGEMENT.md`, `PRE_FLIGHT_REPORT.md`, and `micro-standard-v2-UPDATED/` — **verified byte-identical to the baseline package** (`diff -rq` clean, exit 0). The Phase-2 Standard edits have not been applied yet; this plan therefore targets the **post-Phase-2 contract state** = baseline contracts + the ten fixed additions (§1).

---

## 1. Scope basis — what Prototype v1 must demonstrate (fixed)

The ten contract additions (from the task brief, matching the decision register's "يدخل كعقود عامة" list and the Flash report):

| # | Addition | Register anchor |
|---|---|---|
| A1 | Knowledge-state presentation: known, unconfirmed, unavailable, incomplete, needs-review, estimated + measured zero (distinct honest voids) | U-11, U-05 |
| A2 | Operational-row marker: amount/unit slots, word + marker, optional ≤3px inline-start stripe, never color alone | U-06, U-05 |
| A3 | AUX behavior addendum: route-kind chrome, keyboard-driven chrome hiding, safe-area clearance, context-label suppression, scroll-border, route transition guidance | U-10 |
| A4 | Period-control variants: period chip AND native month/date-input; no product time policy | U-08 |
| A5 | Quiet feedback: inline/quiet completion and result feedback; Snackbar only as explicitly optional contract | U-07 |
| A6 | Overlay vs in-flow: consequential confirmation/deletion in Dialog/Sheet; continuous explanation/editing in-flow | U-17 |
| A7 | Typography floor: 13px labels; 12px non-financial metadata only; financial facts ≥15px; numeric hierarchy hero 28 / primary 24 / secondary 15 / tertiary 13 mono | U-04 |
| A8 | Icon mirror examples with NEUTRAL labels (no forced library) | U-13 |
| A9 | Authority ladder + visible «Visual validation prototype — not product truth» label | U-19 |
| A10 | Baseline set exercised inherently: create/add/FAB `#D97757`; ordinary save `#F5F4ED` + 2px `#C96442` pressed edge + quiet completion; high-consequence `#141413` + consequence wording + independent confirmation; RTL + English digits + bidi isolation; reduced motion; no overflow 320–430px | Foundation (keep-unchanged list) |

**Deliberately OUT of scope for Prototype v1** (keeps it minimal; the existing gallery already covers these): charts family, screen-level empty/no-results/skeleton states (U-18 keeps skeleton optional), tables, quick-action rail, segmented/tabs family (a minimal single-choice chip row is included only as the period control), dark mode, tooltips, sort, any business logic. `PROTOTYPE_COVERAGE.md` must record these exclusions explicitly.

---

## 2. Architecture decision — one phone frame, six scenes, chrome outside the frame

Following the gallery's proven pattern (and keeping the prototype honest about what is contract composition vs. demo apparatus):

- **Demo chrome (OUTSIDE every contract composition):** a top bar holding scene tabs, viewport-width control (تلقائي/320/360/390/430), text-scale control (100/130/200%), motion control (عادية/مخففة), an authority-ladder drawer, a quick self-check readout, and the persistent bilingual badge «Visual validation prototype — not product truth — نموذج تحقق بصري، ليس حقيقة منتج».
- **Phone frame:** one centered frame, max-width 430px, min 320px, RTL `dir="rtl"`, `lang="ar"`, light-first, canvas background. The frame carries shell state as data attributes: `data-route-kind="surface|deep"`, `data-kbd-open`, `data-scrolled`, `data-suppress-context`, `data-safesim`, `data-stripe`. Scene switching swaps scene roots inside the frame; each scene declares its default route kind.
- **Visible non-product-truth label inside the frame too:** a slim strip at the top of the frame content (12px non-financial caption tier — a contract-correct use) so every scene screenshot carries the label, satisfying A9's "visible on screen" requirement beyond the chrome badge.
- **File set (fixed by the brief):** `prototype.html`, `prototype.css`, `prototype.js`, `README.md`, `PROTOTYPE_COVERAGE.md`, `PROTOTYPE_VALIDATION.md`. Standalone, no build step, no CDN, no network, system-font fallback. Class namespace: `pv-` (greppable, no collision with `micro-*` or gallery classes).

---

## 3. Scene list and coverage map (smallest set = 6 scenes)

### 3.1 Scene inventory

| Scene | id | Title (neutral Arabic) | Demonstrates |
|---|---|---|---|
| S1 | `scene-value` | «منطقة القيمة وحالات المعرفة» | A1 (primary), A4, A7 (numeric hierarchy in composition), A2 (secondary: state grammar on tiles), A10 (RTL/digits/bidi/hero values) |
| S2 | `scene-rows` | «الصفوف التشغيلية» | A2 (primary), A1 (secondary: knowledge-state slots on rows), A7 (15px mono amounts), A10 (wrapping, no-overflow, digits) |
| S3 | `scene-shell` | «الهيكل وسلوك الواجهة» | A3 (primary: route-kind, keyboard, safe-area, context suppression, scroll border, transition guidance), A10 (FAB `#D97757`, nav geometry, motion) |
| S4 | `scene-form` | «الإدخال والتغذية الراجعة الهادئة» | A5 (primary), A10 (create button, ordinary save full cycle, amount input 24 mono LTR), A3 (secondary: deep-route default), A6 (secondary: in-flow editing) |
| S5 | `scene-overlay` | «الحوار مقابل التدفق» | A6 (primary: sheet deletion + dialog commit + in-flow explanation/editing), A10 (high-consequence `#141413`, scrim, focus trap, motion timings), A5 (secondary: inline confirm result) |
| S6 | `scene-type` | «الطباعة والأيقونات» | A7 (primary: full floor specimen), A8 (primary: mirror grid + pair boxes + scoped dir toggle), A10 (reduced-motion-safe transitions, geometry) |
| Chrome | — | (outside frame) | A9 (authority ladder + persistent label), A10 (width/text/motion controls, no-overflow harness) |

### 3.2 Coverage map (addition → scenes)

| Addition | Covered by | Evidence anchor |
|---|---|---|
| A1 Knowledge states | S1 (7-presentation tile matrix + hero state cycler), S2 (row state slots) | `.pv-tile.is-*`, `.pv-vz` state cycle, `.pv-row-state` |
| A2 Row markers | S2 (primary), S1 (tiles) | `.pv-row` grid, `.pv-row.is-striped::before` ≤3px, word+marker |
| A3 AUX behaviors | S3 (primary), S4 (deep default), S1/S2 (surface default + scroll border) | `[data-route-kind]`, `[data-kbd-open]`, `[data-scrolled]`, `[data-suppress-context]`, `[data-safesim]` |
| A4 Period variants | S1 (chip ↔ native month toggle) | `.pv-period[data-variant="chip|native"]` |
| A5 Quiet feedback | S4 (inline completion + result line; optional snackbar), S5 (dialog confirm → inline result) | `.pv-result[role=status]`, `.pv-btn-save` lifecycle, `.pv-snackbar` (default hidden, labeled اختياري) |
| A6 Overlay vs in-flow | S5 (primary), S4 (in-flow editing) | `.pv-sheet`, `.pv-dialog`, `.pv-details`, `.pv-note` |
| A7 Type floor | S6 (specimen), S1 (hierarchy), S2 (amounts), all scenes (13/12 floors) | `--text-*` consumption; `.pv-amount`, `.pv-hierstrip` |
| A8 Icon mirror | S6 | `.pv-icongrid`, `.pv-mirrorpair`, scoped `[dir]` |
| A9 Authority + label | Chrome (badge + drawer) + frame strip in every scene | `.pv-badge`, `.pv-authority`, `.pv-truthstrip` |
| A10 Baseline | S3 (FAB/nav), S4 (create/save), S5 (commit), all (RTL/digits/bidi/motion/geometry) | `.pv-fab`, `.pv-btn-create`, `.pv-btn-save`, `.pv-btn-commit` |

**Why not fewer than six:** merging S1+S2 would conflate the primary-value composition contract with the list-anatomy contract (different slots, different geometry); folding S6 into S1 would bury the floor/mirror specimens inside a data scene; S3/S4/S5 are three distinct interaction systems (shell state machine, form feedback lifecycle, overlay/focus system) whose behaviors must not share a scene's DOM. Six is the minimum with zero coverage loss and zero contract conflation.

---

## 4. Per-scene build specification

Shared shell markup (all scenes inherit):

```
.pv-frame[data-route-kind][data-kbd-open][data-scrolled][data-suppress-context][data-safesim]
  .pv-truthstrip            ← «نموذج تحقق بصري — ليس حقيقة منتج» (12px caption, always visible)
  .pv-header                ← 56px mock: context label (.pv-header-label) + 2 icon buttons
  .pv-scroll                ← scene content (scroll container; drives [data-scrolled])
    .pv-scene#scene-*       ← active scene root
  .pv-kbdmock               ← simulated keyboard (only when [data-kbd-open])
  .pv-actionbar             ← deep-route save bar (safe-area aware)
  .pv-fab                   ← 56px Clay FAB, own gutter, opens add-sheet
  .pv-nav                   ← 64px mock: 4 destinations «قسم 1..قسم 4», active pill + Clay edge
```

Header behavior: at rest, flat canvas + `--vf-border-soft` hairline; when `[data-scrolled]`, `--vf-border` + `--shadow-e2` + `--vf-header-translucent` background (scroll-border contract, 120ms). When `[data-suppress-context]`, the context label is hidden (context-label suppression). When `data-route-kind="deep"` or `[data-kbd-open]`: header, nav, and FAB hidden (route-kind chrome + keyboard-driven chrome hiding); the action bar remains. While any overlay is open, nav/FAB also get `visibility:hidden` + `aria-hidden` (focus containment). Safe area: `padding-block-end: env(safe-area-inset-bottom)` always on nav/action bar; `[data-safesim]` adds a labeled simulated inset («منطقة أمان — محاكاة»).

### S1 — «منطقة القيمة وحالات المعرفة» (default route kind: surface)

**Layout (top→bottom):**
1. Hero value zone `.pv-valuezone`: label slot («القيمة الإجمالية التوضيحية», 13px label), value slot (mono hero 28/600, `dir="ltr"`, `unicode-bidi:isolate`, English digits, e.g. `12,480.50`), currency-unit slot «د.أ» outside the number, period slot, delta slot («أعلى من الفترة السابقة» + up-arrow marker + word).
2. Period control `.pv-period` with variant toggle («طريقة العرض: رقاقة / إدخال شهري»):
   - chip variant: `.pv-chiprow` of 2–3 chips («آخر 30 يوم», «هذا الشهر») — single choice, 36px visual / 44px hit (`::after` hit area), selected = 2px `#C96442` inset edge + bold ink, never black fill;
   - native variant: label «اختر الشهر» (13px) + `<input type="month">` styled per input contract (white surface, structural border, warm-ink focus). No default-period logic, no ranges — presentation only (A4: no product time policy).
3. Knowledge-state matrix `.pv-tilegrid`: 7 tiles, each = label (13px) + value slot (15px mono, end-aligned, isolated) + state word + non-color marker:
   - known → «مؤكد» + check marker, ink (no special hue);
   - unconfirmed → «غير مؤكد» + question/info marker, Info hue on marker only;
   - estimated → «تقديري» + tilde/approx marker, word in ink;
   - incomplete → «غير مكتمل» + half-filled marker, word in ink;
   - unavailable → «غير متاح» + minus/document marker (honest void; no number shown);
   - unrecorded → «قيمة غير مُدخلة» + **action chip «أضِف قيمة»** (honest void → action chip; neutral substitution for the Standard's illustrative «سجّله» text — see §7.3);
   - measured zero → «صفر» + value `0` rendered with a visible baseline mark (distinct from unavailable and unrecorded).
4. Hero state cycler: button «تنقّل بين حالات المعرفة» cycles the HERO value zone through all 7 presentations from a fixed literal array (static strings only — no computation).
5. Numeric hierarchy strip `.pv-hierstrip`: the same illustrative value rendered at hero 28 / primary 24 / secondary 15 / tertiary 13 (mono, isolated) with 12px non-financial captions naming each step («أساسي 28» … «ثالثي 13»).

**JS:** `setPeriodVariant()`, chip single-select, `cycleKnowledgeState()`. No arithmetic.

### S2 — «الصفوف التشغيلية» (surface)

**Layout:** one `.pv-rowlist` card (16px padding, radius-card, shadow-e1) with 7 rows + a stripe toggle above.

Row anatomy (one grid): `.pv-row` → `.pv-row-tile` (leading icon tile, neutral glyph), `.pv-row-main` (`.pv-row-title` 15/600 wrapping Arabic; `.pv-row-sub` caption 12px non-financial metadata + isolated date `17/07/2026`), optional `.pv-row-state` (word + marker, 13px), `.pv-row-trail` (`.pv-row-amt` mono 15/600 `dir="ltr"` isolated end-aligned + `.pv-row-unit` «د.أ» beside, optional `.pv-row-chev` icon button 44px hit). Dividers inset 72px from inline start.

Rows (states reused from S1 grammar — A1×A2 integration):
1. clean known row (amount `1,250.00`, no state slot);
2. «غير مؤكد» word+marker, no stripe;
3. «بحاجة لمراجعة» word + eye marker (Status hue on marker) **+ 3px inline-start stripe**;
4. «تقديري» word + approx marker, amount `900`;
5. «غير مكتمل» word + half marker;
6. unavailable row: amount slot shows «غير متاح» (no number);
7. unrecorded row: amount slot shows compact action chip «أضِف»;
8. measured zero row: amount `0` + «صفر» word in the state slot.
One row must use a deliberately long neutral title («عنصر تجريبي بعنوان طويل لتوضيح التفاف النص العربي داخل العمود المرن دون دفع القيمة الرقمية خارج حدود الشاشة») to prove wrapping never pushes the trailing slot off-screen.

**Stripe toggle:** «الشريط الحافي: ظاهر / مخفي» toggles `[data-stripe]` — proves optionality; the word+marker persists either way (never color alone). Stripe = `border-inline-start: 3px solid <state semantic token>` (computed width must be ≤3px).

**JS:** stripe toggle, chevron press state (0.97 @ 80ms). No list mutation (insert/remove/undo stays a gallery demo, out of scope).

### S3 — «الهيكل وسلوك الواجهة» (surface by default; this scene drives the shell)

**Layout:** an options card `.pv-optlist` + long scroll content + route-transition guidance card (in-flow).

Options (each a labeled segmented control, 13px labels):
1. «نوع المسار»: سطح ↔ عميق → sets `data-route-kind` on the frame. Surface: header+nav+FAB visible. Deep: chrome hidden, in-content work title + `.pv-actionbar` (with ordinary save button) visible. Transition: chrome opacity/translate 200ms (`--motion-normal`, `--ease-standard`); reduced motion → opacity only.
2. «لوحة المفاتيح (محاكاة)»: toggles `data-kbd-open` → header+nav hide (keyboard-driven chrome hiding), `.pv-kbdmock` (recessed block, ~38% frame height, labeled «لوحة مفاتيح — محاكاة» in 12px caption) appears, action bar docks above it with safe-area clearance.
3. «التمرير»: buttons «مرّر للأسفل» / «مرّر للأعلى» scroll `.pv-scroll` programmatically (for reviewers without wheels); the scroll listener sets `data-scrolled` past 8px → header border+shadow+translucent background (scroll-border behavior).
4. «تكرار عنوان الصفحة»: when ON, the scene's in-content `h1` text equals the header context label → header label is suppressed (`data-suppress-context`); when OFF, header shows «واجهة توضيحية» and the h1 differs (context-label suppression contract).
5. «منطقة الأمان (محاكاة)»: toggles `data-safesim` → simulated insets on nav/action bar with a thin labeled marker («منطقة أمان — محاكاة»); real `env(safe-area-inset-*)` always applied.

Scroll filler: 8 neutral blocks «محتوى تمرير توضيحي 1..8» (recessed surface, caption text). FAB: 56px, radius 12px, Clay fill, white plus icon, inline-end gutter 16px (sits 80px above nav: 64px nav + 16px offset), `aria-label="إضافة عنصر"`, opens the shared add-sheet (S5 instance). Nav mock: 4 destinations «قسم 1» … «قسم 4», active pill = filled pill with `#C96442` edge (chosen/current), 64px min height, `aria-current="page"` on active. Route-transition guidance card (in-flow, always visible in this scene): brief Arabic text of the addendum — surface-like routes keep chrome; deep/work routes hide it; transitions are 200ms opacity-led; content never jumps; reduced motion collapses to opacity.

**JS:** shell state machine (the five toggles are independent; deep + kbd-open compose).

### S4 — «الإدخال والتغذية الراجعة الهادئة» (default route kind: deep — form/work route, chrome hidden, action bar present)

**Layout:** form card + action bar.

1. Text field: label «اسم العنصر التجريبي» (13px, 500), input (white surface, `--vf-border`, warm-ink focus 2px outline), helper caption 12px («نص توضيحي فقط»).
2. Amount field `.pv-field-amt`: label «قيمة توضيحية»; LTR numeric input (`dir="ltr"`, `inputmode="decimal"`, English digits only — reject/normalize Arabic-Indic digits on input), in-field type 24/600 mono (`--text-amount-input-size`); unit slot «د.أ» rendered **outside** the input's numeric string; empty/zero/entered values visually distinct.
3. Native date field: label «تاريخ توضيحي» + `<input type="date">` (input-system baseline).
4. Inline error demo: a field with error state — word «قيمة غير صالحة» + alert marker in `--vf-error` (6.02:1 text-safe) + recovery hint; input preserved.
5. Action bar (`.pv-actionbar`, safe-area aware):
   - ordinary save `.pv-btn-save` — Warm Tint `#F5F4ED` surface + `#141413` ink + save icon; `:active` shows 2px inset `#C96442` edge (surface stays Warm Tint); click → loading (spinner replaces leading icon, label «جارٍ الحفظ» persists, width stable, duplicate clicks blocked ~1.2s) → **quiet completion**: check icon + past-tense word «تم الحفظ» on the quiet surface, then return to default; simultaneously an inline result line appears: `.pv-result[role="status"][aria-live="polite"]` = «تم حفظ العنصر التجريبي» + check marker (A5 primary path: inline, not toast).
   - create `.pv-btn-create` — text-bearing Clay `#D97757` + `#141413` ink + plus icon, pressed `#C96442`; click → quiet completion «تمت الإضافة» (inline result line; a static tile is appended from a fixed literal — no computation).
   - destructive `.pv-btn-danger` — outline/surface, `#B53333` ink + alert icon, label «حذف العنصر التجريبي» → opens the deletion sheet (S5 instance).
6. Optional Snackbar toggle: «عرض عقد Snackbar (اختياري)» — default OFF. When ON, the save completion ALSO fires `.pv-snackbar` (warm-ink `#141413` fill, white text, `role="status"`, 5000ms hold, z 500). The toggle's own label carries «اختياري» so the demo never reads as a mandate (A5/U-07).

**JS:** save lifecycle state machine (idle → loading → quiet-complete → idle), duplicate-submit guard, optional-snackbar flag, digit normalization, inline error show/dismiss.

### S5 — «الحوار مقابل التدفق» (surface)

**Layout:**
1. In-flow explanation card `.pv-details` (continuous explanation stays in-flow): «توضيح العقد — الحوار مقابل التدفق»: الإجراءات ذات الأثر تُأكَّد في لوحة أو حوار؛ الشرح والتحرير المستمر يبقى داخل التدفق. Plus a `<details>`-style collapsible and an in-flow editable note (`.pv-note` textarea directly in the page flow — in-flow editing, not an overlay).
2. Trigger buttons: «فتح اللوحة» (outline) → **Sheet**; «فتح الحوار» (outline) → **Dialog**.
3. **Sheet** `.pv-sheet` (deletion confirmation — consequential deletion lives in an overlay): 20px top radius, drag handle (drag-down dismiss; drag-up expand 84% → 94%), enter/exit 240/180ms, title «تأكيد حذف العنصر التجريبي», consequence wording («سيُزال العنصر التجريبي من هذه القائمة التوضيحية»), destructive confirm uses the high-consequence anatomy: consequence word + icon + explanation + independent «إلغاء» / «تأكيد الحذف» pair (never single-tap). Confirm → sheet closes → inline result line «تم حذف العنصر التجريبي» + marker (quiet feedback again).
4. **Dialog** `.pv-dialog` (high-consequence commit): centered, enter/exit 160/120ms, title «تنفيذ نهائي», body = consequence explanation, actions = «إلغاء» (outline) + «تنفيذ نهائي» `.pv-btn-commit` — `#141413` fill, white text, pressed `#3D3D3A`, consequence word + icon. Confirm → inline result «تم التطبيق» + check.
5. Shared scrim `.pv-scrim` (200ms, `--vf-scrim`), one active modal at a time, focus trap + focus return, Esc/scrim-click safe dismissal, scroll lock while open, nav/FAB hidden while open.

**Z-ladder (token consumption, recorded):** scrim 250 < overlay 300 < FAB 400 < snackbar 500.

**JS:** sheet/dialog controllers (open/close/expand/drag-dismiss), focus trap + return, one-active enforcement, inline results.

### S6 — «الطباعة والأيقونات» (surface)

**Layout:**
1. Type specimen `.pv-typespec` — one row per step; sample on the inline-end, step note as 12px non-financial caption on the inline-start:
   - title 28/1.3/700 (Arabic sample «عنوان تجريبي»), title-sm 20, section 17, card-title 15, body 15, label 13, caption 12 (explicitly labeled «بيانات وصفية غير مالية — الحد الأدنى 12px»);
   - numeric: hero 28 / primary 24 / secondary 15 / tertiary 13 mono samples (`4,321.00` with «د.أ» unit outside), amount-input 24;
   - a floor note line: «الحقائق والقيم المالية لا تقل عن 15px؛ 12px للبيانات الوصفية غير المالية فقط».
2. Icon mirror `.pv-icongrid`: ~10 inline-SVG glyphs (24 viewBox, stroke 1.8, round caps, `currentColor`, composed in the Standard's outlined grammar — registry path data from the Standard's own sprite may be reused), each cell = glyph + neutral Arabic label + flag chip («ينعكس» / «ثابت»): «إضافة» ثابت، «إغلاق» ثابت، «تحقق» ثابت، «معلومات» ثابت، «تنبيه» ثابت، «سهم للأمام» ينعكس، «سهم للخلف» ينعكس، «مشاركة» ينعكس، «تنزيل» ثابت، «رفع» ثابت.
3. Mirror pair `.pv-mirrorpair`: two boxes side by side — «الاتجاه: من اليمين إلى اليسار» (RTL) vs «الاتجاه: من اليسار إلى اليمين» (LTR via scoped `[dir="ltr"]`) showing the same directional glyphs; mirrored glyphs carry `.mirror` (`transform: scaleX(-1)` or mirrored path), static glyphs never flip. Optional scoped live toggle «اعكس اتجاه الشريط» confined to the icon strip (a global page dir toggle is optional and must not be required for validation).

**JS:** optional scoped dir toggle only.

### Chrome (outside the frame) — A9

- `.pv-badge` — persistent, always visible: «Visual validation prototype — not product truth» + «نموذج تحقق بصري — ليس حقيقة منتج».
- `.pv-authority` drawer («سلطة الوثيقة») — the authority ladder in Arabic: المعيار (Standard) = عقود بصرية؛ ربط Micro (runtime token mapping) = حامل التنفيذ؛ وثائق Micro = إرشاد تنفيذ؛ النطاق/التطبيق/التخزين = المعنى والاستمرار. Plus the Prototype-boundary sentence (evidence only; never a source of product copy/routes/data/financial meaning — decision 13).
- Controls: scene tabs; width (تلقائي/320/360/390/430 → sets frame width); text (100/130/200% → `--ts` multiplier, §5); motion (عادية/مخففة → `data-motion="reduced"`, initialized from `matchMedia('(prefers-reduced-motion: reduce)')`).
- `.pv-checks` quick readout (evidence aid): current frame width, horizontal-overflow probe result («تجاوز أفقي: لا»), count of visible knowledge-state presentations, current route kind. Static probes only.

---

## 5. Token usage plan

**Embedding rule:** `prototype.css` embeds the **complete token block** from the Standard's `design-tokens.css` `:root` (all 120 custom properties: 67 `--vf-*` + 53 unprefixed), bound to the same values, as the first rule of the file, with a comment citing the source file and SHA. **Dependency:** embed the **post-Phase-2** `micro-standard-v2-UPDATED/design-tokens.css` block (today that file is byte-identical to baseline — verified; if Phase 2 adds tokens, e.g. a route-transition timing or knowledge-state alias, the final block is embedded instead).

**One disclosed transformation (text-scale emulation):** the eleven `--text-*-size` tokens are wrapped as `calc(<px> * var(--ts, 1))` where `html[data-text="130"] { --ts: 1.3 }` and `html[data-text="200"] { --ts: 2 }`. At `--ts: 1` computed values must equal `design-tokens.css` byte-for-byte (validation asserts this). This is the only modification to the embedded block and it exists to emulate OS/browser text scaling for the no-overflow requirement (the gallery's data-text control only adjusts line-height; that is not sufficient evidence for 200%).

**Color rule:** all colors resolve through tokens; the only color literals in the entire prototype live inside the embedded token block (the 18 approved hex + the 2 disclosed alpha derivatives `rgba(20,20,19,.45)` and `rgba(250,249,245,.86)` + the recorded shadow-ink family `rgba(60,50,40,x)` that ships inside `--shadow-*`). Icons use `currentColor`. No gradients, no opacity-based new colors, no hex outside the block.

**Consumption map:**

| Token group | Consumers |
|---|---|
| `--vf-canvas/ground/recessed/surface/tint/soft/border/border-interactive/border-soft` | page/frame bg, save button bg, kbd-mock & skeleton-free recessed blocks, cards/sheet/dialog/fields, dividers, header border, secondary buttons |
| `--vf-ink/-secondary/-tertiary/-on-dark/-on-tint/-pressed` | text ramp, commit text, snackbar text, pressed commit fill |
| `--vf-clay / --vf-clay-interactive` | FAB, create button, pressed states, selected chip/segment edge, active nav pill edge |
| `--vf-info / --vf-status / --vf-success / --vf-error` | non-text markers (unconfirmed, needs-review, completion check, destructive/error ink) — words always in text-safe ink |
| `--vf-focus`, `--vf-field-border-focus`, `--vf-disabled-*` | focus rings, field focus, disabled pair (if any disabled demo) |
| `--vf-action-create*/-save*/-commit*` and `--vf-btn-*` | the three action classes + secondary/outline/ghost/destructive bindings |
| `--text-*` (11 steps) | all typography; mono steps for numerals via `--vf-font-mono` |
| `--vf-radius-control/card/segment/sheet/full` (+ unprefixed aliases) | buttons/inputs, cards, chip row container, sheet, pills/flags |
| `--shadow-sm/e1/e2/e3` | chrome lift, cards/rows, scrolled header/menus, FAB/dialogs/snackbar |
| `--motion-press/fast/normal/sheet-in/out/dialog-in/out/scrim/snackbar-hold`, `--vf-motion-*`, `--ease-*` | press 0.97@80ms, header border 120ms, route transition 200ms, sheet 240/180, dialog 160/120, scrim 200, snackbar 5000 |
| `--vf-control-height`, `--control-height-compact`, `--topbar-height`, `--nav-height-min`, `--fab-size`, `--fab-offset`, `--icon-sm/md`, `--progress-track-height` (if used) | control/chip geometry, 56px header, 64px nav, 56px FAB @ 80px gutter, 20/24px icons |
| `--z-scrim/overlay/fab/snackbar` | overlay ladder |
| `--vf-scrim`, `--vf-header-translucent` (+ `--color-*` aliases), `--color-negative-50/-on-tint/positive-100/primary-100/200` | scrim, scrolled header, tinted state marks |
| `--vf-font-sans/mono` | typography with system fallback (no CDN) |

---

## 6. Interactive/JS inventory (complete list — nothing else)

1. Scene switcher (tabs → active `.pv-scene`; sets per-scene default `data-route-kind`).
2. Frame width control (320/360/390/430/auto).
3. Text-scale control (`data-text` → `--ts`).
4. Motion control (`data-motion="reduced"`; initialized from media query).
5. Authority drawer toggle.
6. Shell state machine: route-kind switcher, keyboard-open simulation, programmatic scroll + `data-scrolled` listener, context-suppression toggle, safe-area simulation toggle.
7. Period variant toggle + chip single-select.
8. Knowledge-state hero cycler (fixed literal array).
9. Row stripe toggle.
10. Save lifecycle (idle → loading → quiet completion → idle) + duplicate-submit guard + optional snackbar flag; create quiet completion; inline error toggle.
11. Sheet/dialog controllers: open/close, drag-dismiss, expand, focus trap + return, one-active enforcement, Esc/scrim dismissal, scroll lock, chrome hiding while open.
12. Digit normalization in the amount input (English digits only).
13. Self-check probes (read-only: scrollWidth vs clientWidth, computed token samples) feeding `.pv-checks`.

**Hard JS rule:** no arithmetic on displayed values, no aggregation, no formulas, no generated/faked product data — only class/attribute toggles and fixed literal string arrays.

---

## 7. Vocabulary plan

### 7.1 Allowed Arabic strings (closed allowlist — every visible Arabic string in the three code files must be one of these or a clearly-derived inflection recorded in PROTOTYPE_COVERAGE.md)

- **Meta / boundary:** «نموذج تحقق بصري — ليس حقيقة منتج»؛ "Visual validation prototype — not product truth"؛ «عينة»؛ «توضيح العقد»؛ «عرض توضيحي»؛ «محاكاة»؛ «تجريبي»؛ «توضيحي»؛ «لأغراض العرض فقط».
- **Chrome/controls:** «المشاهد»؛ «العرض»؛ «حجم النص»؛ «الحركة: عادية/مخفضة»؛ «سلطة الوثيقة»؛ «فحص سريع»؛ «تجاوز أفقي: نعم/لا».
- **Scene titles:** «منطقة القيمة وحالات المعرفة»؛ «الصفوف التشغيلية»؛ «الهيكل وسلوك الواجهة»؛ «الإدخال والتغذية الراجعة الهادئة»؛ «الحوار مقابل التدفق»؛ «الطباعة والأيقونات».
- **Nav/header placeholders:** «قسم 1» «قسم 2» «قسم 3» «قسم 4»؛ «واجهة توضيحية»؛ «إضافة عنصر» (FAB aria-label).
- **Value zone:** «القيمة الإجمالية التوضيحية»؛ «قيمة توضيحية»؛ «الفترة التوضيحية»؛ «آخر 30 يوم»؛ «هذا الشهر»؛ «اختر الشهر»؛ «تاريخ توضيحي»؛ «أعلى من الفترة السابقة» / «أدنى من الفترة السابقة» (delta words + marker).
- **Knowledge states (A1 words + markers):** «مؤكد» (known)؛ «غير مؤكد» (unconfirmed)؛ «تقديري» (estimated)؛ «غير مكتمل» (incomplete)؛ «بحاجة لمراجعة» (needs-review)؛ «غير متاح» (unavailable — Standard honest-void word)؛ «صفر» + `0` (measured zero — Standard honest-void presentation)؛ «قيمة غير مُدخلة» + action chip «أضِف قيمة» (unrecorded void).
- **Rows:** «عنصر تجريبي»؛ «عنصر تجريبي — رقم 1..8»؛ the long-title wrapping specimen (§4 S2)؛ «محتوى تمرير توضيحي 1..8»؛ unit «د.أ» beside numbers only.
- **Buttons/actions:** «حفظ»؛ «جارٍ الحفظ»؛ «تم الحفظ»؛ «إضافة عنصر»؛ «تمت الإضافة»؛ «حذف العنصر التجريبي»؛ «تأكيد الحذف»؛ «تنفيذ نهائي»؛ «تم التطبيق»؛ «إلغاء»؛ «تأكيد»؛ «تطبيق»؛ «إعادة المحاولة»؛ «تنقّل بين حالات المعرفة»؛ «طريقة العرض: رقاقة / إدخال شهري»؛ «الشريط الحافي: ظاهر/مخفي»؛ «نوع المسار: سطح/عميق»؛ «لوحة المفاتيح (محاكاة)»؛ «مرّر للأسفل/للأعلى»؛ «تكرار عنوان الصفحة»؛ «منطقة الأمان (محاكاة)»؛ «عرض عقد Snackbar (اختياري)».
- **Results/feedback (word + marker):** «تم حفظ العنصر التجريبي»؛ «تم حذف العنصر التجريبي»؛ «النتيجة:» prefix؛ «قيمة غير صالحة» + recovery hint «أدخل قيمة رقمية بالأرقام الإنجليزية».
- **Overlay copy:** «تأكيد حذف العنصر التجريبي»؛ «سيُزال العنصر التجريبي من هذه القائمة التوضيحية»؛ «تنفيذ نهائي»؛ «سيُطبَّق هذا الإجراء على العنصر التجريبي ولن يكون التراجع متاحًا من هذه الواجهة.»
- **Guidance cards (contract wording, no product meaning):** AUX addendum summary (§4 S3)؛ «الحقائق والقيم المالية لا تقل عن 15px؛ 12px للبيانات الوصفية غير المالية فقط»؛ «الحوار مقابل التدفق: الإجراءات ذات الأثر تُأكَّد في لوحة أو حوار؛ الشرح والتحرير المستمر يبقى داخل التدفق.»
- **Icon labels + flags:** «إضافة» «إغلاق» «تحقق» «معلومات» «تنبيه» «سهم للأمام» «سهم للخلف» «مشاركة» «تنزيل» «رفع» «قائمة» «بحث» «تقويم» «ساعة»؛ flags «ينعكس» / «ثابت»؛ pair boxes «الاتجاه: من اليمين إلى اليسار» / «الاتجاه: من اليسار إلى اليمين».
- **Authority ladder (drawer):** «المعيار = عقود بصرية»؛ «ربط Micro = حامل التنفيذ (وقيم الرموز وقت التشغيل)»؛ «وثائق Micro = إرشاد تنفيذ»؛ «النطاق/التطبيق/التخزين = المعنى والاستمرار»؛ «هذا النموذج دليل بصري فقط وليس مصدرًا لأي نص أو مسار أو بيانات أو معنى مالي في المنتج.»
- **English fragments allowed:** the bilingual badge sentence; token/file names inside the authority drawer and code comments (`--vf-*`, `design-tokens.css`, scene ids). No other English content.

### 7.2 Forbidden strings (build-time grep gate — zero tolerance)

- **Micro product vocabulary:** «مشروعي الآن»، «العمل»، «مالي»، «أدواتي»، «سجّل» (any inflection: سجّل/سجّله/سجِّل/تسجيل/مسجّل/غير مسجل)، «سجّل أول قيد»، G5/«قرار» decision-panel vocabulary, «مستحق»، «متأخر»، «عُكس»، «رُوجعت»، «مسودة»، «بالانتظار»، «جزئي» (as standalone state-slot words; «غير مكتمل» replaces partial), «غير معروف» (the prototype demonstrates knowledge states, not the financial unknown; S1 uses «غير متاح»/«غير مؤكد» instead — recorded in PROTOTYPE_COVERAGE.md).
- **Standard/Micro navigation labels as recorded:** «الرئيسية»، «المالية»، «الطلبات»، «الأدوات» (recorded from Micro per U-09 — replaced by «قسم 1..4»).
- **Gallery demo vocabulary (English):** Received, In progress, Moved, Returned, Ready, Sent, Closed, Posted, Failed, Pending, Unknown, Reviewed, Draft, "Morning batch", "Weekly restock invoice", "Draft entry", "New sale", "Collect", "Add expense", "Add purchase", "Withdrawal", "New invoice", "Finalize period", "Add record", "Record saved", "Entry removed", "Undo", "Sync result unknown".
- **Route/tech leakage:** `/finance`, `/orders`, `/tools`, `/setup`, `/assets`, `/loans`, `/cash`, `/review`, `QuickActionSheet`, `routeClassifier`, `micro-` class prefix, any Micro component name.
- **Retired/unapproved colors:** `#964E33`, `#5F3120`, `#CC785C`, `#B4613F`, `#079FA0`, `#256B4A`, `#B42318`, `#7A5C20`, `#3E5C76`, `#B79C86`, `#8C7A66`, `#1F1E1D` (plus the general rule: no hex outside the embedded token block).
- **Financial formulas/policy:** any `+ - * /` on displayed values, any sum/total computation, any «صافي/رصيد/إجمالي حقيقي» product-semantic framing beyond the explicitly-neutral «القيمة الإجمالية التوضيحية» label.
- **Prototype v0 content:** by construction — the builder never opens Prototype v0 or Micro screens; all strings come from §7.1.

### 7.3 Documented substitutions (must be recorded in PROTOTYPE_COVERAGE.md so Agent-5 does not misread them)

1. **Unrecorded void chip:** Standard's illustrative chip text «سجّله» → neutral «أضِف قيمة» (register/تسجيل is Micro-coupled vocabulary; the contract demonstrated is structural: unrecorded → action chip).
2. **Nav labels:** Standard navigation-shell's recorded destinations («الرئيسية/المالية/الطلبات/الأدوات», recorded from Micro per U-09) → neutral «قسم 1..4».
3. **Snackbar:** contract exists in the Standard; the prototype shows it ONLY behind an explicitly-labeled optional toggle, default OFF (U-07: inline is the ratified default).
4. **Known-state word:** «مؤكد» is the prototype's neutral rendering of "known" (a recorded, confirmed fact); financial posted-state wording («تم» as a standalone tag) is deliberately absent.

---

## 8. Validation plan outline (what PROTOTYPE_VALIDATION.md must check)

1. **Per-contract evidence table** — each of A1…A10 → scene(s), selector(s), and expected computed/observable evidence. Examples: save pressed edge = `box-shadow: inset 0 0 0 2px var(--vf-action-save-pressed-edge)` (computed `#C96442`/rgb equivalent); stripe computed width ≤ 3px; `.pv-row-amt` computed font 15px/600 mono + `direction: ltr` + `unicode-bidi: isolate`; hero 28 / primary 24 / secondary 15 / tertiary 13 computed; knowledge tiles = exactly 7 distinct presentations; sheet enter/exit 240/180ms; dialog 160/120ms; scrim 200ms; snackbar hold 5000ms; FAB 56px at 80px above nav; chip 36px visual with ≥44px hit box; header 56px; nav ≥64px.
2. **Geometry matrix** — frame widths 320/360/390/430 × text scales 100/130/200% (via `--ts`) → assert no horizontal overflow (`document.scrollingElement.scrollWidth ≤ clientWidth` AND frame content `scrollWidth ≤ clientWidth`), rows wrap without clipping the trailing slot, long-title specimen never pushes the amount off-frame. Record the overflow probe from `.pv-checks` per combination.
3. **Token integrity** — at `--ts:1`, computed values of all embedded tokens equal `design-tokens.css` (scripted `getComputedStyle` comparison against the source file); grep proof that no hex literal exists outside the embedded block; the 18-hex + 2-alpha-derivative (+ recorded shadow rgba family) attestation.
4. **RTL/bidi/digits** — `html[dir="rtl"]` everywhere; every numeric slot `dir="ltr"` + isolated; rendered digits match `[0-9]` only (no Arabic-Indic `٠-٩` in value slots); «د.أ» always outside the numeric string; dates displayed as `DD/MM/YYYY` in isolated slots.
5. **Reduced motion** — `prefers-reduced-motion: reduce` and manual `data-motion="reduced"` both collapse animations/transitions to ≤0.01ms or opacity-only; press scale removed; spinner remains identifiable as a static ring with persistent label; all state meaning still carried by words/markers.
6. **State redundancy (never color alone)** — for every state presentation (7 knowledge tiles, row states, results, errors): word + marker present in DOM regardless of stripe/hidden-color simulations; a checklist per element.
7. **AUX behaviors** — route-kind switch hides/shows chrome; kbd-open hides header+nav and docks the action bar; scrolled header gains border+shadow+translucent token; context suppression hides the header label only when h1 duplicates it; safe-area padding present (env + sim labeled «محاكاة»).
8. **Overlay correctness** — one active modal; focus trapped and returned; Esc/scrim dismiss; scroll locked; nav/FAB hidden while open; sheet drag-dismiss + 84→94 expand.
9. **Quiet feedback** — save cycle order and wording; duplicate-submit blocked during loading; result line `role="status"`; snackbar appears ONLY when the optional toggle is ON.
10. **Honest limitations (mandatory section)** — no physical-device testing; no screen-reader testing; no Micro runtime integration; keyboard and safe-area are labeled simulations; text-scale is a `--ts` emulation (real browser zoom recommended as a secondary manual check); fonts fall back to system fonts offline (IBM Plex Mono unavailable → `ui-monospace` fallback, tabular alignment approximate); the prototype proves contract presentation only, never product behavior; Prototype is evidence, not acceptance truth (decision 13).

---

## 9. Anti-contamination checklist (run before delivery; record results in PROTOTYPE_COVERAGE.md §"نقاء المحتوى")

1. **Closed-vocabulary grep:** extract every Arabic string from `prototype.html/.js` and every `content:`/text node in `prototype.css`; each must match §7.1 (or a documented inflection listed in PROTOTYPE_COVERAGE.md). Any unmatched string = build failure.
2. **Forbidden-pattern grep (zero hits required):** the full §7.2 list, case-insensitive, across all prototype files (code + comments): Micro words, nav labels, gallery English tags, route paths, Micro class/component names, retired hexes. Include fuzzy forms: `سجّل|سجل` family regex, `مشرقي` typo-guard, `Received|in progress|Moved|Returned|Ready|Sent|Closed|Posted|Failed|Pending|Unknown|Reviewed|Draft|Finalize|sale|expense|invoice|Withdrawal|Undo`.
3. **Color scan:** every hex/rgba in `prototype.css` must sit inside the embedded token block; `prototype.html/.js` contain zero color literals (icons = `currentColor`).
4. **No-network scan:** no `<link>`, `@import`, `url(http`, `fetch(`, `XMLHttpRequest`, `import ` from remote, no CDN references. `xmlns` SVG namespaces are permitted (not fetches).
5. **No-formula scan:** `prototype.js` contains no arithmetic operators applied to displayed numeric content (grep `+ - * /` in numeric contexts; the only permitted math is layout probes like `scrollWidth` comparisons).
6. **Boundary-label check:** the bilingual non-product-truth badge is present in the chrome AND the frame strip is visible in all six scenes (screenshot-level check per scene).
7. **Process attestation:** builder confirms (in PROTOTYPE_COVERAGE.md) that no Prototype v0 file, no Micro screen, and no gallery demo *content* was opened or copied during the build; the gallery was used only as a structural pattern reference (chrome-outside-frame, demo-note convention), and Standard registry icon path data is the only reused asset, relabeled neutrally.
8. **Substitution log:** §7.3's four substitutions restated with before/after so the adversarial reviewer can distinguish deliberate neutrality from accidental drift.

---

## 10. Deliverable file outlines (for the builder)

- **README.md:** what this is (visual validation prototype for the updated Standard); how to open (`file://`, no server); control guide (scenes, width, text, motion, authority drawer); scene map; the boundary statement (evidence only — decision 13); token provenance (embedded from `micro-standard-v2-UPDATED/design-tokens.css`, one disclosed `--ts` transformation); known limitations.
- **PROTOTYPE_COVERAGE.md:** the §3 coverage map; per-addition element inventory with selectors; the four documented substitutions; out-of-scope list (§1); anti-contamination results (§9); process attestation.
- **PROTOTYPE_VALIDATION.md:** the §8 checks with recorded results, the geometry matrix table, token-integrity diff output, and the honest-limitations section.

---

## 11. Risks and watch items (for the main agent / Agent 5)

1. **Vocabulary drift is the #1 contamination vector** — builders improving Arabic copy ad hoc. Mitigation: §7.1 closed allowlist + grep gate before delivery; PROTOTYPE_COVERAGE.md must list any additions.
2. **The «أضِف قيمة» substitution** could be misread by reviewers as the prototype rejecting the Standard's «سجّله» example; the substitution log must state the Standard text is unchanged and only the prototype renders neutral wording.
3. **Simulation fidelity:** keyboard, safe-area, and text-scale are labeled simulations; validation must never phrase them as device-verified (stop condition in the brief).
4. **Snackbar optionality:** any default-on snackbar would visually contradict U-07; the toggle ships default-OFF and labeled «اختياري».
5. **Shell state-machine combinatorics (S3):** five independent toggles can interact (deep + kbd-open + scrolled + suppressed + safesim); spec keeps them as independent frame attributes, but the builder must smoke-test all-pairs combinations.
6. **Token embed staleness:** if Phase 2 changes `design-tokens.css` (e.g., adds a route-transition token), the embedded block must be refreshed from the UPDATED package — build order dependency: Phase 2 → Phase 4.
7. **Mono fallback offline:** without IBM Plex Mono, `ui-monospace` may differ in tabular figures; noted as a limitation, not a failure.
8. **Z-ladder vs. open overlays:** FAB (z 400) sits above overlay (z 300) per tokens; the spec hides nav/FAB while overlays are open to preserve focus containment — recorded as a deliberate composition decision, not a token change.
9. **Scope creep:** charts, tables, skeletons, empty-screen states, segmented control family, and quick-action rail are all tempting; they are out of the fixed scope and must stay out (the gallery already evidences them).
10. **200% at 320px:** the `--ts` emulation is the primary evidence; real browser zoom should be spot-checked manually and recorded honestly as a secondary check.

---

## 12. Coverage self-check (final)

- A1 ✔ S1+S2 · A2 ✔ S2(+S1) · A3 ✔ S3(+S4,S1/S2) · A4 ✔ S1 · A5 ✔ S4(+S5) · A6 ✔ S5(+S4) · A7 ✔ S6(+S1,S2,all) · A8 ✔ S6 · A9 ✔ chrome + every scene · A10 ✔ S3/S4/S5 + all scenes + chrome harness.
- Six scenes, one shared frame, closed vocabulary, token-only colors, no formulas, no Micro/gallery/v0 content, honest limitations section mandatory.
- This plan is analysis only; no prototype artifact was produced by Agent 4.

**Agent 4 — end of report.**
