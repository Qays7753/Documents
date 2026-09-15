# 02 — Native Direction Synthesis

**Delivery:** `micro-native-mobile-direction-001`
**Stage:** 1 — research consolidation, three native directions, recommendation (not finalization)
**Date:** 2026-09-07
**Author:** central orchestrator (decision owner). Inputs: specialist reports 01–05, Stage-0 lessons and audit.
**Status:** recommendation only. The owner selects at the Stage-3 gate; nothing here is an approval.

---

## 1. Consolidated findings

1. **The failure was structural, so the correction must be structural.** All five specialists converge: the rejected concepts were scrollable web compositions inside phone-shaped boxes. The native correction is the four primitive system — **destinations (tabs), a navigation stack (push/pop with reliable back), transient surfaces (sheets/dialogs), and temporal state** — applied through an app-level information hierarchy (Specialist 1, R-01…R-03). Nothing downstream can compensate for a missing stack.
2. **A native app cannot be faked by styling.** The countable native-premium floors (≤1 grouped surface per screen state, chrome ≤19% of viewport, one row template per list, two scroll-driven header states, ≤2 elevation levels, exactly 3 radii, ≤10% brand-hue pixels) separate "native premium" from "styled web" in observable pixels (Specialist 2, N1–N8).
3. **The mobile-only grammar is the moat.** Row long-press, swipe actions, FAB capture, edge-swipe back, drag-dismiss sheets — interactions a web page cannot convincingly fake — are the strongest anti-"web-in-a-phone" evidence available in HTML (Specialist 5, kill-test B).
4. **Motion is structure, not decoration.** A structural transition class (T-struct 300±40ms, interruptible, finger-driven) joins the retained calm register; easings E-decel / E-accel / E-flat; zero overshoot; tab switches crossfade with cached scroll; push enters from the trailing edge (RTL: left), back lives on the leading edge (RTL: right) (Specialist 3, M-01…M-04).
5. **Arabic-first composition is geometric, not translated.** Entry point at the top-right; hierarchy carried by Arabic typography; full mirroring table with a never-mirror list (digit runs, dates in isolates, logo, neutral icons, bottom-center capture); the refined money bidi contract (digit-run LTR isolate + «د.أ» in RTL flow, one nowrap atom, U+2212 inside) (Specialist 4, AR-01…AR-05).
6. **Money voice is a cross-direction constant.** ASCII digits, two decimals, tabular face, fixed 88/96px column, decimal alignment, «—» at number size for unknown. Differentiation lives in display figures and anatomy — never in number discipline.
7. **State honesty is the trust surface.** The 11-state Arabic vocabulary (محصّل، معلّق، تقديري، غير محدد، بانتظار المزامنة، متزامن، تعارض، ملغى، معكوس، تصحيح، عجز/فائض), each as glyph + word, never color alone; temporal states that appear, resolve, and leave — never a permanently-successful dashboard.

**Adversarial ranking (risk scores, not approvals):** B «الدفتر» 80.5 · A «الخلاصة اليومية» 64.9 · C «الصندوق» 63.0 (Specialist 5). Architecture ranking: B > A > C (Specialist 1). Art-direction scores: B 8.6 · A 8.2 · C 7.4 (Specialist 2). RTL fitness: A and B HIGH, C MEDIUM-HIGH (Specialist 4).

**Orchestrator rulings on specialist conflicts (documented, single owner):**
- **C's day agenda — paging vs push.** Specialist 1 ruled the agenda should push (two-axis ambiguity); Specialists 2/3 define day paging as C's signature. Ruling: prototype C keeps the strip + snap-paged agenda as its *signature* (strip is a control; one day per page; work pushes), with S1's dissent recorded — if the owner selects C, Stage 4 re-tests the two-axis concern with real owners.
- **Keypad entry model.** Specialist 1 proposed ATM-style auto-decimal slotting. Ruling: prototypes implement conventional keypad entry (0–9, «٫»/decimal, ⌫, live grouping, two decimals on commit, quick chips) — predictable for review; ATM-style slotting is a Stage-4 device-test decision.
- **English LTR verification scope.** Full English label switching (`?lang=en`) is implemented in the recommended direction only (B); A and C expose `?dir=ltr` structural mirroring with Arabic content retained, documented as layout verification.

---

## 2. The three native directions

All three share: fixed Terracotta palette per measured roles; the money voice; the Arabic state vocabulary; the 4-destination + capture-action shell (R-01); per-tab stacks with back; sheet-first capture with keypad and quiet completion; the four consequential dialogs; widths 320/360/390/430 with 320 built first; light + dark; reduced-motion alternatives; the canonical Arabic corpus (§4); no bezel, no review chrome in the viewport (AC-01).

### Direction A — «الخلاصة اليومية» / The Daily Brief

| Dimension | Specification |
|---|---|
| **Name** | «الخلاصة اليومية» — The Daily Brief |
| **Core metaphor** | The owner's morning briefing: the day as a statement you read in one pass, then act in |
| **Composition grammar** | Single-column iOS-editorial. The date is the collapsing large title (28/36 → 17/24, scroll-linked, absorbs the position figures into the compact bar). Position block = typographic ink on paper, edge-to-edge, zero containers; then a bounded "what changed" line; then the chronological timeline (rail on the right in RTL, hollow nodes); then an attention strip; then people snapshot. Digest capped at 5 blocks (AD/AC bound). |
| **Surface & depth** | One surface level (canvas + hairlines); E1 only for sheets/dialogs/capture slot. Light: warm paper `#faf7f4`. Dark: warm near-black `#1a1613`-family; the position block gains one tonal step; labels `#d59172`. |
| **Shape language** | Radii 4/10/16 (markers/buttons/sheet tops); 1px hairlines; attention marker = 2px `#964e33` edge bar; timeline rail 1px with 8px hollow nodes |
| **Information density** | 5 blocks before scroll at 390; timeline rows 64px, ≤2 lines; 24–32px breathing between blocks, zero variance inside lists |
| **Navigation model** | Tabs (RTL order): «الخلاصة» Brief → «الدفتر» Register → «الناس» People → «أدوات» Tools + **center-slot capture «سجّل»** in the tab bar (action, never a tab). Stack depth ≤3; capture always a sheet |
| **Primary screen composition** | Large title (day + date) → cash figure (32/40·700 tnum) with delta line → لك/عليك inline figures as hairline-divided tappable rows → one-sentence "what changed and why" → timeline of today's events (time, party, amount, state) → attention rows (overdue, due-tomorrow, conflict) |
| **Money & operational data** | Hero in ink; timeline rows carry amount + party + one action word (anti-news-feed correction); money atom contract everywhere; charts only in the pushed financial-truth screen |
| **Motion language** | Signature: **large-title collapse that absorbs the position figures**; timeline rows settle as one block; push/pop, sheet rise, quiet completion per the shared register |
| **Why it feels native** | iOS large-title anatomy, day-scoped digest, real stack into register/people, sheets for capture — the "Weather/Stocks + statement" discipline |
| **Why not POS/banking/ERP** | No checkout grids, no wallet hero (figures are ink on canvas, not balance displays), rows ≤2 lines with one action word, decisions before reading |
| **Risks** | Editorial drift into a news feed (bounded: 5-block cap, every row actionable); quiet days look empty (honest quiet-day state designed); narrative lines could read templated (bounded to one sentence + largest driver) |

### Direction B — «الدفتر» / The Register — **recommended**

| Dimension | Specification |
|---|---|
| **Name** | «الدفتر» — The Register |
| **Core metaphor** | The digitized دفتر: the home *is* the running register; financial truth is a pinned, live filter above it |
| **Composition grammar** | Compact 56px app bar (title + search) → **pinned truth bar (72px)**: «النقد \| لك \| عليك» as three live tabular figures that **filter the register when tapped** → one-line "what changed" caption (absorbed from A) → date-pinned sections with day totals → hairline rows (subject right, fixed money column left). Zero cards, zero containers. |
| **Surface & depth** | One level; the truth bar earns a single tonal step (white band on paper `#faf7f4`); E1 only for sheets/dialogs/FAB. Dark: canvas `#191512`, truth bar on raised `#201b17`, warm hairlines `rgba(213,145,114,0.18)` |
| **Shape language** | Radii 0/4/12 (rows/chips/sheets); the **2px Terracotta rule under the app bar** is the direction's only ornament; selected filter underlined in the truth bar |
| **Information density** | Densest: 128px pinned chrome (≈18%); 8–9 rows of 64px visible at 390; day pins carry inline day totals (داخل/خارج) |
| **Navigation model** | Tabs (RTL order): «الدفتر» Register → «الناس» People → «العمل» Orders (operations seat, absorbed from C) → «أدوات» Tools + **FAB «سجّل» 56dp** (bottom-inline-end, mirrors), `#964e33`/white, never auto-hides. Per-tab stacks; capture always a sheet |
| **Primary screen composition** | App bar → truth bar (three tappable truths + sync state) → what-changed line → «اليوم» pinned section with the day's events (time, subject, state glyph, amount in money column) → earlier days pinned sections → FAB |
| **Money & operational data** | Fixed 88px (320) / 96px (390+) mono tabular money column, inline-end aligned = decimal alignment; unit sub-column; state glyph + word per row; unknown «—» at number size; operational rows (العمل) reference money states without becoming checkout |
| **Motion language** | Signature: **truth-bar context shift** — tapping «لك» re-anchors the filter while rows crossfade beneath and the figures never travel (anti re-count); row press identity (color-only, 90ms, `#b4613f`) |
| **Why it feels native** | The list *is* the product: register-first working surface; FAB capture; long-press row menus; swipe actions on operational rows; push details with back — mobile-only grammar throughout (the critic's moat) |
| **Why not POS/banking/ERP** | The register lists *events*, never SKUs or checkout grids; the truth bar is a compact working filter, never a celebratory balance hero; one search field, no toolbar forests; rows ≤2 lines |
| **Risks** | Reading as a gray translated table (mitigations: warm ink hierarchy, Almarai + mono money voice, honest status words, demonstrated gestures); truth bar must be *seen* filtering (AC-04 proven in flow); distance from Calm Ledger kept by interactivity (live filter, mono column, FAB, pinned chrome) |

### Direction C — «الصندوق» / The Counter Hub

| Dimension | Specification |
|---|---|
| **Name** | «الصندوق» — The Counter Hub |
| **Core metaphor** | The cash desk: position first, the day's work one swipe away |
| **Composition grammar** | Position-first hub. Full-bleed **cash hero on deep warm ink** (~216px): label + delta + source-state + 40/48·700 warm-white figure (no spend affordances). **Counter split** (128px): «لك»/«عليك» as two large counters on one raised surface divided by a single 1px hairline (no gap, no border). **Day strip** (72px, right→left, snap) + paged day agenda. Macro-blocks, full-bleed, never boxed insets. |
| **Surface & depth** | Two in-flow levels (canvas + tonal macro-surfaces: hero deep, split raised); E1 sheets/dialogs/capture pill. Light: hero deep warm ink `#221c18`-family (~14:1 text), split `#ffffff` on paper. Dark: hero `#14100e`, split `#292420`, tints `#332d27` — a luminance ladder, not inversion |
| **Shape language** | Radii 8/16/20 continuous (day pills/buttons/sheets); selected day = `#f4e4db` pill + 4px `#cc785c` underline; hairline is the zero-space divider |
| **Information density** | Block-paged, not row-scrolled: 3 macro-blocks (416px) + 4–6 agenda rows at 390 |
| **Navigation model** | Tabs (RTL order): «الصندوق» Counter → «العمل» Orders → «الناس» People → «أدوات» Tools + **wide bottom capture pill «سجّل حركة»** (bottom-center, never mirrors). **Sheet-first**: most contextual work in sheets; deep work pushes |
| **Primary screen composition** | Hero (cash + delta + source-state) → counter split (tap → receivables/obligations stacks) → day strip + paging agenda (the day's events with amounts and states) |
| **Money & operational data** | Display figures proportional-bold (Alexandria); aligned/tabular money in lists and sheets per the shared money voice; counters carry sub-lines («من 4 جهات») — position glanceable in one screen |
| **Motion language** | Signature: **day paging + counter press** — pages run right→left in RTL, strip marker slides, settle 260ms E-decel; counter press color-only, heavy, quiet |
| **Why it feels native** | Material-3 macro-surface composition; sheet-first is the most one-handed-native model; day strip + paging is Calendar-grade native interaction |
| **Why not POS/banking/ERP** | Hero is labeled truth with delta and source-state — no spend affordances, no card number, no «ادفع», no asset tiles; counters are working entry points (tap → stack), not KPI tiles; all functions in sheets, so no module dashboard |
| **Risks** | Wallet silhouette (critic's C4 = 4/10 as originally specified; mitigations per S2/S5 applied: labeled truth, no spend affordances, split as one hairline surface); two-axis ambiguity (S1 dissent recorded; mitigated: strip = control, shallow pages, work pushes); geometric typeface body-size legibility (Alexandria title-only where large) |

**Differentiation proof:** the three differ in core composition (editorial scroll narrative / dense register + live filter control / macro-block hub + paging), header behavior (collapsing large title / compact bar + pinned truth bar / collapsing hero + sticky strip), primary interaction (read-then-act rows / filter + scan + FAB / tap counters + page days + sheet-first), density, and containers — with identical palette and money discipline.

---

## 3. Recommendation — Direction B «الدفتر» (not final; owner decides)

**B is recommended because its failure modes are quality problems, not category errors.** Its anatomy — register list, live truth-bar filter, FAB, long-press/swipe, push details — is mobile-only grammar that a web page cannot fake, which directly answers the owner's complaint. A leans toward the web-article error (bounded here, but the digest is inherently editorial); C leans toward the wallet/dashboard error (mitigated, but its silhouette is adjacent to an already-rejected category). B also carries the strongest bidi/money discipline (the fixed tabular column is its natural home), the smallest drift surface, and the owner's own vocabulary (دفتر). Per the critic's ruling, B **absorbs**: A's bounded "what changed" line and quiet-day state, and C's sheet-first capture and orders-as-operations seat. Nothing else is borrowed — each prototype keeps exactly one motion signature (M-16).

## 4. Canonical content corpus (all three prototypes)

Shop: **مؤسسة الحوراني للأدوات الصحية** (خالد الحوراني), Amman. Day: **الاثنين 07/09/2026**. Opening (Sunday close): النقد **3,180.00** · لك **2,380.00** · عليك **7,150.00**. End of day: النقد **3,477.50** (قبضت 825.00، صرفت 527.50 — أعلى بـ 297.50) · لك **2,240.00** (أخفض بـ 140.00) · عليك **6,650.00** (أخفض بـ 500.00). Parties: محمد الخطيب 940.00 لك (متأخر منذ 21/07/2026, 48 يومًا) · ورشة الأمان 540.00 لك (260.00 بيع اليوم + 280.00 سابقة بعد تحصيل 100.00 اليوم) · أبو زياد للمقاولات 760.00 لك (منذ 27/08) مع تعارض أمس (150.00 محلي مقابل 180.00 جهاز آخر) · مقهى الياسمين 0.00 (محصّل الأحد — صفر حقيقي) · شركة الرشيد للتوزيع 2,350.00 عليك (استحقاق 15/09) · مصنع البتراء للسيراميك والبلاط — فرع السخنة 4,300.00 عليك (استحقاق 30/09؛ طلب اليوم غير محدد القيمة) · مؤسسة الشرق للتجهيزات 0.00 (مسدّد). Ten Monday events (08:15 بيع نقدي 425.00 متزامن … 17:05 تعارض) exactly per Specialist 4 §8, arithmetic verified: 3,180 + 425 − 500 + 300 − 15 + 100 − 12.50 = 3,477.50. Week chart (01/09–07/09): in 620/545/730/gap/480/690/825, out 340/410/505/gap/385/455/527.50 — **الجمعة 04/09 unrecorded = gap + footnote**; totals in 3,890.00 / out 2,622.50. Aging: 0–30 يوم 1,300.00 · 31–60 يوم 940.00. One ملغى row + تصحيح link in Sunday's section; وجبة عمال 12.50 تقديري; تحصيل ورشة الأمان 100.00 بانتظار المزامنة.

## 5. Binding build decisions (numbered, single-owner)

| # | Decision |
|---|---|
| DSY-01 | Each direction = a folder `prototype/direction-{a,b,c}/` (`index.html` + `styles.css` + `app.js`), self-contained, opening as a **full-viewport application** — no bezel, no simulated status bar, no fixed device height, no review console in the viewport (AC-01). Review controls = URL parameters + separate `prototype/review-index.html` only |
| DSY-02 | URL parameters (all directions): `?screen=<id>` deep-link, `?theme=light\|dark`, `?width=320\|360\|390\|430`, `?dir=ltr` (mirror check), `?demo=offline\|error\|loading\|conflict\|closed`; B additionally `?lang=en` (full English LTR verification) |
| DSY-03 | Navigation = real per-tab stacks (JS): push from trailing edge (RTL: left, 300ms E-decel, outgoing 33% + dim), pop reversible, back chevron points right in RTL, focus returns to originating row; tab switch = crossfade + preserved per-tab stack and scroll (R-02/R-04, M-02…M-04) |
| DSY-04 | Sheets: 320ms E-decel rise, scrim 0.40, grabber, 1:1 drag-to-dismiss (96px/500px/s threshold), one sheet at a time; the four consequential dialogs only (cash-close confirm, sync conflict, correction preview, discard guard) — destructive dialogs never dismiss on scrim tap (R-06, M-05/M-06) |
| DSY-05 | Capture sheet (all directions): type segmented → keypad amount (first focus; 0–9, decimal, ⌫, live grouping, 2 decimals on commit, quick chips +5/+10/+20) → party field → note; input-accessory bar «إلغاء · حفظ»; keyboard-aware (sheet re-anchors, simulated keyboard block labeled as review affordance); quiet completion per §3 of report 03 with «تراجع» as an equal-weight path; discard guard protects typed amounts |
| DSY-06 | Truth-bar (B) is app-bar chrome pinned above the list and a **live filter** — tapping «النقد/لك/عليك» re-filters the register with persistent selection; figures update after a capture completes (AC-04) |
| DSY-07 | Money contract everywhere (AR-01…AR-04): `<bdi dir="ltr">` digit runs (sign inside, U+2212), «د.أ» in RTL flow, nowrap atom, tabular faces, fixed 88/96px column in list surfaces, «—» at number size for unknown |
| DSY-08 | States as glyph + Arabic word per the §3 vocabulary of report 04; temporal (appear → resolve → leave); offline banner non-modal; conflict = alert row + dialog; synced decays to neutral; queue badge counts real writes |
| DSY-09 | Type systems (AD-12): A = IBM Plex Sans Arabic (+ tnum); B = Almarai + IBM Plex Mono money; C = Alexandria display (+ Tajawal fallback) with the shared money voice in lists. Nothing below 13px; body 15px; rows ≥56px; no letter-spacing on Arabic |
| DSY-10 | Themes: light canvases `#faf7f4`-family; dark warm-dark ladders per direction (A `#1a1613`, B `#191512`/`#201b17`, C `#14100e`/`#292420`/`#332d27`); dark action fill `#8fd5d6` + `#1c1815` label; numbers in neutral ink, never brand color |
| DSY-11 | Charts: week cash trend (paired in/out bars, RTL time-flow, gap for unrecorded day + footnote, period/unit/source-state/interpretation sentence) in the pushed financial-truth screen; aging buckets as person list; relationship bar in party detail. Never in a home's first fold; ≤2 forms per direction |
| DSY-12 | Screen set per direction (8+): overview/root, financial truth (pushed), quick capture (sheet), receivables/obligations (people + party detail), orders/operational context, purchases/supplier context, cash closing (push + confirm dialog + closed/correction states), settings/profile. Plus search/filter, empty, loading skeleton, offline/sync, error+retry, pending/estimated/unknown, success, correction |
| DSY-13 | Long-press row menu (register rows: تفاصيل / تصحيح / مشاركة) — never the sole path; swipe actions on operational rows only (demonstrated on order rows); no swipe on money rows, no swipe-to-delete (M-12) |
| DSY-14 | Reduced motion: full alternatives (instant swaps, static marks, identical announcements); scroll-linked collapse retained; `prefers-reduced-motion` honored by default |
| DSY-15 | 320px built and verified first (subject budget arithmetic, 2-line truncation, money column ≥88px); then 360/390/430 via container queries |
| DSY-16 | The fixed logo appears once per direction (settings/profile header) — nowhere else (AD-15) |
| DSY-17 | Honest-copy rules: unknown ≠ 0 («قيمة غير محددة بعد», «—»); true zero only where truthfully zero (مقهى الياسمين، مؤسسة الشرق); deltas as Arabic sentences («أعلى بـ 297.50 عن أمس») |

## 6. What the prototypes must visibly prove (gate list)

Back-at-depth with restored scroll and filter state; a push and a pop in both directions; the capture sheet with keypad, saving state, quiet completion receipt, and تراجع; the truth-bar live-filtering (B) / counter stacks (C) / collapse-absorbs-figures (A); search with real filtering and a no-match empty state; loading skeleton on first open of a data tab; offline banner + queued row + queue badge; sync error with retry preserving state; pending/estimated/unknown rows; the conflict row and its resolution dialog; cash closing with variance dialog and closed state; the ملغى/تصحيح pair; light/dark; 320/390 widths; reduced-motion; RTL correctness of every mirrored element — and, decisively, **that opening a screen feels like an application screen, not a website presenting a device mockup**.

## 7. Known limitations (pre-declared)

HTML is a review medium only; platform behaviors (predictive back, haptics, OS keyboard, real detents, edge gestures) are approximated and labeled; gesture demos are simplified (long-press menus implemented; swipe actions demonstrated on operational rows); data is a static canonical corpus; A and C carry layout-level LTR verification only; no backend, no persistence beyond the session; production integration and Stage-4 files are not started.
