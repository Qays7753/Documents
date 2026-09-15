# Independent Visual Foundation Source Pack

## Purpose

This workspace is a neutral, product-independent source pack for reviewing and normalizing a mobile visual and interaction foundation. It is not an application repository and it is not a product implementation.

## Source authority

Treat the files under `source-reference/`, `reference-components/`, `reference-layout/`, `reference-assets/`, and `rendered-reference/` as visual evidence from one existing mobile system. Preserve the intended visual language unless a documented accessibility, consistency, implementation, or measurement issue requires correction.

The source files are read-only references. Do not modify or overwrite them. Do not write into the source-pack folders. All generated work must go under `output/` and every run must use a unique `RUN_ID` folder.

## Scope

Review and normalize only what a user can see or directly feel: colors, ramps, surfaces, text roles, typography, numbers, spacing, dimensions, radii, borders, shadows, elevation, buttons, fields, cards, rows, sheets, dialogs, navigation, icons, states, feedback, motion, responsive behavior, RTL behavior, and accessibility.

Do not infer or invent a product domain. Do not import any external product knowledge. Do not preserve product-specific labels, calculations, database assumptions, page maps, business workflows, or state meanings except when a state is necessary to explain a generic visual component.

## Required behavior

Start in Plan mode. First inventory the source pack, identify contradictions, and propose a file-by-file normalization plan. Do not generate the final package during the inventory phase.

Use read-only subagents for independent review. Only the primary synthesizer may write the final output package. Subagents must return evidence, not taste-based assertions.

For every changed token or component rule, record the source evidence, the reason for change, the compatibility impact, and a verification method. Preserve the source value when it is valid and coherent; do not redesign merely to show originality.

The final HTML gallery must work offline, render without placeholders, and show each component family independently in all important states. It must be checked at 320, 360, 390, and 430 CSS pixels, with RTL and LTR geometry checks, large text, and reduced motion.

Completion requires evidence: all required files exist, tokens parse, the gallery opens offline, screenshots or render checks are captured, no source file was modified, and the final report lists assumptions, corrections, unresolved questions, and verification results.

## Safety and hygiene

Do not access unrelated repositories, external product code, GitHub history, user accounts, or private services unless explicitly authorized for this source-pack task. Do not add dependencies unless the plan explains why and the dependency is necessary for the neutral visual package.

Do not use product-specific names in the final neutral documentation. Use generic labels such as `primary action`, `positive state`, `negative state`, `selected`, `warning`, `information`, `confirmed`, and `disabled`.

Do not claim pixel-perfect parity without measured evidence. Do not claim a visual defect is fixed until the rendered output has been checked.

## Output location

Write all generated deliverables under:

`output/<RUN_ID>/`

Never overwrite a previous run. Keep a `run-manifest.json` and `verification-report.md` in the final run folder.
