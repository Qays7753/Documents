# Claude Mobile App — UI Component Contracts

**Artifact:** `claude-mobile-component-contracts.md`
**Date:** 2026-09-11 · **Coordinator synthesis (Agents 1, 2, 4 evidence)**
**Scope:** reusable component contracts for the official Claude mobile app — anatomy, dimensions, variants, states, accessibility, motion, usage rules. Dimensions are approximate (measured at 392 px capture width; scale ≈ dp at ~1×) or explicitly UNVERIFIED. Every contract states its evidence basis.

> **Disclaimer.** Independent research; not affiliated with or endorsed by Anthropic. Contracts describe observed/documented behavior of the official app for study purposes; values marked UNVERIFIED are open contracts, not assertions.

**Legend:** (D) DOCUMENTED · (O) OBSERVED via official capture · (M) MEASURED-approx · (I) INFERRED · (U) UNVERIFIED

---

## 1. Chat top bar / header

- **Role:** screen identity + primary utilities; transparent over canvas, does not scroll with content (O).
- **Anatomy:** left: menu icon (opens navigation — drawer `I`); right: circular "+" (new chat / create) and "⋯" (iOS) / "⋮" (Android) overflow (O + D, article 8230524). Profile = "your initials in the upper right corner" (D, 10065434) — coexists with these controls in the top-right zone. Share button lives "in the upper right corner of a chat" (D, 10593882).
- **Dimensions:** ≈30–36 px tall at 392 capture scale (M); touch targets should meet platform minimums (44 pt iOS / 48 dp Android — platform requirement, U for this app's specifics).
- **Radius/shape:** icon buttons circular (O). **Shadow:** none — borderless on canvas (O).
- **States:** default; pressed (U); the "+" reads neutral in chat captures but clay-filled on the list surface (O) — treat as context variant.
- **Usage:** one top bar per screen; keep utilities ≤3 on the right; never brand-colored except the single list-surface "+" (O).
- **A11y/motion:** U (no documented behavior).

## 2. Navigation drawer / "app's navigation"

- **Role:** primary navigation; contains the **Code** entry ("Tap Code in the app's navigation to reach your sessions" — D, code.claude.com/docs/en/mobile).
- **Evidence boundary:** drawer existence is `I` (top-left menu icon observed; no bottom tab bar in any capture); drawer contents beyond the Code entry are U.
- **Contract fields:** anatomy U; dimensions U; opening motion U; scrim U. Any derivative must label the drawer itself INFERRED and its extra entries UNVERIFIED.

## 3. Conversation list row

- **Role:** entry into a conversation; supports rename/delete.
- **Anatomy:** title row with per-row actions via touch-and-hold (iOS) or multi-select mode via "checklist icon in the top right corner" + trash icon (Android) (D, 8230524). Visual styling (avatar/thumb, timestamp, snippet) U.
- **States:** default; selected (multi-select — checklist state documented D); destructive confirm dialog on delete (D).
- **Usage:** destructive actions always confirm (D).

## 4. Chat message pair

- **User message:** rounded container, tinted fill **gray-250/300 (#DEDCD1–#D1CFC5 ramp; sampled #d5d5d1–#d7d6cf)**, max-width ≈65–75 % of column (M), radius ≈18–24 px at 392 scale (M); alignment U (margins measured near-symmetric — do not assume left or right). Contains message text in ink (M, contrast 12.5–13.4:1).
- **Claude response:** plain text on canvas, no bubble, no avatar (O), ink `#141413` (D ramp + M), full column measure.
- **Spacing:** vertical rhythm between turns ≈10–14 px family (M); horizontal column inset ≈10–14 % (M).
- **Variants:** response may embed artifact cards (§6), connector cards (D 13454812: inline compact cards or fullscreen view with input available), device-action cards (D 11869619/29), inline charts/diagrams (D release notes Mar 2026), thinking section (D: expandable, above the response, with timer).
- **States:** default; loading (thinking timer + expandable section — D); streaming (U); error/retry (D strings — §16); message action rows (copy/retry/edit) U.
- **Usage:** the asymmetry (container for user, bare text for Claude) is the system's core conversation grammar (O).

## 5. In-chat code / content block

- **Evidence:** no capture resolves in-chat code-block rendering; brand mono families documented (Anthropic Mono, JetBrains Mono — D CSS). **Contract is open (U).** Any derivative must label code-block styling UNVERIFIED and may only reuse the documented mono-family + dark-surface values as *hypothesis*, visibly tagged.

## 6. Artifact / content card (light)

- **Role:** rich response content container (files, maps, presentations, task results).
- **Anatomy:** white sheet; optional icon + bold title + gray metadata subtitle; content zone (media, sub-cards, fields, tone pills) (O captures 01/05/08).
- **Dimensions/radius:** white `#FFFFFF` fill (M); radius ≈12–20 px at 392 scale (M/VLM); soft subtle shadow (O); hairline border in gray-200/300 range (M).
- **Variants observed:** map card with black rating pills + horizontal sub-cards (01); presentation card "title · PPTX" with document icon (05); letter card with labeled Subject/Body fields + tone pills (08).
- **States:** default; error state with "Try fixing with Claude" affordance near the error (D, 9487310).
- **Usage:** one primary card per response region; cards float on canvas — never tint them with accent.

## 7. Dark immersive artifact surface

- **Role:** fullscreen focused-content overlay (flashcards et al.).
- **Anatomy:** outer surface **#262624**; inner card **#3D3D3A/#575755**; header with ✕ left / ⋯ right; white bold title + gray subtitle; thin progress line; white status pill ("0 correct") + green check; content pills e.g. violet "ANSWER" `#6e6b96` (all M, capture 04).
- **Elevation:** by lightness, not shadow (M).
- **Usage:** dark surface = immersion signal; content-accent hues may appear only here (violet) (M).

## 8. Composer (message box)

- **Role:** the screen's primary interactive element; also mode switch host.
- **Anatomy (O captures 05/09 + D articles):** one stadium (full-pill) white container, ≈48 px tall at 392 scale (M), inset ≈10 % per side (M): `[circular "+" attach]` · `[pill model selector "Opus"]` · `[gray placeholder text]` · … · `[mic icon]` · `[circular clay send button with up arrow]`.
- **Documented controls (D):** dictation mic "on the right side of the chat input field" (10065434); voice-mode icon "sound wave symbol next to the microphone icon" (11101966); "The model menu next to the send button controls three settings" — model, effort (Low/Medium/High/Extra high/Max), thinking toggle, plus "More models" (8664678); attachments via "+" with type/size limits (8241126).
- **Fill:** pill interior sampled `#fafafa` (M) — white/near-gray-000; reads borderless white-on-cream (O).
- **States:** empty (placeholder "Chat with Claude", send arrow hidden — O capture 09); composed (arrow visible — O 05); voice mode active (voice settings button "in the bottom left corner while chatting" — D); incognito variant (ghost icon upper-right start + "Incognito chat" label — D 12260368); Cowork mode via "select 'Cowork' in the bottom left corner" of the message box, "Chat" to return (D 15520349).
- **A11y/motion:** keyboard avoidance U; opening motion U.
- **Usage:** single composer per screen; it is the only clay-filled control in the chat viewport (O).

## 9. Attachment chip

- **Anatomy:** white chip above/inside composer zone: thumbnail + type badge (blue "DOC", gray "PDF") + filename (O capture 05).
- **Dimensions:** pill radius (O); height ≈ chip-scale ~36–44 px (M-approx).
- **States:** default; error "Uploaded file is too large" (D).
- **Usage:** chips cluster horizontally; badges carry the type signal so the thumbnail can stay decorative.

## 10. Buttons

| Variant | Fill / text | Evidence | Notes |
|---|---|---|---|
| Brand (clay) | `#D97757` fill (pressed/hover `#C96442`), off-white glyph | D CSS + M | icon-only circular usage observed (send, "+"); white-on-clay 3.12:1 — UI-component pass only, no small text |
| Primary (ink) | `#141413` fill, off-white text; hover `#1F1E1D` | D CSS | web-documented; mobile occurrence U |
| Secondary | `#E8E6DC` fill, `#4D4C48` text; hover swaps to white fill + ink text | D CSS | — |
| Tertiary (ghost) | transparent, `#5E5D59` text; hover ink | D CSS | — |
| Approve-style | white fill, ink text, hairline border, full-width in card | M (capture 07) | confirm action in task cards |

**States:** default; hover (web-documented: border-width doubles, fill swaps); pressed U; disabled (disabled text tier gray-400/500 — D role, step I); loading U.
**Touch targets:** platform minimums 44 pt / 48 dp — requirement of iOS/Android, U for this app's specifics.

## 11. Icon buttons

Circular (O); examples: "+" (attach/new), "⋯/⋮" (overflow), menu, mic, ✕. Sizes ≈36–44 px at 392 scale (M-approx). Neutral glyph on canvas or white; the context-variant clay fill follows the one-accent rule (§1). States beyond default U.

## 12. Model selector pill ("Opus")

- **Anatomy:** pill inside composer, left of mic/send; carries current model name; opens model menu (model/effort/thinking) (O + D).
- **Styling:** white/near-white fill (M); border/chevron U.
- **States:** default; open menu (D behavior, visuals U); "More models" option (D).

## 13. Filter chip (list surface)

- **Anatomy:** pill row under header: "All 300", "Blocked 12", "In progress 3", "Done" (O capture 07).
- **States:** unselected (light tint `≈#edeceb–#f6f5f2` family M); selected (darker gray tint — M; consistent with documented selection semantics = darker neutral, clay reserved elsewhere).
- **Usage:** chips segment a list; counts inside chips are tertiary-tier text (O).

## 14. Badges / status indicators

- **Pills:** gray "Completed" (O 06-context); white-on-dark "0 correct" + green check (O 04); violet "ANSWER" (O 04).
- **Dots:** small (~6 px M) bright blue `#1490ff–#2e9cff` for active items (O/M 07); **green dot** beside computer icon = Remote Control session online (D — the documented Code-session signal).
- **Semantic rule:** green = success/online; blue = status; gray = neutral state; violet = artifact content (D+M).

## 15. Menus, popovers, bottom sheets, dialogs

- **Documented behaviors:** delete/rename confirmations (8230524); share pop-out with visibility dropdown + Shared-chats modal incl. empty state "No shared content found" (10593882); attachment menu "+" → "Add files or photos" (8241126, web-worded); Remote Control **forwarded dialogs** (permission prompts, AskUserQuestion) stay open until answered; other dialog types expire after ~5 min and continue with the no-action default (code.claude.com/docs/en/remote-control); notification-permission prompt on setup (D).
- **Visual styling:** U (no capture resolves sheet/menu chrome). Any derivative labels visuals INFERRED at best.
- **Usage rule:** dialogs that gate agent actions must not auto-dismiss (D behavior above).

## 16. Empty / loading / error / retry blocks

- **Loading:** "Thinking" indicator with timer; expandable Thinking section above the response; "the rest of Claude's thought process is not available" for incomplete thoughts (D 8664678). Compaction progress shown in Code sessions (D).
- **Error strings (D, verbatim):** "Approaching 5-hour limit." · "5-hour limit reached - resets [time]" · "5-hour limit resets [time] - continuing with usage credits." · "Your message will exceed the length limit for this chat. Try attaching fewer or smaller files or starting a new conversation." · "Due to unexpected capacity constraints, Claude is unable to respond to your message. Please try again soon." · "There was an error logging you in" · "Uploaded file is too large" · "Try fixing with Claude" (artifact errors) · Code-session failures "Session creation failed", API errors surfaced in-conversation (500, 529 Overloaded, 429, Prompt is too long).
- **Retry:** "Please try again soon" wording (D); dedicated retry control visuals U.
- **Empty:** chat landing greeting (O 09); "No shared content found" (D); other empty states U.
- **Warning channel:** usage-limit warnings are text-first with concrete reset times (D) — warning is informational, not color-coded (no dedicated warning token found — U).

## 17. Code-tab components (documented structure, U visuals)

- **Session list row:** Remote Control sessions carry "a computer icon with a green status dot when online"; offline appears "within seconds" (D). Row anatomy/styling U.
- **New-session composer:** select repository + branch, describe task, submit (D; deep-link params q/mode=plan|code/repo/branch documented in 14898120).
- **Permission-mode dropdown:** cloud = Accept edits / Plan / Auto; Remote Control = Manual / Accept edits / Plan; Bypass unavailable; Auto unavailable on RC (D).
- **Diff indicator/pane:** "a diff indicator with lines added and removed, like +42 -18"; diff pane of uncommitted changes (D). Diff color tokens U.
- **Session interactions:** steering messages; stop subagents/background workflows from the device; rename syncs to CLI; /mcp text summary; /config key=value (D).
- **Push notifications:** "when a long-running task finishes or when it needs a decision from you"; toggles "Push when Claude decides" / "Push when actions required" (D).

## 18. Settings rows

- **Documented existence:** Color mode (Light / Match System / Dark); Chat font (Default / Match System / Dyslexic Friendly); Speech Input Language; Memory toggles ("Search and reference chats", "Generate memory from chats", "Include sensitive topics in memory"); Shared chats management (D, articles 8887527, 10065434, 11817273, 10593882). Entry point: initials (top-right) on mobile (D).
- **Visual styling:** U. Mobile settings location beyond the entry point U (articles web-worded).

---

## Cross-component rules

1. **One clay-filled control per viewport** (O) — it is the strongest action; everything else is neutral or hairline.
2. **Elevation = lightness step**, shadow only a soft whisper on white cards (O/M); dark surfaces never use shadow (M).
3. **Pill geometry everywhere**; no sharp corners observed (O).
4. **Hairline borders (gray-200/300) not boxes**; structure is tonal (O/M).
5. **Confirm destructive actions** (D). **Dialogs gating agent actions persist until answered** (D).
6. **Status semantics are small and color+shape+text redundant** (dot + text label; check + pill) (O/D).
7. **Any UNVERIFIED field above must be labeled as such in derivative artifacts** — open contracts, not defaults.
