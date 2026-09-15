# User Journey Review — Agent 04 (User Viewpoint & Accessibility)

Run: `20260908T133347Z-352b` · Task `2-d` · Artifact: review framework to be executed against the built library (Task 3).
Persona: Jordanian small-business owner (Irbid stationery shop), phone-only, Arabic-first RTL, one hand busy, skeptical of "fancy" software, trusts paper receipts and visible numbers.

---

## How to read this document

Each journey is written in second person, as the owner, because the final library must be judged from inside the owner's day — not from inside the component code. For every journey you get: the step-by-step expectation, the **3-second first-glance test** (the single cheapest abandonment predictor we have), the states that may appear (offline local save, conflict, failed), the acceptable recovery path, and the trust wording (concise, action-oriented Arabic; infrastructure jargon is never allowed in primary cards). Anything that breaks a journey here is a build-blocker for Task 3, regardless of how polished the component looks in isolation.

---

## Journey A — Morning check: "كم رصيد الصندوق اليوم؟ وما الذي يحتاج متابعتي؟"

It is 07:42. You are opening the shop, holding the shutter keys in one hand and your phone in the other. You open the app for one reason: know the cash, know what needs you, and get back to work.

**Steps and expectations.**

1. App opens directly on the dashboard. No splash animation, no onboarding wall, no fake system status bar. First paint shows content or skeletons — never a blank canvas.
2. **Before any scroll at 390px** you must see: the PrimaryValueBlock with the label "رصيد الصندوق اليوم" and the value `3,047.250` in English digits (bidi `dir="ltr"`), currency `د.أ` (never "JOD"), 32px strong ink; a quiet update line "آخر تحديث اليوم 07:30" in ink-muted 14px; at least two MetricRows (e.g. "مستحقات متأخرة — 1,312.400 د.أ · عميلان" as a warning row, "مبيعات الأمس — 850.750 د.أ" as a plain row); and ≥28px of the QuickActionRail peeking above the bottom navigation.
3. Tapping the overdue row leads to the customer list filtered to overdue — one tap, no dead ends.

**The 3-second first-glance test.** Screenshot the fully painted screen at 390px, hand it to someone who has never seen the app, and ask: "كم رصيد الصندوق؟ وشو يحتاج متابعته؟" They must answer both, exactly, within 3 seconds. If the balance is below the fold, competes with a second big number, or is mid count-up animation, the screen fails.

**States that may appear.**

- *Fresh load (network slow):* value skeleton (a single block-shaped skeleton, not a spinner wall), ≤1s before content or cached data appears.
- *Offline:* show the cached value immediately with "آخر تحديث أمس 21:15" plus a quiet info-toned line "بيانات محفوظة على الجهاز" — informational, never a red alarm, never a full-screen blocker.
- *Unknown (no data yet):* the value slot shows "غير متوفر" with an info icon. **Unknown must never render as `0.000`** — a false zero balance is a trust-destroying, potentially business-damaging error for this persona.
- *Failed refresh:* one automatic retry, then a small inline action "أعد المحاولة". The previous value stays on screen.

**Acceptable recovery.** Stale-but-labeled data is always better than empty. The owner decides what to do with a timestamp; the app must not decide for them by hiding the number.

**Trust wording (do / don't).**

| DO (primary cards) | DON'T (ever, user-facing) |
|---|---|
| "رصيد الصندوق اليوم 3,047.250 د.أ" | "Cash balance: JOD 3,047.250" |
| "آخر تحديث اليوم 07:30" | "Last sync: 07:30 (OK)" |
| "تعذّر التحديث — أعد المحاولة" | "خطأ في المزامنة مع الخادم (500)" |
| "بيانات محفوظة على الجهاز وستُرسل تلقائيًا" | "Queue flushed to persistence layer" |

**Abandonment triggers (any one is a fail):** spinner-only screen longer than 3s; balance that counts up from zero; `0.000` shown for unknown; the balance smaller than a decorative number near it; a date that reads `2026/09/08`; any English UI string in the primary cards.

---

## Journey B — Collect a debt from خالد الحوراني and get PROOF it was recorded

خالد owes 1,312.400 د.أ. He hands you 150.000 cash at the counter. You need the app to (1) record it in seconds, (2) prove it was recorded, and (3) show what remains — because with خالد, the remaining balance is the whole relationship.

**Steps and expectations.**

1. From the morning overdue row (or the customers tab), you tap "خالد الحوراني". The row shows his name, "مستحق 1,312.400 د.أ" and an overdue chip (warning tint + label + icon — never color alone).
2. A bottom sheet opens: title "تسجيل دفعة", the owed amount visible at top, an amount field with the English-digit keypad, and a primary "تسجيل الدفعة" button (48px, bottom of the sheet, thumb zone). A quick chip "المبلغ كامل" is offered for full settlement.
3. You type `150.000`. The display renders as an LTR cluster `150.000` with `د.أ` to its left; grouping comma only past thousands; exactly 3 decimals.
4. You press "تسجيل الدفعة". **Loading:** the button swaps to a spinner + "جارٍ التسجيل…" at the same width and position (no layout jump); the sheet does not close; double-taps are absorbed (button disabled while pending).
5. **Completion — quiet, no count-up:** the button area resolves to a check + "تم تسجيل الدفعة". Directly under it, the proof row: "رقم القيد 0042 · 09:41". In place, the numbers update: "المتبقي على خالد 1,162.400 د.أ" and, after the sheet closes, the dashboard cash value is already 3,197.250 د.أ — it changed when you saved, not gradually.
6. **Proof persists.** The entry is navigable later from "سجل الحركة" as a receipt-style record (customer, amount, remaining, entry ID, timestamp). A toast alone is NOT proof — it must never be the only confirmation.

**The 3-second first-glance test (completion state).** On the completion screen, ask: "هل انحفظت؟ وشو باقي عليه؟" Both answers (yes — check + entry ID; 1,162.400) must be readable in 3 seconds without tapping anything.

**States and acceptable recovery.**

- *Offline local save:* completion shows "تم الحفظ على الجهاز — سيُرسل عند رجوع الاتصال" with a small info "معلّق" badge on the record. The owner can walk away; the record exists locally with its entry ID.
- *Conflict (the debt changed on another device):* a dialog states the fact and asks: "تغيّر المبلغ المستحق على خالد إلى 1,250.000 د.أ. هل تريد تسجيل الدفعة 150.000 كما هي؟" with explicit "تسجيل" / "إلغاء" choices. Never a silent overwrite, never a crash back to the form.
- *Failed:* exactly one automatic retry, then "تعذّر التسجيل" with a clear "أعد المحاولة" action. The typed amount and any note survive — re-typing 150.000 by hand is the kind of friction that makes this persona go back to a notebook.
- *Double-submit:* pressing the button twice must produce exactly one payment. Money errors are the unforgivable category.

**Trust wording.** Concrete nouns and timestamps: "تم تسجيل الدفعة", "رقم القيد 0042", "المتبقي 1,162.400 د.أ". No "تمت مزامنة البيانات بنجاح", no spinner-language ("يرجى الانتظار"), no exclamation marks.

**Abandonment triggers:** completion state indistinguishable from loading; toast-only confirmation; sheet closes but dashboard value unchanged; value counts up; amount re-rendered as `000.150` or with Arabic-Indic digits anywhere.

---

## Journey C — Record a cash expense of 431.100 د.أ with the amount keypad

You paid 431.100 cash for restock boxes. You are standing, one thumb free, and you want this out of your head in under 20 seconds.

**Steps and expectations.**

1. From the QuickActionRail you tap the "مصروف" tile (88×92 target, in the bottom 60% of the screen — one-hand reachable).
2. A bottom sheet opens: "تسجيل مصروف نقدي". **Visible before scroll at 390px:** the amount display (sunken field, large, English digits, exactly 3 decimals, `د.أ` as a static label outside the number cluster), single-select category chips ("قرطاسية", "شحن", "مواصلات", "أخرى"), and the top of the keypad. The save button sits under the keypad or pinned to the sheet bottom.
3. **Keypad contract:** ASCII digits 0–9 only; entry fills fils right-to-left so typing `431100` displays `431.100`; a backspace key; every key ≥48px tall with ≥8px gaps; press feedback = 8% ink overlay within 80ms; the live display wraps, never clips, never shows Arabic-Indic digits (٤٣١ is forbidden in values).
4. The display renders `431.100` as an isolated LTR cluster with `د.أ` to its left. Copying/pasting a figure from an SMS must land the same way.
5. You tap "حفظ المصروف". Loading → completion as in Journey B: check + "تم تسجيل المصروف — 431.100 د.أ" and the cash line updates in place: "رصيد الصندوق الآن 2,766.150 د.أ" (immediately, no count-up).
6. Validation is advisory, not blocking: an amount larger than the cash balance shows a warning line "المبلغ أكبر من رصيد الصندوق الحالي" with a confirm dialog on save — the owner may genuinely have paid from another pocket.

**The 3-second first-glance test.** On the opened sheet: "وين أكتب المبلغ؟ وشو زر الحفظ؟" Both must be identifiable in 3 seconds — the amount field is the visually dominant input, the save button is the only filled brand action.

**States and acceptable recovery.** Offline → local save with the same "معلّق" pattern as Journey B; failed → one retry then "تعذّر الحفظ" with amount and category preserved; validation → warning tint + icon + text (never color alone).

**Trust wording.** "تم تسجيل المصروف — 431.100 د.أ من الصندوق". The sentence ties the amount to the cash drawer — that causal link is what makes the owner believe the number later.

**Abandonment triggers:** digits render RTL or reversed (`100.431`); the decimal point drifts (4311.00 / 431.1); keypad keys under 48px; the sheet requires two-handed reach; balance doesn't move after saving; any Arabic-Indic digit appears in the amount.

---

## Cross-journey wording rules

1. Primary cards carry **facts and actions** ("رصيد الصندوق اليوم", "سجّل الدفعة"), never system vocabulary (sync, cache, API, token, queue). Infrastructure may only appear in quiet footnotes when a record is pending: "محفوظ على الجهاز وسيُرسل تلقائيًا".
2. Every money string: English digits, 3-decimal fils, thousands comma, `د.أ` currency, `<bdi dir="ltr">` isolation, dates as DD/MM/YYYY.
3. Completion is quiet: check + "تم الحفظ" family + immediate value update + persistent proof. Never a count-up, never a toast as the only evidence, never an auto-dismiss faster than the eye can read.
4. Errors name the action that failed and the action to fix it: "تعذّر الحفظ — أعد المحاولة". One automatic retry maximum; after that, the human decides.
