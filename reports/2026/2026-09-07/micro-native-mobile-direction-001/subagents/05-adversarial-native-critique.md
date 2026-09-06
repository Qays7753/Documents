# 05 — Adversarial Native Critique: Seeds A / B / C

**Delivery:** `micro-native-mobile-direction-001`
**Stage:** 1 — Specialist 5 (Task 3-e), adversarial native critique
**Date:** 2026-09-07
**Author:** Specialist 5 — Adversarial Visual Critic

**Evidence base:** Stage 0 documents (`en/00`, `en/01`); direct inspection of both rejected artifacts — Warm Ledger (`.device` frame, bezel, simulated status bar, CSS view-switching, review controls around the phone) and Calm Ledger (typographic page wrapped in a desktop review console with 340px sidebar and scaled thumbnails); the fixed identity constraints.

**Standing warning.** Both rejected deliveries self-scored 7.90/10, 28/30, and VLM 8.5–9/10 — and were rejected. Every number below is a **risk score, not an approval**: my job is to intercept anything that passes technical checks yet still reads as "a web page displayed inside a phone frame."

---

## 1. The adversarial rubric

Twelve weighted pass/fail criteria, observable in a screenshot or two-minute hands-on — never in a component inventory. Total 100 points. Gate rule: **any criterion ≤4/10 fails the direction regardless of total**; the owner's verdict was categorical, not an average.

| ID | Pass question | Wt | Fail signature |
|---|---|---|---|
| C1 | Would this screen pass as an App Store screenshot of a major company's app in Micro's category? | 12 | News app, wallet app, or design case study |
| C2 | Does nothing only make sense as a web artifact (device bezel, status-bar simulation, review console, thumbnails, view-switching)? | 10 | One instance = fail |
| C3 | One navigation grammar: real destinations, a stack, visible back. Tab-removal test: strip the tab bar — still an app? | 10 | A scrolling document |
| C4 | Category integrity: unmistakably Micro (truth + operations), not POS/banking/wallet/ERP/dashboard? | 12 | Balance hero, checkout grids, KPI tiles, reading walls |
| C5 | One scroll context per screen, sheets and dialogs outside it? | 8 | Long page scroll, nested overflows |
| C6 | One-handed reality: primaries in the bottom 60%, 44/48px targets, credible at 320px? | 8 | Top-corner actions, hover-only affordances |
| C7 | Money typography: fixed tabular column, ASCII digits, two decimals, isolated digit run, «د.أ» in RTL flow? | 8 | Money in prose or centered display type |
| C8 | Arabic-first: RTL geometry designed, not mirrored; ≥13px Arabic; copy written, not translated? | 8 | LTR skeleton with Arabic poured in |
| C9 | Honest quiet states: empty/loading/unknown/offline/syncing designed? | 7 | Perpetually-successful dashboard |
| C10 | Restraint: Terracotta per measured roles, one primary per screen, logo once? | 6 | Washes, chip rain, repeated logo tiles |
| C11 | Surface discipline: sheets for short tasks, dialogs only for consequential binaries, keyboard-aware? | 6 | Everything pushed — or everything modal |
| C12 | Motion that explains: origin-anchored push/pop/sheet, 150–220ms, zero overshoot? | 5 | Bounce, number rolls, loops |

## 2. Applying the rubric to the seeds

Concept-level scores (0–10 per criterion, × weight/10 from §1): how safely each seed, **as specified and uncorrected**, clears the rubric.

| # | A «الخلاصة اليومية» | B «الدفتر» | C «الصندوق» |
|---|---|---|---|
| C1 | 7 | 8 | 6 |
| C2 | 6 | 8 | 7 |
| C3 | 8 | 8 | 6 |
| C4 | 7 | 9 | 4 |
| C5 | 5 | 8 | 7 |
| C6 | 6 | 8 | 8 |
| C7 | 6 | 10 | 7 |
| C8 | 7 | 8 | 6 |
| C9 | 6 | 7 | 6 |
| C10 | 6 | 8 | 5 |
| C11 | 6 | 7 | 9 |
| C12 | 7 | 6 | 6 |
| **Total /100** | **64.9** | **80.5** | **63.0** |

### Seed A — «الخلاصة اليومية» / The Daily Brief — 64.9

**Strengths.** It answers the real owner question («ما الذي تغيّر منذ أمس؟»); the collapsing large-title app bar is genuine native anatomy; a designed "nothing changed" state serves C9.

**Lazy failure mode: it drifts into a news feed.** The "what-changed narrative line" becomes templated prose — the canned «الخطوة التالية» noise the prior cycle rejected; the timeline becomes narrative cards; the position block demotes to a KPI tile; the whole surface becomes one long editorial scroll — the Warm Ledger failure wearing a nicer header. Atmosphere-only Terracotta risks a washed page where nothing looks actionable.

### Seed B — «الدفتر» / The Register — 80.5

**Strengths.** The list *is* the product: register-first means the home is the owner's working surface, not a summary. Fixed tabular money column, date-pinned sections, truth-bar as live filter, FAB in #964e33, zero cards — native-list DNA. Row swipe and long-press are mobile-only grammar — a web page cannot convincingly fake a swipe, making this the hardest seed to regress into web-in-a-phone. Almarai is an Arabic-first face; the دفتر name is the owner's own vocabulary.

**Lazy failure mode: a boring translated table.** If rows are hairline grays with truncated names and no tonal hierarchy, the register reads as every fintech's transactions list — generic and cold; the compact app bar gives no brand moment; swipe and long-press stay invisible unless demonstrated; static truth-bar figures degrade into a decorative stat strip.

### Seed C — «الصندوق» / The Counter Hub — 63.0

**Strengths.** Sheet-first is the most natively fluent interaction model of the three; the orders tab as operations seat is right; the day strip handles "the day" naturally; larger radii and tonal surfaces can read as modern platform design.

**Lazy failure mode: two big KPI cards pretending not to be cards.** لك / عليك as split counters plus a full-bleed cash hero is a consumer wallet's anatomy — a drift the prior cycle rejected and the brief repeats. Deep tonal washes are precisely the aesthetic CSS demos produce. A horizontally paging day agenda layered on tab navigation creates two competing grammars — the confusion web prototypes exhibit, not apps.

## 3. Kill tests

**A — "A digest is a content product; Micro is a truth product."** Most days are boring: either the digest pads itself with filler (canned narrative — immature) or honestly shows a near-empty screen (a dead home). The fix is self-defeating: bound the digest so it terminates, make timeline rows real register entries with actions, make the position block live and tappable. Apply all three and A converges toward B with narration on top — its weakest layer. **Verdict: fixable, but only by demoting the editorial voice; the digest may survive as a secondary surface, not the home's spine.**

**B — "A ledger list is what every fintech ships; it is generic by default."** True if executed as a gray data table — but that is a styling failure, not a category failure: nothing in B's anatomy is web-native or imitates a rejected category. The counter is identity: Arabic-first row grammar (subject anchored right, fixed amount column far left, mirroring the paper دفتر), honest status words («بانتظار التسليم», «متبقٍ 12.50»), warm ink hierarchy, a truth-bar that visibly filters, demonstrated swipes. **Verdict: not fatal — the strongest argument against B is answerable within its own anatomy.**

**C — "This is the best-executed wrong app."** The full-bleed cash hero with split counters is a wallet home on a KPI dashboard's skeleton; fixing it means demoting the hero, shrinking the counters into a filter bar, grounding the top in the running day — i.e., rebuilding it as B with C's sheets. What survives of C is interaction (sheet-first capture, the operations seat), not composition. **Verdict: fatal as specified; salvageable as parts.**

## 4. Mapping to the owner's vocabulary

| Owner's word | A | B | C |
|---|---|---|---|
| web-like | **High** — the editorial scroll is the prior failure's signature | Low — list/sheet/push anatomy is app-only | Medium — counters read as dashboard blocks |
| traditional | Low | Medium — a gray register can look old-fashioned; well-typed, the دفتر is an asset | Low |
| generic | Medium — feed chrome, digest cards | Medium — the transactions-list default | **High** — every fintech hero home |
| immature | Medium — generated narrative lines are a template tell | Medium — only if hierarchy is flat | Medium — tonal decoration reads as demo |
| coding-driven | Medium — log-assembled prose smells templated | Low — data-honest rows | **High** — tonal washes are CSS-demo aesthetics |
| not native | Medium — collapsing bar helps; the scroll page hurts | **Low** — swipe, long-press, FAB, push are mobile-only | Medium — paging risks a web-carousel feel |

## 5. Ranking and binding pre-build corrections

**Ranking: B (80.5) > A (64.9) > C (63.0).** B wins not because it is prettiest but because it is the only seed whose failure modes are quality problems, not category errors. A and C are nearly tied yet fail in opposite directions: A leans toward the *web-article* error, C toward the *wallet/dashboard* error — both adjacent to already-rejected categories. B's prototype must absorb the losers' strengths — A's bounded "what changed" line and quiet-day state as a register header, C's sheet-first capture and orders-as-operations seat — and must obey:

- **AC-01 — No mock hardware.** The app fills the viewport at 320/360/390/430 CSS widths; no bezel, simulated status bar, notch, or review chrome inside the viewport — review controls live in a separate `review-index.html` + URL parameters only.
- **AC-02 — Real navigation stack.** Four tab roots plus pushed detail screens (customer, order, entry, statement), visible back («رجوع»), scroll-state restoration on return; CSS view-switching as navigation is prohibited.
- **AC-03 — One navigation grammar.** List → detail push; bottom sheets for short tasks; no horizontal paging inside tab roots; dialogs only for consequential binaries.
- **AC-04 — The truth-bar is a live filter.** Tapping cash / لك / عليك filters the register with persistent selection state; figures change after a capture completes — proven in the flow, not asserted.
- **AC-05 — RTL-native row grammar.** Subject anchored right; fixed tabular money column (≥88px) far left; rows 56–64px; one Arabic action word per actionable row; leading-edge swipes (right in RTL) with a visible first-run hint.
- **AC-06 — Money contract enforced everywhere.** ASCII digits, two decimals, LTR-isolated digit run, «د.أ» in the RTL flow, `tabular-nums`, «—» at number size for unknown; never prose money.
- **AC-07 — Sheet-first capture.** The FAB (#964e33) opens the NumericSurface as a draggable, keyboard-aware bottom sheet; completion is a quiet receipt sentence stating the new cash position.
- **AC-08 — Honest states proven, not promised.** The prototype renders an empty day, an unknown amount, an offline/syncing state, and a cancelled/reversed pair — as real screens.
- **AC-09 — Restraint.** Zero cards on the home root; hairline separation; Terracotta per measured roles (atmosphere on soft surfaces; single primary #964e33; #b4613f press-only); the fixed logo appears once — app bar or profile.
- **AC-10 — Gate rule.** Any rubric criterion ≤4/10 on the built prototype blocks the review gate; all published scores are labeled risk assessments, never approvals.

## 6. What makes it feel like a major company's mobile product

1. **Confidence through restraint.** One decisive thing per screen, trusted; an app that shows everything it can do reads as a demo.
2. **One navigation grammar, held everywhere.** Predictability earns more trust than any visual flourish; every exception quietly costs it.
3. **Real back behavior with memory.** Back is always present, means the same thing, and restores scroll and filter state — its absence is the loudest "web page" tell.
4. **Money typography as identity.** A fixed tabular column, one money language, aligned digits on every screen — for a financial product, the numbers are the brand.
5. **Honest quiet states.** Empty, offline, unknown, and error as first-class screens; admitting what it does not know feels mature, fabricating zeros feels dangerous.
6. **Platform respect.** Safe areas, reach zones, keyboard-aware sheets, mirrored RTL geometry — respecting the device is how the app respects the owner.
7. **Motion that explains, never performs.** Origin-anchored push, pop, and sheet slide in a 150–220ms register; nothing bounces, spins, or celebrates.
8. **Arabic written, not translated.** Labels in the rhythm of the owner's speech — «دفتر الناس», «وين الكاش؟» — and geometry drawn RTL first, so Arabic feels native, not fitted.

---

*This critique treats the owner's rejection as the standing verdict: its scores rank risk, not beauty; its corrections are binding inputs for the orchestrator's decision; nothing here constitutes approval.*