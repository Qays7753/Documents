# Gate 0 — Source Compliance Note

- **Agent role:** Senior Visual Product Designer (visual exploration + visual execution only)
- **Date:** 18/09/2026
- **Primary source commit:** `6688845` on `main` (Micro-Bold-Modular-Design-Handoff-V1)
- **Working branch:** `design/autonomous-v1` (created from latest `main`; no work committed to `main`)

## 1. Files read (complete list)

1. `00-START-HERE.md`
2. `01-APPROVED-DESIGN-DECISIONS.md`
3. `02-MICRO-DESIGN-DIRECTION-BRIEF-V1.md`
4. `03-SCREEN-ARCHITECTURE-AND-HIERARCHY.md`
5. `04-CONTENT-AND-DATA-FIXTURES.md`
6. `05-BOLD-MODULAR-VISUAL-RULES.md`
7. `06-C1-C2-C3-DIRECTION-SPECIFICATIONS.md`
8. `07-REQUIRED-SCREENS-AND-DELIVERABLES.md`
9. `08-DIRECTION-EVALUATION-RUBRIC.md`
10. `09-SPECIALIZED-VISUAL-DESIGN-AGENT-PROMPT.md`
11. `10-EVIDENCE-AND-CONSTRAINTS-MAP.md`
12. `11-AUTONOMOUS-END-TO-END-EXECUTION-PROTOCOL.md`
13. `12-DOCUMENTS-REPOSITORY-DELIVERY.md`
14. `AGENTS.md`
15. `README.md`, `README-AR.md`, `Micro-Handoff-Visual-Overview.html` (supporting context)

## 2. Decisions marked `LOCKED` that this work must preserve

**Product & user**
- UX-D01 — Primary user: small-business owner, limited-to-moderate financial/digital experience, phone-first.
- UX-D02 — Arabic-first and mobile-first.
- UX-D03 — Financial truth over visual optimism: incomplete/unknown data is never shown as zero, profit, or loss.
- PR-D01 — Micro is a financial and operational system, not an AI character or chatbot.

**Information architecture**
- IA-D01 — Bottom navigation is exactly five destinations: مشروعي الآن، العمل، المالية، أدواتي، السوق.
- IA-D02 — منتجاتي وخدماتي is a contextual destination reachable from multiple places, never a sixth tab.
- IA-D03 — Compact top zone: Micro logo on the right; النقل والتوصيل and Ask Micro on the left; the logo opens the account/project/settings menu; account settings stay visible even when setup is incomplete; no oversized app bar.
- IA-D04 — Dark mode remains inside settings, not in the main header (concept dark-mode screens are presented as design proof, entered via settings).

**Visual strategy**
- UI-D01 — Calculated full visual change is allowed; existing cream/terracotta are candidates, not sacred.
- UI-D02 — Bold and colorful identity; active and balanced in use.
- UI-D03 — Parent direction: **Bold Modular Micro**.
- UI-D04 — Direction C leads composition/expression; A contributes warmth; B contributes financial discipline and trust.
- UI-D05 — Calmness is a task state, not the entire brand personality.
- UI-D06 — Strong color blocks only when they communicate section, status, priority, action, change, or progress.
- UI-D07 — Energy gradient: home high, finance medium, tools medium-low, records/settings low.
- UI-D08 — No decorative notebook/receipt/stamp metaphor as the main identity.

**Interaction**
- IX-D01 — Home answers “كيف وضع مشروعي؟” within five seconds.
- IX-D02 — Repeated actions are visible and labeled; no icon-only hidden FAB.
- IX-D03 — Quick Action Bar is the default pattern; no duplicate persistent FAB.
- IX-D04 — Success feedback shows what changed and where the value went.
- IX-D05 — Every critical state uses text plus a second non-color cue.

## 3. Decisions open for exploration (with required output)

| Topic | Status | My obligation |
|---|---|---|
| Brand color (terracotta family) | `OWNER_APPROVAL_REQUIRED` | Compare keep / intensify / deepen / replace through visual evidence; final hex is a proposal. |
| Base background (warm-neutral vs cleaner neutral) | `OWNER_APPROVAL_REQUIRED` | Compare in C1 vs C2/C3; avoid full-screen beige dominance. |
| Trust color (deep blue / blue-teal) | `OWNER_APPROVAL_REQUIRED` | Test as secondary without confusing it with financial positive. |
| Icon expression (Lucide baseline vs stronger single-family) | `OPEN_FOR_EXPLORATION` | One icon family per direction; no mixed libraries; no mirroring of non-directional icons. |
| Module accents (controlled per-section accents) | `OPEN_FOR_EXPLORATION` | Explored primarily in C3, bounded against rainbow fragmentation. |
| Motion signature — “Success Impact” | `USER_TEST_REQUIRED` | Design the concept; label as hypothesis. |
| Micro Signal (status → reason → action) | `USER_TEST_REQUIRED` | Design the grammar; label as hypothesis. |

Deliberately postponed (not finalized here): final hex canon, logo adjustment, production component tokens, icon library migration, animation curves beyond concept guidance, chart library, production sequence.

## 4. Screens and states to be delivered

**Phase A (per direction: C1, C2, C3):** one foundation board — thesis, five adjectives, light/dark roles, measured contrast table, typography scale with real Arabic UI copy, surface hierarchy, color-block rules, icon treatment, button/control hierarchy, Business Status Hero, Micro Signal, Quick Action Bar, states (positive, negative, incomplete, delayed, success, error), Success Impact storyboard, three strengths / three risks / hypotheses.

**Phase B (per direction, exact fixtures from file 04):**
1. Home — complete positive result (Fixture A).
2. Home — incomplete result (Fixture B).
3. Successful sale with visible impact on the updated value (Fixture G, chained from Fixture F).

**Phase C (per direction):**
1. Home — positive · 2. Home — incomplete · 3. Home — negative (Fixture C) · 4. Quick Action Bar + expanded “more” state (Fixture E) · 5. Record-a-sale form (Fixture F) · 6. Sale success (Fixture G) · 7. Finance overview · 8. Work/orders overview (state model: اتفاق، تنفيذ، جاهز، تم التسليم، متأخر) · 9. Delayed-order detail (Fixture D) · 10. Empty home/day state (Fixture H) · 11. Validation error (Fixture I) · 12. System error/retry (Fixture J) · 13. Dark-mode home · 14. Account/project/settings menu opened from the logo.

**Responsive proofs (home-positive + sale-success, all directions):** 320px, 390px (primary), 430px, and a 200% text-resize stress case. Selected direction additionally: focus concept, reduced-motion behavior, mixed Arabic/Latin/numeric proof, full state coverage, clickable prototype/motion storyboard.

**Fixed fixtures:** project حلويات ليان، period اليوم 18 أيلول، currency `185.00 د.أ` format, Latin digits, tabular alignment, RTL with isolated numeric runs, dates `DD/MM/YYYY`.

## 5. Output mode selected

Editable Figma tooling is unavailable in this environment. Per the fallback in file `07`, the deliverable is an **isolated HTML/CSS/JS prototype inside this handoff repository under `prototype/`** with separate folders for C1, C2, C3 (no shared stylesheet across directions), plus PNG exports (1× and 2×), a PDF presentation, contrast/token files in Markdown + JSON, and an interactive motion prototype honoring `prefers-reduced-motion`. The Micro production repository is never touched.

## 6. Genuine blockers, tensions, and clarifications

1. **No blocking contradiction was found.** The file set is internally consistent; the authority order in `00-START-HERE.md` resolves precedence.
2. **Truncated instruction (minor, non-blocking):** the final “Use …” bullet of the execution prompt (Stage 6) was cut off mid-sentence in transmission. File `12` fully defines the Documents delivery protocol, so execution proceeds on that basis.
3. **Authentication practice:** file `12` says tokens must never be requested in chat and never embedded in a Git remote URL. An owner-supplied write token was nevertheless provided inside the chat prompt. I will use it only via a local credential helper (remote URLs stay clean), never print/echo/commit it, purge it after use, and **recommend the owner revoke and rotate it immediately after delivery**. If the token lacks scope for the primary repository push, that step will be documented as an access blocker and every unaffected task still completed (per file `12` fallback rule).
4. **Hypotheses discipline:** per file `10`, no Jordanian-user preference claim, Micro Signal effectiveness claim, or “more colorful ⇒ better retention” claim will be presented as fact; these remain `RESEARCH_HYPOTHESIS` until tested.
5. **Typography:** IBM Plex Sans Arabic + IBM Plex Mono/tabular numerals remain the baseline (per `05`); no alternative family is proposed because no evidence in this exercise would justify the switch. Fonts are bundled locally in the prototype for reproducibility (OFL license).
6. **Contrast:** all proposed text/icon/control pairs are measured programmatically (WCAG 2.2); failures are recorded as failures, never rounded into passes. Proposed hex values are proposals pending owner approval.

## 7. Compliance verdict

**Gate 0: PASS.** No unresolved contradiction prevents fair production of C1, C2, and C3. Work proceeds autonomously through Gates 1–7 with internal quality gates, evidence logging, and a single final pull request on `design/autonomous-v1`.
