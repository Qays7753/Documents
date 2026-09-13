# GitHub Upload Policy for ZAI

## Repository

- Repository URL: `https://github.com/Qays7753/Documents`
- Handoff branch already published: `micro-standard-v2-zai-execution-handoff-20260913`
- Handoff path: `planning/micro-standard-v2-execution-handoff-2026-09/`
- Current main must remain unchanged.

## Token placeholder

The user will provide a restricted token manually to ZAI. The token must never be committed, written into a file, printed in a report, included in a screenshot, or returned in chat.

```text
GITHUB_REPOSITORY: https://github.com/Qays7753/Documents
GITHUB_ACCESS_TOKEN: <USER_WILL_PASTE_A_SHORT_LIVED_RESTRICTED_TOKEN_HERE>
TARGET_BASE_BRANCH: main
TARGET_WORK_BRANCH: micro-standard-v2-zai-execution-20260913
```

If ZAI cannot safely use the existing handoff branch, it must create a new execution branch from the verified current `main` and report its exact name before uploading. It must not push to `main`, force-push, delete branches, open or merge a pull request, or change repository settings.

## Required upload destinations

All execution outputs must be uploaded under a new run folder inside the handoff branch, for example:

`planning/micro-standard-v2-execution-handoff-2026-09/runs/<RUN_ID>/`

The run folder must contain the changed Standard package snapshot or a complete patch plus the exact changed-file list, wave reports, hashes, test outputs, and rollback boundary.

The interactive prototype must be uploaded separately under:

`planning/micro-standard-v2-execution-handoff-2026-09/runs/<RUN_ID>/prototype-v0.1/`

It must include the HTML file, local CSS/JS assets, `PROTOTYPE_README.md`, `PROTOTYPE_COVERAGE.md`, `PROTOTYPE_VALIDATION.md`, and key screenshots when available.

## Required upload records

At the end of each wave, upload:

- a wave execution report;
- a changed-file list and diff summary;
- SHA-256 records where applicable;
- tests and limitations;
- rollback boundary;
- an explicit `PASS`, `PASS WITH LIMITATIONS`, or `BLOCKED` status.

At the end of the complete run, upload one `FINAL_RUN_MANIFEST.json` and one `FINAL_RUN_README.md` linking the Standard result, the Prototype, and every report.

## Completion proof

After uploading, ZAI must return:

1. the exact repository URL;
2. the exact branch name;
3. the exact commit SHA;
4. the exact run folder path;
5. a file inventory;
6. confirmation that `main` was not modified;
7. confirmation that the token was not stored or exposed.

If upload fails, ZAI must not claim completion. It must deliver the files in the chat as a fallback and state the failure plainly.
