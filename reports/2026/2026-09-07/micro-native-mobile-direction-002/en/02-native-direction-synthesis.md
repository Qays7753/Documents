# 02 — Native Direction Synthesis

**Delivery:** `micro-native-mobile-direction-002` · Stage 1 · 2026-09-07
**Author:** central orchestrator (sole decision owner, per `en/01` §6)
**Inputs:** five specialist reports (`subagents/01…05`), `en/00` lessons buckets, `en/01` audit, fixed constraint register.
**Status:** three directions defined and one **recommended — not finalized**. Nothing here is approved; Stage 2 builds all three as interactive prototypes for the owner's decision.

---

## 1. What the specialist research established

1. **The failure was anatomical, so the fix is anatomical.** Every specialist converged: the previous deliveries composed *page content* (cards, document sections, review consoles). A native product composes *application chrome* (pinned headers, destination bars, stacks, sheets, rows). The binding rule adopted from the art-direction report: **the anatomy gate** — every pixel must have an application address (app bar / header / row / group / sheet / bar / chip); a "section of a page" is rejected on sight.
2. **Nativeness is a checklist, not a mood.** The architecture report produced 14 "native tells" (N-01…N-14) and a 15-item web-smell test; the critic independently produced a 12-criterion web-smell test with 10-second probes. Overlapping fatal four: chrome-free document flow, navigation without consequence, missing back discipline, motion-as-page-behavior. All three directions must pass all criteria.
3. **RTL is a direction system, not a translation.** Mirror travel and reading; never mirror data (specialist 04 §1). Back chevron points right at top-right; push enters from the left; edge-swipe back from the **right** edge; row chevrons point left; in/out uses ↑/↓ + verb + sign (never ←/→ which mirror); money = `<bdi dir="ltr">digits</bdi> د.أ` with the unit visually left of the number in RTL flow.
4. **Money discipline is fixed delivery-wide:** 3-decimal fils JOD everywhere (receipt = display = input), ASCII digits, `tabular-nums`, fixed amount slots, minus inside the isolate, compact form only where the row names direction and the surface names the unit.
5. **Truth is structural.** «صندوق / لي / عليّ» with confirmed-only main figures, visible pending deltas, and the reconciled corpus (closing 07/09/2026: صندوق **431.100** مؤكد (+27.750 بانتظار المزامنة), لي **664.250**, عليّ **348.500**) seeds all three prototypes verbatim. Honest-state vocabulary (10 states, glyph+label, color tertiary) is a delivery-wide acceptance criterion.
6. **Motion is navigation grammar.** Tokens: micro 80–140ms / standard 160–260ms / surface 280–360ms, hard caps (400ms single / 600ms sequence); curves — standard `cubic-bezier(0.2,0,0,1)`, decelerate `(0.05,0.7,0.1,1)`, emphasized push `(0.32,0.72,0,1)`, non-bouncy sheet `(0.22,1,0.36,1)`; interruption = retarget/reverse-from-current, 1:1 gesture handoff. Push/pop/sheet/tab/header-collapse each have one specified meaning; zero overshoot; page-fades are banned.
7. **Restraint contract (binding on all three):** one primary action per viewport; shadows only on sheets/dialogs (+C's FAB); ≤1 tinted surface per screen (tint marks money only); terracotta ≤8% of viewport (per-direction budgets below); teal ≤3%; body-size teal text banned on `#f4e4db`; radius only where a finger presses or a sheet floats; density floor ≥4 rows in first 60% of list screens; charts only under the K-10 honesty contract; decoration ban.
8. **The critic's pre-mortem is enforced in the builds:** no pager anywhere (pager vs RTL swipe-back is irreconcilable in review); truth header must prove itself as chrome within seconds; assemble motions ≤200ms, once per session; no chips cluttering first paint; hub-style truth "surfaces" only from persistent, visibly chrome-like controls.

## 2. The three directions

The three are orthogonal in **navigation model, screen anatomy, composition grammar, and interaction model** — not three recolorings. All share the fixed Terracotta roles, the honest-state grammar, the corpus, and the motion register.

| Attribute | **A — «الطاولة» / The Counter** | **B — «الأدراج» / The Drawers** | **C — «الميزان» / The Scale** |
|---|---|---|---|
| **Name** | الطاولة — The Counter | الأدراج — The Drawers | الميزان — The Scale |
| **Core metaphor** | The shop counter at closing: everything that matters lies flat on one surface; money is pinned, the day scrolls under it | The organized chest of drawers: the top drawer is always money; every drawer opens a focused list | The weighing scale: each screen weighs one question; truth sits in a settle-once slab; actions are sheets placed on the scale |
| **Composition grammar** | Three strata: (1) pinned full-bleed money band 112→64px, structural, never a card; (2) scroll of full-bleed 64px rows with day separators in the hairline gutter; (3) translucent frosted bottom bar. **Zero containers anywhere** | Large-title nav bar collapsing to inline; vertical stack of **inset groups** (12px radius, no shadows) on a deeper canvas; 13px section headers outside groups; money group tinted `#f4e4db` as a structural section | Small top app bar + **weigh slab** (~140px full-bleed `#f4e4db`: hero figure + لي/عليّ sub-figures) + soft 68px rows; **FAB «سجّل»**; truth sub-figures open half-sheets — truth never navigates away, it surfaces |
| **Surface & depth** | Tonal bands + hairlines; zero content shadows; L0 content / L1 frosted chrome (real blur + 0.5px hairline) / L2 sheet+scrim | Two-tone canvas makes groups read as drawers *without shadows*; hairlines inside groups only; groups separated by 8–12px canvas | Tonal ladder (canvas → surface → surface-2); hairlines rare; elevation only for FAB + sheets/scrim |
| **Shape language** | Controls 12 / sheets 20 / pills 999; **radius forbidden on rows, bands, separators, bar** — full-bleed stays square | Groups 12 / rows square inside / buttons 12 / sheets 20 / segmented 10 / chips 999; no radius on canvas, headers, amount columns | Controls 14 / groups 16 / sheets 24 / FAB 16 / pills 999; no radius on slab top edge or keypad strip |
| **Density** | Highest: 10–11 rows @390, 8 @320; quotas ≤2 bands, ≤12 rows, 0 cards | Medium: money group ~124px + 6–7 rows; quotas ≤4 groups, ≤5 rows/group, ≤1 tinted group | Lowest, deliberate: slab + 5–6 rows; quotas ≤6 blocks, 1 FAB, sheets absorb the rest |
| **Navigation model** | 4 destinations «اليوم · المال · الناس · العمل» + **docked capture seat «سجّل» in the bar** (opens capture sheet); per-tab stacks preserved; swipe-back from right edge | 5 seats «مشروعي الآن · العمل · **سجّل** · مالي · أدواتي» with سجّل as center action seat (capture sheet); large-title pushes with labeled back «رجوع»; segmented controls for period/status switching | 4 destinations «اليوم · المال · العمل · حسابي» + **FAB capture** (container-transform into capture sheet); sheet-first: collections, filters, and truth drill-downs are sheets; details push |
| **Primary screen (اليوم)** | Pinned money band (expanded: صندوق hero + لي/عليّ lines + sync meta) → day separator «اليوم 07/09» → 10 event rows → «أمس» rows continue under the frosted bar | Large title «مشروعي الآن» → tinted money group (3 truth rows + «سجّل عملية» primary row) → group «اليوم» (3–5 events) → group «يحتاج انتباهك» (conflict, overdue) | App bar → weigh slab (hero 40px صندوق + لي/عليّ sub-figures + sync state) → «آخر الحركات» 4–5 rows → FAB in thumb corner |
| **Money & operations treatment** | Amount column fixed 96px at row's left edge, tabular, sign inside isolate; out-amounts `#964e33`; swipe-left row actions (تحصيل/تعديل) on flat tonal pans | Amount slot fixed 88px in every row; chevron pushes to دفتر الجهة; inline value discipline; effect-preview dialog for corrections | Amount slot 96px; in/out ↑/↓ + verb + sign everywhere; slab carries state chip + «متزامن حتى 07/09 08:52»; tapping لي/عليّ opens half-sheet with the list |
| **Motion language** | Continuous scroll-linked header collapse; 1:1 interactive swipe-back with parallax peek; frosted bar persists; row action pans follow the finger | Large-title collapse; group-preserving pushes; action sheets from the bottom; segmented crossfades 160ms | Slab settles 260ms decelerate on truth change; FAB container-transform 260ms into sheet; pill indicator slides between destinations; sheets with detents |
| **Why it feels native** | Every element is chrome: pinned money, frosted bar, swipe rows, edge-swipe back — the card wall is *structurally impossible*; money literally never leaves the screen | The canonical native list dialect at major-company polish; large-title collapse, chevrons, segmented controls are the platform's own vocabulary | The most "installed-app" Android grammar: FAB, pill nav, sheet detents, state layers — nothing resembles a web composition |
| **Why it never becomes POS/banking/ERP** | No product grids, no checkout surfaces, no form-tables; operations appear only as event rows explaining money | Groups answer owner questions (who owes, what changed), not catalog/ledger-bookkeeping modules | One question per screen is constitutional; capture is a money event, never a cashier flow; suppliers are context rows, not procurement screens |
| **Risks (and build-time mitigations)** | Blur must be *real* (`backdrop-filter`) or it becomes mockup theater; swipe actions must not fight right-edge back (long-press alternative documented); highest build honesty budget | Least distinctive — could read as "settings app in terracotta"; identity must come from the tinted money group + IBM Plex Sans Arabic voice | Generic-fintech risk — strictest terracotta quota; sheet-first must not bury truth (slab always pins; drill-downs are sheets, not replaces) |

**Typography:** A = system Arabic stack (SF Arabic / Segoe UI / Noto Sans Arabic) — the platform voice; B = IBM Plex Sans Arabic (Google Fonts, system fallback); C = Readex Pro (Google Fonts, system fallback; digit audit at build — fallback to Noto Sans Arabic if numerals fail tabular discipline). All: 13px floor, 15px body, rows ≥56px (A: 64 / B: 60 / C: 68), line-height ≥1.6, zero letter-spacing on Arabic, `tabular-nums` on every digit run.

**Per-direction neutrals (free design space, warm, no pure black/white):**
- A light: canvas `#f7f2ec` · ink `#221b15` · muted `#6f6257` · hairline `rgba(34,27,21,0.10)` — dark: canvas `#18140f` · band `#332d27` · ink `#f3eadf`.
- B light: canvas `#eee9e2` (deeper so groups read as drawers) · groups `#ffffff` · ink `#221c18` — dark: canvas `#131010` · groups `#1f1b17` · money group `#332d27`.
- C light: canvas `#f4efe8` · surface `#fbf8f4` · surface-2 `#eae4db` — dark: canvas `#16120e` · surface `#211c17` · surface-2 `#2b2620`.

## 3. Comparison and recommendation

| Criterion (owner's bar) | A Counter | B Drawers | C Scale |
|---|---|---|---|
| Kills "web page in a phone" decisively | **Highest** — no containers exist to become cards | High — grouped lists cannot read as dashboards | High — but FAB+slab must not drift to "any fintech" |
| Financial truth central | **Highest** — money permanently pinned | High — money is the first group, one tap away | High — slab is emphatic; sheet-first must not bury it |
| Distinctive vs rejected work & vs generic apps | High | Medium (safest, least distinctive) | High |
| Arabic fit | High (max line length for names) | High (RTL-proven list dialect) | High (Arabic-designed face; slab labels fit) |
| Density for a working owner | **10–11 rows** | 6–7 | 5–6 |
| Build honesty in HTML review | Medium-high (blur/pin/swipe must be real) | **Highest** (every tell is a proven CSS/JS pattern) | Medium-high (detents, container-transform) |
| POS/banking/ERP drift risk | Low | Lowest | Low-medium |

**Recommendation: A — «الطاولة» The Counter.** It answers the owner's exact complaint most decisively (the card wall is structurally impossible; money truth is *pinned chrome*, not a floating hero card — the A-02 adaptation done literally), it carries the highest working density, and its tells (pinned band, frosted bar, swipe rows, interactive back) are unmistakably phone-native. **B** is the strongest fallback: the least risky build and the safest native dialect, at the cost of distinctiveness. **C** is the capture-ergonomics donor (sheet-first + FAB + docked numeric surface) with the highest genericness risk if its terracotta quota slips.

Per the adversarial critic: this ranking is argued, not scored into authority — the three prototypes exist precisely so the owner's eye, not a rubric, decides.

## 4. Binding build decisions for Stage 2 (all three prototypes)

| # | Decision |
|---|---|
| B-01 | Corpus verbatim from specialist 04 §6; reconciliation must survive: صندوق 431.100 مؤكد (+27.750 pending → 458.850), لي 664.250, عليّ 348.500; aging 47.650 / 553.400 / 63.200 / لا يوجد |
| B-02 | 3-decimal fils JOD, «د.أ» after isolated digit runs; DD/MM/YYYY; ASCII digits; ↑/↓ + verb + sign for in/out |
| B-03 | Screen set (min): اليوم · المال · الناس(لي/عليّ) · دفتر الجهة · الطلبيات + detail · المشتريات/الموردون · إغلاق الصندوق · سجّل (sheet) · البحث · الإعدادات/حسابي |
| B-04 | Honest states mandatory and visible in natural contexts: بانتظار المزامنة (07/09 27.750 sale), تقديري (electricity), تسوية (correction with before/after), تعارض (كافيه سما 20.000 vs 12.000 — resolution sheet with effect preview), ملغي (duplicate excluded from totals), unknown name («زبون غير مسجل»), loading skeleton (first visit to المال), empty search, quiet completion on save |
| B-05 | Charts only: 7-day cash in/out (earliest at right, gap hatched for 25–31/08 with footnote, source caption, text interpretation) + receivables aging bars (right baseline); no donuts/gauges |
| B-06 | Navigation: RTL push from left with 24–28% parallax + dim; interactive back from right edge; sheets with grabber + drag-dismiss; dialogs for consequential decisions only; browser back integrated via history stack |
| B-07 | Motion per specialist 03 tokens; reduced-motion = full alternatives (instant swaps, static marks), honored via `prefers-reduced-motion` + review toggle |
| B-08 | Review apparatus lives outside the app surface only: a small labeled review toolbar (width 320/360/390/430 · theme · motion · back to index) + `review-index.html`; the app surface contains product UI exclusively; **no bezel, no fake status bar, no desktop console** |
| B-09 | 320-first verification arithmetic (specialist 04 §7); two-line row grammar when state chip present; amounts/dates/state words never truncate |
| B-10 | A11y: focus order = reading order; `role="alert"` for conflict; aria-labels expand money/dates (interim, V-02); targets ≥44px (48 primary) |

## 5. What Stage 2 produces

`prototype/direction-a/`, `prototype/direction-b/`, `prototype/direction-c/` — three self-contained, interactive, app-like HTML routes (Arabic RTL default) covering B-03's screen set, plus `prototype/review-index.html` (comparison entry, state tour, review questions). Verification: headless-browser smoke pass per direction before the gate. Then **Stage 3 stops** — no approval, no Stage 4.
