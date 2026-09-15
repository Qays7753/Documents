# Component Contracts — DRAFT (Agent 01, Task 2-a)

- **Status: DRAFT contract, documented for implementation — nothing here is implemented.**
  Agent 03 turns these into tokens/HTML; Agent 02 assigns color values; Agent 04 audits.
- Every contract targets: phone-only 320/360/390/430 px, portrait, RTL, **light mode only**,
  IBM Plex Sans Arabic 400/500/600 (both arabic+latin subsets loaded — digits and "−" live in
  the latin subsets).
- **Shared tokens (referenced by all contracts):** screen edge 16 px · radius scale 12 / 16 / 24
  · touch target min 44 px (preferred 48) · type: value 32/600, sheet-title 20/600, section 15/600,
  label 15/400–500, body 14/400, qualifier & rail-tile label 13/400 (the ONLY 13 px uses) ·
  money: `<bdi dir="ltr">` + Western digits + "," thousands + exactly 3 decimals + "د.أ" outside
  the bdi · direction sign "−" (U+2212) inside the bdi, color secondary · motion 80/120/240 ms,
  easing `cubic-bezier(0.2, 0, 0, 1)` · focus ring 2 px, offset 2 px · hairline divider 1 px.
- Arabic copy in this file uses the Jordanian trade register established for Micro.

---

## C1 · PrimaryValueBlock

- **Purpose:** the single most important number of a composition, readable in <1 s — label,
  value, sign/state, and freshness in one glance block.
- **Use when:** a composition has exactly ONE headline money number (رصيد الصندوق، المتبقي
  لعميل، مستحق التسوية). **Exactly one per composition, on the canvas — never inside a card,
  never repeated** (the same key value must not appear twice on screen).
- **Never use for:** secondary metrics (→ MetricRow), several parallel values (→ MetricGroup),
  values inside sheets/dialogs (sheets use a 24/600 header total instead).
- **Anatomy (top→bottom):** label 15/500 (e.g. "رصيد الصندوق") → value row: bdi number 32/600
  line-height 40 + "د.أ" 15/500 to its left (RTL reading order: number then currency) →
  qualifier 13/400 line: freshness ("آخر تحديث 14:20") and/or the composition's single signed
  delta ("+12.500 عن أمس") / single comparison pair ("المخطّط 400.000"). No background, no
  border, no elevation, no radius — it is canvas content. Block height ≈ 104 px.
- **Variants:** default (positive/neutral) · negative-aware (sign carried inside bdi) · with
  inline comparison pair (counts as the composition's ONE pair) · compact (28/600 value, 88 px
  height, customer-sheet headers only).
- **States:** known (number) · unknown ("—" U+2014 at 32/600 + qualifier "قيد المزامنة…") ·
  unavailable ("غير متوفّر" 15/400 muted) · true zero ("0.000" with currency, never dropped) ·
  updating (120 ms crossfade old→new; value slot never empty mid-swap).
- **Interaction & motion:** not interactive as a block; tap target optional (→ detail sheet).
  On value change: 120 ms opacity crossfade, NO count-up animation. Never auto-refresh spins.
- **RTL:** label right-aligned; bdi isolation per shared tokens; currency outside bdi renders
  left of the number; qualifier reading right→left with isolated numbers.
- **A11y:** `aria-live="polite"` on the value row so balance updates are announced once;
  label+value+currency announced as one phrase ("رصيد الصندوق 431.100 دينار أردني" via
  aria-label with proper currency wording — visual stays "د.أ").
- **Copy (ar):** "رصيد الصندوق" / "المتبقي لخالد الحوراني" / "مستحق التسوية — أرامكس".
- **Micro examples:** home: "رصيد الصندوق 431.100 د.أ · آخر تحديث 14:20"؛ customer sheet:
  "المتبقي 250.000 د.أ · أقدم ذمم 12/08/2026"؛ settlements: "مستحق للتسوية 730.500 د.أ".
- **Responsive:** 320: qualifier wraps to a 2nd line (+18 px); value stays 32/600 (max realistic
  "9,999,999.999" ≈ 211 px + currency fits 288 px column). 430: one-line qualifier, wider value
  row, unchanged type scale.
- **Limitations:** not a card — cannot carry elevation/shadow variants; one per composition;
  comparison pair and delta share the single qualifier line (never both stacked).

## C2 · MetricGroup

- **Purpose:** 2–5 related metrics on ONE surface so the eye compares them as a set (aligned
  labels, aligned values, shared dividers) instead of hunting across separate cards.
- **Use when:** 2–5 metrics belong to the same question ("كيف سار اليوم؟" — sales/expenses/
  receivables). **ONE per composition by default; two allowed only with a documented reason**
  (e.g. customer context: نشاط العميل + شطب الذمم), each still 2–5 rows.
- **Never use for:** a single metric (use a bare MetricRow on canvas), 6+ metrics (choose a
  different composition), or as a dashboard grid of tiles.
- **Anatomy:** surface: full column width (358 px at 390), radius 16, padding 12 top/bottom + 16
  start/end, light elevated background (Agent 02); optional 13/400 group caption; 2–5 MetricRows
  (48 px each, see C3) separated by 1 px hairlines (internal hairlines COUNT toward the
  composition's 3-divider budget). Height ≈ 170 px for 3 rows.
- **Variants:** plain · with group caption ("اليوم") · with one row promoted to mini-comparison
  (label + planned-vs-actual pair inline, counts as the comparison pair).
- **States:** known rows · rows may individually show "—" (unknown) or "غير متوفّر" — never 0;
  loading: 3 skeleton rows shimmer; error: caption swaps to "تعذّر التحميل" + row-level "—".
- **Interaction & motion:** rows are tappable (≥44 px zone, 80 ms pressed overlay) → context
  sheet. No swipe, no reorder. Value updates crossfade 120 ms per row.
- **RTL:** rows flow right→left; values right-align at the row END (left edge of the column) so
  all bdi numbers share one alignment axis; hairlines full-width.
- **A11y:** group as `role="list"`, rows `role="listitem"`; each row label announced before
  value; state qualifiers announced ("قيد المزامنة").
- **Copy (ar):** "مبيعات اليوم" / "مصروفات اليوم" / "ذمم العملاء" / "مستحقات الموردين".
- **Micro examples:** home MetricGroup: مبيعات اليوم 1,240.500 · مصروفات اليوم −86.250 · ذمم
  العملاء 3,418.750؛ settlement context: "طرود اليوم 14" · "نقدي مُحصّل 412.000" · "فروقات
  التسوية 18.500".
- **Responsive:** 320: still one column, values keep alignment axis; 2 rows on <600 px-height
  viewports (3 default). 430: unchanged structure, more breathing room (padding 16).
- **Limitations:** exactly one surface — never per-metric cards; no mixed alignment; max 5 rows;
  counts as 1 of the 3 visible surfaces.

## C3 · MetricRow

- **Purpose:** one label + one money/count value (+ optional qualifier) in a 48 px row, the atom
  inside MetricGroup (and the only metric atom on canvas).
- **Use when:** any secondary metric anywhere (groups, sheets, detail headers). On canvas without
  a group only for a SINGLE isolated metric.
- **Never use for:** the headline number (→ PrimaryValueBlock), actionable operation records
  (→ OperationalRow), or as a button (rows navigate at most).
- **Anatomy:** label 15/400 start (right) · value 16/600 END-aligned (left) inside
  `<bdi dir="ltr">` + "د.أ" 13/500 · optional qualifier 13/400 under the label (max 1 line) ·
  optional trend marker replacing the qualifier ("▲" replaced by word, see C13.4). Row height
  48 px; tap zone full row.
- **Variants:** plain · with qualifier · with trend marker · with delta sign (value carries −/+)
  · compact 40 px (13 px label, in-sheet use).
- **States:** known / unknown "—" / unavailable "غير متوفّر" 13/400 in the value slot / true zero
  "0.000" / loading (skeleton bar 120×16).
- **Interaction & motion:** tap → context sheet (240 ms rise); pressed overlay 8 %, 80 ms; value
  change crossfade 120 ms; no hover states (touch).
- **RTL:** label start-right, value end-left; the shared value axis across rows makes magnitude
  comparison preattentive; sign inside bdi, color on the value ≤ the 2 colored-values budget.
- **A11y:** announced as "label، value، qualifier" in DOM order; `aria-live` only on rows that
  update in place; contrast ≥4.5:1 at 15/16 px.
- **Copy (ar):** "ذمم العملاء" / "نقدي مُحصّل اليوم" / "مستحق لمستودع زهران".
- **Micro examples:** "ذمم خالد الحوراني — 250.000 د.أ، آخر دفعة 04/09/2026"؛ "مصروفات الوقود
  −45.000"؛ "طرود بانتظار التسوية 6".
- **Responsive:** identical at all four widths (single-line invariant); qualifier truncates with
  ellipsis at 320 only if exceeding 288 px column (measure, don't guess).
- **Limitations:** no icons next to values (icon budget: OperationalRow only); never wraps to two
  lines; not a checkbox/select target.

## C4 · CompactTile

- **Purpose:** one action in 88×92 px — icon + 13 px label — the atom of the QuickActionRail.
- **Use when:** high-frequency verbs need one-tap discovery inside the rail (سجّل بيعة، أضف
  مصروفًا). Also usable as a fixed pair of choices inside sheets (e.g. "نقدي / آجل" as two
  tiles) when segmented doesn't fit the semantics.
- **Never use for:** navigation destinations (bottom nav owns those), data display, dashboard
  grids (forbidden pattern), or more than one filled tile per visible layer.
- **Anatomy:** 88 w × 92 h, radius 12, background per variant; icon 24/24 centered at 20 px top
  padding; label 13/400 centered, max 1 line ≈ 84 px (two short words allowed: "سجّل بيعة");
  pressed overlay 8 %; target = whole tile (≥ 44 ✓).
- **Variants:** neutral (surface tint) · **filled brand — the ONE filled brand-family action per
  visible layer** (first rail tile only) · outline (in-sheet pairs).
- **States:** rest / pressed (overlay 8 %, 80 ms) / focus (2 px ring, offset 2) / disabled (40 %
  opacity, non-interactive) / loading (spinner replaces icon, label frozen).
- **Interaction & motion:** tap opens a sheet (240 ms rise) — tiles never navigate to pages
  directly; snap neighbors in the rail (C5); no long-press.
- **RTL:** icon and label centered (no mirroring issues); tile order flows right→left; the
  filled tile is always first (rightmost).
- **A11y:** real `<button>`; `aria-label` repeats label text verbatim; focus order follows visual
  order right→left; 13 px labels are the documented exception — pair with icon redundancy.
- **Copy (ar):** "سجّل بيعة" / "أضف مصروفًا" / "استلم دفعة" / "فاتورة مورد".
- **Micro examples:** rail: [سجّل بيعة][أضف مصروفًا][استلم دفعة][فاتورة مورد][تحصيل]؛ sheet pair:
  [نقدي][آجل].
- **Responsive:** fixed 88×92 at all widths; count visible without scroll: ~3.3 at 320, 3.9 at
  360, 4.3 at 390, 4.9 at 430 (remainder as 16 px peek + fade).
- **Limitations:** label truncation forbidden — verbs must fit ~84 px at 13/400 (verified:
  "فاتورة مورد" ≈ 78 px upper-bound at 13); max 8 tiles per rail; no two-line labels.

## C5 · QuickActionRail

- **Purpose:** horizontal RTL-scrolling, snapping strip of CompactTiles — quick actions live
  HERE, never in a dashboard grid.
- **Use when:** a composition needs 4–8 high-frequency verbs reachable without scrolling the
  page. **Exactly one rail per composition.**
- **Never use for:** more than 8 actions (curate instead), data cards, or a second rail anywhere
  on screen (including inside sheets — sheets use tile pairs or buttons).
- **Anatomy:** zone 124 px total = tile 92 + 16 top + 16 bottom; tiles 88×92 gap 8; snap points
  96 px (88+8); trailing 16 px fade mask (left edge in RTL) signaling continuation; no header,
  no scrollbar (scroll indicator = the fade + peeking tile only).
- **Variants:** default (5–8 tiles) · minimal (4 tiles, no scroll on ≥390 — fade hidden when
  nothing overflows).
- **States:** idle / dragging (tile scale 0.97 on the pressed tile only) / scrolled (fade
  intensity 0→100 % over first 32 px of scroll) / empty-state N/A (rail is always curated, never
  data-driven).
- **Interaction & motion:** `scroll-snap-type: x mandatory`, RTL initial scroll anchored right;
  flick decelerates to next snap; keyboard: arrow keys move focus tile-by-tile; page vertical
  scroll never hijacked (rail scrolls horizontally only — one vertical scroll owner is the page).
- **RTL:** scrolls right→left; the filled brand tile is the first (rightmost) element = the
  composition's single filled brand action; fade mask ONLY on the left (trailing) edge.
- **A11y:** container `role="list"` labeled "إجراءات سريعة"; tiles are buttons (C4); when
  keyboard-focused, browser auto-scrolls (snap) — announce via focus, not live region.
- **Copy (ar):** rail as a whole needs no visible title; tiles per C4.
- **Micro examples:** home rail (filled first): سجّل بيعة · أضف مصروفًا · استلم دفعة · فاتورة
  مورد · تحصيل · تسوية توصيل؛ customer-context sheet: no rail (buttons instead).
- **Responsive:** visible count per C4; at 320 the first THREE tiles (incl. filled) fit the
  292 px glance band fully — the money-critical verbs are never below the scroll horizon.
- **Limitations:** horizontal-only scrolling; no vertical variant; no pagination dots; tile count
  is a curation decision (data-driven rails are forbidden).

## C6 · OperationalRow

- **Purpose:** one real-world event in a feed — who, what, how much, when, and its current
  state — scannable by name first.
- **Use when:** any ledger-style feed: sales, cash-in/out, purchases, settlements, schedules.
  Height 72 px.
- **Never use for:** metrics (C3), static settings rows, or marketing/hero content.
- **Anatomy:** start (right): entity 15/500 line 1 ("خالد الحوراني") + action/category 13/400
  line 2 ("بيعة — 3 أصناف") · end (left): amount 16/600 bdi with sign ("−86.250" /
  "+250.000") + time 13/400 ("10:24") · optional status glyph 16 px before the entity
  (pending/conflict only). No leading icon by default — the NAME is the anchor.
- **Variants:** default · with entity avatar-less initial chip (24 px, radius 12) · settlement
  variant (entity = company + parcels count qualifier) · schedule variant (time becomes date
  DD/MM/YYYY + "بانتظار" state).
- **States:** normal · pending (clock glyph + "بانتظار التأكيد" 13) · conflict (flag glyph +
  "نسختان متعارضتان" — resolves via dialog) · failed ("فشلت العملية" + retry affordance) ·
  cancelled (muted 60 %, qualifier "أُلغيت العملية", sign kept) · reversed (muted + qualifier
  "عُكست العملية", a counter-row appears adjacent) · completed (default look; qualifier optional).
- **Interaction & motion:** tap → detail sheet (240 ms); swipe (drag left) reveals up to 2
  actions 48 px wide each ("عكس"، "إلغاء") anchored at the leading/right edge; destructive
  actions NEVER execute on release — confirm dialog always; swipe disabled while pending.
- **RTL:** entity right, amount left (shared value axis with C3/C2); swipe direction and
  action-anchor mirror LTR conventions; time uses bdi ("14:20").
- **A11y:** row as listitem; state announced BEFORE amount ("فشلت، تحصيل، 250.000"); swipe
  actions must have keyboard/AT equivalents (row detail sheet contains the same actions).
- **Copy (ar):** "خالد الحوراني — بيعة · 86.250 · 10:24" / "مستودع زهران — فاتورة · −1,150.000 ·
  أمس" / "أرامكس — تسوية · +730.500 · بانتظار التأكيد".
- **Micro examples:** feed rows above; schedule variant: "متابعة خالد الحوراني — 09/09/2026";
  threshold alert row: "زيت زيتون 1ل — بقي 4 قطع".
- **Responsive:** 320: action/category line truncates with ellipsis (never the entity name);
  amount never truncates (bdi fixed). 430: category line may show extra qualifier. Batch loading:
  20 rows, prefetch near last 5, 3 skeleton rows of 72 px.
- **Limitations:** no two-line entity names (truncate with full name in sheet); max 2 swipe
  actions; never nests an interactive control other than swipe affordances.

## C7 · Button family

- **Purpose:** the action vocabulary: primary / secondary / quiet / destructive / icon-only,
  with loading / disabled / focused / pressed as STATES (not variants) and quiet-completion as
  a transient post-success state.
- **Use when:** committing money, confirming, retrying, dismissing. Heights: 48 primary
  (full-width in sheet action bars), 44 standard, 44×44 icon-only. Radius 12.
- **Never use for:** navigation tabs (C8 tab / C12), rail verbs (C4), row swipe actions (48 px
  swipe affordances are a row feature, not this family).
- **Variants:** **primary** = filled brand, the ONE filled brand-family action per visible layer
  · **secondary** = 1 px brand-tinted outline, transparent fill · **quiet** = text-only 14/500
  brand · **destructive** = red family (outline default; filled only inside destructive dialogs;
  counts toward the 2-semantic-family budget) · **icon-only** = 44×44, icon 20, `aria-label`
  mandatory, used for close/retry glyphs.
- **States:** loading (label swaps to 20 px spinner + frozen width, pointer-events off, NEVER
  text like "..." alone) · disabled (40 % opacity, height preserved, no pressed) · focused (2 px
  ring offset 2 — must survive on light bg) · pressed (8 % darker overlay, 80 ms) ·
  **quiet-completion** (after success, label becomes "تمّ ✓" in 15/500 for 1.6 s then reverts or
  the sheet closes — replaces toasts for minor ops).
- **Interaction & motion:** press feedback ≤80 ms; tap target includes 4 px external margin;
  destructive always preceded by confirm dialog; loading stops auto-progress after first
  failure → error state + retry.
- **RTL:** label icons mirror (arrows flip); check/clock glyphs do NOT mirror; button order in
  bars: primary at the END (leftmost) of an action bar, quiet/secondary to its right.
- **A11y:** `aria-busy` on loading; disabled uses `disabled` attribute (not just opacity);
  icon-only exposes the label ("إغلاق"، "أعد المحاولة"); focus visible on every variant.
- **Copy (ar) — verb-first, ≤2 words:** "سجّل بيعة" / "احفظ" / "أعد المحاولة" / "تجاهل" /
  "عكس العملية" / "إلغاء" / "عرض الكل".
- **Micro examples:** sheet action bar: primary "احفظ" + quiet "تجاهل"؛ conflict dialog:
  "النسخة المحلية" / "النسخة السحابية"؛ error strip: icon-only retry "أعد المحاولة".
- **Responsive:** primary stays full-width 48; at 320 two buttons stack vertically (48+48+8);
  icon-only never shrinks below 44.
- **Limitations:** no gradients/shadows beyond Agent 02's elevation spec; no multi-line labels;
  quiet-completion is transient, never a persistent state.

## C8 · Input family

- **Purpose:** capture text, money, search, dates, selections, segmented choices, tabs,
  checkboxes, switches — every field a Micro task needs.
- **Use when:** inside sheets (recording flows), search bars on lists, filters. Field height 48
  (search 44), radius 12, label 14/400 above, helper/error 13/400 below.
- **Never use for:** read-only values (use C3/MetricRow), or placing more than ~6 fields in one
  sheet (split steps instead).
- **Variants & specs:**
  - **text:** single-line 48, RTL placeholder 14/400 ("ملاحظة على الفاتورة").
  - **amount:** digits only via bdi LTR; grouping on blur ("1,250.000"); 3-decimal lock;
    "د.أ" 13/500 suffix at the field START (right); starts EMPTY with placeholder "أدخل المبلغ"
    — never prefilled "0.000"; optional quick-chips row (‎+5.000‎/‎+10.000‎/‎+20.000‎, 32 px height,
    radius 12) above the action bar.
  - **search:** 44 height, leading (right) 20 px icon, clear "×" icon-button 44×44 when text
    present, placeholder "ابحث عن عميل…".
  - **date:** readonly field showing bdi "DD/MM/YYYY", opens peek sheet with calendar; manual
    typing forbidden (mis-entry risk).
  - **selection:** field opens a medium sheet with search + radio list (never native select);
    chosen value 14/500 in field.
  - **segmented:** 2–4 options, container radius 12, options h44 labels 14/500, active thumb
    slides 160 ms; RTL order right→left (e.g. "نقدي | آجل").
  - **tab:** underline style for feed filters ("الكل · مبيعات · مصروفات"), labels 14/400→15/500
    active, 2 px underline, equal flex widths, horizontally scrollable if >4.
  - **checkbox:** 24×24 radius 12, 2 px border, check 16; label 14 min 44 px row.
  - **switch:** 52×32 track radius 16 (pill), thumb 24, on = brand, 160 ms slide; change never
    auto-saves (save via button).
- **States:** default / focused (2 px ring) / filled / error (13/400 red family message + field
  border; message names the fix: "أدخل مبلغًا أكبر من صفر") / disabled (40 %).
- **Interaction & motion:** amount formats on blur only (never mid-typing); segmented/tab
  160 ms; switch 160 ms; validation on submit, not per keystroke.
- **RTL:** label above (right-aligned); amount suffix at start; segmented thumb motion mirrors;
  checkbox check does not mirror; error message right-aligned.
- **A11y:** every field has a programmatic label; error text linked via `aria-describedby`;
  switch/checkbox expose state; date field announces "التاريخ: 15/10/2026".
- **Copy (ar):** "أدخل المبلغ" / "ابحث عن عميل…" / "أدخل مبلغًا أكبر من صفر" / "نقدي | آجل".
- **Micro examples:** expense sheet: amount + category selection ("وقود") + note; receivable
  sheet: amount prefilled 250.000 + date; customers tab: search + filter tabs.
- **Responsive:** single column at all widths; field max-width = column (358 at 390); quick-chips
  count drops to 2 at 320.
- **Limitations:** no multi-column layouts; no inline editing in rows (edit lives in sheets);
  date input depends on the sheet calendar (C10).

## C9 · State family

- **Purpose:** tell the truth about data and operations: empty / loading / error /
  offline-local-save / pending / conflict / failed / completed / cancelled / reversed.
- **Use when:** feed regions, rows, sheet flows, and inline strips. Line-based, ONE line of
  14/400 + at most one action — **no illustrations, no icon art beyond a 16–20 px status glyph**.
- **Never use for:** decorating happy paths (completed is quiet), or modal interruption of
  non-blocking states.
- **Per-state spec:**
  - **empty:** 15/500 line + quiet action ("لا عملاء بعد — أضف أول عميل" + "أضف عميلًا").
  - **loading:** 3 skeleton rows (72 px, shimmer 1200 ms loop, `prefers-reduced-motion` → static
    12 % overlay) + 13/400 "جارٍ التحميل…" when region-level.
  - **error:** 14/400 + retry button ("تعذّر التحميل — أعد المحاولة"); **auto-retry stops after
    the first failure**; retry is always a visible control.
  - **offline-local-save:** inline strip on the saved row + qualifier ("محفوظ محليًا — سيُزامن
    عند الاتصال"); syncs automatically on reconnect; never blocks entry.
  - **pending:** row glyph + "بانتظار التأكيد" (13/400).
  - **conflict:** row flag + "نسختان متعارضتان"; resolution via Dialog (C11).
  - **failed:** "فشلت العملية — أعد المحاولة" + icon-only retry.
  - **completed:** quiet-completion (C7) or row qualifier "تمّ تسجيل البيعة".
  - **cancelled:** muted row + "أُلغيت العملية".
  - **reversed:** muted row + "عُكست العملية" + adjacent counter-row with flipped sign.
- **Interaction & motion:** transitions between states crossfade 120 ms; skeletons never
  jump-replace mid-scroll (batch-append below fold).
- **RTL:** text states right-aligned; glyphs at line start (right); numbers in states stay bdi.
- **A11y:** `aria-live="polite"` region for feed-level state changes; assertive ONLY for
  failure of a submitted money operation; conflict dialog traps focus.
- **Copy (ar):** per the table in `ux-architecture-report.md` §5 (all ≤6 words).
- **Micro examples:** offline expense saved → row strip; receivable sync conflict → flag on
  "دفعة خالد الحوراني"؛ delivery settlement pending → "بانتظار التأكيد" on أرامكس row.
- **Responsive:** invariant structure; skeleton count fixed at 3; empty-state line truncates
  with action preserved (never the action).
- **Limitations:** no illustration/empty-art (hard rule); no stacking two state strips in one
  region; conflict resolution UI lives in Dialog, not inline.

## C10 · Sheet

- **Purpose:** the task surface for recording money — bottom-anchored, thumb-reachable, keyboard
  friendly. Replaces page navigation for all create/edit flows.
- **Use when:** any input flow (see decision matrix, report §3.3): sales, expenses, payments,
  purchases, pickers, date, filters.
- **Never use for:** destructive/irreversible confirmations or either/or conflicts (Dialog),
  or persistent content.
- **Anatomy:** top radius 24 (the only 24 in the system); drag handle 36×4 centered at 8 px;
  title 20/600 + optional 13/400 subtitle; content scrolls INTERNALLY (sheet owns vertical
  scroll while open — page scroll locked); bottom action bar 64 px + safe-area: primary 48
  full-width + quiet "تجاهل" stacked or side-by-side ≥360; scrim rgba(0,0,0,
  0.4) with 160 ms fade.
- **Variants (snap heights):** peek 40 % (date/pickers) · medium 60 % (amount-first flows) ·
  tall 92 % (multi-field: sale, invoice). Drag between snap points, 240 ms settle.
- **States:** rising (240 ms, `cubic-bezier(0.2,0,0,1)`) · open · settling · dismissing (200 ms
  down) · dirty-dismiss-blocked (swipe-down on dirty form → confirm dialog "تجاهل التغييرات؟").
- **Interaction & motion:** handle + tap-outside dismiss when clean; internal scroll only in
  content area; keyboard pushes sheet (never covers action bar); quick-chips row sits directly
  above action bar (one-thumb amounts).
- **RTL:** title right-aligned; action bar primary at END (left); drag handle centered; content
  RTL; amount field per C8.
- **A11y:** `role="dialog"` + `aria-modal`; focus trapped; title announced; Escape/handle closes
  (with dirty guard); scrim tap is a control with label "إغلاق".
- **Copy (ar):** "بيعة جديدة" / "تحصيل من خالد الحوراني" / "فاتورة من مستودع زهران".
- **Micro examples:** receivable sheet: prefilled 250.000 + date + primary "احفظ"؛ expense
  sheet: empty amount + category picker + quick-chips؛ supplier invoice: tall sheet + due date
  15/10/2026.
- **Responsive:** width = viewport; at 320 action bar buttons stack (48+48); peek % constant,
  so peek = 226 px at 568-height devices (date sheet still fits: calendar 336 + bar 64).
- **Limitations:** no left/right side sheets; no nested sheets (picker sheets replace their
  parent's content region instead); max one sheet open; 92 % max height (never fullscreen —
  the nav stays visible as the persistent anchor).

## C11 · Dialog

- **Purpose:** pause and resolve: destructive confirmations and either/or conflicts. Centered
  with a LOWER vertical bias so its buttons land in the thumb zone.
- **Use when:** confirm إلغاء/عكس, sync conflict (two labelled values), dirty-dismiss guard.
- **Never use for:** inputs (any input → sheet), long explanations, non-blocking info (→ state
  strip).
- **Anatomy:** max width 328 (288 at 320 screens), radius 16, padding 20; title 16/600 (≤2
  lines); body 14/400 (≤3 lines); optional two value rows 15/500 for conflicts (each a labelled
  bdi amount — this pair is a *choice*, not the composition's comparison pair); action row max 2
  buttons; vertical bias: dialog block positioned so ~60 % of it sits below screen midpoint.
- **Variants:** confirm (quiet "إلغاء" + primary) · destructive (quiet "رجوع" + destructive
  filled — the red family counts in the color budget) · conflict (two value rows + "النسخة
  المحلية" / "النسخة السحابية").
- **States:** appearing (120 ms fade+scale 0.96→1) · open · action-loading (button spinner,
  dialog locked) · action-failed (13/400 error line replaces body's last line, retry once —
  no auto-retry loop).
- **Interaction & motion:** scrim tap = quiet cancel (never triggers destructive); Escape same;
  focus trapped on the safe action initially.
- **RTL:** actions ordered: safe (quiet) start-right, destructive/primary end-left; value rows
  label right + bdi amount left.
- **A11y:** `role="alertdialog"` for destructive/conflict; title + body + outcome line announced
  together; buttons ≥44; no auto-dismiss timers ever.
- **Copy (ar):** "عكس تحصيل 250.000؟" + "سينشأ قيد عكسي بتاريخ اليوم" / "تعارض في دفعة خالد
  الحوراني" / "تجاهل التغييرات؟".
- **Micro examples:** cancel sale confirm: "إلغاء بيعة خالد الحوراني 86.250؟ — سيعود المبلغ
  إلى الذمم"؛ conflict: local 250.000 vs cloud 200.000.
- **Responsive:** width 288–328; at 320 buttons full-width stacked (44 each); bias preserved.
- **Limitations:** max 2 buttons, max 2 value rows; no scrollable dialogs (content must fit) —
  if it doesn't, it's a sheet.

## C12 · BottomNavigation + integrated top zone with Avatar

- **Purpose:** the ONLY persistent chrome (nav) + the in-flow identity zone (top) — together
  they replace app bars, drawers, and floating buttons.
- **Use when:** every composition. Nav: 64 px + safe inset, **radius 0, edge-to-edge**, 5 slots
  (4 destinations + "المزيد"). Top zone: 64 px in-flow block at canvas start, scrolls away.
- **Never add:** second bar, hamburger, FAB, notification bell, settings gear, more avatars.
- **Anatomy (nav):** icons 24 px over labels 14 (400 inactive / 500 active + brand color);
  slot 64 px wide (320/5); per-slot target 64×48; badge 16 px dot on "المزيد" (conflicts count,
  max 2 digits); no elevation shadow — a 1 px top hairline separates it from content (NOT
  counted in composition divider budget — chrome hairline).
- **Anatomy (top zone):** start-right: business name 15/600 "بقالة النور" + context 13/400
  ("صندوق اليوم · 08/09/2026" or "غير متصل — محليًا")؛ end-left: ONE Avatar 40×40 radius 12,
  initials "أ.ن" → page "الحساب والإعدادات" (unified profile/settings).
- **Variants:** nav: default · with-badge; top zone: default · offline-context (context line
  swaps to offline wording + sync dot).
- **States (nav):** active (500 + brand + 3 px weight emphasis, no pill) · inactive · pressed
  (8 % overlay, 80 ms, light haptic on switch). Nav never hides on scroll.
- **States (top zone):** scrolls away with page (by design — money numbers drift toward the
  thumb); offline line swaps with 120 ms crossfade.
- **Interaction & motion:** tab switch instant content swap (no shared-element animation);
  80 ms pressed; "المزيد" opens a plain destination page listing sections.
- **RTL:** slot order right→left: الرئيسية (rightmost) → العمليات → الذمم → المزيد (leftmost);
  active underline/indicator NOT used (weight + color suffice); top zone mirrored as specified.
- **A11y:** `role="navigation"` labelled "التنقل الرئيسي"; current page `aria-current="page"`;
  labels always visible (14 px — never icon-only mode); avatar exposes "الحساب والإعدادات".
- **Copy (ar):** "الرئيسية · العمليات · الذمم · المزيد" / context: "صندوق اليوم · 08/09/2026".
- **Micro examples:** slot widths at 320: 5×64; chosen labels measured (upper-bound @14/500):
  الرئيسية 70.2 · العمليات 64.4 · الذمم 35.6 · المزيد 41.9 (shaped ≈15–25 % narrower — fits
  60 px safe width; re-verify with engine, see report §6).
- **Responsive:** nav slot 64→86 px across 320→430; labels 14 constant; top zone identical
  (avatar 40 constant).
- **Limitations:** labels cannot drop to 13 px (min-14 rule) nor be ellipsized; max 5 slots;
  the fifth slot is ONLY "المزيد" — domain words don't fit at 320 (documented in report §6).

## C13 · Chart primitives (sparkline · planned-vs-actual · target meter · trend marker)

- **Purpose:** tiny, glance-first, DIRECT-LABELLED charts — no axes, no grids, no tooltips, no
  legends. The number sits next to the shape, never inside it.
- **Use when:** reinforcing a MetricRow or PrimaryValueBlock qualifier; planned-vs-actual is the
  composition's single comparison pair.
- **Never use for:** exploration (tap → detail sheet instead), more than ONE chart per
  composition, or charts as the primary content.
- **Shared specs:** time flows **RTL: oldest at right → newest at left** (matches reading
  direction); values always Western digits in bdi; line/fill colors from the brand family +
  at most one semantic family; height ≤48 px; `prefers-reduced-motion` → static render.
- **C13.1 Sparkline:** 96×32 area, 2 px stroke, no fill (or 12 % fill tint); 4 px dot on the
  newest (LEFT) point; direct value label adjacent (13/400), not on the line; min 7 points;
  used in MetricRow qualifier zone. Micro: "مبيعات الأسبوع" trend beside "1,240.500".
- **C13.2 Planned-vs-actual:** horizontal bar pair in a 48 px stack: planned bar = 12 px height,
  neutral outline/tint; actual bar = 12 px, brand fill; bars grow from the RIGHT edge leftward;
  both DIRECT-LABELLED at their end ("المخطّط 400.000" / "الفعلي 431.100"); delta qualifier
  below ("+31.100 عن المخطّط", signed). Counts as THE comparison pair. Micro: cash collected vs
  plan for the week.
- **C13.3 Target meter:** 12 px track, radius 12 (pill), full column width; fill from the right
  (RTL) in brand color; label beside/under: "65% من هدف الشهر" (percent digits bdi); fill
  never animates on load (static) but crossfades 120 ms on update. Micro: تحصيل الذمم مقابل
  هدف الشهر.
- **C13.4 Direct-labelled trend marker:** text-only, replaces arrow icons: direction word +
  signed bdi number, 13/400 — "أعلى +12.500 عن أمس" / "أدنى −8% من المخطّط". Color optional
  (semantic budget), sign mandatory. Lives in qualifiers and row states.
- **States:** data-known (drawn) · unknown (sparkline area empty + "—" 13/400, NEVER a zero
  line) · unavailable ("غير متوفّر" replaces the chart) · updating (120 ms crossfade).
- **Interaction & motion:** non-interactive in v1 (tap region → detail sheet); no hover, no
  tooltip, no crosshair.
- **RTL:** all four mirror as specified above (newest LEFT, growth RIGHT→left); labels for bar
  ends sit OUTSIDE the bar edge they describe.
- **A11y:** every chart carries `aria-label` with the full sentence ("المبيعات أعلى من أمس
  بمقدار 12.500 د.أ") — the direct labels ARE the accessible description; no role="img"
  without label; contrast ≥3:1 for strokes.
- **Copy (ar):** "المخطّط 400.000 · الفعلي 431.100" / "65% من هدف الشهر" / "أعلى +12.500 عن
  أمس".
- **Micro examples:** customer sheet sparkline (مشتريات خالد الحوراني)؛ settlement
  planned-vs-actual (نقدي متوقع مقابل مُحصّل)؛ month target meter (تحصيل الذمم).
- **Responsive:** sparkline fixed 96×32; meter full-width; bar pair full-width with labels
  wrapping UNDER bars at 320 (labels never truncate).
- **Limitations:** one chart per composition; no interaction; no dual-axis; sparkline min 7
  points (fewer → trend marker instead).
