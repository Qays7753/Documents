# 02 — Native Art Direction Hypotheses

**Delivery:** `micro-native-mobile-direction-002` · Stage 1 · 2026-09-07
**Author:** Specialist 2 — Senior Art Director & Visual Systems Designer
**Scope:** research/analysis only. This report proposes visual-direction hypotheses; it does **not** pick the final direction (the orchestrator decides in `en/02`), does not define navigation models (another specialist owns that — each hypothesis only *names* its assumed navigation context), and does not build anything.

**Inputs read in full:** `en/00-previous-work-lessons.md`, `en/01-intake-and-previous-work-audit.md`, the fixed constraint register (C-01…C-08), and the K/A/R/V buckets derived from `micro-visual-product-concept-001` and `-002`.
**Inputs inspected visually (3 PNGs):** `001/…/01-today-390-light-ar.png`, `002/…/shot-01-home-light-ar.png`, `002/…/shot-06-statement.png`.

---

## 1. What the rejection means for art direction

The audit's diagnosis ("web content composed inside a phone frame") converts into five hard art-direction rules that every hypothesis below obeys:

1. **Anatomy gate.** Every pixel must have an *application address*: app bar / collapsing header / list row / grouped section / bottom sheet / bar chrome / keypad surface. No pixel may have a *page address* (hero section, content card, article block, caption strip). R-03/R-04/R-05 die here.
2. **Depth is earned by structure, not decoration.** Separation comes from pinned headers, hairlines, tonal steps, blur, and scrim — never from stacked floating rounded boxes (R-03).
3. **Terracotta is structure, not atmosphere (R-06).** It marks the single primary action and the money-header region; it never washes a screen.
4. **The screen is edge-to-edge (R-01/R-02).** No bezels, no fake status bars, no desktop consoles, no spec prose in-frame. Chrome is app chrome only.
5. **Transitions are navigation grammar (R-11).** Push/pop, sheet up/down, tab crossfade — each with a distinct, meaning-only motion in the 80–280 ms register, zero overshoot.

Additional hard floors carried unchanged into every direction: Arabic ≥13 px anywhere, body 15 px, rows ≥56 px, line-height ≥1.6, **never letter-spacing on Arabic**, ASCII digits with `tabular-nums`, digits isolated `<bdi dir="ltr">` with «د.أ» after the run in RTL flow, `DD/MM/YYYY`, unknown never `0.00`, glyph+label not color-alone.

---

## 2. Shared measured pairings (computed this run; re-verify in Stage 2 QA per V-07)

These apply to all three directions and are labeled *computed, not inherited*.

| Pairing | Value | Verdict / role |
|---|---|---|
| `#964e33` fill + `#ffffff` text | 6.11:1 (inherited) | the ONLY terracotta resting action fill |
| `#b4613f` fill + white | ≈4.45:1 | press state ONLY, ≤200 ms transient, never a resting pair |
| `#964e33` text on `#f4e4db` | ≈5.0:1 | hero money figure on the soft money band is legal |
| `#d59172` fill + `#1c1815` text (dark) | ≈6.8:1 | dark mirror of the action fill |
| `#d59172` text on `#332d27` (dark) | ≈5.2:1 | dark hero money on dark soft band |
| `#057b7c` on `#f4e4db` | ≈4.1:1 | **fails 4.5 for 13–15 px text** — accent text is banned on tinted surfaces at body sizes; large/glyph only |
| `#079fa0` on white | 3.24:1 (inherited) | graphics OK |
| `#079fa0` on warm canvas (`#f8f3ed`) | ≈2.9:1 | **borderline fail** — teal strokes on warm canvas must use `#057b7c` (≈4.6:1); `#079fa0` only as ≥3 px fills on white/near-white groups |
| `#cc785c` on warm canvas | ≈3.0:1 | atmosphere/decorative only; never text; prefer `#964e33` strokes on canvas |

Practical consequence adopted by all three directions: **in-money = teal family, out-money/action = terracotta family, both at text-grade values on canvas; brighter values only inside white groups or as fills.**

---

## 3. Direction hypotheses

At a glance:

| | A «الطاولة» The Counter | B «الأدراج» The Drawers | C «الميزان» The Scale |
|---|---|---|---|
| Grammar | full-bleed bands + rows, zero containers | grouped inset lists | tonal steps + sheets |
| Depth | pinned chrome + blur | tonal groups, no shadows | tonal ladder + FAB/sheet elevation |
| Density | 10–11 rows | 6–7 rows | 5–6 rows |
| Terracotta budget | ≤4% | ≤6% | ≤8% |
| Face | system Arabic stack | IBM Plex Sans Arabic | Readex Pro |
| Nav context | bottom bar + stack + sheet capture | 5-seat bottom bar + pushes | bottom nav + FAB + sheet-first |

> A fourth hybrid ("Counter header + Drawer groups") was sketched and deliberately **not** developed, to keep the hypotheses orthogonal for the orchestrator.

### Direction A — «الطاولة» · The Counter

**Core metaphor.** The shop counter at closing time: everything that matters lies flat on one surface — money first, then today's movement — nothing floats, nothing decorates. The truth is *pinned*, the day *scrolls under it*.

**Composition grammar (application anatomy only).** A screen is exactly three anatomical strata:
1. **Pinned money header (structural, never a card).** Full-bleed soft band `#f4e4db` (dark `#332d27`), 112 px expanded → 64 px collapsed; carries the hero figure, its state glyph, and «آخر مزامنة ٠٨:١٥». It compacts on scroll like a large title — it is chrome, not content.
2. **Scroll of full-bleed event rows**, grouped by thin day separators («اليوم ٠٧/٠٩», 13 px label in the hairline gutter), each row 64 px: right-aligned title+meta, left-edge fixed 96 px amount column (LTR-isolated, tabular).
3. **Translucent bottom bar** (frosted canvas at 82% + 0.5 px top hairline) carrying the destination set; capture opens a bottom sheet, not a screen.
Push = detail screen; every mutation = bottom sheet. No white boxes exist anywhere in this direction.

**Surface & depth language.** Tonal *bands* + hairlines; **zero shadows on content**. Max elevation levels = **3**: L0 content (flat), L1 pinned translucent chrome (blur + hairline), L2 sheet/dialog over `rgba(20,16,12,0.45)` scrim. Depth is signaled by "what stays pinned while other things move."

**Shape language.** Radii set: controls 12, sheets 20 (top corners), chips/pills 999, sheet grabber 4×32. **Radius is forbidden** on rows, bands, day separators, canvas, and the bottom bar — anything full-bleed stays square; the finger only ever meets a rounded *control*, never a rounded *container*.

**Information density.** Highest of the three. 320 px: money band 112 + 8 rows of 64 px visible. 390 px: 10–11 rows. Block quota: **≤2 bands, ≤1 pinned header, ≤12 rows, 0 cards.** One question per screen; detail is a push.

**Typography plan.** **System Arabic stack** (SF Arabic on iOS / Noto Sans Arabic system default on Android) — the platform voice, so the app feels installed, not embedded. Digits = system `tabular-nums`. Scale (390 px / 320 px):

| Role | Size/LH/Weight |
|---|---|
| Hero money | 36/44 700 → 32/40 700 |
| Screen title | 28/34 700 → collapses to 17/22 600 in bar |
| Section label | 13/18 600 |
| Row title | 15/24 500 |
| Row meta | 13/18 400 |
| Caption | 13/17 400 |
| Amount column | 15/24 600 tabular, fixed 96 px |

**Terracotta usage.** **≤4% of viewport surface.** Roles only: money band `#f4e4db` (structural, one per screen), one primary fill `#964e33`+white (pressed `#b4613f`), `#964e33` for out-money amounts and active-tab tint. `#cc785c` appears only as decorative glyph fill inside white groups.

**Dark theme philosophy.** "Counter lamp at night": canvas `#18140f`, band `#332d27` (fixed), hairline `#3b342b`, ink `#f3eadf` / `#b7a897`, bar scrim `rgba(24,20,15,0.78)` — bars *darken* on blur, never lighten. Terracotta shifts to `#d59172` text/graphics; never an inverted-light look.

**Native tells (what makes it read as a phone app).**
1. Collapsing pinned money header with hairline fade-in on scroll.
2. Full-bleed rows with **swipe-left actions** (تحصيل / تعديل) revealing flat tonal action pans — no buttons in rows.
3. Translucent frosted bottom bar with scroll-under content.
4. Pull-to-refresh wired to sync truth («جارٍ التحديث…» → «تمت المزامنة ٠٨:١٥»).
5. Edge-swipe back with previous screen parallax peek (RTL-aware).

**Row anatomy (one line of spec so prototypes cannot drift).** Row = 64 px tall, 16 px side padding, title 15/24 at the top, meta 13/18 beneath (glyph+label state), amount 15/24 600 in a 96 px fixed slot at the visual left edge, `tabular-nums`, sign inside the `<bdi dir="ltr">`, «د.أ» in the RTL flow after the run. Separator: 0.5 px hairline inset 16 px on the trailing side only. Press state: 6% ink overlay, no color swap.

**Screen walkthroughs (how the grammar composes).**
- *اليوم (Today):* pinned money band (expanded) → day separator «اليوم ٠٧/٠٩» → 10 full-bleed event rows → day separator «أمس ٠٦/٠٩» → rows continue under the frosted bottom bar. The only tinted pixels are the band + one «سجّل عملية» text action in the bar area.
- *مالي (Money):* pinned band with three compact figure lines (نقد / لي / عليّ) → one «إغلاق اليوم» primary sheet-invoker → receivables rows → obligations rows with due-date meta. Detail of any row is a push; collection is a swipe action or sheet.

**Direction-local reject list (in addition to §6):** no tinted chips beside titles (color exercise); no rounded “summary cards” above lists (R-03 in disguise); no hairline frames around the band; no white content boxes ever — even for empty states (empty state = inline rows + dashed slots, not an illustration card).

**Assumed navigation context (owned elsewhere):** 4–5-seat translucent bottom bar + stack pushes + sheet capture; compatible with the A-10 seat vocabulary.

**Honest-state rendering.** Unknown = the amount slot renders «قيمة غير محددة بعد» + «سجّل» inline action with a dashed hairline slot — never 0.00. Syncing = 2 px `#057b7c` progress hairline under the pinned band. Estimated/pending/conflict = glyph+label inside the row meta column.

---

### Direction B — «الأدراج» · The Drawers

**Core metaphor.** The organized small-office chest of drawers: the top drawer is always money; every drawer opens to a focused list. Familiar native structure — *grouped inset lists* — used at major-company polish, with a warm Jordanian-market palette instead of cool gray.

**Composition grammar (application anatomy only).** A screen is:
1. **Large-title nav bar** («مالي», «العمل»…) that collapses to an inline title on scroll.
2. **A vertical stack of inset groups** (12 px radius, 16 px side margins, no shadows): the **money group** is first and tinted `#f4e4db` (dark `#332d27`) as a *structural section*, not a floating hero card; content groups follow with 13 px section headers *outside* the group (weight/size only — never letter-spaced Arabic).
3. Rows 60 px with chevron affordance for pushes, inline value at the left edge (88 px fixed, LTR-isolated), swipe actions inside groups.
4. **Translucent bottom bar** + occasional inline notice row (pinned under the nav bar with hairlines — a native inline alert, not a banner card).
Detail = push with labeled back («رجوع»); confirmations = action sheets; everything else = inline rows.

**Surface & depth language.** Two-tone canvas: a slightly deeper grouped backdrop makes white groups *read as drawers without shadows*. Max elevation levels = **3**: L0 canvas, L1 groups (pure tonal step, no elevation), L2 translucent chrome, L3 sheet/dialog over scrim (levels L1–L3 are the three *functional* ones). Hairlines live **inside** groups only; groups are separated by 8–12 px of canvas, never by lines.

**Shape language.** Radii set: groups 12, inner rows 0 (square, hairline-separated at 16 px inset), buttons 12, sheets 20, segmented control 10, chips 999. **Radius forbidden** on canvas, on hairlines, on the amount column, and on section headers.

**Information density.** Medium. 390 px: money group (~124 px) + 6–7 rows visible. Quotas: **≤4 groups per screen, ≤5 rows per group, ≤1 tinted group, 0 cards** (a group with <3 rows must merge with a neighbor).

**Typography plan.** Single bespoke Google face: **IBM Plex Sans Arabic** (400/500/600/700) — an engineered, ledger-serious voice; Latin digits carry `tnum` for tabular discipline (fallback: system `tabular-nums`). Scale:

| Role | Size/LH/Weight |
|---|---|
| Hero money (in group) | 32/40 600 |
| Screen title | 28/34 700 → 17/22 500 |
| Section header | 13/18 600 |
| Row title | 15/24 400 |
| Row meta | 13/20 400 |
| Caption | 13/18 400 |
| Amount column | 15/24 600 tnum, fixed 88 px |

**Terracotta usage.** **≤6% of viewport.** Roles: the one tinted money group, primary action fill `#964e33`+white (one per screen; pressed `#b4613f`), `#964e33` for amounts-out and chevron-active states. All other groups stay neutral — the tint marks *money*, nothing else.

**Dark theme philosophy.** "Drawers closed for the night": canvas `#131010`, groups `#1f1b17`, money group `#332d27` (fixed), hairline `#373028`, ink `#f4ece2` / `#ab9e8f`. Groups brighten one tonal step, never glow; terracotta action becomes `#d59172` fill with `#1c1815` content (≈6.8:1).

**Native tells.**
1. Large-title collapse into inline nav bar with back label.
2. Grouped-inset lists with inset hairlines and chevrons — the canonical native list dialect.
3. Translucent bottom bar with content scrolling beneath.
4. System edge-swipe back + iOS-style action sheet for destructive confirmations.
5. Segmented control for period switching (اليوم/الأسبوع/الشهر) inside group headers.

**Row anatomy.** Row = 60 px tall inside groups, 16 px inner padding, title 15/24 right, meta 13/20 under, value 15/24 600 in an 88 px fixed slot at the left edge, chevron 16 px at the far left for pushes, hairline separator inset 16 px starting *after* the text gutter. Press state: 6% ink overlay inside the group (clipped by the group radius).

**Screen walkthroughs.**
- *مشروعي الآن (Home):* large title «مشروعي الآن» → money group (نقد / مستحق لي / عليّ rows + «سجّل عملية» primary row) → group «اليوم» (3–5 event rows) → group «تحتاج انتباهك» (receivables due, conflict). Two groups max beyond money on this screen.
- *العمل (Work):* large title → segmented control (الطلبيات / الزبائن) → group per status section header (13 px, outside groups) → rows with status glyph+label in meta; order detail is a push with labeled back.

**Direction-local reject list (in addition to §6):** no tinted group except the money group (a second tinted group = color exercise); no groups with a single row; no icon-drawer grids (R-08 equal tiles); no document-style ruled full-width lines between groups (R-04 tell); no section headers inside groups (headers belong outside, in canvas).

**Assumed navigation context (owned elsewhere):** the 5-seat bottom bar «مشروعي الآن · العمل · سجّل · مالي · أدواتي» (A-10, re-derivation pending) with stack pushes; sheets only for actions.

**Honest-state rendering.** Unknown = money row renders «قيمة غير محددة بعد» with a dashed underline slot and «سجّل» chevron-row; never 0.00. Estimated = «تقديري» glyph+label in row meta with `#057b7c`-only-as-reinforcement. Conflict = pinned inline notice row under the nav bar with «تعارض — بحاجة لقرارك» + action, never a floating banner card.

---

### Direction C — «الميزان» · The Scale

**Core metaphor.** A weighing scale: every screen *weighs* one question. Money truth sits in a settle-once weigh slab; every action is a deliberate sheet placed on the scale — capture, correction, collection. The friendliest and most action-centric of the three.

**Composition grammar (application anatomy only).** A screen is:
1. **Small always-on top app bar** (17/22) — this direction keeps titles compact so the slab dominates.
2. **The weigh slab:** full-bleed `#f4e4db` band (dark `#332d27`), ~140 px, one hero figure + two sub-figures (لي / عليّ) with glyph+label states; it *settles* (260 ms decelerate, zero overshoot) when values change.
3. **A soft content list** of 68 px rows (taller, friendlier) with pill press state-layers.
4. **Bottom navigation bar with active pill indicator** + **one tonal FAB «سجّل»**.
All mutations = bottom sheets with detents (half/full); the capture sheet docks the numeric surface above the keyboard; confirms = centered dialogs with effect preview (K-09).

**Surface & depth language.** **Tonal steps first** (canvas → surface → surface-2 ladder), elevation reserved for exactly two things: the FAB (one soft shadow) and sheets (scrim). Max elevation levels = **3** (tonal content / chrome+FAB / modal). Hairlines are 0.5 px and rare — this direction separates by tone, not lines.

**Shape language.** Roundest of the three: controls 14, groups 16, sheets 24 top, FAB 16, pills 999. **Radius forbidden** on hairlines/dividers, on the top edge of the weigh slab (it meets the screen edge full-bleed), and on the keypad display strip.

**Information density.** Lowest, most deliberate. 390 px: slab 140 + 5–6 rows visible. Quotas: **≤6 blocks per screen, 1 FAB, 1 primary, sheets absorb everything else**; one question per screen is constitutional here.

**Typography plan.** Google face **Readex Pro** (400/500/600/700) — generous apertures, strong at large sizes, Arabic-first design; digits rendered tabular via `tabular-nums`, with Inter digits as the Stage-2 fallback if Readex numerals fail the tabular audit (V-05-style check, explicit). Scale:

| Role | Size/LH/Weight |
|---|---|
| Hero money | 40/48 700 |
| Screen title | 24/32 600 → 16/22 500 |
| Section label | 13/20 600 |
| Row title | 15/24 400 |
| Row meta | 13/20 400 |
| Caption | 13/18 400 |
| Amount column | 15/24 600 tabular, fixed 96 px |

**Terracotta usage.** **≤8% of viewport** (highest budget, still minority): weigh slab `#f4e4db`, FAB container `#f4e4db` with `#964e33` icon+label (state layer on press; or `#964e33` fill variant with white), nav pill `#f4e4db`+`#964e33`, amounts-out `#964e33`. `#cc785c` decorative only.

**Dark theme philosophy.** "Damped scale": canvas `#16120e`, surface `#211c17`, surface-2 `#2b2620`, slab `#332d27` (fixed), hairline `#3d362d`, ink `#f5ecdf` / `#b4a695`. FAB inverts to `#d59172` container with `#1c1815` content (≈6.8:1) — the one luminous object in a dark room, deliberately.

**Native tells.**
1. Bottom-sheet capture with detents, scrim, grabber, and drag-to-dismiss.
2. Tonal FAB with press state-layer (never a color swap to a failing pair).
3. Bottom nav bar with pill indicator that slides between destinations.
4. Numeric surface docked above the system keyboard, stable digits (A-07 discipline).
5. Weigh-slab settle animation on truth changes + edge-swipe back.

**Row anatomy.** Row = 68 px tall, 20 px side padding, title 15/24 + meta 13/20 stacked right, amount 15/24 600 in a 96 px left-edge slot, pill-shaped press state-layer (full-row, clipped only by screen edge — rows are not rounded containers here, the press pill is). Separators: 0.5 px hairline, used sparingly; rows are otherwise separated by 4 px of canvas tone.

**Screen walkthroughs.**
- *الميزان (Hub):* app bar «الميزان» → weigh slab (hero 40/48 + لي/عليّ sub-figures + sync meta) → rows «آخر الحركات» (4–5) → FAB «سجّل» in the thumb corner. Tapping any slab sub-figure opens a half-sheet with its rows — truth never navigates away, it *surfaces*.
- *التسجيل (Capture sheet):* full detent sheet over scrim → segmented نوع العملية (قبض/دفع/فاتورة) → numeric surface docked above keyboard (A-07 discipline: big digits, visible state) → quiet closure sentence with final digits (K-08).

**Direction-local reject list (in addition to §6):** no second hero surface anywhere (the slab is the only `#f4e4db` band); no FAB menu clusters (one FAB, one action); no full-screen modal captures — capture is a sheet, always dismissible; no decorative rounded frames around the slab; no chart panel on the hub (charts live behind a question, K-10).

**Assumed navigation context (owned elsewhere):** 3–4-seat bottom navigation + FAB capture; hub-and-sheet rather than deep stacks.

**Honest-state rendering.** Unknown = slab renders «قيمة غير محددة بعد» with tilde glyph and a direct «سجّل» action; estimated = «تقديري» chip inside the slab meta line (glyph+label, color tertiary); syncing = small ring beside «آخر مزامنة» in the slab; conflict = full-width sheet summon from the slab («تعارض في القيمة — راجع») rather than an alert card.

---

## 3.5 Shared transition grammar (applies to every direction; completes A-09)

Both rejected deliveries had no navigation events, so no transition grammar. These are the five events every direction must own, at the shared register (80–280 ms, decelerate, zero overshoot, meaning-only):

| Navigation event | Motion | Duration | Content behavior |
|---|---|---|---|
| Push (detail) | incoming view slides from the leading (left in RTL) edge; previous view parallax-shifts −24% and dims 8% | 240 ms | back affordance visible mid-gesture |
| Pop / edge-swipe back | reverse of push; gesture-proportional, cancellable | ≤240 ms | previous header unpins last |
| Tab switch | crossfade + 8 px vertical settle, no slide | 160 ms | scroll position preserved per tab |
| Sheet up/down | slide 24 px→rest + fade scrim to 45%; down reverses, grabber-drag proportional | 200 ms up / 160 ms down | focus returns to invoker |
| Header collapse | continuous, scroll-linked (not timed); hairline fades in at collapse start | scroll-linked | money figure crossfades to compact size |

Haptic notes stay open (V-03); the visual grammar must not depend on them.

---

## 4. Comparison matrix

| Criterion | A «الطاولة» The Counter | B «الأدراج» The Drawers | C «الميزان» The Scale |
|---|---|---|---|
| **Distinctiveness vs rejected work** | **High** — zero-card, full-bleed band grammar; maximal break from card walls and document flow | Medium — closest to platform-native defaults; the tinted money group is its only signature | **High** — slab + sheet-first grammar; nothing in either rejected delivery resembles it |
| **Arabic fit (RTL, floors, bidi)** | **High** — full-bleed rows give Arabic titles maximum line length; day separators in the gutter read naturally RTL | **High** — grouped lists are RTL-proven at platform level; chevrons mirror correctly; Plex Arabic is strong at 15 px | High — Readex Pro is Arabic-designed; slab long-labels («قيمة غير محددة بعد») fit; needs Readex numeral audit |
| **Financial-trust feel** | **Highest** — money is literally always pinned on screen; deltas visible while scrolling | High — tinted money group + disciplined amount column; money one tap away, not always visible | High — the weigh slab is emphatic, but sheet-first hides truth *between* actions |
| **Dashboard-risk (reverting to SaaS feel)** | **Low** — no cards, no tiles, density is list-like | **Lowest** — grouped lists cannot read as dashboards | Low — FAB+pill nav is generic-app, not dashboard; slab is emphatic but singular |
| **Implementation honesty (HTML prototype, Stage 2)** | Medium-high — pinned/blur/swipe are real but need care to not look browser-made; blur is the riskiest illusion | **Highest** — every tell is a well-understood CSS/JS pattern with honest desktop equivalents (no blurred-chrome gambles) | Medium-high — sheet detents and keyboard docking must be simulated carefully to avoid "web modal" tells |
| **Density for a working owner** | **Highest** (10–11 rows) | Medium (6–7 rows) | Lowest (5–6 rows, deliberate) |
| **Risk noted for the orchestrator** | Blur/translucency must be *implemented*, not faked, or it becomes mockup theater again | May read as "settings app" — needs the money group and warm palette to carry identity | Generic-friendliness risk (any fintech looks like this); terracotta quota discipline matters most here |

---

## 5. Ranked recommendation (with reasoning; final call is the orchestrator's)

**1. A — «الطاولة» The Counter.** It answers the owner's exact complaint most decisively: the card wall is structurally impossible (no containers exist), the money truth is *pinned chrome* rather than a floating hero card (the A-02 adaptation done literally), and the density fits a working micro-owner's day. Its tells (collapsing pinned header, swipe rows, frosted bar) are unmistakably phone-native. Main cost: the Stage-2 prototype must genuinely implement blur/pinning/swipe — honesty is achievable but must be budgeted.

**2. B — «الأدراج» The Drawers.** The safest native dialect and the strongest implementation honesty; if the owner's bar is "feels like a major company's app," this is the fastest guaranteed route. It ranks second only because its grammar is the least *distinctive* — it risks reading as "an iOS settings app in terracotta" unless the tinted money group and IBM Plex Arabic voice carry the identity.

**3. C — «الميزان» The Scale.** The best *capture ergonomics* (sheet-first + docked numeric surface is the right home for the A-07 discipline) and the warmest personality, but it fragments financial truth across sheets and carries the highest generic-fintech risk. It is the natural **hybrid donor**: if the orchestrator merges directions, C's sheet grammar is the component to graft onto A or B — not its navigation.

**Hybrid note.** A's header + B's groups is the obvious merge candidate; I deliberately did not develop it so the orchestrator weighs three orthogonal grammars first.

---

## 6. Shared restraint contract (anti-card-wall, anti-color-exercise)

Binding on every direction, prototype, and the eventual synthesis:

1. **Anatomy gate:** nothing enters a screen without an application address (header, row, group, sheet, bar, chip, keypad). If a component's address is "section of a page," it is rejected on sight.
2. **One primary per screen:** exactly one `#964e33`+white fill per viewport; every other action is text, tonal chip, or row. `#b4613f` exists only as its ≤200 ms press state.
3. **No floating-box rule:** shadows are permitted on exactly three object classes — FAB (C only), sheets, dialogs. Any other shadow = card wall regression = reject.
4. **Group minimums:** a group must hold ≥3 rows or merge; a screen shows ≤1 tinted surface (`#f4e4db`/`#332d27`); tint marks money only.
5. **Color quotas:** terracotta family ≤8% of any viewport (A: ≤4%, B: ≤6%, C: ≤8%); accent teal ≤3%; the screen is ≥89% neutral. Color never carries meaning alone (K-04).
6. **Contrast law on tinted surfaces:** body-size teal text is banned on `#f4e4db` (≈4.1:1); accent strokes on warm canvases use `#057b7c`, not `#079fa0` (≈2.9:1).
7. **Radius forbearance:** radius only where a finger presses or a sheet floats; full-bleed strata stay square. Never on hairlines, canvas, amount columns, or Arabic text containers of any kind.
8. **Density floor:** any list screen shows ≥4 rows within the first 60% of scroll height — a screen that posters instead of listing is rejected.
9. **No horizontal card carousels;** period switching uses segmented controls or sheets. Charts only under the K-10 honesty contract (question, period, unit, source state, text alternative, gaps ≠ zero).
10. **Motion is navigation grammar:** push/pop, sheet up/down, tab crossfade, header collapse — 80–280 ms, decelerate, zero overshoot, no page-fades. Motion without a navigation event is deleted.
11. **Decoration ban:** no Jordanian motifs (C-07), no logo repetition (C-01), no illustration without an information duty.
12. **State grammar is glyph+label first** (K-03/K-04): unknown never 0.00, estimated/pending/offline/syncing/synced/conflict/correction are first-class in *every* direction's grammar, rendered per its own row/sheet anatomy.

---

## 7. Hand-offs and open items for the orchestrator

- I did **not** decide navigation models, destination sets (V-06), or the typography production gate (V-05); each hypothesis states its assumed context and its verification need (Readex numeral audit for C; Plex `tnum` confirmation for B).
- My computed pairings (§2) are labeled *computed this run* and must be re-measured in Stage 2 QA per V-07.
- Stage-2 honesty budget (highest-risk illusions): A's blur/translucency and swipe rows; C's sheet detents and keyboard docking; B is the low-risk build.
- If the owner wants a single testable direction fastest, B is the least risky prototype; if the owner wants the strongest conceptual answer to "not a web page," A is the sharpest.
