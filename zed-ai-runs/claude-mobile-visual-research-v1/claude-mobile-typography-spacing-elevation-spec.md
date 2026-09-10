# Claude Mobile App — Typography, Spacing & Elevation Spec

**Artifact:** `claude-mobile-typography-spacing-elevation-spec.md`
**Date:** 2026-09-11 · **Coordinator synthesis (Agents 2 + 4 evidence)**

> **Disclaimer.** Independent research; not affiliated with or endorsed by Anthropic. Official values = public CSS / documentation. Measured values = approximations from 392-px-wide official captures (±2–4 RGB; proportions ±10–15 %). The mobile runtime type scale is UNVERIFIED — the "prototype scale" below is a labeled reconstruction for the research prototype only.

**Legend:** (D) DOCUMENTED · (O) OBSERVED via official capture · (M) MEASURED-approx · (I) INFERRED · (U) UNVERIFIED

---

## 1. Font families

| Family | Weight range | Evidence | Observed usage |
|---|---|---|---|
| Anthropic Sans | 300–800, roman + italic (variable) | D (claude.ai CSS) | working UI text, message body, metadata (O — reads as grotesque sans; runtime family I) |
| Anthropic Serif | 300–800, roman + italic (variable) | D (claude.ai CSS) | new-chat greeting "What are you thinking?" (O); marketing captions (O) |
| Anthropic Mono | 300–800 (variable) | D (claude.ai CSS) | in-app usage U (no capture resolves a code block) |
| JetBrains Mono | 400 | D (claude.ai CSS) | web/code contexts; mobile U |
| Noto Sans | 400/500/600 | D (claude.ai CSS) | CJK fallback on claude.ai; mobile U |
| Tiempos Text | — | D (anthropic.com CSS) | anthropic.com serif; not observed in app captures |

Fallback stacks documented in CSS: Helvetica Neue / Arial / sans-serif; `monospace`. Dyslexic-friendly font option documented as a product setting (D, article 8887527 — rendering U).
**Runtime verdict:** mobile font family = `I` (Anthropic Sans-family); no official statement ties the app binary to these families. Any derivative must label font rendering as approximate.

## 2. Type scale (reconstruction — U as official values)

No official mobile type scale exists. Evidence anchors: text hierarchy is tonal (ink → gray-750 → gray-600) more than size-based (O); titles bold, subtitles gray, body ink, captions/timestamps tertiary (O). The research prototype uses this labeled scale (base 16 px at 360 dp-class width):

| Role | Size / line-height | Weight | Color tier | Basis |
|---|---|---|---|---|
| Greeting (serif display) | ~28–32 / 1.2 | 400–500 serif | ink | O (capture 09 proportion) — size M-approx |
| Card title | ~16–17 / 1.35 | 600 | ink | O + M proportion |
| Message body | ~16 / 1.5 | 400 | ink | O; 1.5 line-height I (readability convention) |
| Metadata / subtitle | ~13–14 / 1.35 | 400 | gray-750/600 | O |
| Caption / timestamp | ~12–13 / 1.3 | 400 | gray-600 | O |
| Placeholder | ~15–16 | 400 | gray-400/500 family | O (gray sans placeholder) |
| Badge / chip text | ~11–12 | 500 | contextual | O |

Letter spacing: no evidence of tracking beyond normal (O reads default); U officially. Dynamic Type / system text scaling on iOS/Android: U (no documentation found) — the prototype therefore provides its own 100 %/130 %/200 % text-scale checks.

## 3. Layout metrics (measured approx at 392 px capture width)

| Metric | Approx value | Evidence |
|---|---|---|
| Screen column inset (cards/lists) | ~14 % per side (x≈56–336 of 392) | M |
| Composer inset | ~10 % per side | M |
| Composer height (pill) | ~48 px | M |
| Top bar height | ~30–36 px | M |
| Card list gap | ~10–14 px | M |
| User-bubble max width | ~65–75 % of column | M |
| Card radius | ~12–20 px (≈16 typical) | M + VLM |
| Bubble radius | ~18–24 px | M + VLM |
| Chip / badge radius | full pill | O |
| Button radius | circular (icon buttons) | O |
| Icon-tile shape | squircle | O |
| Border weight | hairline (<2 px at capture scale; exact U) | M |
| Status dot | ~6 px | M |

## 4. Spacing rhythm

The captures show a compact 4-based rhythm consistent with the measured values (gaps 10–14 px, insets 10–14 %, composer 48 px, chips ~40 px): **4 / 8 / 12 / 16 px** steps with 24 px section breaks (I from measurements; official spacing tokens U — web CSS ships 2–24 px radius tokens and em-based paddings, not transferable to mobile assertions). Density: comfortable-medium — one message pair or 1–2 cards per viewport height with breathing room (O).

## 5. Surfaces & elevation model

Light theme stack (O + M + D):
1. Canvas `#FAF9F5` (background-primary)
2. Tint surfaces `#F5F4ED` / `#F0EEE6` (secondary/tertiary)
3. White cards `#FFFFFF` with soft shadow + hairline border
4. Tinted containers (bubbles/chips `#E8E6DC–#D1CFC5`)

Dark surface stack (M, capture 04):
1. Outer `#262624` (gray-800)
2. Inner card `#3D3D3A` (gray-700) / `#575755` (gray-600–650)
3. White text `≈#FCFCFA`

**Elevation rule:** light theme elevates by whiteness + soft shadow; dark elevates by lightness steps of the same ramp, no shadow (M/O). Shadow parameters (blur/offset/color) U — renders as "soft, subtle" (O).

## 6. Borders & dividers

Border tiers documented: primary `#B0AEA5`, secondary `#D1CFC5`, tertiary `#E8E6DC` (D). Observed usage: hairlines on white cards/buttons (approve-style button = white + thin border — O 07); composer reads borderless (O). Hover doubles border width (D web-side: `calc(var(--border-width--main)*2)`). A distinct divider token: U (borders likely serve).

## 7. Keyboard, safe areas, orientation

- Keyboard: U for avoidance behavior; documented adjacent behavior — in fullscreen connector views "the conversation input remains available" (D 13454812); OS microphone and notification permission prompts documented (D).
- Safe areas: punch-hole displays documented for the Samsung reference devices (D Samsung footnote: "actual viewable area is less due to the rounded corners and/or camera hole"); the app's own inset handling U — see `claude-mobile-device-frame-validation.md` for harness assumptions (labeled UNVERIFIED).
- Orientation: U (no landscape behavior documented); captures are portrait only.

## 8. Prototype usage notes

The research prototype must: use system font stacks approximating the documented families (offline constraint — no webfonts), label typography as INFERRED; implement the measured proportions above as the default; expose 100 %/130 %/200 % text scaling; and treat all values in this spec as study approximations, never official tokens.
