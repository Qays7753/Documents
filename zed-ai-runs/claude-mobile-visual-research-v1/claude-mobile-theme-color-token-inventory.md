# Claude Mobile App — Theme & Color Token Inventory

**Artifact:** `claude-mobile-theme-color-token-inventory.md`
**Date:** 2026-09-11 · **Coordinator synthesis (Agents 2 + 4 evidence)**
**Scope:** role-based colors, theme roles, foreground/surface relationships, evidence, confidence, and contrast notes for the official Claude mobile app.

> **Disclaimer.** Independent research; not affiliated with or endorsed by Anthropic. "Official token" = value read from publicly inspectable official CSS (claude.ai / anthropic.com) or stated in official documentation. "Sampled" = MEASURED approximation from rasterized official App Store captures (±2–4 RGB) — **never** an official token. Confidence: **High** = official token / multi-source · **Medium** = single official source or well-corroborated sample · **Low** = inference or unresolved.

---

## 1. Official neutral ramp (claude.ai public CSS — `--swatch--gray-*`)

DOCUMENTED (T1). The entire structural system is this one warm ramp; anthropic.com aliases the same values as ivory / slate / cloud.

| Step | Hex | anthropic.com alias | Typical role (documented mapping) |
|---|---|---|---|
| gray-000 | `#FFFFFF` | — | white cards, sheets, dots-on-track |
| gray-050 | `#FAF9F5` | ivory-light | **background-primary (app canvas)** |
| gray-100 | `#F5F4ED` | — | background-secondary |
| gray-150 | `#F0EEE6` | ivory-medium | background-tertiary; switch track |
| gray-200 | `#E8E6DC` | ivory-dark | border-tertiary; secondary-button fill |
| gray-250 | `#DEDCD1` | — | pictogram-accent; user-bubble family (sampled ≈) |
| gray-300 | `#D1CFC5` | cloud-light | border-secondary |
| gray-350 | `#C2C0B6` | — | — |
| gray-400 | `#B0AEA5` | cloud-medium | border-primary |
| gray-450 | `#9C9A92` | — | — |
| gray-500 | `#87867F` | cloud-dark | disabled/icons-on-white family |
| gray-550 | `#73726C` | — | — |
| gray-600 | `#5E5D59` | slate-light | foreground-tertiary |
| gray-650 | `#4D4C48` | — | secondary-button text |
| gray-700 | `#3D3D3A` | slate-medium | dark-surface inner layer (sampled ≈) |
| gray-750 | `#30302E` | — | foreground-secondary |
| gray-800 | `#262624` | — | dark-surface outer layer (sampled =) |
| gray-850 | `#1F1E1D` | — | button-primary hover |
| gray-900 | `#1A1918` | — | — |
| gray-950 | `#141413` | slate-dark | **foreground-primary (ink)**; button-primary fill |
| gray-1000 | `#000000` | — | — |

Warmth mechanism: at every light step red ≥ green > blue (e.g. `#F0EEE6` = 240/238/230), giving the cream cast; the dark end keeps the same warm hue.

## 2. Accent & semantic swatches (official CSS)

DOCUMENTED (T1): clay `#D97757` (text-accent, heroes-accent, selection at 50 % alpha) · clay-interactive `#C96442` (button-brand fill) · error `#B53333` · switch-active `#2C84DB`. Secondary hues (used sparingly, content/status domains): olive `#788C5D`, cactus `#BCD1CA`, sky `#6A9BCC`, heather `#CBCADB`, fig `#C46686`, coral `#EBCECE`, peach `#EBC9B7`, oat `#E3DACC`, mineral `#629987`, plum `#827DBD`; anthropic.com adds kraft `#D4A27F`, manilla `#EBDBBC`, and its own site accent `#C6613F` (website token — **not** an app-UI value). Alpha-tint layering: ivory-faded-10/20 and slate-faded-10/20 (10 %/20 % alpha tints of `#FAF9F5`/`#141413`).

## 3. Role-based inventory (the mobile surface table)

"Value" column: **bold** = official token (DOCUMENTED) · *italic* = MEASURED approximation from official captures · plain = INFERRED. Contrast = WCAG 2.x ratio computed by the coordinator (`scripts/contrast-check.py`).

| Mobile surface | Role | Verified value or approximation | Foreground/surface relationship | Where used | Evidence type | Confidence |
|---|---|---|---|---|---|---|
| App canvas | background-primary | **#FAF9F5** (= sampled *#faf9f5*) | ink 17.50:1 (AAA) | chat bg, list bg, all light screens | DOCUMENTED + MEASURED | High |
| Recessed surface | background-secondary | **#F5F4ED** | ink 16.72:1 | subtle inset zones | DOCUMENTED | High |
| Elevated tint surface | background-tertiary | **#F0EEE6** | ink ~15:1 | chips, switch track | DOCUMENTED | High |
| Card / sheet | elevated surface | **#FFFFFF** (sampled *#ffffff/#fcfcfb*) | ink 18.43:1 | artifact cards, task cards, composer pill | DOCUMENTED + MEASURED | High |
| User message bubble | container | **gray-250/300 #DEDCD1–#D1CFC5** (sampled *#d5d5d1–#d7d6cf*) | ink 12.5–13.4:1 | user turns in chat | MEASURED (ramp corroborated) | Medium |
| Chip / tint fill | interactive tint | **#E8E6DC** (gray-200) | ink 14.73:1 | attachment-zone fills, secondary buttons | DOCUMENTED | High |
| Dark immersive surface (outer) | artifact overlay | **#262624** (sampled *= gray-800) | white 14.76:1 | flashcards/artifact fullscreen | DOCUMENTED + MEASURED | High |
| Dark surface (inner card) | elevated-on-dark | **#3D3D3A** ≈ sampled *#3d3d3a/#575755* | white 10.6:1 / 7.05:1 | inner cards on dark | MEASURED (ramp match) | Medium |
| Primary text | foreground-primary | **#141413** (sampled AA-thinned *#2d2d2b*) | — | Claude replies, titles, body | DOCUMENTED + MEASURED | High |
| Secondary text | foreground-secondary | **#30302E** | 12.55:1 on canvas | subtitles, metadata | DOCUMENTED | High |
| Tertiary text | foreground-tertiary | **#5E5D59** | 6.26:1 on canvas (AA) | captions, timestamps | DOCUMENTED | High |
| Placeholder / disabled text | muted | **gray-500/400 #87867F–#B0AEA5** | 3.47:1 / 2.11:1 (non-AA as text) | composer placeholder, disabled | DOCUMENTED (role) + INFERRED (step) | Low–Medium |
| Brand accent (clay) | primary action fill | **#D97757** (sampled *#d9795a*) | white glyph 3.12:1 (UI-component pass) | send button, "+" button, spark mark | DOCUMENTED + MEASURED | High |
| Interactive accent | pressed/hover fill | **#C96442** (button-brand) | off-white 3.70:1 | pressed/hover brand buttons | DOCUMENTED | High |
| Ink button | alt primary action | **#141413** fill, off-white text | 18.43:1 | web-side button-primary; mobile occurrence UNVERIFIED | DOCUMENTED (CSS) | Medium |
| Secondary button | secondary action | **#E8E6DC** fill, **#4D4C48** text | 4.9:1 | hairline-adjacent actions | DOCUMENTED (CSS) | Medium |
| Tertiary button | ghost action | transparent, **#5E5D59** text | 6.26:1 | borderless text actions | DOCUMENTED (CSS) | Medium |
| "Approve"-style button (capture) | confirm action | *white fill + ink text + hairline border* | 18.43:1 | task-card confirm | MEASURED-approx | Medium |
| Focus indication | focus ring | UNVERIFIED value | — | — | UNVERIFIED | Low |
| Selection | selection | **clay #D97757 @ 50 % alpha** (documented) / *darker chip tint* (sampled) | — | selected filter chip, text selection | DOCUMENTED + MEASURED | Medium |
| Positive / success | semantic | green family: *green check + "Connected" text* (sampled hue); ramp has mineral #629987 | — | online dot, completed check | MEASURED-approx + DOCUMENTED (existence) | Medium |
| Negative / error | semantic | **#B53333** | 5.72:1 on canvas (AA text) | error messages | DOCUMENTED | High |
| Warning | semantic | UNVERIFIED dedicated token | — | limit warnings are text-only strings | UNVERIFIED | Low |
| Information / status | semantic | *bright blue #1490ff–#2e9cff* (likely iOS system blue) · **#2C84DB** switch-active | 3.1–3.3:1 non-text | status dots, switches | MEASURED + DOCUMENTED | Medium |
| Content-accent violet | artifact content | *#6e6b96* (ANSWER pill) | white text 4.99:1 | flashcard content pills | MEASURED-approx | Medium |
| Custom cream icon bg | illustration accent | *#f3d49a* | — | squircle icon tiles | MEASURED-approx | Low |
| Border (primary) | structural | **#B0AEA5** (gray-400) | decorative | strong dividers | DOCUMENTED | High |
| Border (secondary/tertiary) | structural | **#D1CFC5 / #E8E6DC** | decorative | card/button hairlines | DOCUMENTED + MEASURED (hairline range) | High |
| Divider | separator | UNVERIFIED distinct token — likely border tier | — | — | INFERRED | Low |
| Message/content/code surfaces | content containers | user bubble (above); code block styling UNVERIFIED (not visible in captures; dark-surface values are the only measured darks) | — | — | UNVERIFIED | Low |
| Light theme canvas ↔ Dark equivalent | theme pair | Light canvas **#FAF9F5**; full dark canvas UNVERIFIED; dark surfaces measured *#262624/#3D3D3A/#575755* = gray-800/700/600–650 → same-ramp inversion | — | — | DOCUMENTED + MEASURED | Medium (dark canvas: Low) |

## 4. Contrast notes (computed, `scripts/contrast-check.py`)

Passing: ink/canvas 17.50:1 (AAA); ink/card 18.43:1 (AAA); secondary text 12.55:1 (AAA); tertiary text 6.26:1 (AA); ink on bubbles/chips 12.5–14.7:1 (AAA); error `#B53333` on canvas 5.72:1 (AA text); white on dark surfaces 7.05–14.76:1 (AAA–AA); white on violet ANSWER pill 4.99:1 (AA).
Bounded: white on clay `#D97757` 3.12:1 — passes WCAG 1.4.11 (3:1) for UI components/graphical objects; the send button is an icon-only control, so this is compliant usage, but clay must not carry small text. Off-white on clay-interactive 3.70:1 — large-text/UI only. Clay as *text* on cream 2.96:1 — fails AA; the system accordingly uses clay as fills/marks, with the documented text-accent role belonging to web hero/marketing contexts. gray-400 on canvas 2.11:1 — decorative border only, never text. Placeholder gray family (3.47:1 and below) — placeholders sit outside AA body-text expectations; disabled states are exempt.
Status blue dots 3.08–3.25:1 non-text — at/above the 3:1 UI-component minimum; sky `#6A9BCC` 2.78:1 fails non-text and is not used for UI indicators in any capture.

## 5. Light/dark theme architecture

DOCUMENTED: Color mode setting exists product-wide (Light / Match System / Dark — support article 8887527; mobile settings location UNVERIFIED). MEASURED: the only dark surfaces inside the app visible in captures (fullscreen artifact/flashcard surface) reuse the same ramp's dark end — `#262624` outer, `#3D3D3A`/`#575755` inner, white `≈#FCFCFA` text, muted violet `#6e6b96` content pill. INFERRED (labeled as such in any derivative): full dark theme likely remaps background-primary toward gray-800/850 with foregrounds toward gray-050/100 — exactly the inversion pattern documented on anthropic.com dark sections ("dark sections remap background-primary to gray-800/850/950 — same ramp inverted"). The full mobile dark canvas/composer/bubble values remain UNVERIFIED and must not be asserted as tokens.

## 6. Distribution rules — how the system avoids accent inflation

1. **One clay control per viewport** (OBSERVED in all captures: send button OR "+" button, never both filled on the same screen — the chat top-bar "+" reads neutral/outline in chat captures while the list-surface "+" is clay-filled).
2. **The ramp carries all structure**: backgrounds, bubbles, chips, borders, and four text tiers are all neutral; hierarchy is tonal, not chromatic.
3. **Semantic hues are small and load-bearing**: blue = status/selection only (dots, switch); green = success/online only; violet = artifact content only; red = errors only, and muted (`#B53333`, not saturated).
4. **Filled brand surfaces are rare and small** (circular buttons, spark marks); large surfaces stay neutral — white sheets over cream canvas.
5. **Interactive states stay within the family**: pressed/hover deepens clay (`#D97757` → `#C96442`); selection is clay at 50 % alpha over the canvas; borders double on hover (documented web-side: `calc(var(--border-width--main)*2)`).

## 7. Sampling provenance

All sampled values come from the nine official iPhone App Store captures (392×696, `raw/shots/`, VLM cross-checked grid sampling via `scripts/agent2-sample-colors.py` and passes 2–3) and the Play hero tile. Photographic captures (Voice_Mode, Tools, Dispatch) and Apple's marketing canvases were excluded from app-UI token inference. Sampled values are corroboration for official tokens, never a substitute: e.g. canvas sampled `#faf9f5` = exact gray-050; send button sampled `#d9795a` ≈ clay `#D97757`.
