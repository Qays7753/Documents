# UX Architecture Report — Micro Arabic-First Component Library

- **Run:** 20260908T133347Z-352b · **Task:** 2-a · **Agent:** 01 — UX Architecture
- **Scope of this document:** UX foundations, information hierarchy, native phone patterns, state
  truth, Arabic copy guidelines, navigation proposal. This is research + writing only — everything
  here is *documented for implementation*, nothing is *implemented*. Engineering (tokens, CSS,
  HTML) belongs to Agent 03; visual identity (color/type assignments) to Agent 02; accessibility
  review to Agent 04.
- **Product frame:** phone-only, portrait-first, validated at 320 / 360 / 390 / 430 px widths.
  Arabic-first RTL. Light mode only. Jordanian small-business finance + operations ("Micro").
  Demo corpus: business "بقالة النور" (owner "أبو النور"), customer "خالد الحوراني", supplier
  "مستودع زهران".

**Verified font facts used in this document** (measured from the shipped woff2 subsets in
`final/fonts/` with fontTools — these are facts about the font files, not layout measurements):

- The fonts are split subsets: Arabic glyphs live in the `*-arabic.woff2` files; Western digits,
  `U+2212 MINUS SIGN`, `%`, `,`, `.`, `…`, `—` live in the `*-latin.woff2` files. Any test page
  must load both subsets, or money values will fall back to a system font.
- `U+2212` (true minus) is present in all three latin subsets (400/500/600) → safe to use as the
  primary financial-direction sign.
- The Arabic subsets **do** contain Arabic-Indic digits (U+0660–0669), so a careless
  implementation *can* render them. The system must never emit Arabic-Indic digits; this is a
  review checkpoint for Agent 04.
- Label width estimates below use the isolated-glyph advance sum (an **upper bound**; shaped
  connected text runs ~15–25 % narrower). Agent 03 must re-verify with a real shaping pass.

---

## 1. User model

The Micro user is أبو النور: he runs the till, the shelf, and the phone at the same time. He is
standing, often mid-transaction, frequently in sunlight at the shop door. He is **not
finance-trained**, is impatient with interfaces, and has zero tolerance for anything that slows
the next customer. His scanning behavior is a mirrored F-pattern: first fixation lands at the
**top-right** of the screen (RTL start), sweeps one line right→left, then walks down the right
edge looking for a **familiar name** (خالد الحوراني، مستودع زهران) before he trusts any number
next to it. Numbers are scanned by magnitude and sign, not read digit-by-digit: "−86.250" must
communicate *expense, eighty-something* in under a second. Every composition must survive a
**1.5-second glance test** answering four questions: what is this number (label), how big and
which direction (value + sign), is it current and trustworthy (state), and what can I do next
(one visible action).

One-hand use is the norm, right thumb dominant, left hand holding cash or boxes. All
*money-committing* actions must be reachable in the bottom 60 % of the screen; recording flows
accept that both hands may join (the customer waits anyway), so sheets may host keyboards — but
the **commit button** still anchors at the sheet bottom, and quick-amount chips reduce typing.
Decision speed: owners answer questions like "هل وصلت دفعة خالد؟" in ≤3 seconds; comparisons
(planned vs actual) must be precomputed and adjacent, never a drill-down away.

**Trust in money display** is behavioral, not stylistic: (a) unknown is never painted as 0 — an
invented zero is a lie that costs real dinars; (b) exactly three decimals with "د.أ" every time —
fils ambiguity reads as sloppiness; (c) a visible "آخر تحديث" timestamp; (d) offline honesty —
"محفوظ محليًا؛ سيُزامن عند الاتصال"; (e) reversibility — "عكس العملية" always exists, which
gives the courage to act fast; (f) no counting-up number animation (a mid-animation value can be
misread as final); (g) sign is the direction signal, color only reinforces — the screen is often
read in glare, and ~8 % of male users don't parse red/green.

## 2. Information hierarchy — component test composition at 390 px

The canonical test composition is the **الرئيسية (home) composition**, because it exercises every
budget rule at once: one PrimaryValueBlock, one QuickActionRail, one MetricGroup, one list owner,
one filled brand action, one comparison slot, ≤3 surfaces, ≤3 dividers. The order below is the
mandatory before-scroll plan. Viewport 390×844; content column = 390 − 2×16 px edge = 358 px;
single vertical scroll owner = the page.

| # | Zone | Height | Contents and rules |
|---|------|--------|--------------------|
| 1 | Integrated top zone (in flow, not sticky) | 64 px | Start (right): business name "بقالة النور" 15/600 + context line 13/400 ("صندوق اليوم · 08/09/2026"). End (left): the ONE Avatar 40×40, radius 12 — entry to "الحساب والإعدادات". No back button, no title bar. |
| 2 | PrimaryValueBlock (on canvas, NOT in a card) | 104 px | Label 15/500 "رصيد الصندوق" → value 32/600 `<bdi dir="ltr">431.100</bdi>` + "د.أ" → qualifier 13/400 "آخر تحديث 14:20 · <bdi dir="ltr">+12.500</bdi> عن أمس" (signed delta; may carry the composition's single comparison pair). |
| 3 | QuickActionRail zone | 124 px | Tiles 88×92 (icon 24 + label 13), gap 8, radius 12; RTL scroll, snap; first tile = the single filled brand action "سجّل بيعة"; 16 px trailing-edge fade signals continuation. |
| 4 | MetricGroup — ONE surface, radius 16 | 170 px | Surface padding 12; 3 MetricRows × 48 px ("مبيعات اليوم 1,240.500"، "مصروفات اليوم 86.250"، "ذمم العملاء 3,418.750") + 2 internal hairlines (counted in divider budget). |
| 5 | Section header | 36 px | "أحدث العمليات" 15/600 + quiet action "عرض الكل" 14/400; 1 hairline below (divider #3). |
| 6 | Operational list start | 72–216 px | First OperationalRow 72 px ("خالد الحوراني · بيعة · <bdi dir="ltr">86.250</bdi> · 10:24") + partial second row as scroll affordance. |

Running total: 64+104+124+170+36+144 = 642 px + 4 inter-block gaps ×8 = **674 px**. Visible canvas
above the bottom nav on 390×844 ≈ 716 px (844 − 44 status − 64 nav − 20 home-indicator inset),
so two full rows plus ~40 px of a third sit above the fold; in a desktop browser test frame
(no status bar) ~760 px → 2.5 rows. The glance layer (zones 1–3, 292 px) always fits, even on
320×568-class devices (≈440 px visible), where zones 4–6 compress to two MetricRows and one list
row.

**Deliberately below the fold:** the full operational feed (20-row batches, prefetch triggered
near the last 5 rows, 3 skeleton rows on load), the planned-vs-actual comparison chart when used,
schedules preview, any second MetricGroup (only with documented reason), search and filters for
the feed, older dates, and the "عرض المزيد" quiet action. Below-fold content is *reference*,
not *glance*; it may scroll, the glance layer may not. No element above the fold may be sticky
except the bottom navigation (the only persistent chrome) — the top zone scrolls away on purpose,
keeping money numbers closer to the thumb.

**Budget recap enforced by this hierarchy:** one rail; one MetricGroup; one PrimaryValueBlock;
max one comparison pair (in the qualifier or the planned-vs-actual chart, never both); no
repeated key value (the صندوق number appears exactly once); max 3 visible surfaces (MetricGroup +
one optional state banner + rail-as-zone — interpretation documented in §7); max 3 visible
dividers (2 in MetricGroup + 1 under section header); one vertical scroll owner (page; sheets
lock it while open; the rail scrolls horizontally only); max one filled brand-family action
(the first rail tile, or a sheet's primary button — never both visible in the same layer); max
two semantic color families and max two colored numeric values per composition.

## 3. Native phone patterns

### 3.1 Bottom navigation (the only persistent chrome)
Height 64 px + bottom safe-area inset, **radius 0, edge-to-edge** — it is part of the device
frame, not a floating pill, and it never hides on scroll (hiding chrome disorients this
audience and breaks the "one persistent anchor" mental model). Five slots: 4 destinations +
"المزيد". Icons 24 px (style from Agent 02); labels 14 px — 400 inactive, 500 active in the
brand color; per-item touch target 64×48 (exceeds the 44 px minimum). A badge (16 px dot, max
two digits) on "المزيد" counts unresolved sync conflicts. Switching is instant with an 80 ms
pressed state and light haptic; there is **no state in the nav other than active/inactive** and
no hamburger, no drawer, no tab bar on top. "المزيد" opens a plain full page of sections
(المخزون، شركات التوصيل، الجدولة، التقارير) — it is a destination, not a sheet.

### 3.2 Integrated top zone
The top zone is page content, not a detached bar: it scrolls with the page, has no elevation,
no divider of its own, and no back affordance. Top-level tabs never need back (switching is
non-destructive); detail and task flows live in **sheets**, whose dismissal affordance is the
drag handle and close button. The zone carries identity (business name), context (one 13 px
line: date or "غير متصل — محليًا"), and exactly **one Avatar 40×40** (radius 12, initials "أ.ن"
or photo) → "الحساب والإعدادات" — the unified profile/settings
entry. There is no second avatar, no settings gear, no notification bell anywhere in the
library; notifications surface as state rows in context (a threshold alert is an inline row in
the materials list, not a bell badge).

### 3.3 Sheet vs dialog decision matrix

| Situation | Pattern | Micro example |
|---|---|---|
| Any recording flow (keyboard + multiple fields) | Bottom sheet, tall 92 % | "سجّل بيعة" لخالد الحوراني: عميل + أصناف + مبلغ |
| Amount-first entry with prefilled data | Bottom sheet, medium 60 % | تحصيل دفعة خالد: المتبقي 250.000 معبأة مسبقًا |
| Picker from a searchable list | Bottom sheet, medium, search input on top | اختيار "مستودع زهران" في فاتورة مورد |
| Date selection | Bottom sheet, peek 40 %, calendar + DD/MM/YYYY display | تاريخ استحقاق الفاتورة 15/10/2026 |
| Filters over long lists | Bottom sheet + segmented + checkboxes | تصفية الذمم: "متأخرة فقط" |
| Irreversible / destructive confirmation | **Dialog** (never sheet) | "عكس تحصيل 250.000؟" مع سطر النتيجة |
| Either/or conflict resolution (≤2 options) | Dialog with two labelled value rows | تعارض مزامنة: النسخة المحلية 250.000 مقابل السحابية 200.000 |
| Brief blocking error on a flow | Inline error strip in the sheet action bar first; dialog only if context is lost | فشل حفظ المصروف |
| Transient success confirmation | Quiet-completion or state row — never modal | "تمّ تسجيل البيعة" |

Rules: dialogs never contain inputs; sheets never carry destructive confirmation; dialog buttons
max 2; while a sheet is open it **owns vertical scroll** (page scroll locked); a dirty sheet
(unsaved input) does not dismiss on swipe — it shows a confirm dialog "تجاهل التغييرات؟".

### 3.4 Swipe and drag expectations
- **OperationalRow:** single-direction swipe (drag the row toward the left) reveals up to two
  actions anchored at the row's leading (right) edge, each 48 px wide with 14 px labels (e.g.
  "عكس"، "إلغاء"). A destructive action **never executes on swipe release** — it always routes
  through a confirm dialog. Swipe is disabled on rows in pending-sync state.
- **Sheets:** 36×4 drag handle; snap points 40 / 60 / 92 %; drag-to-dismiss only when clean.
- **QuickActionRail:** RTL horizontal scroll; `scroll-snap-type: x mandatory` at 96 px (tile 88 +
  gap 8); initial position anchored to the right (RTL start); 16 px fade mask on the left edge
  only. No drag-reordering, no long-press context menus — hidden gestures do not survive this
  audience.
- **Pull-to-refresh:** allowed on list feeds as a *manual* retry channel (it never triggers
  automatically; auto-retry stops after the first failure per the state policy).
- **Charts:** not interactive in v1 — tapping opens a detail sheet. Glance integrity beats
  exploration.

### 3.5 One-hand reachability map (bottom 60 %)
On 390×844 the thumb zone starts ≈338 px from the top (40 % down). **Must live in the bottom
60 %:** all commit/save buttons (sheet action bars are bottom-anchored + safe-area aware), the
bottom navigation itself, retry actions in inline error states, swipe-revealed row actions
(rows scroll into the lower band), and segmented/checkbox controls inside sheets. **Dialogs**
sit with a lower vertical bias (~60 % of the dialog below screen midpoint) so their buttons land
in the thumb arc. **Documented tradeoff:** the QuickActionRail occupies y ≈ 224–348 (27–41 % from
top) — a stretch zone, not the lazy thumb zone. This is accepted because the rail is a
*discovery* surface (glance value), every rail action is also reachable through the "العمليات"
destination (nothing is thumb-locked), and the actual commit step always happens at a sheet
bottom. The Avatar is a navigation entry, not an action, and is intentionally top-left. Amount
quick-chips (‎+5.000‎ / ‎+10.000‎ / ‎+20.000‎) sit directly above the sheet's primary button to keep
one-thumb amount entry possible.

## 4. State truth for financial values

The four value conditions are **distinct and never interchangeable**. Displaying an unknown as
"0.000" is classified as a data-integrity defect, not a styling choice.

| Condition | Meaning | Display (value slot) | Arabic wording | Micro example | Forbidden |
|---|---|---|---|---|---|
| Unknown | Value exists but is not yet determined (still loading, sync in flight) | Em-dash "—" (U+2014), 32 px, same slot and weight as a number | Qualifier: "قيد المزامنة…" | رصيد صندوق الفرع الآخر أثناء المزامنة | "0.000", blank, spinner in the value slot |
| Unavailable | Value cannot be shown (source down, feature off, permission) | Text "غير متوفّر" 15/400, muted, same slot | "غير متوفّر" | رصيد تسوية شركة توصيل قبل ربط الحساب | "—", "0.000", hiding the row silently |
| True zero | Verified zero (checked against ledger) | `<bdi dir="ltr">0.000</bdi>` exactly, with label + currency | Label carries it: "رصيد خالد الحوراني" | خالد سدّد كل ذممه — المتبقي 0.000 | Dropping decimals ("0"), "—" |
| Empty input | User has not entered anything yet | Placeholder 14/400 "أدخل المبلغ" — no value rendered | "أدخل المبلغ" | حقل المبلغ في ورقة "أضف مصروفًا" | Pre-filled "0.000" (biases entry), validation before submit |

**Sign conventions.** Direction is carried by the minus sign, not color: "−" is **U+2212**,
placed inside the LTR bdi immediately before the digits — `<bdi dir="ltr">−86.250</bdi>` — so it
can never be mirrored or re-ordered by the RTL context. "+" appears only in delta/comparison
contexts (qualifiers, planned-vs-actual), never on a primary balance. Number format: Western
digits 0–9 only, thousands grouped with "," (e.g. "1,250.000"), **exactly three decimals**,
trailing zeros preserved. Color (one red family, one green family, max two colored values per
composition) reinforces but never replaces the sign. Cancelled/reversed rows keep their original
sign, rendered muted with a state qualifier — the sign is history, not a live signal.

**Bidi isolation rules.** (1) Every money value, delta, count, and date is wrapped in
`<bdi dir="ltr">…</bdi>` inside the RTL document. (2) The currency "د.أ" stays **outside** the
bdi and is written after the number in logical order, so RTL layout renders it to the *left* of
the number — the correct Arabic reading (number first, then currency). (3) "د.أ" only — never
"JOD", never "دينار أردني" spelled out. (4) Dates are DD/MM/YYYY, English digits, bdi-isolated
(slashes are bidi-neutral and will otherwise scramble). (5) U+2212 is verified present in all
shipped latin subsets; digits, comma, and period live only in the latin subsets — both subsets
must be loaded on every test page. (6) The Arabic-Indic digits U+0660–0669 do exist in the Arabic
subsets; the system must never emit them (checkpoint for Agents 03/04).

## 5. Arabic copy guidelines

Copy is written for a Jordanian shopkeeper reading at a glance: **verb-first actions, ≤2-word
buttons**, ≤6-word state lines that always end in an action or a clear next step. The register is
living Jordanian trade Arabic — "بيعة"، "تحصيل"، "ذمم"، "مورد"، "صندوق"، "تسوية" — not stiff MSA
("يرجى القيام بتسجيل…") and not Gulf or Levantine slang. Numbers in copy are always Western
digits inside a bdi. Diacritics are used only where misreading is likely (متوفّر، محليًا، عُكست،
أُلغيت، سيُزامن). Error copy names the failing action — "تعذّر تحميل الذمم — أعد المحاولة" —
never a bare "خطأ". Empty states are one line + one action, no illustrations. Buttons never
exceed two words; if a third word feels necessary, the concept is too heavy for a button and
belongs in a sheet title.

| State | Proposed copy (≤6 words) | Notes |
|---|---|---|
| empty (feed) | "لا عمليات بعد — سجّل أول بيعة" | Line + the rail's filled tile answers it |
| empty (list/search) | "لا نتائج مطابقة" + action "امسح البحث" | Verb-first 2-word action |
| loading | "جارٍ التحميل…" | With 3 skeleton rows, never a blocking spinner |
| error | "تعذّر التحميل — أعد المحاولة" | Retry is a visible button; auto-retry already stopped |
| offline saved | "محفوظ محليًا — سيُزامن عند الاتصال" | Passive future is honest, not blaming |
| pending | "بانتظار التأكيد" | Clock glyph optional; sync in flight |
| conflict | "نسختان متعارضتان — اختر الأحدث" | Dialog title carries entity: "تعارض في دفعة خالد الحوراني" |
| failed | "فشلت العملية — أعد المحاولة" | After one auto-retry attempt, manual only |
| completed | "تمّ بنجاح" / "تمّ تسجيل البيعة" | Quiet-completion, no modal toast for minor ops |
| cancelled | "أُلغيت العملية" | Muted row state; amount keeps original sign |
| reversed | "عُكست العملية" | Muted row + counter-entry row appears |

Reference buttons (verb-first, ≤2 words): "سجّل بيعة" · "أضف مصروفًا" · "استلم دفعة" ·
"سدّد موردًا" · "عكس العملية" · "إلغاء" · "احفظ" · "تجاهل" · "أعد المحاولة" · "عرض الكل" ·
"جدول متابعة". Sheet titles are noun phrases ("بيعة جديدة", "تحصيل من خالد الحوراني");
buttons inside them stay verb-first.

## 6. Navigation proposal — 4 destinations + "المزيد"

| Slot | Label | Domain | Rationale |
|---|---|---|---|
| 1 | الرئيسية | Glance composition: صندوق balance, quick actions, today metrics, live feed | The money question answered in 1.5 s |
| 2 | العمليات | Recording + feed: sales, cash-in, expenses, purchases | Highest-frequency verbs live one tap from every tab |
| 3 | الذمم | Customers/receivables + suppliers/payables | Jordanian trade word; covers both sides in one short label |
| 4 (overflow) | المزيد | المخزون، شركات التوصيل والتحصيل، الجدولة، التقارير | Short label (≈42 px) always fits; preserves hierarchy |

Profile/settings is **not** a destination: the single Avatar in the integrated top zone owns it
("الحساب والإعدادات").

**Why five full labels would clip at 320 px.** At 320 px, five slots give 64 px each; after 2 px
insets per side the safe label width is 60 px. Nav labels are 14 px minimum (the 13 px exception
is reserved for qualifiers and QuickActionRail labels) and cannot be ellipsized — "التح…" is
unreadable and destroys destination recognition. Measured upper-bound widths at 14 px/500
(isolated-advance method, shipped font): "الرئيسية" 70.2 px, "العمليات" 64.4 px, "الصندوق"
63.3 px, "المبيعات" 67.1 px, "التسويات" 72.8 px, "المستحقات" 82.6 px, "التحصيلات" 85.9 px,
"شركات التوصيل" 118.1 px; the chosen set: "الرئيسية" 70.2, "العمليات" 64.4, "الذمم" 35.6,
"المزيد" 41.9. Shaped (connected) text runs ~15–25 % narrower than these bounds, so the chosen
four fit 60 px with slack — but the fifth-slot *domain* candidates that would justify a full
label (collections, payables, settlements) all have upper bounds ≥63 px: relying on shaping
gains to save them is not a guarantee, and even the best case ("المخزون" 49.1, "الجدولة" 50.1)
demotes a money-critical domain to a coin-flip while leaving zero slack in the "الرئيسية" slot.
Additionally, Micro has nine domains; any flat five flattens priority. So: 4 destinations + a
short, guaranteed-safe "المزيد". **To verify (Agent 03):** re-measure shaped widths in a real
layout engine; if "الرئيسية" measures >60 px shaped at 320 px, the fallback is the shorter
"الرئيسي" is NOT acceptable — instead reduce insets to 0 and re-measure before any label change.

## 7. Handoff notes (documented, not implemented)

- **Agent 02:** needs color assignments for: brand family (one filled action), two semantic
  families (direction red/green as *secondary* signal), muted/ink hierarchy for 32/15/13 px type,
  contrast ≥4.5:1 on the light background for all text.
- **Agent 03:** implement tokens: 16 px screen edge, radius 12/16/24, targets 44/48, tile
  88×92, row 72/48, nav 64+inset, value 32/600, label 15, qualifier 13, body 14; motion 80/120/
  240 ms, `cubic-bezier(0.2, 0, 0, 1)`; bdi wrappers per §4; sheet snap 40/60/92 %.
- **Agent 04:** checkpoints — never Arabic-Indic digits; unknown ≠ 0; sign not color-only;
  focus rings 2 px on light; live-region announcements for state transitions; 14 px Arabic
  minimum with the two documented exceptions.
- **Agent 05 (open interpretation):** "max 3 visible surfaces" is interpreted here as three
  content-block surfaces (MetricGroup, one optional state banner, the rail counted as ONE zone,
  not per-tile). MetricGroup internal hairlines count toward the 3-divider budget. Both
  interpretations need sign-off.
