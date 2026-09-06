# 03 — Native Motion & Interaction System for Micro

**Task ID:** 3-c · **Agent:** Specialist 3 — Mobile Interaction & Motion Designer · **Date:** 2026-09-07
**Delivery:** `micro-native-mobile-direction-001`
**Basis:** binding constraints from `en/00-previous-work-lessons.md` and the prior cycle's motion report — its timing scale and forbidden register are ratified; its flaw (motion on a CSS page composition) is replaced by **structural, platform-native motion**: a navigation stack, real sheets, keyboard choreography, system gestures. Platform grounding (iOS UIKit/SwiftUI conventions, Material 3 tokens) is professional knowledge.

**Terminology ruling.** Forward screens enter from the **trailing entry edge**: LTR = right, **RTL = left**. The interactive **back edge** is the leading edge: LTR = left, **RTL = right**.

---

## 1. Motion token system

### 1.1 Easings — zero overshoot, everywhere

| Token | cubic-bezier | Role / feel |
|---|---|---|
| **E-decel** | `(0.05, 0.7, 0.1, 1)` | entrances/expansion — fast in, soft landing (Material emphasized-decelerate) |
| **E-accel** | `(0.3, 0, 0.8, 0.15)` | exits/collapse — slow leave, fast gone (Material emphasized-accelerate) |
| **E-flat** | `(0.4, 0, 0.2, 1)` | symmetric state swaps, fades (Material standard) |
| **Linear** | — | loops only — state, not transition |
| **System** | OS-owned | keyboard, scroll physics, pull-to-refresh — never overridden |

Curve-by-role: enter = E-decel, exit = E-accel, swap = E-flat. Exits never use entrance curves; one event, one curve; co-movers differ ≤ one duration class.

### 1.2 Duration scale

| Class | ms | Role |
|---|---|---|
| **T-micro** | 80–120 | press color, focus ring, glyph swap, chevron, underline |
| **T-std** | 150–220 | crossfades, row collapse/insert, dialogs, scrim, banner, stable-frame swaps |
| **T-surface** | 240–280 | sheet settle/return, height settles, keyboard re-anchor |
| **T-struct** | **300 ± 40** | **stack push/pop, sheet present, day-page settle** — the one improvement |
| T-loop / T-hold | 1200 linear / 600 flat | sync arc, skeleton pulse / single figure highlight |

**T-struct justification.** The 280ms cap was set when travel was fake (CSS view-switching). Real structural transitions are full-width, **interruptible, finger-driven** travels — duration is travel time the user controls, not read time. iOS pushes run ≈350ms and Material 3 emphasized durations 300–500ms; 300ms is the calm, fast end of native. Everything else keeps the prior cap; **nothing programmatic exceeds 340ms**, and longer motion is only OS-owned or user-driven.

### 1.3 Distances, parallax, stable elements

| Motion | Travel | Secondary | Stable |
|---|---|---|---|
| Push | incoming 100% width | outgoing **33%** (≈107–142dp) + dim 0→0.12 | tab bar at root; outgoing scroll |
| Pop | exiting 100% | root returns 33%→0 | same |
| Sheet present | 100% height | scrim 0→0.40; FAB fades 120ms | standing screen + scroll |
| Day page | 100% width | strip marker slides | counters header, day strip |
| Offline banner | 44dp + safe inset | content shifts as one block | content order, scroll anchor |
| Tab switch | **content 0 — crossfade only** | indicator slides between tab centers | per-tab scroll cache |
| Large-title collapse | none timed — scroll-linked 1:1 | compact title fades (120 E-flat) | pinned bar height |
| Row press | 0 — color only | — | tabular numerals never scale |

**Instant:** every state commit — tab selection, filter result, badge count, disabled logic, keypad glyphs under rapid typing, press color on touch-down, focus moves, announcements, deep-link first paint (renders settled), all reduced-motion alternatives. Motion never delays truth.

---

## 2. Motion inventory

Interrupt doctrine: **user-driven transitions retarget from current progress with velocity handoff; programmatic, non-reversible moments (dialogs, completion) are short and offer explicit exit buttons instead of reversal.**

### A — Navigation & structure

| Motion | Trigger → start → end | RTL / LTR | Dur · ease | Interrupt | Reduced · a11y |
|---|---|---|---|---|---|
| **Tab switch** | tap → content crossfades 1→0 / 0→1, zero travel; indicator slides | content identical; indicator follows reading order | 150 E-flat; 180 E-decel | re-tap retargets instantly; scroll cache restores | instant swap; focus→h1; `tablist`/`aria-selected` |
| **Stack push** | row tap → screen slides 100% in from trailing entry edge; outgoing 33% + dim | mirrored (RTL entry = left) | 300 E-decel | edge-back / new push retargets with velocity | instant; focus→h1; back «رجوع» |
| **Stack pop** | back tap / edge drag → detail exits 100%; root returns 33%→0; scrim fades | back edge = RTL right / LTR left | 260 E-accel + root E-decel | push mid-pop retargets | instant; **focus returns to originating row** |
| **Large-title collapse** | scroll → title translates 1:1 with content; compact title + hairline appear at threshold | vertical, identical | scroll-linked; compact fade 120 E-flat | scroll reversal reverses 1:1, no snap | retained (finger-driven); compact title always in a11y tree |

### B — Surfaces

| Motion | Trigger → start → end | RTL / LTR | Dur · ease | Interrupt | Reduced · a11y |
|---|---|---|---|---|---|
| **Sheet present** | FAB/row tap → sheet rises 100%→0, scrim 0→0.40, FAB fades | vertical; interior RTL | 320 E-decel; scrim 200 E-flat | no reversal first 60%, then drag takes over; re-tap ignored while open | instant present; `role=dialog`, focus trap, focus→title, «إغلاق» |
| **Sheet dismiss + drag** | drag handle → 1:1 translateY, scrim proportional; release >96dp or >500px/s → dismiss, else return | vertical | 180 E-accel / E-decel | new touch re-enters tracking; typed input → discard guard | tracking retained (direct manipulation); settle instant; guard = `alertdialog` |
| **Dialog present** (cash-closing, correction, conflict) | confirm → scrim 0→0.44; fade + scale 0.96→1; **interior static** | center; layout RTL | 180 E-decel / 140 E-accel | scrim tap never dismisses destructive dialogs | instant; `alertdialog`, focus title, confirm gated + reason |
| **Keyboard + input accessory** | field focus → OS keyboard; sheet re-anchors by exact cover distance; accessory («التالي/تم») pins above keyboard | vertical; field order RTL | ≈250 System | field switch re-targets live | OS-owned; focus ring; accessory buttons ≥44dp |

### C — Content & feedback

| Motion | Trigger → start → end | RTL / LTR | Dur · ease | Interrupt | Reduced · a11y |
|---|---|---|---|---|---|
| **Row appearance on load** | first paint → rows render settled, **no stagger**; skeleton (first load only) crossfades to content | mirrored layout | 150 E-flat | n/a | identical; `aria-busy` cleared; swap announced only if meaning changed |
| **Row insert** (sync, quick write) | data arrives → row height 0→row; rows below translate as one block | mirrored layout | 180 E-decel | inserts coalesce; one mover | instant insert; polite «وصل سجل جديد» if visible |
| **Search/filter reveal** | search tap → field expands in place + keyboard; typing → non-matching rows collapse; **matched rows never move** | mirrored layout | reveal 200 E-decel; collapse 180 E-accel | typing supersedes instantly | instant filter; count announced («3 نتائج») |
| **Quiet completion** | money write in capture sheet → §3 | — | — | not interruptible; explicit buttons | full alternative, §3 |

### D — Truth & waiting

| Motion | Trigger → start → end | RTL / LTR | Dur · ease | Interrupt | Reduced · a11y |
|---|---|---|---|---|---|
| **Offline banner** | connectivity lost → banner drops 44dp + safe inset, content shifts as block; truth line «شغال بدون إنترنت — كل شي محفوظ على جهازك» | vertical | 220 E-decel / 180 E-accel | state flips supersede | instant banner; `role=status`, announced once |
| **Sync start→finish** | sync begins → hollow dot → rotating arc; queue badge counts pending writes; finish → static check 2.5s → fades | neutral | swaps 150 E-flat; arc 1200 linear | state changes supersede | arc → static dot + text «جارٍ المزامنة…»; synced announced only after visible syncing; badge count in label |
| **Conflict alert** | conflict detected → glyph becomes static diamond (never animates); alert row inserts at list top; tap → resolution dialog | row insert per C | 180 E-decel | persists until resolved | identical (already static); assertive announcement; composed row label |
| **Pull-to-refresh** | pull at top → **system** refresh control — gesture physics, not content truth; list stays visible; release → sync via glyph | system, RTL-native | System | OS-owned | OS-owned; **refresh also a button** beside the glyph |

### E — Gestures & Seed C

| Motion | Trigger → start → end | RTL / LTR | Dur · ease | Interrupt | Reduced · a11y |
|---|---|---|---|---|---|
| **Swipe row actions** | drag row toward trailing direction → actions pinned at trailing edge; full swipe = one recoverable state-advance | RTL: drag **rightward** reveals actions at the **left** edge (system mirroring of LTR) | reveal 1:1; settle 180 | new touch re-enters tracking | instant reveal; actions are labeled buttons |
| **Long-press** | 500ms hold → context menu fades in; **row never scales** (tabular digits) | menu-neutral; item order RTL | 150 E-decel | tap elsewhere dismisses | instant menu; `role=menu`; never sole path |
| **Day paging** (Seed C) | horizontal drag → pages track 1:1; release → settle to nearest page; strip marker slides | pages run right→left in RTL; **forward in time = drag leftward** | settle 260 E-decel; fling >1200px/s → next page | new touch re-enters tracking | drag retained; strip tap = 150 crossfade; strip = segmented control, day announced («الثلاثاء») |

---

## 3. Quiet completion — money write in the capture sheet

| Time | Event |
|---|---|
| **T0** | Tap «سجّل البيع»; press color; idempotency key minted. |
| **T0+80** | Saving: label → «جارٍ التسجيل…» (150 E-flat), 16dp inline arc (1200 linear), button width reserved, `aria-busy`; fields inert, not dimmed; **nothing else changes**. |
| **T_W** | Write commits (local-first; offline identical). If >600ms, nothing new animates — the button stays truthful. |
| **T_W+120** | Form fades out (150 E-accel). Sheet frame, scrim, standing screen unchanged. |
| **T_W+270** | Receipt settles: sheet height → receipt height (200 E-decel, bottom-anchored); check mark 0.8→1 + fade (180 E-decel, **zero overshoot**). |
| **T_W+420** | Closure sentence + actions (150 E-flat): «سُجّل بيع 20.00 د.أ — الكاش صار 165.00 د.أ» — final tabular digits, **never counted**. Buttons [افتح السجل] · [تراجع] · [تم]. Focus → receipt; polite live region duplicates the sentence. Then **settle — nothing moves**; no auto-dismiss. |
| **«تم»** | Sheet dismisses (220 E-accel); scrim fades; FAB returns. The one changed figure beneath gets the 600ms highlight fade (once). |
| **Failure** | Button returns; inline error in reserved slot, assertive; **typed amount stays on screen**; nothing navigates. |

**Announcements:** saving = `aria-busy` on the button only; completion = polite closure sentence (money in one language: «20.00 دينار»); the mark reinforces, the sentence carries semantics. **تراجع without applause:** an equal-weight text button opening the static CorrectionPreview dialog («ما سيتغيّر / ما لن يتغيّر», confirm gated by reason). No timers, no auto-undo, no sound — correction is a normal, dignified path. **Reduced motion:** instant form→receipt swap, static full-size mark, identical announcements, highlight omitted.

---

## 4. Gesture map

| Gesture | Purpose | Guardrails |
|---|---|---|
| Tap | every action | nothing tap-inaccessible; one action word per row |
| Long-press | context menu incl. «تصحيح» | never on the tab bar; never the sole path; money edits stay gated by dialogs |
| Swipe row (trailing) | **operational rows only** — state advance («أكمل», «استلم»), recoverable | **no swipe on money rows** (capture sheet + correction only); no swipe-to-delete anywhere |
| Sheet drag | dismiss intent | 1:1, threshold 96dp / 500px/s; typed input → discard guard; handle ≥44dp |
| Edge-swipe back | pop | RTL right edge / LTR left; interactive 1:1; editors with input show the 3-choice guard |
| Scroll + pull-to-refresh | reading + explicit sync | system physics (incl. edge rubber-banding — physical, not decorative); PTR absent when nothing to sync |
| Day-page drag | move between days | 1:1 + settle; strip shows position; never auto-advances |

**Must not exist:** swipe on the tab bar, multi-finger shortcuts, shake-to-undo, any gesture whose meaning is not also a printed button.

---

## 5. Waiting & truth states

- **Skeletons only on first load of unknown geometry**, in the exact shape of the real layout, with a text label. Once data has ever rendered, **cached values + staleness mark** («آخر تحديث 10:24 ص» + hollow dot) are more honest — never erase truth to fake waiting.
- **Spinner discipline:** only the button-level saving arc and the system PTR control; never a spinner over rendered content.
- **Queue badge:** pending-write count on the sync glyph, decremented instantly as writes land — no number roll.
- **Anti "permanently successful dashboard":** the synced check decays to neutral; staleness ages; the offline line persists while offline; conflict persists until resolved; the badge counts only real writes. No standing green "all good".

---

## 6. Forbidden register & reduced-motion doctrine

**Forbidden:** bounce/overshoot/elastic settle; confetti/celebration sounds; animated counters/number rolls; **morphing one amount into another** (container transforms may touch chrome, never numerals); decorative parallax/depth; glow or pulsing focus; mascots/coins/badges; spinners over truthful content; shake-on-error; auto-advancing or auto-playing motion; timed travel >340ms (non-OS); more than one simultaneous mover; staggered list entrances; press scale on rows.

**Reduced-motion doctrine — full alternatives, never shortened durations:** (1) every programmatic transition becomes an **instant swap with identical end state and identical announcements**; (2) direct manipulation stays (sheet drag, scroll, edge-back, day-page drag are finger physics); (3) scroll-linked large-title collapse stays; (4) loops stop → static states with text; (5) OS keyboard/scroll respect the system setting.

---

## 7. Per-seed motion identity (ONE signature each)

- **Seed A «الخلاصة اليومية» — large-title collapse + timeline settle.** Collapse makes day→detail depth legible; new rows settle as one block. *Rationale:* the brief is a narrative read downward. *Risk:* live reordering turns settle into churn — one mover, coalesced inserts.
- **Seed B «الدفتر» — truth-bar context shift + row press identity.** Filters re-anchor the sticky truth-bar while rows crossfade beneath — truth persists while context shifts. *Risk:* truth-bar figures must never travel between filter states — crossfade only, or money appears to "re-count".
- **Seed C «الصندوق» — day paging + counter press.** Paging makes the day the unit of work; counter press is color-only, heavy, quiet. *Risk:* paging can hide unpaid yesterdays — the day strip must carry honest states (conflict/unsettled marks), not plain dots.

---

## 8. Binding recommendations

- **M-01** Tokens as §1: E-decel/E-accel/E-flat/Linear/System; T-micro 80–120, T-std 150–220, T-surface 240–280, **T-struct 300±40**; nothing programmatic >340ms.
- **M-02** Navigation is a **stack**: forward from the trailing entry edge (RTL: left), 33% outgoing parallax, tab bar stable at root.
- **M-03** RTL back edge = right; interactive pop retargets with velocity; focus returns to the originating row.
- **M-04** Tab switches: crossfade + cached scroll, zero content travel; indicator slide only.
- **M-05** Sheets: 320ms E-decel rise, scrim 0.40, 1:1 drag, 96dp/500px/s threshold, discard guard.
- **M-06** Destructive dialogs: never dismiss on scrim tap; static interiors.
- **M-07** Keyboard system-owned; sheets re-anchor by exact cover distance; accessory = real buttons.
- **M-08** Quiet completion per §3, with تراجع as an equal-weight quiet path and the 600ms one-time highlight.
- **M-09** No entrance stagger; inserts single-mover, coalesced.
- **M-10** Filters collapse non-matching rows; matched rows never move; truth-bar crossfades, never travels.
- **M-11** Skeletons only for never-seen geometry; otherwise cached values + staleness; synced decays; conflict static + persistent.
- **M-12** Swipe actions on operational rows only, system-mirrored in RTL; **no swipe on money rows, no swipe-to-delete**; long-press never sole path.
- **M-13** Day paging: 1:1 + 260ms settle, right→left in RTL, strip = segmented control with honest day states.
- **M-14** Reduced motion = full alternatives; direct manipulation and scroll-linked collapse retained; loops become static text.
- **M-15** Every gesture action has a printed button equivalent.
- **M-16** One motion signature per seed — prototypes may not borrow another seed's signature.
