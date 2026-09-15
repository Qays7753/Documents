# Micro Product Rebuild Flow Studio

An independent, offline, single-file **Arabic RTL workspace** for the Micro product owner. It is not a report to read
and not only a diagram viewer — it is a working tool that combines four capabilities in one HTML file:

1. **Current-State Audit** — how Micro works today, imported from the verified User Flow Atlas (stable IDs preserved, evidence intact).
2. **Owner Flow Editor** — a simple Arabic canvas where the owner adds, connects, branches, annotates and versions workflows.
3. **Target-State Product Rebuild** — 17 Feature Build Cards, a justified 15-phase build roadmap, screen contracts, textual wireframes and current-vs-target comparison.
4. **Agent Review Package** — one-click export of an Arabic Markdown brief + machine-readable JSON diff that tells an implementation agent exactly what changed, why, and what must not change.

The owner is non-technical. Everything owner-facing is Arabic RTL plain language; technical identifiers (stable IDs,
file paths, test names) stay in English in secondary detail fields.

## Baseline and integrity

| Item | Value |
| --- | --- |
| Micro repository (read-only) | https://github.com/Qays7753/Micro |
| Micro commit analyzed | `4af025d38f04dfb36ee645a4f9ca3345e362bf5b` (main, 2026-09-06T13:21:03+03:00) |
| Source Atlas | `reports/2026/2026-09-06/micro-user-flow-atlas-001` in Qays7753/Documents |
| Source Atlas commit | `622af98c309160bc97625231bd4268a6a075808c` |
| Micro modifications by this package | **None** — no file touched, no PR, no branch. Analysis and design only. |

All 53 flows / 192 steps / 57 screens / 72 features / 48 services / 31 entities / 57 states / 28 transitions /
14 scenarios / 20 gaps / 22 decisions / 30 traceability rows from the Atlas are imported **with their original stable
identifiers** (no renames, no merges; the pre-existing cross-collection `ACT-01` actor/feature collision is handled by
typed references and documented in `MIG-002`).

## How to open

1. Download / clone this folder (the HTML plus `…-data.json` is self-contained — the JSON is embedded inside the HTML; the external copy is provided for tools).
2. Double-click `micro-product-rebuild-flow-studio.html` — it opens from `file://` with **zero network, zero CDN, zero remote fonts**.
3. Start on «ابدأ من هنا» and follow the four mode cards.

The owner's edits are saved locally in the browser (`localStorage`). «⤓ تصدير» produces a JSON backup;
«⤒ استيراد» restores it. The imported Atlas layer is immutable — editing an Atlas flow creates a derived
proposal copy (`FLW-P*`), never an overwrite. If `localStorage` is unavailable the studio says so honestly and
keeps work in memory.

## Contents

| File | Purpose |
| --- | --- |
| `micro-product-rebuild-flow-studio.html` | The offline workspace (all modes, editor, validator, versioning, exports) |
| `micro-product-rebuild-flow-studio-data.json` | Full data model 2.0.0: Atlas import + authored target layers |
| `micro-product-rebuild-flow-studio-schema.json` | JSON Schema description of the model (collections, IDs, enums) |
| `micro-product-rebuild-flow-studio-user-guide-ar.md` | Arabic owner guide (modes, editor actions, saving, exports) |
| `micro-product-rebuild-flow-studio-current-state-ar.md` | Arabic summary of the verified current state |
| `micro-product-rebuild-flow-studio-target-state-ar.md` | Arabic definition of the target design + honesty rules |
| `micro-product-rebuild-flow-studio-build-roadmap-ar.md` | Arabic build roadmap (15 phases, dependencies, alternative) |
| `micro-product-rebuild-flow-studio-feature-cards-ar.md` | Arabic digest of all 17 Feature Build Cards |
| `micro-product-rebuild-flow-studio-validation-report-ar.md` | Arabic validation report (structural + financial checks, QA evidence) |
| `micro-product-rebuild-flow-studio-agent-review-protocol-ar.md` | Arabic protocol for producing/reviewing Agent Review Packages |
| `micro-product-rebuild-flow-studio-change-log.md` | Build change log of this delivery |
| `examples/` | Six worked examples (feature cards, target flow graph, review package MD+JSON) |
| `supporting/qa-screenshots/` | Headless-browser QA captures (desktop + 390px mobile) |
| `INDEX.md` | Stable identifier catalog for this delivery |
| `metadata.yml` | Machine-readable metadata |

## Layer vocabulary (enforced in data and UI)

- `CURRENT_STATE` — verified in the Micro repository at the baseline commit.
- `APPROVED_TARGET` — explicitly approved future behavior (the owner approves inside the studio; nothing ships pre-approved).
- `FUTURE_EXPANSION` — supplier portal, courier access, multi-user, cloud sync, conversational assistant when not implemented. **Never displayed as implemented.**
- `OWNER_PROPOSAL` — created/edited by the owner, not yet approved.
- `UNVERIFIABLE` — cannot be proven from available evidence.

## Financial boundaries preserved

Collection is not profit · Debt is not cash · Purchase is not automatically COGS/expense · Owner money is separate ·
Unknown is never zero · A sale is recognized at delivery · A deposit is liquidity linked to an order, applied once at
delivery · Orders and deposits may exist without a saved customer · Receivables need a reusable party or an honest
unnamed state · Internal cashboxes are not banking · Corrections preserve history. The studio's validator flags
violations of these rules in Arabic with links to the offending nodes.

## Honest limitations

- Composed diagram **edges** of the 26 Atlas diagrams live only in the Atlas HTML; this studio imports their metadata and links out relatively (`../micro-user-flow-atlas-001/micro-user-flow-atlas.html`) — works when both folders sit side by side, as in the repository.
- PNG export rasterizes the SVG in-browser; under strict `file://` policies some browsers refuse — the SVG export (vector, same content) is the reliable path and the UI says so.
- No cloud sync, no multi-user, no server persistence, no automatic GitHub integration — by design; do not pretend otherwise when using the review package.

## Verification summary

Full details in `micro-product-rebuild-flow-studio-validation-report-ar.md`. Headline: JSON parses and all
cross-references resolve; stable IDs unique per collection namespace (Atlas collision documented); validator reports
**zero findings on the shipped seed data** and correctly flags deliberately broken examples (decision without
branches, revenue before delivery, duplicate deposit application); `file://` boot with zero console/page errors;
add/connect/drag/undo/redo/version-save/diff/review-export/persistence-across-reload all exercised in a real browser;
Arabic shaping, RTL layout and mobile 390px no-overflow confirmed by visual inspection.
