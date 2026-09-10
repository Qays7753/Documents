# Claude Mobile App — Composition Patterns (Phone-First)

**Artifact:** `claude-mobile-composition-patterns.md`
**Date:** 2026-09-11 · **Coordinator synthesis (Agents 2 + 4 evidence)**

> **Disclaimer.** Independent research; not affiliated with or endorsed by Anthropic. Patterns are derived only from official captures and official documentation; no product logic or domain workflows are included.

**Legend:** (D) DOCUMENTED · (O) OBSERVED via official capture · (M) MEASURED-approx · (I) INFERRED · (U) UNVERIFIED

---

## 1. The one-accent rule (strongest action)

In every analyzed capture, exactly **one clay-filled control** occupies the viewport: the composer send button in chat screens, or the top-right "+" on the list surface (O; sampled `#d9795a` ≈ clay `#D97757` — M). The strongest action is therefore always unambiguous without labels or size inflation. Derivative rule: if a viewport needs a second accent, the composition is wrong — demote one control to neutral/hairline.

## 2. Filled-surface budget

A chat viewport contains at most 1–3 white cards (artifact/attachment) floating on the cream canvas (O; quantized color census of capture 05: white family ≈ 20 %, canvas ≈ 18 %, everything else text/tints). List surfaces raise card density but keep the card:white-to-canvas ratio ~1:1.3 (capture 07 census: canvas 31 %, white 26 %, ink surround 32 % — the surround is Apple's marketing frame, not app UI). The canvas itself is never pure white (M `#faf9f5`) — cards earn elevation by being *whiter than the canvas*, not by heavy shadow.

## 3. Secondary-action subordination

Secondary actions demote through material, not size: hairline-bordered white buttons ("Approve" — O), borderless tertiary text buttons (D CSS role), neutral icon buttons, tint chips. The documented button ladder (brand clay → ink → secondary tint → tertiary transparent — D CSS) is a *material* hierarchy.

## 4. Structural bands (portrait phone)

From the captures, the chat screen is a three-band composition (O/M):
1. **Top band** (~30–36 px + status area): transparent top bar — identity (menu) left, utilities ("+", "⋯") right; never colored.
2. **Content band** (flexible, scrolls): single column, ~10–14 % side insets, conversation rhythm or card list.
3. **Bottom band** (composer + system inset): the white pill composer is the visual anchor — the second-strongest element after content, and the only clay element.
Overlays (dark artifact surface) replace bands 1–3 entirely with the immersion pattern (§7). The keyboard does not introduce a fourth band — the composer adapts (documented only as input availability; visuals U).

## 5. Whitespace vs information density

The system is comfortable-medium density: ~1 message pair or 1–2 cards per viewport height (O); list gaps 10–14 px; card internal padding reads generous relative to text size (O proportion). Density is added by *stacking cards*, not by shrinking type or margins: task lists keep the same card anatomy as artifact cards (O).

## 6. Alignment grid

A single-column grid with paired insets: content column ≈86–88 % of width; composer inset ≈10 % per side — slightly wider than card lists (M). Everything left-aligns to the column start (titles, bodies, chips); timestamps right-align within task cards (O). No multi-column layouts observed; horizontal scrolling appears only *inside* cards (restaurant sub-cards — O).

## 7. Pattern library

**P1 — Landing/greeting (O, capture 09):** empty column, centered serif greeting + spark mark, composer at bottom with hidden send arrow. Emotion-first, task-light.
**P2 — Conversation (O, captures 01/05/08):** greeting scrolls away; alternating rhythm of gray user bubbles and bare ink responses; white cards interrupt the rhythm as content events; attachment chips stack above the composer.
**P3 — Task list (O, capture 07):** filter chip row directly under the top bar; white task cards with icon/title/path/timestamp rows; status dots inline; expanded card reveals context + one full-width confirm action. (Task-list grammar; its identity as a specific product surface is unconfirmed.)
**P4 — Immersive dark (O/M, capture 04):** full-bleed dark surface with ✕/⋯ header; content centered; lightness-stepped inner cards; white/pill status elements; one hue accent (violet) allowed inside content.
**P5 — Mode-select in place (D):** the composer itself hosts mode selection ("Cowork" bottom-left of message box; model menu next to send) — mode switching without navigation.
**P6 — Overlay dialogs (D):** confirmation and permission dialogs gate destructive/agent actions; gating dialogs persist until answered.

## 8. Separation of concerns (color semantics)

Four visual channels never mix (O + M + D):
- **Identity** — brand marks (spark), serif greeting, clay as *brand voice*.
- **Interaction** — clay-filled controls (one per viewport), white pills, hairline borders.
- **Selection** — darker neutral tints (chips), clay@50 % documented for text selection.
- **Semantic status** — blue dots (active), green (online/success), muted red `#B53333` (errors), violet (artifact content only).
A control carries at most one channel; e.g., the send button is interaction-only, status dots are status-only (O).

## 9. Message/content rhythm

Conversation rhythm is asymmetry-based: container (user) vs bare text (Claude) alternate with consistent vertical gaps (~10–14 px family — M); cards insert as larger rhythm events with their own internal padding; the thinking section inserts *above* responses as a meta-event (D). Horizontal rhythm: user bubble max-width 65–75 % leaves an L-shaped silence that the response's full measure fills (M) — the composition encodes turn-taking.

## 10. Cross-size behavior (prototype-facing summary)

Composition is width-relative (insets in %, radii in px clamped): at 320–430 CSS px the same single column persists; the composer pill and card radii stay constant; text scale changes flow height, not column structure (prototype checks). Orientation and split-view behavior: U — portrait-only patterns are the studied reality.
