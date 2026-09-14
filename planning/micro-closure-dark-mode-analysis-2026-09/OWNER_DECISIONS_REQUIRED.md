# OWNER DECISIONS REQUIRED — Micro Closure Analysis (2026-09-15)

**Source:** Five-agent read-only closure analysis of `Micro@micro-standard-ui-aux-integration-20260914` (`ece7be3630739d551b9ba7caf37d30a9a63c872f`).
**Rule:** None of these may be resolved by an execution agent inventing product or financial meaning. Each decision below states the evidence, the options, the consequence of each option, and what is blocked until it is decided. Nothing here has been implemented — this analysis was read-only.

**How to read urgency:**
- **BLOCKING (must decide before the next user-journey phase starts):** D1, D2, D3, D7
- **SHOULD-DECIDE-EARLY (unblocks remediation waves R3/R4):** D4, D5, D10
- **PARALLEL (can be decided any time; registered so they are not lost):** D6, D8, D9

---

## D1 — Dark-mode runtime reachability (HIGHEST URGENCY — HIGH severity)

**Findings:** A4-01 (HIGH), A5-03 (MEDIUM, same root).
**Evidence:** `apps/prototype-web/client/src/App.tsx:13` (`<ThemeProvider defaultTheme="system" switchable>`), `contexts/ThemeContext.tsx:20-23,47-59`, `components/layout/AppHeader.tsx:48-56`, `components/settings/SettingsAppearanceSection.tsx:34-36`, `index.css:107-151` (`.dark` = retired v0 palette).

**The situation:** The completion run's "Dark Mode not activated" is a *ratification* statement, not a runtime state. The theme is `system`-default and switchable, with visible toggles in AppHeader and Settings. On an OS-dark device, the app loads the `.dark` block today — which carries the retired v0 palette and leaves the entire W2 primitive layer light-locked (quiet-button text computes to 1.05–1.18:1 — invisible; commit-button boundary 1.18:1; Row/Field/EmptyState titles 1.18:1; see DARK_MODE_READINESS_REVIEW.md §4).

**Options:**
1. **Pin light** (recommended): `defaultTheme="light"`, `switchable={false}` (or hide the toggle) until the owner-gated dark wave. Consequence: OS-dark users see the vetted Light surface; the broken dark path becomes unreachable; a one-line change + test; fully reversible.
2. **Accept broken dark as a live surface**: keep reachability, add dark parity to every journey test matrix now. Consequence: significant immediate test burden on an unratified palette; contradicts ADR-007's own boundary.
3. **Do nothing**: dark remains reachable and broken; every week of new screens adds dark-debt. Consequence: compounding risk, silent brand damage on OS-dark devices.

**Blocked until decided:** the scope of Wave R4 (semantic contracts) is not blocked, but the release-safety posture of every subsequent wave is. **Recommendation: Option 1 (pin light) recorded in MIGRATION_STATUS.md U-03.**

## D2 — Row/Field convergence sequencing (BLOCKING for journey-phase planning)

**Finding:** A5-11 (MEDIUM).
**Evidence:** `components/primitives/index.ts:20-21` exports Row/Field; zero production consumers (only `primitives.test.tsx`); meanwhile `micro-field` has 430 uses across 67 files and ≥10 bespoke row families carry the product (supplier-list articles, setting-row ×12, home-fact, today-item, loan/asset cards, owner-list-row, list-item, recurrence-card, event-row, `micro-finance-event` ×13). Registered waves #2/#3.

**Decision needed:** run the registered convergence waves BEFORE the journey phase, or run the journey phase first and converge opportunistically inside it?
**Consequences:** Converging first stabilizes the component contracts a journey phase will rest on, but delays user-visible work and may converge patterns the journeys would reshape. Journey-first delivers user value sooner but risks a journey phase restructuring 430 field compositions twice. **Either is defensible; it must simply be recorded before list/form-heavy journey work begins.**

## D3 — Commit-class expansion scope (BLOCKING for one ink-per-act consistency)

**Finding:** A5-06 (MEDIUM).
**Evidence:** `pages/AssetDetail.tsx:374-403` — «تخلّص بمقابل» (disposal for value) and «اشطب الأصل» (write-off) wear `secondary`, despite being terminal, reason-required acts (compare: order cancellation = `destructive`, corrections = `commit`). Also uncovered: OrderDetail «تسجيله دينًا» (register as debt) = `secondary`. Registered decision #7.

**Decision needed:** which action class (and confirmation path) governs disposal/write-off/register-as-debt — destructive, commit, or a ratified secondary-with-confirmation?
**Consequences:** leaving it undecided means the journey phase inherits ambiguous high-consequence semantics; deciding it lets ADR-008 gain a one-ink-per-act addendum and the classes be applied consistently.

## D4 — Surface-tone grammar registration

**Finding:** A3-03 (MEDIUM).
**Evidence:** a parallel `data-tone` vocabulary (accent/warning/danger/update/offline) is set directly in pages (`Orders.tsx:152`, `Statement.tsx:501,561`, `DirectSaleEditor.tsx:599,608`, `Schedule.tsx:950`) plus a local state→tone ternary in `G5DecisionPanel.tsx:116-122`, outside the State Adapter — while `SOURCE_OF_TRUTH.md:14` says pages set no direct data-tone.

**Decision needed:** register the surface-tone grammar as a sanctioned second vocabulary (documented, with dark-layer selectors), or route surface state through the State Adapter over time.
**Consequences:** unregistered, it is exactly the pattern a future agent will copy wrongly in new journey screens; registered, it gets one authoritative home and a documented path.

## D5 — Light-theme contrast floors

**Finding:** A2-07 (MEDIUM).
**Evidence:** contrast is never computed anywhere in the repo; the documented 7.4:1 (`SOURCE_OF_TRUTH_MATRIX.md:16`) has no computation artifact.

**Decision needed:** enforce light-theme contrast floors now (a computed-ratio guard over the token table wired into `pnpm check`), or defer to the dark-mode parity matrix with a recorded date/trigger.
**Consequences:** a guard converts a documented claim into a mechanical invariant; deferring keeps the claim unverifiable until the dark wave.

## D6 — Conditional-feedback restructuring

**Finding:** A5-14 (LOW, with a named hazard).
**Evidence:** 10 message-classification ternaries sniff content prefixes; `pages/CashDistribution.tsx:214` classifies success by `startsWith("ان")` — any alef-nun-initial string (including failures) classifies as success. Registered decision #4.

**Decision needed:** approve the restructuring pattern (explicit channel — structured kind or explicit tone — instead of prefix sniffing), prioritizing the «ان» hazard.
**Consequences:** the Wave R1 FeedbackNote fix (A5-01/02) lands the primitive-level pattern; this decision extends it to the remaining per-surface ternaries.

## D7 — Link-ink ratification (BLOCKING companion to the pressed-state fix)

**Finding:** A5-04 (MEDIUM; the fix is CLOSE_BEFORE_NEXT_PHASE, the ratification is owner input).
**Evidence:** 22 FinanceActivity filters, Finance view tabs, Statement ranges, LockSettings options, and Corrections/Events toggles wear `micro-text-action` + `aria-pressed` with zero pressed styling — the only pressed rule in the tree is `.micro-suggest-chip` (`index.css:5853`). 104 link-ink uses across 37 files carry link+toggle+tab semantics. Registered decision #6.

**Decision needed:** ratify link-ink as a primitive-level role (including warning/withdrawal ink variants) and its pressed state, or direct a chip-migration instead.
**Consequences:** without a pressed state, active filters/tabs/options are invisible as selected — a direct journey-safety defect; the code fix can land provisionally, but its final shape (link-ink vs chip) is this decision.

## D8 — FinanceActivity chip splitting copy

**Finding:** A5-09 (LOW).
**Evidence:** `pages/FinanceActivity.tsx:270-275` — EmptyState without the no-data/no-results state slot that `Orders.tsx:335` and `Parties.tsx:138-147` already implement.

**Decision needed:** the copy distinction for the two void kinds (not-recorded vs filtered-out), then adopt the state slot.
**Consequences:** minor per-surface honesty improvement; already patterned elsewhere, so cost is low once copy is decided.

## D9 — Completion ✓ copy marker

**Finding:** A5-10 (LOW).
**Evidence:** literal ✓ appears in success copy on three surfaces — `pages/Settings.tsx:294` (registered), `presentation/cashCountMessages.ts:19` and `pages/CashDistribution.tsx:129-130` (unregistered).

**Decision needed:** one marker rule for completions across all three surfaces (widen the registered Settings decision).
**Consequences:** cosmetic consistency; should be sequenced AFTER the Wave R1 classification fix so the marker lands on correctly-classified messages.

## D10 — Standard mode-neutrality clarification (STANDARD_STEWARD-gated)

**Finding:** A4-07 (LOW).
**Evidence:** `micro-standard-v2` is deliberately silent on themes (`self-critique.md:9,27`; `color-system.md`; `accessibility.md:23`).

**Decision needed:** at the next Standard revision, add the minimum **product-agnostic** clarification: (1) token role names are theme-agnostic; (2) contrast bindings are per-theme re-derivations, not fixed hexes; (3) non-light themes require a `color-scheme` declaration; (4) semantic roles must not encode theme-specific values. No Micro-specific content, no dark palette values, no second palette source.
**Consequences:** without it, every future theme implementation improvises its own contract reading; with it, the semantic-roles wave (A4-02) and any future dark wave trace to Standard language.

---

## Relationship to the prior run's registered decisions

The completion run already registered these decisions in `docs/architecture/MIGRATION_STATUS.md`: Dark Mode gate (U-03), Row/Field convergence waves (#2/#3), conditional feedback restructuring (#4), link-ink ratification (#6), commit-class expansion (#7), Settings ✓ copy, FinanceActivity chip split. **This analysis does not resolve any of them.** What it adds: exact evidence, five-option classification, the newly-surfaced reachability hazard (D1), the convergence-vs-journey sequencing question made explicit (D2), and the three unregistered items now surfaced (surface-tone grammar D4, contrast floors D5, the two extra ✓ surfaces in D9).

## Decision summary table

| ID | Title | Urgency | Severity | Source finding | Blocks |
|---|---|---|---|---|---|
| D1 | Dark-mode runtime reachability (pin light vs accept) | BLOCKING — decide first | HIGH | A4-01 / A5-03 | Release-safety posture of all waves; scope of dark testing |
| D2 | Row/Field convergence vs journey-phase order | BLOCKING | MEDIUM | A5-11 | Journey-phase planning (list/form-heavy work) |
| D3 | Commit-class expansion (disposal/write-off/debt) | BLOCKING | MEDIUM | A5-06 | One-ink-per-act consistency in journey screens |
| D4 | Surface-tone grammar registration | SHOULD-DECIDE-EARLY | MEDIUM | A3-03 | Wave R3 doc scope; future-agent correctness |
| D5 | Light-theme contrast floors | SHOULD-DECIDE-EARLY | MEDIUM | A2-07 | Optional guard in Waves R2/R4 |
| D6 | Conditional-feedback restructuring pattern | PARALLEL | LOW | A5-14 | Extension of Wave R1 fix to remaining ternaries |
| D7 | Link-ink ratification + pressed state | BLOCKING (companion) | MEDIUM | A5-04 | Final shape of the pressed-state fix in Wave R3 |
| D8 | FinanceActivity chip-split copy | PARALLEL | LOW | A5-09 | One-surface honesty improvement |
| D9 | Completion ✓ marker rule | PARALLEL | LOW | A5-10 | Cosmetic consistency (after Wave R1) |
| D10 | Standard mode-neutrality clarification | SHOULD-DECIDE-EARLY (steward) | LOW | A4-07 | Standard traceability for the semantic-roles wave |
