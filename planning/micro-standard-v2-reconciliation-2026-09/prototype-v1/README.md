# Prototype v1 — Visual Validation of the Updated Micro Standard v2

**Visual validation prototype — not product truth · نموذج تحقق بصري — ليس حقيقة منتج**

## What this is

A standalone, dependency-free HTML/CSS/JS artifact that demonstrates every contract changed by reconciliation run `run-20260914-msv2-reconciliation-01` (branch `micro-standard-v2-reconciliation-final-20260914`). It is built from the updated Standard contracts — not copied from Prototype v0 and not copied from Micro production screens.

## How to open

Open `prototype.html` directly in any modern browser (no build step, no network, no external dependencies). The declared fonts are the Standard's families ("IBM Plex Sans Arabic" / "IBM Plex Mono") with system fallbacks; on machines without them, the system Arabic font renders instead.

## Demo chrome (outside every composition)

- **Scene tabs** — six scenes (see `PROTOTYPE_COVERAGE.md`).
- **Width** — 320 / 360 / 390 / 430px frame widths.
- **Text** — 100 / 130 / 200% text scale, emulated at the token level (the `--text-*` size tokens are scaled; this is a disclosed emulation method, equivalent to browser text scaling for a token-driven system).
- **Motion** — normal / reduced (plus native `prefers-reduced-motion` support).
- **سلطة العقود** — the authority ladder drawer.
- A persistent truth label in the chrome **and** a truth strip inside the frame, so every screenshot carries the boundary.

## What it deliberately is not

- It defines **no** Micro routes, Micro state words, financial formulas, product terminology, or future product decisions.
- The only vocabulary it uses is the Standard's own documented examples («سجّله» action chip, «غير متاح», the official four navigation destinations) and neutral illustrative labels («عنصر توضيحي», «قيمة توضيحية»).
- The knowledge-state words («مؤكد», «غير مؤكد», «تقديري», «غير مكتمل», «بحاجة لمراجعة», «غير معروف») are the Standard's example words — product-owned, presentation-only.
- `د.أ` appears only as the Standard's contextual currency unit beside numbers, never inside them; numerals are English digits, bidi-isolated (`dir="ltr"`), inside the Arabic-first RTL composition.
- The Snackbar appears **only** behind an explicit opt-in toggle (default OFF) because it is an optional contract, not a mandatory one.

## Files

- `prototype.html` — structure and neutral content.
- `prototype.css` — the updated Standard token block (embedded verbatim values) plus demo styles.
- `prototype.js` — behaviors only; every displayed value is a fixed literal (no computation on displayed numbers).
- `PROTOTYPE_COVERAGE.md` — the contract-to-scene coverage map.
- `PROTOTYPE_VALIDATION.md` — what was validated, how, and the honest limitations.
- `evidence/scene-s1..s6.png` — full-page captures at 390px (local headless Chromium; system Arabic fonts).
