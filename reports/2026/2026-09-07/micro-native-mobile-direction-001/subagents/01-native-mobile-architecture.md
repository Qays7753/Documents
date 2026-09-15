# 01 — Native Mobile Product Architecture

**Delivery:** `micro-native-mobile-direction-001` · **Task ID:** 3-a · **Date:** 2026-09-07
**Agent:** Specialist 1 — Native Mobile Product Architect
**Inputs:** `worklog.md`, Stage-0 lessons (`en/00-previous-work-lessons.md`), intake audit (`en/01-intake-and-previous-work-audit.md`), both 2026-09-06 syntheses. Basis: iOS HIG (navigation bars, large titles, tab bars, sheets, keyboard avoidance, safe areas, back gestures, scroll edge effects) and Material 3 (navigation, predictive back, bottom sheets, FAB, insets).

**Thesis.** The prior deliveries failed a structural test, not a visual one. A native app is four primitives — destinations (tabs), a stack (push/pop, reliable back), transient surfaces (sheets/dialogs), and temporal state. A native Micro is a **stack-first list application with a persistent truth surface**, not a scrollable statement page. Values below are binding-ready; RTL stated for the Arabic-first build, LTR verification only.

---

## 1. Web-vs-native smell test (apply to every Micro screen)

| # | Test | Pass criterion |
|---|---|---|
| N-01 | Back-at-depth | Every screen below depth 1 returns via system back (Android) or chevron + edge-swipe (iOS); in-page "back" alone = fail |
| N-02 | Push transition | Row taps push a screen over the previous one (source-anchored); no in-place viewport re-render |
| N-03 | Sheet detents | Short contextual actions are draggable bottom sheets (detents, grabber, drag-to-dismiss), not centered web modals |
| N-04 | Keyboard shift | Focus keeps the field and primary action visible above the keyboard; the screen shifts, never "grows" |
| N-05 | Single scroller | One vertical scrolling region; any second axis is a snapped carousel, not a nested scroll body |
| N-06 | Reach | Primary actions in the bottom ~40% (thumb arc); top bar holds navigation and search only |
| N-07 | Safe areas | Insets respected at 320/360/390/430; no simulated status bar, no fixed 780/844px frame |
| N-08 | App bar behavior | Large title collapses on scroll (roots); compact bar gains material/tonal elevation (scroll edge effect) |
| N-09 | Temporal state | Loading/saving/error/offline appear, resolve, leave; a permanent "success" module = fail |
| N-10 | Tab mechanics | Tabs preserve each root's stack and scroll; re-tap pops to root / scrolls to top |
| N-11 | RTL edge gesture | Back swipe works from the correct RTL edge; chevron points toward leading (right in RTL) |
| N-12 | Dialog scarcity | Dialogs only for consequential confirmations — never navigation, forms, or reading |
| N-13 | Honest refresh | Pull-to-refresh only on server-fed data; PTR on the local Register is a fake affordance |
| N-14 | Review chrome | Zero review controls inside the app viewport (URL params + separate review index only) |

---

## 2. Top-level destinations

Owner questions: *position now* (truth), *what changed / why* (events), *who owes me / what I owe* (people), *attention today*, *capture*. Four tabs + one capture action: five tabs dilute reach, and capture is an **action, never a destination**. RTL order: first destination at the **right** end, Tools at the **left**; LTR mirrors.

| Seed | Verdict | Corrected destinations (RTL order) | Capture |
|---|---|---|---|
| A «الخلاصة اليومية» | Sound; labels fixed here | «الخلاصة» Brief → «الدفتر» Register → «الناس» People → «أدوات» Tools | Center slot «سجّل» in the tab bar — raised, action color, always opens the capture sheet, never switches tabs |
| B «الدفتر» | Sound; People must be top-level (highest-frequency question after cash) | «الدفتر» Register → «الناس» People → «العمل» Orders → «أدوات» Tools | FAB «سجّل» 56–64dp, does not auto-hide on scroll |
| C «الصندوق» | Orders seat justified only because home is position-scoped | «الصندوق» Counter → «العمل» Orders → «الناس» People → «أدوات» Tools | Persistent bottom action (center slot / FAB per platform) |

This replaces the verified five-seat shell «مشروعي الآن | العمل | سجّل | مالي | أدواتي» — the owner must ratify the new set at review (Stage-0 §4.1).

---

## 3. Navigation architecture per seed

**Stack norms (all seeds):** depth ≤ 3 per tab (root → entity detail → leaf/correction). No depth 4 in core flows. Capture is always a sheet over the current tab, never a push.

| Interaction | Push | Sheet | Dialog |
|---|---|---|---|
| Row → entry / party / order detail | ✔ | | |
| Capture (sale / expense / payment / delivery) | | ✔ large | |
| Truth-bar filters (B), filter chips | in-place state change | | |
| Collect / deliver / complete one row | | ✔ medium | |
| Share statement, period choice | | ✔ medium | |
| Cash closing | count screen (push) | summary sheet | final confirm |
| Delete / correct entry | | | ✔ CorrectionPreview |
| Sync conflict on an amount | | | ✔ keep-local / replace |
| Discard typed amount | | | ✔ guard |

**Back path (RTL).** iOS: chevron at top-leading (right in RTL), glyph points right, previous title if ≤24 chars; pop gesture on the **leading (right) edge** — verify on device, never ship a left-only recognizer. Android: bar arrow auto-mirrors right; **predictive back on** (Android 14+): back previews the destination (previous screen or home exit); back first dismisses an open sheet, then pops; at a tab root it previews app exit. Back never jumps tabs.

**State restoration.** Each tab owns an independent stack (iOS one `NavigationStack` per tab; Android per-tab back stack): persist screen identifiers, top entity ID, scroll anchor, active filter; restore on process death. Tab re-tap: iOS pops to root and scrolls to top; Android scrolls to top. Tab switch never resets sibling stacks — this is precisely what CSS view-switching broke.

---

## 4. Screen anatomy templates

| Element | iOS | Android M3 | Justification |
|---|---|---|---|
| Root app bar (A, C) | Large title ≈96pt + status inset, collapses to 44pt | Large top app bar 152dp → 64dp | Large title only where the title is the owner's question; not on working lists |
| Register root (B) | Compact 44pt + **pinned truth bar** 56pt (cash / لك / عليك, tappable) | Compact 64dp + pinned 56dp | B is a working list: truth never scrolls away. The bar must be app-bar/collapsing-toolbar chrome — a CSS `position:sticky` div is the exact web smell to avoid |
| Details | Compact 44pt / 64dp, back, title = entity, ≤1 trailing action | | Browsing surfaces, not reading pages |
| Tab bar | 49pt + 34pt inset, labels 10–11pt | Navigation bar 80dp incl. inset | 4 destinations + capture slot/FAB |
| Margins | 16pt/dp at all widths; amount column fixed 88px (retained) | same | 320 built and verified first |

Safe areas: content height = viewport − insets at all four widths; nothing pins to a fixed device height; scroll edge effect (iOS material / M3 tonal elevation) on every scrollable screen.

---

## 5. Sheet system and dialog rules

**Detents:** medium ≈ 50% of viewport (quick actions, filters, collect-a-payment); large ≈ 92% (capture form with keypad, cash-close summary). Grabber 36×4dp; top corners 12–16dp; scrim `rgba(34,28,24,0.40)` (retained). Drag-to-dismiss anywhere on the sheet. **Stacking limit: one sheet over a screen** — never a sheet over a sheet.

**A sheet must become a pushed screen when any of:** content exceeds ~90% height, needs >2 viewports of scrolling, has its own sub-navigation, or the task runs >~30s. In practice: party ledger, order detail, statement week — all push.

**Dialogs — consequential decisions only; exactly four in Micro:**
1. **إقفال الصندوق** confirm — variance sentence with final digits («عُدّ 142.75 د.أ · النظام 145.00 — فرق 2.25 د.أ. أكّد الإقفال؟»).
2. **Sync conflict** — two amounts with source sentences; «احتفظ بالمحلي» / «استبدل بالمتزامن».
3. **Correction/delete entry** — static will-change / won't-change lists (retained CorrectionPreview).
4. **Discard guard** — «في رقم مكتوب — تسجّله أو تتجاهله؟».

Anything else that feels like a dialog becomes a sheet, an inline row state, or a push.

---

## 6. Keyboard-aware capture form

Field order (sale): type segmented (بيع / مصروف / قبض / تسليم) → **المبلغ** (first focus) → الطرف (autocomplete) → تفاصيل (collapsed) → حفظ. The amount is the truth: first focus, prime zone.

- **Amount entry:** Micro's own keypad, not the OS keyboard — 3×4 grid, 48px keys (≈96px wide at 320), auto-slotting two-decimal places, live `1,245.50 د.أ` tabular formatting, long-press ⌫ clears, 3–4 quick chips (+5.00 / +10.00 / +20.00 / 0.50). Anchored to the sheet's bottom edge.
- **Primary action:** input-accessory bar (44pt) above the keypad — «إلغاء · حفظ» — never at the sheet top. One primary per form.
- **Avoidance:** focused field scrolls into view; sheet content shifts (iOS in-sheet avoidance; Android `adjustResize`); field and accessory bar never covered. OS keyboard only for note/party-search fields.
- **Draft protection:** typed amount survives dismissal behind dialog 4.
- One-handed: all capture controls in the bottom ~55%; the thumb never leaves the keypad arc.

---

## 7. Scroll ownership and refresh

One vertical scroller per screen. Seed C's day strip is a snapped horizontal carousel (a control, not a scroll body), and its day agenda should **push as a screen** instead of paging beneath the strip — paging under a strip creates two-axis ambiguity and steals back-gesture meaning. Sticky headers: Register date pins stick under app bar + truth bar (B); section headers may stick; nothing else. Pull-to-refresh: Brief root and People only (server-fed, stale-able); **never the Register** — an honest app doesn't "refresh" truth it owns. Spinner enters from the leading (right) edge in RTL.

---

## 8. State presentation architecture

| State | Surface | Rule |
|---|---|---|
| Loading (first boot) | Skeleton in the scroller | Skeletons only for unknown content; cached figures + staleness qualifier otherwise (retained) |
| Saving | Button state → receipt | Quiet completion in-sheet: closure sentence with final digits, one calm mark, dismiss |
| Field/row error | Inline at the point of action | Retry preserves input; never a modal for a field error |
| Offline | Thin 28–32px bar under the app bar: «غير متزامن — التسجيل يعمل» | Non-modal, self-dismissing; queue count in Tools |
| Syncing/synced | Status line in the truth slot («الحالة: مسجل · متزامن») | Temporal — appears during work, leaves when done |
| Conflict | Alert row at the source entry → dialog 2 | Never a quiet chip (retained) |

Sequencing: states are overlays with lifecycles, ordered by proximity to cause (row → bar → dialog). A screen rendering success/synced as permanent composition fails N-09.

---

## 9. Platform deltas

| Dimension | iOS | Android (M3) |
|---|---|---|
| Back | Chevron + leading-edge swipe (right edge in RTL) | System/predictive back; bar arrow mirrors |
| Capture | Center slot in tab bar | FAB, persistent |
| Sheets | Native detents, grabber | Modal bottom sheet, back-dismiss with predictive preview |
| Tabs | Translucent tab bar, tinted `#964e33` (light) | Nav bar with active indicator pill |
| Type | SF Arabic; tabular digits | Noto Sans Arabic; tabular digits |
| Haptics | Light impact on keypad commit; success notification on save | Equivalent `HapticFeedback` mappings |

**One deliberate cross-platform choice:** the capture keypad + quiet-completion receipt choreography is identical on both platforms — money-entry muscle memory must not fork. Everything else honors its platform.

---

## 10. Risks and ranked verdict

- **Seed B «الدفتر» — Rank 1.** Strongest native skeleton: a working list as root (the most native mobile structure), persistent truth bar, filters as tappable truths, FAB capture, push details, swipe/long-press row actions (destructive on trailing swipe; long-press → context menu with first-run hint for low-tech owners). Risks: undifferentiated stream at root (mitigate: date pins + attention markers); sticky bar must be real app-bar chrome; row gestures need discoverability.
- **Seed A «الخلاصة اليومية» — Rank 2.** Best answer to "what needs attention today"; large-title collapse is genuinely native. Risks: a day digest is editorial content — the most webward-drifting genre; quiet days hide position; "what-changed" blocks read as page sections unless every row is tappable-to-source and the timeline stays list-shaped.
- **Seed C «الصندوق» — Rank 3.** Sheet-first interaction is legitimately native; collect/deliver sheets are its best idea. Risks: cash hero + two counters is the closest to rejected banking drift; strip + paged agenda creates two-axis navigation; over-sheeting until the stack atrophies (deep work needs pushes, not detents).

---

## Binding recommendations

- **R-01.** Four destinations + capture as an action (never a fifth tab); per-seed labels and RTL order per §2; owner ratifies the shell change.
- **R-02.** Independent per-tab stacks with full state restoration (IDs, top entity, scroll anchor, filters); tab switch preserves siblings; re-tap pops to root / scrolls to top.
- **R-03.** Stack depth ≤ 3; the §3 push/sheet/dialog matrix is binding; capture is always a sheet.
- **R-04.** Back path per §3: iOS leading-edge (right in RTL) pop, right-pointing chevron; Android predictive back on; back dismisses sheet → pops → previews exit; never jumps tabs.
- **R-05.** App bars per §4: large titles only on Brief/Counter roots; Register = compact bar + pinned 56pt truth bar as real chrome, not sticky CSS.
- **R-06.** Sheets: medium 50% / large 92%, one-sheet limit, §5 conversion rule; dialogs restricted to the four named consequential cases.
- **R-07.** Capture per §6: type → amount (first focus) → party → details; custom keypad, 48px keys, two-decimal auto-slot, accessory-bar primary, draft guard.
- **R-08.** Single-scroller rule; C's day agenda pushes instead of paging; pull-to-refresh on Brief/People only, never the Register.
- **R-09.** State presentation per §8 — temporal, cause-adjacent, never permanent success composition.
- **R-10.** Platform deltas per §9; the single cross-platform constant is the capture keypad + receipt choreography.
- **R-11.** Verdict: B «الدفتر» first, A «الخلاصة اليومية» second, C «الصندوق» third; C's collect/deliver sheet model may be adopted into the winning direction.
- **R-12.** The N-01…N-14 smell test is a mandatory gate for every Stage-2 prototype screen before owner review.

---

*No HTML, CSS, or implementation produced. The three absent source packages remain un-inspected; nothing herein claims their contents.*
