# Claude Mobile Visual Research — Device Frame Validation (Samsung S25 Series Harness)

**Artifact:** `claude-mobile-device-frame-validation.md`
**Date:** 2026-09-11 · **Coordinator synthesis (Agent 3 specs + Agent 4 boundary rules)**
**Scope:** the device-frame presets of the research prototype `claude-mobile-visual-research-prototype.html` — Samsung Galaxy S25 / S25+ / S25 Ultra frame proportions, inner CSS viewport presets, safe-area assumptions, overflow checks, and hardware-verification limits.

> **Disclaimer.** Independent research artifact. Samsung specifications are used only for outer-frame proportions, display-size/aspect reference, and device naming. Browser HTML does **not** reproduce physical hardware pixels, device pixel ratio, One UI safe areas, touch latency, haptics, display refresh, or font metrics. Every such behavior is labeled UNVERIFIED in the prototype.

---

## 1. Official Samsung inputs (T1 unless noted)

| Value | Galaxy S25 | Galaxy S25+ | Galaxy S25 Ultra |
|---|---|---|---|
| Display (full rectangle) | 6.2" / 156.4 mm | 6.7" | 6.9" / 174.2 mm |
| Display (rounded corners) | 6.0" / 152.3 mm | 6.5" | 6.8" / 172.2 mm |
| Resolution | 2340 × 1080 (FHD+) | **QHD+ class (official); 3120 × 1440 = T3-agreed approximate** | 3120 × 1440 (QHD+) |
| Aspect ratio | 19.5:9 — COMPUTED from official px (INFERRED; Samsung prints no ratio) | 19.5:9 — computed from T3 px (INFERRED) | 19.5:9 — computed (INFERRED) |
| Physical H × W × D | 146.9 × 70.5 × 7.2 mm | 158.4 × 75.8 × 7.3 mm | 162.8 × 77.6 × 8.2 mm |
| Weight | 162 g | 190 g | 218 g |
| Screen tech | Dynamic AMOLED 2X, 120 Hz (1–120) | same | same |
| Front camera | 12 MP F2.2, punch-hole (footnoted) | 12 MP F2.2, FOV 80° | 12 MP F2.2 (+ autofocus) |
| Announced / released | Jan 22, 2025 (US) / Feb 7, 2025 (snippet-level + T3 corroboration) | same | same |
| Frame character | Armour Aluminum, more-rounded corners | Armour Aluminum | Titanium, boxier corners, S Pen |

Sources: samsung.com/uk + samsung.com/fr spec pages (S25, S25 Ultra — dual-region identical); news.samsung.com global press release (all three); samsungmobilepress.com S25+ snippet. S25+ exact px is the only T3-dependent number and is labeled as such everywhere it appears.

## 2. Frame presets (harness implementation)

The outer frame is drawn from **physical-dimension ratios** (not pixel ratios), with a cosmetic bezel; the inner viewport uses the **screen aspect ratio**. Both are reported by the harness.

| Preset | Outer frame aspect (H:W from mm) | Inner viewport aspect (screen) | Cosmetic frame notes |
|---|---|---|---|
| Galaxy S25 | 146.9 / 70.5 ≈ **2.084** | 2340/1080 = **2.167** (19.5:9) | rounded corners, center punch-hole dot, right-side button nubs |
| Galaxy S25+ | 158.4 / 75.8 ≈ **2.090** | 3120/1440 = **2.167** (T3-agreed px) | as S25, slightly larger at equal scale |
| Galaxy S25 Ultra | 162.8 / 77.6 ≈ **2.098** | 3120/1440 = **2.167** | boxier corners (larger corner radius on frame, squarer silhouette), S Pen silhouette NOT drawn (avoid implying hardware fidelity) |

Frame scaling: the harness scales the frame to fit the stage while preserving the outer aspect; a caption reports device name, official display inches, resolution (+ S25+ T3 caveat), and the aspect-ratio provenance (computed/INFERRED).

## 3. Inner CSS viewport presets

The studied application viewport is an independent CSS box, deliberately decoupled from hardware claims. Presets: **320, 360, 390, 430 CSS px** width (plus the Samsung frame presets, which default to 360 CSS px width). Height = width × 2.167 for Samsung presets (screen aspect) — reported as a CSS box, not a hardware claim. The harness reports both values at all times, e.g. `frame: Galaxy S25 Ultra · outer ratio 2.098 · viewport: 360 × 780 CSS px`.

No DPR claim is made anywhere; CSS pixels are declared as browser units.

## 4. Safe-area assumptions (all UNVERIFIED, visualized as assumptions)

- Punch-hole: documented to exist (Samsung footnote); drawn as a small dot top-center in the status overlay. Exact One UI status-bar height: UNVERIFIED → the harness draws a **status-area strip with an "assumed inset" label** (default ~28 CSS px, adjustable toggle).
- Bottom gesture/navigation area: One UI exact inset UNVERIFIED → drawn as a **gesture strip with "assumed inset" label** (default ~20 CSS px, toggle).
- The studied UI is required to remain fully operable with the safe-area overlays on or off (checks §5). Rounded-corner clipping is cosmetic only.
- Apple-device specifics are out of scope for this harness (the reference devices are the three Samsung presets).

## 5. Harness check panel (validation checks)

The prototype's QA harness (external to the studied UI) exposes live checks, each reporting pass/fail/assumption:

1. **Portrait orientation** — Samsung presets are portrait-only (landscape is UNVERIFIED for the app; harness locks portrait and says so).
2. **Top status area** — visible strip + assumption label.
3. **Bottom gesture/navigation area** — visible strip + assumption label.
4. **Safe-area padding** — toggle; verifies content clears both strips at 320/360/390/430 widths.
5. **Keyboard expansion** — simulated keyboard panel over the composer; verifies composer visibility and scroll ownership (page scroll vs conversation scroll).
6. **Scroll ownership** — the conversation list scrolls; composer/top bar stay fixed; no body-level scroll inside the viewport.
7. **Overflow** — automated horizontal-overflow detection per viewport width × text-scale combination (scrollWidth vs clientWidth of the app root), reported in the check panel.
8. **Text scale** — 100 % / 130 % / 200 % applied to the studied UI root (rem-based); checks that no fixed-height clipping occurs (overflow check re-runs).
9. **Motion mode** — normal vs reduced; reduced disables non-essential transitions (all motion is a research stand-in — app motion is UNVERIFIED).
10. **Theme** — light/dark toggle; dark values beyond the measured dark-artifact surface are labeled INFERRED in the evidence panel.
11. **Offline self-containment** — no network requests (harness greps the source for external URLs at build time; runtime loads from `file://`).

## 6. Hardware-verification limits (explicit non-claims)

The harness and prototype state that browser HTML **cannot verify or reproduce**: physical pixel density or DPR (Samsung devices run ~500 ppi class panels at One UI-configured densities); One UI system UI (status icons, gesture bar behavior, notification shade); 120 Hz adaptive refresh; touch sampling/latency; haptics; display color management; Samsung font metrics (One UI Sans etc.); exact dp/canonical viewport sizes as configured by One UI (documented nowhere in the inspected official pages). Inner viewport values are CSS boxes chosen for study, and are labeled as such. The only hardware facts used are §1's official dimensions/display figures, with their documented provenance and the S25+ px caveat.

## 7. Validation protocol executed for this study

For each of the three Samsung presets: default 360 px viewport → run checks 1–7 → switch widths 320/390/430 → re-run overflow/scroll checks → apply text scales 130 % and 200 % → re-run overflow → toggle keyboard sim → toggle safe-area overlays → toggle motion modes → verify frame caption values against §1. Results recorded by Agent 4 in `claude-mobile-prototype-qa.md` (independent review; no repair).
