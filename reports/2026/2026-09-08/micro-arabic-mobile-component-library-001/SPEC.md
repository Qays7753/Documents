# Micro Arabic-First Mobile Component Visual Library — Authoritative Run Specification

> This document is the full specification for this run. It is identical to the coordinator's brief except that repository credentials have been sanitized: the access token is handled only by the coordinator via a secure file outside all committed paths and is never echoed, printed, stored, or committed. No agent may ask for, print, or commit any credential.

---

## 1. Role and mission

The team is a small, senior design-systems studio. The job is to create a **single, cohesive, Arabic-first mobile component visual library** for a Jordanian small-business financial and operational application.

This is not a request to build the full product, production screens, backend, data model, API, authentication, or business workflow. It is a request to create the **reusable visual foundations and components from which future product screens can later be composed**.

The quality bar is equivalent to a serious specialist design-system engagement. The result must feel native to a real phone application, not like a web dashboard, a documentation website, a collection of generic cards, or an AI-generated concept gallery.

The team must produce **one selected direction**, not multiple visual concepts.

---

## 2. Run identity, isolation, and repository rules

```
RUN_ID  = 20260908T133450Z-16d11
RUN_ROOT = zed-ai-runs/20260908T133450Z-16d11/
```

Folder layout:

```
zed-ai-runs/20260908T133450Z-16d11/
├── 01-ux-architecture/
├── 02-visual-identity/
├── 03-design-system-engineering/
├── 04-user-and-accessibility-review/
├── 05-synthesis-and-redesign/
├── final/
└── run-report.md
```

Every agent works only inside its own folder. Never overwrite another run. Never touch unrelated repository content. Commit only the new run folder.

Upload target: `DOCUMENTS_REPOSITORY_URL: https://github.com/Qays7753/Documents.git` (public HTTPS URL; authentication is handled securely by the coordinator only — the raw token must never appear in any repository file, Markdown file, HTML file, shell history, log, screenshot, or report).

Credential rules (binding on all agents):
- Never ask for, print, echo, store, or commit a raw token.
- If repository access fails, keep the verified local deliverables, write a blocker report, and do not invent a successful upload.

At the end of the run the coordinator reports:

```
run_id:
agent_outputs:
final_outputs:
repository_path:
commit_id:
upload_status:
blockers:
```

---

## 3. Skill use and instruction hierarchy

The coordinator's brief named five skills: `professional-ux-system`, `muapi-ui-design`, `tailwind-design-system`, `dispatching-parallel-agents`, `prompt-engineer`. Where those are unavailable in this environment, the closest local guidance is used (mobile UX discipline, UI quality review, token architecture, accessibility baseline, anti-generic-design craft rules, multi-agent dispatch with isolated folders).

If generic skill guidance conflicts with the Micro specification below, **the Micro specification wins**. In particular, do not automatically import Inter, an 8-point-only grid, Glassmorphism, desktop dashboards, generic card galleries, dark mode, or any default theme that is not explicitly defined below.

Do not expose hidden chain-of-thought. Reason internally, then record concise decisions, evidence, trade-offs, and verification results in the required artifacts.

---

## 4. Product context

The product is a **phone-only Arabic-first operational and financial application for small businesses in Jordan**. Its users are busy owners and operators who want the useful result immediately and do not want to read long explanations.

Product domain includes: sales and orders; cash-in and collections; expenses and cash-out; customers and receivables; suppliers and payables; purchasing; materials and inventory; delivery companies and settlement follow-up; schedules and operational follow-up.

Use these domains to make the components feel specific and believable. The library must include realistic examples such as cash received, expense paid, supplier purchase, receivable collection, delivery settlement, material threshold, customer balance, and an operational exception. Do not create a generic banking dashboard or a generic SaaS admin panel.

The product audience is fast, sometimes impatient, and not necessarily professionally trained in finance or design. The first glance must communicate the important number, label, state, and next action with minimal text.

---

## 5. Visual reference rule

Use this neutral visual benchmark description only:

> The desired comfort level is a warm, composed, practical small-business product with comfortable surfaces, meaningful density, strong hierarchy, calm spacing, and restrained elevation. It should feel lived-in and trustworthy, not empty, cold, decorative, or overly technical. It may have visual warmth and personality, but it must remain direct and operational.

Do not copy any other product's code, component names, layout, screen map, token values, brand identity, or visual signature. Do not produce a clone of a reference application. The goal is an independent Micro visual language derived from the specification below.
---

## 6. Non-negotiable Micro visual foundations

### 6.1 Platform and locale

- Phone-only, portrait-first.
- Validate at 320px, 360px, 390px, and 430px widths.
- Arabic-first, RTL as the primary direction.
- English digits `0–9` in all financial values and dates.
- Dates use `DD/MM/YYYY`.
- Jordan-only currency context: use `د.أ`, `دأ`, or omit the currency when the surrounding context makes it unambiguous. Never use `JOD` in user-facing examples and never spell out the currency name in ordinary UI.
- Use `bidi dir="ltr"` or an equivalent bidi-isolation strategy for values, dates, percentages, identifiers, and mixed currency strings.
- Test Arabic labels, long Arabic text, increased text size, and one-handed use.

### 6.2 Light mode

Light Mode only. Do not create dark tokens, a theme switch, `.dark`, or `prefers-color-scheme` behavior. The system status-bar area follows the canvas and uses dark system icons. Do not create fake system UI inside the HTML lab.

### 6.3 Final color system

Use these exact tokens and roles. Do not invent substitute browns or legacy brand colors.

#### Brand

```
brand-atmosphere: #CC785C
brand-tint:       #F7EAE4
brand-ink:        #964E33
on-brand:         #FFFFFF
press-overlay:    #1F1E1D at 8%
```

`#CC785C` is the calm visible identity/graphic brand surface. Use approved dark ink over it when text is required. `#964E33` is the readable brand ink and may also be used as a **limited filled text-bearing primary CTA with white text** when needed for normal-text contrast. It is not a general-purpose surface, number, border, or status color. `press-overlay` is the press treatment; do not use `#B4613F`.

#### Product surfaces

Exactly three product surface roles:

```
canvas:  #FAF9F5
surface: #FFFFFF
sunken:  #F0EEE6
```

Do not create additional product planes such as paper, grouped, quiet, app, atmosphere, or custom beige surfaces. Semantic tints are allowed only for their semantic roles and should not become a hidden fourth surface system.

#### Ink and structure

```
ink-strong:  #1F1E1D
ink:         #33322E
ink-muted:   #6E6A60
ink-subtle:  #767265
ink-disabled:#B7B2A6
line-soft:   #EAE6DC
line-strong: #DED9CB
scrim:       #1F1E1D at 45%
```

#### Semantic families

```
positive: #2E7D57     positive-tint: #E7EFE7
 danger:  #B42318     danger-tint:   #F7E7E2
 warning: #8A6520     warning-tint:  #F4EDD8
 info:    #3E5C76     info-tint:     #E8EDF1
```

Use semantic color to communicate operational meaning, not decoration:

- positive: cash received, confirmed, completed, favorable movement;
- danger: cash out, negative financial direction, real failure, destructive action;
- warning: overdue, threshold, attention required, estimate exceeded;
- info: in progress, decision-critical pending context, neutral operational information.

Color is never the only status signal. Pair it with a sign, label, icon, pattern, or structural cue.

#### Color economy with useful energy

The product should feel warm, confident, and alive without becoming noisy:

- maximum one filled brand-family surface/action per viewport;
- maximum two semantic families in one composition;
- maximum two colored numerical values in one composition;
- maximum one tinted QuickActionRail tile;
- maximum three visible dividers;
- maximum two nested surface levels;
- use the full semantic palette across the library, but do not place all semantic families into every composition;
- never color an entire card just to make the screen look lively;
- use semantic accents in realistic Micro examples, not isolated color swatches only.

### 6.4 Typography

- Primary: IBM Plex Sans Arabic.
- Fallback: Noto Sans Arabic, then system sans-serif.
- Weights: 400, 500, 600.
- Use `font-variant-numeric: tabular-nums lining-nums` where supported.
- English digits in financial values.
- Main numeric value: approximately 32px / 600 / 1.15.
- Regular labels: approximately 15px / 400 / 1.55.
- Qualifiers and compact metadata: approximately 13px / 400 / 1.4.
- Arabic text minimum: 14px in user-facing UI.
- Do not use a display typeface, mono font, or decorative font as the primary product voice. A mono face may be used only for small technical/audit values in documentation, never as the dominant user-facing visual language.

### 6.5 Spacing, geometry, and touch

Spacing scale: `2, 4, 8, 12, 16, 24, 32, 40px`.

Screen edge: 16px at all target widths. Use content-driven heights. Do not use aspect-ratio or fixed heights for variable Arabic content.

Radius scale: `6, 12, 16, 24, full`. Do not make every control a pill. Bottom Navigation is edge-to-edge with radius 0.

Touch targets: 44px minimum; 48px for primary actions; 8px minimum gap between adjacent targets unless the platform pattern explicitly requires otherwise.

### 6.6 Icons and RTL

Use Lucide-style icons or a coherent equivalent, with 2px stroke and 24px default / 20px row sizing. Create an explicit RTL mirror registry. Mirror directional icons such as back, forward, chevrons, and directional arrows. Do not globally flip every SVG. Semantic/object icons do not mirror. Do not use a paper-plane send icon.

### 6.7 Shell and navigation

- The top zone is integrated into the page content, not a detached conventional top bar.
- Use one Avatar entry for the unified profile/settings area.
- Bottom Navigation is the only persistent chrome.
- Use a small number of top-level destinations with labels that fit Arabic at 320px. If five labels would clip, use four destinations plus a clearly labelled More destination or another justified native pattern; do not create a blank disabled seat.
- Quick actions belong in a horizontal `QuickActionRail`, not in a floating desktop-style dashboard grid.

### 6.8 QuickActionRail

The QuickActionRail is a reusable component, not a decorative strip:

```
Tile: 88 × 92px
Icon: 24px
Label: 13px
Icon-to-label gap: 8px
Rail padding: 16px
```

Use 4–5 stable actions, primary action first, right-to-left horizontal scrolling, proximity snap, and a subtle canvas edge fade. At most one tile is tinted with `brand-tint`.

Target a visible next-item cue of 28px at wider widths while keeping the locked tile/gap/padding geometry. Document the measured responsive exception at 320px: 16px peek at 320px, with the wider-width measurements verified rather than overclaimed. Do not change tile width, gap, or start padding to fake a universal 28px value.

Use believable actions such as `إضافة بيع`, `تحصيل دين`, `إضافة مصروف`, `إضافة شراء`, and `تسجيل دفعة`, but treat them as lab examples rather than a final product navigation map.
### 6.9 Component architecture

Build and visibly demonstrate these reusable families:

1. `PrimaryValueBlock`: exactly one per test composition, on the canvas rather than trapped inside a card. It shows the real number first, with a short label and a decision-relevant state only when needed.
2. `MetricGroup`: one surface containing 2–5 secondary values. Use aligned `MetricRow` rows and compact qualifiers. Do not create one card per metric.
3. `MetricRow`: label and aligned numeric value on one row; support positive, negative, attention, and unavailable examples.
4. `CompactTile`: for a genuine comparison pair or QuickActionRail item, not a generic mini-card grid.
5. `OperationalRow`: repeating operational content on a canvas or within one meaningful grouped surface. Use Micro examples such as supplier purchase, delivery settlement, collection, stock threshold, and expense.
6. `Button` family: primary, secondary, quiet/text, destructive, icon-only, loading, disabled, focused, pressed, and quiet completion.
7. `Input` family: text, amount, search, date, selection, segmented control, tab, checkbox, and switch only where the setting is immediate.
8. `State` family: empty, loading, error, offline/local-save, decision-critical pending, conflict, failed, completed, cancelled, and reversed where relevant. Keep user-facing wording concise and action-oriented.
9. `Sheet` and `Dialog`: correct phone behavior, scrim, focus return, dismiss rules, and reduced-motion behavior.
10. `BottomNavigation` and integrated top zone with Avatar.
11. `Chart` primitives: sparkline, planned-vs-actual, target meter, and direct-labelled trend marker; use text alternatives.

The lab must show each family as a visual matrix of meaningful variants. The word "component library" must not mean a single composition with repeated inline HTML only.

### 6.10 Composition budget

For each test composition:

- exactly one `PrimaryValueBlock`;
- one `QuickActionRail`;
- one `MetricGroup` by default, two maximum only with a documented reason;
- one comparison pair maximum;
- no repeated key value in the same composition;
- maximum three visible surfaces;
- one vertical scroll owner; the QuickActionRail may scroll horizontally;
- no full product screen map and no production integration.

### 6.11 Motion and interaction

Use restrained native-feeling motion:

```
press: 80ms
fast: 120ms
normal: 200ms
sheet in/out: 240/180ms
dialog in/out: 160/120ms
scrim: 200ms
```

Use standard and exit cubic-bezier curves. Do not use bounce, spring, count-up animation for financial values, page-wide slide transitions, or toast-only proof. The final numeric value appears immediately. Include reduced-motion behavior that preserves state meaning without spatial animation.

Every important interactive component must show its real interaction contract: press, focus, disabled, loading, completion proof, error recovery, swipe/drag where applicable, and safe dismissal.

### 6.12 Lists, empty states, and data

- Empty states are concise line-based states with a useful action when one exists. No illustration by default and no empty-card theatre.
- Use a 20-row batch, prefetch near the last 5 rows, and 3 skeleton rows.
- Stop automatic retries after the first failure and expose a clear retry action.
- Do not show a technical synchronization phrase in an ordinary primary card unless it changes the user's understanding or next action. When a state is decision-critical, use concise user-facing wording rather than infrastructure language.
- Unknown, unavailable, true zero, and empty input are distinct. Never display unknown as `0`.
- Negative sign is the primary financial-direction signal; color is secondary.

### 6.13 Charts

The time axis stays LTR inside the chart even in an RTL interface; text labels remain Arabic RTL. At 320px use direct labels and avoid a detached legend. Planned, actual, and forecast must be distinguishable by line or texture style and direct labels, not color alone. Provide a text alternative for every chart.
---

## 7. Five-agent execution plan

Agent 01 — UX architecture and Micro domain contracts (scope: `01-ux-architecture/`): define future-state component contracts, component-to-task mapping, information hierarchy, native phone patterns, state truth for financial values, before-scroll priorities, concise Arabic labels and user-facing states.

Agent 02 — Visual identity, color, typography, and visual energy (scope: `02-visual-identity/`): design ONE independent visual direction that feels warm, energetic, confident, and operational rather than merely quiet, obeying the exact Micro tokens and the composition color budget.

Agent 03 — Design-system and Tailwind v4 architecture (scope: `03-design-system-engineering/`): clean token hierarchy and extraction-ready component architecture, Tailwind v4 CSS-first `@theme` if Tailwind is used, Light Mode-only, component variants and states without a generic dashboard or card-gallery system.

Agent 04 — User viewpoint, interaction, accessibility, and verification (scope: `04-user-and-accessibility-review/`): act as the skeptical owner/operator and mobile accessibility specialist. Review whether a fast Arabic-speaking small-business owner can understand and act without reading long explanations across 320/360/390/430px portrait, RTL and a geometry-only LTR check, 100/130/200% text scaling, reduced motion, long Arabic labels, one-hand reachability, financial sign/value/bidi correctness, touch targets and focus states, all states, color meaning without relying on color alone, visible next action and recovery path.

Agent 05 — Lead synthesizer, critic, and controlled redesign (scope: `05-synthesis-and-redesign/`): runs only after Agents 01–04 complete. Reads their reports and artifacts. Does not create a fifth competing direction. Synthesizes one final direction, resolves conflicts transparently, and redesigns only the parts that fail the acceptance criteria. Compares the proposal against the exact Micro specification, the neutral comfort benchmark, native mobile behavior, and the user's need for energy and confidence; willing to reject a visually safe but lifeless result; does not add arbitrary colors or decoration to compensate.

## 8. Required final deliverables

```
final/
├── micro-component-visual-library.html
├── micro-component-visual-library.css
├── micro-component-visual-library.js
├── tokens.css
├── component-contracts.md
├── visual-direction.md
├── color-role-map.md
├── motion-and-interaction.md
├── accessibility-rtl-report.md
├── coverage-matrix.md
├── decision-log.md
├── self-critique.md
├── verification-report.md
└── README.md
```

### HTML lab requirements

The final HTML lab is the primary visual deliverable. It must:

- open locally in a browser with no missing placeholders such as `{{...}}`;
- have no required remote runtime or unavailable project-specific support file;
- use real Arabic labels and realistic Micro operational examples;
- show one selected direction only;
- provide a clear switch or index between `Foundation`, `Component Library`, `Test Composition`, and `Verification` views without becoming a product screen map;
- show visible component matrices, not only prose or token tables;
- include interactive examples for press, selection, loading, completion, sheet, dismissal, and reduced motion;
- show 320/360/390/430px previews and RTL as the default;
- keep audit evidence separate from the primary visual showcase;
- not contain long explanations, raw Hex values, rejected colors, or implementation notes inside the phone composition itself;
- use semantic colors in meaningful Micro examples, with at most two semantic families per composition;
- use the final currency display rule and never show `JOD`.

### Documentation requirements

Every component contract must include: `name`, `purpose`, `when to use`, `when not to use`, `anatomy`, `content hierarchy`, `sizes`, `spacing`, `radius`, `surface role`, `brand role`, `semantic color role`, `variants`, `states`, `interaction and motion`, `RTL behavior`, `accessibility`, `Arabic copy examples`, `Micro operational examples`, `responsive behavior`, `known limitations`.

The `coverage-matrix.md` must map every required family and state to an actual HTML location and a verification status. "Documented" is not the same as "implemented."

The `decision-log.md` must record important choices once, with the chosen decision, rejected alternatives, reason, and evidence.

The `verification-report.md` must list each tested viewport, direction, scale, motion mode, and observed result. Include screenshots or local paths when the environment supports them.

## 9. Acceptance rubric

Agent 05 must score the final result 1–5 on each dimension and explain every score below 4:

| Dimension | Passing expectation |
| --- | --- |
| Micro specificity | Examples and component behavior clearly serve small-business operations |
| Native mobile quality | Feels like a real phone application, not a web page in a phone |
| Visual warmth | Comfortable surfaces and hierarchy without paper/ledger styling |
| Visual energy | Approved semantic colors create confidence and life without noise |
| Directness | The number, label, and next action are understood quickly |
| Component reusability | Families and states are visibly inspectable and extractable |
| Color correctness | Exact final tokens and roles are used; no invented/legacy colors |
| Arabic RTL quality | Arabic text, digits, bidi, mirroring, and long labels hold up |
| Interaction quality | Press, focus, loading, completion, error, sheet, and reduced motion are clear |
| Accessibility | Contrast, targets, non-color status, and text scaling are verified |
| Responsive integrity | 320/360/390/430px show no clipping or broken hierarchy |
| Handoff quality | Files are organized, documented, and ready for a later integration phase |

Decision rules:

- Any hard conflict with the exact color, currency, Light Mode, phone-only, or RTL rules blocks acceptance.
- Any missing final HTML lab or missing coverage matrix blocks acceptance.
- Any visual score below 4 for Micro specificity, native mobile quality, visual energy, or component reusability requires a revision before upload.
- Do not average away a hard failure.

## 10. Final response format from the coordinator

Return a concise final message and save the full report to `run-report.md`, including the structured block:

```
<zed_run_report>
{
  "run_id": "...",
  "status": "complete|blocked|needs_revision",
  "agents_completed": ["01", "02", "03", "04", "05"],
  "final_score": { "micro_specificity": 1, "native_mobile": 1, "visual_warmth": 1, "visual_energy": 1, "directness": 1, "component_reusability": 1, "color_correctness": 1, "rtl_accessibility": 1, "interaction_quality": 1, "responsive_integrity": 1, "handoff_quality": 1 },
  "files_created": [],
  "repository_path": "...",
  "commit_id": "...",
  "upload_status": "uploaded|local_only|blocked",
  "hard_failures": [],
  "remaining_assumptions": [],
  "next_action": "..."
}
</zed_run_report>
```

After the structured block, provide a short Markdown summary of what was actually built, what was verified, and what remains. Do not claim a file is implemented merely because it is described in a document.

## 11. Final instruction reminder

Create one coherent, lively, confident, Arabic-first Micro component visual language. Use warm comfort as a foundation, but do not let warmth become a monochrome brown system. Use semantic color as operational meaning, not decoration. Build the visual library first, then prove the relationships with one small test composition. Keep all work isolated under the current `RUN_ID`, verify it, and upload only the final run folder to Documents using secure credentials.
