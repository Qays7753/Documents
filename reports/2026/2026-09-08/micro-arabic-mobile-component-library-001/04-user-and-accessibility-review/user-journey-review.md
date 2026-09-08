# User Journey Review — Walking the Proposed Design as أبو محمد

Agent 04 · Task 3 · Run `20260908T133450Z-16d11`. Reviewed: all Agent 01–03 artifacts. Method: each journey is walked through the **proposed composition and contracts only** at 320/360/390/430px, RTL primary, 100% and 200% text scale, one-handed. Every failure carries a concrete fix for Agent 05. Values use English digits, `د.أ`, `DD/MM/YYYY`.

---

## Journey A — The 2-second morning glance (07:40, between customers)

One thumb, three looks: the big number, the warning, the button.

**What works.** The hierarchy serves the glance path exactly: the top zone (`مخبز أبو محمد` / `الثلاثاء 08/09/2026`) orients cheaply; `نقد اليوم 1,284.50 د.أ حتى 14:20` sits on the canvas — a fact, not a widget — at 32px/600 tabular digits; the rail puts `إضافة بيع` first (rightmost, the single tinted tile); the `MetricGroup` answers the flow question with sign-led rows (`+210.00` colored, `-92.50` plain ink, minus leading); `متابعة اليوم` opens with the warning row (`شركة التوصيل السريع — بانتظار التحويل — منذ 05/09/2026 — 142.00 د.أ`) carrying clock icon + word + since-date, so urgency survives without color. Unknown is `—`, never `0`; the pending 142.00 is absent from cash — consistency he can verify against his pocket.

**What fails or risks failing.**
1. **At 320px the warning may fall below the fold.** Agent 01 budgets ~700px of pre-fold content at 390px with 40px top breathing and 32px of air above the block; at 320px content grows (wrapping) while the air stays. Glance element #2 ("what needs me") can be cut, leaving the 142.00 hidden behind a scroll. **Fix (Agent 05):** JS-measure the fold at all four widths; if the warning row is cut at 320px, step top breathing 40→32 and pre-block air 32→24 (on-scale, 320px only) and re-measure. Never reorder sections — the order *is* the glance path.
2. **State-line and qualifier Arabic at 13px.** The `--with-state` line (`بانتظار تحويل…`) and `حتى 14:20` are proposed at 13px while SPEC §6.4 sets a 14px Arabic floor — and these are words he must read. **Fix:** adopt the Agent 04 ruling (a11y report §7): Arabic-word qualifiers and state lines at 14px; 13px reserved for numeric/Latin runs and the SPEC-mandated rail labels.
3. **Stale morning cash.** A cached value shows `آخر تحديث 12:40` — good — but nothing marks "yesterday's number" when he is deciding whether to buy flour with it. **Fix:** the stale qualifier must *lead* with `آخر تحديث` (already in the copy bank); retry lives in the existing error line — no new component.

---

## Journey B — Recording a cash sale mid-rush, one-handed (12:15)

A customer pays 96.00 in cash; the tray is in his left hand; he has seconds.

**What works.** The rail tile is an 88×92px target — double the 44px minimum — in the comfortable stretch band; the sheet opens in 240ms with the amount field focused (`dir="ltr"`, `0.00` placeholder never committed), `نقدي | آجل` already on `نقدي`, date defaulting to `اليوم` so no date touch is needed; the 48px full-width `brand-ink` CTA is bottom-pinned in the thumb zone; loading keeps the footprint; completion is inline quiet proof (check + `تم`), never a toast; `مبيعات اليوم` and `نقد اليوم` update immediately with no count-up; the live region announces `تم تسجيل البيع`. The dirty-guard dialog (`تجاهل التغييرات؟`) protects a half-typed entry — exactly right for money.

**What fails or risks failing.**
1. **The sheet may exit before he sees the proof.** The task map says "CTA → loading → quiet completion → sheet exits 180ms"; only the button contract mentions a ≥1.5s settle. His eyes are on the customer; an exit 180ms later makes the proof invisible. **Fix (Agent 05):** the completion state dwells ≥1.5s before the sheet exits (or exits on his next tap), and the announcement fires at completion, not at dismissal.
2. **All dismissal routes must pass through the dirty guard.** The contract lists scrim tap, drag, Escape, and back gesture; the guard is described only generically. **Fix:** state explicitly that all four routes route a dirty sheet through `تجاهل التغييرات؟` — none may silently discard.
3. **Error/helper text at 13px** (`أدخل مبلغًا أكبر من صفر`) is action-required Arabic. **Fix:** 14px per the ruling; errors also use `role="alert"` + `aria-describedby`.
4. **Conflict path (double-tap save).** `عملية مشابهة موجودة` with `عرض الموجودة` / `تسجيلها مع ذلك` preserves records — correct; keep both as ≥44px quiet buttons (not 28px chips).

---

## Journey C — Recovering a failed entry (recorded in the basement, no signal)

He recorded a 96.00 collection downstairs; the send failed; he is back with signal.

**What works.** SPEC §6.12 is honored: automatic retries stop after the first failure; the failed row shows `فشل الإرسال` with a real, focusable `إعادة المحاولة` button; the record stays locally saved; the completed flip is inline (check + `تم`, 120ms crossfade); conflict resolution keeps both candidates. This is the strongest part of the proposal.

**What fails or risks failing.**
1. **State-model ambiguity between offline-save and failed.** The copy bank has `محفوظ على الجهاز` + `يُرسل عند عودة الاتصال` AND `فشل الإرسال` + `إعادة المحاولة`. If an offline-saved entry's auto-send-on-reconnect fails, the row could show both stories. He needs one answer: "is it saved, and what do I press?" **Fix (Agent 05):** one explicit state machine in the contracts: no connection at save → `offline` (reassurance first); send attempted and failed → `failed` (retry first); succeeded → `completed`. A row never shows two states; offline→failed is a transition, not an overlay.
2. **Retry placement vs the thumb.** The inline retry sits at the row's inline-end — visual **left** in RTL — mid-screen: a right-thumb stretch on the far side. **Fix:** keep the inline retry for glance use, but make the row tap open the detail sheet with `إعادة المحاولة` bottom-pinned (thumb zone), honoring Agent 01's own rule that failed-row retries belong in the natural-rest band.
3. **Redundant entry on retry (WCAG 2.2 §3.3.7).** Reopening the failed entry must repopulate the amount from the locally saved record — never re-typing. **Fix:** the sheet hydrates from the saved record; `تجاهل` may only discard a *new* edit, never the underlying entry.
4. **Announcement parity.** Failure uses `role="alert"`, completion `role="status"`, both at state change (checklist row).

---

## Journey D — Who owes what (19:50, before closing the till)

**What works.** The single comparison pair (`ذمم العملاء 1,175.00 د.أ عند 4 عملاء` | `ذمم المورّدين 640.00 د.أ مؤسسة الشرق`) answers one question in one glance; both tiles are ≥44px targets; taps drill into detail views anchored by `PrimaryValueBlock` with `تحصيل دفعة` / `تسجيل دفعة` as sheet CTAs; true zero renders `0.00 د.أ` at full weight; unavailable renders `—` + `غير متاح حاليًا` — the rule that stops him from waiving a real debt.

**What fails or risks failing.**
1. **Direction confusion.** Both values are unsigned neutral ink and both labels share the root `ذمم`; a 2-second glance can misread which number is money-in. **Fix (copy only, locked copy bank):** label the pair `مستحق لك` / `مستحق عليك`, keeping `ذمم العملاء` / `ذمم المورّدين` as 13px numeric metadata qualifiers or dropping them.
2. **The warning dot is a color-only signal.** The CompactTile contract permits "a tiny warning dot" — a bare dot carries meaning by color/position alone and fails the non-color rule. **Fix:** drop it (the `متابعة اليوم` count already carries urgency) or give it an accessible name (`يوجد متأخرات`) — never ship it silent.
3. **Mixed availability.** The pair synchronizes loading, but one source can be down while the other is live. **Fix:** loading synchronized; unavailable per-tile (`—` + reason + `إعادة المحاولة`) — a fresh-looking stale number is the worse failure. One clarifying line in the contract.
4. **Below the fold by design** — acceptable here (not the morning glance); no change requested.

---

## Handoff to Agent 05 (fix list)

1. Measure the 320px fold; compress top breathing 40→32 / air 32→24 at 320px only if the warning row is cut.
2. Completion dwell ≥1.5s before sheet exit; announce at state change.
3. Dirty-guard routing for scrim tap, drag, Escape, and back on edited sheets.
4. One offline→failed→completed state machine; never two states per row.
5. Failed-row retry also bottom-pinned in the detail sheet; sheet hydrates from the saved record.
6. Pair labels `مستحق لك` / `مستحق عليك`; no silent warning dot.
7. 14px for Arabic-word qualifiers, state lines, errors/helpers (ruling in the a11y report); 13px stays for numeric runs and rail labels.
