# Claude Mobile App — Interaction, Motion & Accessibility Spec

**Artifact:** `claude-mobile-interaction-motion-accessibility-spec.md`
**Date:** 2026-09-11 · **Coordinator synthesis (Agents 1, 2, 4 evidence)**

> **Disclaimer.** Independent research; not affiliated with or endorsed by Anthropic. Documented behaviors carry official sources; visual/motion specifics that no official source or capture resolves are UNVERIFIED and marked.

**Legend:** (D) DOCUMENTED · (O) OBSERVED via official capture · (M) MEASURED-approx · (I) INFERRED · (U) UNVERIFIED

---

## 1. State matrix

Legend per cell: signal channels used — C color · B border · S shape · Ic icon · T text · Mo motion · L layout · K keyboard · N system notification.

| Component | Default | Pressed | Focus | Disabled | Loading | Success/done | Error/retry | Selected/expanded | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| Composer | white pill, placeholder gray, send arrow hidden when empty | U (web analogue: clay→clay-interactive `#C96442`) | U (keyboard focus is implicit via input) | U | thinking indicator (T+Mo: timer; expandable section L) | response renders inline (L) | error strings in-conversation (T); "Please try again soon" retry wording | Cowork mode switch in bottom-left of message box (D) | O+M+D |
| Send button (clay) | clay `#D97757` fill, white arrow | U — pressed within clay family (I: `#C96442`) | U | hidden when input empty (O) — not "disabled" styling | n/a | n/a | n/a | n/a | O+M+D(CSS) |
| User message bubble | gray-250/300 fill, ink text | n/a | n/a | n/a | n/a | n/a | n/a | n/a | O+M |
| Claude response | plain ink text on canvas | n/a | n/a | n/a | "Thinking" indicator + timer; expandable section above response (T+Mo+L) | streaming completion U | inline error text; artifact errors offer "Try fixing with Claude" (T+Ic) | Thinking section expand/collapse (L+Ic) | D+O |
| Model selector pill | white pill with model name ("Opus") | U | U | U | n/a | n/a | n/a | opens model menu (model/effort/thinking) — menu visuals U, contents D | O+D |
| Icon buttons (+, ⋯, menu, mic, ✕) | neutral glyph on canvas/white | U | U | U | n/a | n/a | n/a | list-surface "+" is clay-filled (context variant, O) | O |
| Filter chips | light tint pill `≈#f6f5f2` | U | U | U | n/a | n/a | n/a | selected = darker tint (M) + count text | O+M |
| Task card / "Approve" button | white card; white+hairline "Approve" button | U | U | U | task in progress: blue dot (C) | "Done"; green "Connected" text (C+T) | "Blocked" chip state (O) | expanded card reveals context + full-width action (L) | O+M |
| Session row (Code tab) | list row; Remote Control rows show computer icon | U | U | U | offline appears "within seconds" (T+Ic state change) | green status dot when online (C+Ic) | failure notification with reason (N+T) | open session; rename syncs to CLI | D |
| Forwarded dialogs (RC) | permission prompt / AskUserQuestion | U | U | n/a | stays open until answered (D) | answered → session continues | n/a — no timeout for these | other dialogs expire ~5 min → no-action default (Mo+T) | D |
| Push notifications | off/on | n/a | n/a | "No mobile registered" warning (D) | n/a | "when a long-running task finishes" (N) | "when it needs a decision from you" (N) | toggles "Push when Claude decides" / "Push when actions required" | D |
| Buttons (brand/ink/secondary/tertiary) | documented fills (see contracts) | hover documented web-side: border-width doubles; fill swaps | U | disabled = gray-400/500 text tier (D role) | U | n/a | n/a | n/a | D(CSS) |
| Attachment chips | thumbnail + type badge | U | U | n/a | upload progress U | attached state (O) | "Uploaded file is too large" (T) | n/a | O+D |
| Usage limits | normal operation | n/a | n/a | n/a | n/a | n/a | warning "Approaching 5-hour limit." (T); block "5-hour limit reached - resets [time]" (T) | n/a | D |
| Empty states | chat landing greeting (O); session list content U | n/a | n/a | n/a | n/a | n/a | n/a | n/a | O+D+U |
| Dark/artifact surface | `#262624` overlay | U | U | n/a | progress line (L) | "0 correct" pill + green check (T+Ic+C) | "Try fixing with Claude" near artifact errors (T) | fullscreen vs inline variants (L) | M+D |
| Theme setting | Light / Match System / Dark | n/a | n/a | n/a | n/a | applies system-wide | n/a | one active option | D |

## 2. State-signal channel analysis

The system never relies on color alone; documented/observed signals are redundant:
- **Color + icon**: green dot + computer icon (online); green check + white pill (correct answers).
- **Color + text**: "Connected" green text; "Blocked" chip + count; error red text family with full sentences.
- **Text + timing**: limit messages embed concrete reset times ("resets [time]").
- **Layout/motion**: expandable Thinking section; expanded task cards; fullscreen connector views where "the conversation input remains available".
- **System channels**: push notifications for task completion and decision requests; OS permission prompts; biometric step-up.
- **Persistence semantics**: gating dialogs stay open until answered; non-gating dialogs expire (~5 min) with the no-action default — a safety-relevant timing contract.
What is U: pressed/focus visual treatments, haptics, sounds, animation curves. Any derivative must not invent them as fact — the prototype implements *neutral stand-ins* labeled as such (e.g., opacity/pressed-tint changes tagged UNVERIFIED styling).

## 3. Transitions & motion

Documented motion: none specific (no durations/easings/transition specs found in any official source; captures are static). Documented dynamics that imply motion: drawer/navigation opening ("Tap Code in the app's navigation" implies a navigation transition — form U); sheet/dialog presentation (visuals U); keyboard avoidance (U); reconnect queueing delivering queued "messages, permission prompts, and status updates" on reconnect (D); compaction progress display (D); offline state appearing "within seconds" (D — a timing contract: status change latency ≤ seconds).
Verdict: **motion design of the app is UNVERIFIED as a whole.** The prototype therefore implements only conservative, functional transitions (sheet slide/fade, list updates) and a reduced-motion mode, and labels all motion as research stand-ins.

## 4. Focus, touch & keyboard

- Focus indication: U (no documented focus styles; captures static). Platform conventions (iOS focus rings via keyboard, Android touch feedback) apply but are not app-documented.
- Touch targets: platform minimums 44 pt (iOS) / 48 dp (Android) are OS requirements; the app's own target sizes are U, though observed controls (circular buttons ≈36–44 px at 392 scale) sit in that family (M).
- Keyboard: text input always visible in chat and fullscreen connector views (D); dictation as an input alternative with 12 languages (D); voice mode as hands-free (default) or push-to-talk (D).
- Safe areas: see `claude-mobile-device-frame-validation.md` — hardware insets documented for reference devices, app handling U.

## 5. Accessibility

Documented: biometric step-up (Face ID/Touch ID/passkey, 18-hour sign-in freshness) gating Remote Control session access (D); OS permission flows (mic, notifications); iOS Focus and notification-summary suppression effects; Android battery-optimization guidance for push reliability (D); dyslexic-friendly font option (product setting, web-documented); multi-language dictation (D).
UNVERIFIED: VoiceOver labels/traits, Dynamic Type, contrast settings, reduced-motion support, screen-reader announcements for streaming responses, accessible drag targets. Store listings state no accessibility features.
The prototype's accessibility obligations (its own, not the app's): visible focus, keyboard-operable controls, AA contrast for text, 200 % text scale without loss, reduced-motion mode, ARIA labeling of QA harness controls.

## 6. Loading & completion patterns

- Loading: thinking indicator with live timer (D) — progress is *time-based text*, not a spinner; compaction progress in Code sessions (D); upload progress U.
- Completion: push notification on task finish (D); "Completed" pill on task cards (O); "Done" filter state (O).
- Partial results: expandable Thinking section; "the rest of Claude's thought process is not available" (D).

## 7. Error & retry patterns

Verbatim error strings are a design asset (D — see contracts §16). Pattern rules: errors render inline in the conversation as text (D for capacity/length/API errors); artifact errors co-locate a repair affordance ("Try fixing with Claude"); session failures notify with reason (D); retry is encouraged by wording ("Please try again soon") rather than a documented dedicated control. API error surfacing in Code sessions: 500, 529 Overloaded, 429, "Prompt is too long" (D).

## 8. Reduced motion, haptics, sound

All U for the app. The prototype ships its own reduced-motion mode and avoids decorative/perpetual motion entirely (per research-prototype requirements).
