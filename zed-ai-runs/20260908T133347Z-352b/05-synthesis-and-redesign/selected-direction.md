# Selected Direction — «دفء الحانوت / The Warm Counter» (as built)

**Run:** 20260908T133347Z-352b · **Status:** the ONE final direction of this run, as
delivered in `final/` and verified live. **This replaces no prior approved direction:**
the repository's earlier concept lineages (دفتر / طاولة / ميزان and sibling concepts)
never passed their approval gates and stayed staged; nothing approved was superseded.
This run's synthesis selected exactly one direction (decision D-01) and built it.

---

## 1 · What the direction is

A warm, composed, practical small-business product. Every Jordanian corner shop has one
counter — a warm wooden surface where money is counted and decisions land in seconds.
The direction is that counter: **warmth in the ground, decisiveness in the figures.**
The canvas is cream `#FAF9F5` like daylight inside the shop; one terracotta moment per
frame (`#CC785C` family) lands like the owner's stamp — placed once, on purpose; the
rest is ink and numbers. It is explicitly not «quiet beige administration», not a
monochrome-brown archive, and not a glossy AI gallery.

## 2 · Composition grammar (as enforced in the build)

Canvas-first: the page starts from `#FAF9F5`, never from a colored header or gradient;
the PrimaryValueBlock sits directly on the canvas (never carded). The loudness ladder is
fixed: 32/600 `ink-strong` value → 15/400 `ink` labels → one semantic state (chip or one
colored value) → the single brand moment → everything else muted. One vertical rhythm:
16px screen edge, 12px intra-group, 16–24px between blocks, 32px between sections;
spacing separates content before hairlines do (≤3 dividers). Capture actions live in one
horizontal snap rail with the first action tinted — a counter-top of taps, not a
dashboard grid (`.mc-rail`, 88×92 tiles, locked pitch 96px). The bottom nav is the only
persistent chrome (radius 0, edge-to-edge); the top zone is content with the single
Avatar profile entry. Money is always an LTR-isolated `bdi` island: English digits,
three-decimal fils, U+2212 minus, thousands comma, «د.أ» outside the run, end-aligned so
decimal points column-align by themselves.

## 3 · Surface logic

Exactly three planes: `canvas` (page) → `surface` (groups, sheets, dialogs, inputs, nav)
→ `sunken` (tracks, chips, icon wells, skeletons). Maximum two nested levels; no
`sunken` inside `sunken`; no white card inside a white card. Zero resting shadows —
elevation exists only during overlays (45% scrim + derived ink-12% sheet shadow, per
D-13, because the scrim edge alone is 2.96:1) and during press (8% ink veil). Semantic
tints are statuses, never a fourth surface. Pressable content is surface-backed so the
press veil never breaks text contrast (Agent 04's computed rule, D-07).

## 4 · Terracotta arithmetic

Per viewport exactly ONE filled brand-family element: **either** a `brand-ink` filled
CTA (white label, 6.11:1) **or** the `brand-tint` rail tile **or** an atmosphere identity
mark — never two. Text on atmosphere is `ink-strong` only (5.08:1); white-on-atmosphere
(3.28:1) and positive-on-positive-tint (4.27:1) are forbidden as text and appear in the
lab only as FAIL-verified rules. The nav indicator (24×3) and the avatar tint are
identity marks, not action surfaces. `#B4613F` does not exist in this system; every
color resolves through `tokens.css` verbatim.

## 5 · Energy sources

Energy comes from meaning, not paint: (1) signed money semantics — a green «+150.000»
against a red «−182.500» is the living state of the business (≤2 semantic families,
≤2 colored numbers per composition); (2) the one terracotta moment in the action
position; (3) tabular-figure texture — lining digits, fixed fils, decimal columns
stacked like a real counter ledger; (4) strict alignment (one text start, one money
edge, 12/16/24 rhythm); (5) 80ms press micro-motion — energy appears at touch, never at
rest. The check that lands in the CTA after «تم الحفظ», and numbers that change
discretely the moment a save completes, are the direction's proof of life.

## 6 · Anti-drift guardrails

**Not a SaaS dashboard** — no stat-card grid, no KPI tiles, no sidebar, no top app bar,
no default blue. **Not a paper ledger** — no ruled lines, no beige-on-beige, no
ornamental numerals; data lives on white surfaces over the cream canvas. **Not an AI
gallery** — no glass, gradients, glows, neon semantics or placeholder filler; every
example is a working بقالة النور truth (خالد الحوراني, مستودع زهران, تسوية برق) with
real states (متأخرة, بانتظار, معلّقة, محفوظ محليًا). First-glance acceptance: within
3 seconds at 320px the owner answers كم / ماذا تغيّر / ما يحتاج مني / أن أثق — enforced
by the ladder, not by reviewer goodwill.

## 7 · Where it lives

`final/micro-component-visual-library.html` (composition = the grammar live; components
= the matrices; foundation = the token truth; verification = the audited evidence),
`final/visual-direction.md`, `final/color-role-map.md`, `final/component-contracts.md`,
`final/tokens.css`, plus my rulings in `05-synthesis-and-redesign/decision-log.md`.
