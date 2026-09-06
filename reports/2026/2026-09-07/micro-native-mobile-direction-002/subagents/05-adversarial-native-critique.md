# 05 — Adversarial Native Critique

**Delivery:** `micro-native-mobile-direction-002` · Stage 1 · 2026-09-07
**Author:** Specialist 5 — adversarial visual critic (retry)
**Mandate:** research/critique only. No prototypes, no code. Rank and argue; the orchestrator decides.
**Inputs read:** `en/00-previous-work-lessons.md`, `en/01-intake-and-previous-work-audit.md` (only, by instruction). The three direction sketches (A/B/C) are taken exactly as the orchestrator stated them. I deliberately did not read subagents 01–04: a critic who has absorbed the other advocates' briefs argues with their conclusions, not against their directions.

**Ground rule:** the Stage-0 audit is not re-derived here. Buckets K/A/R are treated as settled ground truth. My job is to attack the three sketches *as they will actually be built in HTML*, on the single question that has killed this work twice: does it read as a web page assembled by code, or as a native product? Internal scores carry no authority (R-09 applies to my own report too — my ranking below is an argument, not a scoreboard).

---

## 1. The web-smell test — 12 criteria

Derived from the owner's exact complaint ("web pages displayed inside a phone frame"; "responsive web UI / dashboard / design-review artifact"). Each criterion is deliberately detectable in a **live prototype within 10 seconds** by a non-designer — that is the standard the owner implicitly set by rejecting work that passed 30-point rubrics. A prototype that fails any three of these on first open has already lost, whatever the deeper quality.

| # | Criterion | The 10-second test |
|---|---|---|
| W-01 | **Chrome-free document** — nothing pins, compacts, or shrinks; content scrolls like an article | Flick-scroll once. Did the top of the screen *do* anything? |
| W-02 | **Card-wall default** — primary surface built from stacked rounded boxes, not grouped rows on a canvas | Count boxes vs. rows at first paint. More than one box before content = smell |
| W-03 | **Device costume** — bezel, fake status bar (09:41), desktop stage, captions under the screen | Is anything on the page *not* app UI? |
| W-04 | **Review apparatus inside/near the product** — demo buttons, spec prose, annotated columns hugging the app surface | Where does the eye land first: the money, or the apparatus? |
| W-05 | **Navigation without consequence** — taps swap content in place (anchor jump, fade-in), no push slide, no stack | Tap a list row. Did a screen *arrive from an edge*, owning the viewport? |
| W-06 | **Back is a browser, not a stack** — back exists only as an in-page arrow or browser back | After two pushes: how do I go back one level with my thumb? |
| W-07 | **Sheet-less modality** — capture/add flows appear as new pages or inline expansions, not rising sheets with dimmed background and grab handle | Tap the primary capture action. Did a sheet rise, and can you dismiss it downward? |
| W-08 | **Dead scroll physics** — momentum stops hard at edges (overflow:auto tell), or the whole page rubber-bands including chrome | Overscroll at top and bottom. What bounces? |
| W-09 | **Platform-blind chrome** — no tab-bar behavior (translucency, pressed states), no safe-area logic; the bottom 80px is just a footer | Look at the bottom 80px. Does it know it's a phone? |
| W-10 | **Dashboard rhythm** — stat tiles, equal grids, chart panels; scanning happens in columns, not decision-lines | Does any screen read as a grid of things instead of a sequence of questions? |
| W-11 | **Motion as page behavior, not navigation behavior** — fades, assemble-on-load staggers, decorative loops; transitions not tied to push/pop/sheet/tab events | Navigate three times. Are all three transitions the *same grammar*? |
| W-12 | **Form-factor blindness** — full-width text lines, desktop spacing, hover-only affordances, primary action outside the thumb zone | Is the most important action where a thumb actually is? Any pointer-only interaction? |

Two meta-points. First, W-01/W-05/W-06/W-11 are the fatal four: they are what "web page assembled by code" *means*, and both rejected deliveries failed all four. Second, the test is asymmetric: a prototype can survive "generic" (W-10) but cannot survive a visible apparatus (W-03/W-04) — the owner reads apparatus as proof of the category error.

### 1.1 Exposure map — how the criteria attach to the history and to the three directions

| Criterion | 001 (rejected) | 002 (rejected) | A exposed | B exposed | C exposed |
|---|---|---|---|---|---|
| W-01 chrome-free document | medium | **fatal** | medium (if collapse is faked) | **high** | low–medium |
| W-02 card-wall default | **fatal** | low | low (inset groups ≠ cards) | low | **medium** (tonal stacking) |
| W-03 device costume | **fatal** | high | — (banned by Stage-0) | — | — |
| W-04 visible apparatus | high | **fatal** | — (banned by Stage-0) | — | — |
| W-05 navigation without consequence | high | **fatal** | low | **high** | medium |
| W-06 back is a browser | high | **fatal** | low | **medium** | low |
| W-07 sheet-less modality | high | high | low | low | low |
| W-08 dead scroll physics | high | high | medium | **medium** | medium |
| W-09 platform-blind chrome | high | **fatal** | low | **high** | low |
| W-10 dashboard rhythm | medium | low | low | low | **medium** (chips/tones) |
| W-11 motion as page behavior | high | **fatal** | medium | **high** (assemble-on-load) | low–medium |
| W-12 form-factor blindness | high | medium | low | medium | low |

Read the map honestly: Stage 0's hard bans (R-01/R-02/R-10) have already deleted W-03/W-04 *as design choices* — but they are also the criteria that re-fire fastest if any subagent's prototype drifts, so they stay on the checklist. What remains to be won or lost in Stage 2 is exactly where each direction is most exposed: A must not fake its collapse, B must not be a feed, C must not be a template.

---

## 2. Pre-mortem — direction A «السجل الهادئ / Quiet Ledger»

**Where it could still read as web / design-artifact.**
- **The clone can be skin-deep (W-05, W-11).** If A ships the iOS *look* (inset groups, large title, translucent bar) but the pushes are fades and the back is a chevron that runs `history.back()`, it is worse than a neutral direction: it is "a web page wearing an iOS costume" — precisely the owner's complaint with better makeup. iOS anatomy raises the promise; broken iOS anatomy breaks the promise louder.
- **Large-title collapse that doesn't collapse (W-01).** A static large title that was never "large" in a scrollable sense reads as a document H1 — this is exactly what killed 002. The collapse must be a scroll-linked behavior with correct timing, not a fixed header that swaps at a threshold.
- **Inset groups ≠ identity.** Inset-grouped lists are Apple's most generic surface. Strip the terracotta and A is indistinguishable from a thousand iOS apps. The owner asked for "a serious native product," not "an iOS clone" — A must find its distinctiveness inside the grammar (money typography, truth header, honest states) or it passes the smell test and fails the memorable test.

**Strongest native tell.** Working edge-swipe-back with fractional tracking + parallax push + translucent tab bar is the single most legible "this is a real app" signature on the market. No other direction has a floor this high: A's anatomy is *hard* to make look like a web page, because every element is chrome.

**Weakest point.** Distinctiveness, plus one RTL-specific trap: the sketch's "swipe-back from right edge" is correct for RTL (the back edge mirrors), but in an HTML prototype the right edge is also where iOS Safari's own back gesture lives. A half-working simulated swipe that sometimes loses to the browser reads as broken app, which reads as web-adjacent jank.

**Verdict: PASS (conditional).** Highest nativeness floor; its risks are execution risks with known fixes, not concept risks.

**What the 10-second test returns if built correctly:** tab bar with translucent behavior + large title that visibly collapses on the owner's first flick + a push that slides with parallax when the owner taps a row. Three native signatures in ten seconds; the owner's "app or page?" question answers itself. If built incorrectly: static large title + fade on tap = Settings-styled document, and the costume critique applies with interest.

**Three mandatory fixes.**
1. **Ship the motion stack or downgrade the promise.** Push transitions must be slide-with-parallax (incoming 100→0, outgoing −30→0, ~350ms, platform curve), back must be the reverse, and large-title collapse must be scroll-linked pixel-for-pixel. If interactive edge-swipe back cannot be made reliable in the review browser, replace it with a visible RTL back affordance + full slide-back transition and *say so in the review guide* — a stated limitation is native honesty; a broken half-swipe is a web tell.
2. **Make the truth structural, not a hero row.** صندوق / لي / عليّ live in a per-tab persistent header region that compacts with scroll (title collapse and truth collapse are one system). Money is the typographic identity: tabular figures, isolated digits (K-05), the fixed decimal-aligned column (A-03) rendered as row anatomy — not a styled block floating in a list.
3. **Differentiate inside the grammar.** Warm-neutral canvas tuned away from stock `systemGroupedBackground` (A-05 gives license); honest-state glyph+label rows (K-04) as the visible signature; hairlines only, zero cards on primary surfaces. The screen must be recognizable as Micro *because* of its rows, not recognizable as iOS Settings with warm paint.

---

## 3. Pre-mortem — direction B «موجز اليوم / The Daily Brief»

**The mandated interrogation: native or stylized web feed?** Honest answer: **B is the direction most likely to produce the third web-page rejection if its chrome under-delivers, and the most distinctive product if it doesn't.** A hub with no tab bar has real native precedents, but every one of them is native because of *behavior*, not layout: the top region pins and compacts like an app bar, modality is sheets, back is edge-swipe with preserved hub state, and the bottom pill behaves like a keyboard accessory. If those four behave, B reads as a mature single-surface app. If the pinned header is a sticky div and the "narrated brief" rows scroll like an article with chips — B is an editorial website, and W-01/W-04/W-11 will all fire within 10 seconds of the owner's scroll.

**Where it could still read as web / design-artifact.**
- **Assemble-on-load is a landing-page move (W-11).** The staggered once-only assemble motion is exactly what designed marketing pages do; a native app is *assembled before you look at it*. "Once-only" helps; but on every review reopen it plays again — the owner will see it twice in a 3-minute review, which is already too clever.
- **Destinations as text (W-05, W-06).** Header figure taps and a "sections sheet" are fine *if* they push full-screen with stack slides and return via edge-swipe to a scroll-position-preserved hub. If figures are underlined-styled text rows or the sheet's items do in-place swaps, B becomes an SPA menu.
- **No persistent chrome = 10-second ambiguity (W-09).** On first open, B shows *no* unmistakable app chrome. A reviewer's first 10 seconds are an editorial screen with numbers. It takes 15–30 seconds of interaction before B's app-ness becomes visible. That is a real, measurable handicap against the owner's spontaneous "app or page?" reaction.

**Strongest native tell.** The bottom capture pill behaving as an input accessory + capture-as-sheet + the three truth figures as compacting header chrome. Also the best *product* fit: this owner checks "what happened today" before anything else — B is the only direction whose home screen answers the owner's first question of the day in the owner's own sentence rhythm.

**Weakest point.** Discoverability and orientation. With no tab bar, the four destinations exist only in the user's memory; nothing at rest shows the app has parts. For the daily check this is fine; for "أين المال؟" and Operations history it demands the owner learn that header figures and the sheet are the navigation. That learnability cost is acceptable in a real installed app (you learn it once) but is *amplified in a browser review*, where there is no icon on a home screen to anchor the product's identity.

**Verdict: RISKY.** Highest variance. B should only be built if the team commits to chrome-first behavior; half-built B is the most fatal of the three.

**What the 10-second test returns if built correctly:** the owner flicks once, the truth header visibly compacts and grows a hairline, taps «صندوق», and a full-screen surface slides in over the hub. App-ness proven in one scroll + one tap — but note that this requires the owner to *do* something. If built incorrectly: the header sits still, figure taps swap content beneath it, and the staggered assemble motion plays — an editorial landing page with numbers, failing W-01/W-05/W-11 inside ten seconds.

**Three mandatory fixes.**
1. **Prove the chrome in the first three seconds.** The pinned truth header must visibly compact on the first flick (hairline + background opacity + height change), and all three figures must have real pressed states and push full-screen with stack slides. If the owner does nothing but scroll once and tap one figure, they must already have seen: app bar behavior + push transition. Those are the two 10-second proofs.
2. **Demote the assemble motion to meaning.** Total stagger ≤ 200ms, once per session, tied to data arrival — or cut it entirely (K-08/A-09 register: motion is meaning, never showcase). Never replay on navigation returns; the hub must reappear exactly as left.
3. **Give the hub a native memory aid and a comparison contract.** The sections sheet must open from a persistent, discoverable control and list destinations in the same order as A/C's tab bar, so the three directions remain comparable on IA. And the hub must survive pushes untouched (scroll position, sheet dismissal state) — a hub that resets on back is a web SPA tell.

---

## 4. Pre-mortem — direction C «مساحات العمل / Working Surfaces»

**The mandated interrogation 1: Material-genericness.** M3 is the most-cloned design system on the planet, and its vocabulary — FAB, filter chips, tonal surfaces, container-transform — is *also* the current fashion in web apps. A terracotta-recolored M3 reads as native, but anonymous: "a Google app with custom colors." That is a lesser sin than web-ness (a native generic app passes the owner's letter of the complaint) but it forfeits "a serious product from a major company," which implies an *owned* identity. C's identity must come from Micro content — honest states, aging relationship bars, the truth header — or C is a template.

**The mandated interrogation 2: pager vs. swipe-back at 320px.** This is a real conflict, not a nitpick. A horizontal pager on the first three destinations consumes the same gesture space as the RTL edge-swipe back (right edge). At 320px there is no room for disambiguation: a thumb starting mid-screen with slight diagonal drift will trigger the wrong system roughly half the time. The standard native compromise (pager swallows horizontal moves, edge zone keeps back) requires reliable touch edge detection and velocity disambiguation — the two things HTML prototypes are worst at. And C already has three navigation systems (bottom nav + pager + back); every one that misfires *once* in front of the owner produces a jank moment that reads as "web page with touch handlers." That is the complaint, reintroduced through the back door.

**Where it could still read as web / design-artifact.**
- **Chips + tonal surfaces are 2024+ web-app fashion (W-02, W-10).** Filter chips and stacked container tones are what modern *web* dashboards wear. If chips appear on first paint, the 10-second read is "modern web app," full stop.
- **Compacting header that scrolls away with the pager (W-01).** If the sticky truth header only pins per-page and the pager swipe moves the money off-screen, the pager hides the product's reason to exist.

**Strongest native tell.** FAB container-transform into the capture sheet — the single most recognizable Material-native signature motion. Done correctly it is unmistakable "real Android app" language, and it lands the capture action in the perfect thumb zone (K-12).

**Weakest point.** Gesture reliability in the delivery medium, and anonymity.

**Verdict: RISKY.** Recoverable — but only by cutting, not tuning: the pager and the first-paint chips must go.

**What the 10-second test returns if built correctly:** bottom nav with real pressed states + FAB that container-transforms into a capture sheet on first tap. Two unmistakably Material-native moments. If built incorrectly: chips on first paint + a pager that half-fires when the owner means to go back = "modern web app with touch handlers" — the complaint, re-armed.

**Three mandatory fixes.**
1. **Resolve the gesture conflict by decision, not by hope.** Either (a) drop the pager — bottom nav + edge-swipe back only — or (b) keep the pager and make the pager's swipeable area exclude a documented edge zone, stating the tradeoff in the review guide. Do not ship both half-working. My recommendation as critic: (a) — the pager adds no information the bottom nav doesn't already carry, and it spends the scarcest resource in an HTML prototype: gesture credibility.
2. **De-template the M3 vocabulary.** No chips on first paint; tonal surfaces only where hierarchy demands (capture, states), never as stacked boxes (W-02); aging relationship bars as structural row anatomy with real width-legends, not decorative progress bars. Terracotta stays scarce and structural (R-06 discipline).
3. **Pin the truth across the whole surface.** The compacting header must persist across destination switches (including any pager movement), with measured heights (e.g., 96→56px) and the three figures always tappable. The money must never scroll away — that is the product's truth-at-the-center promise rendered as chrome.

---

## 4.1 Non-negotiables every direction inherits (regardless of ranking)

The pre-mortems above attack what differentiates A/B/C. This list attacks what they share — the failure of any one of these is a rejection no ranking survives, so they are checked per direction, per screen, in Stage 2 QA:

- **Honest states first-class (K-03/K-04):** at least one unknown («قيمة غير محددة بعد»), one estimated (تقديري), and one syncing/conflict surface visible somewhere in each prototype; never color-alone.
- **Bidi contract (K-05/K-06):** `<bdi dir="ltr">` digit isolation, «د.أ» after the number in RTL flow, ASCII tabular digits, no parentheses around money.
- **Legibility floors (K-07):** ≥13px Arabic, 15px body, ≥56px rows, line-height ≥1.6, zero letter-spacing on Arabic — at 320px first.
- **Thumb discipline (K-12):** primary capture in bottom reach, 44/48pt targets, safe-area respect.
- **Review hygiene (K-11/R-01/R-02/R-10):** product frame contains product UI only; apparatus lives in the review index and a clearly external toolbar; no bezel, no fake status bar, no spec prose near the screen.
- **Score silence (R-09):** no numeric verdicts inside any prototype or review artifact.

---

## 5. Ranking — with the reasoning shown

Decided by argument; the table only records it. If you read the numbers as the decision, you have misread this section (and repeated R-09).

| Direction | Verdict | Nativeness floor | 10-second read | Distinctiveness | Gesture credibility in HTML | Product-ritual fit |
|---|---|---|---|---|---|---|
| **A Quiet Ledger** | PASS | Highest | Instantly an app | Medium — must be earned in-grammar | High (nav taps are reliable; swipe-back is the only fragile piece) | High |
| **C Working Surfaces** | RISKY | High | Instantly an app | Low-medium — M3 anonymity | **Low** (pager vs. back at 320px) | High |
| **B Daily Brief** | RISKY | Medium — conditional on chrome | **Ambiguous** — needs interaction to prove app-ness | Highest | Medium (no pager conflict; edge-back critical) | **Highest** |

**1st — A.** The failure that killed this work twice is web-smell, and A is structurally the hardest direction to make smell like web: its every element is app chrome. Its weakness (anonymity) is a polish problem, soluble inside the grammar (fix A-3), and it is the only direction whose worst realistic outcome is "competent native app" rather than "another rejection." In a two-strikes situation, you build the direction with the highest floor first. Its conditional is strict: the motion stack is not decoration, it *is* the direction — A without real push/collapse/swipe mechanics is a costume and must not be shown.

**2nd — C.** Its 10-second read is as convincing as A's, and the FAB container-transform is the best single native moment available. It ranks below A only because its two risks are *concept-embedded*: the pager conflict is designed into the sketch (fixable only by amputation), and M3 recoloring starts from anonymity, one recolor further from Micro than A's blank iOS canvas. With fix C-1 (drop the pager) and C-2 (no first-paint chips), C is a legitimate co-finalist; without them, it will produce one jank moment per review — and jank is how "web page assembled by code" smells from inside a browser.

**3rd — B.** The best product idea and the highest ceiling: the narrated daily brief in the owner's own sentence rhythm is the only home screen among the three that answers the owner's actual first question of the day, and it is the only direction that doesn't lean on a platform's borrowed clothes. It ranks third for one measurable reason: **it fails or blurs the 10-second test by construction.** No persistent chrome means the first spontaneous impression is "editorial screen with numbers," and this owner has already proven willing to reject good work on the spontaneous impression. B should be built only as the *second* prototype of the session, never first, and only with all three B-fixes non-negotiable. If its chrome lands, B may win the owner's heart on day two of use — but the gate here is a first session in a browser, and B's first 10 seconds are its weakest 10 seconds.

**A closing argument against my own ranking.** If the review condition were "a week of real use on the owner's phone," B would rank first: daily-brief intimacy compounds, tab bars don't. The ranking above is honest *for this gate* — a browser-based first session where the 10-second read and gesture credibility dominate. The orchestrator should weigh that context explicitly: choosing B is choosing to win a later gate at higher risk at this one.

### 5.1 What would change this ranking (falsifiability)

A ranking that cannot be wrong is an opinion, not a critique. These are the observed conditions under which I would reorder:

- **A drops below C** if A's swipe-back cannot be made to work *or be honestly disabled* in the review browser, while C drops its pager cleanly — a broken native signature beats no native signature only when the break is visible; an invisible break is just jank.
- **B rises above C** if the orchestrator commits to sequencing the review session B-first with a pre-briefed owner ("this one has no buttons at the bottom — that is the point"), which neutralizes B's 10-second handicap by instruction rather than by luck.
- **Any direction falls to FAIL** if its prototype replays assemble motion on every navigation, resets hub scroll on back, or shows a chip/card/box on first paint — those are not polish gaps, they are the complaint returning.

---

## 6. Review-gate standard — experiential questions for the owner

Asked one direction at a time, in the owner's own words, **no design vocabulary, no leading questions** ("doesn't this feel native?" is forbidden — it teaches the answer). Before any question: open the prototype fullscreen (remove browser chrome — see §7) and let the owner use it unguided for 60 seconds.

**Interview discipline.** Ask in the order Q1→Q6 and do not skip Q1: it is the only question that reproduces the spontaneous condition under which both previous deliveries died. Record the owner's *first words* verbatim before any elaboration — the first sentence is the data; the second sentence is negotiation. If the owner asks "is this the final design?", answer honestly (it is a direction prototype) — but note that the question itself is a soft rejection signal: a native-feeling product does not prompt the category question.

| # | Question (plain Arabic register) | Approval sounds like | Focused rejection sounds like |
|---|---|---|---|
| Q1 | After half a minute — were you using an app, or looking at a page? | "An app" — immediate, unelaborated | Any of: صفحة، موقع، تصميم، عرض — or hesitation before answering |
| Q2 | Where did your eyes go first? | Names a money figure or a transaction | Names the frame, toolbar, caption, or "the presentation" |
| Q3 | Open a transaction, then come back. Did that movement remind you of any app you already use? | Names a real app (iPhone, WhatsApp, any bank app) | "Like clicking a link on a site" — or no navigation memory at all |
| Q4 | If I handed you this phone right now to record a sale, where would you press? | Immediate correct answer, thumb-zone action named | Searching, pointing at the wrong element, or "I'd have to try" |
| Q5 | Do you believe these numbers? Anything that feels fake or demo-ish? | Reads as a real ledger; trusts unknown/estimated honesty | "It's a demo," "where's the real data," anything that feels staged |
| Q6 | Is this *Micro* — or could this be any app? (distinctiveness probe) | Recognizes its own business in the content and its grammar | "Any app" — record as a distinctiveness rejection, separate from web-smell |

**Gate outcomes, defined exactly:**
- **Approval** = owner names one direction unprompted as "this one" AND Q1–Q5 land in the approval zone for that direction. Q6 alone does not block approval, but is recorded as a Stage-4 identity obligation.
- **Focused rejection** = the owner's own words contain web/dash/presentation vocabulary (Q1/Q2), navigation fails Q3/Q4, or staging fails Q5. Focused rejection must return *named elements*, not moods — the review guide must ask "which screen, which element" so Stage 2 can fix rather than restart.
- **"This part of A + that part of B"** is not approval. It is a legitimate composite, but it re-opens synthesis, and the composite must itself pass this same gate before Stage 4. No composite inherits approval from its parents.
- **"I need to see it on my phone"** is a defer, not a rejection — but it is *blocking*, and it means the gate has not been passed, whatever the enthusiasm.

---

## 7. Residual risks that survive every fix — said plainly

These are limits of the HTML review medium. No amount of prototype craft removes them; the owner must be told, once, in the review guide, what is being suspended or deferred.

1. **The URL bar will be visible.** However good the prototype, the owner first sees an app *inside a browser*. The single highest-leverage review decision is environmental: fullscreen/add-to-home-screen mode, native browser chrome hidden, orientation locked. If the review opens in a plain tab, the gate is compromised before the first question. This belongs in `en/03` and `en/04`, not in the prototypes.
2. **Keyboard avoidance cannot be honest.** HTML cannot reproduce real keyboard insets and scroll-avoidance on the review device. The capture sheet can *simulate* the layout shift, but on a laptop review the whole dimension is absent. Owner must suspend: "how saving *feels* with a real keyboard" is unanswerable at this gate. Prototype must state in-frame (outside the product surface, per K-11): *keyboard behavior simulated; verified on device at Stage 4.*
3. **Haptics do not exist.** Quiet completion (K-08) is half visual, half physical on a real device. Every "saved" moment will be visual-only here. Owner must suspend: whether completion *feels* finished — the closure sentence and final digits are reviewable; the physical settle is not. Do not fake it with vibration APIs where available: browser vibration is a different sensation and will read as cheap.
4. **Scroll physics are approximate.** Momentum curves, rubber-banding, and especially nested scroll-ownership (pinned truth header inside a scrolling body) are approximations. Worst case: an overscroll-chaining bug exposes the page behind the app — the one moment where the prototype *literally* becomes a web page. Mitigate (locked viewport, full-bleed app container), but a rare leak may occur; pre-brief the owner so one glitch is read as medium, not design.
5. **Edge-swipe back fights the browser.** On iOS Safari and Android gesture nav, the browser's own edge gesture can win, exiting the review entirely. The prototype must claim the edge where possible, but the owner may occasionally leave the app "sideways." Pre-brief, one sentence: "if the screen slides away, come back the same way." Note the asymmetric exposure: A and B lean on edge-swipe as a native signature; C (after fix C-1, pager dropped) depends on it least. If the review device is an Android with 3-button navigation, the conflict disappears — check the device before the session and record it in the review evidence.
6. **Blur cost on cheap Android.** Translucent bars depend on backdrop blur; on the low-end devices this owner class likely holds, blur can stutter, and a stuttering translucent bar reads as broken, not native. Every translucency must have a solid fallback, and the fallback must be tested at 320px.
7. **First-paint font flash.** Arabic web-font loading can flash a fallback glyph shape for a moment — a small but genuine "web page" tell on the very first open. Preload/subset; accept that first open may cost one blink.
8. **And one non-medium risk:** scores. If any subagent report, synthesis, or review guide reintroduces numbers as authority (7.9/10 energy), this delivery repeats the exact failure it was created to avoid. §5's table is a record of argument, not a verdict-generator. The gate is the owner's answers to six questions, nothing else.

9. **Review-condition risk, stated as a duty.** Every item above is survivable *if pre-briefed* and corrosive *if discovered*. One paragraph in the review guide — "what you cannot judge today: keyboard, vibration, and scroll feel are simulated; judge structure, honesty, and navigation" — converts all five medium risks from hidden liabilities into declared scope. The delivery that says plainly what it cannot show is the delivery that has earned the right to be believed about what it does show (K-14 applied to the review itself).

---

*End of report. This critic ranks A > C > B for this gate, with the explicit caveat in §5 that B wins a different gate. The orchestrator decides.*
