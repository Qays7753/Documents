# 04 — RTL, Accessibility & Data-Visualization Trust Contract

Delivery: `micro-visual-product-concept-001` · Stage 1 · sub-agent 4 of 5 · 2026-09-06
Scope: binding rules for the Arabic-first, RTL-first, mobile-first concept — mirroring, bidi text, computed WCAG 2.x contrast, touch ergonomics, screen-reader meaning, honest charts, state truth matrix.

## 0. Verdict up front

Computation re-verifies the prior audit: white on `#cc785c` = **3.28:1** and on `#079fa0` = **3.24:1** fail normal text; white on `#964e33` = **6.11:1** and on `#057b7c` = **5.08:1** pass fully; white on `#b4613f` = **4.45:1** stays press-only. Two prior figures differ trivially (≈6.07→6.11, ≈4.42→4.45) — rounding only; documented, not reconciled. **Consequence: no filled button may carry body-size white Arabic on `#cc785c` or `#079fa0`** — filled actions use `#964e33`/`#057b7c`; `#cc785c`/`#079fa0` are icon/large-text/non-text-UI colors.

## 1. RTL composition rules

### 1.1 Mirror / do-not-mirror

| Element | Rule | Notes |
|---|---|---|
| Page & row layout | Mirror | Leading = right, trailing = left; set `dir="rtl"`, never `row-reverse` (breaks SR order). |
| Chevron (drill-in) | Mirror | Points **left** (direction of travel). |
| Back arrow | Mirror | Points **right** toward the start; label «رجوع». |
| Progress / steppers | Mirror | Fill starts right, grows leftward; step 1 rightmost. |
| Swipe-to-act | Mirror | Trailing actions revealed on the **left** by dragging rightward; destructive at the far-left edge. |
| Media, photos, logos, clocks | **No mirror** | Fixed identity, LTR semantics; playback per platform convention. |
| Time-series axis | Mirror deliberately | Oldest day rightmost, newest left; value axis right; horizontal bars grow leftward from the right baseline; caption states this. |

### 1.2 Mixed-direction text (bidi contract)

| Case | Rule |
|---|---|
| Amounts in sentences | Wrap the numeric token «1,245.50 د.أ» in a directional isolate (`dir="ltr"` + `unicode-bidi: isolate`, or `U+2066…U+2069`) so the run never re-orders against neighboring Arabic. |
| JOD placement | Currency word **after** the digits logically (visually left of them), NBSP-joined: `1,245.50 د.أ`; in amount fields it anchors at the field's left edge. Never floating, never «د.أ 1,245.50». |
| Dates, phones, IDs | DD/MM/YYYY in one LTR isolate (never renders YYYY/MM/DD); day-first is the Arabic convention. Phones/IBAN: LTR isolate, groups as written; digits never transliterated. |
| Trailing punctuation | A Latin/digit run at sentence end can drag the period to the wrong side — end the sentence inside the Arabic run, or isolate it, so «.» stays with the Arabic clause. |
| Buttons | Arabic-only labels; a trailing Latin token flips the visual start. |

### 1.3 Long Arabic text & numerals

| Rule | Value |
|---|---|
| Line-height | 1.6–1.8 for Arabic body (diacritics need room); ≥1.5 in dense finance rows. |
| Business names | List row: 1 line, ellipsis «…», full name in accessible name/detail header; detail header max 2 lines; never below 15px. |
| Alignment | Right (start); **never justify** Arabic on mobile (kashida/rivers); never center multi-line body. |
| Numerals | **Western 0–9 with `tabular-nums`.** Why: the verified JOD contract (`1,245.50 د.أ`) is digit-native; Jordanian invoices/receipts the owner already reads use Western digits; one numeral system everywhere keeps scanning predictable; tabular figures align decimal points. «د.أ» hangs outside the digit column, never inside it. |

## 2. Computed contrast audit (WCAG 2.x, Python)

Thresholds: normal ≥4.5 · large ≥3.0 (≥24px / ≥18.66px bold) · UI ≥3.0.

| Foreground on background | Ratio | Norm 4.5 | Large 3.0 | UI 3.0 | Permitted roles |
|---|---|---|---|---|---|
| `#ffffff` on `#cc785c` | **3.28** | FAIL | PASS | PASS | Large text, icons, non-text UI on brand fill |
| `#ffffff` on `#964e33` | **6.11** | PASS | PASS | PASS | Primary filled button label (light) |
| `#ffffff` on `#b4613f` | **4.45** | FAIL | PASS | PASS | **Press state only** (transient) |
| `#ffffff` on `#079fa0` | **3.24** | FAIL | PASS | PASS | Large text, icons, non-text UI on accent fill |
| `#ffffff` on `#057b7c` | **5.08** | PASS | PASS | PASS | Accent filled buttons, links, active tabs |
| `#964e33` on `#f4e4db` / `#057b7c` on `#e3f5f5` | **4.94 / 4.51** | PASS | PASS | PASS | Text on brand-soft / accent-soft chips & cards |
| `#d59172` / `#5ec0c1` / `#8fd5d6` on `#332d27` | **5.26 / 6.33 / 8.19** | PASS | PASS | PASS | Brand & accent text/UI on dark soft surface |
| `#1f1a17` / `#5c5148` on `#faf7f4` (proposed light ink, muted) | **16.15 / 7.22** | PASS | PASS | PASS | Body ink / secondary text & captions |
| `#f1e9e3` / `#b9aca2` on `#191512` (proposed dark ink, muted) | **15.13 / 8.20** | PASS | PASS | PASS | Body ink / secondary text, dark |
| `#1f1a17` on `#f4e4db` / `#e3f5f5`; `#f1e9e3` on `#332d27` / `#2a2521` | **13.93 / 15.30 / 11.33 / 12.64** | PASS | PASS | PASS | Ink on soft & raised surfaces |
| `#cc785c` / `#079fa0` on `#faf7f4`; `#d59172` on `#191512` | **3.07 / 3.04 / 7.02** | FAIL/PASS | PASS | PASS | Icons ≥3.0 only on light canvas; brand accent text OK on dark canvas |

**Conclusion (binding):** light filled buttons = `#964e33` bg + white label (6.11); `#cc785c` fill only behind large text, icons or non-text UI, with `#b4613f` **only** as the transient pressed state. Accent mirrors this: filled accent actions use `#057b7c`; `#079fa0` is icon/large-text/UI-only. Chip text uses the text-on-soft pairs (all ≥4.51). Body copy always uses ink pairs (≥7.2). Dark theme permits all brand/accent tokens as text on `#332d27`.

## 3. Touch & ergonomics

| Rule | Value |
|---|---|
| Primary targets | **48×48px** recommended; **44×44px absolute floor**. |
| Finance rows & spacing | Rows ≥56px, **64px** amount rows (name+value+state chip); ≥8px between adjacent targets, **12px** in dense lists; inline links padded to 44px. |
| Five-seat shell | 390px ÷ 5 ≈ 78px/seat — safely ≥48px; stacked icon+label, 8px above the gesture bar. |
| Thumb zone (RTL) | Primary CTA: full-width bottom bar, or anchored to the **start (right)**; secondary/destructive to the left. «مشروعي الآن» sits rightmost, under the right-thumb arc. Effect-preview «تنفيذ» sits bottom-start; «تراجع موثق» stays a full 48px row above it, never a corner icon. |

## 4. Accessible names & screen-reader meaning

| Surface | Rule |
|---|---|
| Icon-only buttons | Arabic `aria-label` with product vocabulary («تراجع موثق», «حذف»), never tool names. |
| Amount rows | Announcement order: **label → value+currency → state → period**: «صافي المركز، 1,245.50 دينار أردني، محدّث، هذه الفترة». Unknown announces «قيمة غير محددة بعد» — the SR must never hear «صفر». |
| State chips | Always **text + icon + shape/pattern** (dashed border = estimated; hatching = pending/syncing; «!» = conflict); color is never the sole cue. |
| Focus order | DOM order = visual RTL order (start = right first); dialogs trap and restore focus. |
| Live regions | Completion is **polite and quiet**: one `aria-live="polite"` message «تمت المزامنة — القيم محدثة»; conflicts use `role="alert"`; silent while the owner types. |
| Charts | `role="img"`; accessible name = question + one-sentence answer (§5); text summary as fallback. |

## 5. Data visualization contract

Every chart answers one real owner question, and names its **period**, **unit (JOD)** and **source state**.

| # | Form | Owner question | Honesty rules |
|---|---|---|---|
| 1 | 14-day cash in/out columns (oldest right → newest left) | Where did cash go these two weeks? | Missing day = empty slot + «لا توجد عمليات في هذا اليوم»; offline days hatched «غير مزامَن بعد»; never interpolated |
| 2 | Receivables aging buckets (horizontal bars: current / 1–30 / 31–60 / +60) | Who owes me, and how old is it? | Bars grow leftward from the right baseline; caption «طول الشريط = نسبة من أكبر قيمة» |
| 3 | Payables due buckets (same form, accent color) | What do I owe, and when? | Same caption; unknown totals show «قيمة غير محددة بعد», never 0.00 |
| 4 | Position delta breakdown (waterfall: opening → in/out groups → closing) | What changed and why? | Max 5 segments; non-cash steps labeled «غير نقدي: لا يدخل نتيجة الفترة»; unknown segment hatched |
| 5 | Expense-share stacked bar (top 4 categories + «أخرى») | Where do expenses go? | Verified precedent «طول الشريط = نسبة من أكبر قيمة» (S8); shares <3% merged, never exploded |

**Rejected forms (never ship):** 3D/perspective charts, dual-axis, radial gauges, animated counters, pies >5 slices, sparklines without period/unit.

**Standing rules:** «د.أ» on every value axis and tooltip; period in the title (DD/MM/YYYY range); source-state chip beside the title; one-sentence interpretation under the figure doubles as its accessible description; RTL geometry per §1.1.

## 6. State truth matrix

| State | Visual (never color alone) | Text — Arabic (English) | Where used | Must NEVER happen |
|---|---|---|---|---|
| Unknown | Dashed-border chip, «؟» glyph | «قيمة غير محددة بعد» / «قيمة الهدر غير معروفة بعد» (value not determined yet) | Unknown-cost movements, waste value | Rendered as `0.00` or any confident number |
| Estimated | «~» glyph, dashed underline | «تقديري» (estimated) | Pre-confirmation previews | Styled as synced; entering totals |
| Pending | Clock glyph, hatched stripe | «قيد الانتظار» (pending) | Awaiting confirmation/receipt | Counted as final in the period result |
| Offline | Cloud-off glyph chip | «غير متصل» (offline) | No connectivity | Silent queueing, no banner |
| Syncing | Rotating-arrows glyph | «جارٍ المزامنة» (syncing) | During upload/download | Blocking the owner's editing |
| Synced | Quiet check chip | «محدّث» (synced) | After successful sync | Celebration; implying bank verification |
| Conflict | «!» glyph, `role="alert"`, effect-preview box | «تعارض بحاجة لمراجعتك» (conflict needs your review) | Diverging local/remote edits | Auto-resolution or silent overwrite of either side |

## 7. Sources & limitations

Prior audit re-verified computationally (§2); rounding documented in §0. Copy precedents (verified repo evidence): honest-unknown register (S6/S7), non-cash disclaimer (S7), bar-proportion caption (S8), five-seat shell (S7). The S2/S3/S4 absences do not affect this contract.
