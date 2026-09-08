# Micro — Arabic-First Mobile Component Visual Library

Run `20260908T133450Z-16d11` · One direction («دفء الطابون» · Taboun Warmth) · Light Mode only · RTL-first · IBM Plex Sans Arabic.

## Open it

Open `micro-component-visual-library.html` directly in any modern browser (Chrome/Edge/Firefox/Safari, 2023+). No build step, no server, no network required. With internet, IBM Plex Sans Arabic loads as an enhancement; without it, the stack falls back to Noto Sans Arabic / system Arabic fonts and every feature still works.

## The four views

- **الأساسيات (Foundation)** — exact color tokens, type roles, spacing/radius scales, motion table, and the RTL icon mirror registry. Hex values live *only* here.
- **المكوّنات (Component Library)** — visual matrices for all 11 families: PrimaryValueBlock, MetricGroup/MetricRow, CompactTile, QuickActionRail, OperationalRow, Button, Input (+segmented/tabs/checkbox/switch), State (10 states), Sheet & Dialog, BottomNavigation + top zone, and 4 chart primitives. Interactive: button flow, retries, sheet and dialog stages.
- **تركيبة تجريبية (Test Composition)** — the single demo composition («يوم مخبز أبو محمد») inside a real device frame with width (320/360/390/430), direction, text-scale (100/130/200%) and motion controls. Press «إضافة بيع» for the full recording flow.
- **التحقق (Verification)** — device-pair previews, a geometry-only LTR clone, the live QuickActionRail peek measurements, the 9-check audit engine, grayscale mode, and the documented exceptions.

## Files

| File | Role |
|---|---|
| `micro-component-visual-library.html` | the lab (4 views, icon sprite, composition template) |
| `micro-component-visual-library.css` | base layer + all component families + lab chrome |
| `micro-component-visual-library.js` | views, instantiation, measurements, audit engine, overlays |
| `tokens.css` | source of truth: 77 `--mc-` tokens (spec-exact) |
| `component-contracts.md` | all 11 families × all required contract fields |
| `visual-direction.md` / `color-role-map.md` | the selected direction and every token's role/rules/contrast |
| `motion-and-interaction.md` | motion tokens and per-family interaction contracts |
| `accessibility-rtl-report.md` | contrast tables, bidi/mirroring audit, scaling risks |
| `coverage-matrix.md` | every family/state → HTML location → status |
| `decision-log.md` / `self-critique.md` / `verification-report.md` | decisions, review, and measured evidence |

## Hard rules the lab enforces

Light Mode only (no dark tokens, no switching); Arabic-first RTL; English digits; `DD/MM/YYYY`; currency `د.أ` only (never the Latin code); values bidi-isolated; `IBM Plex Sans Arabic` stack; spacing 2–40; radius 6/12/16/24/full (nav at 0); touch 44/48; QuickActionRail geometry locked (88×92 min, gap 8, padding 16) with measured peeks 16px at 320 and ≥28px above; motion 80/120/200/240-180/160-120/200ms; no bounce/spring/count-up.

## Extracting a family later

1. Copy `tokens.css` (add `tailwind-v4-theme.css` only if the host uses Tailwind v4).
2. Copy the family's marked CSS section — its header lists dependencies (always the base layer: focus rule, press base, `.icon-mirror`, reduced-motion rule).
3. Copy the JS module named in the section header if the family has behavior (`sheet`, `dialog`, `segmented`, `switch`, `list`, `motion`).
4. Copy the family's HTML matrix snippet as the canonical markup example.
5. Check `coverage-matrix.md` — every hook and state must survive the copy.

## Known limitations

Verification previews are inert by design; the 20-row batched-list policy and 28px value fallback are contract-level (see coverage matrix §5); screen-reader proof is structural (roles/labels/live regions) rather than an AT session; drag-to-dismiss is implemented but was verified through Escape/scrim equivalents in a headless environment.
