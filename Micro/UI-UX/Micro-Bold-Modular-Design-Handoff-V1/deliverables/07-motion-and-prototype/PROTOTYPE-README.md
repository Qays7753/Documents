# Prototype README — How to View

## What this is

An isolated, self-contained HTML/CSS/JS prototype of the three Micro visual directions and the refined candidate. It runs offline (fonts bundled, no build step) and lives only inside this design handoff repository. The Micro production repository is untouched.

## Quick start

**Option A — just open it:** open `prototype/index.html` in any modern browser. The hub links to every screen of every direction.

**Option B — local server (recommended):**

```bash
cd prototype
python3 -m http.server 8799
# then visit http://localhost:8799
```

## Layout

```
prototype/
  index.html                  hub: all screens of all directions
  assets/fonts/               IBM Plex Sans Arabic + IBM Plex Mono (OFL, local)
  assets/app.js               interactions (sale flow, sheets, choice chips)
  c1-warm-bold/               direction C1 (15 screens + tokens + stylesheet)
  c2-confident-bold/          direction C2
  c3-dynamic-modular/         direction C3
  c2r-selected-candidate/     refined selected direction (C2 base + refinement layer)
```

Each screen is a standalone HTML file; `foundation.html` in each direction folder is the foundation board (palette, measured contrast, type scale, components, states, storyboard).

## The interactive path (Success Impact demo)

1. Open `c2r-selected-candidate/home-positive.html`
2. Tap **بيع** in the Quick Action Bar.
3. The sale form opens (amount 25.00, fixtures from file 04).
4. Press **سجّل البيع** — immediate press feedback, then «جارٍ التسجيل…».
5. Success screen: amount, destination, and the updated cash value **161.00** with a single highlight pulse.
6. **عرض العملية** returns to context.

## Proof controls (query parameters — no visible UI chrome)

| Param | Effect |
|---|---|
| `?scale=text200` | 200% text stress (doubles rem-based text; no horizontal scroll) |
| `?static=1` | neutralizes the sticky bottom nav (for clean full-page screenshots) |

Example: `home-positive.html?scale=text200`

## Dark mode

`home-dark.html` in each direction folder renders the dark palette (design proof; in-product entry stays inside Settings per IA-D04).

## Reduced motion

The prototype honors the OS `prefers-reduced-motion` setting automatically — all pulses and transitions collapse to static highlights.

## Fair-comparison note

C1, C2, and C3 render the **same DOM** from one content model with the exact fixtures of file 04. All visual differences live in each direction's own stylesheet — one designer, one quality bar, same content and figures everywhere.
