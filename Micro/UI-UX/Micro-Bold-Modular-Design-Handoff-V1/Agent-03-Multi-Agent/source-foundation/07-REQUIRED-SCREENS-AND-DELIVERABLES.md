# Required Screens and Deliverables

## Phase A — Foundation board

Before full screens, deliver one foundation board per direction containing:

- Direction thesis and adjectives.
- Palette roles and contrast results.
- Typography scale with Arabic examples.
- Surface hierarchy.
- Color-block logic.
- Icon treatment.
- Button and control hierarchy.
- Status examples: positive, negative, incomplete, delayed, success, error.
- Business Status Hero.
- Micro Signal.
- Quick Action Bar.
- Success Impact storyboard.
- Light/dark relationship.

Do not continue to full production until foundation boards pass the internal gate in `11-AUTONOMOUS-END-TO-END-EXECUTION-PROTOCOL.md`. Record the gate result and continue without waiting for owner feedback unless a genuine blocker exists.

## Phase B — Critical concept screens

For C1, C2, and C3, produce:

1. Home — complete positive result.
2. Home — incomplete result.
3. Successful sale — impact and updated figure.

Primary viewport: 390×844. Include full initial viewport and full-scroll presentation when content extends below the fold.

## Phase C — Full direction set

After critical concepts pass the internal quality gate, produce:

1. Home — complete positive result.
2. Home — incomplete result.
3. Home — complete negative result.
4. Quick Action Bar and expanded “more” state.
5. Record a sale form.
6. Sale success state.
7. Finance overview.
8. Work/orders overview.
9. Delayed-order detail/state.
10. Empty home/day state.
11. Validation error.
12. System error/retry.
13. Dark-mode home.
14. Account/project/settings menu opened from logo.

## Responsive proof

For the selected critical home and sale screens, show:

- 320px width.
- 390px width.
- 430px width.
- One 200% text-resize or equivalent stress-test example.

## Deliverable formats

Preferred:

- Editable design source in Figma or equivalent.
- PDF presentation of all boards and screens.
- PNG exports at 1× and 2×.
- Contrast and token proposal in Markdown/JSON.
- Short motion storyboard or interactive prototype.

If editable design tooling is unavailable:

- Build an isolated HTML/CSS/JS prototype outside the Micro repository.
- The prototype may live in this handoff repository under `prototype/`; it must not modify the Micro production repository.
- Provide separate routes or folders for C1, C2, and C3.
- Do not share styles across directions in a way that erases their differences.
- Provide screenshots and a self-contained local preview.

## Autonomous completion requirement

Complete Phase A, Phase B, Phase C, responsive proof, evidence, self-audit, provisional direction selection, selected-direction refinement, and final handoff in one uninterrupted execution. Internal gates are mandatory checkpoints, not owner-wait states. If a direction fails a gate, revise it and rerun the gate before continuing.

## Naming convention

- `C1-Warm-Bold-*`
- `C2-Confident-Bold-*`
- `C3-Dynamic-Modular-*`

## Required rationale per screen

For every screen, document:

- Primary user question.
- Primary focal point.
- Primary action.
- Color-block purpose.
- Accessibility considerations.
- What was intentionally kept quiet.
- What remains a hypothesis.

## Rejection conditions

A direction is rejected before completion if:

- It cannot show business status in five seconds.
- It hides frequent actions.
- It treats incomplete result as zero, profit, or loss.
- It uses color without text or shape for critical meaning.
- It fails key contrast requirements.
- It becomes a card grid with equal visual weight.
- It copies a reference product’s visual identity.
- It changes navigation or product scope.
- It looks like three disconnected products across modules.
