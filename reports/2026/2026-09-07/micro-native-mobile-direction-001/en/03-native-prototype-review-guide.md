# 03 — Native Prototype Review Guide

**Delivery:** `micro-native-mobile-direction-001`
**Stage:** 3 — how to inspect the three prototypes before deciding
**Date:** 2026-09-07
**Audience:** the owner (decision maker). Time needed: ~15–20 minutes.

---

## 1. How to open the prototypes correctly

Start from **`prototype/review-index.html`** — it is the review control surface, and it lives *outside* the product. Every direction link opens as a full application screen: **no phone bezel, no simulated status bar, no desktop console**. If you ever see review chrome inside a product screen, that is a defect — none exists in these builds.

- **Best experience:** open the links on an actual phone (or set the browser window to a phone width). At real phone widths the app fills the whole screen.
- **Desktop review:** the app renders as a centered column at the chosen width; the space around it carries no controls.
- **Widths:** every direction is verified at 320 / 360 / 390 / 430. Use the width links in the review index or add `?width=320` (etc.) to any direction URL.
- **Themes:** light and dark ship together. Use `?theme=dark`, or switch inside **أدوات → المظهر** (a real product path).
- **English LTR verification:** direction B carries a full `?lang=en` mirror. Directions A and C expose `?dir=ltr` (layout mirror with Arabic content retained) — layout-level verification only, by design.
- **Fonts load from Google Fonts** (IBM Plex Sans Arabic / Almarai + IBM Plex Mono / Alexandria). Offline, system fallbacks render with slightly different metrics; layout is unaffected.

## 2. URL parameters (the only review affordances)

| Param | Values | Effect |
|---|---|---|
| `screen` | `register/brief/hub, ledger, people, work, tools, position, entry, party, order, closing` | Deep-links that screen (pushed screens arrive pushed) |
| `theme` | `light · dark` | Overrides theme (default follows the OS) |
| `width` | `320 · 360 · 390 · 430` | Sets the app column width for desktop review |
| `demo` | `offline · error · loading (B) · closed · collapsed (A/C)` | Freezes a state: offline banner + queue; sync error + retry; loading skeleton; closed day; collapsed hero |
| `lang` | `en` (B only) | Full English LTR verification |
| `dir` | `ltr` (A/C) | Layout mirror check |

## 3. The same money rules everywhere (judge consistency)

All three directions share one money language, on purpose: ASCII digits, two decimals (`1,245.50 د.أ`), the unit after the number in Arabic reading order, tabular mono digits, a fixed aligned money column, «—» at number size for unknowns. If any screen breaks this, flag it — number discipline is not a per-direction style.

## 4. Review routes per direction (~5 minutes each)

### B — «الدفتر» The Register (recommended)

1. **Register root.** Note the pinned truth bar (النقد · لك · عليك) and the 2px terracotta rule. **Tap «لك» then «عليك»** — the register re-filters live, day pins and totals re-contextualize, figures never move. This is B's signature.
2. **Scroll** — the FAB hides downward and returns upward; date pins stay pinned.
3. **Long-press any row** (≈ half a second) — a context sheet offers details / correction.
4. **FAB «سجّل»** → type an amount on the keypad (try the +5/+10/+20 chips) → **حفظ** — watch the quiet completion: saving state on the button, then a receipt sentence with the new cash total, then «تم». The truth bar updates and the new row lands highlighted.
5. **Search** (app bar icon) — type «الخطيب» — filtering is live; try a word with no matches for the honest empty state.
6. **الناس tab** — skeleton on first open, then customers/suppliers segments, chips (متأخر / هذا الأسبوع), search with Arabic normalization (try «الرشيد» and «رشيد»).
7. **العمل tab** — operational rows; **drag a waiting row toward the right** — the quick-action reveals (swipe, demonstrated on operational rows only — never on money rows).
8. **المركز المالي** (scale icon in the app bar) — position detail, week chart with the unrecorded Friday as a gap, aging buckets, then **إغلاق الصندوق**: type `3469` → variance (عجز 8.50) → تأكيد → the confirm dialog → closed state → قيد تصحيح.
9. **States:** the conflict row at the top of today — tap it, resolve it (choose 150.00 or 180.00), watch the alert become a resolved record. `?demo=offline` → banner + queue badge + the 15:50 row awaiting sync; capture something offline and read the receipt note. `?demo=error` → retry → syncing → synced toast.
10. **English LTR:** `?lang=en` — the whole product mirrors; money and digits never mirror.

### A — «الخلاصة اليومية» The Daily Brief

1. **Brief root.** Read it top to bottom like a statement: large title, cash figure, لك/عليك hairline rows, one-sentence "what changed and why", the timeline (rail on the right, hollow nodes), attention rows, people snapshot.
2. **Scroll down** — the large title collapses and the compact bar absorbs the cash figure (A's signature). Scroll back — it expands.
3. **Timeline rows** are real records: tap one → the entry detail pushes; back returns to the same row.
4. **Center capture slot** in the tab bar («سجّل») → the full capture sheet → receipt → updated hero + compact bar + a new "الآن" timeline row.
5. **الدفتر tab** — the full register (all of today's and earlier records), search, the ملغى row in Saturday and the تصحيح flow from Sunday's صيانة المولدة row.
6. **`?dir=ltr`** — mirror check with Arabic content.

### C — «الصندوق» The Counter Hub

1. **Hub root.** The deep cash hero (label + figure + delta + sync state — no spend affordances, no wallet chrome), then the counter split: لك / عليك on **one** surface divided by a single hairline, then the day strip.
2. **Swipe the agenda horizontally** (drag left/right) — pages snap; the strip follows and the active day highlights (C's signature). Tap a strip cell to jump.
3. **Find الجمعة 04/09** — an unrecorded day: an honest empty page, never zero bars.
4. **Scroll** — the hero condenses to a slim cash strip; the day strip stays pinned.
5. **Capture pill «سجّل حركة»** at the bottom — sheet-first capture; same keypad, same receipt.
6. **Tap a counter** → the position screen pushes; back returns. **العمل tab** is C's operations seat; resolve the conflict from today's page and watch the strip's today marker turn to a check.

## 5. What to judge — and what not to

**Judge visually and experientially:** does it feel like a real mobile app from a serious product company; is it comfortable one-handed in Arabic; is the money legible and calm; do navigation, back, sheets, and states feel predictable; is the composition distinctive.

**Do not judge:** colors of the palette (fixed by identity), code quality, performance, data depth (a static, arithmetically consistent demo corpus), or the exact typefaces (web-review stand-ins for SF Arabic / Noto Sans Arabic device fonts — the per-direction type systems are the decision, the faces are Stage-4 tunable).

## 6. Known limitations (pre-declared, honestly)

- Platform behaviors are approximated in HTML: no predictive back, no real haptics, no OS keyboard (a labeled simulated keyboard demonstrates sheet re-anchoring instead), detents are single-step, edge-swipe back is replaced by the back button and Escape.
- Swipe actions are demonstrated on operational rows only; long-press menus exist in B (A and C use row-tap + sheets).
- Data is static and session-only; "sync" is choreography, not a backend. Refresh pull-to-refresh is intentionally absent from local lists (honest refresh).
- The fixed Micro logo asset is not present in the repository; a reserved placeholder slot appears once (settings/profile header) — no logo was invented.
- The C day strip horizontally scrolls at 320px by design (a control, not a page).
- `?lang=en` (B) swaps UI chrome and row labels; realistic party names remain Arabic by intent.

## 7. Defects found and fixed during build QA (transparency)

Tab-bar icon key mismatch (fixed), truth-bar figure overflow at 320/390 (fixed — figures now measured to fit at both widths), queue-badge anchoring (fixed), FAB/pill overlap with the last row (mitigated with scroll clearance + native hide-on-scroll), one bidi typo (fixed). Verified with headless Chromium: no console errors, capture→receipt→truth-update flow, live filter, conflict resolution, closing flow, offline and error demos, 320/390 layouts, light/dark.
