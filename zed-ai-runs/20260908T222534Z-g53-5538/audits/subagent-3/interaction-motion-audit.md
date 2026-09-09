# Interaction & Motion Audit — Subagent 3 (Task R4-c)

**Target:** `/home/z/my-project/repos/Documents/zed-ai-runs/20260908T201936Z-g53-252a/visual-foundation-package/` (offline gallery: `component-gallery.html` + `.css` + `.js`, `design-tokens.css`)
**Date:** 2026-09-09 · **Mode:** read-only research + report. No file outside `audits/subagent-3/` was touched; the repo was evidence only; live behavior exercised via `agent-browser` CLI over `file://` (no network, no persistence).

---

## 1. Methodology

1. **Full JS read** — `component-gallery.js` (317 lines) mapped end-to-end: gallery controls (viewport/dir/text/motion), evidence panel, chips single-select, segmented pill (RTL-aware thumb) + underline, search clear, amount grouping, select menu, overlay open/close/focus-trap/Escape, snackbar (5 s timer + undo), loading→completion→reset (double-submit guard), retry, clear-filters, nav switching. The file contains **exactly one keyboard listener (keydown, line 207)** and **zero pointer/touch/drag handlers** — decisive for the drag findings.
2. **Full CSS read** — `component-gallery.css` (621 lines) + `design-tokens.css`: every declared transition/animation enumerated (below). Keyframes `slideUp/slideDown/fadeIn/scaleIn/snackbarIn/ghostOut` are **defined (design-tokens.css:293–300) but referenced nowhere** — all overlay motion is un-wired.
3. **Docs cross-check** — `motion-interaction.md`, `button-system.md`, `overlay-system.md`, `component-contracts.md`, `empty-loading-error-states.md`, `verification-report.md` claims vs CSS/JS truth and live behavior.
4. **Live behavior via agent-browser** (persistent headless Chromium): clicks on demo triggers; Tab / Shift+Tab / Enter / ArrowRight / Escape; computed styles (`transition`, `animation`, `outline`), `activeElement`, `getBoundingClientRect` visibility after "close"; `performance.now` sampling of the segmented thumb slide (−15→−82 px over ~320 ms); snackbar 5 s boundary (open at 4.6 s, hidden-attr at 5.4 s); drag attempt on the sheet handle (no-op).
5. **Matrix re-runs** — key checks at 390 px and 320 px, LTR and RTL (via the gallery's own direction control), large text (`data-text-size=large`), reduced motion (`data-motion=reduced`); attribute state re-verified inside each eval to rule out toggle races.
6. **Classification** — each required behavior marked present / partial / missing with executable evidence; each finding classified as works / documented-but-not-implemented / implemented-but-divergent / missing.

---

## 2. Timing matrix (required system vs tokens vs docs vs CSS actual)

| Use | Required | Tokens | Docs claim | CSS/live actual | Verdict |
|---|---|---|---|---|---|
| press | **80 ms** | `--motion-press: 120ms` (tokens:184) | 120 ms scale 0.97 (motion:11) | `.btn` transform+bg 120 ms ease-out (css:126); computed 0.12 s | **divergent** (+40 ms) |
| fast | **120 ms** | `--motion-fast: 200ms` (tokens:185) | 200 ms scrim/border (motion:12) | input border 200 ms (css:191); chip 200 ms (css:260); scrim not transitioned | **divergent** (+80 ms) |
| normal | **200 ms** | `--motion-base: 300ms` (tokens:186) | 300 ms thumb/snackbar/nav (motion:13) | thumb 300 ms ease-out (css:292), live slide ~320 ms | **divergent** (+100 ms) |
| sheet-in | **240 ms** | `--motion-sheet: 340ms` (tokens:187) | 340 ms slide (motion:14/34; overlay:16) | **no motion** — computed `all 0s ease`; instant `[hidden]` swap | **claimed-not-implemented** |
| sheet-out | **180 ms** | none | 340 ms down exit (motion:34) | instant hide (`.sheet[hidden]`, css:477) | **missing** |
| dialog-in | **160 ms** | none | scaleIn 200 ms (motion:34; overlay:24) | **no motion**; scaleIn unused | **claimed-not-implemented** |
| dialog-out | **120 ms** | none | 200 ms fade+scale (motion:34) | none (and "close" doesn't hide — S3-01) | **missing** |
| scrim | **200 ms** | (bound to `--motion-fast`) | 200 ms fade (motion:12/34) | `.scrim` no transition; pops instantly | **claimed-not-implemented** |
| snackbar in/out | (n/a) | (docs: 300 ms) | 300 ms slide+fade + 250 ms exit (overlay:36) | none; `snackbarIn` unused; JS hides instantly at 5 s | **claimed-not-implemented** |
| snackbar hold | 5000 ms | `--snackbar-duration: 5000ms` | 5 s | JS timer 5000 ms; live 4.6 s open → 5.4 s hidden-attr | **pass** (element stays rendered — S3-02) |
| quiet completion | documented (800 ms) | none | 800 ms (motion:30) | JS 800 ms; live verified | **pass** |
| menu open | (n/a; docs 200 ms) | none | 200 ms fade/scale (overlay:28) | none | **claimed-not-implemented** |
| drag release | required behavior | docs: .3 s | "preserved exactly" (motion:38) | no drag code at all; live drag no-op | **missing** |
| skeleton | (pulse allowed) | 1.5 s | 1.5 s opacity pulse | 1.5 s ease-in-out infinite (css:552) | **pass** |
| spinner | (n/a) | none | spin for loading | 0.8 s linear infinite (css:175) | **pass** |

**Timing summary:** 3 pass · 4 divergent (all four inherited faithfully from the source and self-consistently documented, but off the run-authority system) · 5 claimed-not-implemented · 3 missing (no token, no code). The only motions that actually run today: press 120 ms, chips 200 ms, thumb 300 ms, nav pill 300 ms, spinner 0.8 s, skeleton 1.5 s.

---

## 3. Behavior matrix (50 rows — 30 present / 4 partial / 16 missing)

Full machine-readable rows in `interaction-motion-audit.json`. Condensed:

### Present (verified live)
- **Button states**: six interaction states of one "Save" button, labeled as states (html:136–163) — default/pressed-hold (primary-800 step + `.press` scale 0.97)/focused (fill unchanged + 2 px ring, `rgb(5,123,124)` offset 2)/disabled (no shadow, no press, not-allowed)/loading/quiet completion. Not presented as six terracotta identities (variants live in a separate frame).
- **Double-submit guard**: repeat clicks at 0 ms and 0.5 s during the 1600 ms load ignored — cycle ran exactly once.
- **Quiet completion cycle**: 800 ms check state → reset → "Record saved" snackbar (live-sampled at 1.7 s / 2.7 s).
- **Chips single-select** (one `.on` at a time) and **clear-filters** (resets to "All" + snackbar).
- **Segmented pill thumb**: real 300 ms slide, RTL-correct logical placement (rect-matched to the active segment in RTL).
- **Select menu open/select/value-update/close-on-select** with `aria-expanded`.
- **Sheet opens** with scrim, 36×5 handle, title, 48 px rows; **focus moves in** on open; **Tab trapped** (8 tabs + Shift+Tab wrap; same in RTL); **Escape and scrim-click close** (attribute-level).
- **Dialog**: opens, focus to Cancel, Tab trapped, Escape/Confirm/Cancel/scrim close (attribute-level).
- **Snackbar**: fires, `role=status`/`aria-live=polite`, 5 s timer correct, replaces prior (timer reset), undo button present.
- **Retry** (busy-guarded 1400 ms + success snackbar), **nav switching** (one active), **search clear + refocus**, **amount live grouping** (`1234567` → `1,234,567`).
- **Keyboard reachability/operation** (all controls are native buttons/inputs; Enter activates chip/menu/triggers), **visible 2 px focus ring**.
- **Reduced motion**: `data-motion=reduced` collapses every transition/animation to 0.01 ms / iteration 1 (computed live); state meaning preserved (selection fill, loading label+disabled, completion color, thumb lands instantly).
- **320 px usable** (no horizontal overflow; sheet 286 px in-viewport; rows 48 px; input 246 px), **large text usable** (root 17 px, button 51 px, chip row scrolls), **RTL parity** for all key interactions (defects reproduce identically).
- **Prohibitions upheld**: no bounce/springs/glow, no count-up, no page-wide slide, skeleton is an opacity pulse (no wave).

### Partial
- **Loading state**: works (spinner + disabled + guard) but label changes "Save"→"Saving" (label must be preserved), no icon slot exists to replace, no `aria-busy` (S3-14).
- **Underline segmented variant**: selection works; indicator swaps instantly per-button instead of the source's shared sliding indicator (S3-16).
- **Escape closes top layer**: closes sheet/dialog; does NOT close the select menu or evidence panel (S3-12).
- **Error recovery near failed control**: message below the field exists, but static — no in-place recovery preserving input (S3-17).

### Missing (16)
focus-restore-on-close (broken, S3-03) · sheet entry/exit motion (S3-04) · sheet drag-to-dismiss + snap points (S3-06) · sheet safe-area (S3-13) · body scroll lock (S3-21) · dialog **visual** close (blocker S3-01) · dialog entry motion · scrim motion · snackbar **visual** dismissal (blocker S3-02) · snackbar enter/exit motion · state-restoring undo (S3-08) · staged filter sheet with Apply/Reset/Cancel + active count (S3-07) · quick-action rail with snap + next-item cue (S3-09) · chevron direction feedback · local row insert/remove feedback (S3-10) · progress bar with immediate final numbers (S3-11).

---

## 4. Findings by severity (22 total)

### Blockers (2)

| ID | Area | Finding (evidence) | Fix |
|---|---|---|---|
| **S3-01** | dialog | **The dialog never visually closes.** `.dialog { display:flex }` (css:503–509) overrides the UA `[hidden]{display:none}`; only `.sheet[hidden]` and `#evidence-panel[hidden]` have explicit rules (css:477, 581). Live: after Escape/scrim/Cancel/Confirm — `hidden=true` yet rect 324×194, Cancel still visible and clickable; focus stays on the "closed" Cancel; same in RTL. The prior verification-report:55 marked close PASS from the hidden attribute alone. | Add `.dialog[hidden], .snackbar[hidden] { display:none }` (or class-based open state); re-verify with rect/offsetParent. **corrected** |
| **S3-02** | feedback | **The snackbar never visually dismisses.** Same root cause (css:518–524). Live: after the 5 s timer, `hidden=true` but rect 254×68 still rendered — once fired, a snackbar (with its live Undo button) stays on screen indefinitely; "Undo" merely swaps the message. | Same CSS fix + implement the documented 300 ms enter / 300 ms+250 ms exit. **corrected** |

### Majors (9)

| ID | Area | Finding | Fix / class |
|---|---|---|---|
| **S3-03** | focus | **Focus restore to trigger is broken.** `openOverlay()` (js:181–188) calls `overlayClose()` first, which nulls `openTrigger` (assigned at js:191/198 *before* the call). Live: sheet Escape → `activeElement=BODY` (focus lost); dialog Escape → focus on hidden Cancel. Docs claim restore (motion:26, overlay:20). | Pass the trigger into `openOverlay` and set it after the internal close; one fix covers scrim/Escape/close-button paths. **corrected** |
| **S3-04** | timing | **All overlay motion is documented but not implemented.** Live computed: sheet/dialog/scrim/snackbar/menu all `transition: all 0s ease`, `animation: none`; keyframes (tokens:293–300) referenced nowhere. Claims: motion-interaction.md:34, overlay-system.md:16/24/28/36. | Wire `slideUp/slideDown/scaleIn/snackbarIn/fadeIn` with token durations (needs a closing-class pattern so exits animate before `display:none`). **corrected** |
| **S3-05** | timing | **Token durations diverge from the required system**: press 120 (req 80), fast 200 (req 120), base 300 (req 200), sheet 340 (req 240); no sheet-out/dialog-in/dialog-out tokens. Values are faithful source inheritances and match the docs — but not the run authority. | Normalize the token set to 80/120/200/240/180/160/120/200 with dedicated in/out tokens; update motion-interaction.md and the evidence-panel Motion table. **normalized** |
| **S3-06** | sheet | **Drag-to-dismiss + snap points absent.** Zero pointer handlers in JS (grep: none; only keydown at :207); live drag of the handle is a no-op. motion-interaction.md:38 claims the source drag ("preserves the geometry and motion exactly" — BottomSheet.jsx:88–126: −50 expand / +130 close / −44 clamp, transition suppressed during drag). | Port the source drag model: pointer events on the handle (`touch-action:none`), thresholds, 84 %/94 % snap states, `.3s` release transition, Escape collapses first. **corrected** |
| **S3-07** | filter | **Staged filter sheet missing entirely.** The only sheet is an "Add record" action sheet (html:488–501). No Filter trigger, no grouped choices (status/date/type/sort), no Apply/Reset/Cancel commit semantics, no active-count. Required behavior C. | Build it: compact filter trigger (+count) → sheet with grouped staged choices, sticky [Reset | Apply] row, commit-on-apply / discard-on-cancel, parent-side summary. **proposed** |
| **S3-08** | undo | **Undo is a message swap.** js:236–240 fires a second snackbar ("Deletion reversed"); no state exists to restore. Criterion: undo must actually restore state; no toast-only proof. | Pair the snackbar with a live list: delete removes a row (ghostOut), Undo re-inserts it at the same index; count updates. **proposed** |
| **S3-09** | rail | **No quick-action rail.** Only plain `overflow-x` rows (chip-row css:249–253; segctl-lines css:303). No scroll-snap, no proximity snap, no next-item cue. Required behavior G. | Add a rail demo: `scroll-snap-type: x proximity`, center snap-align, next-item peek, `overscroll-behavior` containment. **proposed** |
| **S3-10** | rows | **No local row insert/update/removal feedback.** `ghostOut` keyframe (tokens:300) unused; no mutating demo. Contracts §6 and motion:13 claim it. | Wire ghostOut (300 ms height+opacity, no sibling transform) + an insert highlight; local only. **corrected** |
| **S3-11** | feedback | **No progress/relationship bar.** Nothing animates a fill, and the "final numeric value immediately" pattern is undemonstrated. | Add a compact progress bar whose fill transitions at the normal token while the mono numeric label jumps instantly to the final value (no count-up). **proposed** |

### Minors (6)

| ID | Area | Finding | Fix / class |
|---|---|---|---|
| **S3-12** | menu | Menu ignores Escape and outside clicks; focus never moves into it (live: open after Escape/outside click). overlay-system.md:28 claims both close paths "same focus containment". `overlayClose` (js:171–177) excludes the menu. | Include menu in Escape + document-level outside close; focus first/selected option; restore to trigger; arrow keys. **corrected** |
| **S3-13** | safe-area | No `env(safe-area-inset-*)` applied anywhere in the gallery (utilities at tokens:247–248 unused). Live: sheet paddingBottom 0 px; nav padding 8/12/16; actionbar 12/16. responsive-geometry.md:26 claims five surfaces. | Apply `.safe-area-bottom` (or `calc(32px + env(...))`) to sheet/nav/actionbar. **normalized** |
| **S3-14** | buttons | Loading changes the label ("Save"→"Saving", js:253) instead of preserving it; no icon slot; no `aria-busy` (contract §1 claims it; button-system.md:31 claims "label persists"). | Keep label constant; swap a leading icon slot to the spinner; set `aria-busy`. **corrected** |
| **S3-15** | keyboard | Contract ARIA not implemented: chips lack `aria-pressed`, nav active item lacks `aria-current`, segmented lacks `role=radiogroup`/arrow keys (contracts §3/§4/§8). Controls remain Tab/Enter-operable. | Add the three semantics + roving tabindex with mirrored arrow keys in RTL. **normalized** |
| **S3-16** | segmented | Underline variant does not slide — per-button border swap (css:304–311) vs source's shared 300 ms indicator (SegmentedControl.jsx:79–85; contract §4 "underline slides same"). | Shared absolutely-positioned 4 px indicator, inset-inline-start/width like the pill thumb. **corrected** |
| **S3-17** | error-recovery | Field error is display-only (html:221–222, static "12,4o0"); no in-place recovery preserving typed input. Retry is a separate surface panel. | Make the invalid-amount demo live: validate on input, keep value editable, clear error on fix without losing focus. **proposed** |

### Notes (5)

- **S3-18** `.chip { transition: all … }` (css:260) violates the package's own "one property per transition" principle (motion:5). → restrict properties. *normalized*
- **S3-19** Spinner is fixed-white (css:172–175) vs documented `currentColor` (button-system.md:31). Fine on primary; non-reusable. *normalized*
- **S3-20** The static "Quiet completion" demo (html:158–161) lacks the check icon — only the loading cycle shows it. *corrected*
- **S3-21** No body scroll lock while overlays are open (overlay-system.md:20; source locks at BottomSheet.jsx:33). *normalized*
- **S3-22** Method gap in the prior run: verification-report.md:54–58 asserted closes via the `hidden` attribute only — both blockers and the missing motion layer passed unnoticed. Repair verification must use rect/offsetParent visibility + computed transition assertions. *unresolved*

---

## 5. Keyboard & focus audit (results)

| Check | Result |
|---|---|
| All interactive controls Tab-reachable | **pass** (native buttons/inputs throughout) |
| Enter operates chips / select menu / overlay triggers / nav | **pass** (live) |
| Visible focus ring (2 px, offset 2, accent.600) | **pass** (computed `2px solid rgb(5,123,124)`) |
| Focus moves into overlay on open | **pass** (sheet Close, dialog Cancel; 60 ms delay) |
| Tab containment in sheet & dialog | **pass** (8 tabs + Shift+Tab wrap; both directions) |
| Escape closes overlay | **pass** for sheet/dialog (both directions); **fail** for menu (stays open) |
| Focus restored to trigger on close | **fail — broken** (BODY after sheet; hidden-dialog Cancel after dialog; S3-03) |
| Focus never lost | **fail** (see above; the dialog case is masked by S3-01) |
| Arrow keys on segmented (contract) | **not implemented** (Tab+Enter works; no radiogroup semantics) |

## 6. RTL interaction checks (re-run in RTL via the gallery's own direction control)

- Sheet: opens, focus-in, Tab trap, Escape — **same behavior as LTR** (trap verified, `insideSheet:true`).
- Dialog: opens, Escape "closes" — reproduces both LTR defects (stays rendered; focus on Cancel).
- Segmented thumb: **RTL-correct** (JS computes `inset-inline-start` with an RTL branch, js:89–93; live rect-matched to the active segment; flex order flips correctly).
- Chevrons: mirrored only where `.mirror` is applied in the icon demo; the select's trailing chevron sits on the inline-end side via flex — correct.
- Conclusion: RTL parity holds for everything that works, and for everything that doesn't.

## 7. Reduced-motion audit

- `data-motion="reduced"` (design-tokens.css:283–290) plus the `prefers-reduced-motion` media query (275–282): **live-verified** — btn/chip/thumb `transition-duration: 1e-05s`; spinner/skeleton `animation-duration: 1e-05s`, iteration 1.
- State meaning preserved: selection fill/weight, loading label + disabled + static ring, completion check + positive tint (color-only), snackbar text. **pass**.
- Caveat: because the gallery implements almost no spatial movement, the kill-switch has little to neutralize — reduced-motion conformance is trivially satisfied. The real test (sheet slide suppressed while final state is instant and legible) can only be assessed after S3-04/S3-06 are repaired.

## 8. Concrete repair recommendations (what to build, with which tokens/timings)

1. **Fix the two blockers first (CSS, ~2 lines):** `.dialog[hidden], .snackbar[hidden] { display: none; }`. Re-verify closes visually.
2. **Fix focus restore (JS, ~5 lines):** `openOverlay(el, screen, trigger)` — call `overlayClose()` first, then set `openTrigger = trigger`; keep `overlayClose()` consuming it.
3. **Wire overlay motion with a closing-class pattern:** open → `animation: slideUp var(--motion-sheet-in) var(--ease-standard)`; close → add `.is-closing` (`slideDown var(--motion-sheet-out) var(--ease-in)`), hide on `animationend`; dialog `scaleIn var(--motion-dialog-in)` / fade-out `var(--motion-dialog-out)`; scrim `transition: opacity var(--motion-scrim)` (toggle a `.is-open` class); snackbar `snackbarIn var(--motion-base)` + 250 ms exit delay already documented; menu `fadeIn` fast.
4. **Normalize the timing tokens to the authority system:** `--motion-press: 80ms; --motion-fast: 120ms; --motion-normal: 200ms; --motion-sheet-in: 240ms; --motion-sheet-out: 180ms; --motion-dialog-in: 160ms; --motion-dialog-out: 120ms; --motion-scrim: 200ms` (alias `--motion-base` → 200 ms or migrate thumb/nav to `--motion-normal`). Update motion-interaction.md's table and the evidence-panel Motion table (html:704–711) in the same commit so docs stay truthful.
5. **Port sheet drag** from `BottomSheet.jsx:88–126` (pointer events, −50/+130/−44 thresholds, 84 %/94 % snaps, transition suppression, Escape-collapses-first) — then re-verify reduced motion still lands instantly.
6. **Build the staged filter sheet** (behavior C): Filter trigger + active-count → sheet with grouped choices, staged state, sticky [Reset | Apply], cancel-without-commit, parent summary chip.
7. **Build the feedback proofs:** live list with ghostOut removal + state-restoring Undo; progress bar (width transition at normal token, immediate final numbers); quick-action rail (x-proximity snap + next-item cue); in-place error recovery preserving typed input; chevron direction feedback on the select/menu open.
8. **Cheap contract fixes:** `aria-busy` on loading; `aria-pressed` on chips; `aria-current` on nav; radiogroup + arrows on segmented; menu Escape/outside close; safe-area utilities on sheet/nav/actionbar; keep the loading label constant; add the check icon to the static completion demo; restrict `.chip` transition properties.
9. **Verification discipline for the repair run:** assert *visibility* (rect/offsetParent), *computed motion* (`transitionDuration !== 0s` where claimed), *focus* (`activeElement === trigger` after close), and *timing* (sampled transitions) — not attributes alone.

## 9. Explicit unresolved list

- **S3-05 (timing authority conflict):** the four divergent tokens are faithful source inheritances, self-consistent with the package docs; the run authority requires different values. Needs an explicit authority ruling: normalize to 80/120/200/240 or ratify the inherited 120/200/300/340 (the JSON marks it `normalized` as the suggested default).
- **Sheet snap geometry:** the source's 84 vh/94 vh snap points presuppose a full-viewport sheet; the gallery mounts overlays inside a phone frame (`max-height: 84%`). Porting drag requires deciding frame-relative vs vh semantics.
- **Whether the gallery must demonstrate back-button/history dismissal (SOP §8.5 first rule):** out of scope for a file:// gallery in this run, but the contract language ("correct back behavior", navigation-shell) leaves the receiver's obligation open.
- **Safe-area verification on-device:** the CSS must be present (S3-13), but actual inset rendering remains a declared human-QA item (self-critique.md).
- **The `dir` reset anomaly** observed once between eval commands (attribute flipped back LTR after being set RTL) — not reproducible in isolated re-tests and harmless to conclusions (all RTL evidence was gathered with `dir` verified inside the same eval); worth remembering if the gallery ever gains state persistence.
