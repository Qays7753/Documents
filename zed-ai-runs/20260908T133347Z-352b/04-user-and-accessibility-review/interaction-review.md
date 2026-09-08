# Interaction Review — Agent 04 (Interaction Contracts & Anti-Patterns)

Run: `20260908T133347Z-352b` · Task `2-d` · These are the interaction contracts the final library (Task 3) must honor. Each contract states the numbers, the expected behavior, and the objective PASS criterion the coordinator will test in Task 4. Anything not listed here defaults to "no invented behavior": if a component has no defined contract, it must behave like the platform default, not like a demo.

These contracts exist because the persona (busy owner, one-hand use, money data) interacts under load: standing, in a hurry, trusting the numbers on screen. Interaction feedback must therefore be **fast, quiet, and never lie about state**. A 300ms spring animation is not "delight" here — it is a delay between the owner's thumb and the truth about their cash. Every contract below optimizes for the moment of doubt: "هل انحفظت؟"

---

## 1. Press (touch/pointer feedback)

- **Contract:** on `pointerdown`, an overlay of `#1F1E1D` at 8% alpha appears over the target within **80ms**; on `pointerup`/`pointercancel` it is removed with a fade ≤120ms. The overlay is a composited layer — it must not replace the element's background token (checked: ink on the pressed composite `#EDEDED` keeps ≥10.9:1, and white on pressed brand-ink `#8C4A31` keeps 6.69:1, so text stays AA during press).
- **Scope:** every interactive element — buttons, list rows, tiles, rail tiles, nav tabs, keypad keys, chips. Keyboard `:active` equivalent via Enter/Space on focus.
- **PASS criterion:** screen-record a press at 60fps; the overlay is visible in the frame at or before 80ms after pointerdown; label/number contrast never drops below 4.5:1 mid-press; no scale, shadow, or motion change accompanies the overlay (press is color, not movement).

## 2. Focus-visible (keyboard + switch access)

- **Contract:** every interactive element is keyboard reachable (Tab/Shift-Tab, Enter/Space activate; arrow keys move within the rail and nav); focus order equals DOM order equals logical reading order (in RTL, the first focusable is the topmost/rightmost). The ring: **2px `ink-strong` outline, 2px offset**, shown **only on `:focus-visible`** (mouse clicks must not paint rings). Ring contrast vs any background it can appear on is ≥3:1 (ink-strong on surface = 16.64:1; on canvas 15.80:1; on tints ≥12:1 — computed, always passing).
- **PASS criterion:** Tab through a full composition: 100% of interactive elements receive a visible ring; no element is skipped (interactive-but-unfocusable = fail); ring never clips outside the viewport; focus is never hidden by the bottom sheet's scrim (sheet traps focus, see §6).

## 3. Loading

- **Contract:** button loading = in-place spinner (16px, same color token as the button's content) + label swap to a progress phrase ("جارٍ الحفظ…"); the button keeps its exact width and height — **zero layout shift (≤1px)**. List/screen loading = **skeletons, exactly 3 rows** in the shape of the real rows (MetricRow-shaped skeletons for metric groups), not generic gray bars. No skeleton shimmer unless motion is allowed; under reduced motion the skeleton is static.
- **PASS criterion:** toggle a demo "loading" state; measure bounding boxes before/during: identical ±1px; screenshot: 3 skeletons, matching final geometry; no full-screen spinners anywhere in the library.

## 4. Completion (quiet completion)

- **Contract:** success resolves as **check icon + "تم الحفظ"-family label** in the place of the action (button or row), held for ≥1200ms (or until next interaction); the affected value (cash balance, remaining debt) updates **immediately and discretely** — the new number simply is there. **No count-up, no odometer, no tween on financial values, ever.** Proof is persistent (record/entry ID), never toast-only (see anti-pattern A1).
- **PASS criterion:** trigger the save demo; frames show the old number then the new number with no intermediate interpolated values (screen-record and step frames); a check glyph appears; the completion text is Arabic, action-confirmed ("تم تسجيل الدفعة"), not system-confirmed ("تمت المزامنة").

## 5. Error recovery

- **Contract:** at most **one automatic retry**, then a visible, specific failure state with a clear retry action ("تعذّر الحفظ — أعد المحاولة"); user input (amount, note, category) is preserved verbatim across the retry; the retry action target is ≥44px and in the same visual region as the failed action. Error text pairs danger tint/icon/word — never color alone. Money is never silently dropped: an unsaved record either exists locally with a "معلّق" badge or the user explicitly cancelled.
- **PASS criterion:** run the failure demo: exactly 1 auto attempt, then error UI; cancel and reopen the sheet — typed amount still present; after retry succeeds, completion per §4.

## 6. Sheet (bottom sheet)

- **Contract:** opens in **240ms**, closes in **180ms** (translateY, ease-out — no overshoot); scrim = `#1F1E1D` at **45%** fading in/out; dismiss by **swipe/drag down** (≥40px travel commits, <40px springs back — spring only on the *cancel* gesture, ≤150ms), **Esc key**, and **scrim tap** (never a tiny × as the only close). Focus moves into the sheet on open (first meaningful control), is trapped inside while open, and **returns to the trigger** on close. The sheet's primary action is a 48px button pinned in the thumb zone; the sheet never scrolls its primary action out of view.
- **PASS criterion:** time the open/close animations from video frames (240ms±40 / 180ms±40); test all three dismissal paths; Tab beyond the sheet's last control — focus stays inside; after close, focus is back on the tile that opened it; drag 30px and release — sheet returns fully.

## 7. Dialog (including destructive)

- **Contract:** opens in **160ms**, closes in **120ms** (scale 0.96→1 or fade — no slide); scrim 45%. Destructive confirm pattern: title states the consequence in plain Arabic ("سيُحذف القيد نهائيًا"), body names the object ("قيد رقم 0042 — دفعة خالح الحوراني 150.000 د.أ" style), the destructive button is **danger-filled with white text** (6.57:1, computed) and the safe action is a quiet secondary placed first in RTL reading order. Confirm is disabled while pending; no double-fire. Esc maps to the safe action, never to the destructive one.
- **PASS criterion:** trigger the delete demo; verify timings; press Esc → safe path; press Enter repeatedly on confirm → single deletion event; buttons: destructive = filled danger + white; cancel reachable without crossing the destructive target (hit zones ≥8px apart… ≥44px each).

## 8. Reduced motion (`prefers-reduced-motion: reduce`)

- **Contract:** all spatial animation (sheet slide, dialog scale, icon translation, skeleton shimmer) drops to **≤100ms opacity-only fades or instant state change**; state meaning is preserved by opacity, color, and label — e.g. sheet open state is still unmistakable because the scrim (45%) and layout change carry the meaning, not the motion. No parallax, no auto-playing loops, no shimmer.
- **PASS criterion:** enable reduced motion in the harness (`html { … }` + `@media (prefers-reduced-motion: reduce)` simulation); walk every interactive demo; each state transition is still perceivable in a static screenshot pair (before/after); no element moves on screen except crossfades.

---

## Anti-pattern rejection list (each is a build-blocker)

| # | Anti-pattern | Why it is rejected (persona + a11y) |
|---|---|---|
| A1 | **Toast-only proof** (save confirmation that exists only as a transient toast) | The owner's mental model is a receipt: proof must persist (entry ID + record). Toasts vanish before trust forms; screen-reader users may never hear them; they can't be re-read during a dispute with خالد. |
| A2 | **Count-up financial values** (balance animating 0→3,047.250) | Under time pressure, a mid-animation number is a wrong number (the 3-second test fails mid-count). Vestibular users get motion they didn't ask for. Numbers change discretely — like a ledger, not a slot machine. |
| A3 | **Fake system status bar / notch / battery** drawn by the web page | Impersonating OS chrome is deception; it breaks zoom and clipping math (the fake bar doesn't scale), and it will look wrong on the coordinator's device — the library must render only app-owned pixels. |
| A4 | **Page-wide slide transitions** between tabs/sections | Sliding whole pages implies spatial hierarchy that doesn't exist (tabs are siblings), costs 300ms+ per navigation, and violates reduced-motion budgets. Navigation swaps content instantly or with ≤120ms crossfade; only sheets (overlay surfaces) slide. |
| A5 | **Bounce / spring / overshoot physics** on any UI movement | Springs are wasted time between intent and result, and they never degrade gracefully under `prefers-reduced-motion`. Easing budget: ease-out family only; the single allowed spring-back is the sheet-cancel gesture (≤150ms, ≤40px). |
| A6 | **Color as the only status signal** (a row is "overdue" because it's orange) | 1 in 12 Jordanian men has a color-vision deficiency; sunlight on a phone screen washes color. Every semantic state pairs color with sign (+/−), word (وارد/صادر/متأخر), icon, or structure. |
| A7 | **"JOD" string or Arabic-Indic digits in user-facing values** | The persona writes د.أ and reads English digits in the ledger; mixing ٤٣١/431 breaks bidi isolation and the keypad contract; "JOD" is forbidden in every user-facing example. |
| A8 | **Paper-plane "send" icon** | The forbidden icon. It never mirrors correctly in RTL, it's Latin-tech slang for a cash-receipt culture, and the spec bans it outright. Send/save actions use Arabic text labels ("إرسال", "حفظ") with optional directional arrows that mirror per policy. |
| A9 | **Disabled look = only gray + no semantics** | ink-disabled (2.11:1) is intentionally below contrast; therefore disabled must also drop `pointer-events`, be announced as disabled, and never carry the only copy of critical info. |
| A10 | **Spinner walls / blocking splash on load** | Nothing between the owner and the balance. Skeletons and cached values render in the first paint; the only full-screen blocking surface is a modal dialog the user opened on purpose. |
