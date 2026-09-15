# 03 — HTML Review Guide

Artifact: `prototype/micro-visual-concept-review.html` — one self-contained file, no network, no dependencies. Open it in any modern browser (double-click or File → Open). Desktop or mobile both work; the artifact renders its own phone frame.

## 1. What you are looking at

Everything **inside the black phone frame is the simulated Micro product** in the recommended direction **A — «السجل الدافئ» / The Warm Ledger**. Everything **outside the frame is review chrome** (controls and notes) and is not part of the product design. Directions **B** and **C** are compact, real compositions of the rejected alternatives with the reason for rejection written under them.

## 2. The control set (outside the frame)

| Control | What to do with it |
|---|---|
| **Direction** | Switch between A (recommended), B and C (rejected previews). Screen-jump chips are disabled for B/C by design. |
| **Language / RTL** | «العربية RTL» is the default product language and direction. «English LTR» is a **verification mode** — it proves the layout mirrors correctly; it is not the localization deliverable. |
| **Theme** | Light and Dark use the fixed Terracotta values with a deliberate (not inverted) dark mapping. |
| **Motion** | Normal / Reduced. Reduced kills all transition and animation, mirroring both the in-product «تقليل الحركة» switch and `prefers-reduced-motion`. |
| **Width** | 320 / 360 / 390 / 430 — the four contracted portrait widths. Watch long Arabic business names truncate honestly at 320. |

## 3. Recommended route through direction A (≈ 8 minutes)

1. **Today (390, light, Arabic).** The hero truth block: one number that matters, today's delta, and «لماذا؟» for the explanation rows. Below it, «ما الذي يحتاج انتباهك اليوم؟» — three actionable rows with distinct states. Scroll: the **Top Focus Shell** condenses and keeps «المتاح» visible. The cash chart names its period, unit (JOD), source state, and carries the honesty caption; note the dashed empty slot for the missing day.
2. **Wait ~3 seconds on Today** — the offline banner slides in. Dismiss it.
3. **Financial Truth.** Available / owed to me / owed by me, deposits-as-obligation explanation, the position-change breakdown with source caption, and the **sync-conflict alert row** (an alert, not a quiet chip).
4. **سجّل (Quick Capture).** The **NumericSurface**: tap +1/+10/−1/−10 (hold to repeat), or drag horizontally on the number. Digits drift directionally; the surface never jitters. Fill any amount, then **حفظ العملية**: button shows a calm busy state, then quiet completion («تم الحفظ») and the row appears under «ما سُجّل اليوم». Note the effect-preview box for an uncollected sale.
5. **ليّ (Receivables).** Aging buckets grow from the right baseline (RTL-correct); the long business name truncates with ellipsis. Press **تحصيل** on any row: an **effect-preview sheet** states exactly what will change («وينخفض ليّ إلى 555.00 د.أ»), confirm → quiet completion, row becomes «محصّل».
6. **العمل (Orders).** Skeleton → rows. Status dots, «عربون — قيد الانتظار», «تم الاعتراف بالبيع» (completion-based recognition), «قيمة غير محددة» honest unknown. Search filters live; the filter button opens the **bottom sheet** (Esc / scrim / ✕ all close it).
7. **المشتريات.** The partial-receipt progress («قيمة مستلمة: 60.00 من 120.00 د.أ»), a supplier order with unknown price, a paid/synced row.
8. **إغلاق الصندوق.** Type a counted value (try «1,200.00») — the difference row appears, documented not silently adjusted. Confirm → quiet completion.
9. **أدواتي.** Vertical settings rows (no tile grid). The «تقليل الحركة» switch is wired to the same motion system as the review toggle.
10. **المساعد.** Tap a suggested question; the answer cites the same numbers as the surfaces (640.00 / 815.00 / 150.00 د.أ).
11. **Now verify, don't admire:** switch to **English LTR** (layout mirrors, spine moves to the left edge), **Dark** (deliberate luminance ladder, no inversion), **320 width** (long names truncate, nothing overflows), **Reduced motion** (all movement stops, all meaning survives — states are text+icon, never motion-only).
12. **Finally:** switch Direction to **B** and **C** to see, on real compositions, why the ledger won.

## 4. What "good" looks like (acceptance intuition)

- One dominant entry point per screen; bands answer owner questions in a fixed order.
- Terracotta never carries body-size white text; `#964e33` only on the primary action; press state is momentary.
- Money is always tabular, always with its state; unknown is never 0.00.
- Every gesture has a tap alternative; every state is readable without color or motion.

## 5. Known preview limitations

A non-exhaustive list: the simulation is front-end only (no persistence; save/collect/closing effects are visual demos); the English mode is a verification layer, not finalized localized copy; charts use representative demo data with one deliberately missing day; the assistant returns canned answers citing real surface numbers; swipe-on-row is represented by visible tap actions (full gesture wiring belongs to implementation); iOS/Android native safe-area insets are represented by the `env()` tokens but not device-tested.
