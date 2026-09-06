# 03 — HTML Review Guide

**Delivery:** `micro-visual-product-concept-002`
**Artifact:** `prototype/micro-visual-concept-review.html` (self-contained; open directly in any modern browser — Chrome, Edge, Firefox, or Safari; no server, no build step)
**Recommended direction:** **A — «دفتر هادئ» The Calm Ledger**
**Reading time:** 3 minutes before you open the file; plan 10–15 minutes for the review itself.

---

## 0. What this artifact is — and is not

It is a **working visual and interaction concept**: a real, interactive HTML simulation of the Micro product at 390×844 (switchable to 320/360/430) with the full recommended visual language applied — typography, ledger composition, surfaces, states, motion, charts, and the NumericSurface. Every control you see actually works.

It is **not** the production app, not a data layer, and not final navigation: demo writes are in-memory only, and screens other than the live figures hold the scenario snapshot (one coherent week, 06–12/09/2026, reconciled to the dinar: opening 82.50 + in 85.00 − out 22.50 = 145.00 available). Arabic web fonts load progressively from Google Fonts when online; with no network the system fallback renders (documented decision DSY-22: two-font path for the review, single-face decision at Stage 4).

---

## 1. The review console (outside the phone — by design)

Everything above and beside the phone is the **review console**: Mode (recommended concept / compare directions), Language (العربية RTL default · English LTR verification), Theme (light/dark — both ship complete), Motion (normal/reduced), and Width (320/360/390/430). Five demo buttons run complete behaviors inside the phone. Nothing inside the phone frame is a development control — the product frame stays product-real.

## 2. Recommended route (15 minutes)

**Stop 1 — Home «مشروعي الآن» (2 min).** The opening question, the 2px terracotta rule, today's rows with action words (سلّم / حصّل / أكمل), the ruled 2×2 facts grid (not cards) with «—» where the owner money is unrecorded, the locality truth line, and the quiet links row. One primary exists on the whole screen: the center «سجّل».

**Stop 2 — Finance «مالي» (2 min).** The 34px hero answers «وين الكاش؟» before anything else. Then the decision line (with the single contextual primary), the segmented wallet-composition row with the **hatched amanah segment** and its dual-truth sentence, the position grid, and the collapsed layers as quiet rows. Tap «قراءة الفترة» to reach the statement.

**Stop 3 — Statement «كشف الأسبوع» (2 min).** The paired-bar week chart: time flows **right-to-left**, Thursday 10/09 is labeled as the peak, and **Friday 11/09 renders a gap — not a zero bar** — with the footnote. Every chart carries period, unit, source state, and a text interpretation sentence (that sentence is the non-visual alternative). The six-line ledger summary includes an **estimated** profit and an **unavailable** profit — two different honest states.

**Stop 4 — The سجّل sheet and quiet completion (4 min).** Tap the center «سجّل» → «تسجيل بيع». Type `2` then `1` on the keypad (watch the digits shift deterministically, cursor pinned under the ones slot). Try the position stepper (◀ ▶), tap a digit slot directly, or swipe across the amount. Add a quick chip (+10). Press «سجّل البيع» and watch the full quiet-completion choreography: button-level saving → receipt replaces the form → calm check mark → closure sentence with **final** numbers (no counting animation) → «افتح السجل · تراجع · تم». Press «تم» and notice the single localized highlight on the Home cash figure.

**Stop 5 — Correction (2 min).** Record another sale, then press «تراجع»: the impact-preview dialog shows **what changes / what stays** before anything happens. Execute it: cash reverts, and a documented correction note appears in Home's recent changes.

**Stop 6 — Work «العمل» (1 min).** The decision panel comes first. Search «خالد» (live filter), then search a word with no match (honest empty state), then try the filter chips. Note the relationship bar under Sara's order with the **hatched «عربون محفوظ» bracket** inside the collected segment and its caption.

**Stop 7 — Toggles (2 min).** Switch **English LTR**: chevrons, back arrows, and the chart mirror; money and dates never mirror. Switch **dark**: warm hairlines and the warm emphasis keep it from going cold. Switch **320**: rows, facts cells, and long labels all survive (this width was built and checked first). Switch **reduced motion** and run the save demo again: instant swaps, static mark, same announcements.

**Stop 8 — Compare directions (1 min).** Mode → «مقارنة الاتجاهات»: the three directions side by side, B and C static and type-floor-compliant, each with its rule bullets and the reason it lost. This is what the direction decision actually was.

## 3. The five demo buttons

| Demo | What it proves |
|---|---|
| ▶ Quiet save | The full T0→receipt choreography, ms-accurate to the motion report |
| ▶ Offline → sync | Truth line appears, writes stay enabled, syncing arc → synced glyph; never a blocking modal |
| ▶ Save failure | Error stays inline, **the typed amount survives**, nothing navigates — retry succeeds |
| ▶ First-paint skeleton | Skeletons only for genuinely-unknown content (first opening of the statement) |
| ▶ Discard guard | Closing the sheet with a typed amount asks «في رقم مكتوب — تسجّله أو تتجاهله؟» |

## 4. What to judge

1. **Does it read as a real product** — calm, operational, trustworthy — rather than a component gallery?
2. **Can you find the money in under two eye movements** on Home and Finance?
3. **Is the Arabic composition natural** — subject on the reading side, amounts in a stable column, nothing fighting the reading direction?
4. **Do the honest states carry their own visual language** («—», تقديري, غير متاح, عربون محفوظ, offline)?
5. **Is the motion calm and interruptible** — does quiet completion feel like closure rather than celebration?

## 5. Known limitations (stated, not hidden)

- Demo writes are in-memory; the artifact holds a single scenario snapshot, not a database.
- Web fonts are progressive enhancement: offline first paint may render system Arabic fallbacks.
- Haptics, real screen-reader passes on devices, RTL chart time-flow validation with real owners, and «د.أ» pronunciation under TalkBack/VoiceOver remain device-test questions (open questions register in `en/02` §5.3).
- Settings, party ledger page, cash closing, assistant shell, and wallet ledger are explicitly out of scope for this review (coverage list published in the artifact and in `en/02` §4) — committed for Stage 4 after approval.

## 6. If you approve

Approve direction A (or request a revision of A, or pick B/C with focused feedback). Stage 4 then refines the chosen direction into the final visual package: design tokens, component/state contracts, motion and gesture system, chart system, content contract, current-work audit, and the implementation handoff — without touching the production codebase in this task.
