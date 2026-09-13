# Micro Standard v2 — Full ZAI Flash Execution Prompt

## 0. Nature of This Task

You are acting as the **lead visual-system and controlled-execution agent** for Micro Standard v2. This is not a short theoretical review, not a generic code audit, and not a rebuild of Micro. You must read the current Standard package in full, implement only the approved delta inside the Standard, verify it through controlled waves, create an independent interactive HTML Prototype that represents all visual changes for approximate visual review, and upload every output to the Documents repository under the GitHub policy below.

Do not invent replacement colors. Do not restore an old palette. Do not copy code, screens, workflows, terminology, or brand treatment from Accounting. Do not treat the Brand Book or the external ZAI review as higher authority than the owner-approved decisions in this prompt and the handoff folder.

## 1. Sources and Current Source of Truth

Repository:

`https://github.com/Qays7753/Documents`

Current Standard package:

`https://github.com/Qays7753/Documents/tree/main/micro-standard-v2`

Verified `main` commit at handoff preparation:

`dfa8bf7d7f7a2c01f256d4c77d359c8a5770d60b`

Current handoff folder:

`https://github.com/Qays7753/Documents/tree/micro-standard-v2-zai-execution-handoff-20260913/planning/micro-standard-v2-execution-handoff-2026-09`

Read these files before touching any package file:

1. `README.md`
2. `OWNER_APPROVED_DECISIONS.md`
3. `EXECUTION_PROCEDURE.md`
4. `GITHUB_UPLOAD_POLICY.md`
5. `PREVIOUS_WAVE_BOUNDARIES.md`
6. `REFERENCE_INDEX.md`

Then read every current file under `micro-standard-v2/`. The current package contains 29 core files plus `MANIFEST.json` and `RELEASE.md`, for 31 files in total.

Use `MICRO_STANDARD_COMPREHENSIVE_UIUX_REVIEW.md` as diagnostic evidence only after independently inspecting the actual current files. Use the Brand Book and logo archive to understand identity and logo construction only; they do not automatically authorize every brand color as a product UI token. Use Prototype v0 only as composition evidence; do not copy it and do not move it into Micro.

Do not use an unpublished historical branch or commit such as `micro-standard-v2-foundation-development` or `f64e8616...` as the working source. Verify the actual current `main` at execution time and start from that state.

## 2. Required Outcomes

This task must produce four categories of deliverables:

1. **A controlled development of the current Standard package**, modifying only files that require an actual change after all 29 core files have been read.
2. **A complete execution record** showing, for every one of the 29 core files, whether it was unchanged, changed, deferred, or blocked, with the reason, wave, and related tests.
3. **An independent interactive HTML Prototype** after Standard changes have been completed and verified, showing all visual changes for approximate visual review.
4. **A complete cloud upload** of all files, reports, Prototype assets, screenshots, hashes, and validation evidence to Documents, with branch, commit, run-folder, and proof that `main` was not modified.

The target is the 29-file Standard package, but this does **not** mean editing all 29 files blindly. Read all 29 files, then change only the justified delta. Do not normalize or rewrite files merely for stylistic consistency.

## 3. Owner-Approved Identity and Color Decisions — Do Not Reopen

Preserve the current direction: Light-only, warm light surfaces, Arabic-first RTL, phone-first, quick first-glance comprehension, English numerals with numeric bidi isolation, and restrained warm layers.

| Color | Approved role | Must not be used for |
|---|---|---|
| `#D97757` | Micro identity, create, add, and FAB | financial values, chart fills, statuses, profit/loss, card or screen fills |
| `#C96442` | selected/current/pressed edge, underline, and selection boundary | generic filled buttons, success/error, profit/loss |
| `#141413` | primary financial value, clear commitment, high-consequence confirmation, and justified danger | default background for every important element, decoration, or an all-ink chart |
| Existing Warm Tint `#F5F4ED` | ordinary save and ordinary confirmation surface | it must not be treated as proof of financial success by itself |
| Existing semantic colors | success/error/info/pending/review/status | they must not be replaced by identity colors or relied on without words/shapes |

### Action contracts

**Create/Add:** Use the existing Terracotta `#D97757` for the FAB or a clear create action. It must not display a financial value and must not become the general color for all commitments.

**Ordinary Save/Confirm:** Do not use a filled black surface. Use the existing Warm Tint `#F5F4ED` with dark `#141413` text and icon. On press, show a clear `#C96442` edge. Pressing must not turn the action into a success state. After actual completion, show a success word and semantic marker; do not rely on color alone.

**High-Consequence Commit/Destructive Confirmation:** Use `#141413` as a filled surface when a strong pause is appropriate, with white text, a word describing the consequence, an appropriate icon, a short consequence explanation, and an independent confirmation path.

### Rejected decisions for this execution

Do not introduce `#964E33` or `#5F3120` as tokens or primary buttons. Do not use `#B79C86` or `#8C7A66` as product UI colors; they are logo-reference neutrals only. Do not add a new palette. Do not ratify a new Teal role in this execution. Do not open Dark Mode. Do not recolor Terracotta into data, success, or failure states.

## 4. Standard versus Micro Boundary

Standard owns visual representation, tokens, contracts, slots, visible states, neutral composition guidance, and state presentation. Micro owns data, meaning, formulas, product policy, permissions, routes, sync, posting/reversal, and the actual product decision of when a state appears.

Do not introduce formulas, data sources, accounting or tax policy, posting/reversal, permissions, authentication, sync, conflict resolution, delivery behavior, or product-writing semantics into Standard or the Prototype.

## 5. Five Sub-Agents

Use five complementary sub-agents. They may analyze sources in parallel, but no sub-agent may directly create conflicting edits. The main agent owns the unified plan and final implementation.

### Agent 1 — Source and Boundary Auditor

Verify the current `main`, inventory the 31 files, compare the current package with historical reports, identify what is actually present, and prevent repeated work or use of an unpublished branch. Produce a source map and file-boundary map before edits.

### Agent 2 — Contract and Token Truthing

Inspect `design-tokens.css`, `design-tokens.json`, `color-system.md`, `button-system.md`, `component-contracts.md`, state files, and accessibility files. Define the minimum changes required to distinguish create, ordinary save, high-consequence commitment, danger, success, error, pending, unknown, and review without adding new color values.

### Agent 3 — Gallery and Composition Implementer

Inspect and update only neutral Gallery examples. Demonstrate that Warm-Ink does not fill everything, ordinary save uses Warm Tint, Terracotta is for create, selected/current has a clear signal, and charts are not entirely black or Terracotta. Do not turn the Gallery into a Micro product or an Accounting copy.

### Agent 4 — Interactive Prototype Builder

Start only after the Standard changes have been completed and verified. Build an independent HTML Prototype that consumes the final Standard tokens and contracts and demonstrates all required visual changes and interactions without product logic, real data, or production routes.

### Agent 5 — QA, Accessibility, Responsive, and Upload Auditor

Check contrast, focus, pressed, disabled, loading, reduced motion, RTL, zoom, and overflow. Verify that states do not depend on color alone. Verify hashes, file inventory, GitHub upload, and completion proof. Do not permit a completion claim until the upload proof is complete.

## 6. Mandatory Execution Sequence

### Wave 0 — Baseline and Rollback

Create a new work branch from the verified current `main`. Do not change any content inside `micro-standard-v2/` in this wave. Create an inventory of the 29 core files plus metadata, a complete baseline copy, a complete rollback copy, SHA-256 records, a file-boundary register, and a Wave 0 report.

Prove that `main` was not modified. Stop if you cannot prove the starting point or rollback boundary.

### Wave A — Contracts and Token Truthing

After Wave 0 passes, update only the contracts and tokens required by the approved delta. The contracts must make these action and state differences executable rather than vague prose:

- create/add/FAB;
- ordinary save/confirm;
- pressed save;
- high-consequence commit/destructive confirmation;
- success/error/pending/unknown/review;
- amount/value/context/period slots;
- color independence and non-color signals.

Do not add a raw color value. If a semantic alias is needed, bind it to an existing approved value; do not invent a new hex value. Do not change Light Mode, RTL, numeric isolation, or base geometry unless a concrete test proves a real defect and the owner decision is explicitly required.

Deliver a diff, report, hashes, test results, and rollback boundary. Stop if the gate fails.

### Wave B — Gallery and Component Composition

After Wave A passes, update only the required examples in `component-gallery.html`, `component-gallery.css`, `component-gallery.js`, and the directly related files. The Gallery must show at least:

- create/FAB using `#D97757`;
- ordinary save/confirm using Warm Tint `#F5F4ED` with dark text/icon;
- pressed save with a `#C96442` edge;
- high-consequence/destructive confirmation using `#141413`;
- primary values clearly visible without creating many black surfaces;
- selected/current segments and chips without automatic black fills;
- success/error/pending/unknown/review with a semantic color, word, and shape;
- row/metric/value/period/amount slots;
- a question-led chart with zero/no-data/loading and a text alternative;
- sheets/dialogs, bottom navigation, and overflow when they are part of the current contract.

Do not add product routes, writes, formulas, or business actions. Use only the local interaction needed to demonstrate the visual states.

### Wave C — Verification and Documentation

After Waves A and B pass, update documentation, manifest, and verification files according to the actual changed files. Record what changed and what did not, link contracts to examples, and clearly distinguish local browser evidence from any real device test.

### Wave P — Interactive HTML Prototype

After the Standard is complete and verified, create an independent interactive HTML Prototype under the run folder, not inside `micro-standard-v2/`.

The Prototype must cover every visual change implemented, not a single abbreviated screen. At minimum, include these scenes:

1. Create/add and FAB.
2. Ordinary save/confirm using Warm Tint.
3. Pressed, loading, and quiet completion.
4. High-consequence confirmation and destructive deletion.
5. A financial value with context, period, and currency-unit slot.
6. An OperationalRow with amount slot, status, and overflow.
7. Selected/current and segments/chips.
8. Success/error/pending/unknown/review with word, marker, and shape.
9. A question-led chart with zero/no-data/loading and text alternative.
10. Sheet/dialog, bottom navigation, and overflow where applicable.

Local interaction is required: press actions, cycle states, open/close sheets and dialogs, loading, quiet completion, and illustrative period/state changes. No real data source, formulas, writes, posting, production routes, or remote assets.

The Prototype must be Arabic RTL, work at 320/360/390/430px, be inspectable at 100/130/200%, honor reduced motion, and have no horizontal overflow. Include:

- a downloadable HTML file;
- local CSS/JS as needed;
- `PROTOTYPE_README.md`;
- `PROTOTYPE_COVERAGE.md` linking each scene to the Standard file and contract it represents;
- `PROTOTYPE_VALIDATION.md` recording tests and limitations;
- key screenshots when available.

Any issue found in the Prototype must first be recorded as a Prototype composition issue. Do not automatically modify Standard because of a Prototype issue.

## 7. Mandatory Tests

After each wave and after the Prototype, run the applicable checks:

- `git diff --check`;
- JSON parsing and manifest consistency;
- file inventory and changed-file proof;
- 320/360/390/430px;
- RTL, Arabic text, English numerals, and numeric bidi isolation;
- 100/130/200%;
- focus/pressed/disabled/loading/quiet completion;
- reduced motion;
- contrast for borders, text, and surfaces;
- no horizontal overflow;
- FAB does not cover the amount column;
- no unjustified concentration of black surfaces within one viewport;
- states do not rely on color alone;
- charts are not entirely black or entirely Terracotta;
- do not claim physical Samsung or screen-reader testing unless it was actually performed.

Each wave must end with an explicit status: `PASS`, `PASS WITH LIMITATIONS`, or `BLOCKED`.

## 8. Hard Stop Rules

Stop immediately and record the reason if:

- you need to change `#D97757`, `#C96442`, `#141413`, or the approved base surfaces;
- you need to add a new color;
- a conflict appears between an owner decision and the Brand Book or ZAI report;
- you need Dark Mode;
- you need Micro logic, policy, or formulas;
- you need bulk file moves or structural refactoring;
- you cannot prove rollback;
- you cannot prove that `main` was unchanged;
- the Prototype cannot represent the Standard changes;
- GitHub upload fails.

If structural refactoring or bulk file moves appear necessary, do not execute them. First perform the required read-only Structure/Architecture/Code Organization Scan, then stop for owner review.

## 9. GitHub and Cloud Upload

Read `GITHUB_UPLOAD_POLICY.md` and follow it exactly.

The user will manually fill these values:

```text
GITHUB_REPOSITORY: https://github.com/Qays7753/Documents
GITHUB_ACCESS_TOKEN: <USER_WILL_PASTE_A_SHORT_LIVED_RESTRICTED_TOKEN_HERE>
TARGET_BASE_BRANCH: main
TARGET_WORK_BRANCH: micro-standard-v2-execution-20260913
RUN_ID: <CREATE_A_UNIQUE_RUN_ID>
```

Never print the token, write it to a file, place it in screenshots or reports, or return it in chat. Do not push to `main`, force-push, delete branches, change repository settings, merge, or open a pull request.

Upload all outputs under:

`planning/micro-standard-v2-execution-handoff-2026-09/runs/<RUN_ID>/`

Upload the Prototype separately under:

`planning/micro-standard-v2-execution-handoff-2026-09/runs/<RUN_ID>/prototype-v0.1/`

Upload every wave report, changed-file list, diff summary, hashes, tests, limitations, and rollback boundary. At the end upload:

- the final Standard snapshot or a complete applicable patch;
- the Prototype HTML, CSS/JS, README, Coverage, and Validation files;
- `FINAL_RUN_MANIFEST.json`;
- `FINAL_RUN_README.md`;
- key scene screenshots when available.

After upload, return in the chat and in `FINAL_RUN_README.md`: repository URL, branch, commit SHA, run folder, inventory, main status, and token-exposure status. If upload fails, do not claim completion; state the failure and provide the files as a fallback.

## 10. Final Report Format

Return the complete report in the chat and attach it as a downloadable Markdown file. It must contain:

1. Summary of what was implemented.
2. Starting point, baseline, and rollback.
3. A row for every core file showing changed/unchanged/deferred/blocked and the reason.
4. Color-role table and test evidence.
5. Details and status of every wave.
6. Prototype scenes and coverage mapping.
7. Test results by viewport, zoom, and state.
8. What was not tested.
9. Remaining issues separated into Standard, Prototype, and Micro composition.
10. Links, commit, run folder, and hashes.
11. Explicit confirmation that Micro, Accounting, and `main` were not changed.
12. Explicit confirmation that the Access Token was not stored or exposed.

Do not claim that Standard is ready to transfer into Micro until Standard, Prototype, validation, and owner review are complete.

## 11. Required First Response Before Any Edit

Before modifying any file, return a short preflight plan in the chat containing:

- the commit and branch you actually read;
- the 31-file inventory;
- files expected to change and files expected to remain unchanged;
- wave plan;
- Prototype plan;
- upload plan;
- any conflict or ambiguity discovered.

After the preflight is complete, start Wave 0 only. Do not begin implementation before baseline and rollback exist. Do not invent a decision not present in this prompt or the handoff.
