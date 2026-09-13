# Previous Wave Boundaries and Current Starting Point

## GitHub state verified before this handoff

- `origin/main`: `dfa8bf7d7f7a2c01f256d4c77d359c8a5770d60b`
- `origin/micro-standard-v2-current-20260912`: `f417cad89429d37ce8891e944849a19aa548b835`
- `origin/micro-standard-v2-foundation-development`: not present on remote at verification time.
- Historical `f64e8616...` is not a usable remote source and must not be treated as the current package.

## What the current published package is

The package in `main` contains 31 files: 29 core/executable files and two metadata files. The hashes of the key package files checked on `main` and `micro-standard-v2-current-20260912` match for `design-tokens.css`, `component-gallery.html`, and `README.md`.

## History boundary

The prior Wave 0/A+B+C/D work was performed in a development context whose final commit was not confirmed as a published remote branch. Do not reconstruct or assume unpublished changes. Read the current 31-file package on `main` as the execution baseline, create a new baseline/rollback from that exact state, and apply only the approved delta.

## Do not redo silently

The new execution must not:

- overwrite `main`;
- assume `f64e8616...` is available;
- re-run an old wave simply because an old report mentions it;
- reintroduce old gold, broad Terracotta recolor, dark mode, generic dashboard/card gallery, or Accounting skin;
- use Prototype v0 as a source package;
- treat the external ZAI review as a substitute for inspecting the actual current files.

## Safe execution boundary

All changes must be made on a new feature branch from current `main`, with a complete baseline and rollback. Every changed file must be listed and justified. If a change is already present in the current file, preserve it and record it as already satisfied instead of editing it again.

## Verification limitations

The current handoff does not claim physical Samsung testing or screen-reader testing. ZAI must distinguish local browser/rendered evidence from device or assistive-technology evidence and must not write a stronger claim than the test performed.
