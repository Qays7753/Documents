# 03 — Native Motion & Interaction System (Specialist Research)

**Delivery:** `micro-native-mobile-direction-002` · Stage 1 · 2026-09-07
**Author:** Specialist 3 — Mobile Interaction & Motion Designer
**Status:** Research input only. No direction is selected here; the orchestrator decides. No prototype is specified.
**Inputs read:** `en/00-previous-work-lessons.md`, `en/01-intake-and-previous-work-audit.md` (buckets K/A/R/V), constraint register C-01…C-08.
**Mandate answered:** A-09 — supply the transition grammar **connected to navigation events** that both prior deliveries lacked (R-11: "page fades or no transitions at all").

---

## 0. Doctrine — four rules everything below derives from

| # | Rule |
|---|---|
| D-1 | **Motion = navigation truth.** Every transition states a spatial/logical relationship (deeper, lateral, modal, transient). A motion that states nothing is deleted. |
| D-2 | **Zero overshoot.** No easing output ever exceeds 1.0. No bounce, no elastic settle, no oscillation — ever. |
| D-3 | **One continuity anchor per transition.** Each transition keeps exactly one element visually stable (a bar, a field, the header) so the eye never re-orients from zero. |
| D-4 | **Interruptible and honest.** Running motion yields to user input immediately and continues from its *current* value (retarget), never restarting. Gestures take over 1:1 with zero handoff jump. |

**Direction convention:** all horizontal values are stated in **RTL physical terms** (Arabic-first build, C-05). The LTR verification build mirrors every left↔right value exactly; durations, curves, thresholds, and vertical motion never change. Coordinates below are physical (CSS-style): positive X = rightward.

---

## 1. Motion tokens

### 1.1 Duration classes (the only three)

| Class | Range | Nominal | Assigned to |
|---|---|---|---|
| `micro` | 80–140 ms | 100 ms | press states, selection ticks, glyph swaps, focus, value attaches |
| `standard` | 160–260 ms | 200 ms | in-screen changes: scrims, inline reveals, error attach, indicator morphs |
| `surface` | 280–360 ms | 320 ms | navigation-level surfaces: push/pop, sheet rise, dialog, tab switch, pager settle |

**Hard cap:** no single motion exceeds **400 ms**; no composed sequence (stagger chains) exceeds **600 ms** total. Loops are permitted only while actually waiting and only functional (progress spinner, skeleton pulse). Gesture *tracking* is exempt from duration caps while the finger is down — it is user motion, not animation.

### 1.2 Easing curves (exact values)

| Token | Cubic-bezier | Character | Assigned to |
|---|---|---|---|
| `ease-standard` | `cubic-bezier(0.2, 0, 0, 1)` | smooth both ends | in-screen property changes: scrims, tints, indicator morphs |
| `ease-decelerate` | `cubic-bezier(0.05, 0.7, 0.1, 1)` | fast start, long settle | enters: incoming surfaces, reveals, error attach |
| `ease-accelerate` | `cubic-bezier(0.3, 0, 0.8, 0.15)` | slow start, fast exit | exits: outgoing surfaces, dismissals |
| `ease-emphasized` | `cubic-bezier(0.32, 0.72, 0, 1)` | iOS-like push curve | horizontal navigation: push/pop, pager settle |
| `ease-sheet-spring` | `cubic-bezier(0.22, 1, 0.36, 1)` | critically damped, **non-bouncy** (y never > 1) | programmatic sheet settle, gesture release settle |
| `linear` | `linear` | constant | spinner rotation and skeleton pulse **only** — never element position |

Overshoot check: every curve above is monotonic toward y=1 with no y>1 segment; `ease-sheet-spring` reads "springy" through velocity, not through overshoot — that is the point.

### 1.3 Interruption rules

| # | Rule |
|---|---|
| I-1 | **Retarget:** a new target mid-flight makes the current computed value the new start. Never restart from origin, never jump to the end. |
| I-2 | **Reverse-from-current:** direction flip mid-flight plays the reverse from the current position; remaining duration = remaining-distance fraction × original duration, floored at `micro` (100 ms). |
| I-3 | **Gesture handoff:** touch engaging during an animation takes control 1:1 at the current value, zero jump; release velocity is carried where the platform allows. |
| I-4 | **One retarget deep:** a retargeted motion may be retargeted once more, then must settle (livelock prevention). |
| I-5 | **Last input wins:** a new navigation event cancels pending/queued transitions; nothing animates twice for one event. |

---

## 2. Navigation transition grammar — connected to events

Preamble: there are **no full-surface opacity fades** in navigation (R-11). Only layers fade (scrim, dim); screens move or swap. The recommended stable anchor for stack navigation is the **bottom destination bar** (persists during push/pop; covered by scrim under sheets/dialogs) — flagged for orchestrator confirmation. Scrim = neutral black at 45–50% opacity unless stated.

### P-1 · Stack push (forward, deeper into stack)

| Field | Value |
|---|---|
| Trigger | Tap on a row/destination opening a child screen (اليوم → سجل اليوم; مالي → تقرير; row → تفاصيل). |
| Start state | Incoming screen fully off-screen **left** (`translateX(-100%)`), carrying an 8dp leading-edge (right-edge) shadow; outgoing at rest, undimmed. |
| End state | Incoming at 0 covering viewport; outgoing parked at `translateX(+28%)` with a 14% dim, kept alive for instant back. |
| What is stable | Bottom destination bar + system status area; outgoing content is never rebuilt. |
| Direction — RTL | Incoming enters from the **left**; outgoing parallaxes **rightward** (28%) and dims. |
| Direction — LTR | Mirrored: incoming from the right; outgoing parallax leftward. |
| Duration | 320 ms (`surface`). |
| Easing | `ease-emphasized` `cubic-bezier(0.32, 0.72, 0, 1)` both layers. |
| Interruption | Retargetable (I-1); back gesture may grab at any point (I-3). |
| Reduced motion | Instant swap — no transform, no dim ramp; focus still moves; title announced. |
| A11y alternative | Back is **always** a visible button, never gesture-only; focus moves to the new screen's heading; screen name available to screen readers. |

### P-2 · Stack pop (programmatic: back button)

| Field | Value |
|---|---|
| Trigger | Back button («رجوع»), system back, or logical completion (saved → return). |
| Start state | Top screen at 0; beneath at +28%, dimmed 14% (its parked push state). |
| End state | Top exits **left** to `translateX(-100%)` and is discarded; beneath returns to 0, dim 14%→0. |
| What is stable | Bottom destination bar; beneath screen content restored, never reloaded. |
| Direction — RTL | Top slides out to the left; beneath returns from the right. |
| Direction — LTR | Mirrored. |
| Duration | 300 ms (slightly shorter than push — exits feel faster). |
| Easing | `ease-emphasized`. |
| Interruption | Retargetable; re-push mid-pop retargets (I-1/I-5). |
| Reduced motion | Instant swap; beneath appears at rest. |
| A11y alternative | Focus returns to the originating row/trigger; screen change announced. |

### P-3 · Interactive edge-swipe back (gesture pop)

| Field | Value |
|---|---|
| Trigger | Touch within **24 dp of the right edge** (RTL), vertical span between top and bottom safe-area insets; horizontal drag **leftward** ≥12 dp engages, then direction locks. |
| Start state | Top at 0; beneath at +28%/14% dim (parked state). |
| During | 1:1 tracking — no easing while finger is down; dim (14%→0) and parallax (+28%→0) interpolate with progress *p*. |
| Commit | Release with *p* > 0.45 **or** velocity > 600 dp/s in back direction → finish from current position, 220 ms `ease-emphasized`. |
| Cancel | Otherwise → settle back to start, 240 ms `ease-sheet-spring`; dim and parallax reverse-from-current (I-2). Never snaps instant (except reduced motion). |
| What is stable | Bottom destination bar; beneath screen is the reference frame. |
| Direction — RTL | Right-edge contact, leftward drag, top exits left. |
| Direction — LTR | Mirrored: left-edge contact, rightward drag, top exits right. |
| Duration | User-driven; settle steps 220–240 ms. |
| Easing | Tracking = none; settle = `ease-emphasized` / `ease-sheet-spring`. |
| Interruption | Inherently the interruption path (I-3); re-grab during settle allowed. |
| Reduced motion | Tracking kept (user-driven); commit/cancel settle = instant (≤80 ms opacity only). |
| A11y alternative | Visible back button on every pushed screen; swipe is an accelerator, never the only path (K-12). |

### P-4 · Bottom sheet open (capture «سجّل تحصيل», details, edit)

| Field | Value |
|---|---|
| Trigger | Primary action in the bottom thumb zone (K-12) or a row action. |
| Start state | Sheet off-screen bottom (`translateY(100%)`), 16dp top corner radius, 36×4 dp handle pill centered; scrim 0%. |
| End state | **Detent A = 56% of viewport height** (default landing); user may drag/grab-flick up to **detent B = full height minus top inset**; scrim 45%; underlying screen does **not** move or scale. |
| What is stable | Underlying screen (frozen, dimmed only); handle pill anchored center. |
| Direction — RTL | Vertical rise — identical in both directions; no horizontal geometry anywhere. |
| Direction — LTR | Identical. |
| Duration | Sheet 320 ms; scrim 200 ms (parallel). |
| Easing | Sheet `ease-sheet-spring` (non-bouncy settle); scrim `ease-standard`. |
| Interruption | Grabbable mid-rise (I-3); keyboard appearance retargets the sheet's top edge, 200 ms `ease-standard` (device behavior = V-04). |
| Reduced motion | Sheet appears instantly at detent A; scrim 80 ms fade. |
| A11y alternative | `role="dialog"` `aria-modal`, labelled (e.g. «سجّل تحصيل»); focus trap into first field; ✕/Esc closes; focus returns to trigger on close. |

### P-5 · Bottom sheet close (✕ / scrim tap / drag-down / تم)

| Field | Value |
|---|---|
| Trigger | Any of the four; drag-down engages from the **handle strip = top 48 dp of the sheet** (handle pill plus padding — target ≥44 px, K-07), whole sheet body also draggable except form inputs. |
| Start state | Whatever position the user reached (any point between detents). |
| During | 1:1 tracking downward; resistance ×0.25 when pulled above detent B (rubber-band without overshoot, D-2). |
| Commit (dismiss) | Release velocity > 700 dp/s downward **or** dragged > 40% of the detent gap → finish 240 ms `ease-accelerate` to `translateY(100%)`. |
| Expand / settle | Velocity > 700 dp/s upward → settle to detent B, 280 ms `ease-sheet-spring`; otherwise settle to nearest detent, 240 ms `ease-sheet-spring`. |
| Scrim | Fades 45%→0 over 180 ms, parallel with sheet. |
| Direction — RTL/LTR | Identical (vertical). |
| Interruption | Re-grab anytime (I-3); dirty-form close raises the unsaved-changes dialog (P-6) — honest states, no silent discard. |
| Reduced motion | Instant close (≤80 ms); scrim 80 ms. |
| A11y alternative | ✕ is a real ≥44 px button; scrim tap equivalent; focus restored. |

### P-6 · Dialog (confirmations, conflict, effect preview — K-09)

| Field | Value |
|---|---|
| Trigger | Irreversible or money-affecting decisions: conflict resolution, correction effect preview, unsaved-changes, delete confirmations. |
| Start state | Centered, `scale(0.92)` + opacity 0; scrim 0%. |
| End state | `scale(1)` + opacity 1; scrim 45%. **No slide — never enters from an edge** (edges belong to navigation, dialogs are not places). |
| What is stable | Screen behind is frozen and dimmed; dialog is the only moving layer. |
| Direction — RTL/LTR | Identical (centered, non-directional). |
| Duration | Enter 180 ms; exit 120 ms; scrim 150 ms. |
| Easing | `ease-decelerate` in, `ease-accelerate` out, scrim `ease-standard`. |
| Interruption | None — modal and deliberately gesture-free; no drag-to-dismiss. |
| Reduced motion | Opacity-only, 80 ms (no scale). |
| A11y alternative | `role="alertdialog"` for conflicts/errors; focus trap; initial focus on the **safe** action; effect lists (will-change / won't-change, K-09) read as text. |

### P-7 · Tab / destination switch — **decision: fade-through with 8dp rise**

Why fade-through wins over crossfade: a crossfade dips *both* screens to ~50% opacity mid-transition, flashing the background through — a page fade (R-11) in disguise. Fade-through keeps exactly one opaque surface at all times: outgoing fades out first (90 ms `ease-accelerate`), then the incoming fades in (180 ms `ease-decelerate`) rising 8 dp (`translateY(8dp)` → 0). The 8 dp rise is deliberately **vertical**: sibling destinations have no spatial order, so a horizontal slide would fake an axis that doesn't exist and would need pointlessly mirrored variants; a vertical settle reads "arriving" and is RTL/LTR-identical. Total ≤270 ms, within cap.

| Field | Value |
|---|---|
| Trigger | Tap a seat in the bottom destination bar. |
| Start state | Current destination opaque; target either cached (opacity 0) or cold. |
| End state | Target opaque at rest; previous removed from hit-testing; each destination preserves its own scroll position. |
| What is stable | The destination bar itself + status area; large-title headers compact/expand per scroll, independent of this transition. |
| Direction — RTL/LTR | Identical (vertical rise only). |
| Duration | Out 90 ms + in 180 ms (total ≤270 ms). |
| Easing | `ease-accelerate` out, `ease-decelerate` in. |
| Interruption | I-5: tapping another seat mid-switch retargets the incoming phase directly; the out-phase never replays. |
| Reduced motion | Instant swap, no rise, no fades. |
| A11y alternative | Bar is a `tablist`; destination name announced; focus moves to the destination heading. |

### P-8 · Search open/close — **decision: overlay expansion (not push)**

Why not push: search is a *mode*, not a destination — pushing it would add back-stack depth to a state users abandon within seconds, and the keyboard already owns the bottom edge. The field stays where it was, becoming the stable anchor (D-3); results arrive beneath it; cancel is a ✕, not a pop.

| Field | Value |
|---|---|
| Trigger | Tap the search field (header region). |
| Start state | Field at rest; results panel opacity 0, +12 dp. |
| End state | Field unchanged (anchor); results panel opacity 1 at rest; 32% scrim over everything else; keyboard up (system-driven). |
| Close | ✕ → panel fades 120 ms, scrim releases 120 ms, keyboard dismisses; field returns to rest. Query text persists while the screen lives. |
| Direction — RTL/LTR | Identical (vertical arrival; text alignment follows content direction automatically). |
| Duration | Panel 200 ms in / 120 ms out; scrim 150 ms. |
| Easing | `ease-decelerate` in, `ease-accelerate` out. |
| Interruption | Typing mid-transition retargets (I-1); results replace panel content by crossfade, never by panel re-animation. |
| Reduced motion | Instant panel; scrim 80 ms. |
| A11y alternative | `role="searchbox"` with label; result count announced politely when loaded; ✕ is a real ≥44 px button. |

### P-9 · Pager swipe (shared-axis X with neighbor preview)

Used only between **equal-rank siblings** (e.g., today ↔ yesterday ledger pages). Never between hierarchy levels — that is what push/pop is for.

| Field | Value |
|---|---|
| Trigger | Horizontal drag on the pager body. |
| Start state | Current page at rest; neighbor visible as a **24 dp peek** at the leading edge — the left edge in RTL — so swipeability is discoverable without coaching. |
| During | 1:1 tracking; both pages translate together on the shared X axis (shared-axis, not a cover). |
| Commit | Travel > 50% or fling > 800 dp/s → settle to neighbor, 260 ms `ease-emphasized`. Cancel otherwise → return, 260 ms `ease-emphasized`. |
| What is stable | Shared pager title/header if present; peek edge constant. |
| Direction — RTL | Next page lives to the **left**; advancing = finger drags leftward; peek on left edge. |
| Direction — LTR | Mirrored. |
| Duration | User-driven; settle 260 ms. |
| Easing | Tracking none; settle `ease-emphasized`. |
| Interruption | Re-grab during settle (I-3); fling chains allowed (I-4 bounds). |
| Reduced motion | Instant page swap; static peek retained. |
| A11y alternative | Visible ‹ › pager buttons ≥44 px with mirrored RTL arrow order; page title announced on change. |

---

## 3. Gesture set

| Gesture | Geometry (RTL) | Engagement & tracking | Thresholds | Mirrored in LTR | Reduced motion | Verdict |
|---|---|---|---|---|---|---|
| Edge-swipe back | Right edge, 24 dp wide, between safe insets | Drag leftward ≥12 dp engages, direction locks, 1:1 | Commit: p>0.45 or v>600 dp/s; cancel settles 240 ms | Yes (left edge, rightward) | Tracking kept; settles instant | Core — v1 |
| Sheet drag | Handle strip = top 48 dp of sheet; body draggable except inputs | 1:1; ×0.25 resistance above detent B (no overshoot) | Dismiss v>700 dp/s or 40% of detent gap; expand v>700 dp/s up | No (vertical) | Tracking kept; settles instant | Core — v1 |
| Pull-to-refresh | Vertical overscroll at top of **eligible lists only** | Rubber-band ×0.35; 16 dp spinner appears at threshold, holds while loading | Trigger at 72 dp overscroll; settle ≤300 ms on complete | No (vertical) | No stretch: fixed indicator + «تحديث…» text | Allowed only on server-truth surfaces (اليوم, مالي); **never** on capture sheets, tool screens, or cached-first lists that already show a sync chip |
| Long-press menu | Any non-input list row | 500 ms hold, 8 dp movement tolerance; menu scales 0.96→1 + fade 120 ms at press point, clamped to edges | Scroll before threshold cancels silently | Menu anchoring mirrors | Instant menu, no scale | Accelerator **only** — every row keeps a visible ⋮ affordance as the primary path; light haptic tick on open |
| Row swipe actions | See decision below | — | — | — | — | Deferred / sparing |

**Row swipe actions — recommendation (sparing, per mandate):** ship **zero destructive** swipe actions in v1. If a direction ships one at all, it is a **single non-destructive action (تعديل)** on today's ledger rows: revealed from the **trailing side, which is the left in RTL** — the row content moves rightward under a rightward finger drag, exactly mirroring the LTR "swipe left to reveal" reflex. Discoverability is guaranteed by an always-visible edit affordance (the swipe is an accelerator, never the only path) plus a one-time 12 dp peek on first appearance. Thresholds: open at 25% width or velocity; snap open/close 200 ms `ease-standard`; any tap elsewhere closes it; destructive outcomes always route through a dialog (P-6 / K-09). If these conditions can't be met in a direction, drop the gesture — a visible button beats an invisible one.

---

## 4. Feedback choreography

| Pattern | Trigger | What moves | Duration · easing | Interruption | Reduced motion | A11y |
|---|---|---|---|---|---|---|
| Loading — cached-first | Screen enter with any cached data | **Nothing.** Content renders instantly with a quiet sync chip («من المحفوظات» / sync state); fresh data arrives by 120 ms content crossfade | 120 ms on arrival | Immediate | Same | Content itself is the non-visual alternative |
| Loading — skeleton | Known stable shape, cold cache, expected wait >400 ms | Block opacity pulse 0.55↔0.8, 1000 ms, `ease-in-out`, 60 ms stagger, max 4 rows. **No gradient shimmer sweep** — it is an animated gradient (banned, §6) | Loops only while waiting | Content replaces pulse with 120 ms crossfade | Static blocks @0.6 + «جارٍ التحميل…» text | Text status + polite announcement when ready |
| Saving | Tap «حفظ» | Button label → «جارٍ الحفظ…» + 16 dp inline spinner, disabled; fields lock; then receipt swap (§5) | 80 ms press; swaps 100–150 ms | I-1 retarget; double-submit blocked by disabled state | Instant swaps + text | Button state announced; `aria-live="polite"` for result |
| Error recovery | Save/submit fails | **Calm error:** inline message above the action area (glyph + word, K-04), 8 dp rise + fade 150 ms; input fully preserved; button becomes «إعادة المحاولة» | 150 ms `ease-decelerate` | Repeated failure **does not re-animate** — text updates only (a re-shake/re-flash is noise, not information) | Instant | `role="alert"`; focus moves to the error; **no shake — banned** |
| Offline → syncing → synced | Connectivity change / queued saves | One persistent status slot in the header region: glyph crossfade 120 ms + label swap («غير متصل — سيُرفع عند العودة» → «جارٍ المزامنة…» + 16 dp spinner → «تمت المزامنة» + check, quiets to neutral after 2.5 s) | 120 ms morphs | Immediate retarget to newest state (I-5); no banner ever slides in or out (R-03: no banner cards) | Unchanged (morphs already minimal) | `aria-live="polite"` on offline and synced; state is also text, never color-alone (C-04) |
| Pending / estimated / unknown / conflict attach | State becomes known or labeled | **One-time 120 ms opacity attach, then static.** No pulse, no color cycling, no motion again until the state itself changes | 120 ms, once | n/a | Same | Glyph + word carry meaning (K-04): «تقديري», «قيمة غير محددة بعد» + «سجّله» action; conflict opens P-6 |

**Why pending/estimated/conflict get (almost) no motion:** these are *persistent truths*, not events. Animating them would present a standing fact as if it were happening just now — the exact dishonesty Micro exists to prevent. Only two exceptions, both one-shot and local: (1) conflict always *demands a decision*, so it opens the P-6 dialog with the K-09 effect preview; (2) when a correction applies, the affected digits crossfade **once** in place (150 ms) — final values appear final, never a count-up.

---

## 5. Quiet completion spec — «سجّل تحصيل» (record a collection), ms-by-ms

Normal-motion path (K-08: closure sentence + one localized highlight; never confetti/counters/overshoot):

| Clock | Surface | Event | Motion |
|---|---|---|---|
| T+0 | «حفظ» button (48 dp, #964e33 fill, C-03) | Touch down | Fill → press-only #b4613f, 80 ms |
| T+80 | Button | Label → «جارٍ الحفظ…», 16 dp inline spinner, disabled; all fields lock | 100 ms swap |
| T+80 → T+600 | — | Save executes | Nothing else moves; no progress bar for sub-second work |
| T+600 | Sheet | Result known → keyboard dismisses; form crossfades to the receipt sentence | Keyboard 200 ms (system); content crossfade 150 ms |
| T+620 | Receipt | «حُفظ التحصيل: <bdi dir="ltr">25.00</bdi> د.أ — نقداً» + time/customer line; ASCII digits, `tabular-nums`, unit after the number (K-05/K-06) | **The one localized highlight:** tint fades in on the amount 120 ms, out by T+1200 — total ≤600 ms, single, never repeated |
| T+600 | Screen reader | `aria-live="polite"` announces the same sentence verbatim | — |
| T+720 | Action area | Primary becomes «تم» (receipt is already the confirmation — the button is an exit, not a celebration) | 120 ms fade |
| T+2200 | Sheet | **Auto-dismiss** if untouched (receipt shown ≥1.6 s): slide down 260 ms `ease-accelerate`, scrim out 180 ms | Underlying list row was inserted at T+600; row receives its own single 400 ms tint (one highlight per surface) |
| user tap | «تم» | Any tap ≥T+720 dismisses immediately via the same 260 ms path | — |

Total experience: **≈2.5 s** from tap to closed sheet; the truth (final digits) is visible at T+770 at the latest.

**Failure path:** at T+600 failure → button restores «حفظ» (150 ms), calm inline error appears (§4, `role="alert"`), amount field keeps its value, focus moves to the error, retry re-enters the flow from T+80. No shake, no dialog for recoverable errors, no data loss ever.

**Reduced-motion variant:** T+600 → **instant swap** to the receipt sentence (no choreographed keyboard/content sequence); amount is static bold, no tint; «تم» available immediately; dismissal at T+2200 or on tap is instant (≤80 ms opacity); the list row appears immediately with a **static text mark** instead of a tint. Announcement and timing policy identical — timing is not motion, so auto-dismiss at T+2200 is kept.

---

## 6. Forbidden register (explicit)

| Banned | Why it fails | Instead |
|---|---|---|
| Bounce / overshoot / spring oscillation | Childish; breaks D-2; reads as a toy, fatal for money | `ease-sheet-spring` (critically damped, zero overshoot) |
| Confetti / celebration particles | Decoration ≠ meaning; undercuts financial seriousness | Quiet completion (§5) |
| Count-up / rolling numbers | Fake precision on real money; breaks tabular honesty (K-06) | Digits appear final; at most one 150 ms crossfade |
| Spinning hero loaders >1 s | Reads as a stall on the truth-first moment | Cached-first + skeletons + inline spinners ≤16 dp |
| Parallax wallpaper / depth spectacle | Web-showcase grammar (R-01 lineage); motion without meaning | The only parallax allowed is functional: outgoing push screen (P-1) |
| Page fade-ins on every screen | The defining web tell (R-11) | Event-connected grammar (§2) |
| Hover-dependent affordances | No hover on touch; invisible on the primary device | Always-visible affordances; press states carry feedback |
| Animated gradients | Decorative noise; includes skeleton shimmer sweeps | Flat fills; opacity-pulse skeletons |
| *(derived)* Stagger chains >600 ms | Delays the truth past the cap | One anchor element; total ≤600 ms |
| *(derived)* Infinite decorative loops | Attention theft from financial content | Loops only while actually waiting, functional only |

---

## 7. Reduced-motion strategy

**Sources:** the system `prefers-reduced-motion` setting **or** an explicit toggle in the out-of-frame review toolbar (K-11 compliance — the review apparatus never enters the product surface). A permanent in-product setting would later live in أدواتي; that placement is the orchestrator's call. Prototypes must ship and be reviewable in **both** modes.

**Rule: reduced ≠ broken.** Every function stays reachable, every confirmation becomes textual, every gesture stays operable.

| Motion | Reduced alternative |
|---|---|
| Push / pop / edge-swipe settle | Instant swap; only scrim/dim fades ≤80 ms |
| Tab switch / pager | Instant swap; static peek retained |
| Sheet open/close | Instant present/dismiss; scrim 80 ms |
| Dialog | Opacity-only 80 ms (no scale) |
| Skeletons | Static blocks at fixed opacity + «جارٍ التحميل…» text |
| Saving highlight | Static bold amount + text confirmation; no tint pulse |
| Sync/offline morphs | Unchanged — they are already ≤120 ms local swaps |
| Pull-to-refresh | No rubber-band; fixed indicator + «تحديث…» text |
| Interactive gesture tracking | Kept — user-driven motion is the user's own |
| Haptics | Unchanged; verified separately (device-only) |

---

## 8. Haptic moments (documentation only — device-verification pending)

All rows are **device-verification pending** (V-03, V-04: no hardware has been touched in any delivery so far). Patterns are named generically across platforms; final selection happens at device verification. Haptics never substitute for visible states (C-04) — they only accent confirmed events.

| # | Moment | Suggested pattern (generic) | Intensity | Never fires when | Status |
|---|---|---|---|---|---|
| H-1 | Save success (receipt shown) | Success tick (iOS `.success` / Android `CONFIRM`) | Light | Save failed | Device-verification pending |
| H-2 | Variance warning (amount far off the row's typical range) | Warning thud (iOS `.warning` / Android `HEAVY`) | Medium | Routine saves; estimated values | Device-verification pending |
| H-3 | Selection ticks (segmented control, stepper, sheet detent snap, unit toggle) | Selection-changed tick | Light | Continuous scrolling / dragging | Device-verification pending |
| H-4 | Long-press menu opens | Light impact | Subtle | Menu cancelled | Device-verification pending |
| H-5 | Edge-swipe back commits | Soft tick | Light | Cancel path | Device-verification pending |
| H-6 | Pull-to-refresh triggers | Tick at threshold | Light | Passive overscroll below threshold | Device-verification pending |
| H-7 | Error presentation | **None** — calm-error doctrine | — | — | Recommended none; pending |

---

## 9. Handoff notes to the orchestrator (decisions this report recommends, does not finalize)

1. **Bottom destination bar persists during stack push/pop** as the continuity anchor (D-3); it is covered only under sheets/dialogs. Direction teams may override per direction, but each direction must then name its own single anchor per transition.
2. **Fade-through (P-7) and search-overlay (P-8)** are decisions-with-justification as mandated; both are RTL/LTR-identical by construction, which keeps the RTL-first contract clean.
3. **Row swipe actions:** recommend defer, or ship only the single non-destructive تعديل accelerator under the stated conditions.
4. **Sheet detent 56%** is validated only at 320/390 logical widths; keyboard avoidance and safe-area behavior on hardware are V-04 open items.
5. All ms values are contract *ranges* (§1.1) with nominals as defaults; prototype tuning may move within ranges, never outside them, and never past the 400/600 ms caps.
6. The haptics table is documentation until device verification; nothing in Stage 2 prototypes should claim haptic behavior as verified.
