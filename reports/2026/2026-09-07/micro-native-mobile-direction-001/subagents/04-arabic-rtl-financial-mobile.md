# 04—Arabic-First RTL Composition, Money Bidi Contract & Financial Truth Vocabulary

**Delivery:** `micro-native-mobile-direction-001`
**Task ID:** 3-d·**Agent:** Specialist 4—Arabic RTL Financial Mobile Specialist
**Date:** 2026-09-07
**Inputs:** worklog brief, `en/00-previous-work-lessons.md`, prior-cycle RTL/a11y report (bidi contract, legibility floors, contrast arithmetic), fixed palette + seeds A/B/C.
**Honesty note:** contrast figures recomputed today (WCAG 2.x formula)—matching the carried prior values exactly; bidi/mirroring/input guidance is professional-knowledge-based analysis. 07/09/2026 is a Monday (calendar-verified).

---

## 1. Arabic-first composition doctrine

An RTL-native screen is not an LTR screen with arrows flipped. The **top-right corner is every screen's entry point**—where Arabic reading begins. Anatomy: large title (inline-start, right) → the one truth this screen owns → supporting rows, right-anchored (`text-align: start`), money at the inline-end (left) edge as the row's terminus. Hierarchy is done by **Arabic typography itself**—size steps, weight, x-height contrast between display and naskh-body forms—never by translated web chrome (sidebars, breadcrumbs, card grids).

**Mirroring rules:**

| Element | RTL behavior |
|---|---|
| Forward push / back pop | new screen slides in from the **left**; back from the right |
| Back affordance / disclosure chevron | back arrow top-**right** pointing **right**; row chevron points **left** |
| Edge-swipe back / row full-swipe actions | from the leading **right** edge |
| Tab order / DOM focus | reading order—first focusable top-right, moving right→left |
| Tab underline, slider, stepper, paging | fill/grow from inline-start; later days page in from the left |
| Sheet grabber | centered pill—symmetric, nothing to mirror |
| Chart time-flow | **right (earliest) → left (latest)**—§4 |

**Must NOT mirror:** digit runs and dates inside their LTR isolates (only *position* moves); physical/numeric keyboard layout; logo and fixed artwork; direction-neutral icons (check, plus, gear, magnifier, spinner); the bottom-center capture control. Numbers are content, not chrome—flipping them flips the value.

---

## 2. The bidi/money contract (refined, binding)

Retained core + two refinements:

1. **Isolate exactly the digit run**—digits, `en-US` grouping comma, decimal point, sign—inside `<bdi dir="ltr">`.
2. **Unit «د.أ» OUTSIDE the isolate**, in the RTL flow: `<span class="money"><bdi dir="ltr">1,245.50</bdi> د.أ</span>`. In RTL a later element renders further left, so the unit lands left of the number = **after it in reading order** («1,245.50 د.أ»); the same markup reads correctly in the LTR verification view. Unit-inside-isolate was measured to render «د.أ 20.00»—forbidden.
3. **Sign inside the isolate, one minus codepoint (U+2212):** `<bdi dir="ltr">−5.00</bdi> د.أ`—outside, it detaches.
4. **Refinement—money atom as one nowrap unit:** number + unit wrap together or not at all; money never truncates or breaks mid-run—a truncated number is a fabricated number.
5. **Refinement—delta sentences isolate the bare number between Arabic words:** «أعلى بـ <bdi dir="ltr">215.50</bdi> عن أمس»—بـ and عن أمس stay in the RTL flow. Times likewise: «<bdi dir="ltr">10:05</bdi> صباحًا».

| Content | Contract |
|---|---|
| Plain money | `<bdi dir="ltr">425.00</bdi> د.أ`—renders «425.00 د.أ» |
| Signed delta | `<bdi dir="ltr">+300.00</bdi> د.أ` / `<bdi dir="ltr">−500.00</bdi> د.أ` |
| Date range | `<bdi dir="ltr">06/09/2026</bdi> إلى <bdi dir="ltr">12/09/2026</bdi>`—bare `06/09–12/09` forbidden |
| Parentheses | only INSIDE an isolate with their content; **accounting `(85.00)` negatives forbidden**—use −85.00 |
| Mixed names | bare `<bdi>مكتب العبدلي Ltd</bdi>` (first-strong auto-isolation)—Latin tail never reorders |

**Fixed money column (register surfaces):** constant width for the largest tabular value; values inline-end aligned; with two decimals + `tabular-nums`, inline-end alignment **is** decimal alignment. Unit gets its own sub-column. Missing shows «—» at number size, never 0.00.

---

## 3. Financial truth surfaces in Arabic

**Naming hierarchy—headline = owner's word, qualifier = bookkeeping term:**

| Surface | Primary label | Qualifier (small, muted) |
|---|---|---|
| Cash | **النقد المتاح** | — (compact: «النقد») |
| Receivables | **لك** | ذمم مدينة |
| Payables | **عليك** | ذمم دائنة |

The triad announces as one group: «النقد المتاح 3,477.50 د.أ، لك 2,240.00 د.أ، عليك 6,650.00 د.أ».

**State vocabulary (glyph + word; color never alone):**

| State | Label | Glyph | Appears when |
|---|---|---|---|
| Collected | **محصّل** | filled dot + check | payment landed in cash |
| Pending | **معلّق** | hollow dot | recorded, not yet collected/paid |
| Estimated | **تقديري** | dashed-outline dot + badge | value from memory, no receipt |
| Unknown | **غير محدد** | hollow circle with em-dash | price never agreed—never 0.00 |
| Awaiting sync | **بانتظار المزامنة** | outlined cloud + up-arrow | saved locally, offline queue |
| Synced | **متزامن** | double check | record confirmed to cloud |
| Conflict | **تعارض** | split/two-tone dot | two versions of one record; never mistakable for synced |
| Cancelled | **ملغى** | circle with diagonal slash | voided before effect; stays visible |
| Reversed | **معكوس** | two opposing curved arrows | undo of a posted money effect |
| Correction | **تصحيح** | hollow dot + link to original | paired with the record it fixes |
| Shortage/surplus | **عجز / فائض** | attention ring / ring + plus | day-close cash count vs recorded; net position |

**Delta wording:** «أعلى بـ 297.50 عن أمس»·«أخفض بـ 140.00 عن أمس»·«كما هي عن أمس»—never a bare sign on summary surfaces.

**"What changed and why" narrative pattern** (headline delta → mechanism → largest driver → open items):
«النقد المتاح 3,477.50 د.أ—أعلى بـ 297.50 عن أمس، لأنك قبضت 825.00 وصرفت 527.50. أكبر قبضة اليوم: 300.00 د.أ من محمد الخطيب. عندك سجل واحد بانتظار المزامنة وتعارض واحد ينتظر مراجعتك.»

---

## 4. Charts in RTL financial context

Time flows **right→left**: earliest at the inline-start (right) edge, latest at the left; bars and fills grow from inline-start, staying inside the screen's reading rhythm; the LTR verification toggle mirrors it with the same data.

Chart contract (no exceptions): **period** (isolated dates), **unit** «د.أ» in the header, **source state** chip («متزامن»/«محلي»), and a **text interpretation line that IS the non-visual alternative** (`role="img"` + `aria-label` = the sentence verbatim). Tick labels: tabular digits in isolates; weekdays as Arabic words («السبت، الأحد، الاثنين…»); values only at totals and the peak (clutter cap). A day with no records is a **gap + footnote**, never a zero bar.

A chart earns its place by answering an owner question: (1) **cash week trend**—paired in/out bars per day, teal/brown with pattern distinctness; (2) **aging buckets**—person list oldest-first with inline segment bars (solid current, hatched overdue)—aging is a per-person decision; (3) **collection split**—one horizontal track: من أصل «لك»—محصّل this week vs متبقٍ, hatched bracket for retained deposits. Anything else is decoration.

---

## 5. Accessibility beyond color

Every state = glyph + word (§3). **Carried measured pairs (recomputed):** white on #cc785c **3.28:1—forbidden for text** (atmosphere/surface only); #964e33 + white **6.11:1**—the action pairing; #057b7c + white **5.08:1**—accent text; dark #d59172 with dark ink **5.26:1 (#332d27) to 6.82:1 (#1c1815)**.

**Recommended neutral extensions (measured; central confirmation required):**

| Theme | Token | Role | Measured |
|---|---|---|---|
| Light | #332d27 on #ffffff / #e3f5f5 | primary ink | 13.59 / 12.07:1 |
| Light | #6e6156 on #ffffff / #f4e4db | muted secondary text | 5.99 / 4.84:1 |
| Light | #9a8d81 | hairlines (non-text ≥3:1) | 3.23:1 |
| Dark | #332d27 | canvas (fixed token) | — |
| Dark | #3a332c | elevation step | ink 10.04:1; #8fd5d6 7.49:1; #d59172 4.81:1 |
| Dark | #f4e4db on #332d27 | body ink | 10.98:1 |
| Dark | #cfc2b7 on #332d27 | muted secondary | 7.80:1 |
| Dark | #8fd5d6 / #5ec0c1 on #332d27 | accent text / graphics | 8.19 / 6.33:1 |

- **Focus in RTL:** full-perimeter 2px ring at 3:1 vs adjacent; focus follows reading order; first focusable = top-right primary control.
- **Touch floors:** ≥44×44 targets (48 primary/keypad); full rows 56–64px, single targets; ≥8px gaps; transparent padding gives quiet links («سجّله») a 44px hit area.
- **Money mutations → screen reader:** one polite announcement, never stacked: «سُجّل تحصيل 300.00 د.أ من محمد الخطيب—النقد المتاح صار 3,405.00 د.أ». Validation/conflict: assertive once, then downgrade.
- **Scaling/expansion:** Arabic runs ~15–25% longer than English; Dynamic-Type-like scaling to 200%; money wraps as whole atoms, never truncates. 320px test: «مصنع البتراء للسيراميك والبلاط—فرع السخنة» → 2-line clamp + fade, word-boundary truncation only (joined letters cannot break mid-word), full name in the accessible name. Floors: body ≥15px, caption ≥13px, line-height ≥1.6.

---

## 6. Keyboard and input in Arabic

- **Amount field:** `inputmode="decimal"`; value always stored/displayed as **ASCII digits regardless of keyboard layout**—Arabic-Indic keys (٠١٢٣…) normalize to ASCII on input; «٫» U+066B and «٬» U+066C map to `.` and `,`. Live grouping as typed; two decimals on commit.
- **Date field:** DD/MM/YYYY, `inputmode="numeric"`, content in one LTR isolate; long-form dates stay pure Arabic with ASCII digits («12 أيلول 2026»).
- **Arabic search normalization (query and corpus both):** strip diacritics and tatweel (ـ U+0640); unify أ/إ/آ → ا; ة → ه; ى → ي; optionally strip leading «ال» on both sides—«الرشيد» finds «شركة الرشيد للتوزيع», «حوراني» finds «مؤسسة الحوراني للأدوات الصحية».
- **Long party names in pickers:** search + recents first; options clamp to 2 lines, full name in the accessible name.

---

## 7. Dark mode for Arabic financial UI

Warm-dark, never pure black: **#332d27 canvas** + recommended **#3a332c elevation step**—sheets lift off by warmth, not cold gray. Body ink #f4e4db (10.98:1); numbers are the **highest-luminance data after the title**—the eye lands on the figure before any label.

**Numbers stay neutral warm ink, never brand color.** Money is fact; fact gets text ink. Brand color is emphasis/opinion; brand-tinted numbers import the light theme's 3.28:1 problem and create false hierarchy (most-colored reads as most-important regardless of truth). Emphasis in rows comes from size and tabular weight; #8fd5d6 and #d59172 stay on states, actions, accents.

---

## 8. Realistic Arabic content pack (canonical corpus for the seeds)

Shop: **مؤسسة الحوراني للأدوات الصحية** (sanitary-ware, Amman). Day: **الاثنين 07/09/2026**. Opening (end of Sunday 06/09): النقد المتاح **3,180.00**·لك **2,380.00**·عليك **7,150.00**.

**Parties (end-of-day balances):**

| Party | Role | Balance | Aging / state |
|---|---|---|---|
| محمد الخطيب (مقاول تركيبات صحية) | customer | 940.00 لك | متأخر—مستحق منذ 21/07/2026 (47 يومًا) |
| ورشة الأمان (ورشة صيانة) | customer | 540.00 لك | 260.00 بيع اليوم + 280.00 منذ 25/08 |
| أبو زياد للمقاولات | customer | 760.00 لك | مستحق منذ 27/08/2026؛ تعارض بالأمس |
| مقهى الياسمين (مشروع تجديد) | customer | 0.00 لك | محصّل بالكامل—سدّد الأحد 06/09 (true zero) |
| شركة الرشيد للتوزيع (مواد صحية بالجملة) | supplier | 2,350.00 عليك | استحقاق 15/09/2026 |
| مصنع البتراء للسيراميك والبلاط—فرع السخنة | supplier | 4,300.00 عليك | استحقاق 30/09/2026؛ طلب اليوم غير محدد القيمة |

**Monday's events (chronological):**

| # | Time | Event | Party | Amount | State |
|---|---|---|---|---|---|
| 1 | 08:15 | بيع نقدي—خلاطات ومستلزمات | عميل تجزئة | 425.00 د.أ نقدًا | متزامن |
| 2 | 09:20 | دفعة سداد للمورد | شركة الرشيد للتوزيع | 500.00 د.أ نقدًا | متزامن |
| 3 | 10:05 | تحصيل | محمد الخطيب | 300.00 د.أ نقدًا | محصّل |
| 4 | 11:10 | بيع بالذمة—أنابيب ووصلات | ورشة الأمان | 260.00 د.أ على الحساب | معلّق |
| 5 | 12:30 | طلب شراء—بلاط 60×60، 40 صندوقًا | مصنع البتراء—فرع السخنة | القيمة غير محددة بعد (خصم الكمية قيد الاتفاق) | غير محدد |
| 6 | 13:40 | مصروف—وقود سيارة التوصيل |—| 15.00 د.أ | متزامن |
| 7 | 14:20 | توصيل مجدول لمشروع أبو زياد—الأربعاء 09/09/2026 | أبو زياد للمقاولات |—| معلّق (operational) |
| 8 | 15:50 | تحصيل | ورشة الأمان | 100.00 د.أ نقدًا | **بانتظار المزامنة** (سُجّل بدون إنترنت) |
| 9 | 16:20 | مصروف—وجبة عمال |—| 12.50 د.أ | **تقديري** (من الذاكرة، لا إيصال) |
| 10 | 17:05 | تعارض في سجل أمس: تحصيل من أبو زياد بنسختين—150.00 (هذا الجهاز) مقابل 180.00 (جهاز آخر) | أبو زياد للمقاولات | فرق 30.00 د.أ غير محسوب حتى المراجعة | **تعارض** |

**End of day:** النقد المتاح **3,477.50** (قبضت 825.00، صرفت 527.50—أعلى بـ 297.50 عن أمس)·لك **2,240.00** (أخفض بـ 140.00)·عليك **6,650.00** (أخفض بـ 500.00)·الصافي: عليك أكثر من النقد ولك بفارق 932.50 د.أ. Aging: 0–30 يوم 1,300.00·31–60 يوم 940.00 (محمد الخطيب).

---

## 9. Per-seed RTL fitness verdicts + binding recommendations

**Seed A «الخلاصة اليومية»—HIGH fit.** The most Arabic-native composition: spoken-business culture reads «قبضت… وصرفت…» before any chart, and position block → narrative → timeline mirrors reading order. The large-title collapsing bar mirrors cleanly; IBM Plex Sans Arabic suits it—verify `tnum`, lock off contextual Arabic-Indic digit swap. Risks: timeline keeps newest at top with isolated LTR time islands; narrative obeys the money-atom contract mid-sentence.

**Seed B «الدفتر»—HIGH fit, best bidi discipline.** The sticky truth-bar (cash/لك/عليك as tappable figures) is the position triad as one semantic group; hairline rows + **fixed money column** enforce the tabular/decimal contract—the register is its natural home. Risks: دفتر informs hierarchy, never a skeuomorphic paper page (rejected lesson); FAB stays bottom-center (never mirrors).

**Seed C «الصندوق»—MEDIUM-HIGH fit.** Position-first hero + split counters is honest and glanceable; sheet-first is the most one-handed-native (thumb reach). Risks: the لك/عليك split must not read as spatial good/bad—لك at inline-start (primary), عليك secondary, same weight class; the geometric Arabic typeface is title-only (geometric faces lose body-size legibility, often lack tabular ASCII digits); day-strip pages leftward for later days.

**Binding recommendations:**

- **AR-01**—Money atom = isolated LTR digit run (sign, digits, separators inside) + «د.أ» in the RTL flow; one nowrap unit; unit-inside-isolate forbidden.
- **AR-02**—Fixed money column: constant width for the max tabular value, inline-end aligned, two decimals, own unit sub-column; money never truncates; missing = «—» at number size.
- **AR-03**—Signs inside isolates, U+2212 for minus; accounting parentheses around money forbidden.
- **AR-04**—Dates DD/MM/YYYY in isolates; long dates pure Arabic with ASCII digits; ranges = «إلى» between two isolates.
- **AR-05**—Mirror per §1; never mirror digit runs, physical keyboard, logo, neutral icons, bottom-center capture.
- **AR-06**—Every state = glyph shape + Arabic word (§3 table); color never carries state alone.
- **AR-07**—Contrast roles per §5; carried pairs binding, neutral extensions need central confirmation.
- **AR-08**—Touch floors: 44/48px targets, 56–64px single-target rows, 8px gaps.
- **AR-09**—Money mutations: one polite closure sentence with the final position; conflicts assertive once.
- **AR-10**—Input: `inputmode="decimal"`; normalize Arabic-Indic digits + U+066B/U+066C to ASCII; search rule per §6.
- **AR-11**—Dark theme: #332d27 canvas + #3a332c elevation; numbers in neutral ink #f4e4db, never brand-colored.
- **AR-12**—The §8 corpus is the canonical test content for all seeds; 320px long-name tests use «مصنع البتراء للسيراميك والبلاط—فرع السخنة».

*End of report—Task 3-d.*
