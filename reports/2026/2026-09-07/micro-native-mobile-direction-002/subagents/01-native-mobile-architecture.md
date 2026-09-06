# 01 — Native Mobile Architecture

**Delivery:** `micro-native-mobile-direction-002` · Stage 1 · Specialist report 01
**Task ID:** 3-a · **Agent:** Native Mobile Product Architect
**Date:** 2026-09-07
**Inputs read in full:** `en/00-previous-work-lessons.md` (buckets K/A/R/V) · `en/01-intake-and-previous-work-audit.md`
**Inputs skimmed:** `micro-visual-product-concept-001/en/02-research-and-direction-synthesis.md` · `micro-visual-product-concept-002/en/02-research-and-direction-synthesis.md` (failure causes only)

**Mandate:** define what makes Micro *feel* like a real native mobile product from a major company — in concrete, adoptable terms. RESEARCH ONLY: no prototype, no final direction choice (orchestrator decides).
**Non-goals:** no visual styling (palette/type belong to other specialists), no prototype, no scores-as-authority (R-09).

---

## 1. Native tells checklist — the observable properties of "native"

Both rejected deliveries failed on **behavior**, not decoration: no collapsing app bar, no navigation stacks, no sheet physics, no back semantics (R-04, R-05, R-11). Nativeness is a checklist of observable properties. Every Micro screen must pass **all** of them; a screen missing two or more reads "web in a phone" regardless of typographic quality.

| # | Tell | Concrete native behavior | RTL rule for Micro |
|---|---|---|---|
| N-01 | App bar collapses with scroll | Question-led header (A-06) renders as a large title that collapses into a compact 56–64px bar during scroll; the compact bar keeps the destination word («اليوم»، «المال») plus contextual icons (search, identity). The question is **never** a static in-body H1. | Identical mechanics; text start-aligned right; the collapse is direction-agnostic. |
| N-02 | Persistent vs per-screen chrome | The bottom bar exists **only** on top-level destinations. Every pushed screen hides it and carries a back affordance. Sheets and dialogs never show the bottom bar. Tabs + back button simultaneously = web smell. | Bottom bar order reads right→left in RTL; capture sits center or start-adjacent per model (§2). |
| N-03 | Back affordance on every pushed screen | Back control sits at the **start edge** (top-right in RTL) with a chevron pointing **right** (mirrored iOS pattern), optionally labeled with the previous screen's word or «رجوع». | Back is top-right; never top-left; the chevron never points left in Arabic mode. |
| N-04 | Transitions tied to navigation events | Push = incoming screen slides from the **left** in RTL (outgoing parallax to the right), 240–280ms, inside the 80–280ms register (A-09); pop reverses. Tab switch = instant cross-state, no travel. Never a page fade (R-11). | Push direction mirrors: RTL slides from left, LTR verification slides from right. |
| N-05 | Edge-swipe back | Interactive pop: finger starts at the **right edge**, drags **leftward**, pulling the previous screen in from the right with parallax. Live on every pushed screen; must not be blocked by any custom horizontal widget. | Mirrors LTR (left-edge swipe). This tell is what kills Model C's pager (§2.4). |
| N-06 | Scroll ownership | Exactly **one** vertical scroll container per screen; the app bar collapse is driven by that scroll; sheet content scrolls inside the sheet; the body under a sheet never scrolls. No nested scroll panes, no inner scrollable sections. | Unchanged; scrolling content stays start-aligned right. |
| N-07 | Keyboard avoidance | The focused input is always visible above the keyboard via viewport insets; the pinned save control rides **above** the keyboard with inset padding; scroll position adjusts so the active field is unobstructed. No zooming, no manual pan hacks. | Arabic keyboard assumed default; fields mirror; digit runs stay LTR-isolated (K-05). |
| N-08 | Sheet physics | Bottom sheets drag from a grabber with ≥2 snap detents (≈50% and ≈90%), dismiss by drag with velocity, scrim tap cancels. iOS: detents medium/large. Android: modal bottom sheet with drag handle. A "sheet" that fades in and needs an × to close is a web modal. | Grabber is direction-neutral; content inside mirrors. |
| N-09 | Dialog semantics | Destructive/confirm dialogs are centered, blocking, non-draggable, carry no navigation. Android system back cancels them via the cancel path. Effect preview before irreversible actions lives here (K-09). | Dialog text mirrors; action order mirrors (cancel at start edge, confirm at end edge). |
| N-10 | Tab state persistence | Each top destination keeps its own stack, scroll position, and segmented selection. Returning restores position exactly; data revalidates silently (cached-first, DSY-17). | Same. |
| N-11 | Haptic moments | Haptics only at meaning events: save success (success notification), record-type/segment selection (selection tick), discard guard appears (warning), destructive confirm (single impact), pull-to-refresh trigger (light). **Never** during scroll, drag, or tab switching. Final values are a device-test item (V-03). | Same on both platforms. |
| N-12 | Real chrome and safe areas | Real status bar; content respects top and bottom safe-area insets (C-06). No bezel, no fake 09:41 battery (R-01). Review frames live strictly outside the product surface (K-11). | Safe-area identical; home-indicator zone reserved on both. |
| N-13 | Immediate press feedback | Every touchable answers within one frame with its press state (the fixed color-press doctrine; no scale). No hover styles exist anywhere. Targets ≥44pt, 48pt for primary/keypad, ≥8px separation (K-12). | Mirrored hit areas; targets unchanged. |
| N-14 | Empty-to-content flow | An empty state is a full-body native composition — glyph + word + one action («سجّل أول دفعة») — that hands off to content with a settle, not a placeholder-box swap and never a page fade. First content paint animates rows in 160–280ms. | Empty-state composition mirrors. |

---

## 2. Information architecture — three candidate top-level models

### 2.1 What the home must answer first

| Owner question | First answerer | Second answerer |
|---|---|---|
| وين الكاش؟ — my position now | «اليوم» (first scroll moment) | «المال» |
| ماذا تغيّر؟ ولماذا؟ — what changed & why | «اليوم» (recent changes → event detail) | «المال» (movements) |
| مين مدين لي؟ — who owes me | «الناس» · زبائن (person-first, aging) | «المال» (receivables total) |
| ما عليّ؟ — what do I owe | «المال» (obligations) | «الناس» · مورّدين |
| شو يحتاج انتباه اليوم؟ — attention today | «اليوم» (attention rows) | status glyphs inside other lists |
| شو الخطوة الجاية؟ — what next | «اليوم» (next-step line) | — |

The legacy five-seat vocabulary «مشروعي الآن · العمل · سجّل · مالي · أدواتي» (A-10) is **re-derived** here per V-06: «مشروعي الآن» becomes «اليوم», «مالي» becomes «المال», «أدواتي» dissolves (settings push + assistant row + utilities), and «الناس» is added because person-first ledgers are the owner's receivables mental model. Owner re-confirmation is a review-gate question.

### 2.2 Model A — four tabs + docked capture («اليوم · المال · سجّل · الناس · العمل»)

Bottom bar: 5 slots at 64px + safe area (row heights per inherited D4); labels always visible, glyph+word (K-04); capture occupies the center slot.

| Position (RTL right→left) | Arabic label | Gloss | Stack above | Chrome |
|---|---|---|---|---|
| 1 (start) | «اليوم» | Today | root only; pushes: «كشف الأسبوع»، event detail, «البحث»، «الإعدادات» | Large title (N-01) |
| 2 | «المال» | Money | root → movement detail, «الأمانات»، «ما عليّ» filtered list | Compact bar + period segmented «اليوم · الأسبوع · الشهر» |
| 3 | «سجّل» | Capture | not a destination — opens capture sheet | — |
| 4 | «الناس» | People | root (segmented «زبائن · مورّدين») → «دفتر الزبون» party detail | Compact bar + search |
| 5 (end) | «العمل» | Work | root → order/invoice detail, «المشتريات»، drafts | Compact bar + search + filter chips |

- **Home answers first:** position now, what changed, attention today, what next (all four "today" questions).
- **Trade-offs:** fastest daily operation; capture always in thumb reach; 4 independent stacks cost memory/state care; «المال» vs «الناس» overlap is resolved by role — totals & movements vs person-first ledgers.
- **Web-feel risk: LOW** — provided N-01…N-14 are enforced; the capture slot must behave as chrome, not as a web FAB slapped on content.

### 2.3 Model B — hub-and-spoke «مشروعي الآن», capture bar, no tabs

One persistent home; spokes («المال»، «الناس»، «العمل»، «كشف الأسبوع») are pushes; a docked capture bar sits at the bottom of the hub; cross-spoke travel returns through the hub.

- **Home answers first:** the same four "today" questions, with maximum canvas for the truth moment.
- **Stack depth:** 1–2 typical, 3 max; every spoke is a clean push with back (N-03/N-05).
- **Trade-offs:** purest app identity and the strongest "one dominant truth block" (A-02); but back-heavy between tasks (collect → receipt → next party costs two pops), and the hub can grow into a long scrolling page that recreates document flow (R-04) unless block quotas hold (A-04: ≤8 blocks, ≤5 today rows).
- **Web-feel risk: LOW–MEDIUM** — risk concentrates entirely in hub scroll length; a capped hub is native, a long one is an article page.

### 2.4 Model C — bottom bar + swipeable pager

Model A's destinations plus horizontal swipe between top destinations; RTL pager order mirrors (اليوم rightmost).

- **Fatal friction:** swipe-between collides with RTL edge-swipe back (N-05) on the right-edge tab; the centered «سجّل» slot breaks pager continuity (swiping would pass through capture); horizontal row gestures become ambiguous; Android predictive back + pager produces state confusion.
- **Home answers first:** same as A, but the pager invites "slides" composition that trends back toward card walls (R-03).
- **Web-feel risk: MEDIUM** — keeping it means disabling a defining native tell (edge-swipe back) or fighting the system every screen.

### 2.5 Comparison matrix (input to the orchestrator's decision, not the decision)

| Dimension | A — tabs + capture | B — hub-and-spoke | C — tabs + pager |
|---|---|---|---|
| Capture in one-hand reach | always (bar) | always (bar) | always (bar) |
| Taps to «مين مدين لي؟» | 1 | 2 (out of hub) | 1 |
| Taps between «اليوم» and «العمل» mid-task | 1 | 2 (via hub) | 1 + gesture conflict |
| State complexity | 4 stacks | 1 stack | 4 stacks + pager index |
| Gesture conflicts | none | none | edge-back vs pager (N-05) |
| 320px behavior | 5 × 64px slots fit | bar = capture only, simplest | pager adds no width cost but breaks at capture slot |
| Long-hub document-flow risk (R-04) | none | real — must cap hub | none |
| Differentiation potential | high (chrome discipline) | highest (single truth stage) | low (pager reads generic) |
| Specialist lean | **strongest for daily operation** | most distinctive-native alternative | carries conflicts that undermine native tells |

### 2.6 Recommended handling regardless of model

- **Capture — two-tier.** «سجّل» opens the capture **sheet**: segmented record types «قبض · صرف · مصروف · طلب», amount surface (A-07 discipline), party, date defaulting to today (DD/MM/YYYY), save in thumb zone. Creating a «طلب»/invoice (multi-line, عربون deposit) **upgrades to a full-screen push**, transferring state. Money events are single-value → sheet wins; documents need space and back-state → push wins.
- **Search — one global entry.** Magnifier in «اليوم» and in «العمل»/«الناس» bars pushes a full search screen with the keyboard pre-raised; results grouped by segmented «الكل · أشخاص · فواتير · حركات». Never a dropdown/autocomplete overlay (web tell).
- **Settings/profile — a push, not a tab.** Identity control in «اليوم»'s app bar pushes «الإعدادات» (vertical grouped rows; no tile grid, R-08). A settings tab is where apps start feeling like websites, and it wastes the scarcest chrome slot. Format constants (JOD «د.أ»، DD/MM/YYYY, ASCII digits) appear as read-only verification rows.
- **Assistant — an entry row, not a destination.** «اسأل ميكرو» as a quiet row pinned at the end of «اليوم»'s body (or an app-bar icon), pushing a full-screen conversation in a later phase. Never a floating chat bubble overlay (web-widget smell).

---

## 3. Navigation stack rules

### 3.1 Surface decision table — push vs sheet vs dialog

| Micro action | Surface | Why | Dismiss/back semantics |
|---|---|---|---|
| «حصّل» record collection | Bottom sheet | One amount + party context; stay on the list | Drag down, «تم», or system back |
| «تعديل فاتورة» edit invoice | Full push | Multi-line document; needs space and dirty-state | Back = discard guard if edited |
| «فرق الجرد» cash-count variance | Full-screen guided flow | Multi-step; must not be dropped casually | Back = guard «في جرد غير مكتمل — تكمله؟» |
| Delete / discard record | Center dialog | Blocking, destructive; carries the K-09 effect preview | Confirm/cancel; system back = cancel |
| «تصفية» filter list | Non-modal sheet | Applies on confirm; active chips stay visible in the bar | Drag down; system back closes |
| «اختيار زبون» pick customer | Full push with search field | Long lists; needs keyboard + recents | Back returns; selection preserved (§3.3) |
| Change date | Platform date picker | Native control; ar-JO, Gregorian, DD/MM/YYYY, ASCII digits (C-05) | Platform cancel |
| Correction preview | Dialog with will-change/won't-change lists (K-09) | Irreversible money action | «تأكيد» / «تراجع» |
| «كشف الأسبوع» statement | Full push | Reading surface with period switcher | Edge-swipe / system back |
| «سجّل» → «طلب» | Sheet → full push upgrade | Document needs room | Back resolves to the originating list; sheet state transfers |

**Rule of thumb:** one value + context = sheet; a document or a list-over-list = push; a consequence the owner must own = dialog.

### 3.2 Back semantics

| Trigger | Behavior in Micro |
|---|---|
| App back button (RTL top-right chevron) | Pops one level; guarded when the form is dirty |
| iOS edge swipe (RTL) | From the right edge, dragging leftward; interactive pop with parallax |
| Android system back / predictive back | Pops stack; dismisses in order dialog → sheet → screen; predictive back previews the previous screen |
| Review-HTML back (prototype only) | Wired to in-app back via history so reviewers feel real stack semantics; it is review apparatus, not product behavior |

### 3.3 State preservation on back (binding)

1. Form inputs survive a picker push: pick customer → back → the typed amount is untouched (generalization of DSY-18's failure rule).
2. List scroll position restores exactly on pop; new arrivals insert above with a positional anchor, never a jump.
3. Tab stacks persist (N-10); switching tabs never resets a half-read ledger or a chosen segment.
4. Discard-guard cancel returns to the form intact with the keyboard re-raised on the offending field.
5. Drafts persist locally as «مسودات» visible in «العمل» — a capture interrupted by a crash is never silently lost.

---

## 4. Screen anatomy templates

### 4.1 Shared grammar (composition that cannot read as a web page)

- **Header region** = collapsing app bar (N-01) + truth slot (one status line carrying sync/state words per K-03/DSY-15) + the screen's primary figure. The figure is **structural** — part of the header region or the first scroll moment — never a floating rounded card (A-02).
- **Body** = one scroll owner; content is **rows** (hairline-separated groups, tonal steps between sections) and a fixed money column (A-03). Sections are not boxed cards (R-03); card quota ≤1 and usually zero (DSY-12).
- One screen = one owner question (A-04); details are pushes; actions are sheets; rows ≤3 lines; one action word per row (DSY-25).
- Primary actions live in the bottom third (K-12); destructive controls live far from them.
- 320px arithmetic (DSY-24): 288 content width − 88 amount column − row padding leaves ≈148px for the subject — every row must survive it.

### 4.2 «اليوم» — Today overview

- **Header:** large title = date DD/MM/YYYY + question «وين الكاش اليوم؟»; truth slot = sync line («متزامن 08:30» / «الوضع: بدون اتصال · التسجيل محفوظ على الجهاز»); app bar: search, identity → «الإعدادات».
- **Body order:** (1) cash truth line — cash now + delta since yesterday; (2) attention rows ≤5, glyph+word+one action («حصّل»، «أكمل»); (3) «ماذا تغيّر؟» — 3 recent events, tap → movement detail (the "why"); (4) next-step line «الخطوة الجاية: …»; (5) assistant row «اسأل ميكرو».
- **Persistent bottom:** 5-slot bar with docked «سجّل».
- **Actions:** capture in the bar; row actions inline; nothing floats above content.

### 4.3 «المال» — Financial truth

- **Header:** compact bar + period segmented «اليوم · الأسبوع · الشهر»; truth slot; primary figure = cash now, structural.
- **Body order:** (1) three-position line — «لي / عليّ / أمانات» with honest unknowns («قيمة غير محددة بعد» + «سجّله», K-03); (2) movements list, fixed amount column, direction carried by row grammar; (3) at most one honest chart (K-10): period + unit + source state + text interpretation; unrecorded = gap + footnote, never zero.
- **Persistent bottom:** bar; «سجّل حركة» via capture.
- **Actions:** movement tap → detail push; period = segmented in the header region.

### 4.4 «الناس» — Receivables/Obligations list + party detail

- **Header:** compact bar + segmented «زبائن · مورّدين» + sort control «الأقدم أولاً» + search icon.
- **Body:** person rows — name, balance in the fixed column, aging word («منذ 14 يوم»), status glyph; tap → «دفتر الزبون».
- **Party detail:** app bar = person name; header region = dominant balance + truth state (A-02); body = per-party events; actions: «حصّل» (sheet) and platform contact/share intents (native tell, optional phase).

### 4.5 «العمل» — Orders

- **Header:** compact bar + search + filter chips (active filters visible); decision line first («طلبان بانتظار التسليم»).
- **Body:** order rows with status word + payment relationship («قبض 30.00 من 50.00», DSY-16) as row content, not a chart panel; «مسودات» group at the end.
- **Actions:** one word per row («سلّم»، «أكمل»); row tap → order detail push.

### 4.6 «المشتريات» — Purchases/Suppliers

- Lives under «العمل» as a filtered view or segmented sibling; supplier rows carry the received-value bridge («استلمت 8 من 10» grammar, inherited from 001); same row grammar as Orders. The supplier **ledger** (what I owe whom) lives in «الناس» · مورّدين — documents and people are different destinations.

### 4.7 «جرد الدرج» — Cash closing flow

- **Full-screen guided sequence:** (1) count entry — big digits, decimal keyboard; (2) live variance «الفرق: −3.50 د.أ» with the sign inside the LTR isolate (K-05); (3) reason picker «علّل الفرق» (نقص تحصيل / خطأ تسجيل / …); (4) confirm with effect preview (K-09).
- Back at any step = guard «في جرد غير مكتمل — تكمله؟»; completion = quiet closure sentence with final digits (K-08), returning to «اليوم».

### 4.8 Capture sheet «سجّل»

- **Anatomy:** grabber + title + close; segmented record types «قبض · صرف · مصروف · طلب»; amount surface (A-07: big digits, visible state, tap alternative); party picker (push); date row defaulting today; optional note; save pinned bottom, inset-aware.
- **Keyboard:** raises on amount focus; toolbar holds «التالي / تم / مسح»; save sits above the keyboard in the thumb zone.

### 4.9 «البحث» — Search

- Full-screen push; field auto-focused; recents row; results grouped by segmented «الكل · أشخاص · فواتير · حركات»; honest empty («ما في نتائج عن "…"»); keyboard dismisses on scroll; results are rows, not cards.

### 4.10 «الإعدادات» — Settings

- Push from «اليوم»; vertical grouped rows (R-08 forbidden); identity block at top; language row (Arabic default, English verification); read-only format rows (JOD «د.أ»، DD/MM/YYYY, ASCII digits); sync-status row with per-entity state; destructive actions far from the thumb, behind a dialog.

---

## 5. Forms & keyboard

### 5.1 Capture form behavior (binding spec)

1. **Focus order** follows reading order: type → amount → party → date → note → save; «التالي» advances; fields mirror RTL, digit runs never mirror (K-05).
2. **Amount:** numeric keyboard (decimal input mode, 2 decimals), digits render stably (A-07), unit «د.أ» stays in the RTL flow after the number.
3. **Validation:** inline on blur, glyph+word (K-04), never color-alone, never blocks typing; only Save blocks, scrolling the first error into view.
4. **Keyboard toolbar:** «التالي / تم / مسح» only — Save is **not** in the toolbar; it is the pinned bottom control (thumb zone).
5. **Discard guard** on any dismissal with content: «في رقم مكتوب — تسجّله أو تتجاهله؟» — dialog with three paths: تسجيل / تجاهل / إلغاء.
6. **Save → quiet completion in place** (K-08): closure sentence with final digits, then the sheet dismisses revealing the updated list at the anchor position.
7. **Failure preserves** typed values and re-raises the keyboard; retry is inline.

### 5.2 Sheet vs full-screen form trade-offs

| Criterion | Sheet | Full screen |
|---|---|---|
| Data breadth | one value + context | multi-line documents |
| Keyboard conflict | worse — sheet and keyboard split space | better — whole body adjusts (N-07) |
| Context loss | low — the list stays visible | context pushed away |
| Discard cost | low | guard mandatory |
| Micro ruling | money events, filters, quick actions | orders/invoices, closing flow, long-list pickers |

---

## 6. Platform awareness — where iOS and Android diverge for Micro

| Dimension | iOS | Android | Micro ruling (Arabic-first) |
|---|---|---|---|
| App bar | Large-title collapse | M3 scroll-aware top app bar (large flexible variants exist) | Same collapse spec both; the question lives in the collapsing title; never fake iOS on Android |
| Back | Edge swipe from the right edge (RTL), interactive pop | System back + predictive back (14+); gesture edges on both sides | Support both; no custom back drawers; never block system back |
| Sheets | Detents medium/large, grabber | Modal bottom sheet with drag handle | Same snap points; one sheet-over-sheet max on iOS; Android converts deep chains to full-screen dialogs |
| Dialogs | Alert style | M3 dialog | Same content rules; destructive role follows platform convention while the word carries meaning (K-04) |
| Switches / segmented | UISwitch / UISegmentedControl | M3 switch / connected button group | Platform-native controls; never web checkboxes or styled `<select>` |
| Motion | Physics-ish defaults, sheets drag with the finger | Emphasized easing curve, predictive-back animations | Keep the 80–280ms register (A-09) mapped onto platform curves; honor reduced-motion on both |
| Date picker | Compact menu / wheel | M3 date-picker dialog | Both localized ar-JO, Gregorian, DD/MM/YYYY display, ASCII digits (C-05) |
| Context menus | Long-press preview menu | Long-press → bottom-sheet menu | One verb per item (DSY-25); menus open at the start (right) edge |
| Haptics | Notification/impact generators | Vibration effects | Policy per N-11; values are a device-test item (V-03) |
| Keyboard | Inset-driven scroll adjustment | WindowInsets (IME) + edge-to-edge | Never a fixed overlay without inset padding; Arabic keyboard default; no auto-zoom on focus |
| Contacts/share | System contact & share sheets | Intent equivalents | «دفتر الزبون» offers system intents instead of copy-paste text — a quiet native tell |

**Arabic-first on both without hybrid smell:** one RTL interaction spec (this report) plus a platform-delta table. Do not ship iOS patterns on Android or vice versa; do not use web-styled selects, date inputs, or tooltips where a platform picker exists.

---

## 7. State & connectivity UX — as native behaviors

1. **Connectivity is a status line, not a banner.** The truth slot in the header region carries it persistently and thinly: «الوضع: بدون اتصال · التسجيل محفوظ على الجهاز». Never a stacked banner card (R-03), never a toast.
2. **Offline queue:** every money action saves locally first and queues; queued rows show «قيد الانتظار» (D6); the queue drains oldest-first on reconnect, per row: «قيد الانتظار» → «قيد المزامنة» → «متزامن». The owner keeps working through the whole queue; sync never blocks the UI.
3. **Per-row indicators** follow the state grammar (DSY-15): slash = offline, sync glyph = syncing, check = synced, split = conflict, em-dash = unknown — glyph+word always, color tertiary (K-04).
4. **Pull-to-refresh:** native control on both platforms; semantics = revalidate → quiet completion («تم التحديث 08:31»); absent where data is device-only (drafts). It never gates first paint.
5. **Loading:** cached-first always (DSY-17) — figures from the local store with a staleness qualifier; skeletons **only** for genuinely unknown content (first boot); skeletons mirror the final row anatomy (never a spinner on a blank page).
6. **Error recovery is positional:** inline row-level retry «إعادة المحاولة»; form errors preserve input (5.1); conflict = alert row (D7) opening the effect-preview dialog (K-09). Never toast-only; never an alert that blocks the whole screen.
7. **Conflict resolution** shows both values and a choose path; the outcome writes a visible correction — reversed/correction states appear in the ledgers (K-03).

---

## 8. Web-smell test — 15 observable criteria

A reviewer can apply these to any single screenshot or 30-second scroll of any screen. Two or more hits = web-in-a-phone.

| # | Smell (observable) | Native answer |
|---|---|---|
| W-01 | Content sections with no owning destination — one long page of everything | Every screen belongs to a destination; depth is pushes (N-02) |
| W-02 | Page-fade transitions (or none) between screens | Push/pop tied to navigation events (N-04) |
| W-03 | Visible scrollbar or desktop scroll physics | Native momentum; exactly one scroll owner; no scrollbars (N-06) |
| W-04 | Hover-revealed affordances (underline/menus appear on hover) | Press states only, one-frame response (N-13) |
| W-05 | Full-width stacked cards/banners as the composition | Row grammar + hairlines; card quota ≤1 (R-03, DSY-12) |
| W-06 | Footer with links, copyright, or "about" block at screen bottom | No footers; the end of a list simply ends |
| W-07 | A real `<select>`-looking dropdown control | Sheets, segmented controls, platform pickers (§3.1) |
| W-08 | Fake status bar / phone bezel in product frames | Real chrome; review apparatus lives outside the surface (N-12, K-11) |
| W-09 | Browser back exits the app or breaks the stack | Back pops the stack; review HTML wired to in-app back (§3.2) |
| W-10 | Inputs hidden under the keyboard or page jumps on focus | Insets; save rides above the keyboard (N-07) |
| W-11 | Errors surfaced only as toasts | Positional inline recovery (§7.6) |
| W-12 | Web modal: floating ×, no drag physics, no scrim | Grabber + drag sheets; blocking dialogs (N-08/N-09) |
| W-13 | Equal-tile grids for settings or modules | Grouped vertical rows (R-08) |
| W-14 | Max-width centered column with wide gutters at 430px | Full-bleed native anatomy; edge-to-edge rows |
| W-15 | Decorative hero banners or stat tiles | Structural header-region figure only (A-02; R-07) |

---

## 9. Hand-off notes — what this report does NOT decide

- **Final destination model:** the orchestrator chooses among A/B/C; my lean is recorded in §2.5 only as input.
- **Legacy five-seat labels:** re-derived here per V-06; owner re-confirmation is a review-gate question.
- **Haptics final values:** device-test item (V-03); the policy (where, not how strong) is fixed in N-11.
- **Assistant IA position** (row vs app-bar icon): review-gate question; it must not become a fifth tab in v1.
- **Palette/typography:** untouched here by mandate; this report assumed only the fixed doctrine references needed for behavior (K-01…K-04).
