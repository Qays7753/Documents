# 03 — Native Prototype Review Guide

**Delivery:** `micro-native-mobile-direction-002` · Stage 3 · 2026-09-07
**Audience:** the Micro product owner
**Purpose:** how to open and judge the three interactive prototypes in 20–30 minutes. The decision itself lives in `en/04-REVIEW-REQUEST.md`.

---

## 1. What you are opening

Three **independent, self-contained application routes** — not pages inside a review console, and not mockups:

| Route | Direction | One line |
|---|---|---|
| `prototype/direction-a/index.html` | A «الطاولة» The Counter | Money pinned on top forever, full-bleed rows, frosted tab bar, docked «سجّل» seat, swipe-back |
| `prototype/direction-b/index.html` | B «الأدراج» The Drawers | Large title that collapses, inset groups on a deeper canvas, 5-seat bar with center «سجّل», IBM Plex Sans Arabic |
| `prototype/direction-c/index.html` | C «الميزان» The Scale | Weigh slab that settles, truth drill-downs as half-sheets over the slab, FAB capture, pill nav, Readex Pro |
| `prototype/review-index.html` | Review index | The only place with review apparatus: links, state tour, deep-link experiments, decision questions |

**Deliberate absences (by design, per the rejection of the previous deliveries):** no phone bezel, no fake status bar, no desktop control panel framing the product, no spec prose around the screen. The small «مراجعة» pill you will see sits **outside** the app surface and carries the only review controls: width 320/360/390/430, light/dark, reduced motion, and a link back to the index. On phone-width windows it collapses to a handle so it never covers the app's tab bar.

## 2. Ten-minute route per direction (all three share the same data)

1. **اليوم (home).** Read the money surface first. Ask: do I know my position in one glance? Then scroll — watch the pinned band collapse (A), the large title fold into the bar (B), or the slab stay put while rows scroll (C).
2. **Push a detail.** Tap any party row (e.g., مطعم الشام) → its دفتر opens as a stack screen. Confirm the transition direction (RTL: new screen from the left), the back button top-right pointing right, and that browser back works too.
3. **حصّل دفعة.** On the party screen, collect a payment. Watch: sheet rises, amount prefilled, save → quiet completion sentence with final digits, numbers update everywhere (صندوق, the party, اليوم).
4. **سجّل (capture).** Open the dock/seat/FAB. Type an amount, switch نوع العملية, then drag the sheet down to dismiss → the discard guard dialog appears («في رقم مكتوب»).
5. **The honest states** (same in all three): بانتظار المزامنة (07/35 sale), تقديري (electricity), تسوية (tap it — before/after), تعارض (كافيه سما — open it, decide 20.000 vs 12.000 and watch the effect preview), ملغي (duplicate, excluded from totals), اسم غير محدد (زبون عابر).
6. **المال / مالي.** First open shows a skeleton once, then cached content. Read the 7-day in/out chart: earliest day on the right, the hatched «غير مسجل» gap before 01/09, source caption, and the text interpretation under it. Receivables aging bars grow from the right baseline.
7. **إغلاق الصندوق.** Count a different number (e.g., 425.600) → the variance dialog offers a تسوية with effect preview. Nothing is silently corrected.
8. **Widths & themes.** From the review pill: 320 (do it first — nothing may truncate money, dates, or state words), then 430. Dark: warm, no pure black; check the chart and the slab. Reduced motion: transitions become instant swaps — a full alternative, not a speed change.
9. **Search ⌕.** Type «برجر» → honest empty state. Type «كافيه» → parties/orders/events grouped results.
10. **The web-smell test (the owner's own bar).** At any moment ask: does anything here behave like a web page? (No hover-dependence, no page fades, no card walls, no document flow, no review console in frame.)

## 3. Where the directions genuinely differ (what to compare)

| Dimension | A Counter | B Drawers | C Scale |
|---|---|---|---|
| Where money lives | Pinned band, always on screen, collapses on scroll | First tinted group, one tap from home | Slab that settles; drill-downs open **over** it as sheets |
| Navigation | 4 tabs + docked «سجّل» seat in the bar | 5 seats, «سجّل» as center action seat | 4 tabs + FAB; sheet-first interactions |
| Composition | Full-bleed rows, hairlines, zero containers | Inset groups (radius 12) on deeper canvas, hairlines inside groups only | Tonal ladder surfaces (radius 16), sparse hairlines |
| Typography | System Arabic (SF/Segoe/Noto) — "installed app" voice | IBM Plex Sans Arabic — ledger-serious voice | Readex Pro — roundest, most contemporary voice |
| Density | 10–11 rows/viewport | 6–7 | 5–6 + quick-chips |
| Signature interaction | Interactive edge-swipe back with parallax; frosted bar | Large-title collapse; segmented controls | Slab settle animation; truth half-sheets; FAB→sheet |
| Terracotta budget | ≤4% (band + one action) | ≤6% (money group + action) | ≤8% (slab + FAB + pill) |

## 4. Deep-link experiments

The index (`review-index.html`) carries one-tap links; the parameters are:

- `?w=320` (or 360/390/430) — stage width
- `?theme=dark` — dark theme
- `?motion=off` — reduced motion
- `?demo=offline` — offline banner; new saves register as «بانتظار المزامنة»
- `?demo=error` — first save attempt fails with preserved input and a retry

## 5. Verification already performed (and its limits)

**Performed (headless Chromium, this run):** every route boots with zero page errors; tab switching, stack push/pop, sheets (open/drag/dismiss), dialogs, capture → quiet completion, collection with live figure updates, conflict resolution, closing variance → تسوية, search incl. empty state, first-visit skeleton, dark/light, 320/430 rendering, reduced-motion class; screenshots of key states are stored in `supporting/qa-screenshots/` (18 captures).

**Not performed (must stay honest):** real-device testing — keyboard avoidance, safe areas, touch physics of the edge-swipe back, haptics, screen-reader pronunciation of «د.أ», and RTL chart time-flow preference (V-01…V-04). The prototypes demonstrate the behaviors; devices will confirm them. No backend: all data is in-memory and resets on reload.

## 6. If something feels wrong

Note the direction letter, the screen, and what you felt («الشريط مثقل», «الأدراج باردة», «الميزان يخفي النقود»…). Focused rejection feedback is as valuable as approval — it narrows the revision.
