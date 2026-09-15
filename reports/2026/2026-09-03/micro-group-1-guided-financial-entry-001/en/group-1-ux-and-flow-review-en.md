# Group 1 UX & Flow Review — Screen Contracts, Journeys, Arabic Copy, States, Mobile Behavior, Before/After

| | |
|---|---|
| **Report ID** | micro-group-1-guided-financial-entry-001 (UX & flow review) |
| **Date** | 2026-09-03 |
| **Device frame** | 360–390px portrait, one-handed, Arabic RTL, English digits, DD/MM/YYYY, JOD two decimals |
| **Design authority** | Micro's mobile UI/UX reference + design-token guards + text-density caps (§10.1); Zman as journey reference (never mechanism) |
| **Verification basis** | jsdom dom tests + live production-build browser QA at 390×844 with zero console errors |

## 1. Journey overview (before → after)

**Before:** the owner recorded an expense either through the quick sheet (amount + optional note + wallet, one honest effect sentence) or through a detailed editor whose field order was amount → date → counterparty → a collapsed classification layer → note, with a static effect sentence and no wallet question, no category, no allocation review, and no draft recovery. The question sequence existed in the data model but not in the interface's voice.

**After:** both paths speak the owner's question sequence. The quick sheet stays minimal (one mandatory input) and gains an optional one-tap category chip row plus the honesty clause. The detailed editor now asks, in order: what happened (title) → how much (with shared total/percentage when needed) → **from where the money came** (wallet, sheet-identical vocabulary) → date → counterparty → the progressive layer (category first, then nature, relationship, allocation with a live review card, knowledge) → note → save, with a live effect preview derived from the commit intent, path guidance for purchases and honest deferral for assets/loans, draft recovery on reopen, and attribution-failure honesty before any navigation.

The five-seat shell (مشروعي الآن | العمل | سجّل FAB | مالي | أدواتي), the centered FAB, the top bar's role, and the deep/surface route classification are **unchanged** — no sixth seat, no second FAB, no competing bottom bar, no modal-over-page editor.

## 2. Screen contract — FinancialEventEditor (expense types)

- **Screen name:** FinancialEventEditor — «تسجيل مصروف مدفوع» / «تسجيل مصروف مستحق» — routes `/finance/new/operating_expense_cash`, `/finance/new/operating_expense_payable`.
- **User goal:** Record one operating expense with its context — amount, date, spending source, optional category, project relationship and share, knowledge state — and understand its true effect before saving.
- **Entry points:** Finance quick-actions (with `?from` preserved); the editor is create-only (corrections live in the events layer).
- **Return path:** `?from` if valid, else the documented canonical fallback `/finance` (contract 26); auto-return after successful save; manual back passes through the unsaved-changes guard when dirty (guard disarmed after a successful save — SA-5 fix).
- **Primary action:** «حفظ المصروف المصنف» — sticky (`micro-sticky-save`), above the keyboard, disabled with «جارٍ الحفظ…» while saving; becomes «ارجع إلى الوضع المالي» when an attribution-failure note is displayed.
- **Secondary actions:** back «الوضع المالي»; draft restore/discard banner; «افتح السجل المحفوظ» (attribution-failure state).
- **Visible before scroll (360px):** heading (overline + title + description), the effect card with the fixed-height «بعد الحفظ:» region, and the amount field — the amount is reachable without scrolling.
- **Progressive details:** the «أضف سياقًا للمصروف» layer (collapsed at rest): category first («تصنيفك للمصروف» + hint «على شو اندفعت المصاري؟ بنزين، رواتب، إيجار…» + ≤8 chips), then nature («طبيعته: ثابت ولا بتغير؟»), purpose, relationship («للمشروع ولا مشترك مع البيت أو نشاط آخر؟»), shared mode + note + **AllocationReviewCard** + knowledge note, and the two guidance notes at the bottom.
- **Financial effect preview:** «بعد الحفظ:» lines derived from the exact save payload (shared expansion module + domain dry-run); primary line names the wallet («من «الدرج»» / «من الكاش غير الموزع»); payable states «لا يتغير الكاش الآن»; unallocated-shared states it will not enter the result yet; combined negative «بلا حركة أمانة ولا سحب مالك»; category note when set. Fixed min-height region (no jitter above inputs); invalid input falls back to the static known-effect text.
- **Empty state:** creation screen; defaults amount 0, today's date, relationship «project», knowledge «known».
- **Loading state:** no full-screen loader; settleable payables list (settlement type only) loads asynchronously into its select.
- **Validation state:** inline `micro-field-error` (role=alert): invalid amount, empty note, shared percentage out of 0–100; per-field numeric validity through EnglishNumberInput.
- **Offline state:** fully local by design; save works offline; no sync claims.
- **Save success state:** «تم حفظ الحدث المالي محليًا.» then auto-return to source.
- **Save failure / honesty states:** service message inline; key reuse honesty («لم يُحفظ التعديل…») — never a false success; attribution failure keeps the page mounted with «حُفظ الحدث محليًا، لكن نسبته للمحفظة لم تتم… — المال محفوظ ضمن الكاش غير الموزع» + record link.
- **Correction path:** Finance → «السجل والأثر» → row → documented reverse / atomic edit / restore; the label is frozen per event (change = reverse + re-record).
- **Keyboard behavior:** amount uses EnglishNumberInput (decimal inputMode, ASCII digits); date is a native picker read as DD/MM/YYYY; selects need no keyboard; note is an RTL textarea; save stays above the keyboard; back opens the guard when dirty.
- **Small-phone behavior:** field grid collapses to one column under 380px; chips wrap (≈4–5/row, ≤2 rows; each chip capped at 160px with ellipsis + full label in title/aria); preview region fixed height; full-width save.
- **RTL & numeric behavior:** page RTL; all money via MoneyValue/bdi ltr (English digits, 2 decimals); dates DD/MM/YYYY in bdi; Arabic punctuation throughout; the category is free Arabic text.

## 3. Screen contract — ToolsIntegrity (/tools/integrity)

- **Screen name:** ToolsIntegrity — «فحص سلامة مالي» — surface route (bottom nav stays).
- **User goal:** Verify in one read that the numbers are consistent — and reach the right record if something needs a documented correction.
- **Entry points:** Tools module-states row («فحص سلامة مالي», always enabled); Finance truth-section text-action «فحص سلامة مالي — اطمن على أرقامك»; both preserve `?from`.
- **Return path:** `?from` else `/tools` (registered in the fallback registry and contract 26).
- **Primary action:** «افحص الآن» → «جارٍ الفحص…» (disabled while running); re-runnable; each run is a fresh read.
- **Secondary actions:** per-check «افتح السجل المعني» deep link (focused event row `/finance?layer=events&event=<id>` or `/cash`); collapsed «أعرض السجلات المتأثرة (N)» per failing check.
- **Visible before scroll:** back + heading (overline «أداة قراءة» + title) + promise card «يقرأ أرقامك ولا يغيّر شيئًا.» + verdict card with the run button (~first 350–400px).
- **Progressive details:** five check cards (title + status word + icon + detail + «الفارق:» when meaningful + offender count + collapsed sample ids + deep link).
- **Financial effect preview:** not applicable — read-only by contract; the zero-writes guarantee is test-enforced (snapshot equality before/after).
- **Empty state:** «لم يُجرَ الفحص بعد — اضغط «افحص الآن» لقراءة الأرقام كما هي.»
- **Loading state:** «جارٍ الفحص…» on the disabled button.
- **Validation state:** N/A (no inputs).
- **Offline state:** local read by design.
- **Success state:** verdict («سليم — الأرقام متسقة» / WARN / FAIL wording) + run timestamp DD/MM/YYYY + five check cards.
- **Failure state:** unexpected run errors show inline with retry; storage failures surface as failing checks (honest, not crashes).
- **Correction path:** deep links only — the fix happens in the existing documented surfaces; no auto-fix.
- **Keyboard behavior:** buttons only; focus order back → run → links; no traps.
- **Small-phone behavior:** check cards as `micro-setting-row` (icon + wrapping title + status + link); no horizontal overflow; long Arabic titles wrap to two lines.
- **RTL & numeric behavior:** RTL; drift money in bdi ltr; run date DD/MM/YYYY English digits; status always word + icon + color; offender ids (Latin) in bdi ltr.

## 4. Secondary screen deltas (summary contracts)

- **QuickActionSheet (expense mode):** + optional chip row «تصنيف سريع (اختياري)» (≤6 chips, single tap, deselect) placed after note/wallet and before the effect line; effect line gains «— بلا حركة أمانة ولا سحب مالك.»; dirty-check includes the chip; receipt unchanged (success is non-blocking, no undo — financial records never use undo).
- **Statement:** + collapsed «مصاريفي حسب تصنيفي» block (one top-level details; per-tag rows as `micro-finance-event` articles with a button toggle revealing per-event source rows linked to `?event=`); «غير مصنّف» group renders last, honestly; the revenue sentence now uses the service-derived total.
- **EventsLayer:** expanded row detail shows «تصنيفك: <label>» appended to the context line (template literal — the prefix carries no density cost).
- **Tools:** + module-states row «فحص سلامة مالي» (state «مفعّل» — derived truth: read-only, always available); density 28/34.
- **Finance:** + truth-section text-action doorway; five seats, FAB, and all existing layers untouched.

## 5. Arabic copy decisions (register rules applied)

- **Register split (grounded in the codebase):** colloquial Jordanian for questions/hints/empty states; MSA for effect/truth copy. The prompt's colloquial effect lines («الكاش بينقص») were adjusted to the established MSA register («ينقص الكاش X د.أ…»); the guided questions stayed colloquial as hints («من وين طلع المبلغ؟», «على شو اندفعت المصاري؟», «طبيعته: ثابت ولا بتغير؟»).
- **Vocabulary parity:** the wallet question reuses the sheet's exact label «وجهة الصرف» and option texts so one concept keeps one vocabulary.
- **Bidi safety:** the review card renders label:value rows (never inline equations); numerals and Latin ids always run through bdi/`MoneyValue`.
- **Honesty wordings preserved verbatim:** «قرار معلق، ليس خطأً» (MIC-9 WARN); «المتبقي غير موزّع»; «الحصة مؤجلة — لا تصير صفرًا ولا تدخل النتيجة»; «المال محفوظ ضمن الكاش غير الموزع».
- **Guidance lean set (two notes, not three):** the purchase note is a real action; the assets/loans note is one honest deferral line — per the two-priority rule.
- **Seed list tweak:** «أدوات» → «أدوات عمل» (avoids collision with the «أدواتي» seat concept).

## 6. States inventory (changed surfaces)

Every changed surface defines: empty (grouping block hidden; integrity not-run line; editor creation defaults), loading (disabled busy buttons; async select fill), validation (inline Arabic errors), offline (local-by-design, no sync claims), success (non-blocking notes/receipt/verdict), failure (honest messages, never false success; attribution failure keeps the record link), and correction (documented reverse/edit/restore via the events layer). No undo is offered on any financial record.

## 7. Compliance notes

- **Text-density:** three surfaces measured for the first time (ToolsIntegrity 32/32, FinancialEventEditor 138/138, Statement 89/89 — ratchet from day one); Tools 28/34; Finance's measured set unchanged at 181/181 — the new doorway sits inside a pre-existing counter blind spot over the truth section (documented as decision D-026; no cap change needed, counter fix deferred).
- **Design tokens:** all new UI uses existing micro-* classes and tokens; the only new CSS is the suggestion chip (44px touch target, 999px radius, 12px font, token colors, `aria-pressed` state), the fixed-height preview region, the draft/honesty banner, the review card, and the integrity status variants (existing warning/danger tokens + icons) — stylelint and the token guard pass.
- **Accessibility:** status never color-alone (word + icon + color); chips and toggles expose `aria-pressed`/`aria-expanded`; live regions (`role="status"`) on effect previews, receipts, and run results.

## 8. Live QA transcript (evidence)

Production build served locally and driven at 390×844 (headless Chromium):

1. First-use → wallet «الدرج» → zero start → foundation; five seats + centered FAB present.
2. Scenario A: FAB → «تسجيل مصروف» → 25.00 → wallet «الدرج» → chip «بنزين» (pressed) → effect «سينقص الكاش 25.00 د.أ من «الدرج» — مصروف مسجل لا يُعدّ ربحًا ولا يُخصم من دين، وبلا حركة أمانة ولا سحب مالك.» → save → receipt «سُجّل مصروف 25.00 د.أ — الكاش المسجل الآن -25.00 د.أ.» → «افتح السجل» → row detail «للمشروع · معروف · تصنيفك: بنزين».
3. Scenario B: editor → 300.00 → wallet → details layer (category «رواتب», nature «ثابت غالبًا», relationship project) → preview «ينقص الكاش 300.00 د.أ من «الدرج»…» + negatives + «التصنيف «رواتب» لقراءتك لاحقًا — لا يغيّر الأثر المالي» → save → **real attribution-failure honesty** (wallet balance zero): «حُفظ الحدث محليًا، لكن نسبته للمحفظة لم تتم: رصيد المحفظة لا يغطي هذا الصرف… — المال محفوظ ضمن الكاش غير الموزع حتى توزّعه بنفسك.» with «افتح السجل المحفوظ» + «ارجع إلى الوضع المالي».
4. Scenario C: shared + percentage 100 / 60 → review card rows (إجمالي المصروف المشترك 100.00 · حصة المشروع (60%) 60.00 · الباقي خارج حصة المشروع — بيت أو نشاط آخر 40.00 · المتبقي غير موزّع 0.00 د.أ — الحصة موزعة بالكامل) + preview showing the derived 60.00.
5. Scenario E: payable editor shows «بعد الحفظ:» (no cash change now).
6. Integrity: run → «سليم — الأرقام متسقة» · «أُجري الفحص 03/09/2026» · five checks سليم.
7. Finance doorway present; statement grouping expands to رواتب 300.00 + بنزين 25.00 with sources.

**Zero console errors and zero page errors throughout the session.**

## 9. Known UX limitations (deferred with reasons)

- The EventsLayer tag filter (would need a closed-vocabulary `?tag` parameter) is deferred.
- The OwnerWithdrawalEditor loan hint is deferred (its page is at the text-density cap; the expense-editor deferral line covers the guidance need for this group).
- The density counter's truth-section blind spot is documented (D-026) rather than fixed in this group, because fixing the parser changes the measured set materially and warrants its own decision.
- Real-device QA (haptics, IME behavior, PWA install flows on Android/iOS) remains within the repository's standing acceptance boundaries (Pilot-gated).
