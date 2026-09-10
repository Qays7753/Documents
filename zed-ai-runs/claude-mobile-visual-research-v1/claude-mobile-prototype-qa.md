# Independent QA Report — claude-mobile-visual-research-prototype.html

**Reviewer:** Agent 4 — Independent Evidence Verifier and Mobile UX Reviewer (phase 2, Task ID 6)
**Target:** `/home/z/my-project/download/claude-mobile-visual-research-v1/claude-mobile-visual-research-prototype.html` (105,791 bytes, 1,497 lines)
**Protocol:** review only — NO repair, NO modification of any file. Issues below are documented, not fixed.
**Reference standards:** `evidence-notes/agent4-verification.md` §5 (GREEN/YELLOW/RED boundary) + §6 (12-point checklist); `evidence-notes/prototype-brief.md` (binding build brief).

---

## 1. Review method

| Aspect | Method |
|---|---|
| Runtime engine | Headless Chromium via Playwright 1.62.1 (chromium-1234), same approach as Agent 5's Task 5 smoke test (its runner scripts were cleaned up post-task, so equivalent fresh runners were used and deleted after this QA; no repo files created or modified) |
| Runtime coverage | file:// load; 3 device presets; 4 viewport widths × 3 text scales in both Chat and Code modes (12 + 12 combos); keyboard sim on/off (both modes); safe-area overlays on/off; theme light/dark + settings sync + Match System; motion normal/reduced + `prefers-reduced-motion` emulation default; full interaction battery (send/thinking/reply, capacity error + retry, drawer, model sheet, attachment sheet, overflow menu, delete-confirm persistence, Code-mode mode-set enforcement, session detail, diff, permission prompt, queue toast); focus/Tab/Esc/trap; request + console/page-error tracking |
| Static coverage | Full 1,497-line read; targeted greps for external resources, RED representations, hardware-fidelity claims, token usage sites, verbatim strings, tag inventory |
| Contrast | WCAG 2.x relative-luminance recomputation for 23 as-built pairs (same formula as `scripts/contrast-check.py`) |
| Verbatim-string diff | All 7 documented strings byte-compared against the prototype AND the staged T1 articles (a1-errors2.html, a1-upload-files.html, a1-share-chats.html) — all 7 exact in both |
| Limitations | (a) Runtime = desktop Chromium; touch behaviors simulated as pointer/keyboard events. (b) Focus-visible verified via computed outline on keyboard-driven focus, not human visual inspection. (c) `prefers-color-scheme`/`prefers-reduced-motion` tested via Playwright emulation. (d) The s25p caption check "2.090" initially flagged by my string probe is a display-formatting nit (see §7, issue 4), not a value error. All 12 checklist points received runtime verification except where marked "static" in §2. |

## 2. Per-check results (§6 checklist)

| # | Check | Result | Evidence / notes |
|---|---|---|---|
| 1 | Token fidelity (computed styles vs boundary) | **PASS** | Light: canvas rgb(250,249,245)=#FAF9F5, bubble #D1CFC5 r20px maxW72%, card #FFFFFF r16px border #E8E6DC 1px, code #262624 r12px, send #D97757 r50%, ink #141413, tertiary #5E5D59, placeholder #87867F; `:hover` send = rgb(201,100,66)=#C96442. Dark: canvas #1F1E1D, card #262624, tint #3D3D3A, bubble #30302E, ink #FAF9F5, secondary #D1CFC5, tertiary #B0AEA5, borders #3D3D3A, clay unchanged. Measured approximations (#d9795a/#d5d5d1/#d7d6cf/#6E6B96/#1490FF) appear only as evidence-panel citations; #1490FF/#6E6B96 declared as custom properties but used by zero rules (cited-only honored) |
| 2 | Evidence labeling | **PASS** | 22 visible tag/tag-block instances in studied UI (identical set in light & dark) + 2 "inset UNVERIFIED" strip tags + dark-mode dashed INFERRED note; evidence panel enumerates GREEN (label+source), YELLOW (tag text → where), RED (exclusions), hex-provenance table, harness conventions. All 7 verbatim strings exact. Sources cited as bare domains/paths (documented convention — see §7 issue 7) |
| 3 | RED containment | **PASS** | Greps for login/sign-up/onboard/auth/#C6613F/voice UI/tools grid/dispatch/widgets/iPad/17+/18+/lock-screen/Siri: every hit is inside the evidence panel's RED exclusion list (negative statement) or a CSS comment; zero rendered representations; #C6613F appears once, in the RED list only |
| 4 | Contrast (AA for text; 3:1 UI exception for icon-only send) | **PARTIAL** | Light AA text pairs all pass (see §6 ratios). White-on-clay send 3.12:1 = the boundary-sanctioned UI-component exception. **Dark-mode error text #B53333 on #262624 card = 2.52:1 — FAIL** (issue 2). Placeholder 3.65:1 and offline label 3.47:1 are sub-AA token-inherited cases (issue 8) |
| 5 | Focus visibility + keyboard operability | **PASS** | `:focus-visible` → computed `solid 2px rgb(20,20,19)` outline on studied-UI buttons; harness radios/switches have focus-visible ring rules; first Tab lands on #btnMenu (studied UI first); Enter submits composer; sheets: 12 Tabs stay contained, Shift+Tab wraps, Esc closes and returns focus to opener |
| 6 | Text scaling (no clipping, no horizontal overflow) | **PARTIAL** | Chat mode: **12/12 combos PASS** (Δx=0 at all 12; composer visible; no clipped composer controls; 400-char URL + verbatim error wrap at 320×200%). Code mode: **8/12 PASS; all four 200% rows FAIL vertical clipping** — `.code-new` footer extends past the viewport bottom (issue 1). Horizontal overflow = 0 everywhere; scroll ownership holds everywhere |
| 7 | Reduced motion | **PASS** | `html.rm` class + radio sync; sheet transitionDuration 0s in reduced (0.2s normal); Esc closes without transition wait; idle `document.getAnimations()` = 0 in both modes (no perpetual/decorative motion); thinking timer is numeric text in both modes; `prefers-reduced-motion` emulation defaults to reduced (html.rm=true, radio pre-selected, 0s) |
| 8 | Overflow & long-string handling | **PASS** | 400-char unbroken URL bubble and 200-char message at 320×200%: conv/studied/viewport Δx=0 (overflow-wrap:anywhere); repo/branch paths ellipsize; diff pane scrolls in place (overflow-x:auto) |
| 9 | Safe-area handling | **PASS** | Overlays toggle on/off, striped, labeled "assumed inset (UNVERIFIED)", pointer-events:none; with overlays on, typed + sent via real pointer clicks successfully; `env()` not used — absence documented via "no One UI safe-area claim" tooltips, caption, and panel; safe-area padding check reports ASSUMED status |
| 10 | Offline self-containment | **PASS** | Zero non-file requests (1 request total = the file:// document); zero console errors; zero page errors; static grep: no src=/href=/url(/@import/fetch(/XMLHttpRequest/WebSocket; **no http(s):// string anywhere in the file** (even citations use bare domains — stricter than the brief minimum); font-substitution note in header |
| 11 | Interaction fidelity (documented behaviors only) | **PASS** | Full battery in §5 — all documented behaviors reproduced exactly (verbatim capacity string byte-identical; remote mode-set enforcement verified; persisting dialogs ignore Esc + scrim); every non-documented control is a labeled stub toast |
| 12 | Structure | **PASS** | Single self-contained HTML file; runs from file://; phone-frame-first (studied UI inside the device viewport; harness header + QA panel outside, labeled "QA / HARNESS CONTROLS — not part of the studied UI") |

## 3. Device-preset results (runtime-measured)

| Preset | Outer frame (px) | Measured H/W | Target aspect | Caption facts + provenance | Punch-hole | Corners | Viewport values reported |
|---|---|---|---|---|---|---|---|
| Galaxy S25 | 378×788 | 2.0847 | 2.084 (Δ0.0007) | 6.2″ · 2340×1080 FHD+ (official) · 146.9×70.5×7.2 mm · 162 g ✓ | present | 28px outer / 16px screen | caption + valuesLine: outer ratio, outer px, viewport 360×780 CSS px ✓ |
| Galaxy S25+ | 377×788 | 2.0902 | 2.090 (Δ0.0002) | 6.7″ · QHD+ class (official) · **3120×1440 = T3-agreed APPROXIMATE** ✓ · 158.4×75.8×7.3 mm · 190 g | present | 28px / 16px | ✓ |
| Galaxy S25 Ultra | 376×788 | 2.0957 | 2.098 (Δ0.0023) | 6.9″ · 3120×1440 QHD+ (official) · 162.8×77.6×8.2 mm · 218 g | present | **12px outer / 8px screen — boxier ✓** | ✓ |

All three captions carry: "outer aspect … (computed from official dims, weight)", "aspect 2.167; 19.5:9 computed — INFERRED", "proportions only: NOT hardware pixels, DPR, or One UI safe areas", "status & gesture strips are assumed insets (UNVERIFIED)". Inner viewport is independently controllable (320–430) and both outer/inner values are reported in the caption and the live values line. Preset switching re-renders frame, corners, and caption correctly at every width. Frame math (FW = round((W×2.167+8)/aspect)) reproduces official mm aspects within ≤0.0024.

## 4. Cross-width × text-scale results matrix

Chat mode (conversation/composer; Δx = horizontal overflow in px; composer V = visible & inside):

| width \ scale | 100% | 130% | 200% |
|---|---|---|---|
| 320 | PASS Δx=0 V✓ | PASS Δx=0 V✓ | PASS Δx=0 V✓ |
| 360 | PASS Δx=0 V✓ | PASS Δx=0 V✓ | PASS Δx=0 V✓ |
| 390 | PASS Δx=0 V✓ | PASS Δx=0 V✓ | PASS Δx=0 V✓ |
| 430 | PASS Δx=0 V✓ | PASS Δx=0 V✓ | PASS Δx=0 V✓ |

Stress at 320×200% (400-char unbroken-URL bubble + 200-char message + armed capacity error): Δx=0; verbatim error string renders and wraps; Retry succeeds → scripted reply.

Code mode (session list + new-session composer; "inside" = `.code-new` fully within viewport):

| width \ scale | 100% | 130% | 200% |
|---|---|---|---|
| 320 | PASS inside (−20px margin) | PASS (scroll area 52.8px) | **FAIL — clipped +465.6px** |
| 360 | PASS | PASS | **FAIL — clipped +256.6px** |
| 390 | PASS | PASS | **FAIL — clipped +191.6px** |
| 430 | PASS | PASS | **FAIL — clipped +104.6px** |

Horizontal overflow Δx = 0 and scroll ownership (session area owns scroll) hold in ALL 24 combos — the failure is purely vertical clipping of the `flex:none` footer (issue 1). Keyboard sim: composer clears the simulated keyboard in Chat (bottom 593 ≤ kb top 609, kb 328px) and Code (600 ≤ 609) modes; overlays stay operable.

## 5. Interaction-fidelity findings (documented-behavior compliance)

| Behavior | Result | Runtime evidence |
|---|---|---|
| Send → thinking timer → reply | PASS | "Thinking · 0s" numeric seconds indicator; scripted dummy reply appears after ~2s; input cleared; arrow hides again; `role=log`/`aria-live=polite` on transcript |
| Capacity-error scenario | PASS | Arming label explicit; rendered string byte-identical to the DOCUMENTED sentence; Retry present with "retry-control visual UNVERIFIED" tag; retry → thinking → reply succeeds |
| Drawer → Code tab | PASS | Drawer = `role=dialog` `aria-modal`; Code entry carries DOCUMENTED chip; note "Drawer contents beyond the Code entry: UNVERIFIED. Chats / Settings entries are INFERRED placeholders."; Code entry switches modes |
| Model sheet | PASS | Models: Opus / Sonnet / **More models**; Effort: Low / Medium / High / Extra high / Max with **"Default" mini-marker on High**; Thinking **"Extended"** checkbox; selection state + check; Sonnet selection updates the composer pill |
| Attachment sheet → chips | PASS | "Add files or photos" (DOCUMENTED wording); Course notes.docx → chip with DOC badge; Results table.pdf → PDF badge; chip removable |
| Rename / Delete | PASS | Rename → stub toast (no invented workflow); Delete → confirm dialog with `persist` class: **ignores Esc (verified) and scrim click (verified)**; Cancel closes; Delete (demo) resets conversation |
| Settings ↔ QA panel color mode | PASS | Studied-UI Settings → Dark flips studied + viewport + QA radio; QA radio → light flips back; "Match System" keeps sheet selection "system", resolves via prefers-color-scheme |
| Code-mode mode dropdown | PASS | Cloud default = [Accept edits, Plan, Auto]; opening the Remote Control session swaps to **[Manual, Accept edits, Plan] — no Bypass, no Auto** (value=manual); returning to the list restores the cloud set; toast explains the enforcement |
| Diff indicator | PASS (with cosmetic glyph note) | s1 row and detail header show "+42 −18"; tag "diff colors UNVERIFIED"; see issue 3 (U+2212 glyph) |
| Permission "Approve" prompt | PASS | Inline card persists (Esc has no effect — inline, not a sheet); Approve → "Approved (demo) — the prompt persisted until answered." |
| New-session composer | PASS | Submit → toast "Session queued (demo) — … DOCUMENTED fields; no real workflow."; task field cleared; no navigation/state change |
| Focus/Esc/containment | PASS | See §2 row 5 |

## 6. Token / contrast findings (as-built vs boundary; computed ratios)

**Tokens (runtime computed styles):** all match the boundary exactly — see §2 row 1. Bubble = token #D1CFC5 (not the measured #d5d5d1–#d7d6cf, which are cited only); radius 20px; max-width 72% (within the 65–75% MEASURED-approx band); card r16 + #E8E6DC hairline; send #D97757 with #C96442 hover/active; code block #262624 r12; error #B53333; dark theme = measured #262624/#3D3D3A/#575755 plus INFERRED-labeled values (canvas #1F1E1D, bubble #30302E, text ramp) with a visible dashed note in dark mode. #C6613F absent from all CSS and rendered UI.

**Computed WCAG ratios (23 pairs; AA text = 4.5:1, UI component = 3:1):**
- PASS (light): ink/canvas **17.50** · secondary/canvas 12.55 · tertiary/canvas **6.26** · tertiary/white 6.59 · ink/bubble 11.80 · ink2/tint 11.38 · error/white **6.02** · error/canvas **5.72** · code-text #FAF9F5/#262624 **14.39** · approved-green/white 5.07 · toast 17.50 · white-arrow/clay **3.12** (icon-only send — boundary-sanctioned UI exception) · white-arrow/clay2 3.90
- PASS (dark, INFERRED set): ink/canvas 15.80 · secondary 10.65 · tertiary/canvas 7.48 · tertiary/card 6.82 · bubble text 12.55 · code text 14.39 · toast 17.50
- **FAIL (dark): error #B53333 on card #262624 = 2.52:1; on canvas #1F1E1D = 2.76:1** (issue 2)
- Sub-AA token-inherited: placeholder #87867F on white pill **3.65:1** (official gray-500 token, brief-specified, transient text); offline label #87867F 10px on canvas **3.47:1** (issue 8)

## 7. Issues found (documented — NOT repaired, per protocol)

1. **[Moderate — defect] Code-mode footer clipped at 200% text scale (all 4 widths).** Location: CSS `.code-head` / `.code-new` / `.code-mode` (~lines 227–275). At 200%: flex-wrapped Code header grows to 448.8px (320w) / 392.8px (360–430w) — the wrapped rows plus the 224px `mode-note` annotation — and `.code-new` (633.8px at 320×200%) extends past the viewport bottom by +465.6 / +256.6 / +191.6 / +104.6px; the session list collapses to 48px; the Queue button and task textarea are unreachable (`.code-mode`/`.studied` are overflow:hidden; `.code-new` is flex:none with no internal scroll). Evidence: t2d matrix + t2b/t2c geometry dumps. Agent 5's own probe checked horizontal overflow + scroll ownership (both still pass — the live checks cannot detect this), so this escaped its verification. Conflicts with brief §6 ("fully understandable and operable … at 200% text scale") for the Code surface. Chat mode is unaffected (12/12).
2. **[Minor — contrast defect, inherited from the brief's INFERRED dark set] Dark-mode error text.** `--err` #B53333 stays unchanged on dark surfaces per brief §5 ("clay/error/blue unchanged"); computed 2.52:1 on the dark error card (2.76:1 on dark canvas) — fails AA and even the 3:1 UI threshold. Reachable: theme=Dark + arm + send. The dark palette is tagged INFERRED, but the contrast consequence itself is unlabeled. Classification: inherited defect (brief-specified), not a builder deviation.
3. **[Cosmetic] Diff indicator glyph substitution.** Rendered as "+42 −18" / "+8 −2" using U+2212 MINUS SIGN (5 occurrences) instead of the DOCUMENTED "+42 -18" ASCII format (code.claude.com wording "like +42 -18"). Format is not a quoted error string, so the verbatim rule is not strictly violated, but the substitution is undocumented.
4. **[Cosmetic] S25+ aspect displays as "2.09".** JS number-to-string drops the trailing zero of 2.090 in the caption/values line. Value is correct (measured 2.0902); display formatting only.
5. **[Cosmetic] Caption font sizes below the brief's scale.** `.mode-note`/`.code-note` at .625rem = 10px vs brief §5 "12 caption" (6.25% under spec); research tag chips at 9px are a documented px-fixed annotation convention.
6. **[Observation] Placeholder & offline-label contrast.** Placeholder #87867F on white = 3.65:1 — official token (gray-500), brief-specified, transient; acceptable but worth a known-limitation note. Offline label uses the same token at 10px (3.47:1) — an INFERRED visual choice of the session list.
7. **[Acceptable deviation — documented by Agent 5]** (a) evidence tag chips are px-fixed research annotations (documented in the panel); (b) sources cited as bare domains/paths rather than full URLs (documented; traceable via the source register — my boundary §5 asked for "source URL", the panel documents the domain/path convention); (c) GREEN per-element provenance via `data-evidence`/title tooltips (hover) rather than a tap/hold evidence-mode overlay; (d) "Match System" resolves via prefers-color-scheme; (e) extra "Load sample conversation" harness trigger; (f) sheet ✕ close buttons; (g) single mode `<select>` swapping cloud/remote option sets. None contradict the boundary.
8. **[Observation] Verified non-issues.** Long strings wrap (Δx=0 under stress); no perpetual animations (`getAnimations()=0` idle in both motion modes); zero network activity; no proprietary logos (spark = 4-bar CSS asterisk labeled "drawing approximate"; "Claude" drawer text is a plain sans wordmark with an explicit "not a logo" tag); no hardware-fidelity claims (all DPR/One UI/haptics mentions are negative disclaimers); volatile store facts absent.

## 8. Verdict

**The prototype COMPLIES with the phase-1 evidence boundary.** GREEN items are represented with computed-style-exact official tokens (17 measured values all exact, including pressed-state #C96442 semantics); measured approximations appear only inside the evidence layer as citations. YELLOW items are represented only with visible tags — 22 tag instances in the studied UI (identical in both themes) plus inset/dark-palette notes — and the evidence panel enumerates label + source per element. RED items are entirely absent (grep-verified: every sensitive term occurs only inside the exclusion list). Documented behaviors are reproduced faithfully (verbatim strings byte-checked against staged T1 articles; remote-mode enforcement exact; persisting dialogs behave as documented).

Quality caveats (not boundary violations): 1 moderate layout defect (Code-mode 200% text-scale clipping, §7 issue 1), 1 minor inherited contrast defect (dark-mode error text, issue 2), plus cosmetic items (issues 3–5). Recommend (for a future revision, not performed here): make `.code-new` scrollable or cap `.code-head` growth at large text scales; revisit the dark error-text token or label its contrast consequence; normalize the diff-indicator minus glyph to ASCII.

**Checklist score: 9 PASS / 2 PARTIAL (checks 4, 6) / 1 FAIL-equivalent sub-item within check 6 — boundary compliance: PASS.**

## 9. Appendix — selected raw runtime evidence

```
preset s25  outer 378×788px  H/W=2.0847 (target 2.084, Δ0.0007)  punch ✓  corners 28px/16px
preset s25p outer 377×788px  H/W=2.0902 (target 2.090, Δ0.0002)  punch ✓  corners 28px/16px
preset s25u outer 376×788px  H/W=2.0957 (target 2.098, Δ0.0023)  punch ✓  corners 12px/8px
valuesLine: "frame: Galaxy S25 Ultra · outer ratio 2.098 · outer 376×788 px · viewport 360×780 CSS px · text scale 100% · theme light · mode chat"

LIGHT computed: canvas rgb(250,249,245) | bubble rgb(209,207,197) r20px maxW72% | card rgb(255,255,255) r16px
               border rgb(232,230,220)/1px | code rgb(38,38,36) r12px | send rgb(217,119,87) r50%
               arrow rgb(255,255,255) | ink rgb(20,20,19) | tertiary rgb(94,93,89) | placeholder rgb(135,134,127)
send :hover = rgb(201,100,66)  (= #C96442 clay-interactive ✓)
DARK computed:  canvas rgb(31,30,29) | card rgb(38,38,36) | tint rgb(61,61,58) | bubble rgb(48,48,46)
               ink rgb(250,249,245) | secondary rgb(209,207,197) | tertiary rgb(176,174,165) | send unchanged

chat matrix (12 combos): convΔx=0 studiedΔx=0 vpΔx=0 docΔx=0 composerVisible=true clipped=[] — 12/12 PASS
stress 320×200% (400-char URL + capacity error): Δx=0 · verbatim string exact · Retry → reply PASS
code matrix: 100%/130% rows PASS; 200% rows clipped +465.6 / +256.6 / +191.6 / +104.6 px (320/360/390/430)
keyboard sim: chat composer bottom 593 ≤ kb top 609 (kb 328px) PASS; code new-session 600 ≤ 609 PASS
safe-area: "assumed inset (UNVERIFIED)" stripes, pointer-events=none; typed+sent with overlays on PASS
motion: normal sheet transition 0.2s; reduced 0s; Esc close <80ms in reduced; getAnimations()=0 both modes
prefers-reduced-motion emulation → html.rm=true, radio pre-checked, sheet transition 0s (default honored)
offline: total requests 1 (the file:// document); non-file requests 0; console errors 0; page errors 0

interactions: thinking "Thinking · 0s" numeric ✓ | capacity string byte-identical ✓ | retry→reply ✓
drawer role=dialog aria-modal ✓ | models [Opus,Sonnet,More models] ✓ | efforts L/M/H[Default]/XH/Max ✓
Thinking "Extended" checkbox ✓ | attachment chips DOC/PDF ✓ | delete-confirm ignores Esc+scrim ✓
cloud options [Accept edits,Plan,Auto] ✓ | remote options [Manual,Accept edits,Plan] (no Bypass/Auto) ✓
queue toast "Session queued (demo)…" ✓ | approve persists → "Approved (demo)…" ✓
focus: outline solid 2px rgb(20,20,19) ✓ | 12 Tabs contained in sheet ✓ | Shift+Tab wraps ✓ | Esc → opener ✓
aria: 6 role=dialog(modal) sheets · 8 radiogroups · live regions conv:polite + frameCaption:polite · 30 aria-labels
empty state: greeting "What are you thinking?" serif 30px · spark 4 CSS bars (8-ray) tagged "drawing approximate"
            · send arrow visibility:hidden · placeholder "Chat with Claude"
tags: 22 visible tag/tag-block instances (light) · 22 (dark) · + 2 strip "inset UNVERIFIED" dtags
```

*End of QA report — Agent 4, Task ID 6. Review-only protocol observed: no file other than this report and the Task 6 worklog entry was created or modified; temporary Playwright runners were deleted after use.*

