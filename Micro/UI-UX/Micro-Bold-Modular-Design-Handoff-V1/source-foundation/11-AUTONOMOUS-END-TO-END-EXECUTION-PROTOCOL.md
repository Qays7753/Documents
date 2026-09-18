# Autonomous End-to-End Execution Protocol

## Mission

Complete the Micro visual-direction exploration, comparison, provisional selection, selected-direction refinement, prototype, evidence, and final handoff without waiting for owner feedback between stages.

Autonomy does not convert hypotheses into facts. Final owner approval and real-user validation remain pending.

## Repository boundaries

- This repository is the authorized design workspace.
- Never edit the Micro production repository.
- Never deploy to production.
- Never store credentials, access tokens, personal data, or private customer information.

## Branch and review policy

- Create `design/autonomous-v1` from the latest `main` before producing artifacts.
- Commit all generated work to that branch, not directly to `main`.
- Push coherent milestone commits and open one final pull request to `main`.
- Do not merge the pull request automatically; final merge is an owner action.
- At completion, mirror the full handoff to `https://github.com/Qays7753/Documents` under the isolated path and branch defined in `12-DOCUMENTS-REPOSITORY-DELIVERY.md`, without removing the copies in this repository.

## Required working structure

```text
deliverables/
  01-foundations/
    c1-warm-bold/
    c2-confident-bold/
    c3-dynamic-modular/
  02-critical-screens/
    c1-warm-bold/
    c2-confident-bold/
    c3-dynamic-modular/
  03-full-directions/
    c1-warm-bold/
    c2-confident-bold/
    c3-dynamic-modular/
  04-selected-direction/
  05-design-system-candidate/
  06-accessibility-rtl-evidence/
  07-motion-and-prototype/
reports/
  compliance-note.md
  gate-log.md
  comparison-and-recommendation.md
  open-decisions.md
  final-handoff.md
prototype/
exports/
```

## Execution sequence

### Gate 0 — Source compliance

Read all authoritative files. Write `reports/compliance-note.md` with locked decisions, open exploration areas, required screens, repository boundaries, and actual blockers.

Pass condition: no unresolved contradiction prevents fair production.

### Gate 1 — Three foundation boards

Produce C1, C2, and C3 at equivalent quality using identical content obligations. Measure every operational color pairing and document the psychological role of attention, reassurance, warning, progress, and incompleteness.

Pass condition:

- Each direction is visibly distinct but belongs to Micro.
- Arabic typography and RTL are demonstrated with real copy.
- Financial states never depend on color alone.
- Normal-text and large-text contrast requirements are met.
- No direction is a generic equal-weight card grid.

If any condition fails, revise and rerun Gate 1. Do not pause.

### Gate 2 — Critical screens

Produce the three critical screens for every direction using the fixed fixtures.

Pass condition:

- Business status can be understood within five seconds in an expert inspection.
- The next useful action is visible.
- Incomplete data is not presented as zero, profit, or loss.
- Successful action visibly explains what changed.
- C1, C2, and C3 receive equal polish.

If any condition fails, revise and rerun Gate 2. Do not pause.

### Gate 3 — Full direction coverage

Produce all screens and responsive proofs in `07-REQUIRED-SCREENS-AND-DELIVERABLES.md` for all three directions.

Pass condition: coverage, states, dimensions, rationale, and evidence are complete and comparable.

### Gate 4 — Evidence-based comparison

Score all directions with `08-DIRECTION-EVALUATION-RUBRIC.md`. Apply rejection conditions before weighted ranking. Explain every score with artifact evidence.

Pass condition: recommendation follows the evidence rather than visual preference.

### Gate 5 — Provisional selection

Select one direction provisionally. Record why it wins, what it borrows from the other directions, which risks remain, and which assumptions require owner or user validation.

Do not label this as final owner approval.

### Gate 6 — Selected-direction refinement

Refine the provisional winner into:

- Coherent candidate tokens and component rules.
- Light and dark behavior.
- Responsive proofs at 320, 390, and 430px.
- 200% text stress proof.
- Keyboard/focus concept where applicable.
- Reduced-motion behavior.
- Mixed Arabic/Latin/numeric proof.
- Error, empty, delayed, incomplete, success, positive, and negative states.
- Clickable prototype or motion storyboard.

### Gate 7 — Final handoff

Complete the final report, source manifest, exports, known limitations, unresolved owner decisions, and implementation-transfer notes. Verify links and filenames. Commit coherent milestones, push `design/autonomous-v1`, open a final pull request to `main`, mirror the completed handoff to the Documents repository according to file `12`, and leave both repositories in a reproducible state.

## Commit policy

Use clear milestone commits, for example:

- `docs: confirm design source compliance`
- `design: add C1 C2 C3 foundation boards`
- `design: add critical screen comparison`
- `design: complete full direction sets`
- `docs: add rubric evaluation and recommendation`
- `design: refine provisional selected direction`
- `docs: finalize autonomous design handoff`

Do not rewrite shared history or force-push.

## Stop conditions

Stop only if:

- Repository access is unavailable.
- An essential referenced source is missing and cannot be reconstructed without inventing product truth.
- A requirement is technically impossible in the available environment.
- Continuing would require production access or credentials not granted.

For any stop condition, finish all unaffected work and document the smallest precise action needed to unblock completion.
