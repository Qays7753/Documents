# 03 — Mobile Motion & Interaction Specification

Delivery: `micro-visual-product-concept-001` · Stage 1 · Sub-agent 3 of 5 · 2026-09-06
Scope: implementable motion language for Micro (Arabic-first, RTL-first, mobile-first). Sources: task brief (authority 1) + present repo evidence S5–S9 per `en/00-SOURCE-INTAKE-REPORT.md`. Palette, copy, and NumericSurface principles are fixed inputs; this spec adds only motion and behavior.

## 1. Duration & easing budget

|Token|cubic-bezier|Durations|Used for|Why|
|---|---|---|---|---|
|`settle` (enter)|`cubic-bezier(0.22, 1, 0.36, 1)`|160–280ms|all entrances: push, sheet, toast, banner, disclosure|strong decelerate; lands without overshoot|
|`leave` (exit)|`cubic-bezier(0.4, 0, 1, 1)`|120–200ms|all exits: pop, sheet close, dismissal|exits leave faster than entrances arrive|
|`steady`|`linear`|loops; 1:1 drag|finger tracking, scroll-linked collapse, spinner, skeleton pulse|direct manipulation carries no easing|
|`instant`|—|0–80ms|focus ring, press onset, reduced-motion swaps|attention cues never lag input|

Global budget **90–320ms**; enter decelerates, exit accelerates. Only the spinner (900ms) and skeleton (1400ms) loops are continuous, both removable. No spring token exists by design.

## 2. Motion inventory — 14 patterns

|#|Pattern|Trigger|Start → End|Stays stable|Direction (RTL mirrored)|ms|Easing|RTL/LTR behavior|Interruption|Reduced motion|Accessible alternative|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|Forward push|tap drill-in (order, customer, سجّل entry)|current settled → new settled|shell pixel-static; app-bar frame; canvas color|in +24dp from inline-start + fade; out −8dp counter-drift|280/180|settle/leave|LTR enters right; RTL enters left (mirror)|back mid-flight cancels, jumps to nearest state, pops|crossfade 160ms|focus to new heading (`tabindex="-1"`); route announced politely|
|2|Back / pop|system back, app-bar back, edge swipe|new settled → previous restored|shell; restored scroll offset|out +24dp toward inline-end + fade; in −8dp from inline-start|240/200|settle/leave|LTR exits right; RTL exits left|forward tap mid-flight reverses in place|crossfade 160ms|focus returns to trigger|
|3|Bottom sheet open/close|create / edit / confirm / effect-preview|closed → docked, scrim 40%|sheet dock & width; shell dims under scrim, never moves|vertical: translateY 100%→0; scrim fades|260/200|settle|vertical neutral; handle centered; content RTL|mid-open finger follows 1:1; release <30% closes|sheet instant (0ms); scrim fades 120ms|`role="dialog"`, `aria-modal`, focus trap; «إغلاق»/scrim/Esc; focus returns|
|4|Inline disclosure|tap «تصحيح هذه العملية» header|hidden → expanded|trigger row; neighbors shift as one block, no stagger|vertical; chevron rotates 180°|220/180|settle/leave|vertical; rotation neutral|tap reverses from current height|instant toggle|`aria-expanded` + `aria-controls`; labelled region|
|5|Swipe row actions (receivables)|horizontal drag on row|hidden → clamp 128dp (2×64dp: تذكير / تحصيل)|row height; text anchored inline-start|1:1 finger; 0.4 resistance past clamp; opens at ≥40% clamp or ≥0.3dp/ms|160 snap|steady drag / settle snap|LTR drag left → actions trail right; RTL drag right → actions trail left|any release resolves by threshold; reverse drag closes|jump, no tween; «⋯» always available|row overflow button holds same actions|
|6|NumericSurface digit change|stepper tap / keypad entry|value A settled → value B settled|surface box, tabular-numeral columns, magnitude rail — zero layout change|changed-digit group drifts 6dp (increment up, decrement down) + crossfade; never counts up|120|settle|drift encodes ±, identical in RTL; columns never resize|new input retargets from current state, no queue|crossfade 120ms, no drift|`aria-live="polite"` full new value «1,245.50 د.أ»; steppers are real buttons|
|7|Pressed state|pointer down on any control|rest → pressed|control size; neighbors (no scale anywhere)|none|90|instant→steady|none|lift fades tint back from current value|same (color/opacity only)|primary bg → `#b4613f`; rows/cards: terracotta 6% wash — color-press reads faster than scale, cannot jitter digits|
|8|Skeleton → content|async pending → resolved|skeleton boxes → content|box metrics identical, no shift on swap|none; pulse opacity 0.45↔0.7|1400 loop; swap 160|steady; settle|none|swap stops pulse at once|static 0.5 opacity; instant swap|skeleton `aria-hidden`; region `aria-busy`; one polite «جارٍ التحميل…»|
|9|Saving button|submit tap|label → «جارٍ الحفظ…» + 16dp spinner → «تم الحفظ»|button width locked (min-width); position|spinner at inline-start (leading edge)|120 swap; 900 loop|settle; linear|spinner mirrors to inline-start|second tap blocked: disabled + request de-dup|no spin: text + `aria-busy` only|`aria-busy` during; polite «تم الحفظ» on done|
|10|Quiet completion|async success|none → toast docked above shell + row tint|shell; layout (toast is overlay)|toast 12dp rise + fade; affected-row tint terracotta 10%→0 over 600ms, once, replaces nothing|200/160|settle/leave|vertical; text RTL|new toast replaces in place (crossfade 120ms); tap dismisses; 3.2s hold (6s with action)|opacity 120ms; tint applied/removed un-animated|`role="status"` polite «تم تسجيل التحصيل — 50.00 د.أ»; «تراجع» action focusable|
|11|Sync / offline banner|connectivity change|absent ↔ docked under app bar (overlay, no content push)|content position; shell|vertical −100%→0|220/160|settle/leave|vertical neutral; label RTL|state flip retargets instantly; persistent while offline|opacity 120ms|`role="status"` polite «لا يوجد اتصال — سيتم المزامنة تلقائيًا»|
|12|Error recovery|validation / server failure|field valid → inline error visible|layout except the one expanded error line|vertical expand (mechanism of #4); border color 120ms; one 400ms soft terracotta highlight — once, loops never, replaces no text/icon|180/120/400|settle/instant|vertical; error text RTL|re-entry retargets; fixing removes line in 160ms|no highlight; border + text only; instant scroll|focus moves to first invalid field; `aria-describedby` binds error; assertive only if blocking; «تراجع موثق» offered|
|13|Focus ring|`:focus-visible` (keyboard/AT)|unfocused → ringed|everything; outline + offset, zero layout shift|none|≤80|instant|position follows RTL tab order|N/A — a state, not an animation|identical|this *is* the AT affordance; 2dp ring in `#964e33`-role token, 2dp offset; no flying focus|
|14|Top Focus Shell compact on scroll|scroll past 96dp|expanded 64dp header ↔ compact 40dp bar|docked bar; bottom shell; totals remain in DOM|scroll-linked 1:1 between 64–96dp, then commits; no horizontal component|160 commit|steady track / settle commit|vertical only|reverse scroll re-expands from current point|instant swap at threshold, no scroll interpolation|both states in DOM; AT reads full static header; no `aria-live`|

## 3. Screen transition model

|Navigation|Mechanism|Example|Stable throughout|
|---|---|---|---|
|Drill-in (hierarchy)|short push (#1)|العمل → order detail|shell; app-bar frame|
|Peer switch between the five seats|crossfade 160ms, no directional slide (peers have no hierarchy)|مشروعي الآن ↔ مالي|shell; seat indicator transform-only|
|Create / edit / confirm|bottom sheet (#3)|new expense; effect-preview card|underlying view frozen|
|Destructive confirm|sheet, never swipe-dismissable|delete entry|same|
|App start|no splash animation; first frame + skeleton|—|—|

The five-seat shell «مشروعي الآن \| العمل \| سجّل \| مالي \| أدواتي» never slides, scales, or re-renders during any transition; canvas background stays constant; only content layers move.

## 4. Gesture spec

|Gesture|Threshold|Fail / cancel|Tap alternative|Thumb-zone note|
|---|---|---|---|---|
|Row swipe reveal|≥40% of 128dp clamp or 0.3dp/ms|release below threshold; opposite drag|row «⋯» → action sheet|revealed actions land in lower thumb arc (LTR right / RTL left)|
|Long-press|450ms hold, ≤8dp drift|move >8dp cancels|same «⋯» menu|secondary row power-actions only|
|Sheet drag-to-dismiss|≥30% height or ≥0.35dp/ms downward|re-docks 200ms settle|«إغلاق», scrim tap, Esc|handle centered at screen bottom|
|Back edge swipe|≥24dp from inline-start edge (LTR left / RTL right) at ≥0.25dp/ms|settles back 120ms|app-bar back button|inline-start edge is the resting-thumb side in RTL|

Every gesture has a tap alternative — nothing is gesture-exclusive. One-handed rationale: primary actions and revealed swipe actions sit in the bottom 40% of the screen, inside the natural thumb arc; destructive and rare actions sit top inline-end, away from accidental triggers.

## 5. Interruption philosophy

- **Input-first:** every transition is a state machine that accepts new input; animations cancel and jump to the nearest committed state — never rewind, never queue.
- **No motion locks:** nothing awaits an animation; controls stay active mid-transition.
- **Rapid taps:** a 120ms input-grace after a push starts swallows accidental double-taps; after grace, taps are idempotent (re-tap same target = no-op). Double-submit blocked by disable + request de-dup; second tap on a sheet trigger mid-open does nothing.
- Interrupted exits complete as the entry of the previous state; the UI never freezes mid-frame.

## 6. Reduced-motion contract

|Class|Patterns|Treatment|
|---|---|---|
|None needed|7, 13|already opacity/color only|
|Opacity-only|8, 9, 10, 11|fade 120ms; no translate, no spin|
|Crossfade|1, 2, 6|120–160ms opacity swap, no drift|
|Instant|3, 4, 5, 12, 14|0ms state change; sheet scrim still fades 120ms|

`prefers-reduced-motion` is honored by default; manual toggle «تقليل الحركة» in أدواتي persists and overrides it. One driver flag feeds every animation — no per-feature exceptions; spinner/skeleton become static text/opacity, never blank space.

## 7. NumericSurface guarantees

Stable digits → tabular numerals + locked surface box + color-press instead of scale (#7). Directional context movement → the 6dp digit drift (#6) is the only direction-carrying money motion; counting-up banned. Always-visible position → magnitude rail never animates away. Tap alternative → steppers/keys are buttons; every row gesture has «⋯». `#964e33` never animates ambiently — it appears only as primary-action color and focus-ring role.

## 8. Explicitly rejected motion

|Pattern|Why|
|---|---|
|Bounce / overshoot springs|playful physics undermine money-serious trust; overshoot implies imprecise amounts|
|Confetti / celebration bursts|entertainment motion; forbidden|
|Animated count-up of money|violates NumericSurface stability; invites misreading totals|
|Neon glow / luminous accents|fights the fixed terracotta palette and its contrast audit|
|Parallax layers|depth noise; jank on the low-end Android devices common among target owners|
|Traveling shimmer skeletons|entertainment-style; replaced by calm opacity pulse|
|Shake on error|startles without informing; replaced by calm highlight + focus move|
|Flying FAB morph|complex paths break shell stability; sheets replace it|
|Elastic overscroll glow|platform-owned visual, off-brand|
|Any transition >320ms|reads as lag in repetitive one-handed workflows|
|Animated logo splash|delays task access; the first frame is the product|

## 9. Handoff notes

Identity-defining decisions: (1) **color-press identity** — the press signature is the palette's own `#b4613f`, never scale; (2) **6dp directional digit drift** — money moves meaningfully, never theatrically; (3) **stable-shell short push** — the world anchors while content travels. For sub-agent 4: verify `#b4613f` press contrast in dark mode; scrim 40% black (light) / 60% (dark). For sub-agent 2: sheet/scrim layered-depth tokens.
