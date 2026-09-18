# Rubric Evaluation & Direction Comparison — Micro Bold Modular V1

- **Method:** file `08-DIRECTION-EVALUATION-RUBRIC.md`. Rejection gates applied **before** weighted ranking. Scores are expert estimates backed by artifact evidence; they are **not** user validation.
- **Fair comparison mechanism:** all three directions render the **same DOM** from one generator with the exact fixtures of file 04; differences exist only in each direction's stylesheet. Every direction received the same QA passes and revisions.

---

## 1. Rejection-gate screening (all directions)

| Rejection condition | C1 | C2 | C3 | Evidence |
|---|---|---|---|---|
| Cannot show status in five seconds | PASS | PASS | PASS | Hero + state chip + result visible in initial 390×844 viewport; expert inspection (gate 2) |
| Hides frequent actions | PASS | PASS | PASS | QAB measured above nav obstruction in all directions (760–761px vs 764–765px) |
| Incomplete as zero/profit/loss | PASS | PASS | PASS | No result number rendered for incomplete; sales labeled; completion progress + action |
| Color-only critical meaning | PASS | PASS | PASS | Grayscale proof (`exports/grayscale/`): states distinguished by icon + text + symbol + progress |
| Key contrast failures | PASS | PASS | PASS | 213/213 measured pairs pass (`reports/contrast-evidence.md`) |
| Equal-weight card grid | PASS | PASS | PASS | Dominant hero + grouped rows; no uniform KPI grid |
| Copies a reference product | PASS | PASS | PASS | No single-product imitation; references used as patterns only |
| Changes navigation/scope | PASS | PASS | PASS | Five tabs locked; منتجاتي وخدماتي contextual only |
| Looks like three products | PASS | PASS | PASS | Shared shell, single icon family, one accent discipline per direction |

**No direction is rejected.** All three proceed to weighted scoring.

## 2. Weighted rubric scores

| Criterion | Wt | C1 | C2 | C3 | Key evidence |
|---|---:|---:|---:|---:|---|
| Five-second financial understanding | 18% | 4 | **5** | **5** | C2 report-table hero reads fastest to expert eye; C3 tinted field gives instant state; C1 warm figures box slightly softer |
| Action discoverability & speed | 14% | 4 | 4 | **5** | All QABs labeled + measured visible; C3 solid tiles most button-like |
| Sense of control | 12% | 4 | **5** | 4 | C2 "control room" framing (status → reason → action chain strongest); C3 progress language adds control but adds parse load |
| Trust in figures | 12% | 4 | **5** | 4 | C2 numeric discipline (hairline tables, mono-first, period+completeness chips); C3 tinted surroundings slightly riskier around numbers |
| Visual vitality | 10% | 4 | 4 | **5** | C3 clearly most awake; C1 warm-active; C2 restrained at rest |
| Comfort & sustained use | 8% | **5** | 4 | 4 | C1 warm canvas + generous spacing best for long finance sessions; all finance screens are deliberately calmer |
| Low-experience usability | 8% | **5** | 4 | 3 | C1 friendliest (direction A borrowed); C3 carries documented parse-load risk for the locked primary user |
| Distinct Micro identity | 7% | 4 | 4 | **5** | C3 most recognizable; C2's band is strong but nearer to finance-generic; C1 near craft-market risk |
| Arabic RTL quality | 4% | 5 | 5 | 5 | Same engine: isolated Latin numerals, tabular mono, `د.أ` placement, DD/MM/YYYY, non-mirrored non-directional icons |
| Accessibility | 4% | 5 | 5 | 5 | Equal by construction: 213 measured pairs, 44–48px targets, text+icon states, focus-visible, 200% no-hscroll, reduced-motion honored |
| Future scalability | 3% | 4 | 4 | **5** | C3 zone-accent system maps directly to future Market/delivery/cloud modules |
| **Weighted total** | 100% | **4.24** | **4.50** | **4.52** | |

## 3. Reading the result honestly

C3's 0.02 lead over C2 is **inside the noise of expert estimation** — it is a statistical tie, not a win. Decomposing where each direction earns its points:

- On the owner's explicitly ordered priorities — task success, financial comprehension, perceived control, trust, accessibility, **then** distinctive energy — the top four criteria (56% of weight) score: **C2 3.10 / C3 2.56 / C1 2.24**.
- C3's margin comes entirely from vitality, identity, and scalability (20% of weight, ranked last in the design objective).
- C3 holds the single weakest user-facing score in the matrix: low-experience usability **3** — against a `LOCKED` primary user of limited-to-moderate financial and digital experience (UX-D01). Its documented primary risk (fragmentation, cognitive overload) is not theoretical; it is visible in the scoring.

**Per the instruction "do not automatically declare the most expressive direction the winner," the evidence supports C2, not C3.**

## 4. Expert review outputs

### C1 — Warm Bold (4.24) — KEEP
- **Top strengths:** approachability for the target user; long-session comfort; distinct warm identity without logo dependence.
- **Top risks:** craft-market adjacency; warmth can soften financial authority; blue may dissolve if unmanaged.
- **Fixable:** strengthen hero numeric hierarchy; deepen trust-blue role in finance.
- **Structural:** none.
- **User-test questions:** does terracotta read as "my business" rather than "food app"?; warmth vs. seriousness after a 10-minute finance session.

### C2 — Confident Bold (4.50) — KEEP, RECOMMENDED
- **Top strengths:** fastest correct financial reading; strongest figure trust; control-room composure with warm action energy.
- **Top risks:** bank/SaaS adjacency if terracotta recedes; perceived vitality lower at rest; row density on 320px needs care.
- **Fixable:** inject warmth moments (signal ground, success); raise progress-language presence (borrow C3).
- **Structural:** none.
- **User-test questions:** does the dark band read "serious system" or "bank"?; is trust-blue distinguishable from financial positive in task passes?

### C3 — Dynamic Modular (4.52) — KEEP, reserve for extension
- **Top strengths:** instant state recognition; strongest identity; ready extension grammar for future modules.
- **Top risks:** parse load for the locked primary user; fragmentation; color near data if zone accents leak into bodies.
- **Fixable:** restrict zone accents to headers permanently; keep bodies neutral.
- **Structural:** expressiveness ceiling is a product-scope decision (Market future), not a styling fix.
- **User-test questions:** first-action identification time; zone accents as organization vs. decoration; incomplete-vs-loss precision under high expressiveness.

## 5. Provisional selection (Gate 5)

> **Recommended direction: C2 — Confident Bold** — expert recommendation, pending owner approval and real-user validation.

**Why it wins:** it maximizes the owner's declared priority order (comprehension, control, trust first; energy after), for the locked primary user, with the lowest rejection risk and the strongest financial-reading evidence.

**What it borrows (without merging before review):**
- From **C1**: the warm ground treatment for Micro Signal and success moments — keeping the human warmth the brief demands (A contributes warmth). Implemented in the refined candidate as a warmer signal plate and success-card ground.
- From **C3**: the prominence of the progress language — the 8/10 completion bar and order step rail gain stronger presence in the refined candidate.

**What stays reserved:** C3's zone-accent grammar is documented as the leading candidate for the future السوق module identity — a decision for that scope, not this one. C1 remains fully preserved with its evidence for any warm-first pivot.

**Remaining risks to validate with users:** band perception (system vs. bank); terracotta energy sufficiency; progress-language comprehension; 320px row density; dark-mode glare tolerance.

**Rejection-gate re-check on the recommendation:** financial truth ✓ · primary action visible ✓ · RTL integrity ✓ · contrast ✓ · incomplete comprehension ✓ · non-color cues ✓ · no nav occlusion ✓.
