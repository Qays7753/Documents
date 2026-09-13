# Handoff Reference Index

| Path | Classification | Use by ZAI |
|---|---|---|
| `README.md` | Source boundary | Read first. Establishes repository, baseline, authority order, and exclusions. |
| `OWNER_APPROVED_DECISIONS.md` | Approved decision | The only current product/UI decision source for this handoff. |
| `EXECUTION_PROCEDURE.md` | Execution control | Defines waves, stop conditions, rollback, tests, and no-silent-change rules. |
| `GITHUB_UPLOAD_POLICY.md` | Upload control | Defines the restricted-token placeholder, branch/run-folder policy, required uploads, and completion proof. |
| `PREVIOUS_WAVE_BOUNDARIES.md` | History boundary | Prevents use of unpublished branch/commit and repeated work. |
| `micro-standard-v2/` | Executable foundation | Actual 31-file package to inspect and modify on a new branch. |
| `reference/zai-review/MICRO_STANDARD_COMPREHENSIVE_UIUX_REVIEW.md` | External review evidence | Use for findings and gaps after independently checking current files. It does not override owner decisions. |
| `reference/zai-review/MICRO_STANDARD_COMPREHENSIVE_UIUX_REVIEW.zip` | Supporting evidence archive | Use only when a screenshot/session/manifest must be checked. |
| `reference/zai-review/MANIFEST.txt` | Evidence manifest | Confirms the external review delivery. |
| `reference/brand-assets/MicroBrandBook.dc.html` | Brand reference | Read for identity construction and approved logo variants. Do not turn it into an automatic UI palette. |
| `reference/brand-assets/#MicroFinancialLogoSystem.zip` | Brand asset archive | Use for logo assets only. Do not recolor or use logo forms as financial states. |
| `reference/brand-assets/BRAND_REFERENCE_CLASSIFICATION.md` | Brand/UI boundary | Read with the Brand Book to prevent unsafe translation into product UI. |
| `reference/prototype-v0/` | Already published evidence | Use only to understand composition issues; do not copy or transfer it into Micro. |

## Required reading order

Read `README.md`, `OWNER_APPROVED_DECISIONS.md`, `EXECUTION_PROCEDURE.md`, and `PREVIOUS_WAVE_BOUNDARIES.md` before touching any package file. Then inspect the actual current `micro-standard-v2/` files. Read external review and brand references only as supporting context.

## Upload requirement

The final execution prompt must require ZAI to read `GITHUB_UPLOAD_POLICY.md` and upload all wave outputs, the final Standard result, and the interactive Prototype to the specified Documents branch/run folder. No token may be stored or exposed.

## Missing by design

No GitHub access token is stored in this handoff. Authentication, if needed, must be supplied by the user through the external workflow. No Micro or Accounting source code is copied into this package. No old decision document is included as a competing source.
