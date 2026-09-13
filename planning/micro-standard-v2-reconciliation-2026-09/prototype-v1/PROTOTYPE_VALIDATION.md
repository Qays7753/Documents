# Prototype v1 — Validation Record

**Run:** `run-20260914-msv2-reconciliation-01` · validated 2026-09-14 (Asia/Amman).
**Environment:** headless Chromium via Playwright 1.62.1 (local), viewport 390×844 for behavior checks; width matrix 320/360/390/430; text-scale emulation at the token level (the `--text-*` size tokens scaled 100/130/200% — a disclosed method); RTL (the prototype is Arabic-first by design; LTR is covered by the Standard gallery's own direction control); reduced motion via the control and the emulated system preference.

## Static checks (gate)

- **Anti-contamination vocabulary gate** — the three prototype files contain none of: Micro product vocabulary («مشروعي الآن», «بانتظار قرار», «غير محدد بعد», QuickAction, G5), gallery demo tag words (Received / In progress / Moved / Returned / Ready / Sent / Closed / Posted / Failed / Pending / Unknown / Reviewed / Finalize), route paths, or a standalone Micro FAB label «سجّل» (the Standard's own documented «سجّله» example is used deliberately, per the recorded CF-4 decision).
- **Palette gate** — only the 18 approved hex values, the two disclosed alpha derivatives (scrim `rgba(20,20,19,0.45)`, translucent header `rgba(250,249,245,0.86)`), and the recorded shadow tone `rgba(60,50,40,x)` appear. No other color exists in the artifact.
- **Token embed** — the `:root` token block in `prototype.css` carries the updated Standard's values verbatim (the package's `design-tokens.css` is unchanged in this run).

## Behavioral checks (all PASS)

1. **Action classes (computed styles)** — text-bearing Create = Clay `rgb(217,119,87)` + ink `rgb(20,20,19)`; icon-only Create/FAB = Clay + white icon; ordinary Save = `rgb(245,244,237)` + ink with the `#C96442` pressed-edge rule; high-consequence commit = `rgb(20,20,19)` + white; FAB is 56px in its own gutter (measured ≥16px above the nav).
2. **Knowledge/type-floor rebindings** — knowledge words in ink, marks on neutral ground; tag words in `rgb(77,76,72)`; success/status markers only on the white Surface; row amounts in ink 15px mono (negative keeps text-safe error ink); labels 13px; non-financial metadata 12px; hero 28; amount input 24 mono.
3. **AUX behaviors** — deep route hides navigation; keyboard-open hides topbar/nav/FAB while the content and the focused field remain visible; safe-area clearance present (`max(6px, env(safe-area-inset-bottom))`); scroll-border appears after real scroll; context-label suppression when it duplicates the heading; route transition = 200ms `--motion-normal` fade with no layout animation.
4. **Save lifecycle** — `aria-busy` during loading; duplicate-submit blocked; quiet completion = check + past-tense word + `role="status"` inline region; Snackbar appears only after explicit opt-in (default OFF) and holds 5000ms.
5. **Overlays** — sheet opens above the shared scrim `rgba(20,20,19,0.45)` (z 300 > 250) with focus moved inside; Escape closes and releases the scrim; dialog provides the independent confirmation path; in-flow `<details>` stays in flow.
6. **Icons** — 4 directional roles mirrored by the adapter (`transform: scaleX(-1)`), 4 static roles unmoved, flags rendered.
7. **Geometry** — no document-level horizontal overflow and no visible element crossing its composition across 4 widths × 3 text scales × 6 scenes (72 combinations; rect-based element checks with designed internal scrollers excluded; document `scrollWidth` as the hard gate).
8. **Reduced motion** — transitions collapse to 1e-05s under both the control and the emulated system preference.
9. **Bidi/digits** — English digits render in `dir="ltr"` bidi-isolated slots inside the RTL composition.
10. **Truth labels** — visible in the demo chrome and inside the frame.
11. **Console** — zero console/page errors across the full run.

Evidence captures: `evidence/scene-s1..s6.png` (full-page, 390px, reduced motion for stable captures).

## Honest limitations (explicitly not claimed)

- **Local headless Chromium only** — no physical-device testing; no screen-reader/assistive-technology testing (`aria-*` usage was checked in markup only).
- **Font substitution** — the validation machine has no IBM Plex Arabic/Mono; system fallback fonts rendered the Arabic text. Layout was validated with the fallback metrics; final typography should be reviewed on a machine with the declared fonts.
- **Text-scale emulation** — 130/200% were emulated by scaling the `--text-*` size tokens (the contract's own scale), not by a browser-level text-only zoom; the two are equivalent for a token-driven system but the method is disclosed rather than implied.
- **Keyboard and safe-area are simulations** — `data-keyboard="open"` simulates the software-keyboard state (the AUX contract's behavior), and `env(safe-area-inset-bottom)` is 0 on desktop viewports (the rule is present and computed; a notched device would show the inset).
- **The prototype is evidence only** — it is not a source of product copy, routes, data, or financial meaning, and it is excluded from the Standard package's Final Copy acceptance.
