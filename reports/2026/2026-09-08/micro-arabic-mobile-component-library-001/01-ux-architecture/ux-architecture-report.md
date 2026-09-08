# UX Architecture Report — Arabic-First Micro Component Library

Agent 01 · Task 2-a · RUN_ID `20260908T133450Z-16d11` · Scope: UX architecture, information hierarchy, native phone patterns, state truth, test composition, Arabic microcopy.

This report defines how every component family in SPEC §6.9 serves real small-business operations. All prose is English; Arabic appears only as UI copy; values use English digits, `DD/MM/YYYY` dates, and `د.أ` exclusively. Companion files: `component-contracts-draft.md` and `task-to-component-map.md`.

---

## 1. Target user and rapid scanning behavior

أبو محمد runs a bakery plus mini-market in Amman with 2–4 employees. He opens the app between customers, often holding a bag or a tray in one hand, with a customer waiting in front of him. He does not read screens; he hunts for a number, a state, and a button. He trusts numbers he can verify against his pocket and his notebook, and he distrusts anything decorative, ambiguous, or "bank-like".

In the first two seconds his eyes perform a fixed path in RTL reading order: (1) the largest number near the top-right — "how much cash do I have right now?"; (2) any warning-shaped element — clock, alert icon, red or amber chip — "what needs me today?"; (3) the first quick action — "can I record this sale before the customer leaves?". Everything else is optional; if any of these three is missing or buried, the app fails him for that interaction.

Glanceability rules (binding for all agents):

1. Exactly one primary number per viewport (the `PrimaryValueBlock`); it must answer a stock question ("كم عندي؟") or a net question ("صافي اليوم؟") without arithmetic by the user.
2. State is readable as a word plus an icon before it is readable as a color; color is never the only signal (SPEC §6.3).
3. Direction of money is carried by an explicit sign (`+` / `-`) first; color only reinforces (SPEC §6.12).
4. Numbers use tabular lining-nums, always two decimals, thousands separators, so digit columns align vertically and magnitudes compare instantly.
5. Section = one question. "نقد اليوم" answers cash; "حركة اليوم" answers flow; "متابعة اليوم" answers what needs action. No mixed-purpose sections.
6. The most frequent action (recording a sale) is visible without scrolling and is the first tile in the `QuickActionRail`.
7. Anything needing action sits lower on the screen (thumb zone); anything read-only sits higher (eye zone).
8. A peek of at least 16px (320px width) of the next rail tile, or a partially cut row, must always signal continuation — never a dead flat edge.
9. Values, dates, and percentages are bidi-isolated (`dir="ltr"`) so `-92.50` never renders as `92.50-`.
10. If a value is unknown, it is shown as `—` with a reason — never as `0` (see Section 4).

---

## 2. Information hierarchy — exactly what appears before scrolling at 390px

Portrait 390px, default text size, canvas extending under a dark-icon status area (no faked system UI, SPEC §6.2), `BottomNavigation` as the only persistent chrome (~64px + safe area). Estimated content budget before the fold: roughly 700px. In order:

1. **Integrated top zone (~56px)** — "مخبز أبو محمد" (15px/600) over "الثلاثاء 08/09/2026" (13px), Avatar 32px at the far end (visual left in RTL). Reason: orientation (which business, which day) costs one glance and the zone scrolls away with content; the single Avatar is the only profile/settings entry (SPEC §6.7).
2. **PrimaryValueBlock on canvas (~84px)** — label "نقد اليوم", value `1,284.50` at 32px/600, unit `د.أ`, qualifier "حتى 14:20". Reason: the first-fixation answer to the cash question; placed on the canvas, not in a card, so it reads as fact, not as a widget (SPEC §6.9.1).
3. **QuickActionRail (~112px)** — five 88×92 tiles, `إضافة بيع` first (rightmost, the single brand-tinted tile), then `تحصيل دين`, `إضافة مصروف`, `إضافة شراء`, `تسجيل دفعة`. Reason: the recording act must be reachable while the customer is still at the counter; horizontal scroll keeps five actions in one row (SPEC §6.8).
4. **MetricGroup on one surface (~196px)** — title "حركة اليوم", three aligned `MetricRow`s: `مبيعات اليوم 465.00`, `تحصيلات ذمم +210.00` (positive), `مصروفات اليوم -92.50` (sign only, no color). Reason: after the stock answer, the flow answer; one surface, no card-per-metric noise (SPEC §6.9.2).
5. **`متابعة اليوم` section header + first row (~120px)** — header (13px, count `3`), then the pending delivery settlement row: `شركة التوصيل السريع — بانتظار التحويل — منذ 05/09/2026 — 142.00 د.أ` with a warning clock chip. The fold lands on the second row, which is the continuation cue.

Below the fold (still part of the test composition, documented for the lab): the remaining follow-up rows (`أبو أحمد — تحصيل دين — اليوم 12:40 — 120.00 د.أ`, completed; `طحين فاخر 10كغ — متبقي 4 أكياس — الحد 6`, threshold), the single comparison pair (`ذمم العملاء 1,175.00` vs `ذمم المورّدين 640.00`, two `CompactTile`s), and a quiet `عرض كل متابعات اليوم` link. At 320px the same order holds; heights compress only through text wrapping, never fixed heights (SPEC §6.5). At 430px more of section 5 is visible — the order never changes, only the fold position.

---

## 3. Native phone patterns

### 3.1 Integrated top zone with one Avatar

The top zone is page content, not chrome: it lives on the canvas, has no elevation, no fill, no hamburger, no action icons, and scrolls away. It carries business context (name + full date) because أبو محمد must know which day's numbers he is trusting — a wrong-day balance is worse than none. Exactly one `Avatar` (32px, radius full, 44px hit area) sits at the zone's end (visual left in RTL) as the unified profile/settings entry; keeping it out of the scanning start preserves the first two seconds for numbers, and its low frequency justifies the stretch.

### 3.2 BottomNavigation — the only persistent chrome

Five seats: four destinations plus a clearly-labelled More, because five full Arabic destination labels plus More would risk clipping at 320px (SPEC §6.7). Proposed labels, all ≤8 Arabic characters, verified to fit at 320px (64px per seat) at 14px: `اليوم`, `المبيعات`, `الذمم`, `المخزون`, `المزيد`. In RTL order اليوم is the rightmost (first) seat; `المزيد` opens a sheet listing secondary destinations (`المورّدون`, `شركات التوصيل`, `التقارير`, `الإعدادات`) — never a blank or disabled fifth seat. The bar is edge-to-edge with radius 0, icons 24px/2px stroke, labels 14px, item height 64px + safe-area padding, every seat a ≥44px target. Active state: icon and label in ink-strong (600) with a 24×3px indicator bar in `brand-atmosphere` at the top of the seat — this deliberately avoids a brand-tint pill because the QuickActionRail already spends the viewport's one brand-family tinted surface.

### 3.3 Sheets vs dialogs — decision rules

1. **Sheet** for anything with input, selection, scrolling, or more than two choices: recording flows (`إضافة بيع`, `تحصيل دين`, `إضافة مصروف`, `إضافة شراء`, `تسجيل دفعة`), customer/supplier pickers, settlement follow-up details, the More menu. Sheets are thumb-friendly (actions pinned at the sheet's bottom), keep page context behind a 45% scrim, and dismiss by scrim tap, drag handle, or back gesture.
2. **Dialog** only for short binary decisions that need no new context: destructive confirm (`حذف العملية؟`), discard guard on a dirty sheet (`تجاهل التغييرات؟`). Dialogs are centered, small, 160/120ms, and never contain form fields.
3. **Never** a dialog for entry, never a sheet stack deeper than one (a picker opened from a sheet replaces it), and never a toast as the only proof of completion — completion is an inline state change on the originating row or button (check + `تم`).
4. Sheet geometry: top radius 24, drag handle 32×4, entry/exit 240/180ms, scrim 200ms; primary CTA is a full-width 48px filled button in `brand-ink` with white text — the single filled brand-family action of that viewport (SPEC §6.3).

### 3.4 One-hand reachability (thumb zone map)

For a right-thumb (or left-thumb, symmetric) one-handed hold: the natural arc is the bottom third; the stretch zone is mid-screen; the top quarter is read-only territory.

| Screen band | Zone | Placed there |
| --- | --- | --- |
| Bottom ~25% (incl. bottom navigation) | Natural rest | `BottomNavigation` seats, sheet primary CTAs, retry buttons on failed rows, quiet links (`عرض الكل`) |
| Middle band | Comfortable stretch | `QuickActionRail` tiles, `OperationalRow` taps, `MetricRow` drill taps |
| Top ~25% | Eye zone, not thumb zone | `PrimaryValueBlock` (read-only by design), top zone, Avatar (low frequency) |

The rule: **things you must read live high; things you must touch live low.** The most frequent touch target after navigation is the sheet CTA and the rail's first tile — the rail sits at the top of the stretch band, which is acceptable because its tap is a single confident strike on an 88×92 target, far above the 44px minimum.

---

## 4. State truth for financial values

Four conditions are distinct and must never collapse into each other or into `0`:

| Condition | Meaning | Rendering | Example |
| --- | --- | --- | --- |
| Unknown | Value exists but is not yet determined | `—` (em dash, bidi-safe) + 13px reason "قيد التحديد" | delivery settlement amount before the company confirms |
| Unavailable | Value exists but cannot be shown now (offline, source down) | `—` + "غير متاح حاليًا" + retry action when useful | customer balance while offline, after retry policy stops |
| True zero | Determined, meaningful zero | Real value `0.00 د.أ`, same weight as any number, never dimmed | `ذمم أبو أحمد 0.00 د.أ` after full settlement — an achievement, not an absence |
| Empty input | No user content in a field | Placeholder `0.00` in ink-subtle, never committed as a value | amount field before typing |

Two supporting rules: a daily metric whose underlying records have loaded and are genuinely empty may show `0.00` only when zero is operationally meaningful (no expenses recorded today); if records have not loaded, the metric is Unknown (`—`), never `0`. A list with no entries is an empty state ("لا عمليات اليوم" + action), not a zero. Sign is the primary direction signal: stock values (cash on hand, balances) carry no sign; flow values carry an explicit `+` or `-` with the minus always leading inside a `dir="ltr"` isolate. Color is secondary reinforcement — `-92.50` in plain ink-strong is a complete, truthful statement; danger color is reserved for real failures and destructive actions, not for every outflow.

---

## 5. Proposed TEST COMPOSITION — exact content

One composition: **"Today" view for مخبز أبو محمد**, Tuesday `08/09/2026`, 14:20. Section order, exact labels, exact values:

1. **Top zone**: `مخبز أبو محمد` / `الثلاثاء 08/09/2026` / Avatar (32px, end side).
2. **PrimaryValueBlock (canvas)**: label `نقد اليوم` — value `1,284.50` `د.أ` — qualifier `حتى 14:20`. No state line (nothing decision-critical about the value itself).
3. **QuickActionRail (5 tiles, RTL, snap, edge fade)**: `إضافة بيع` (brand-tint, icon plus) → `تحصيل دين` (hand-coins) → `إضافة مصروف` (receipt) → `إضافة شراء` (package) → `تسجيل دفعة` (banknote). Locked geometry: tile 88×92, icon 24, label 13px, icon–label gap 8, tile gap 8, rail padding 16; measured peek 16px at 320px, ≥28px at 360/390/430.
4. **MetricGroup (surface, title `حركة اليوم`, 3 rows, 2 internal hairline dividers)**:
   - `مبيعات اليوم` — `465.00` `د.أ` (neutral)
   - `تحصيلات ذمم` — `+210.00` `د.أ` (positive — colored number 1)
   - `مصروفات اليوم` — `-92.50` `د.أ` (ink-strong, sign only)
5. **`متابعة اليوم` section on canvas (header + 3 rows, no dividers, 12px row gaps)**:
   - `شركة التوصيل السريع` / `بانتظار التحويل` / `منذ 05/09/2026` / `142.00 د.أ` — clock chip, warning family
   - `أبو أحمد` / `تحصيل دين` / `اليوم 12:40` / `120.00 د.أ` — check, positive family (completed)
   - `طحين فاخر 10كغ` / `متبقي 4 أكياس` (colored number 2, warning) / `الحد 6` — threshold icon, warning family
6. **Comparison pair (2 `CompactTile`s on surface, gap 12)**: `ذمم العملاء` `1,175.00` `د.أ` + qualifier `عند 4 عملاء` | `ذمم المورّدين` `640.00` `د.أ` + qualifier `مؤسسة الشرق`. Both values neutral ink.
7. **Quiet link**: `عرض كل متابعات اليوم` (text button).

Budget compliance (SPEC §6.10): one `PrimaryValueBlock` ✓; one `QuickActionRail` with 5 actions, `إضافة بيع` first ✓; one `MetricGroup` with 3 aligned rows ✓; one comparison pair ✓; surfaces = MetricGroup + 2 CompactTiles = 3 ✓; semantic families = positive + warning = 2 ✓; colored numbers = `+210.00` and `4` = 2 ✓; dividers = 2 (inside MetricGroup), one held in reserve ✓; no repeated key value (`1,284.50 / 465.00 / +210.00 / -92.50 / 1,175.00 / 640.00 / 142.00 / 120.00` all unique) ✓; one vertical scroll owner (page), rail scrolls horizontally ✓; brand-family surfaces = one tinted rail tile (the sheet CTA's filled brand-ink appears only when a sheet is open, as the overlay's own single filled action) ✓. Internal consistency: `+210.00` = 120.00 (أبو أحمد, shown) + 90.00 (مطعم النخيل, recorded earlier, not a follow-up); `142.00` is pending, so it is correctly absent from `نقد اليوم`.

---

## 6. Arabic microcopy principles and copy bank

Principles: (1) verb-first, imperative, ≤3 words for buttons — `سجّل`, `احفظ`, `اطّلع`, not noun phrases; (2) numbers in copy are English digits with the unit once, never repeated; (3) state words are nouns/participles a busy reader can pattern-match (`بانتظار`, `مكتمل`, `فشل`) and are always paired with an icon, never color alone; (4) errors name the fix, not the fault — `أدخل مبلغًا أكبر من صفر`, not "invalid input"; (5) no technical sync vocabulary in primary content — "محفوظ على الجهاز" not "queued for synchronization"; (6) dates always `DD/MM/YYYY`, today is `اليوم`, relative time only up to `منذ` + date; (7) never `JOD`, never spelled-out currency; (8) empty states are one line plus one useful action — no illustration theatre.

Copy bank (locked suggestions; agents may extend, not contradict):

- **PrimaryValueBlock**: `نقد اليوم`، `صافي اليوم`، `ذمم العملاء`، `مستحقات المورّدين`؛ qualifiers: `حتى 14:20`، `عند 4 عملاء`، `هذا الأسبوع`.
- **MetricGroup / MetricRow**: `حركة اليوم`، `مبيعات اليوم`، `تحصيلات ذمم`، `مصروفات اليوم`، `مشتريات اليوم`، `مرتجعات اليوم`؛ attention: `تجاوز المخطط`؛ unavailable: `غير متاح حاليًا`.
- **QuickActionRail (locked order)**: `إضافة بيع`، `تحصيل دين`، `إضافة مصروف`، `إضافة شراء`، `تسجيل دفعة`.
- **OperationalRow meta**: `تحصيل دين — اليوم 12:40`، `بانتظار التحويل منذ 05/09/2026`، `متبقي 4 أكياس — الحد 6`، `شراء آجل — 06/09/2026`، `دفعة نقدية — 07/09/2026`.
- **CompactTile / comparison**: `ذمم العملاء`، `ذمم المورّدين`، `طلبات اليوم`، `مستحق لك`، `مستحق عليك`.
- **Buttons**: `تسجيل البيع`، `تحصيل`، `حفظ`، `تأكيد`، `إلغاء`، `حذف`، `إعادة المحاولة`، `إرسال التذكير`، `عرض الكل`، `عرض التفاصيل`، `إضافة`، `تعديل`، `متابعة التعديل`، `تجاهل`، `تسجيلها مع ذلك`، `عرض الموجودة`، `مسح البحث`.
- **Inputs**: labels `المبلغ`، `التاريخ`، `الفئة`، `اسم العميل`، `اختر العميل`؛ placeholders `0.00`، `ابحث عن عميل أو عملية`، `ملاحظة (اختياري)`؛ segmented `نقدي | آجل`؛ tabs `اليوم | الأسبوع | الشهر`; checkbox `تنبيه عند وصول التحويل`; switch `تذكير بالمتابعات`.
- **Sheet / Dialog titles**: `إضافة بيع`، `تحصيل من أبو أحمد`، `شراء من مؤسسة الشرق للتجهيزات`، `تسوية شركة التوصيل السريع`، `حذف العملية؟`، `تجاهل التغييرات؟`، `عملية مشابهة موجودة`.
- **State wordings (chips / lines)**: empty `لا عمليات اليوم` + `سجّل بيعًا`; empty search `لا نتائج مطابقة` + `مسح البحث`; loading (a11y) `جاري التحميل`; button loading `جاري الحفظ…`; error `تعذّر التحميل` + `إعادة المحاولة`; offline local-save `محفوظ على الجهاز` / `يُرسل عند عودة الاتصال`; pending `بانتظار التحويل` / `بانتظار التأكيد`; conflict `عملية مشابهة موجودة`; failed `فشل الإرسال` + `إعادة المحاولة`; completed `تم` / `تم التسجيل` / `تم التحصيل`; cancelled `أُلغيت`; reversed `معكوسة` with detail `عُكست العملية — أُضيف قيد مقابل`، `4 أكياس` context kept action-oriented: `أضف شراء`.
- **Charts**: `المبيعات آخر 7 أيام`، `المخطط مقابل الفعلي — الأسبوع الحالي`، `هدف الشهر`، `+12% عن الأسبوع الماضي`، text alternative `الاتجاه صاعد`.

These principles feed every contract in `component-contracts-draft.md`; conflicts found by Agents 02–04 resolve toward these rules, then Agent 05 logs them.
