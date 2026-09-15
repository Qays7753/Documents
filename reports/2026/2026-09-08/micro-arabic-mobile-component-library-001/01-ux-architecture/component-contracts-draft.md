# Component Contracts (Draft) — Micro Arabic-First Library

Agent 01 · Task 2-a · RUN_ID `20260908T133450Z-16d11`. Draft contracts for all 11 families in SPEC §6.9, for refinement by Agents 02–04 and synthesis by Agent 05. Every contract includes every field required by SPEC §8, in the required order (the brief counts "19 fields" but lists 21; all listed fields are included here).

**Locked conventions referenced throughout** (from SPEC §6 and the coordinator worklog): class names are kebab-case of family names — `.primary-value-block`, `.metric-group`, `.metric-row`, `.compact-tile`, `.quick-action-rail`, `.operational-row`, `.button`, `.input`, `.state-chip`, `.sheet`, `.dialog`, `.bottom-navigation`, `.top-zone`, `.avatar`, `.chart-*`; spacing scale 2/4/8/12/16/24/32/40; radius 6/12/16/24/full (BottomNavigation radius 0); touch targets 44px minimum, 48px for primary actions; QuickActionRail geometry tile 88×92, icon 24, label 13px, icon-to-label gap 8, tile gap 8, rail padding 16, measured peek 16px at 320px and ≥28px at 360/390/430; Light Mode only; English digits, `DD/MM/YYYY`, currency `د.أ`; motion press 80ms / fast 120ms / normal 200ms / sheet 240–180ms / dialog 160–120ms / scrim 200ms; values bidi-isolated `dir="ltr"`.

---

## 1. PrimaryValueBlock

**Name:** `PrimaryValueBlock` (`.primary-value-block`)

**Purpose:** Present the single most decision-relevant number of a view — the one fact أبو محمد opens the app for — at a size and position that wins the first two seconds of attention.

**When to use:** Exactly once per screen or test composition, for a stock value (`نقد اليوم`, `ذمم العملاء`) or a net value (`صافي اليوم`), placed on the canvas above all other content. Use it whenever one number answers the user's dominant question for that moment.

**When not to use:** Never more than one per viewport; never for secondary or comparative metrics (use `MetricGroup`); never inside a card or sheet as a decorative big number; never for values whose meaning depends on a second number shown elsewhere.

**Anatomy:** Label (13px, ink-muted, optional 16px leading status icon only when a state line exists) → value (`1,284.50`, 32px/600/1.15, ink-strong, tabular-nums, bidi-isolated) with currency mark `د.أ` (15px/500, ink-muted, after the value in RTL flow, so it renders to the digits' visual left) → optional qualifier line (13px, ink-subtle, e.g. `حتى 14:20`) → optional decision-critical state line (13px, semantic color + 20px icon + word, e.g. `بانتظار تحويل 142.00 د.أ`).

**Content hierarchy:** Value first (size 32 and ink-strong), label second, state line third, qualifier last. The number must be understandable without the label within one glance, and the label disambiguates period and scope.

**Sizes:** Value 32px/600/1.15; label and qualifier 13px; block height is content-driven (≈76–96px at default size); full viewport width minus 2×16px edge padding. Values up to 9 characters (digits, separators, sign) fit at 32px on all validated widths.

**Spacing:** 16px screen edges; label-to-value 4px; value-to-qualifier 4px; state line 4px below qualifier; 24px below the block before the next section. All values from the locked scale.

**Radius:** None — the block sits directly on canvas with no background and no border; it is a fact, not a container.

**Surface role:** Canvas `#FAF9F5` only. Never on `surface` or `sunken`, and never given a tinted background; this preserves "the number is the page" native feel.

**Brand role:** None. `brand-ink` is explicitly not a number color (SPEC §6.3); the value is always ink-strong. Brand marks may not frame or badge this block.

**Semantic color role:** Only in the optional state line (one semantic family, counted against the composition's ≤2 budget). A negative net value renders with a leading `-` in ink-strong by default; danger color is permitted only when the negative state itself requires action.

**Variants:** Stock (no sign, `1,284.50`); Net (signed, `-45.50` or `+583.00`); With state line (warning/info); Unavailable (`—` + reason); With trend marker (chart primitive 11.4 adjacent, e.g. `+12%`).

**States:** Ready; Loading (label + 2 skeleton bars, block reserved height, aria-busy); Stale (cached value + qualifier `آخر تحديث 12:40`); Unavailable (`—` with `غير متاح حاليًا` + retry when actionable); value appears immediately on load — no count-up (SPEC §6.11).

**Interaction and motion:** Read-only by default; if a drill-down exists the whole block is one 48px-minimum tap target with 80ms press-overlay and 120ms state fades. No parallax, no entrance animation for the value.

**RTL behavior:** Label right-aligned at reading start; digits in an LTR isolate so `1,284.50` and `-92.50` keep the sign leading; `د.أ` follows logically and appears to the digits' left. Any drill chevron mirrors (points left in RTL).

**Accessibility:** Combined accessible name `label + value + unit`, spoken form uses the full currency word (e.g. "نقد اليوم: 1,284.50 دينار أردني") while the visual stays `د.أ`; AA contrast (ink-strong on canvas ≈ 13:1); survives 200% text via wrapping, no fixed heights; if tappable, focus ring 2px and it announces the destination.

**Arabic copy examples:** `نقد اليوم` / `1,284.50` `د.أ` / `حتى 14:20`؛ `صافي اليوم` / `+583.00` `د.أ`؛ `ذمم العملاء` / `1,175.00` `د.أ` / `عند 4 عملاء`؛ unavailable: `—` / `غير متاح حاليًا`.

**Micro operational examples:** Cash on hand at 14:20 between customers; total receivables before deciding whether to push collections this week; month-to-date sales vs the same moment last week. Companion numbers appear only in `MetricGroup` rows so the block is never duplicated.

**Responsive behavior:** Identical at 320/360/390/430 — 32px value, 16px edges; only qualifier wrapping changes height. If a rare value exceeds 9 characters, drop to 28px/600 as a documented exception (never shrink below).

**Known limitations:** One per viewport; cannot host actions or charts; a state line competes with the follow-up section for the ≤2 semantic families; the 28px fallback is an exception, not a scale step.

---

## 2. MetricGroup

**Name:** `MetricGroup` (`.metric-group`)

**Purpose:** Hold 2–5 secondary values that answer one shared question in a single surface, so أبو محمد compares related numbers by scanning one aligned column instead of many cards.

**When to use:** For the second tier of a view's hierarchy — the flow numbers under a primary stock number (`حركة اليوم`), or detail metrics under a customer/supplier balance. Use after `PrimaryValueBlock` and before lists.

**When not to use:** Not for the dominant number of the view; not when metrics belong to different questions (split into sections instead); not for 6+ rows (becomes a list — use `OperationalRow` or restructure); never as one-card-per-metric grids (SPEC §6.9.2).

**Anatomy:** Optional title (15px/500, ink-strong, e.g. `حركة اليوم`) → 2–5 `MetricRow`s stacked → 1px `line-soft` hairlines between rows → optional group footer qualifier (13px, ink-subtle, e.g. `محدّث قبل دقيقتين`). The surface is the only elevated plane in the immediate area.

**Content hierarchy:** Title (scope of the question) → rows ordered by operational importance, not alphabetically (sales before expenses, collections before returns) → footer qualifier last and smallest.

**Sizes:** Surface full width minus 2×16 edges; row minimum height 44px (tap-safe); typical group ≈ 180–220px for 3 rows; title block ≈ 40px.

**Spacing:** 16px surface padding; 12px vertical row padding; title-to-first-row 8px; between-row hairlines sit inside the 12px paddings; 24px above the group (separating from the rail) and 24px below.

**Radius:** 16px on the surface — the standard "meaningful grouped surface" radius; no radius on rows themselves.

**Surface role:** `surface` `#FFFFFF` on `canvas`; maximum nesting one level (rows are content, never nested surfaces); may not stack over another surface.

**Brand role:** None — no brand tint on the group or its title; the family stays neutral so semantic color reads as meaning, not decoration.

**Semantic color role:** Row values may use positive/danger/warning per direction/status, always counted against the composition budget (≤2 colored numbers, ≤2 families total). Group footer and title never use semantic color.

**Variants:** Titled / untitled; 2–5 rows; aligned-numeric (default) or label-with-qualifier rows; mixed-state group (one unavailable row + two ready rows) is the canonical matrix example.

**States:** Ready; Loading (title + 3 skeleton rows, the SPEC §6.12 rule); a group is never partially interactive — if rows are tappable, all rows are.

**Interaction and motion:** Rows may tap through to a drill sheet (80ms press overlay, radius 12 feedback within the surface); group itself has no gesture; state changes fade at 120ms; no staggered entrance animation.

**RTL behavior:** Title at reading start (right); every row keeps label at start and value at end (visual left) so all values form one left-edge numeric column; hairlines run full inner width.

**Accessibility:** Exposed as a list (`role="list"`, rows `role="listitem"`) or as a definition region with per-row accessible names (`مبيعات اليوم: 465.00 دينار`); loading announced once ("جاري التحميل"), not per row; sign and state included in the row's accessible name.

**Arabic copy examples:** `حركة اليوم` → `مبيعات اليوم 465.00 د.أ`، `تحصيلات ذمم +210.00 د.أ`، `مصروفات اليوم -92.50 د.أ`؛ footer `محدّث قبل دقيقتين`؛ `ملخص الأسبوع` → `إجمالي المبيعات 2,730.00 د.أ`، `إجمالي التحصيلات 860.00 د.أ`، `تسويات بانتظار —`.

**Micro operational examples:** The today-movement trio under `نقد اليوم`; customer detail (`رصيد أبو أحمد` + `آخر دفعة` + `أقدم فاتورة`); supplier detail before reordering flour.

**Responsive behavior:** Width follows the viewport minus 32px; value column keeps 2-decimal tabular alignment at all widths; at 200% text, rows wrap the label under the value only when a single line cannot hold both — value alignment column never breaks.

**Known limitations:** ≤5 rows; hairlines consume divider budget (2 for 3 rows — plan the whole composition around the ≤3 cap); cannot mix interactive and non-interactive rows; no horizontal variant.

---

## 3. MetricRow

**Name:** `MetricRow` (`.metric-row`)

**Purpose:** One label plus one aligned numeric value on a single row — the atomic unit of comparison inside `MetricGroup`, making direction and magnitude legible at a glance.

**When to use:** Inside a `MetricGroup` for any secondary metric; also as a compact detail line in a sheet (e.g. outstanding balance under a collection form). Use wherever a label-value pair must scan as one line.

**When not to use:** Not as the view's primary number; not for operational entries that carry identity, time, and state (that is `OperationalRow`); not as a list of tappable records (rows here are data, not transactions); not freestanding on canvas without a group context except in sheets.

**Anatomy:** Label (15px/400, ink, right/start) → optional 13px qualifier under the label (e.g. `الحد 6`) → value at row end (15px/500, tabular-nums, ink-strong, bidi-isolated, 2 decimals, explicit sign for directional metrics) → optional 20px status icon or 28px state chip before the value.

**Content hierarchy:** Value is the strongest element (weight 500); label explains it; qualifier refines it; icon/chip state the condition. A row must read value-first for a scanner tracking the left column.

**Sizes:** Height ≥44px; label 15px; value 15px/500; qualifier 13px; icon 20px (row sizing per SPEC §6.6); chip 28px tall.

**Spacing:** 12px vertical padding; ≥8px between label block and value column; qualifier 2px under label; icon-to-value 4px; rows separated by group hairlines or 8px in sheets.

**Radius:** None for the row; press feedback (when tappable) uses radius 12 matching the parent surface insets.

**Surface role:** Transparent — lives inside `MetricGroup`'s surface or a sheet's content; never gets its own background, border, or card.

**Brand role:** None. Values and labels are ink-family only; brand color on a metric would falsely signal identity rather than meaning.

**Semantic color role:** Positive for confirmed inflows (`+210.00`), danger for action-required negatives only, warning for attention (`تجاوز المخطط`); unavailable uses `—` + 13px reason with no color. Sign always precedes color as the direction signal (SPEC §6.12).

**Variants:** Neutral (`465.00`); Positive (`+210.00`, positive); Negative (`-92.50`, ink-strong + sign only — canonical sign-first example); Attention (warning value + chip, e.g. fuel spend over plan); Unavailable (`—` + `غير متاح حاليًا`).

**States:** Ready; Unavailable; Loading (inline 80×12 skeleton replacing value, label persists); Attention is a content condition, not a loading state, and must not pulse.

**Interaction and motion:** Tap-through to a drill sheet when the row has a destination (80ms press, 120ms sheet open per sheet timing); value changes never animate numerically — old value is replaced immediately with a 120ms crossfade.

**RTL behavior:** Label at start (right), value column pinned to end (left) so the numeric column is vertically continuous across rows; sign and digits inside `dir="ltr"` isolates; qualifiers wrap right-aligned under labels; status icons sit at the value's start (its right side) and never mirror.

**Accessibility:** Accessible name merges label, qualifier, signed value, unit, and state ("مصروفات اليوم: سالب 92.50 دينار") — the screen-reader form spells the sign; unavailable rows announce the reason; contrast of ink on white ≈ 10:1; rows are ≥44px so tappable versions meet touch minimums.

**Arabic copy examples:** `مبيعات اليوم — 465.00 د.أ`؛ `تحصيلات ذمم — +210.00 د.أ`؛ `مصروفات اليوم — -92.50 د.أ`؛ `مصروف الوقود — 96.00 د.أ — تجاوز المخطط`؛ `تسويات بانتظار — — — غير متاح حاليًا`.

**Micro operational examples:** The three `حركة اليوم` rows in the test composition; `أقدم فاتورة — 24/08/2026` and `آخر دفعة — اليوم 12:40` in أبو أحمد's detail; `متبقي — 240.00 د.أ` in the collection sheet.

**Responsive behavior:** At 320px label truncates to one line with ellipsis (full text goes to accessible name and drill sheet) before the value column ever narrows; value column minimum ~96px holds `-1,284.50 د.أ` at 15px tabular at all widths.

**Known limitations:** One value per row (no dual values — use `CompactTile` pair); long Arabic labels truncate; colored values consume the composition's colored-number budget even when subtle; unavailable rows cannot be tappable.

---

## 4. CompactTile

**Name:** `CompactTile` (`.compact-tile`)

**Purpose:** Show exactly two related values side by side as one genuine comparison — "what is owed to me vs what I owe" — or serve as a QuickActionRail tile; a paired, glanceable mini-surface.

**When to use:** For a single comparison pair in a composition (`ذمم العملاء` vs `ذمم المورّدين`, `مخطط` vs `فعلي` summary, `مستحق لك` vs `مستحق عليك`); and as the locked 88×92 rail tile for quick actions. Both tiles of a pair must answer one question.

**When not to use:** Never as a generic mini-card grid (SPEC §6.9.4) — no 3-up or 4-up tile rows; not for primary values; not as decoration or stat chrome; not to repeat a value already shown in `PrimaryValueBlock` or `MetricGroup` (no repeated key value).

**Anatomy:** Label (13px, ink-muted) → value (17px/600, tabular, ink-strong, bidi-isolated, `د.أ` unit at 13px/500) → optional qualifier (13px, ink-subtle, e.g. `عند 4 عملاء`) → optional 20px icon at label level. Pair = two tiles with 12px gap; the pair may carry an implicit shared question via a 13px section line above (no header surface, no divider).

**Content hierarchy:** Value dominates (600 weight); label defines the key; qualifier adds count or counterparty; icon is optional reinforcement only.

**Sizes:** Pair tile width = (viewport − 32 − 12) / 2 (≈173px at 390px); min height 84px; rail tile fixed 88×92 (locked); internal padding 12px.

**Spacing:** Pair gap 12px; edge alignment 16px to viewport; label-to-value 4px; value-to-qualifier 4px; 24px above/below the pair section.

**Radius:** 12px (compact surface, subordinate to MetricGroup's 16); rail tiles also 12px.

**Surface role:** `surface` `#FFFFFF` for pair tiles (each tile is one of the composition's ≤3 surfaces); rail tiles are canvas-level with `sunken` or tinted backgrounds per rail rules — the rail variant is not an elevated surface.

**Brand role:** In the rail only — exactly one tile may use `brand-tint` (the primary action `إضافة بيع`), and no pair tile may carry brand fill; pair tiles stay neutral.

**Semantic color role:** Default none (both values ink-strong — comparisons stay calm); a value may take semantic color only when it is decision-critical and it counts toward the ≤2 colored-number and ≤2 family budgets; a tiny warning dot may flag "overdue exists" without coloring the number.

**Variants:** Comparison-pair tile; Rail tile (88×92, icon 24 + label 13px stacked, one brand-tinted max); Unavailable tile (`—` + `غير متاح حاليًا`).

**States:** Ready; Loading (skeleton 12×48 + 12×84 per tile); Pressed (80ms overlay, radius 12); Unavailable; the pair never shows mixed loading states — both load together.

**Interaction and motion:** Tap opens the tile's drill sheet (both pair tiles and rail tiles); press overlay 80ms; sheet opens 240ms; no hover states (phone-only); no swipe.

**RTL behavior:** In a pair, the primary/first tile sits at reading start (right), e.g. `ذمم العملاء` right of `ذمم المورّدين`; labels right-aligned; values keep LTR digit isolates; rail tiles scroll RTL with `إضافة بيع` rightmost.

**Accessibility:** Each tile is a labeled button whose accessible name merges key, value, unit, qualifier ("ذمم العملاء: 1,175.00 دينار، عند 4 عملاء"); the pair is wrapped in a group labeled with the shared question ("مقارنة الأرصدة"); 84px+ targets exceed the 44px minimum.

**Arabic copy examples:** `ذمم العملاء — 1,175.00 د.أ — عند 4 عملاء` | `ذمم المورّدين — 640.00 د.أ — مؤسسة الشرق`؛ `مستحق لك — 1,175.00 د.أ` | `مستحق عليك — 640.00 د.أ`؛ `طلبات اليوم — 18` | `جاهزة للتسليم — 4`.

**Micro operational examples:** The receivables-vs-payables pair in the test composition; a plan-vs-actual weekly summary pair in a details sheet; rail tiles per the locked five actions.

**Responsive behavior:** Pair width derives from viewport; at 320px each tile ≈138px and qualifiers wrap to two lines (content-driven height, no truncation of values); rail tile geometry never changes at any width (locked).

**Known limitations:** Exactly two tiles per comparison — never 1 or 3+; a pair consumes 2 of the 3 allowed surfaces; rail variant geometry is frozen; tiles cannot contain charts or actions.

---

## 5. OperationalRow

**Name:** `OperationalRow` (`.operational-row`)

**Purpose:** Present one real operational entry — a transaction, follow-up, threshold, or exception — with who/what, when, how much, and what state it is in, so the row itself is the record أبو محمد acts on.

**When to use:** All repeating operational lists: today's follow-ups, customer/supplier activity, material thresholds, exceptions needing resolution. Rows sit directly on canvas (default) or inside one grouped surface when the list is a subsection of a sheet.

**When not to use:** Not for label-value metrics without identity or time (`MetricRow`); not for one-off summary values; not inside multiple per-row cards (never card-per-entry); not for the primary number.

**Anatomy:** Leading status icon (20px, semantic color, only when a state exists) → title (15px/500, ink-strong: counterparty, material, or entry type) → meta line (13px, ink-muted: action + time/date, bidi-isolated dates) → trailing amount (15px/500, tabular, end-aligned, `د.أ`) → optional state chip (28px: tint background, 20px icon, 13px word, radius 6) → optional trailing quiet action (e.g. `إعادة المحاولة` on failed rows).

**Content hierarchy:** Title identifies, meta contextualizes, amount quantifies, state chip governs urgency; the amount column aligns across all rows so totals-vs-items scan vertically.

**Sizes:** Min height 56px; icon 20px; title 15px; meta 13px; amount 15px/500; chip 28px; 20-row batch, prefetch triggered within the last 5 rows, 3 skeleton rows while fetching (SPEC §6.12).

**Spacing:** 12px internal vertical padding; title-to-meta 2px; icon-to-title 8px; meta-to-amount ≥8px; row-to-row 12px on canvas (no dividers — spacing separates) or hairline inside a grouped surface; 24px between sections.

**Radius:** Transparent rows; press feedback radius 12; rows inside a sheet list take the parent's 16 with internal 12 paddings.

**Surface role:** Canvas-level by default (line-based, no individual cards); optionally one grouped `surface` when embedded in a sheet; never `sunken` per row.

**Brand role:** None — rows never carry brand tint or brand icons; identity stays in data, not chrome.

**Semantic color role:** Status icon and chip carry the state family (warning pending/overdue/threshold, positive completed, danger failed, info in-progress when budgeted); amounts stay ink-strong with signs — a colored amount is exceptional (counts toward ≤2 colored numbers, e.g. the threshold quantity `4`).

**Variants:** Entry row (recorded transaction); Follow-up row (pending/overdue, since-date); Threshold row (material, quantity vs limit); Exception row (failed/conflict, with retry action); Cancelled/Reversed row (muted amount + chip, entry preserved in history).

**States:** Default; Completed (positive check icon, amount unchanged, chip `تم` optional); Pending (warning clock + `بانتظار التحويل` + `منذ 05/09/2026`); Failed (danger chip `فشل الإرسال` + visible `إعادة المحاولة` button — automatic retries stopped after the first failure, SPEC §6.12); Conflict (chip `عملية مشابهة` + action opens comparison); Cancelled (`أُلغيت`, amount in ink-muted); Reversed (`معكوسة` + qualifier `عُكست العملية — أُضيف قيد مقابل`); Loading (3 skeleton rows).

**Interaction and motion:** Tap opens the row's detail sheet (240ms in / 180ms out, scrim 200ms); press overlay 80ms; state transitions (pending→completed) crossfade 120ms with the check appearing — no slide, no confetti; trailing retry button is a 44px quiet button; no destructive swipe on financial rows (documented decision — mis-swipes must not delete money records).

**RTL behavior:** Icon and title at start (right), amount at end (left) forming the numeric scan column; dates like `05/09/2026` bidi-isolated; `منذ` prefixes read naturally before the isolate; chevrons mirror; status icons never mirror.

**Accessibility:** Each row is one focusable target with a full accessible name: state, title, meta, amount ("بانتظار التحويل، شركة التوصيل السريع، 142.00 دينار، منذ 05/09/2026"); failed rows expose retry as a separate focusable action inside the row; loading region announces once; state changes announced politely (aria-live) so completion is provable non-visually.

**Arabic copy examples:** `شركة التوصيل السريع — بانتظار التحويل — منذ 05/09/2026 — 142.00 د.أ`؛ `أبو أحمد — تحصيل دين — اليوم 12:40 — 120.00 د.أ`؛ `طحين فاخر 10كغ — متبقي 4 أكياس — الحد 6`؛ `مؤسسة الشرق للتجهيزات — شراء آجل — 06/09/2026 — 350.00 د.أ`؛ `مطعم النخيل — طلب جديد — بانتظار التأكيد — 96.00 د.أ`.

**Micro operational examples:** The three `متابعة اليوم` rows; a supplier purchase on credit; a collection just completed; a failed offline entry waiting for manual retry; a reversed correction that must remain auditable.

**Responsive behavior:** Title truncates at one line with ellipsis (full identity in sheet) before meta or amount compress; at 320px meta may drop the time-of-day keeping the date; amount column minimum ~96px; chips never wrap — wording is capped at ~14 Arabic characters.

**Known limitations:** No per-row cards, no nested rows, one trailing action maximum; colored amounts are budget exceptions; batch/prefetch numbers are contract-level and must be implemented, not simulated; 320px truncation relies on the sheet carrying full data.

---

## 6. Button

**Name:** `Button` family (`.button`)

**Purpose:** Commit the user's decision — record, collect, retry, confirm, dismiss — with one unambiguous action per context and a state that proves the outcome.

**When to use:** One primary button per sheet or dialog (the commit action); secondary/quiet buttons for alternatives; icon-only where a label would repeat adjacent text; every form ends in a button, never a link.

**When not to use:** Not as navigation (rows/tiles navigate); not more than one filled primary per viewport (SPEC §6.3); not for destructive defaults (danger is never the default focus); not pills-everywhere (radius discipline, SPEC §6.5); no toasts as the only completion proof.

**Anatomy:** Label (15px/500, single line, ≤3 words) → optional leading icon (20px, mirrors only if directional) → optional trailing chevron (mirrors) → loading replaces label area with a 20px spinner + `جاري الحفظ…` keeping the button's width stable.

**Content hierarchy:** Label is the contract; icon is optional reinforcement; state changes (loading → completed) happen inside the same footprint so the target never moves.

**Sizes:** Primary height 48px, full-width in sheet action bars; secondary 44px; quiet/text 44px target with 15px label; icon-only 44×44 with 20–24px icon; padding-h 16; min width 88px for text buttons.

**Spacing:** In-sheet action bar padding 16, single full-width CTA or primary + quiet secondary stacked with 8px gap; inline pairs gap 8; label-to-icon gap 8.

**Radius:** 12px for filled/secondary; 6px press feedback on quiet buttons; full (circle) reserved for icon-only buttons; never pill text buttons.

**Surface role:** Filled primary uses `brand-ink` `#964E33` with white label (the limited filled text-bearing CTA per SPEC §6.3); secondary uses `surface` with `line-strong` border; quiet uses transparent/canvas.

**Brand role:** The one filled brand-family action per viewport is the primary CTA (in sheets — the overlay counts as the active layer); on-canvas primary actions are expressed through the tinted rail tile instead, so canvas and brand stay calm.

**Semantic color role:** Destructive confirm uses danger-filled (white text) inside its dialog; quiet destructive text buttons use danger for the label with an icon; positive is never a button fill — completion is a quiet state, not a green button.

**Variants:** Primary (filled brand-ink); Secondary (surface + border); Quiet/text; Destructive (filled in dialog, quiet elsewhere); Icon-only (circle, aria-label); Loading; Disabled (ink-disabled label, no overlay); Focused (2px ring, 2px offset); Pressed (8% press-overlay); Quiet completion (check icon + `تم` fading in at 120ms, settling for ≥1.5s before context dismiss).

**States:** Default; Pressed (80ms overlay); Focused (persistent visible ring); Loading (spinner + label swap, aria-busy, width locked); Disabled (not pressable, aria-disabled, remains in reading order); Completed (check + `تم`); completion is the proof mechanism for recording flows.

**Interaction and motion:** Press 80ms, state fades 120ms, no bounce/spring; loading buttons keep their footprint; on success the button becomes quiet completion, then the sheet exits (180ms) and the originating row/state updates inline; failures stop retries after the first attempt and expose `إعادة المحاولة`.

**RTL behavior:** Label centered (full-width CTAs) or start-aligned; leading icons sit at the label's right; directional icons (chevrons, arrows) mirror, `+`/check/clock do not; loading spinner rotation direction is unchanged (motion, not semantics).

**Accessibility:** 48/44px targets; visible 2px focus ring with 3:1 non-text contrast; loading announced ("جاري الحفظ"); completed announced ("تم تسجيل البيع"); disabled uses aria-disabled and explains why when relevant; icon-only buttons carry aria-labels (`إضافة`, `مسح البحث`).

**Arabic copy examples:** `تسجيل البيع`، `تحصيل`، `حفظ`، `تأكيد`، `إلغاء`، `حذف`، `إعادة المحاولة`، `إرسال التذكير`، `عرض الكل`، `جاري الحفظ…`، `تم`، `متابعة التعديل`، `تجاهل`.

**Micro operational examples:** `تسجيل البيع` in the sale sheet (primary, full width, 48px); `إعادة المحاولة` beside a failed offline entry; `تأكيد الاستلام` in the delivery settlement sheet; `حذف` + `إلغاء` in the destructive dialog.

**Responsive behavior:** Full-width primary in sheets at all four widths; inline pairs collapse to stacked (primary above secondary) below ~340px; labels never wrap — a 320px-failing label is rewritten, not shrunk.

**Known limitations:** One filled primary per viewport; loading label swap needs reserved width to avoid jumps; destructive fills are dialog-only; completion state cannot be skipped for recording flows.

---

## 7. Input

**Name:** `Input` family (`.input`)

**Purpose:** Capture the small set of fields a fast entry flow needs — amount, party, date, category, payment mode — with validation that prevents bad records rather than punishing them after.

**When to use:** Inside entry sheets (`إضافة بيع`, `تحصيل`, `إضافة مصروف`, `إضافة شراء`, `تسجيل دفعة`); search fields above lists; segmented controls and tabs for mode/period switches; checkbox only for deferred flags; switch only for immediate settings.

**When not to use:** Not on the canvas or main composition (inputs live in sheets); not for browsing choices that fit a sheet list; no switches for anything requiring a save step; no multi-line rich text in this library's scope.

**Anatomy:** Label (13–15px, ink, above, always visible — never placeholder-as-label) → field (48px height, `surface` fill, 1px `line-strong` border, 12px padding) → optional affix: `د.أ` unit (13px/500 ink-muted) for amounts, mirrored chevron for selections, search icon at start / clear button at end for search → helper/error line (13px, 4px below).

**Content hierarchy:** Label → current value → helper; the value uses tabular-nums and 15px/500; placeholders (ink-subtle, e.g. `0.00`) mark empty input and are never committed as values.

**Sizes:** Field height 48px (meets primary target); segmented control 44px; checkbox visual 20px on a 44px target; switch visual 48×28 on a 44px target; tabs 44px with 2px active underline.

**Spacing:** Label-to-field 8px; field-to-helper 4px; between fields 12px; sheet form padding 16; segmented segments padding-h 12.

**Radius:** Fields and segmented containers 12; inner selected segment 6; checkbox 6; switch track full (pill is its native geometry, not a styled control).

**Surface role:** Fields are `surface` on the sheet's surface (single nesting level — the sheet itself is the elevated plane); focused fields keep surface fill and gain the focus ring, not a new surface.

**Brand role:** Focus rings may use `brand-atmosphere` (2px) — the only brand appearance; selection states (segmented, tabs, checkbox check) use ink-strong on `sunken`/tint-neutral fills, not brand fills.

**Semantic color role:** Error border and message use danger; no positive fields; date/mode segments are neutral. Error is one family and rarely coexists with another in a sheet.

**Variants:** Text; Amount (numeric, `د.أ` affix, `dir="ltr"` content, placeholder `0.00`, thousands grouping on commit); Search (icon, clear, filters list below); Date (displays `DD/MM/YYYY`, opens picker sheet, quick chip `اليوم`); Selection (opens searchable sheet list, shows chosen value); Segmented (`نقدي | آجل`); Tab (`اليوم | الأسبوع | الشهر`); Checkbox (`تنبيه عند وصول التحويل`); Switch (immediate settings, `تذكير بالمتابعات`).

**States:** Default; Focused (2px ring + border emphasis); Filled; Error (danger border + message `أدخل مبلغًا أكبر من صفر` / `التاريخ غير صالح`, announced); Disabled; Loading (selection inputs show 3 skeleton list rows in their sheet); empty input is a state of value, shown only by placeholder styling — never as `0.00`.

**Interaction and motion:** Focus ring appears without motion; 80ms press on segmented/tabs; switch toggles instantly (no slide animation beyond 80ms knob shift); date picker sheet uses standard sheet timing; amount validation runs on commit, grouping separators applied on blur; error messages appear at 120ms fade, never shake.

**RTL behavior:** Labels and values right-aligned; amount content is LTR-isolated with the unit affix rendered outside the isolate at the field's visual end (left) — same convention as display values; search icon at start (right), clear at end (left); selection chevron mirrors (points left); segmented order RTL (`نقدي` rightmost); tabs order RTL.

**Accessibility:** Every field programmatically labelled; errors linked via aria-describedby and announced politely; switch and checkbox announce state changes; date fields expose their `DD/MM/YYYY` format in the accessible description; 48px fields meet targets; focus never trapped in sheets without a dismiss path.

**Arabic copy examples:** `المبلغ` / `0.00` / `د.أ`؛ `اسم العميل` / `ابحث أو أضف جديدًا`؛ `التاريخ` / `08/09/2026` / `اليوم`؛ `الفئة` / `اختر الفئة`؛ `طريقة الدفع` / `نقدي | آجل`؛ `ابحث عن عميل أو عملية`؛ `ملاحظة (اختياري)`؛ errors: `أدخل مبلغًا أكبر من صفر`، `التاريخ غير صالح`، `اختر العميل أولًا`.

**Micro operational examples:** The `إضافة بيع` sheet (customer selection + amount + `نقدي | آجل` + date defaulting to `اليوم`); `تحصيل من أبو أحمد` with quick-fill chip `المتبقي 240.00 د.أ`; expense category selection; purchase quantity in أكياس with computed total.

**Responsive behavior:** Full-width fields minus sheet padding at all widths; segmented controls never scroll — modes are capped at two options; tabs cap at three (`اليوم | الأسبوع | الشهر`) which fits 320px; long Arabic labels wrap above fields, field height stays 48px.

**Known limitations:** No dark variants, no file upload, no rich text; amount grouping applies on blur (during typing digits stay plain); date entry relies on the picker sheet for correctness; search is the only input allowed above a list.

---

## 8. State

**Name:** `State` family (`.state-chip`, `.state-line`, `.skeleton`)

**Purpose:** Tell the truth about data condition — empty, loading, error, offline-saved, pending, conflict, failed, completed, cancelled, reversed — in wording a busy owner can act on, without illustration theatre or color-only signals.

**When to use:** Inline within rows, forms, sheets, and list regions wherever a condition changes what أبو محمد should do next; every list implements empty/loading/error at minimum; recording flows additionally implement offline-save, failed, and completed.

**When not to use:** Not as full-screen decorative states; not as toasts carrying the only proof of an outcome (SPEC §6.11); not as technical sync vocabulary in primary content; not for states the user cannot act on or that change nothing ("synced at 14:20" under a cash figure is noise).

**Anatomy:** State chip (28px: 20px icon + 13px word, semantic-tint background, semantic icon+text, radius 6) for row-embedded states; State line (one 13–15px line + optional 44px quiet action button) for empty/error/offline in list regions; Skeleton (3 sunken-colored blocks shaped like the content they replace) for loading; inline status line in forms (icon + word + optional detail).

**Content hierarchy:** Word and icon carry meaning; tint is third; the action (when one exists) is the resolution. Empty states show the line + exactly one useful action (`سجّل بيعًا`), never a stack of links.

**Sizes:** Chip height 28px (≥44px hit only when the whole row is the target); line 13–15px; skeleton blocks mimic replaced geometry (row skeletons ~56px); 3 skeleton rows standard (SPEC §6.12).

**Spacing:** Chip padding-h 8, icon-word gap 4; line padding 16 to viewport edges; action-to-line gap 8; skeleton gaps mirror real row gaps (12px).

**Radius:** Chips 6; skeleton blocks 6 (or matching the component they replace, e.g. 12 for tiles); lines have no geometry.

**Surface role:** Chips sit on whatever surface hosts them (tint is a semantic role, not a fourth surface); skeleton blocks use `sunken`; state lines sit on canvas or surface without their own container.

**Brand role:** None — states are semantic territory; brand never communicates condition.

**Semantic color role:** warning = pending/overdue/threshold; positive = completed/confirmed; danger = failed/destructive; info = in-progress when needed. Each chip pairs tint background + semantic icon + semantic text; ≤2 families per composition; cancelled/reversed are neutral (ink-muted) to stay quiet and historic.

**Variants:** Empty (line + action); Loading (3 skeletons, aria-busy); Error (line + `إعادة المحاولة`, no automatic retry after the first failure); Offline local-save (`محفوظ على الجهاز` + `يُرسل عند عودة الاتصال`); Pending (`بانتظار التحويل` + since-date); Conflict (`عملية مشابهة موجودة` + view/override actions); Failed (`فشل الإرسال` + retry); Completed (check + `تم` inline at origin); Cancelled (`أُلغيت`); Reversed (`معكوسة` + `عُكست العملية — أُضيف قيد مقابل`).

**States:** The family itself enumerates states; each variant additionally has appear/disappear transitions (120ms fade) and reduced-motion equivalents (instant swap, meaning preserved).

**Interaction and motion:** Error/offline states expose their retry as a real 44px button; completed checks fade in 120ms; skeletons pulse via a restrained 200ms opacity loop (0.6→1) that becomes static under reduced motion; no state auto-dismisses a failure — the user decides.

**RTL behavior:** Icon before word at reading start (right); since-dates bidi-isolated; chips inline-flow with the row's end alignment; skeleton geometry mirrors the RTL layout it replaces.

**Accessibility:** Condition changes announced politely ("فشل الإرسال" / "تم تسجيل البيع"); skeletons use aria-busy on the region with visuals aria-hidden; every state is word+icon — never color alone (SPEC §6.3); retry actions are keyboard-focusable and announced with context.

**Arabic copy examples:** `لا عمليات اليوم` + `سجّل بيعًا`؛ `لا نتائج مطابقة` + `مسح البحث`؛ `جاري التحميل`؛ `تعذّر التحميل` + `إعادة المحاولة`؛ `محفوظ على الجهاز` / `يُرسل عند عودة الاتصال`؛ `بانتظار التحويل منذ 05/09/2026`؛ `عملية مشابهة موجودة`؛ `فشل الإرسال`؛ `تم` / `تم التسجيل` / `تم التحصيل`؛ `أُلغيت`؛ `معكوسة`.

**Micro operational examples:** An offline collection saved in the bakery's basement showing `محفوظ على الجهاز` with the queue icon; a duplicated `إضافة بيع` attempt flagged `عملية مشابهة موجودة` with `عرض الموجودة` / `تسجيلها مع ذلك`; a threshold row showing `متبقي 4 أكياس`; a settlement flipping from `بانتظار التحويل` to `تم` inline.

**Responsive behavior:** Identical mechanics at 320–430; chips never wrap (wording capped); lines wrap to two lines maximum with the action below; skeletons always match the real layout width so swapping causes no reflow.

**Known limitations:** No illustrations, no auto-retry, no toast-only proof; conflict resolution needs the comparison sheet (extra surface); offline wording cannot promise timing, only order; ≤2 semantic families per composition constrains mixing warning+danger+info in one view.

---

## 9. Sheet & Dialog

**Name:** `Sheet` and `Dialog` (`.sheet`, `.dialog`)

**Purpose:** Focus one decision at a time over a dimmed context — sheets for recording, selecting, and details; dialogs for short binary confirmations — then return focus to exactly where the user was.

**When to use:** Sheets: all quick-action flows (sale, collection, expense, purchase, payment), pickers (customer/supplier/material), settlement follow-up details, the More menu. Dialogs: destructive confirmation (`حذف العملية؟`) and dirty-dismiss guard (`تجاهل التغييرات؟`). Decision rule: if it has an input, a list, or scrolling → sheet; if it is two choices over existing context → dialog.

**When not to use:** No dialogs containing form fields; no sheet stacks deeper than one (a picker opened from a sheet replaces it); no desktop drawers or centered popups for entry flows; no bottom sheets used as persistent panels.

**Anatomy:** Sheet: scrim (`#1F1E1D` 45%) → container (surface, top radius 24, full width) → drag handle (32×4, `line-strong`, 8px from top) → title (16px/600, ink-strong, 12px below handle) → content (form/list/detail, 16px padding) → action bar (16px padding, 12px from content, primary full-width 48px CTA; optional quiet secondary above it with 8px gap). Dialog: scrim → container (radius 16, width = viewport − 2×40) → title (15px/600) → body (13–15px, ≤2 lines) → actions (destructive + quiet, 8px gap, 44px).

**Content hierarchy:** Title states the decision; content is the minimum needed to decide; the primary CTA is the last, lowest, thumb-nearest element — the action lives in the thumb zone by construction.

**Sizes:** Sheet default medium (~70% viewport height), full mode for multi-step flows (purchase with items); dialog ≤ 320×~200; handle 32×4; CTA 48px.

**Spacing:** Sheet paddings 16; handle-to-title 12; title-to-content 12; content field gaps 12; action bar gap 12; dialog padding 16, title-to-body 8, body-to-actions 16.

**Radius:** Sheet top corners 24; dialog 16; both radius 0 at the screen edge (sheet sits edge-to-edge).

**Surface role:** Sheet container is `surface` (the elevated plane); its internal inputs use the same single nesting level; dialog is `surface` centered over scrim.

**Brand role:** The sheet's primary CTA is the one filled `brand-ink` action of the active overlay; dialog destructive uses danger fill; no brand on scrims or handles.

**Semantic color role:** Only through content (state chips, error helpers); sheet chrome itself is neutral; the scrim is fixed ink-based, never tinted.

**Variants:** Medium sheet; Full sheet; Detail sheet (read + actions, no form); Picker sheet (search + 20-row batch list + prefetch + 3 skeletons); More menu sheet (`المورّدون`، `شركات التوصيل`، `التقارير`، `الإعدادات`); Confirm dialog (destructive); Guard dialog (discard changes); Conflict dialog variant shows both entries compactly.

**States:** Entering (sheet 240ms up / dialog 160ms fade-scale-less); Exiting (180/120ms); Scrim (200ms); Dragging (finger-follow, release past 40% height or sufficient velocity dismisses; no bounce); Dirty guard (dismiss attempt on edited form → `تجاهل التغييرات؟` with `متابعة التعديل` / `تجاهل`); Loading (CTA enters loading, sheet stays); reduced motion: sheets and dialogs cross-fade in place (no spatial animation), meaning preserved (SPEC §6.11).

**Interaction and motion:** Dismiss by scrim tap, handle drag, or back gesture; focus is trapped inside while open and returns to the trigger on close; scrim never scrolls the page behind; all timing values locked (240/180, 160/120, 200).

**RTL behavior:** Sheets rise from the bottom regardless of direction; titles start-aligned (right); drag physics direction-agnostic; dialog actions order: primary/confirm at the bottom or at reading end — destructive confirm (`حذف`) placed at the end position with `إلغاء` adjacent, separated by 8px minimum.

**Accessibility:** `role="dialog"` + `aria-modal=true`; focus trap with escape via the dismiss affordances; on close, focus returns to the trigger element; titles labelled; scrim tap is keyboard-accessible via a close button in the sheet (44px icon-only, top start); drag-to-dismiss has a keyboard equivalent (`إلغاء`); reduced-motion respected.

**Arabic copy examples:** Titles: `إضافة بيع`، `تحصيل من أبو أحمد`، `شراء من مؤسسة الشرق للتجهيزات`، `تسوية شركة التوصيل السريع`، `حذف العملية؟`، `تجاهل التغييرات؟`؛ actions: `تسجيل البيع`، `تحصيل`، `تأكيد الاستلام`، `إرسال التذكير`، `حذف`، `إلغاء`، `متابعة التعديل`، `تجاهل`.

**Micro operational examples:** Recording a 96.00 sale to مطعم النخيل (`نقدي | آجل` segmented, date defaulting to `اليوم`); collecting 120.00 from أبو أحمد with the `المتبقي 240.00 د.أ` quick-fill; confirming receipt of the 142.00 delivery settlement; guarding an abandoned expense form.

**Responsive behavior:** Full-width sheets at all four widths with 16px content padding; dialog width = viewport − 80px; at 320px the action bar keeps the full-width CTA and moves secondary actions inline above it; heights are content-driven within the mode cap.

**Known limitations:** One sheet at a time; no nested pickers (replace instead); dialogs cannot scroll — content that overflows becomes a sheet; drag-dismiss velocity threshold needs device testing; guard dialogs add one step to every abandoned flow (accepted for financial safety).

---

## 10. BottomNavigation + integrated top zone (Avatar)

**Name:** `BottomNavigation`, `TopZone`, `Avatar` (`.bottom-navigation`, `.top-zone`, `.avatar`)

**Purpose:** Give the app exactly two pieces of structure: a persistent bottom bar that switches the four primary destinations plus More, and a content-integrated top zone that orients (business + date) with one Avatar entry to profile/settings.

**When to use:** BottomNavigation on every top-level view — it is the only persistent chrome (SPEC §6.7). TopZone on every canvas-scrolled view. Avatar only inside the top zone — one entry, never duplicated elsewhere.

**When not to use:** No top app bars, no toolbars, no hamburgers, no floating tabs; no second navigation row; no badge farms on nav icons; the top zone must not become sticky chrome or gain actions.

**Anatomy:** BottomNavigation: five seats (4 destinations + `المزيد`), each seat = 24px icon + 4px gap + 14px label, height 64px + safe-area, edge-to-edge, radius 0. TopZone: business name (15px/600) over full date (13px, `الثلاثاء 08/09/2026`) at reading start; Avatar 32px circle (initials or photo) at reading end with an invisible 44px hit area. Active seat: ink-strong icon+label (600) + 24×3px indicator bar in `brand-atmosphere` at the seat's top edge.

**Content hierarchy:** Nav: icon identifies, label confirms, indicator marks position. Top zone: name over date — day of week matters because "yesterday's cash" is a common confusion; Avatar is visually last.

**Sizes:** Seats 64px+ wide (≥44 target each); icons 24px/2px stroke; labels 14px; Avatar 32px visual; indicator 24×3px.

**Spacing:** Nav internal icon-to-label 4; seat padding-h 8 within 64–86px seat widths; top zone 16 edge padding, name-to-date 4, vertical padding 8.

**Radius:** BottomNavigation 0 (edge-to-edge, SPEC §6.5); Avatar full; indicator bar full ends.

**Surface role:** BottomNavigation sits on `surface` with a top `line-soft` hairline (does not consume the divider budget — it is chrome, not content, documented for Agent 04 to verify); top zone is transparent canvas.

**Brand role:** The 24×3px active indicator bar is `brand-atmosphere` — a calm identity mark, not a fill; no brand-tint pills behind icons (the viewport's brand-tint budget belongs to the rail tile).

**Semantic color role:** None in chrome; an optional count badge on `اليوم` (follow-ups) uses warning-tint + warning text + number — icon-free is acceptable because the count itself is the signal, but it must repeat in the section header count `3`.

**Variants:** Nav: default / active / pressed (80ms overlay) / focused (2px ring on the seat) / with-count-badge. Top zone: default / scrolled-away (it is content — no sticky variant) / with greeting? (no — context only).

**States:** Active (`aria-current="page"`); pressed; focused; badge states inherit the count's semantics; Avatar pressed (overlay) and focused.

**Interaction and motion:** Seat tap switches destination with a 120ms content crossfade (no page-slide, SPEC §6.11); badge count updates with a 120ms fade; `المزيد` opens its sheet (240ms) — it is a real destination, never a disabled seat.

**RTL behavior:** Seats in RTL order — `اليوم` rightmost, `المزيد` leftmost; indicator bar keeps its top position; top zone name at right, Avatar at left; date bidi-isolated inside its Arabic day-word string.

**Accessibility:** `role="navigation"` labelled `التنقل الرئيسي`; seats are buttons with `aria-current`; labels are always visible (no icon-only mode) which also solves label-fit at 320px; every seat ≥44px; Avatar button labelled `الحساب والإعدادات`; nav reachable via keyboard and announced.

**Arabic copy examples:** Seats: `اليوم`، `المبيعات`، `الذمم`، `المخزون`، `المزيد`؛ top zone: `مخبز أبو محمد` / `الثلاثاء 08/09/2026`؛ Avatar label: `الحساب والإعدادات`؛ More sheet: `المورّدون`، `شركات التوصيل`، `التقارير`، `الإعدادات`.

**Micro operational examples:** Switching from `اليوم` to `الذمم` before calling أبو أحمد about his balance; jumping to `المخزون` when the flour feels low; opening `المزيد` → `شركات التوصيل` to chase the 142.00 settlement; the whole test composition's chrome.

**Responsive behavior:** Five seats divide the full width at every breakpoint (64–86px each); labels ≤8 Arabic characters fit at 320px and 14px; at 430px seats widen, nothing else changes; top zone identical across widths.

**Known limitations:** Label length is capped by 320px seat width (≤8 chars — longer names must be rewritten, not shrunk); no fifth real destination without dropping one; chrome hairline and badge must be counted during color/divider audits even though they are structural.

---

## 11. Chart primitives

**Name:** Chart primitives (`.chart-sparkline`, `.chart-planned-actual`, `.chart-target-meter`, `.chart-trend-marker`)

**Purpose:** Show the shape of a number over time — recent trend, plan vs reality, progress to a target — with every chart directly labelled and textually equivalent, because أبو محمد decides from labels and numbers, not from reading curves.

**When to use:** Sparkline as a compact qualifier inside detail sheets (last-7-days context under a balance or movement); planned-vs-actual for weekly sales/movement review; target meter for month goals; trend marker adjacent to any value whose change matters. All are optional depth, never first-screen content.

**When not to use:** Not in the primary composition's first viewport; no legends, no tooltips (direct labels carry values, SPEC §6.13); no dual-axis charts; no more than 2 series per chart; not for categorical comparisons (that is `CompactTile` or `MetricRow`).

**Anatomy:** Sparkline: 2px polyline (ink-strong) + 4px end-point dot + direct label of the first/last value (13px). Planned-vs-actual: actual solid 2px ink-strong + planned dashed 4-4 2px ink-muted + direct end labels `فعلي` / `مخطط` (13px) + sparse axis ticks (`DD/MM`, 13px, ≤4). Target meter: 8px track (`sunken`) + fill + direct label `1,950.00 من 3,000.00 (65%)`. Trend marker: 16px directional arrow + signed percent (`+12%`, 13px/500, LTR isolate) + optional `عن الأسبوع الماضي` (13px, ink-muted).

**Content hierarchy:** Direct labels before shape: the numbers are stated, the graphic confirms. Text alternative (full sentence) is part of the anatomy, not an appendix.

**Sizes:** Sparkline ≈ 120–160 × 36–48px; planned-vs-actual ≈ viewport−32 wide × ~140px; meter track 8px tall, full width minus 32, label above 4px; trend marker chip height 28px.

**Spacing:** Chart block 16 edge padding; label-to-chart 4; meter label-to-track 4; trend marker gap-to-value 8 (sits beside the number it explains).

**Radius:** Meter track full (native bar geometry); sparkline and lines none; trend marker chip 6.

**Surface role:** Charts sit on canvas or within a sheet's content — never get their own card; the meter track uses `sunken` as an inset element (not a fourth surface — it is semantic-free geometry).

**Brand role:** Sparkline end-dot may be `brand-atmosphere` (a single calm accent); meter fill may be `brand-atmosphere` when status is neutral; no brand on planned-vs-actual lines.

**Semantic color role:** Meter fill turns warning only when behind plan (label repeats the status in words); trend marker uses positive/danger per direction with the sign always explicit; families count toward the ≤2 composition budget; texture (dash/dot) distinguishes series so color is never the only differentiator (SPEC §6.13).

**Variants:** Sparkline (up/down/flat); Planned-vs-actual (on-track / behind — dashed plan always); Target meter (on-track / behind / exceeded); Trend marker (positive `+12%` / negative `-8%` / flat `0%`).

**States:** Loading (skeleton block in the chart's footprint); Empty (`لا بيانات بعد` line); Partial (`بيانات من 24/08/2026` qualifier when the window is incomplete); the numbers in labels never animate.

**Interaction and motion:** Static by default; optional tap opens a detail sheet with the full series as `MetricRow`s (the text alternative made visible); no hover, no pinch-zoom; loading→ready crossfades at 200ms; reduced motion changes nothing (there is no spatial animation to reduce).

**RTL behavior:** The time axis stays LTR inside the plot even in the RTL interface (SPEC §6.13) — oldest at left, newest at right; all text labels remain Arabic RTL outside the plot area; trend arrows are vertical (up/down) and never mirror; no horizontal directional arrows are used in charts.

**Accessibility:** Every chart carries `role="img"` + a full-sentence aria-label ("رسم بياني: المبيعات آخر 7 أيام من 210.00 إلى 465.00 د.أ، الاتجاه صاعد"); direct labels are real text (contrast-checked); meter status is stated in the label, not just fill color; sparklines are decorative-plus-label — never the only carrier of a fact.

**Arabic copy examples:** `المبيعات آخر 7 أيام`؛ `المخطط مقابل الفعلي — الأسبوع الحالي` with `فعلي` / `مخطط` end labels؛ `هدف الشهر — 1,950.00 من 3,000.00 (65%)`؛ `+12% عن الأسبوع الماضي`؛ empty `لا بيانات بعد`؛ partial `بيانات من 24/08/2026`.

**Micro operational examples:** Sales sparkline under `حركة اليوم` details (210.00 → 465.00 over 7 days, rising); weekly planned 2,000.00 vs actual 1,275.00 for the mini-market; monthly flour-purchase target meter; `+12%` beside this week's sales total.

**Responsive behavior:** At 320px planned-vs-actual reduces to 3 axis ticks and shorter direct labels (`مخطط` / `فعلي` already fit); sparkline keeps minimum 120×36; meter label wraps to two lines before ever truncating; trend marker never wraps (chip grows).

**Known limitations:** ≤2 series; no legends/tooltips/dual axes; LTR plot inside RTL page must be defended in review (it looks "wrong" to casual inspectors but is the locked convention); charts without a visible numeric label fail the contract; meter percentages are computed, never hand-entered.
