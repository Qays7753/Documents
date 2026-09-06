# Visual Research and Benchmark Analysis

**Delivery:** `micro-visual-product-concept-002`
**Task ID:** 2-a
**Agent:** Sub-agent 1 — Product Visual Research and Benchmark Analyst
**Date:** 2026-09-06
**Basis of analysis (honesty label):** Mixed, and labeled throughout. (1) **Live web research WAS performed** on 2026-09-06 — ten targeted searches via the web-search function; exact queries are listed in §1. Live results are descriptive/secondary sources (product pages, app-store listings, UX-research articles); **no screenshots or first-party design specifications were visually inspected.** (2) The local Phase 2 research digest (24 cited sources) is the evidence base for market behavior. (3) Product-behavior characterizations of named apps are **knowledge-based analysis** except where anchored to a digest or search result, in which case the source is named inline. No research is claimed that was not performed.

---

## 1. Method and evidence base

Read in full before writing this report:

- `worklog.md`, Task 2-0 entry — shared context brief (product identity, fixed Terracotta palette and contrast role rules, anti-patterns, binding content rules, honesty rules).
- `en/00-SOURCE-INTAKE-REPORT.md` — source register S-1…S-8 and constraints C-01…C-20.
- `en/01-current-work-lessons.md` — the 12-row lessons table of what must not return.
- `reports/Micro-Target-State-Design-Report.md` §0, §3.1, §4.0–§4.5, §4.13, §4.14 — screen contracts, thumb-zone model, JOD/RTL binding rules, the 12-state vocabulary, density critique.
- `scripts/research_digest.md` — Phase 2 benchmark research digest (sections used: `khatabook`, `okcredit`, `whatsapp-biz`, `cod-mena2`, `jordan-mobile`, `jordan-msme`, `jordan-informal`, `jordan-smefinance`, `jordan-wallets`, `recordkeeping`, `wb-practices`).

**Absent and not claimed:** `micro-agent-input.zip`, `micro-recovery-docs.zip`, and `MicroPrimitives-anti-reference.html` were not found in the repository (S-6, S-7, S-8). No content of those packages is invented or characterized beyond the prompt's own description.

**Live searches performed (exact queries):**

1. `Khatabook app user interface design digital ledger merchant screen`
2. `OkCredit OkSupplier app design udhar bahi khata merchant interface`
3. `mobile banking fintech app number typography tabular figures design best practice`
4. `Monzo Revolut mobile app balance screen design information hierarchy`
5. `mobile app empty states error states offline design best practices financial apps`
6. `WhatsApp Business catalog orders small merchants commerce interface features`
7. `open source mobile banking finance app design system github repository`
8. `delivery tracking app order status timeline UX design pattern mobile`
9. `Wave Square small business finance invoicing mobile app UX design`
10. `thumb zone reachability one handed mobile phone use study 49% hard to reach`

**Digest quality note:** the digest's `cashflow-anxiety` section returned low-relevance results and was not used as evidence. No claim in this report rests on it.

---

## 2. Benchmark analysis

Eight pattern families. For each: what the family is, how the strongest products solve it, and a per-pattern table (Pattern | Who does it well | What it solves | Transfers to Micro? | What does NOT transfer | Risk if copied blindly).

### 2.1 Digital ledger / debt-book apps (Khatabook, OkCredit)

The closest category to Micro's «دفتر الناس». Khatabook reports 5 Cr+ businesses on its free apps [khatabook.com, search 1] and is described consistently as "simple and familiar," a ledger of adding and deleting entries against customer names [strivemindz.com; medium.com, search 1], with reports, reminders, and UPI/QR collection [smarther.co, search 1]. OkCredit's differentiator is explicit: "build trust with customers by automatically sharing account balances instantly after every transaction," plus detailed reports and statements [apps.apple.com, search 2 — also in the digest]; real-time ledger visibility is its pitch [mwm.ai, search 2]. Khatabook runs in 11 languages [inc42, digest].

| Pattern | Who does it well | What it solves | Transfers to Micro? | What does NOT transfer | Risk if copied blindly |
|---|---|---|---|---|---|
| Name-first party rows (party name → balance → action) | Khatabook, OkCredit | Owners index their book by person, not by document | **Yes** — دفتر الناس is exactly this shape; «حصّل» belongs in the row | Their payment-request button (needs a payment rail Micro does not have) | Row becomes a collections-pressure tool; tone turns coercive |
| Per-party balance as the screen's dominant figure | OkCredit | "How much am I owed by this one person" in one glance | **Yes** — for PartyDetail / collection surfaces | — | Minimal |
| Statement sharing as the trust object | OkCredit (auto balance share) | Reconciliation without confrontation; two parties see the same truth | **Yes, conceptually** — Micro's equivalent is the closure sentence + «كشف الأسبوع» StatementView | The outbound messaging channel itself (Micro has none; must stay honest about that) | Faking a share loop that does not exist |
| SMS/payment reminders | Khatabook | Chasing receivables at scale | **No** | Reminder spam erodes the calm-trust identity; Jordan runs on WhatsApp, not SMS | Micro acquires debt-collector tone |
| Superapp sprawl (loans, UPI, inventory marketplace, invoices) | Khatabook | Monetization after free-ledger acquisition | **No** | Monetization via lending/payments is a different business model; Micro records reality, it does not move or lend money | Feature sprawl recreates the crowded, unedited feel already convicted in the lessons table |

### 2.2 Lightweight conversational commerce (WhatsApp Business)

The owner's actual daily tool. Catalogs live inside the conversation with no external redirects [developers.facebook.com, search 6]; each item carries price, description, product code [botscrew.com, search 6]. Regional reality: WhatsApp penetration exceeds 80% of the adult population in Gulf states [hyperleap.ai, digest] and is the dominant customer-engagement channel in the Middle East [whatsable.app, digest].

| Pattern | Who does it well | What it solves | What transfers | What does NOT transfer | Risk if copied blindly |
|---|---|---|---|---|---|
| Radical entry lightness (message = the record) | WhatsApp Business | Zero-friction capture in the moment | **Yes** — the shape, not the surface: FAB «سجّل» ≤3-field sheet with amount-first is the correct analog | Chat bubbles as financial UI | — |
| Chat thread as the record of truth | WhatsApp | Conversational context | **No** | Ephemeral, unstructured, totals unsearchable; financial truth needs rows, dates, states | Micro becomes a transcript, not a ledger |
| Name-indexed contact list as navigation | WhatsApp | Find the person, not the document | **Yes** — دفتر الناس browses like contacts | Presence/status indicators | — |
| Catalog card grid inside a thread | WhatsApp Business | Show what you sell without a website | **Partially** — منتجاتي وخدماتي is a reference list, not a storefront; rows over tiles | Storefront commerce framing (buy buttons, carts) | Micro reads as a shopfront app, not an operations record |

### 2.3 Small-business finance mobile apps (Wave, Square Invoices, QuickBooks mobile)

Wave's mobile app centers on invoice status — sent, viewed, paid — with notifications when paid [play.google.com, search 9]. Square Invoices pairs estimate → invoice → payment [apps.apple.com, search 9]. QuickBooks mobile (knowledge-based) compresses a desktop accounting product into reconciliation-first screens.

| Pattern | Who does it well | What it solves | What transfers | What does NOT transfer | Risk if copied blindly |
|---|---|---|---|---|---|
| Lifecycle status chips (sent / viewed / paid) | Wave, Square Invoices | Answer "where is this money?" without opening anything | **Yes** — Micro's order lifecycle (مسودة → اتفاق → تنفيذ → تسليم → تحصيل) as small named states | Their statuses assume an outbound document pipeline | Status vocabulary drifts away from owner language (C-15) |
| Receivable-first hierarchy ("who owes me" before reports) | Wave (knowledge-based), OkCredit | Cash collection is the daily anxiety | **Yes** — position of «لي عند العملاء» above period readings | — | — |
| Notification-on-paid closure | Wave | Confirms the money event | **Yes** as an in-app quiet closure sentence, not a push notification | Push notification chrome (E-00.14) | Attention-app feel |
| Estimate → invoice bridge | Square Invoices | Thinking tool flows into commitment | **Yes** — already Micro's estimate → draft bridge | Document aesthetics: PDF-like headers, logo blocks, "pay now" buttons | Micro promises a payment rail it does not have |

### 2.4 Neobank account composition (Monzo, Revolut, Nubank, Starling)

The best-studied family for "one screen, one money question." Their conventions: balance, recent transactions, and the primary action on the first screen [lollypop.design; orbix.studio, search 4]; deep-dives document sub-accounts, payment gestures, and gamification as their signature moves [flatstudio.co, search 4].

| Pattern | Who does it well | What it solves | What transfers | What does NOT transfer | Risk if copied blindly |
|---|---|---|---|---|---|
| One dominant balance figure + signed delta | Monzo, Starling | Instant position reading | **Yes** — Micro's each-screen question (cash now, owed to me, owed by me) earns exactly one dominant figure | Account/product switching headers | Position reads as bank balance → implies custody Micro does not provide |
| Sub-accounts / "pots" | Monzo, Revolut | Money partitioned by purpose | **Yes** — this is Micro's wallets (الدرج…) and allocation logic, already designed | Savings-goal framing and round-ups | Wallets become gamified budget toys |
| Statement / period view | Monzo | Period truth in one scroll | **Yes** — «كشف الأسبوع» StatementView | — | — |
| Payment gestures (swipe-to-pay) | Revolut | Speed for frequent payments | **No** | Micro's writes are records, not transfers | Implies money movement |
| Gamification (streaks, badges, goal meters) | Revolut, monobank | Engagement metrics for consumer fintech | **No** | Audience mismatch: the owner's uncertainty about cash is a real anxiety, not a game | Trivializes money; breaks "financially serious but emotionally comfortable" |

### 2.5 Banking apps — negative/limited reference only

Banking apps are included because owners see them (JoPACC processed 224.62M transactions in 2024, +77.2% [jopacc.com, digest]) and will bring their expectations — but Micro is not a bank and must not borrow its visual authority.

| Pattern | Who does it well | What it solves | What transfers | What does NOT transfer | Risk if copied blindly |
|---|---|---|---|---|---|
| Honest unavailability language | Multiple (debated at ux.stackexchange, search 5) | Not spinning missing data | **Yes** — Micro's «غير متاح» / «—» wording discipline is stronger than most banking apps | — | — |
| Login/security-first first screen | Retail banks | Custody framing | **No** | Micro is local-first; its privacy line ("بياناتك على هذا الجهاز فقط") is the honest equivalent | Custody theater; false institutional promises |
| Product cross-sell carousels, card art | Retail banks | Sales | **No** | Business model mismatch | SaaS-banking hybrid look; density inflation |

### 2.6 Delivery / status tracking patterns (NN/g, Baymard)

The relevant research distinction: **status trackers are pull; progress updates are push** [nngroup.com, search 8]. Baymard's corpus of 165 order-tracking pages confirms the mature shape: discrete named steps, latest state emphasized, next action attached [baymard.com, search 8].

| Pattern | Who does it well | What it solves | What transfers | What does NOT transfer | Risk if copied blindly |
|---|---|---|---|---|---|
| Pull-based status tracker with named discrete states | NN/g guidelines, e-commerce tracking | "Where is this?" answered without alerts | **Yes** — matches E-00.14 (attention lives in source rows, no bell) | Courier/driver assignment | — |
| Action-specific step labels | Baymard examples | The tracker tells you the next move | **Yes** — «سلّم / حصّل / أكمل» in today-rows is the same principle | — | Canned next-step noise (already convicted in lessons) |
| Live map + ETA countdown | Delivery apps | Logistics telemetry | **No** | A home business with 1–3 active orders has no fleet; logistics theater inflates perceived complexity | Micro looks like a courier app; states get dramatized |

### 2.7 POS apps — negative reference (Square POS, knowledge-based)

Square's surface is a counter clerk's tool: item-button grid, cart, checkout flow, receipt printing, cash-drawer chrome [squareup.com, search 9].

| Pattern | Who does it well | What it solves | What transfers | What does NOT transfer | Risk if copied blindly |
|---|---|---|---|---|---|
| Item-tile grid as home | Square POS | Speed-of-line order entry | **No** | Micro's sales are amount-first, item-optional, often recorded after the fact | «العمل» or Home becomes a till; recording feels like staffing a register |
| Checkout-first flow | Square POS, Square Invoices | Take payment now | **No** | «سجّل» is a recorder, not a till — the fast path has one field (amount), not a cart | Implies payment processing |
| Receipt-printer aesthetics | Square | Physical receipt parity | **Partially** — only as the *verbal* rhythm of closure sentences | Paper-mime visual styling (perforation edges, monospace ledger styling as decoration) | Skeuomorphism contradicts "modern but not trendy" |

### 2.8 Money typography and number communication (fintech typography practice; YNAB/Copilot)

The most directly transferable family. Fintech typography practice is explicit: numbers render as a single text string, rely on **tabular figures**, and **keep trailing zeros** (`54.00`, not `54.34`-style truncation) so columns align and change detection works [medium.com, search 3]; tabular figures wherever numbers align [theskinsfactory.com, search 3]; consider a dedicated numeric face with multilingual safety [telerik.com, search 3]. Personal-finance apps (YNAB, Copilot — knowledge-based) communicate money as plain, large, unambiguous figures with color reserved for direction/state, never decoration.

| Pattern | Who does it well | What it solves | What transfers | What does NOT transfer | Risk if copied blindly |
|---|---|---|---|---|---|
| Tabular lining numerals + fixed 2 decimals | Banking/fintech practice [medium; skinsfactory] | Column alignment, diff-at-a-glance | **Yes — fully**; this makes binding rule C-09 concrete | — | — |
| Dedicated numeric typeface or face feature | fintech apps | Numerals read as a system, distinct from prose | **Yes** — Arabic UI + ASCII numerals may require a two-font stack | Ticker/monospace-as-decoration | Numbers shout; "modern but not trendy" breaks |
| State color discipline (direction only) | YNAB, Copilot (knowledge-based) | Calm, unambiguous money | **Yes** — supports C-06 semantic distinctness | Category color-coding of everything | Color noise; states stop being distinct |
| Sparklines / movement charts inline | trading apps | Volatility reading | **No** | Micro answers "what changed and why," not market movement | Chart wallpaper (generic SaaS dashboard) |

**Open-source references — evidence only, never copy, with license warnings:**

- Moov's "awesome fintech" collection [moov.io, search 7] indexes OSS fintech projects (calculators, charts, currency handling). **Licenses vary per project; nothing may be lifted into Micro's product; the list is pattern evidence only.**
- Public GitHub "mobile banking application" demos [github.com, search 7] are demo/student quality — useful only as cautionary examples of the banking-clone look.
- Established OSS design systems document useful conventions for tabular numerals and state design: Google Material Design (Apache-2.0), IBM Carbon (Apache-2.0), Ant Design (MIT), Fluent UI (MIT). **License labels are from professional knowledge and must be verified before any use; more importantly, restyling Micro on any of them is an explicit anti-pattern (Material/shadcn restyle is banned by the shared brief). They are cited as evidence of documented convention only.**
- "Paychain" free Figma UI kit [figma.com, search 7] is marketing material, not open source — **rejected as a source entirely.**

---

## 3. Jordanian / micro-business owner context — implications for visual choices

What the digest establishes (Phase 2 live research):

- **Scale and formality:** MSMEs are ~98.5% of registered businesses and 60% of formal jobs [leadersinternational.org]; ~99% of ~150,000 registered enterprises, 38.7% micro [World Bank]; informal economy estimates range 15–27% of GDP [worldeconomics; efi-ife.org; haqqi.info].
- **Finance gap:** only 17% of Jordanian SMEs have a bank loan or line of credit [UNDP 2025]; the Arab-world SME finance gap is ~$123B [CGAP]. Owners are largely outside institutional finance.
- **Connectivity:** 92.5% internet penetration, ~10.7M users, overwhelmingly mobile [DataReportal, Digital 2025: Jordan].
- **WhatsApp reality:** 80%+ adult penetration regionally; the dominant business engagement channel [hyperleap; whatsable].
- **Cash culture:** COD was ~11% of Middle East e-commerce transaction value [Worldpay via LinkedIn], is halving as digital payments mature [Checkout.com], yet "remains the predominant choice" in Jordanian e-commerce [ResearchGate]. JoPACC's switch volume grew 77.2% in 2024 [JoPACC] — cash and digital coexist.
- **Record-keeping behavior:** small firms in developing countries score weakly on record-keeping practices; record-keeping is "not widely encouraged" among small-scale enterprises [McKenzie & Woodruff, World Bank/NBER; e-palli 2023].

**Implications for visual choices:**

1. **Familiarity must be behavioral, not visual.** The owner's reference app is WhatsApp: bottom sheets, name-indexed lists, share-to-close-the-loop. Borrow those interaction shapes; never borrow the look (no green, no bubbles, no chat framing). Distinction comes from composition — consistent with C-17.
2. **Cash is physical and countable.** COD + drawer culture means money arrives in hand. Micro's wallet metaphor («الدرج»), counting, and distribution flows match reality; the visual language should treat cash as a quantity you can count (rows, counts, deltas), not as an abstract graph.
3. **Trust is personal, not institutional.** With 17% banked SMEs and deep informality, trust is built between two people seeing the same numbers (OkCredit's strongest pattern). Micro's closure sentences, statements, and «تراجع موثق» corrections are the trust objects — no institutional chrome needed, and institutional chrome would be dishonest.
4. **Teach by structure, not by terminology.** Weak record-keeping practice means labels must be owner language («لي عند العملاء», not "accounts receivable") and numbers must never need interpretation — tabular, unit-attached, signed, unknown shown as «—» with a road.
5. **Low-drama uncertainty.** Unknown/pending states are the owner's normal condition, not an error condition. They must look routine and calm — visually distinct (C-06, C-11) but emotionally quiet.

---

## 4. Recommended pattern set for Micro

Each recommendation is concrete enough to hand to an art director, and traceable to a benchmark finding.

| # | Recommendation | Concrete target | Benchmark trace |
|---|---|---|---|
| R-01 | Information density caps | Home ≤8 top-level blocks before «ما تغير مؤخرًا»; Finance ≤5 body blocks before the first collapsed layer; every list row ≤3 lines (who/what, status, amount) | Monzo/Wave single-question screens [lollypop/orbix, search 4]; density critique §4.13; lessons table |
| R-02 | One dominant figure per screen | Each screen's question (cash now / owed to me / owed by me) earns exactly one large figure + signed delta; ≥3-step typographic size ladder below it | Monzo balance hero [search 4]; Khatabook per-party balance |
| R-03 | List rhythm, cards only for real units | Default: typographic rows separated by hairlines; boxed surfaces reserved for genuine single units (an order + its items; a receipt) | Lessons table (card wall); WhatsApp catalog-in-thread [search 6] |
| R-04 | Number typography | Tabular lining numerals, always 2 decimals incl. trailing zeros, ASCII digits, en-US grouping, LTR-isolated (`bdi`), unit after number, signed deltas isolated | Fintech typography practice [medium; skinsfactory, search 3]; C-09 |
| R-05 | Thumb-zone discipline | Top ~25% orientation only; primary CTA + numeric inputs in bottom ~33%; keypad-first numeric entry (`inputmode`) | Hoober: 49% one-handed use [uxmatters; scotthurff, search 10]; C-13 |
| R-06 | Four navigation depths, chrome by role | Tabs+FAB → hubs (chrome visible) → stack readers (chrome visible, explicit back-to-origin) → deep editors (chrome hidden, unsaved guard) | Micro routeClassifier precedent [§3.1]; neobank bottom-nav conventions [lollypop, search 4] |
| R-07 | Party rows with inline action | Name → balance → action («حصّل») in one row; no payment-request affordance | Khatabook/OkCredit ledger rows [searches 1–2]; C-15 |
| R-08 | Pull-based lifecycle states | Order lifecycle as discrete named states with action-specific labels; no push-alert chrome anywhere | NN/g status trackers [search 8]; E-00.14 |
| R-09 | Quiet closure on every money write | Receipt sentence with closure numbers («سُجّل بيع 20.00 د.أ — الكاش صار 165.00 د.أ»), calm mark, surface settles; no confetti | OkCredit auto statement-share as trust loop [search 2]; lessons (silent saves) |
| R-10 | Distinct honest states | Empty ≠ error ≠ offline ≠ unknown, each with its own visual treatment; empty states suggest exactly one next step; unknown = «—» + road, never 0.00 | Empty-state practice [toptal; setproduct; mobbin, search 5]; 12-state vocabulary (C-11, C-12) |
| R-11 | Statement as trust object | «كشف الأسبوع» composed as a period statement the owner could show a party: week totals, per-party lines, period result | OkCredit statements/reports [search 2]; Monzo statement view |
| R-12 | Local-first offline truth | Offline line only when actually offline; staleness = export date; never render connectivity as failure | Banking offline-language debate [ux.stackexchange, search 5]; Micro's local-first architecture |
| R-13 | Skeleton loading for list reads | Skeleton rows for list reads (estimates, events); never spinners over text | Banking app practice (knowledge-based); §4.14 Tools loading target |
| R-14 | Trust without banking chrome | No security badges, no card art, no cross-sell; trust = reconciling numbers + documented corrections | Banking apps as negative reference (§2.5) |
| R-15 | Calm emotional register | No streaks, badges, goal meters, or collection pressure; states look routine; motion settles rather than celebrates | Revolut/monobank gamification rejected [flatstudio, search 4]; target feel brief |

---

## 5. Explicit rejection register

| Rejected pattern | Source family | Why rejected for Micro (identity-tied) |
|---|---|---|
| POS item-tile grid and checkout flow | Square POS | Micro records after the fact; the owner is alone, not serving a line. «سجّل» is a recorder, not a till. |
| Banking clone chrome (security badges, card art, custody language, cross-sell carousels) | Retail banking apps | Micro holds no custody and moves no money; institutional visual authority would be a false promise. |
| Desktop ERP compression (~13 top-level blocks, dense tables, nested tabs) | QuickBooks desktop / Tally | One-handed 360×640 Arabic-first scanning needs hierarchy and air; already convicted in the lessons table. |
| Generic SaaS dashboard (KPI card grid, chart wallpaper, notification bell) | Admin templates | Charts answer analysts' questions, not owner questions; E-00.14 bans attention chrome. |
| Gamified money (streaks, badges, confetti, goal meters) | Revolut, monobank | Trivializes genuine cash-flow anxiety; contradicts "financially serious but emotionally comfortable." |
| Chat-as-record (bubbles as the ledger) | WhatsApp | Familiar shape, structurally dishonest for financial truth: totals unsearchable, states unexpressible. |
| Superapp sprawl (loans, UPI/QR collection, marketplace modules) | Khatabook/OkCredit monetization | Different business model; collection-pressure features erode calm trust. |
| Material/shadcn default restyle | OSS component kits | Instantly generic; differentiation must come from composition (C-17). |
| Dribbble-shot composition (floating cards, no flow, dev labels in frame) | Portfolio shots / MicroPrimitives characterization | The product must read as an owner's working day, not an exhibit. |
| Ticker/sparkline density | Trading apps | Micro answers "what changed and why," not market movement. |

---

## 6. Open questions for the orchestrator

1. **Statement sharing:** OkCredit's strongest trust loop is outbound statement sharing. Micro has no messaging channel — should «كشف الأسبوع» carry an export/share affordance (text/image), and is that in scope for the concept?
2. **Numeric typeface:** is a font shortlist fixed for the concept? Tabular-figures support in an Arabic-first stack (Arabic UI + ASCII numerals) is a hard constraint and may force a two-font system.
3. **Dark mode:** should representative screens be composed in both themes from the start (C-05 deliberate mappings), or light-first with dark verification later?
4. **Lifecycle visibility:** how much of the order state tracker belongs in the list row versus OrderDetail only? (NN/g pull-tracker logic suggests detail; owners scan pipelines.)
5. **Skeletons for local reads:** IndexedDB reads are typically fast — are list skeletons genuine, or reserved for first boot, import, and large party ledgers?
6. **Correction preview surface:** should «معاينة الأثر» be a modal dialog or a bottom sheet — i.e., how heavy should the correction ritual visually feel?

---

*End of report. Task ID 2-a. No code, no prototype, no repository push was performed.*
