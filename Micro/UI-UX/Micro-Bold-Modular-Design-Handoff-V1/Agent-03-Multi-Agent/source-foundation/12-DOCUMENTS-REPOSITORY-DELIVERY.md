# Documents Repository Delivery Protocol

## Destination

- Repository: `https://github.com/Qays7753/Documents`
- Working branch: `reports/micro-bold-modular-v1`
- Pull-request target: `main`
- Isolated destination root: `Micro/UI-UX/Micro-Bold-Modular-Design-Handoff-V1/`

Do not write outside this destination root. Do not overwrite, rename, move, or delete unrelated content in the Documents repository.

## Authentication safety

- Use only authentication supplied securely by the execution environment or an authorized GitHub connection.
- Never request that a token be pasted into chat.
- Never print, echo, log, commit, screenshot, or store a token.
- Never embed credentials in a Git remote URL.
- If authorization is unavailable, finish and push all work to the primary design repository, document the exact access blocker, and stop only the Documents mirror step.

## What must be mirrored

Copy the completed versions of:

```text
Micro/UI-UX/Micro-Bold-Modular-Design-Handoff-V1/
  README.md
  DELIVERY-MANIFEST.md
  source-foundation/
  deliverables/
  reports/
  prototype/
  exports/
```

### `source-foundation/`

Include the authoritative Markdown instructions from the primary design repository and the exact primary-repository commit SHA used for execution.

### `deliverables/`

Include C1, C2, C3, the comparison, the provisional selected direction, and the candidate design system.

### `reports/`

Include the compliance note, gate log, accessibility/RTL evidence, rubric evaluation, recommendation, open decisions, limitations, and final handoff report.

### `prototype/`

Include a self-contained runnable prototype or the complete motion-storyboard package, plus run/view instructions.

### `exports/`

Include review-ready PDF and PNG exports and any non-secret machine-readable token or contrast files. Do not commit generated dependency folders or caches.

## Delivery manifest

Create `DELIVERY-MANIFEST.md` containing:

- Delivery date and status.
- Primary design repository URL.
- Primary source branch, commit SHA, and pull-request URL.
- Documents repository branch, commit SHA, and pull-request URL.
- Complete file inventory.
- Checksums for final packaged exports when practical.
- Validation commands and their results.
- Known limitations.
- Items pending owner approval.
- Items pending real-user validation.

## Large-file rule

- Do not commit a file at or above GitHub's hard file-size limit.
- Keep review exports reasonably compressed without damaging legibility.
- For an editable source that cannot be stored safely in Git, provide a stable authorized source link plus export and version details in the manifest; never fake an editable source.

## Completion sequence

1. Finish and validate the primary repository work on `design/autonomous-v1`.
2. Push it and open the primary pull request to `main` without merging.
3. Create or update `reports/micro-bold-modular-v1` from the latest Documents `main`.
4. Copy the final handoff only into the isolated destination root.
5. Validate inventory, links, prototype instructions, and report completeness.
6. Commit and push the Documents branch.
7. Open a Documents pull request to `main` without merging.
8. Add both pull-request URLs and final commit SHAs to the delivery manifest and final status response.

## Definition of delivered

Delivery is complete only when both pull requests exist, both repositories contain the expected files on their respective branches, the manifest points to exact commits, and no secret or unrelated repository content was changed.
