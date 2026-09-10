# Claude Mobile App — Visual System Research Report

**Artifact:** `claude-mobile-visual-research-report.md`
**Date:** 2026-09-11 · **Coordinator synthesis of Agents 1–4 evidence**
**Subject:** the official **Claude mobile app by Anthropic** (iOS and Android). The phone UI is the primary source of truth. Browser, desktop, terminal, and IDE interfaces are referenced only where official documentation explicitly connects them to the mobile app.

> **Disclaimer.** This is an independent visual/UI-UX research study. It is not affiliated with, endorsed by, or produced by Anthropic. It contains no proprietary logos or private assets. Sampled colors are approximations of rasterized official marketing captures and are never official tokens. Official token values cited here come from publicly inspectable official CSS and official documentation only.

**Evidence labels:** `OBSERVED` (directly visible in an official capture) · `MEASURED` (calculated from inspectable pixels/CSS/explicit values) · `DOCUMENTED` (stated in an official public source) · `INFERRED` (reasoned from evidence) · `UNVERIFIED` (not provable with available evidence).
**Tiers:** T1 official (anthropic.com, claude.com, claude.ai, support.claude.com, code.claude.com, docs.claude.com, official store listings, official public CSS) · T2 official captures (App Store / Play Store marketing screenshots) · T3 secondary (triangulation only).

---

## 1. Purpose, scope & method

This report studies only the mobile visual system and mobile user experience of the official Claude apps: theme and visual direction; palette and color roles; surfaces, borders, shadows; typography and spacing; components from composer to sheets; states from default to error/retry; motion and accessibility where documented; and behavior across phone sizes and text scales where testable. It deliberately does not analyze model intelligence, benchmarks, pricing, or strategy, and does not compare Claude with any other product.

The method combined five coordinated evidence passes: (1) interface research across official help-center articles, store listings, and Claude Code mobile documentation; (2) visual-system extraction from the publicly inspectable official CSS of claude.ai and anthropic.com; (3) VLM-assisted structural reading plus PIL pixel sampling of all nine official iPhone App Store captures (392×696) and the Play Store hero tile; (4) a source register with dual-region verification of Samsung S25-series hardware specifications for the device-frame harness; and (5) an independent verification pass that re-fetched key sources, re-ran measurements, and rejected unsupported assumptions (notably: user-bubble alignment, which measured pixel margins left near-symmetric — 52/63 px and 54/59 px — and is therefore classified `UNVERIFIED`, not "left-aligned").

Direct app observation was not available in this environment (no authorized device/session). Everything below is therefore grounded in official documentation, official public CSS, and official marketing captures, each labeled. Store-listing metadata is volatile and is cited "as of September 2026".

---

## 2. App identity & platforms

| Fact | Value | Evidence | Source |
|---|---|---|---|
| App name | "Claude by Anthropic" | DOCUMENTED | App Store + Play listings |
| Developer / seller | Anthropic PBC | DOCUMENTED | iTunes lookup API, both stores |
| iOS listing | apps.apple.com/us/app/claude-by-anthropic/id6473753684 | DOCUMENTED | listing + anthropic.com/ios redirect |
| Android package | com.anthropic.claude | DOCUMENTED | Play listing |
| iOS first release | 2024-05-01 | DOCUMENTED | iTunes API releaseDate |
| Android launch | 2024-07-16 | DOCUMENTED | claude.com/blog/android-app |
| OS minimums | iOS 18.0+ / iPadOS 18.0+ · Android 8.0+ | DOCUMENTED | support articles 9266462, 9612887 |
| iPad | same iOS app, no separate build | DOCUMENTED | code.claude.com/docs/en/mobile |
| Current version | 1.260909.19 (as of Sept 2026; listing data volatile) | DOCUMENTED | iTunes API (re-fetch drifted — see §12) |
| Cross-platform sync | conversations sync across phone/desktop/web | DOCUMENTED | Android announcement, claude.com/download |

The app is a chat-first client with an integrated client surface for Claude Code sessions ("Code" tab — §10) and a Cowork mode selectable in the message box ("select 'Cowork' in the bottom left corner" — support article 15520349). This report covers each surface separately (§9 Chat, §10 Code).

---

## 3. Mobile visual concept — the first-glance experience

Every judgment below is tied to the visible mechanism that produces it.

- **Warm before anything else.** The canvas is not white but cream — `#FAF9F5` measured exactly in captures 05/07 and documented as `--swatch--gray-050` in claude.ai's public CSS. The whole light ramp carries a warm yellow-beige cast (e.g. gray-150 `#F0EEE6` = RGB 240/238/230: red ≥ green > blue). The emotional register is paper and ink, not glass and chrome. (`MEASURED` + `DOCUMENTED`)
- **Quiet, low-energy color.** Large surfaces are neutral; chroma appears only in small controls. In every analyzed capture at most **one clay-colored control fills the viewport** (the composer send button in chat captures; the "+" button in the list-surface capture) — measured clay cluster `#d9795a` ≈ official `#D97757`. (`OBSERVED` + `MEASURED`)
- **Soft geometry.** No sharp corners anywhere in the captures: pill composer, circular buttons, ~12–20 px card radii at 392 px capture width, squircle icon tiles, pill badges/chips. (`OBSERVED`)
- **Editorial typography moment.** The new-chat landing centers a serif heading — "What are you thinking?" — with a terracotta spark mark above the composer (capture 09); the brand's public CSS ships both "Anthropic Serif" and "Anthropic Sans" variable families (300–800). The serif is the personality; the sans is the workhorse. (`OBSERVED` + `DOCUMENTED`)
- **Asymmetric conversation rhythm.** User turns render as soft gray rounded bubbles; Claude's replies render as plain ink text directly on the cream canvas with no bubble and no avatar (captures 01/04/05/08). The visual grammar quietly distinguishes *you* (container) from *Claude* (voice on paper). Alignment of the user bubble could not be resolved (near-symmetric margins) and stays `UNVERIFIED`. (`OBSERVED`)
- **Sheets, not boxes.** Cards, artifacts, attachment chips, and task rows are white sheets floating on cream with soft shadows and hairline borders — elevation is conveyed by *lightness* (white over cream over tint), not by heavy shadow. On dark surfaces, elevation is conveyed by lightness steps of the same ramp (`#262624` → `#3D3D3A` → `#575755` measured in capture 04). (`OBSERVED` + `MEASURED`)
- **Dense enough to work, sparse enough to breathe.** Message column and card lists keep ~10–14 % side insets (measured approx: card list x≈56–336 of 392 px; composer inset ≈10 % per side); list gaps ~10–14 px. Hierarchy is carried by text weight and gray tiers, not by color or size explosions. (`MEASURED`-approx)
- **Product polish.** Hairline borders (gray-200/300 range), subtle shadows, consistent pill geometry, and the single-accent rule read as deliberate design-system governance — the same ramp is documented brand-wide (anthropic.com aliases it ivory/slate/cloud). (`OBSERVED` + `DOCUMENTED`)
- **Seriousness with warmth.** Near-black warm ink `#141413` on paper (17.5:1 contrast — AAA) gives a documentary seriousness; the rationed terracotta clay and the spark mark supply the warmth. The combination is the signature: *a serious tool that feels warm*. (`MEASURED` contrast + `OBSERVED`)

---

## 4. Color & theme architecture (summary)

The system is one **warm neutral ramp** (21 documented steps, `--swatch--gray-000…1000`) plus **one brand accent family** (clay `#D97757`, interactive `#C96442`) plus **rationed semantic hues** (error `#B53333`; success green; status blue; content-accent violets). Roles documented in claude.ai CSS: background-primary → gray-050 `#FAF9F5`; background-secondary → gray-100 `#F5F4ED`; background-tertiary → gray-150 `#F0EEE6`; foreground-primary → gray-950 `#141413`; foreground-secondary → gray-750 `#30302E`; foreground-tertiary → gray-600 `#5E5D59`; border tiers → gray-400/300/200; text-accent and selection → clay (selection at 50 % alpha).

Measured app-side confirmation: canvas `#faf9f5` (exact), cards `#ffffff`, user bubbles `#d5d5d1–#d7d6cf` (≈ gray-250/300), composer pill `#fafafa`, send and "+" buttons `#d9795a` (≈ clay), dark artifact surface `#262624`/`#3d3d3a`/`#575755` (≈ gray-800/700/600–650). All sampled values are `MEASURED`-approximate and are corroborations, not tokens.

**How the app prevents accent inflation:** clay is *rationed to one primary control per screen*; blue is reserved for status/selection semantics (measured dots `#1490ff–#2e9cff`; switch-active documented `#2C84DB`); green only for success/online; violet only inside artifact content; and the entire structural load (backgrounds, bubbles, chips, borders, text tiers) is carried by the neutral ramp. There is no second competing brand color, and no large saturated surface exists in any capture.

The complete role-based inventory — every surface, text tier, semantic color, dark equivalents, and contrast notes — is delivered in **`claude-mobile-theme-color-token-inventory.md`**.

---

## 5. Typography & spacing (summary)

Documented families (public CSS): **Anthropic Sans, Anthropic Serif, Anthropic Mono** (variable, 300–800, roman + italic), plus JetBrains Mono and Noto Sans on claude.ai, and Tiempos Text on anthropic.com. In captures: serif appears in the new-chat greeting and marketing captions; all working UI text reads as a grotesque sans; placeholder text is gray sans. The mobile runtime font family is `INFERRED` (Anthropic Sans-family) and the exact mobile type scale is `UNVERIFIED` — no official source states point sizes.

Spacing rhythm measured approximately from captures: composer pill ~48 px tall at 392 px width, inset ~10 % per side; top bar ~30–36 px at capture scale; card gaps ~10–14 px; message bubbles max-width ≈65–75 % of column. Radii: ~12–20 px cards/bubbles, full pill for composer/chips, circles for buttons, squircles for icon tiles. Borders: hairline gray-200/300. Shadows: soft, subtle card shadows (light); elevation-by-lightness (dark). Full spec: **`claude-mobile-typography-spacing-elevation-spec.md`**.

---

## 6. Component system overview

Verified component anatomy covers: chat top bar (menu left; "+" and "⋯" right — `OBSERVED`); composer (single white stadium pill: [+] · model pill ("Opus") · placeholder · mic · circular clay send — `OBSERVED` and `DOCUMENTED` controls reconcile: voice-mode sound-wave glyph next to mic, dictation mic right side, model menu next to send controlling model/effort/thinking); message pair (gray user bubble vs plain-text Claude reply); white artifact/attachment cards with icon + title + gray subtitle; task-list surface (filter chips, white task cards, status dots, white hairline-bordered "Approve" button); dark immersive artifact surface (✕/⋯ header, progress line, status pills, violet ANSWER pill); badges (gray "Completed", white-on-dark "0 correct", violet "ANSWER"); Code-tab structures (session list, computer icon with green online dot, permission-mode dropdown, diff indicator "+42 -18" — all `DOCUMENTED`, visual chrome `UNVERIFIED`).

Full contracts — anatomy, dimensions, variants, states, accessibility, motion, usage rules for each — are delivered in **`claude-mobile-component-contracts.md`**.

---

## 7. Interaction states (summary)

Documented states include exact user-facing strings: usage warnings ("Approaching 5-hour limit."; "5-hour limit reached - resets [time]"), length and capacity errors ("Your message will exceed the length limit for this chat…"; "Due to unexpected capacity constraints, Claude is unable to respond to your message. Please try again soon."), file errors ("Uploaded file is too large"), empty states ("No shared content found"), artifact errors with a "Try fixing with Claude" affordance, and the thinking indicator ("'Thinking' indicator with a timer… expandable 'Thinking' section above Claude's response"). Code-session states: online (green dot), offline within seconds, reconnect queueing, forwarded dialogs that stay open until answered, and others that expire after ~5 minutes with the no-action default. Color mode Light / Match System / Dark is documented product-wide; the full mobile dark palette is `UNVERIFIED` beyond the measured dark artifact surface.

State signaling is multi-channel, never color-alone: color + icon (green check), text + timing (limit strings with reset times), structure (expandable Thinking section), system channels (push notifications), and platform permissions. The complete state matrix and interaction/motion/accessibility behavior are delivered in **`claude-mobile-interaction-motion-accessibility-spec.md`**.

---

## 8. Composition & hierarchy (summary)

Phone-first composition rules derived from the captures: one clay primary action per viewport (send in chat; "+" on list surfaces); filled surfaces limited to white cards on cream (usually 1–3 per viewport); secondary actions subordinate as hairline-bordered or borderless controls; the top bar stays transparent over the canvas while the composer anchors the bottom as the second-most-visual element; alignment runs on a single column with ~10–14 % insets; identity (spark, serif greeting) is separated from interaction (clay controls), selection (darker chip tint), and semantic status (blue dots, green text, gray pills). Full patterns: **`claude-mobile-composition-patterns.md`**.

---

## 9. Chat surface — separated study

**Structure (`OBSERVED` + `DOCUMENTED`):** top bar with menu icon left and circular "+" plus "⋯" right (iOS "⋯" / Android "⋮" per support article 8230524; Share button upper right per 10593882); conversation column; composer pill anchored at the bottom; no bottom tab bar in any official capture. Profile entry: "your initials in the upper right corner" (article 10065434) — top-right account control. Incognito: ghost icon upper right, "Incognito chat" label upper left with a black border, "x" to close (article 12260368).

**Conversation rendering (`OBSERVED`, alignment `UNVERIFIED`):** user turns in gray rounded bubbles (measured ≈ gray-250/300); Claude replies as plain ink text on canvas; artifacts and connectors render as inline white cards — interactive connectors appear "as compact components embedded directly in the conversation" with a fullscreen variant where "the conversation input remains available" (article 13454812); inline custom charts/diagrams documented in release notes (Mar 2026); device-action cards documented (articles 11869619/29).

**Composer (`OBSERVED` + `DOCUMENTED`):** one stadium pill containing [circular "+"] [pill model selector labeled with current model, e.g. "Opus"] [placeholder text] [mic icon] [circular clay send button with up arrow; arrow hidden in empty state — captures 05 vs 09]. Documented controls that reconcile: dictation mic on the right side of the input; voice-mode icon (sound wave symbol next to the microphone); model menu *next to the send button* controlling model + effort (Low/Medium/High/Extra high/Max) + thinking toggle, with a "More models" option; attachments via "+" (web-worded; exact mobile placement `UNVERIFIED`); file limits 500 MB/file, 20 files/chat. Attachment chips observed: thumbnail + blue "DOC" / gray "PDF" badges. Thinking indicator: timer + expandable section above the response; incomplete-thought message documented.

**Greeting/empty state (`OBSERVED`):** centered serif "What are you thinking?" with terracotta spark mark; composer placeholder "Chat with Claude". Other empty states (chat list, Code tab) `UNVERIFIED`.

---

## 10. Mobile Code tab — separated study

The official documentation (code.claude.com/docs/en/mobile, /remote-control, /claude-code-on-the-web; support article 14898120) is explicit: the mobile app is "a client for Claude Code sessions rather than a place where code runs". "Tap Code in the app's navigation to reach your sessions" — the Code tab lives in the app's navigation; since no capture shows a bottom tab bar, the navigation is a drawer opened from the top-left menu (`INFERRED` — visual form `UNVERIFIED`).

Documented contents and behaviors: session list showing cloud sessions and Remote Control sessions, the latter with "a computer icon with a green status dot when online" and offline state appearing "within seconds" of the local process exiting; new-session composer (select repository + branch, describe the task, submit — deep-linkable via `claude://code/new?q=&mode=plan|code&repo=&branch=`); in-session steering ("check progress, answer Claude's questions, or steer it in a new direction"); permission-mode dropdown — cloud sessions: Accept edits / Plan / Auto; Remote Control: Manual / Accept edits / Plan (never Bypass; never Auto on RC); diff pane of uncommitted changes with a diff indicator "like +42 -18"; push notifications "when a long-running task finishes or when it needs a decision from you" (toggles "Push when Claude decides" / "Push when actions required"); command surface — /mcp returns a text summary, /config accepts key=value, text-output commands work while local-only ones (/plugin, /resume) do not; attachments — photos attach directly to messages, other files download and pass as @-references; session rename from the app syncs to the CLI; Trusted Devices verification (Face ID/Touch ID/passkey step-up) gates Remote Control access on Team/Enterprise.

The capture named "Code_Review" shows a *task-list surface* (filter chips All/Blocked/In progress/Done; white task cards with colored squircle icons, repo paths, timestamps, blue status dots, green "Connected" text; expanded card with a hairline-bordered "Approve" button) — its exact mapping to the Code tab is unconfirmed, so it is treated as evidence of *list-surface grammar*, not as the Code tab itself.

---

## 11. Motion & accessibility (summary)

Motion is largely `UNVERIFIED`: no official documentation of transitions, durations, easings, haptics, or sounds was found, and static captures cannot show them. Documented dynamics are behavioral rather than visual: reconnect queueing, dialog expiry (~5 min), push notifications, thinking timer. Accessibility: VoiceOver, Dynamic Type, and reduced-motion support are `UNVERIFIED`; documented items include the biometric step-up, OS permission prompts, iOS Focus/notification-summary effects, Android battery-optimization guidance, and the web-side font setting (Default / Match System / Dyslexic Friendly). Full behavior: **`claude-mobile-interaction-motion-accessibility-spec.md`**.

---

## 12. Evidence limitations & UNVERIFIED inventory

Access limitations: no direct app observation (no authorized device/session); official captures are Apple-compressed 392×696 marketing composites (±2–4 RGB sampling precision; several are photographic and yield no tokens); the original May 2024 iOS announcement page is gone (date anchored via iTunes API); store metadata is volatile (a verification re-fetch returned drifted version/rating/size values — cited "as of Sept 2026"); Samsung US spec pages are retired and page_reader was unreliable during verification (Samsung values verified from staged dual-region fetches: UK + FR + global newsroom).

`UNVERIFIED` (must not be assumed in any derivative artifact): exact navigation chrome beyond "app's navigation" containing Code (drawer itself is `INFERRED`; other entries unknown); user-bubble alignment; message action rows (copy/retry/edit); code-block rendering inside chat; mobile "+" placement (web wording only); the "Tools" surface layout; onboarding/login screens; chat-list and Code-tab empty states; mobile dark-mode palette beyond the measured dark artifact surface; mobile runtime fonts and type scale; exact radii/borders/shadow values; voice-mode UI (capture is photographic); widget colors; haptics/sounds/animations; landscape and iPad layouts; age-rating badge (conflicting 17+/18+ — do not render).

---

## 13. Relationship to the interactive prototype

The companion artifact **`claude-mobile-visual-research-prototype.html`** demonstrates the verified principles above in a phone-first offline research prototype with a Samsung Galaxy S25 / S25+ / S25 Ultra device harness. Every studied-UI element in the prototype maps to the GREEN/YELLOW/RED evidence boundary defined by Agent 4's verification pass: GREEN items are represented with evidence labels; YELLOW items carry visible INFERRED/UNVERIFIED tags; RED items (login, onboarding, voice UI, tools grid, widgets, invented workflows) are omitted. The prototype is an independent research artifact, not an official Anthropic application, and states this on every screen. Independent QA of the built prototype is recorded in **`claude-mobile-prototype-qa.md`**.
