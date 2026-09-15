# 04 — Arabic-RTL Financial Mobile Specialist Report

**Delivery:** `micro-native-mobile-direction-002` · Stage 1 (specialist research) · 2026-09-07
**Author:** Specialist 4 — Arabic RTL Financial Mobile
**Nature:** Research/analysis only. No prototypes, no direction selection — the orchestrator decides (per `en/01` §6).
**Inputs read in full:** `en/00-previous-work-lessons.md` (K/A/R/V buckets), `en/01-intake-and-previous-work-audit.md` (constraint register C-01…C-08).
**Doctrine inherited:** K-01 contrast, K-03 honest states, K-04 glyph+label, K-05 bidi contract, K-06 ASCII digits + tabular-nums, K-07 Arabic legibility floors. All contrast figures in §8 are **computed this run** (WCAG 2.x relative-luminance formula); anything not re-measured here stays labeled inherited per V-07.

---

## 0. Executive summary

1. The owner's rejection ("translated LTR web screens") is primarily a **direction + anatomy failure**. This report fixes the direction layer: mirroring rules (§1), Arabic typography (§2), bidi-safe money (§3), truth surfaces (§4), RTL charts (§5), a reconciling Arabic demo corpus (§6), 320px stress arithmetic (§7), warm dark (§8), and an RTL a11y contract (§9).
2. Headline recommendations: **mirror navigation, never numbers**; one display convention **3-decimal JOD everywhere**; truth strip = «صندوق / لي / عليّ» with confirmed-only main figures and visible pending deltas; charts: **earliest-at-right by default with labeled axes** (V-01 test attached); only 2 charts earn their place — the third slot is a structured list.
3. The corpus in §6 reconciles exactly (صندوق 431.100 مؤكد · لي 664.250 · عليّ 348.500) and contains all required honest states; it is ready to seed all three Stage-2 prototypes.

---

## 1. RTL mirroring rules

Principle: **mirror *direction of travel and reading*, never *data*.** UI chrome is spatial (mirrors); content strings are logical (never mirror). The isolate (`<bdi dir="ltr">`) is the fence between the two worlds (K-05).

### 1.1 What MIRRORS

| Element | LTR behavior | Required RTL behavior |
|---|---|---|
| Back arrow | points left, top-left | points **right →**, sits top-right |
| Push transition | new screen slides in from right | slides in from **left** |
| Pop transition | previous revealed from left | previous revealed from **right** |
| Swipe-back edge | left edge | **right edge** (fixed by task) |
| "Into detail" chevron on rows | points right › | points **left ‹** |
| Progress / stepper | fills left→right, step 1 leftmost | fills **right→left**, step 1 rightmost |
| Horizontal timeline / range slider | earliest/minimum at left | **earliest/minimum at right** |
| Pager / carousel | next page to the right | **next page to the left**; dots order right→left |
| Segmented control | first segment left | first segment **right** |
| Icon + label pairs | icon left of label | icon **right** of label |
| Row action reveal (destructive swipe) | swipe left reveals left-side actions | mirrored — **but conflicts with right-edge swipe-back; recommend long-press/menu instead** (device test V-04) |
| List scroll anchors, FAB position | bottom-right | bottom-**left** (or center — keep consistent) |
| In/out money arrows | avoid ←/→ (they mirror); use ↑ (داخل) / ↓ (خارج) — direction-neutral | same |

### 1.2 What NEVER mirrors

| Content | Rule |
|---|---|
| Digits, money strings | `<bdi dir="ltr">431.100</bdi>` — internal order frozen; minus **inside** the isolate |
| Dates | `07/09/2026` isolated as a unit; never reorder to `2026/09/07` in display |
| Phone numbers | `+962 7 9123 4567` isolated LTR always |
| Latin brand names, emails, URLs, reference IDs | isolated; never reshaped |
| Clock icons, spinning refresh, play/pause/skip, checkmark ✓ | rotation/semantic icons are not mirrored |
| Math signs and ranges | `+`, `-`, `1–3` all inside isolates |
| Logical data order in code (ISO dates, array order) | storage/logic stays LTR; only presentation flips |

### 1.3 Reviewer mirror checklist (run on every screen, light+dark, 320 first)

1. Back affordance: arrow points **right**, sits **top-right** → PASS.
2. Push detail: incoming screen enters from **left**; pop returns revealing previous from **right**.
3. Swipe from **right edge** dismisses/pops (and does not fight any row-action swipe).
4. Row chevrons point **left** toward the detail.
5. Progress bars/steps fill and read **right→left**; step «1» is rightmost.
6. Pager: next content lies **left**; dots read right→left; page indicator matches.
7. Every money string renders as «NUMBER د.أ» with the unit **visually left of the number**, never «د.أ NUMBER» (the K-05 bug).
8. Negative renders `-40.000` (minus attached), never `40.000-`.
9. Dates read `07/09/2026`, not `2026/09/07` or `09/07/2026`.
10. Phone/Latin strings unbroken and unordered.
11. First focusable element in focus order = the element first in **reading order** (top-right region), not top-left.
12. Horizontal timeline/chart: earliest day on the **right** (or explicitly labeled alternative, §5).
13. Icon sits to the **right** of its label in buttons and chips.
14. English LTR verification pass: flip direction to LTR with English strings — nothing structural breaks, no mirrored leftovers (e.g., stray ‹ chevrons).

---

## 2. Arabic UI typography for mobile

### 2.1 Metric floors (K-07, restated as build rules)

| Style | Size | Line-height | Notes |
|---|---|---|---|
| Display figure (صندوق) | 30–34px | 1.15–1.2 (digits) / unit 1.4 | digits only in the big line; Arabic gloss on its own line at 15px |
| Question header (A-06) | 21–24px | 1.35–1.45 minimum | Arabic ascenders/dots need room; never 1.1 |
| Section title | 17px | 1.5 | |
| Body / row primary | **15px** | **1.6 (24px)** | floor is 1.6; 1.7 for two-line descriptions |
| Meta / timestamp | 13px | 1.6–1.7 (≥21px) | absolute floor: **nothing below 13px anywhere** |
| State chip | 13px | 1.6 | glyph + word, full word never abbreviated |

- **Letter-spacing: 0 on Arabic, always.** Letter-spacing breaks glyph joining; do not inherit tracking tokens from Latin styles. Word-spacing is never compressed or stretched — if a line overflows, refactor the copy.
- **Diacritics:** UI copy ships without tashkeel by default; internal shadda/hamza as in «عليّ» must render correctly — line-height floors exist partly for this. Never clip descenders/marks with tight `overflow:hidden`; never justify Arabic UI text (kashida stretching is a print habit, wrong on screens).
- **Truncation:** ellipsis lands at the **visual left** (logical end) — default RTL `text-overflow: ellipsis` behavior. Entity names are start-anchored, end-ellipsified («كافتيريا مدرسة النه…»); middle-ellipsis («كافتيريا … النهضة») reserved for reference numbers only. Amounts, state words, and dates **never truncate** (§7).

### 2.2 Font stack recommendation

```css
--font-ui: -apple-system, "SF Arabic", "Segoe UI", "Noto Sans Arabic",
           "IBM Plex Sans Arabic", sans-serif;
.money { font-variant-numeric: tabular-nums; font-feature-settings: "tnum" 1; }
/* letter-spacing: never applied to Arabic text styles */
```

System-first keeps native rendering (SF Arabic on iOS, Segoe UI Arabic coverage on Windows, Noto Sans Arabic on Android). Two faces maximum in the product; digits must come from the same face as body text unless a measured pairing is proven (V-05).

### 2.3 Honest evaluation of 3 optional faces

| Face | Strengths for Micro | Risks | Verdict |
|---|---|---|---|
| **IBM Plex Sans Arabic** | Designed for UI; humanist-naskh structure keeps letters distinct at 13–15px; wide weights; excellent hinting on low-DPI | Latin digits are proportional by default — must force `tnum`; adds ~bundle weight to a web prototype | **Best optional brand face** for body+headings if the owner wants a distinct voice |
| **Noto Sans Arabic** | Neutral, ships on Android; huge weight axis; safest cross-device consistency; zero-cost fallback | Generic personality (weak differentiation); tabular figures need feature check | **Default/fallback face** — the safe backbone |
| **Cairo** (Kufi-flavored geometric) | Strong display presence; popular and familiar | Tight counters below ~16px; tall vertical rhythm inflates 56px rows; joining clarity degrades at small sizes | **Display-only** (wordmark, ≥22–24px question headers). Never body, never rows, never amounts |

**Kufi rule:** Kufi-flavored faces are appropriate only at large sizes where letterforms are roomy (question headers, the «سجّل» moment) and risky below ~18px; they are **forbidden for digits, money, and dense rows**. Decorative calligraphy remains rejected (C-07 spirit).

---

## 3. Numbers & money in Arabic UI

### 3.1 Decimal convention — recommendation: **3-decimal (fils) everywhere**

| Option | Assessment |
|---|---|
| **3 decimals always (e.g., 431.100 د.أ) — RECOMMENDED** | Matches JOD's native fils convention and Jordanian paper invoices/bank SMS the owner already reads (K-13 receipts = display = input, K-06). Credit ledgers accumulate fils; truncating to 2 creates the classic «من وين الجميل؟» dispute — the exact trust problem Micro exists to kill. Fixed 3 decimals + tabular digits = every amount the same width → decimal alignment is automatic, and 320px arithmetic is predictable (§7). |
| 2 decimals | Saves 1 character per amount, but mixes conventions the moment a fils-bearing entry appears (e.g., 2.500 fils rounding), forces rounding policy debates, and breaks column alignment rhythm. |

One convention, one rounding rule (carry fils honestly in the ledger; never round for display only). If the owner tests 2-decimal and insists, that is a one-token change — but the default recommendation is 3.

### 3.2 Formatting rules

- ASCII digits only (C-05); Arabic-Indic digits ٠١٢ are **not** used in v1, including inside dates.
- `tabular-nums` on every numeric string; amounts in dense lists carry the unit **once in the column header («د.أ»)** to keep rows clean; full «N.NNN د.أ» form is used in truth surfaces (§3.4).
- Grouping: comma thousands separator (`1,850.000`) — the convention Jordanians read with Latin-digit statements.
- **Negatives:** minus sign **inside the isolate**: `<bdi dir="ltr">-40.000</bdi>` — outside, bidi renders the bug «40.000-».
- Canonical markup: `<bdi dir="ltr">431.100</bdi> د.أ` → renders «‏431.100 د.أ» with the unit to the visual **left** of the number, in RTL flow (K-05).
- Parentheses for negatives are forbidden (K-05): they flip visually in RTL and read as accounting jargon to this audience.

### 3.3 In/out conventions without color (K-04)

| Meaning | Glyph | Word | Sign (inside isolate) | Example row |
|---|---|---|---|---|
| Cash in | ↑ | داخل / قبض | `+` | ↑ قبض نقدي `<bdi>+24.500</bdi>` |
| Cash out | ↓ | خارج / دفع | `-` | ↓ دفعة لمورد `<bdi>-40.000</bdi>` |

Sign + glyph + word always travel together; color (teal/terracotta) may reinforce but never carries meaning alone (§9 checklist). Up/down arrows are chosen deliberately: left/right arrows mirror under RTL and would re-introduce the ambiguity we just removed.

### 3.4 Compact vs full money rendering

| Form | Pattern | Mandatory on | Allowed on |
|---|---|---|---|
| **Full** | «431.100 د.أ» with unit + state + timestamp context | Truth strip (§4), account detail headers, receipts/confirmation sheets, effect previews (K-09), exports | — |
| **Compact** | `<bdi>+24.500</bdi>` bare, unit in column header | — | Event rows (verb column present), chips/deltas, chart data labels |

Rule: compact is allowed **only** when the row/surface names the direction (verb or glyph) and the unit appears once in the enclosing surface. If any doubt → full form.

---

## 4. Financial truth surfaces

### 4.1 Truth strip content contract (one instance, persistent header region per A-02 — structural, never a floating card)

| Figure | Label (Arabic) | Gloss line (15px, one sentence) | Value form | State behavior | Tap-through |
|---|---|---|---|---|---|
| 1 | **صندوق** | «اللي في الصندوق الآن — مؤكد» | `<bdi dir="ltr">431.100</bdi> د.أ` | Main figure counts **مؤكد only**. Secondary chip when needed: «<bdi>+27.750</bdi> بانتظار المزامنة». Conflict amounts are held out and surfaced as an alert chip, never folded in. | Cash ledger (days + states) |
| 2 | **لي** | «الزباين يدينولي» | `<bdi dir="ltr">664.250</bdi> د.أ` | Sum of party balances in state «مؤكد»; conflicted payments excluded with a visible chip; unknown-name effects noted, never silently zeroed | Receivables list with aging |
| 3 | **عليّ** | «أنا مدين للموردين» | `<bdi dir="ltr">348.500</bdi> د.أ` | Same grammar as لي | Obligations list |

Each figure carries: **state chip + timestamp** («آخر تحديث اليوم 08:52» / «متزامن حتى 07/09 08:52»). Unknown is never a confident `0.00` — it renders «قيمة غير محددة بعد» with the action «سجّله» (K-03). One truth strip per screen; detail lives in pushes, not in a taller home screen (A-04).

### 4.2 Per-party account line contract

Fields in order: **name (truncate-ellipsis) · aging tag · amount (isolated, compact) · last activity (date + verb)**. Two-line row grammar (§7); example at 320px:

> كافتيريا مدرسة النهضة …  ‹
> أقدم مبلغ 26 يوم · آخر حركة 03/09 بيع آجل · `<bdi>335.000</bdi>`

Aging buckets (Arabic labels): «0–7 يوم · 8–30 يوم · 31–60 يوم · أكثر من 60» (numeric ranges isolated). A party with no balance shows «حساب مسدّد» — never «0.00» floating alone; a party never touched shows «لا يوجد سجل بعد».

### 4.3 Honest-state vocabulary (glyph + label; color strictly tertiary)

| الحالة | When it is used | Glyph + label pairing | Color (tertiary) |
|---|---|---|---|
| **مؤكد** | Recorded, settled, counted in truth figures | ✓ «مؤكد» | ink (default) |
| **معلّق** | Awaiting an owner action/decision (promised payment not yet received; entry awaiting confirmation) | ◌ «معلّق» | neutral gray |
| **تقديري** | Value estimated, not yet actual (electricity before meter reading) | ≈ «تقديري» | neutral gray |
| **غير محدد بعد** | Value/name unknown — never rendered as 0.00; paired with action «سجّله» | ؟ «قيمة غير محددة بعد» | neutral gray |
| **بانتظار المزامنة** | Recorded locally, device offline, will sync | ⟳ «بانتظار المزامنة» | neutral gray |
| **متزامن** | Confirmed and synced to backup | ☁✓ «متزامن» | teal accent |
| **تعارض** | Two versions of the same event exist; needs owner decision (K-09 preview) | ⚠ «تعارض — بحاجة لقرار» | terracotta `#964e33` text (measured 6.11 w/ white contexts; on light bg use as text ink) |
| **ملغي** | Cancelled duplicate/wrong entry; kept visible for audit; excluded from all totals | ✕ «ملغي» | muted gray + strikethrough-free (label carries it) |
| **عكسي** | Reversed by a paired opposite entry; both remain visible | ↩ «عكسي» | neutral gray |
| **تسوية** | Correction/settlement entry adjusting an earlier record (estimate → actual), always with before/after preview | ⧉ «تسوية» | ink + teal edge |

«تصحيح» (correction, C-04/K-03) is implemented as **تسوية** entries and عكسي pairings — one mechanism, two visible moments. Alerts («تعارض») use `role="alert"` and are never quiet chips (K-04).

---

## 5. Charts for Arabic financial questions

Only charts that answer a real owner question earn their place (K-10). Recommendation: **2 charts + 1 structured list.**

### 5.1 Chart 1 — Cash in/out, 14 days («شو دخل وطلع من الصندوق؟»)

- Grouped vertical bars per day: in ↑ / out ↓, Arabic weekday + date labels («الاثنين 07/09»).
- **RTL time-flow recommendation: earliest day at the RIGHT** (reading order), axis explicitly labeled with first/last day so order is never assumed. This is the default to build; V-01 requires a 5-owner test.
- **Honest alternative (if V-01 fails):** keep LTR left→right time axis but add an arrow annotation «البداية ← النهاية»… no — the honest alternative is: keep earliest-at-**left** with a prominent «يوم البداية / يوم النهاية» label pair at both ends; the labels, not the direction, carry the meaning. Decide by test, not taste.
- Gap handling: days before detailed records exist (25/08–31/08 in §6) render as a **hatched gap + footnote** «فترة قبل بدء السجل التفصيلي — غير مسجلة (ليست صفرًا)» (K-10).
- Pending day (07/09) is hatched/overlaid with ⟳ «بانتظار المزامنة».
- Source-state caption (mandatory): «المصدر: سجل الصندوق · متزامن حتى 07/09 08:52».
- **Non-visual contract:** a text interpretation sentence IS the accessible alternative, e.g., «خلال آخر 7 أيام: دخل مؤكد 185.750 د.أ، وطلع 167.000 د.أ. الأسبوع قبل 01/09 غير مسجل بالتفصيل.»

### 5.2 Chart 2 — Receivables aging («مينأ أطول حساب ما انسدّد؟»)

- 4 horizontal bars (0–7 / 8–30 / 31–60 / +60 يوم) growing **leftward from a right-side baseline**; bucket labels on the right; sums isolated «47.650».
- A bucket with no receivables shows «لا يوجد» — a **counted zero** is allowed only when it is known-zero, distinct from unrecorded.
- Caption + text interpretation as in 5.1.

### 5.3 Slot 3 — not a chart

«أكبر 3 حسابات ليّ» as a structured list (name + aging + amount) — answers the same question as a donut without the RTL/label failure modes of pie charts on 320px. Donuts/gauges are rejected for v1.

---

## 6. Realistic content corpus (reconciled — seeds all three prototypes)

Business frame: neighborhood grocery/mini-market (بقالة) in Amman; owner sells retail (cash + آجل) and supplies nearby kitchens/cafeterias. Window: **01/09/2026 (الثلاثاء) → 07/09/2026 (الاثنين)**. Opening balances end of 31/08: صندوق **412.350** · لي **589.100** · عليّ **299.750**. Prior week (25/08–31/08) is deliberately *not* itemized → the chart-gap case (§5.1). All amounts JOD, 3 decimals, DD/MM/YYYY.

### 6.1 Customers (لي — they owe the owner)

| # | الجهة | Opening balance | Last activity | Oldest unpaid from | Aging bucket (at 07/09) |
|---|---|---|---|---|---|
| 1 | أم أحمد (الجوار) | 12.500 | 02/09 دفعة + بيع آجل | 02/09 | 0–7 يوم |
| 2 | أبو محمد | 47.750 | 05/09 دفعة | 20/08 | 8–30 يوم |
| 3 | مطعم الشام | 186.000 | 06/09 دفعة | 18/08 | 8–30 يوم |
| 4 | ورشة أبو يوسف | 0.000 «حساب مسدّد» | 04/09 بيع آجل | 04/09 | 0–7 يوم |
| 5 | مطبخ أم خالد (طعام مناسبات) | 63.200 | 21/08 دفعة 15.000 | 02/08 | 31–60 يوم |
| 6 | كافتيريا مدرسة النهضة | 240.000 | 03/09 بيع آجل | 12/08 | 8–30 يوم |
| 7 | كافيه سما | 31.400 | 06/09 دفعة (تعارض) | 24/08 | 8–30 يوم |
| 8 | أم غيث | 8.250 | 29/08 بيع آجل | 29/08 | 8–30 يوم |

### 6.2 Suppliers (عليّ — the owner owes them)

| # | الجهة | Opening balance | Last activity | State at 07/09 |
|---|---|---|---|---|
| 1 | مخازن الحسن (خضار وفواكه) | 145.500 | 06/09 بضاعة آجل | 290.500 مستحق |
| 2 | شركة المراعي (ألبان) | 96.250 | 03/09 تسوية كاملة | 0.000 «حساب مسدّد» |
| 3 | توزيعات أبو سليم (مواد بقالة) | 58.000 | 24/08 شراء نقدي | 58.000 مستحق |
| 4 | معمل الياسمين للبلاستيك (أكياس) | 0.000 | 19/08 سداد كامل | 0.000 «حساب مسدّد» |

### 6.3 Day events (20 rows, 7 event-days; required special states included)

| # | التاريخ | اليوم | النوع | الجهة | نقد داخل | نقد خارج | أثر الحساب | الحالة |
|---|---|---|---|---|---|---|---|---|
| 1 | 01/09 | الثلاثاء | بيع نقدي | — | 24.500 | — | — | مؤكد |
| 2 | 01/09 | الثلاثاء | بيع آجل | مطعم الشام | — | — | لي +50.000 | مؤكد |
| 3 | 01/09 | الثلاثاء | دفعة لمورد | مخازن الحسن | — | 40.000 | عليّ −40.000 | مؤكد |
| 4 | 01/09 | الثلاثاء | كهرباء (فاتورة غشت قبل القراءة) | مؤسسة الكهرباء | — | 18.000 | — | **تقديري** |
| 5 | 02/09 | الأربعاء | بيع نقدي (زبون عابر) | **اسم غير محدد بعد** | 15.250 | — | — | مؤكد + «؟ قيمة الاسم» |
| 6 | 02/09 | الأربعاء | استلام دفعة | أم أحمد | 10.000 | — | لي −10.000 | مؤكد |
| 7 | 02/09 | الأربعاء | بيع آجل | أم أحمد | — | — | لي +6.750 | مؤكد |
| 8 | 03/09 | الخميس | بيع آجل | كافتيريا مدرسة النهضة | — | — | لي +95.000 | مؤكد |
| 9 | 03/09 | الخميس | دفعة لمورد (تسوية كاملة) | شركة المراعي | — | 96.250 | عليّ −96.250 | مؤكد |
| 10 | 04/09 | الجمعة | مصاريف أجرة مندوب | — | — | 5.000 | — | مؤكد |
| 11 | 04/09 | الجمعة | بيع آجل | ورشة أبو يوسف | — | — | لي +38.400 | مؤكد |
| 12 | 04/09 | الجمعة | نفس البيع — تكرار تسجيل | ورشة أبو يوسف | — | — | — | **ملغي** (لا يُحتسب) |
| 13 | 05/09 | السبت | بيع نقدي | — | 31.000 | — | — | مؤكد |
| 14 | 05/09 | السبت | استلام دفعة | أبو محمد | 25.000 | — | لي −25.000 | مؤكد |
| 15 | 05/09 | السبت | تسوية فاتورة كهرباء غشت: الفعلي 21.300 مقابل التقديري 18.000 | مؤسسة الكهرباء | — | 3.300 | — | **تسوية** (معاينة قبل/بعد) |
| 16 | 06/09 | الأحد | بضاعة آجل | مخازن الحسن | — | — | عليّ +185.000 | مؤكد |
| 17 | 06/09 | الأحد | استلام دفعة | مطعم الشام | 80.000 | — | لي −80.000 | مؤكد |
| 18 | 06/09 | الأحد | دفعة من كافيه سما — نسختان: 20.000 (مسجل محليًا 18:40) مقابل 12.000 (سجل الشريك) | كافيه سما | — | — | معلّق حتى الحسم | **تعارض** ⚠ (لا يُحتسب) |
| 19 | 07/09 | الاثنين | بيع نقدي (صُبّح بدون إنترنت) | — | 27.750 | — | — | **بانتظار المزامنة** ⟳ |
| 20 | 07/09 | الاثنين | بنزين مولدة (قطع كهرباء) | — | — | 4.500 | — | مؤكد |

### 6.4 Reconciliation (must survive unchanged in every prototype)

| Figure | Arithmetic (confirmed only) | Closing 07/09 |
|---|---|---|
| صندوق | 412.350 + in 185.750 (24.5+15.25+10+31+25+80) − out 167.000 (40+18+96.25+5+3.3+4.5) | **431.100** |
| صندوق بعد المزامنة | 431.100 + 27.750 (قيد المزامنة) | 458.850 |
| لي | 589.100 +50 +6.75 +95 +38.4 −10 −25 −80 | **664.250** (parties sum ✓) |
| عليّ | 299.750 −40 −96.25 +185 | **348.500** (suppliers sum ✓) |
| تعارض بعد الحسم | قبول 20.000 → صندوق 458.850+20.000 = 478.850، لي 644.250 · قبول 12.000 → 470.850، لي 652.250 | variants shown in resolution sheet |

Aging totals: 0–7 = 47.650 · 8–30 = 553.400 · 31–60 = 63.200 · +60 = لا يوجد → **664.250 ✓**. The cancelled duplicate (#12) and the conflicted payment (#18) are visible rows excluded from every total — this is how «ملغي» and «تعارض» must behave in all three prototypes.

---

## 7. Text expansion & layout stress (320px first — A-08)

- Expansion budget between Arabic and English UI strings: **±30%**; verify both directions (C-05 English LTR pass). In this domain Arabic is often *shorter* («دفعة لمورد» vs "Supplier payment").
- 320px arithmetic: 320 − 32 (edge margins) = 288 content; − 24 (row padding) = **264px usable**.
- Worst name: «كافتيريا مدرسة النهضة» (22 chars ≈ 165px @15px) + worst amount «335.000» (≈63px tabular @15px) + 8px gap = **236px ✓ one line**. Adding the unit «د.أ» (+≈26px) hits 262px — exactly at the limit → **dense rows use the column-header unit** (§3.4); the full «…د.أ» form lives on truth surfaces.
- Adding the state chip «بانتظار المزامنة» (≈95px @13px) on the same line overflows → **two-line row grammar is mandatory**: line 1 = name + amount; line 2 = date · state · verb (meta 13px).
- Wraps vs truncates: **wrap** (max 2 lines): event descriptions, gloss sentences. **Truncate** (1 line, end-ellipsis): party names, addresses. **Never truncate or shrink:** amounts, dates, state words, timestamps (they move to the next line instead).
- Verify at 360/390/430 after the 320 pass; confirm no widow words inside truth strip labels at 430.

---

## 8. Dark mode for Arabic (warm, deliberate — K-02)

No pure black backgrounds, no pure-white body text; surfaces stay warm. Pairs below computed this run (WCAG formula; re-verify at build per V-07).

| Pair (text on surface) | Ratio | Verdict |
|---|---|---|
| `#ece4dc` body on `#1c1815` base | 14.0:1 | ✓ body |
| `#8fd5d6` on `#332d27` surface | 8.18:1 | ✓ accents/synced state |
| `#d59172` on `#332d27` | 5.26:1 | ✓ action text/fills |
| `#d59172` on `#1c1815` | 6.83:1 | ✓ primary action on base |
| `#b8a99c` meta on `#1c1815` / `#332d27` | 7.72 / 5.94 | ✓ secondary text |
| `#cc785c` on `#332d27` | 4.14:1 | graphics/large only — **never body text** (press fill per C-03) |
| `#ffffff` on `#964e33` (light-mode action) | 6.11:1 | inherited K-01 |

Prohibition: large low-contrast gray blocks — secondary/meta text must stay ≥4.5:1 (target ≥7 for 15px body), and no state may be conveyed by grayness alone (glyph+label still required, §4.3). Money strings in dark mode keep the same isolate grammar; test tabular-nums rendering of `#d59172` digits for stroke thinning at 15px.

---

## 9. Accessibility (RTL-specific)

- **Focus order:** DOM order = logical reading order (top-right first); never manual `tabindex` sequences built LTR. First focus lands on the screen title; truth strip figures are one focus stop each with full spoken value.
- **Touch targets (K-12 audit):** nav destinations 48px; primary bottom actions 48–56px inside the bottom thumb zone; list rows ≥56px; chips ≥44px hit area (visual may be smaller); ≥8px separation; right-edge swipe-back must not conflict with row actions (prefer long-press menus — verify on device, V-04).
- **Dynamic-type break order (what fails first):** 1) state chips wrap to their own line (acceptable); 2) row meta wraps to a third line (acceptable to ~200%); 3) truth strip figures reflow 3-up → 1-per-line stacking (never shrink below 13px, never ellipsize money); at no scale may amounts, dates, or state words truncate.
- **Screen reader (V-02 open):** untested how TalkBack/VoiceOver pronounce «د.أ» (risk: misread as «دولار») and digit strings in Arabic. Interim contract: `aria-label` expands money as «أربعمئة وواحد وثلاثين دينارًا وواحد مئة فلس» and dates as «السابع من أيلول 2026»; the أيلول/سبتمبر month-name choice is an owner copy decision — flag at Stage 3. Real-device SR test mandatory before Stage 4.
- **Never-color-alone verification list:** 1) every state has glyph+word (§4.3); 2) in/out = ↑/↓ + verb + sign; 3) conflict uses ⚠ + label + `role="alert"`; 4) pending-sync uses ⟳ + label, not gray alone; 5) estimated uses ≈ + word; 6) unknown offers «سجّله» action, not blank; 7) chart bars carry text values; 8) dark-mode states keep glyphs (not just hue shifts); 9) focus ring visible on warm dark (≥3:1 against adjacent); 10) cancelled rows readable (no low-contrast-only strikethrough).

---

## 10. Open questions handed to the orchestrator

| # | Question | Tied to |
|---|---|---|
| 1 | RTL chart time-flow: build earliest-right as default, test with 5 owners, alternative pre-specified (§5.1) | V-01 |
| 2 | Screen-reader pronunciation of «د.أ» + digit strings; interim expanded labels defined (§9) | V-02 |
| 3 | Font decision: system stack + Noto Sans Arabic backbone, IBM Plex Sans Arabic as optional voice, Cairo display-only — confirm at the typography gate | V-05 |
| 4 | 3-decimal fils convention recommended (§3.1) — confirm with owner alongside 2-decimal alternative | C-05 |
| 5 | Row-action reveal vs right-edge swipe-back conflict — resolve with long-press pattern after device test | V-04 |
| 6 | Haptics policy still deferred | V-03 |

**Handoff:** §6 corpus is self-consistent and may seed prototypes A/B/C verbatim; §4.3 vocabulary and §1.3 checklist are proposed as delivery-wide acceptance criteria for the synthesis to adopt or override.
