# Change Log — Micro Product Rebuild Flow Studio (delivery 001)

All dates 2026-09-07 (Asia/Amman). Baselines: Micro `main` @ `4af025d38f04dfb36ee645a4f9ca3345e362bf5b`
(read-only throughout); source Atlas `reports/2026/2026-09-06/micro-user-flow-atlas-001` @ Documents `622af98`.

## Phase 0 — Inspection (before building)

- Fetched both repositories. Micro `main` confirmed unchanged since the Atlas baseline (`4af025d`, no new commits) —
  Atlas evidence therefore remains valid; no re-audit performed, none needed. Micro working tree untouched by this task.
- Documents `main` advanced to `6f5d3c3` (parallel deliveries 14/15); local clone synced.
- Read the Atlas data model end-to-end: 16 collections, stable IDs, status vocabulary, per-collection field shapes;
  identified the pre-existing cross-collection `ACT-01` collision (actor vs feature) and recorded the typed-reference
  handling strategy (MIG-002).

## Phase 1 — Analysis and design plan

- Produced the 9-point plan (Atlas model, import strategy, target/proposal model, schema 2.0.0 + migration,
  editor interaction model, feature-card model, versioning & review package, validation rules, deliverables & tests)
  in the conversation before implementation, per the required process.

## Build — data model

- `build_data.py`: imports all 16 Atlas collections preserving IDs verbatim; adds `layer`/`status`/`migration`/
  `atlasStatus` per the documented status map; authors the target layer (17 FTR cards incl. the 36-field build cards
  and the ten Arabic questions, 17 target flows, 17 screens + contracts + textual wireframes, 15 phases, 18
  dependencies, 42 acceptance criteria, 12 financial boundaries, 6 migration notes, 2 personas, 14 domains, 5 seed
  notes, VER-001 + LOG-001..003).
- `schema.json`: JSON-Schema description of model 2.0.0 (collections, ID patterns, enums, layer vocabulary).

## Build — studio application

- Single-file Arabic RTL HTML (`template.html` + six JS modules inlined by `build_studio.py`, seed JSON embedded
  as `<script type="application/json">`): start page, mode switcher, sidebar, global search, modal/confirm system,
  download/export helpers, honest localStorage fallback.
- Mode 1 — audit: dashboard, 12 catalogs, flow detail with step timeline + effects + evidence, screen detail,
  states/transitions, decisions, traceability, Atlas diagram catalog with relative link-out, gaps, glossary, changelog.
- Mode 2 — editor: SVG canvas (pan/zoom/fit, wheel zoom), 12-shape node palette, click-select + properties panel,
  drag with undoable move commands, connect mode, edge editing (label/condition/control|data|failure), safe delete,
  undo/redo stacks, back/forward navigation, keyboard shortcuts, FUTURE-layer protection, `deriveFlow()`
  (Atlas flow → FLW-P* proposal copy; source never modified), SVG export, PNG export with honest limitation dialog.
- Mode 3 — rebuild: feature library with filters, full feature-card view (approve button, open-in-editor, MD export,
  owner notes, add-note), roadmap timeline with dependency table + documented alternative-order proposal,
  current-vs-target comparison.
- Mode 4 + safety: validator (structural + financial + source-integrity rules, Arabic messages, links),
  versions (save with computed diff, timeline, side-by-side compare), agent review package generator (Arabic MD +
  authoritative JSON), workspace JSON export/import with schema check, audit log, unsaved-change guard.

## Fixes during browser QA (recorded honestly)

1. `setPointerCapture` threw on synthetic pointer events and aborted node selection — wrapped in try/catch and
   restructured selection to avoid full redraw (element identity preserved for dragging).
2. `renderNodeProps` referenced an undefined `scs` variable (screens list) — fixed to `scrs`.
3. `C.undoStack`/`C.redoStack` are getter properties, not functions — all call sites fixed; add/undo/redo verified.
4. Validator findings on first run (4×P1 gate-branches missing in FLW-T08/T09; 10×P2 no-exit nodes) — **fixed in the
   seed data** (added missing branches/edges incl. the «لا» branch of the deposit gate and the delivery-failure retry
   loop), then re-validated to zero findings. FIN-UNKNOWN rule refined to exclude input nodes presenting the honest
   unknown option.

## Verification

- `node --check` on all six JS modules (pass); JSON parse + ID uniqueness + cross-reference checks (pass;
  ACT-01 collision documented); offline check — no external resources; secret scan clean.
- Headless-browser QA on `file://` (twice, final run from the delivered folder): boot with zero console/page errors;
  audit flow detail; editor load/add-node/undo/redo/connect/drag/edit-save; validator clean-on-seed and
  catches injected broken examples (decision without branches → P1; revenue before delivery in an order flow → P1;
  duplicate deposit application → P1); version save + diff rows; review-package generation with both downloads;
  search by ID and Arabic; feature card renders ten-questions; persistence across reload; mobile 390px no overflow.
- VLM visual inspection of screenshots: Arabic shaping, RTL layout, SVG node/edge rendering, no overlap/cut-off — pass.
- QA captures saved to `supporting/qa-screenshots/` (6 PNG).

## Deliverables

13 required files + 6 examples + QA screenshots, delivered to
`reports/2026/2026-09-06/micro-product-rebuild-flow-studio-001/` in the Documents repository only.
**No Micro file was modified; no Micro PR was opened; nothing claims Micro implementation of target-state designs.**
