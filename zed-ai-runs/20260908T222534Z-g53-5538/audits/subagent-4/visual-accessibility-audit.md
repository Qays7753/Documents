# Visual & Accessibility Audit — Subagent 4 (Task R4-d)

**Target:** `zed-ai-runs/20260908T201936Z-g53-252a/visual-foundation-package/` (component-gallery.html rendered offline)
**Authority:** `SOP_VISUAL_ONLY.md` §3/§4 + source-pack rendered references · **Date:** 2026-09-09
**Method:** docs-vs-rendered coherence read · live computed-style probes (real keyboard focus, measured heights at 100%/200% root) · independent WCAG 2.1 recomputation of 50 pairs (`sub4-visual-critique.py` → `contrast-grayscale-results.json`) · grayscale luminance-ladder confusability · a11y snapshot review (320/360/390/430 × LTR/RTL) · behavior captures.

---

## 1. Overall verdict

This is a **disciplined, direction-faithful system with one real accessibility defect, a cluster of programmatic-state gaps, and three demonstration gaps against the repair contract**. The palette discipline is genuine: every documented contrast claim in `color-system.md` reproduced exactly in my independent computation (the five corrections — 6.11, 5.08, 7.01, 6.80, 4.51 — are real), terracotta never touches an amount or an error, no gradients/glow/colored shadows exist, and the elevation ladder is intact. The rendered system is calm-but-alive: press scales, a sliding thumb, live chips, a guarded loading button, and the ivory-recess KPI card give it exactly the "energy from hierarchy and feedback" the SOP asks for. **Repair A is fully satisfied** — the six button states appear as one labeled strip of the *same* button (see §6), which is the single most repair-relevant thing the gallery does right.

The failures concentrate where measurement stopped: **real focus behavior** (the ring is killed on inputs by a CSS override — the gallery's static "Focused" demo lies about actual behavior), **programmatic selection state** (chips/segmented/nav are color- and class-only to assistive tech), **the focus ring's relationship to dark fills** (it is literally the same color as the secondary button), and **Repair H's demonstration matrix** (no 130/200% text scale, no long Arabic labels). The color-role risk the repair brief names is present but inherited rather than introduced: teal codes five meanings (secondary action, ghost, focus, dropdown selection, Ready status), and the Ready vs Moved tints are 1.04:1 apart.

**Verdict: repairable within the existing ramp — no new colors are needed for any resolution below.**

---

## 2. Coherence — docs vs rendered system

| Claim (docs) | Rendered reality | Verdict |
|---|---|---|
| "focus shifts the border **and adds the system ring**" (inputs family head; button-system.md Focused contract) | `.input:focus { outline: none }` (component-gallery.css:194) overrides the global `:focus-visible` ring. Verified live: Tab-focused `#f-name`/`#f-notes` compute `outline-style: none`; only a 1px border shifts (1.25→3.24:1) over 200ms | **Contradicted — S4-01 (blocker)** |
| "Every pairing carries an icon or dot" (badges family head, html:300) | Third badge row (Paid/Cancelled/Returned) is text-only; 5 of 7 tags in the Chips section lack icons | Contradicted — S4-08 |
| "long names use line-clamp" (data-display-system.md) | `.row-title` is `nowrap + ellipsis` | Contradicted — S4-15 |
| "Everything is rem-based so large-text mode grows the control" (button-system.md) | Buttons/chips/labels scale ✓; but segmented `min-height: 40px` is hardcoded px (verified: at 32px root the seg button stayed content-sized) | Partially contradicted — S4-09 |
| "Top bar: canvas-colored at rest" / shadow-sm = segmented thumb only | `.iconbtn-primary` carries shadow-sm in the resting top bar (css:167) | Minor — S4-19 |
| "Touch target minimum 44×44" (SOP §6; evidence panel repeats it) | Segmented buttons 40px, underline tabs 40.8px (measured) | Failed — S4-09 |
| Five WCAG corrections + full contrast table | All 33 text pairs re-verified — every value reproduces; no undocumented pair fails (exempt disabled aside) | **Confirmed honest** |
| 320/360/390/430 × LTR/RTL without overflow | `overflow-320-{ltr,rtl}.txt`: scrollWidth == clientWidth == 320; RTL snapshots structurally identical to LTR | Confirmed |
| Zero network, offline-first | console empty, `network-remote-resources.txt` = `[]` | Confirmed |

---

## 3. Terracotta / teal load map

### Terracotta — verdict: **restrained; identity + selection only; no semantic leakage except one inherited tile**

| Element | Location | Step | Role | Verdict |
|---|---|---|---|---|
| Primary button (+ action bar, dialog, empty CTA) | Buttons, Navigation, Overlays, Empty | 700 | identity | appropriate |
| Pressed / loading fill | Buttons › States | 800 | state | appropriate (one step deeper + 0.97 scale — a state, not a 7th color) |
| iconbtn-primary | Buttons pair-row, top bar "More" | 700 | identity | appropriate (shadow-sm violation, S4-19) |
| FAB | Navigation | 700 | identity | appropriate — but deepened from the source's 500 (S4-13) |
| Selected chip | Chips | 700 fill, no border | selection | appropriate (grayscale-strong: L 0.12 vs 1.0) |
| Segmented thumb / underline / count | Segmented | 700 | selection | appropriate (thumb vs ivory track 5.26:1) |
| Active nav pill + icon + label | Navigation | 100 + 700 | selection | appropriate — pill alone is 1.24:1 vs white; icon fill-switch + 700 label carry it |
| **Reserved tile chip** | Cards › featured KPI | 100 + 700 | identity graphic | **risk — quasi-semantic "held funds" meaning next to a positive "Free" tile; Prohibition 5 says terracotta is never data meaning. Inherited from the source's "حق المحل" jar chip. Recommend operational.50/600 (S4-12)** |
| Snackbar action | Overlays | 200 | identity-on-dark | appropriate (10.68:1) |
| theme-color meta | head | **500** | identity | the *only* rendered 500 in the package — zero uses inside compositions (S4-13) |
| Ramp swatches | evidence panel | all | documentation | appropriate (outside compositions) |

**Terracotta overload verdict: no overload.** The ramp is used in a disciplined ladder: 700 identity/selection, 800 state-of-700, 100 tint, 200 dark-surface accent, 500 nowhere-but-meta. No two terracotta steps carry unrelated meanings. The character-level observation (S4-13, judgment): because all text-bearing fills deepened to 700, the rendered identity is uniformly deep brown-terracotta — coherent, but the documented identity color `#CC785C` no longer exists on screen; either give it one sanctioned non-text moment (FAB fill: white icon = 3.28:1, passes 1.4.11) or re-describe 700 as the rendered identity step.

### Teal — verdict: **five roles on one family; the conflation is inherited but the gallery deepens it**

accent.600 = secondary fill, ghost text, focus ring; accent.500 = input focus border; accent.50/600 = dropdown selection **and** the Ready status. Consequences:

- **Ready vs Moved: 1.04:1** (accent.50 #E3F5F5 vs operational.50 #E8EEF3) — two unrelated semantic statuses render as the same pale pill in grayscale and nearly the same in color (S4-04).
- Selected chip (terracotta fill) vs selected menu row (teal tint) = two different "selected" grammars in one system; both documented, inherited divergence (S4-11).
- accent.700 (secondary pressed) vs operational.600 (Transfer fill): 1.08:1 — a state of one family is indistinguishable from a semantic fill of another (grayscale note).

---

## 4. State distinctness + grayscale

**Grayscale luminance ladder** (computed): ink .013 · p800 .073 · accent700 .089 · **op600 .100** · **p700 .122** · ink-sec .145 · **neg500 .149** · **accent600 .157** · **pos500 .159** · accent500 .274 · disabled .447 · p100 .798 · gold50 .841 · **op50 .848** · recessed .854 · **pos50 .859** · **accent50 .882** · canvas .947 · surface 1.0.

| Family | Default | Pressed | Focused | Disabled | Loading | Completion / Error / Empty | Non-color cues? |
|---|---|---|---|---|---|---|---|
| Button | 700 fill | 800 + scale 0.97 | ring (gap-dependent) | grey fill, no shadow | 800 + spinner + "Saving" | completion: pos.50 tint + check + "Saved" | **strong** — every state changes structure/text too |
| Chip | white + border | scale | ring | recessed + grey text | n/a | n/a | good (fill/border change) |
| Input | white + soft border | — | border shift + (ring broken — S4-01) | recessed + grey | — | error: red border + icon + message | good on error; weak on focus |
| Nav | outline icon, grey label | scale | ring | n/a | — | active: filled icon + darker label + pill | **strong** (icon fill-switch) |
| Segment | grey text on ivory | — | ring | n/a | — | thumb slide / underline + count | **strong** |
| Row amount | semantic color + sign + icon | — | — | — | — | — | **strong** (sign + tile icon always) |

**Grayscale risks (computed, §grayscale_risks in JSON):** Ready/Moved tints 1.04; secondary-pressed vs operational fill 1.08; Accept vs Delete fills 1.05 (saved by labels); all tints vs recessed ~1.0–1.07; skeleton vs canvas 1.10 with pulse removed under reduced motion. Pressed deltas themselves survive grayscale (ΔL .05–.07 + scale). The system's saving grace is consistent: **every semantic amount/row pairs color with sign + icon + text**, so grayscale convergence is cosmetic, not informational — except the badge-tint pair (S4-04) where the tint IS the only structural difference between statuses of the same shape.

---

## 5. Measured contrast failures (independent recomputation)

All 33 text pairs pass AA (exempt inactive pairs aside) — the package's table is honest. The failures are in non-text/UI territory the package did not compute:

| Pair | Ratio | Where | Severity |
|---|---:|---|---|
| accent.600 ring / accent.600 secondary fill | **1.00** | secondary button focused (live-verified) | major — S4-02 |
| accent.500 check / accent.50 menu row | **2.88** | Category dropdown selected option (css:245 inline SVG) | major — S4-07 |
| accent.600 ring / primary.700 fill | 1.20 | primary/FAB focused | minor — S4-14 |
| primary.100 nav pill / white nav | 1.24 | active nav pill | minor (composite state compensates) |
| spinner track (white 35%) / primary.800 | 2.44 | loading spinner | note (label+motion carry state) |
| disabled / recessed | 1.82 | disabled chip/input text | note (exempt; recipe inconsistency S4-10) |
| divider / surface · border-soft / surface | 1.47 · 1.25 | chip borders, idle input edges | note (field identification rides a 1px 1.25:1 edge) |
| recessed skeleton / canvas | 1.10 | skeleton on canvas | minor — S4-18 |

**Ring-vs-surface audit (mission item):** ring passes 3:1 on every surface it can appear on — canvas 4.83, surface 5.08, recessed 4.38, ink snackbar 3.27 — but fails against the two dark fills it surrounds (1.00 / 1.20). A single flat ring color mathematically cannot satisfy both (accent.200 passes fills 3.06–3.69 but fails canvas 1.57). Resolution must be geometric (documented 2px gap as part of the indicator + thicker ring) or per-fill (inset `--color-surface` ring on dark fills = 5.08:1) — both use existing tokens.

---

## 6. Repair A check — **satisfied, protect it**

`component-gallery.html:138-162`: one state strip, one button ("Save"), six labeled states — Default / Pressed—hold / Focused / Disabled / Loading—tap / Quiet completion. Pressed = 800 + scale (a state of 700, not a new identity color); Loading = spinner in the icon slot + label change + disabled (double-submit guard verified in `behavior-loading-guard.txt`); Completion = positive.50 tint + check glyph + label change, 800ms, resets (verified `behavior-after-completion.txt`). All six pairwise distinguishable in grayscale. **This is exactly the pattern the repair brief asks for; the repair should extend it (inputs, chips) rather than redesign it.**

## 7. Repair B check — partially satisfied

Operational statuses never masquerade as *filters* (chips are plain text pills; statuses are tags), signs+icons accompany every row amount, and tags are non-interactive spans (no role confusion with buttons). But: the **Badges frame is a permanent wall of 10 colored pills** exposing every status at once (html:305-320) with inconsistent icon coverage, and the **Ready/Moved tint proximity (1.04:1)** is precisely the "near-identical shades for unrelated meanings" failure mode. Resolutions in §10.

## 8. Readability & hierarchy

Type scale matches docs exactly (rem tokens; 12px floor holds inside compositions — only the evidence panel's 10px ramp labels break it, S4-20). Hierarchy in rows/KPI is exemplary: 15/600 title + 12 secondary + signed mono amount; 13/500 label + 24/600 mono + 12 change; 28/700 hero. Bidi is correct (dir="ltr" + `unicode-bidi: isolate` on amounts; RTL snapshots structurally identical). Amount input: mono 24/700, inputmode, live grouping, digits only (D-22 respected — no currency symbols, U+2212 minus). Gaps: single-line ellipsis instead of line-clamp (S4-15), and **no long-Arabic-label demonstration anywhere** — one short string is the entire Arabic proof (S4-06).

## 9. Accessibility checklist

- **Touch targets:** buttons/inputs 48 ✓ · iconbtn 44 ✓ · chips 36+8pad trick = 44 hit ✓ (live-verified) · menu rows 44 ✓ · **segmented 40 ✗, underline tabs 40.8 ✗** (S4-09).
- **Names:** every icon-only control labeled (Add, Search, More, Close, Clear, Add record) ✓ (snapshots).
- **Roles/live:** nav, listbox, dialog(role+aria-modal+labelledby), status regions on snackbar/skeleton ✓; **selection state not exposed** on chips/segmented/nav (S4-03); loading label change unannounced; listbox lacks arrow-key handling (S4-16).
- **Keyboard:** all native controls ✓; Tab trap + Escape + focus-return on overlays ✓ (js:207-220); real input focus ring broken (S4-01).
- **Reduced motion:** system media query + manual toggle ✓; completion keeps text+icon (not color-only) ✓; skeleton pulse removal leaves near-invisible placeholders (S4-18).
- **Text scale:** normal/large only — **130%/200% missing** (S4-05); rem architecture verified to scale correctly at 200% in spot-probes.
- **RTL:** full toggle, logical properties, mirroring demo, RTL thumb placement ✓; long Arabic missing (S4-06).
- **Focus ring visibility:** see §5 — surfaces all pass, dark fills fail.

## 10. Prioritized recommendations (existing ramp steps only)

1. **S4-01 (blocker):** delete `outline: none` from `.input:focus` — one line restores the documented ring on every field.
2. **S4-03:** add `aria-pressed` (chips, segmented), `aria-selected`/radiogroup semantics, `aria-current="page"` (nav) — zero visual change.
3. **S4-02/S4-14:** decide the dark-fill focus strategy: (a) document the 2px offset gap as part of the indicator + 3px ring on filled variants, or (b) inset `--color-surface` ring on accent.600/primary.700 fills (5.08:1, no new color). Do not ship the accent-on-accent case silently.
4. **S4-07:** recolor the menu check stroke to accent.600 (2.88 → 4.51) — one character in the data-URI.
5. **S4-08/S4-04:** restructure Badges into one in-context composition (≤2 semantic families, mandatory icons) + a compact catalog; make the leading icon mandatory on all status tags; document the accent.50/600 dual-role (selection + Ready) and the 1.04 Ready/Moved proximity as an inherited, structure-mitigated risk.
6. **S4-05/S4-06:** add 130%/200% text-scale steps and long-Arabic samples; switch row titles to 2-line clamp.
7. **S4-09:** segmented/tab min-height → `var(--touch-target)`.
8. **S4-12:** Reserved tile → operational.50/600 (terracotta identity-only).
9. S4-10 (unify disabled recipes), S4-15 (line-clamp), S4-16 (aria-busy / menu pattern), S4-18 (divider-based skeleton), S4-19 (drop top-bar shadow), S4-20 (12px floor in evidence panel), S4-21 (safe-area wiring, scoped chip transition), S4-22 (heading hygiene).
10. Optional, taste (S4-13): one sanctioned primary.500 moment (FAB fill) to keep the documented identity hue alive — or re-document 700 as the rendered identity step.

## 11. Explicitly unresolved

- **S4-02/S4-14 (dark-fill focus ring):** no single existing token satisfies both fill-adjacency and surface-adjacency; needs a documented geometric or per-fill decision.
- **S4-04 (Ready vs Moved tints):** cannot be separated within the ramp (accent.100 vs operational.50 is still 1.11:1); resolution is structural (mandatory icons/text), and the inherited conflation must be recorded as accepted-with-mitigation.
- **S4-13 (identity-hue depth):** brand-level judgment (D-01 ripple effect) — legitimately the receiving team's call; both resolutions documented above.
- Real IBM Plex rendering, on-device safe-area/keyboard, and native screen-reader walkthroughs remain declared human work (self-critique.md agrees).

---
*Raw evidence: `contrast-grayscale-results.json`, `sub4-visual-critique.py` (this directory); captures in `audits/captures/`; live probes via agent-browser on the offline file:// render.*
