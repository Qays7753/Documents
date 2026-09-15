# Color Role Map — «دفء الطابون» · Taboun Warmth

- Run: `20260908T133450Z-16d11` · Agent 02 (Visual Identity) · Task `2-b`
- Token source: SPEC §6.3 (authoritative; no color outside this list exists in the direction).
- Light Mode only. No dark tokens, no theme switch, no `prefers-color-scheme` behavior, no invented browns, never `#B4613F`.

## 1. How to read this map

Every ratio below was computed with the WCAG 2.x relative-luminance formula (script in §7) and is written as `foreground / background`. Thresholds: **4.5:1** for normal text; **3:1** for large text (≥24px regular, or ≥18.66px at weight ≥600) and for graphics that carry meaning. "LARGE ONLY" means the pair is legal only as large text or as an icon/graphic; "FAIL" pairs are forbidden for that use and carry a stated mitigation.

## 2. Master token table

| Family | Token | Value | One-line role |
|---|---|---|---|
| Brand | `brand-atmosphere` | `#CC785C` | The one visible identity/graphic surface (terracotta). |
| Brand | `brand-tint` | `#F7EAE4` | Skin of the single tinted QuickActionRail tile. |
| Brand | `brand-ink` | `#964E33` | Readable brand ink; the limited filled text-bearing CTA. |
| Brand | `on-brand` | `#FFFFFF` | Text/icons on `brand-ink` fills only. |
| Brand | `press-overlay` | `#1F1E1D @ 8%` | The press treatment for any pressable element. |
| Surface | `canvas` | `#FAF9F5` | App background — the warm room. |
| Surface | `surface` | `#FFFFFF` | Cards, grouped metrics, sheets, tiles. |
| Surface | `sunken` | `#F0EEE6` | Inset wells: input fills, chart plot, metadata strips. |
| Ink | `ink-strong` | `#1F1E1D` | Primary text: the 32px value, titles, CTA-on-atmosphere. |
| Ink | `ink` | `#33322E` | Body text, row labels, chip text on tints. |
| Ink | `ink-muted` | `#6E6A60` | Labels above values, secondary row text. |
| Ink | `ink-subtle` | `#767265` | 13px qualifiers on surface/canvas only. |
| Ink | `ink-disabled` | `#B7B2A6` | Disabled-control text only (non-signal). |
| Structure | `line-soft` | `#EAE6DC` | Hairline between quiet siblings. |
| Structure | `line-strong` | `#DED9CB` | Control outlines (inputs, tiles). |
| Structure | `scrim` | `#1F1E1D @ 45%` | Behind Sheet/Dialog. |
| Semantic | `positive` / `positive-tint` | `#2E7D57` / `#E7EFE7` | Cash in, confirmed, completed, favorable movement. |
| Semantic | `danger` / `danger-tint` | `#B42318` / `#F7E7E2` | Cash out, negative direction, failure, destructive. |
| Semantic | `warning` / `warning-tint` | `#8A6520` / `#F4EDD8` | Overdue, threshold, attention, estimate exceeded. |
| Semantic | `info` / `info-tint` | `#3E5C76` / `#E8EDF1` | In progress, decision-critical pending context. |

## 3. Token-by-token roles, allowed/forbidden usages, pairing notes

### Brand

**`brand-atmosphere` `#CC785C`**
- Role: the calm visible identity — the one "hot" presence per viewport.
- Allowed: one identity/graphic block per viewport (empty-state graphic, one atmosphere header moment); large display moments; the oven-wall metaphor. Text on it must be `ink-strong` (5.08:1).
- Forbidden: as a text color; as a fill for CTAs (the CTA fill is `brand-ink`); as a border; as a status color; more than one filled atmosphere surface per viewport; white normal-size text on it (3.28:1 → large/graphics only).
- Pairing: `ink-strong` on it passes 4.5:1; `on-brand` white only for large text/icons ≥3:1; never `ink-muted` on it (1.65:1 FAIL). On `brand-tint` it is only 2.78:1 — do not put an atmosphere-colored icon on the tinted rail tile; use `brand-ink` there.

**`brand-tint` `#F7EAE4`**
- Role: the skin of the single tinted QuickActionRail tile.
- Allowed: one rail tile background (icon `brand-ink`, label `ink-strong`); nothing else in product surfaces.
- Forbidden: as a general surface or fourth plane; as chip background (chips use semantic tints); as a fill behind lists or cards; multiple tinted tiles.
- Pairing: `brand-ink` 5.20:1 and `ink-strong` 14.1:1 on it — both safe for text.

**`brand-ink` `#964E33`**
- Role: the readable brand ink and the limited filled text-bearing primary CTA.
- Allowed: primary CTA fill with `on-brand` text (6.11:1); brand-ink text on `surface`/`canvas`/`sunken`/`brand-tint` for small identity touches (e.g., the rail tile icon, a link-style emphasis); focus/identity accents.
- Forbidden: as a general-purpose surface, border, number color, or status color; as a fill for more than one action; any large atmosphere fields in it.
- Pairing: `on-brand` white on it 6.11:1 (pressed composite `#8C4A31` still 6.69:1 — press keeps contrast). As text: 5.20–6.11:1 on all light surfaces. Never pair with `#B4613F` (rejected legacy brown — must not appear anywhere).

**`on-brand` `#FFFFFF`**
- Role: text/icon color on `brand-ink` fills.
- Allowed: CTA label, CTA loading icon, small white glyph badges on semantic solids (all ≥5:1).
- Forbidden: as a background; on `canvas`/`surface`/`sunken`; on `brand-atmosphere` for normal text (3.28:1 — large text/graphics only); on scrim (2.96:1).
- Pairing: see `brand-ink`; on semantic solids 5.02–7.01:1.

**`press-overlay` `#1F1E1D @ 8%`**
- Role: the universal press treatment (80ms) for every pressable element.
- Allowed: as an overlay layer on any pressed control; composites: over `surface` → `#EDEDED` (ink text on it 10.96:1); over `brand-ink` → `#8C4A31` (white on it 6.69:1).
- Forbidden: as a hover-style permanent tint; as a disabled state; any other alpha of `#1F1E1D` except scrim 45% (and the overlay-shadow derivative reserved for Sheet/Dialog elevation, see `type-and-spacing-review.md` §7).
- Pairing: text contrast on pressed surfaces remains ≥4.5:1 in every audited case.

### Surfaces

**`canvas` `#FAF9F5`**
- Role: the app background; the PrimaryValueBlock and OperationalRow feeds live directly on it.
- Allowed: screen background; status-bar area color (dark system icons per SPEC §6.2); canvas-level content.
- Forbidden: card fills inside a surface (that is `sunken`'s job); tinting or recoloring per screen.
- Pairing: all inks pass on it (`ink-strong` 15.80:1 … `ink-subtle` 4.57:1).

**`surface` `#FFFFFF`**
- Role: the counter — cards, MetricGroup, tiles, Sheet/Dialog bodies, rail tiles.
- Allowed: exactly one grouped surface per default composition (SPEC §6.10); Sheet/Dialog fills.
- Forbidden: stacking surface-on-surface-on-surface (max two nested levels total: surface on canvas, sunken in surface); using a border+shadow stack that mimics elevation on static cards.
- Pairing: every text ink passes; hairlines on it are sub-3:1 by design (structure never relies on them alone — §6).

**`sunken` `#F0EEE6`**
- Role: the inset well — input fills on surfaces, chart plot area, compact metadata strips.
- Allowed: level-2 nesting inside `surface`; direct wells on canvas (search fields).
- Forbidden: sunken inside sunken; as a card background; as a divider substitute.
- Pairing: `ink` 11.05:1, `ink-muted` 4.64:1, `brand-ink` 5.26:1, `danger` 5.66:1 all pass; **`ink-subtle` on sunken is 4.14:1 → LARGE ONLY — use `ink-muted` for qualifiers inside wells**; `positive` on sunken 4.32:1 → large values only.

### Ink & structure

**`ink-strong` `#1F1E1D`** — primary reading ink (the 32px value, row values, sheet titles, focus rings). Passes 14.3–16.6:1 on all three surfaces and 5.08:1 on `brand-atmosphere`. Forbidden: as a fill (except press/scrim alphas), as decoration.

**`ink` `#33322E`** — body text, row labels, chip text on semantic tints (10.7–11.0:1 on tints; 12.2–12.8:1 on surfaces). On `brand-atmosphere` only 3.92:1 → LARGE ONLY; prefer `ink-strong` there.

**`ink-muted` `#6E6A60`** — labels above values, secondary text: 5.39/5.12/4.64:1 on surface/canvas/sunken (all pass). 4.60:1 on `positive-tint` (passes). On `brand-atmosphere` 1.65:1 — forbidden. Not for 13px qualifiers inside sunken (margin too thin) — use ≥15px there or promote to `ink`.

**`ink-subtle` `#767265`** — 13px qualifiers and compact metadata: 4.81:1 on `surface`, 4.57:1 on `canvas` (pass), **4.14:1 on `sunken` (FAIL normal) — restricted to surface/canvas**. Never for amounts or anything the user must act on.

**`ink-disabled` `#B7B2A6`** — text on genuinely disabled controls only (2.11:1 on surface — WCAG treats disabled-control text as incidental). Mitigation: disabled is *also* communicated by removal of press feedback, `line-soft` outline, and copy order; it is never a state the user must interpret from color alone. Forbidden anywhere the text still matters (unavailable values use `ink` + a label, not a faded number).

**`line-soft` `#EAE6DC`** — hairline between quiet siblings (1.25:1 on surface). Decorative rhythm only; never the sole boundary or a status signal.

**`line-strong` `#DED9CB`** — control outlines (inputs, tiles, quiet buttons) (1.41:1 on surface). Because it is sub-3:1, component identification is backed by fill vs canvas, typography, and the 2px `ink-strong` focus ring; the outline is texture, not the signal.

**`scrim` `#1F1E1D @ 45%`** — behind Sheet/Dialog only. Composites: `#979694` over canvas, `#9A9A99` over surface. Not a text surface, not a dimming utility elsewhere, never animated faster than 200ms.

### Semantic families (meaning, not decoration)

For each: **solid** = sign, icon, large value, chart line; **tint** = chip/state-segment background only.

- **`positive` `#2E7D57` / `positive-tint` `#E7EFE7`** — cash received, confirmed, completed, favorable movement (e.g. «قبض + 385.00 د.أ — مطعم النخيل»). Solid on surface 5.02:1, on canvas 4.76:1 (pass); **on its own tint 4.27:1 → LARGE ONLY for text (32px/600 values are fine); 13–15px chip text uses `ink`/`ink-strong`**; icons on tint 4.27:1 pass the 3:1 graphic bar. On `sunken` 4.32:1 → large only.
- **`danger` `#B42318` / `danger-tint` `#F7E7E2`** — cash out, negative direction, real failure, destructive action (e.g. «− 65.00 د.أ»). Solid passes everywhere including on its tint (5.47:1) — chip text in danger on its tint is legal but the default remains ink text + danger icon/sign.
- **`warning` `#8A6520` / `warning-tint` `#F4EDD8`** — overdue, threshold, attention (e.g. «طحين فاخر 10كغ — تحت الحد»). Passes on surface (5.30), canvas (5.03), tint (4.53 — narrow margin; keep warning text ≥15px and always sign/icon-paired).
- **`info` `#3E5C76` / `info-tint` `#E8EDF1`** — in progress, decision-critical pending (e.g. «قيد التسوية — شركة التوصيل السريع»). Passes everywhere (5.94:1 on tint).

Forbidden for all semantic colors: coloring an entire card; use as general UI accents (links, focus, selection use ink/brand roles); more than two families in one composition; status signaled by color alone — every semantic use is paired with a sign, label, icon, or structural cue (SPEC §6.3).

## 4. Computed contrast — text pairs (WCAG, threshold 4.5 normal / 3 large)

| Foreground | Background | Ratio | Verdict |
|---|---|---|---|
| ink-strong | surface | 16.64:1 | PASS |
| ink-strong | canvas | 15.80:1 | PASS |
| ink-strong | sunken | 14.33:1 | PASS |
| ink | surface | 12.83:1 | PASS |
| ink | canvas | 12.18:1 | PASS |
| ink | sunken | 11.05:1 | PASS |
| ink-muted | surface | 5.39:1 | PASS |
| ink-muted | canvas | 5.12:1 | PASS |
| ink-muted | sunken | 4.64:1 | PASS |
| ink-subtle | surface | 4.81:1 | PASS |
| ink-subtle | canvas | 4.57:1 | PASS |
| ink-subtle | sunken | 4.14:1 | **LARGE ONLY** — restrict ink-subtle to surface/canvas |
| ink-disabled | surface | 2.11:1 | **FAIL** — disabled controls only (WCAG-incidental; non-color cues required) |
| ink-disabled | canvas | 2.01:1 | **FAIL** — same rule as above |
| brand-ink | surface | 6.11:1 | PASS |
| brand-ink | canvas | 5.80:1 | PASS |
| brand-ink | sunken | 5.26:1 | PASS |
| brand-ink | brand-tint | 5.20:1 | PASS |
| ink-strong | brand-atmosphere | 5.08:1 | PASS — the required text ink over atmosphere |
| ink | brand-atmosphere | 3.92:1 | **LARGE ONLY** — prefer ink-strong |
| ink-muted | brand-atmosphere | 1.65:1 | **FAIL** — forbidden |
| on-brand | brand-ink | 6.11:1 | PASS — white text lives ONLY on the brand-ink CTA |
| on-brand | brand-atmosphere | 3.28:1 | **LARGE ONLY** (large text / icons) |
| positive | surface | 5.02:1 | PASS |
| positive | canvas | 4.76:1 | PASS |
| positive | sunken | 4.32:1 | **LARGE ONLY** |
| positive | positive-tint | 4.27:1 | **LARGE ONLY** for text; icons OK (≥3:1) |
| danger | surface | 6.57:1 | PASS |
| danger | canvas | 6.24:1 | PASS |
| danger | sunken | 5.66:1 | PASS |
| danger | danger-tint | 5.47:1 | PASS |
| warning | surface | 5.30:1 | PASS |
| warning | canvas | 5.03:1 | PASS |
| warning | warning-tint | 4.53:1 | PASS (narrow margin — keep warning text ≥15px, sign/icon-paired) |
| info | surface | 7.01:1 | PASS |
| info | canvas | 6.65:1 | PASS |
| info | info-tint | 5.94:1 | PASS |
| on-brand | positive | 5.02:1 | PASS (small filled badges) |
| on-brand | danger | 6.57:1 | PASS |
| on-brand | warning | 5.30:1 | PASS |
| on-brand | info | 7.01:1 | PASS |
| ink-strong | positive-tint | 14.19:1 | PASS — default chip text ink |
| ink | danger-tint | 10.68:1 | PASS |
| ink | warning-tint | 10.97:1 | PASS |
| ink | info-tint | 10.89:1 | PASS |
| ink-muted | positive-tint | 4.60:1 | PASS |
| ink-muted | surface | 5.39:1 | PASS |

## 5. Computed contrast — graphics & structure (threshold 3:1)

| Foreground | Background | Ratio | Verdict |
|---|---|---|---|
| brand-atmosphere | surface | 3.28:1 | PASS (identity graphic on white) |
| brand-atmosphere | canvas | 3.11:1 | PASS (narrow — verify on real screens) |
| brand-atmosphere | brand-tint | 2.78:1 | **FAIL** — no atmosphere-colored icon on the tinted tile; use `brand-ink` |
| brand-ink | positive-tint | 5.21:1 | PASS |
| positive | positive-tint | 4.27:1 | PASS (icon/sign on tint) |
| danger | danger-tint | 5.47:1 | PASS |
| warning | warning-tint | 4.53:1 | PASS |
| info | info-tint | 5.94:1 | PASS |
| line-strong | surface | 1.41:1 | Below 3:1 by design — decorative texture; never the sole boundary or status signal |
| line-soft | surface | 1.25:1 | Same rule as line-strong |
| line-strong / line-soft | canvas | 1.34:1 / 1.18:1 | Same rule as line-strong |
| surface | canvas | 1.05:1 | Sub-3:1 by design — card/canvas separation comes from grouping + spacing, not from a contrast step; content hierarchy never relies on the card edge |
| sunken | surface | 1.16:1 | Same rule as surface/canvas |
| sunken | canvas | 1.10:1 | Same rule as surface/canvas |

**Mitigation (structure):** inputs and quiet controls are identified by fill-vs-canvas, typography, placeholder/label text, and a 2px `ink-strong` focus ring (16.6:1); the beige outlines are finish, not signal. This satisfies WCAG 1.4.11 without inventing darker line colors.

## 6. Alpha composites (press & scrim)

- `press-overlay` over `surface` → composite `#EDEDED`; `ink` text on it **10.96:1**, `ink-muted` **4.61:1** — pressed states keep full readability.
- `press-overlay` over `brand-ink` CTA → composite `#8C4A31`; `on-brand` white text on it **6.69:1** — the CTA press stays compliant.
- `scrim` over `canvas` → `#979694`; over `surface` → `#9A9A99`. The scrim is not a text surface (content sits on the Sheet/Dialog surface above it); `on-brand` on scrim is 2.96:1, which is why nothing readable is ever placed directly on the scrim.

## 7. Method

Ratios computed with the WCAG 2.x relative-luminance formula (sRGB linearization, L = 0.2126R + 0.7152G + 0.0722B; ratio = (L1+0.05)/(L2+0.05)), alpha pairs composited before computing. The script used (run once, results recorded above):

```python
def h2rgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def lin(c):
    c/=255.0
    return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def lum(h):
    r,g,b=[lin(x) for x in h2rgb(h)]; return 0.2126*r+0.7152*g+0.0722*b
def cr(fg,bg):
    l1,l2=lum(fg),lum(bg); hi,lo=max(l1,l2),min(l1,l2)
    return (hi+0.05)/(lo+0.05)
def comp(fg,alpha,bg):
    f,b=h2rgb(fg),h2rgb(bg)
    return '#%02X%02X%02X'%tuple(round(f[i]*alpha+b[i]*(1-alpha)) for i in range(3))
```

Pairs audited: all inks on all surfaces/tints, brand family cross-pairs, semantic solids on surfaces and own tints, white on all solids, structure lines, surface steps, and press/scrim composites.

## 8. Color-economy enforcement (SPEC §6.3 checklist)

1. Max one filled brand-family surface/action per viewport → CTA (`brand-ink`) or empty-state atmosphere block, never both.
2. Max two semantic families per composition → positive+danger pair, or warning alone, or info alone.
3. Max two colored numerical values per composition → the +/− pair; everything else `ink-strong`.
4. Max one tinted QuickActionRail tile → first tile, `brand-tint` + `brand-ink` icon + `ink-strong` label.
5. Max three visible dividers → spacing-first layout; hairlines reserved (see `type-and-spacing-review.md` §6).
6. Max two nested surface levels → canvas → surface → sunken.
7. Never color an entire card → semantic color only on chips, signs, icons, and the two metric values.
8. Color never the only status signal → every semantic use is paired with sign, label, icon, or structure.
9. No invented colors → only the 27 tokens above (plus the two spec-defined `#1F1E1D` alphas) exist in the direction; `#B4613F` must never appear.
