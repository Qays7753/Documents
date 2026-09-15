# Micro Component Visual Library — README

**Run:** `zed-ai-runs/20260908T133347Z-352b/` · 2026-09-08
**Deliverable:** a single, cohesive, Arabic-first mobile component visual library
(visual foundations + reusable components) for a Jordanian small-business financial
and operational application. This is NOT a product, screen map, backend, or
authentication — it is the layer future product screens will be composed from.

## 1 · Open it

Open `final/micro-component-visual-library.html` directly in a browser
(file:// works — everything is local, including the fonts in `final/fonts/`).
No server, no build, no network. Four views via the top tabs:

| Tab | What it is |
|---|---|
| الأسس (Foundation) | the token system rendered as real usage: surfaces, brand, ink, semantics, type, spacing, icons + mirror registry, motion |
| المكونات (Components) | one visible matrix per family with real variants and states; interactive demos |
| تركيبة اختبار (Test Composition) | one product-grade composition obeying the full budget; the five sheets are live (try «إضافة مصروف» → save and watch the numbers update instantly) |
| التحقق (Verification) | four live frames (320/360/390/430) + a runtime audit panel (rail peek measurements, overflow scans, touch-target scans, text scans, contrast table) |

Header controls: direction (RTL default / LTR geometry check) · text scale
(100/130/200%) · motion (full/reduced) · frame width. Audit evidence is deliberately
kept out of the phone compositions.

## 2 · Files

| File | Role |
|---|---|
| `micro-component-visual-library.html` | the lab (views, composition, matrices, verification) |
| `micro-component-visual-library.css` | component styles (`.mc-*`), lab chrome, foundation & verification styles |
| `micro-component-visual-library.js` | view switching, controls, sheet/dialog engine, demos, runtime audits |
| `tokens.css` | canonical token layer — the single source of truth (exact Micro tokens) |
| `fonts/` | IBM Plex Sans Arabic 400/500/600 (arabic+latin woff2 subsets) for offline use |
| `component-contracts.md` | 19-field contract for every family |
| `visual-direction.md` | the selected direction «دفء الحانوت» |
| `color-role-map.md` | every token's role + computed contrast contract |
| `motion-and-interaction.md` | timing scale + proven interaction contracts |
| `accessibility-rtl-report.md` | contrast, targets, scaling, bidi, mirroring, SR |
| `coverage-matrix.md` | family/state → location → verified status |
| `decision-log.md` | 22 decisions with rejected alternatives and evidence |
| `self-critique.md` | the seven mandated questions, answered honestly |
| `verification-report.md` | what was tested, what passed, bugs found & fixed |

Optional adapter (kept separate per spec): `../03-design-system-engineering/
tailwind-v4-theme.css` maps the same tokens to Tailwind v4 `@theme`. The lab itself
is deliberately framework-neutral vanilla HTML/CSS/JS (the target repo has no code stack).

## 3 · Hard rules baked in (grep-verified)

Light mode only (no `.dark` / `prefers-color-scheme`) · currency is «د.أ» only (never
"JOD") · English digits, bidi-isolated, 3-decimal fils, U+2212 minus · DD/MM/YYYY ·
Arabic ≥14px (rail labels 13px is the spec-pinned exception) · 44/48px touch targets ·
≤2 semantic families and ≤2 colored numbers per composition · one filled brand action ·
one tinted rail tile · no paper-plane icon · no count-up, no bounce · chart time axes
stay LTR · unknown is never rendered as 0.

## 4 · Agent lineage

01 UX architecture · 02 visual identity · 03 design-system engineering · 04 user &
accessibility review · 05 synthesis & critique (see sibling folders and
`../run-report.md`). The lab was built by the coordinator from these inputs and then
verified headlessly (see `verification-report.md`).

## 5 · Known limitations (honest)

Phone-lab previews use fixed device-class heights; nav switching is demo-state (no
screen map by spec); conflict resolution is represented, not implemented; verification
ran on one engine (Chromium) — on-device and screen-reader passes are future work.
