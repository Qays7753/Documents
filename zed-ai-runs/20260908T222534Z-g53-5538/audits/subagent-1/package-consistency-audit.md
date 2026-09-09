# Package & Token Consistency Audit — Subagent 1 (Task R4-a)

**Target:** `repos/Documents/zed-ai-runs/20260908T201936Z-g53-252a/visual-foundation-package/` (29 files)
**Source pack (read-only truth):** `repos/Documents/accounting-visual-foundation-source-pack-v1/`
**Date:** 2026-09-09 · **Agent:** Subagent 1 — Package and Token Consistency Auditor
**Machine-readable companion:** `package-consistency-audit.json` (same directory)

---

## 1. Methodology

1. Read the source pack's token evidence in full: `source-reference/source-tokens.json` (68 canonical hex + 5 warm-shadow rgba), `tailwind.config.source.js`, `index.css.source`, `SOP_VISUAL_ONLY.md`, `source-reference/SOURCE_AUDIT_NOTES.md`.
2. Read all **29 package files end-to-end** (23 markdown, `design-tokens.json`, `coverage-matrix.json`, `design-tokens.css`, `component-gallery.css/html/js`).
3. **Scripted CSS↔JSON parity** (`audits/subagent-1/audit_tool.py`): all 170 custom properties in `design-tokens.css` vs all 148 token records in `design-tokens.json`, `var()` references resolved one level deep; values, roles, and classification tags compared.
4. **Scripted WCAG 2.1 recomputation** of every ratio claimed in the evidence panel (`component-gallery.html:640-659`), `color-system.md`, `accessibility.md`, CSS comments and JSON usage fields — 33 claimed pairs + 14 additional implemented pairs — cross-checked against the run's own `scripts/sub3-contrast.py` and `agents/sub3/contrast-results.json` (both executed read-only).
5. **Motion matrix** built from the REQUIRED TIMING SYSTEM vs the token block, the docs, the actual transition/animation declarations in the gallery CSS, the JS timers, and the computed/behavior captures.
6. **Prohibited-value scan** across all 29 files: off-ramp hexes, rgba, remote URLs, emoji, TODO/TBD/FIXME/lorem, sub-12px font sizes.
7. **Rendered-vs-documented:** all 25 capture files in `audits/captures/` cross-checked against documented claims, plus a scripted class-usage cross-check (HTML/JS classes vs selectors in both CSS files).
8. **Structure check:** 29-file contract, flat layout, filename map, extra artifacts; the repos copy was diffed against the `download/` copy (identical).

Every finding cites file + line (or capture + value). One inference is explicitly labeled: the FAB/nav overlap in S1-14 is CSS arithmetic, not visual confirmation.

---

## 2. Headline results

| Check | Result |
|---|---|
| 29-file contract (exact count, names, flat, no extras, >200 B) | **PASS** — download copy byte-identical |
| Token value parity (170 CSS props ↔ 148 JSON records, var() resolved) | **PASS — 0 value mismatches** (2 font records are prose, not literal stacks) |
| Classification tag parity (CSS comment tags vs JSON classifications) | 6 records drift (S1-11) |
| Consumed-token documentation (every `var()` used by the gallery is defined + documented) | **PASS** |
| Contrast claims recomputed | **32/33 exact; 1 wrong** (8.39 → 8.55, S1-06) |
| Required color roles (700/600 text-bearing fills, no #CC785C+white text, E1/E2/E3) | **PASS** — rendered and captured |
| Required geometry (48/12/600 buttons, 36/44 chips, radii 12/16/20, FAB 56) | **PASS** (icon-size and FAB-offset doc drift, S1-08/S1-14) |
| REQUIRED TIMING SYSTEM | **FAIL — 0 of 8 values implemented** (S1-01) |
| Documented overlay motion actually running | **FAIL — none implemented** (S1-02) |
| Prohibited values | **Clean** (one 10px chrome font hit, S1-17; no emoji-icons, no gradients, no off-palette code colors, no remote resources, no placeholders) |
| Coverage-matrix / state-matrix claims vs DOM | **8 claims mark nonexistent states as ✅/verified** (S1-04) |

---

## 3. Findings by severity

Severity counts: **2 blockers · 3 majors · 21 minors · 9 notes** (full records with evidence, criterion, and recommendation in the JSON).

### 3.1 Blockers

| ID | Area | Finding (short) |
|---|---|---|
| **S1-01** | tokens | **REQUIRED TIMING SYSTEM implemented nowhere.** `design-tokens.css:184-192`: press 120ms (req 80), fast 200ms (req 120), base/normal 300ms (req 200), sheet single 340ms token (req 240 in / 180 out); **no dialog-in (160), dialog-out (120), or scrim-duration tokens exist**. All six running transitions use the divergent values (gallery css 126/191/260/292/300/448; `computed-tokens.txt` 120/200/300/340). Values are source-inherited (`index.css.source:51`, `tailwind.config.source.js:204-210`, `BottomSheet.jsx:150`) but diverge from run authority. → Retokenize to the 8 required values and retime every consumer. |
| **S1-02** | gallery | **All documented overlay motion is claimed but never implemented.** `.scrim` (css:464-468), `.sheet` (:469-477), `.dialog` (:503-509), `.snackbar` (:518-531) have no transition/animation; JS only toggles `hidden` (js:171-188, 224-232); keyframes `slideUp/slideDown/fadeIn/scaleIn/snackbarIn/ghostOut` are defined (`design-tokens.css:293-300`) and referenced by **zero** rules; `--motion-sheet` and `--snackbar-duration` are never consumed. Claims live in `motion-interaction.md:34`, `overlay-system.md:16,24,28,36`, `component-contracts.md:89`, `visual-direction.md:17`, and the evidence panel (html:702-713). Captures show instant flips. → Implement the required durations (keyframes already exist) or retract the claims in all six documents. |

### 3.2 Majors

| ID | Area | Finding (short) |
|---|---|---|
| **S1-03** | docs | **Sheet-drag claims contradict the code and the package's own self-critique.** `motion-interaction.md:38` ("preserves the geometry and motion exactly"), `overlay-system.md:11,17,44` ("snap points 84/94vh", "live drag-handle affordance", "expanded snap"), `component-states.md:28` ("✅ open + expanded snap") vs no drag handlers in JS, static `max-height: 84%` (css:474), and `self-critique.md:18` which truthfully admits drag is not interactive. → Align the two docs with self-critique or implement drag. |
| **S1-04** | coverage | **Eight documented states don't exist in the DOM.** `coverage-matrix.json:105` marks "dialog destructive confirmation" as **verified-both** (only the non-destructive "Confirm summary?" dialog exists, html:503-510); `component-states.md:14` ✅ search trailing spinner (none, html:181-187); `:24` ✅ row error variant (none, html:372-416); `:31` ✅ snackbar error variant (all messages success/info, js:233-306); `:28` ✅ sheet expanded snap; `navigation-shell.md:38` "large-title subheader" (never rendered; `--topbar-height-large` unused) and "all five destinations" (gallery has **4** nav items, html:445-462); `responsive-geometry.md:22` "5-segment segmented control ... the gallery renders them" (gallery has **3** segments, html:281-286). → Fix the ✅/verified statuses to "specified" and correct the counts, or add the demos. |
| **S1-05** | gallery | **Gallery header controls are unstyled.** `component-gallery.html:60,70,77,84` use `class="seg seg-sm"` for the viewport/direction/text/motion controls; **no `.seg`/`.seg-sm` selector exists in either CSS file** — the controls render as native buttons in every screenshot (they still *work*, per the a11y captures). Dead classes: `has-lead` (html:184), `sheet-close` (html:492). → Add the small chrome pill style; remove dead classes. |

### 3.3 Minors (21)

| ID | Area | Finding (short) |
|---|---|---|
| S1-06 | docs | `accessibility.md:15` white/primary.800 = **8.39**; recomputed **8.55** (the run's own sub3 script and archive agree on 8.55). Only wrong ratio found; all other 32 claims exact. |
| S1-07 | docs | Input focus transition documented **150ms** (`input-system.md:22`, `component-contracts.md:25`) but implemented **200ms** (`--motion-fast`, css:191); `motion-interaction.md:12` says 200ms — docs contradict each other. |
| S1-08 | gallery | Nav icons documented **24px** (`navigation-shell.md:20-21`, `iconography.md:14`) but rendered **20px** (`.ic` default; no 24px rule). FAB icon is correctly 24px. |
| S1-09 | docs | Icon count claimed **26** in five docs (`iconography.md:20` lists 27 names, `decision-log` D-29, `self-critique:19`, `coverage-matrix:124`, `component-contracts:100`); sprite has **34** symbols; grid renders **24**. |
| S1-10 | gallery | Press scale inconsistent: 0.97 (btn/chip/FAB via `.press`) vs **0.95** no-transition (`clear-btn`, `navitem`, `snackbar-action`, css:221/457/531); `motion-interaction.md:24` "Every tappable surface uses .press — 0.97" is false for those three. |
| S1-11 | tokens | Classification-tag drift: CSS `[corrected role]` on primary.700 vs JSON "inherited" (css:23 / json:85-90); CSS `[corrected]` on ink-secondary vs JSON "normalized" (css:116); JSON-corrected operational.600, gold.700, positive-on-tint, gold-ink untagged in CSS. Values themselves: 0 mismatches. |
| S1-12 | docs | Snackbar action documented **14px/700** (`overlay-system.md:36`) but implemented **13px label token** (css:528) — the doc violates the package's own 14→13 mapping (typography.md:39). |
| S1-13 | gallery | Dialog documented "centered" (`overlay-system.md:24`, `surface-system.md:30`, `component-contracts.md:89`) but implemented top-anchored at **24%** (css:504), horizontally centered only. |
| S1-14 | gallery | FAB offset documented/tokenized **80px** (nav-shell:30, spacing:31, evidence panel; `--fab-offset` css:165) but the demo FAB is anchored **20px** above its wrapper bottom (css:425) — by CSS arithmetic it overlaps the bottom-nav band; `--fab-offset` is never consumed. (Inference from CSS math; verify visually.) |
| S1-15 | docs | Empty-state "48px vertical breathing" (`empty-loading-error-states.md:13`) vs implemented **32px** padding (css:536). |
| S1-16 | docs | Snackbar spec "fixed, 96px above nav" (`overlay-system.md:36`) vs gallery "absolute, 24px above frame bottom" (css:519) — approximation undocumented. |
| S1-17 | gallery | Evidence-panel ramp labels at **10px** (css:597) — the only sub-12px font in the package; violates the "absolute 12px floor" (typography.md:45, accessibility.md:58). Chrome-only. |
| S1-18 | docs | Icon-floor contradiction: `iconography.md:16,40` "no sub-20px icons" vs `component-contracts.md:53` / `data-display-system.md:25` specifying **12px badge icons / 6px dots** (implemented as `.ic-dot`, css:112). |
| S1-19 | gallery | A11y attributes claimed in contracts but absent from the DOM: **aria-busy** (loading button), **aria-pressed** (chips), **aria-current** (active nav) — `component-contracts.md:15,37,85` vs 0 occurrences in html/js. |
| S1-20 | coverage | Dead-in-gallery tokens (defined + documented, never rendered): `--motion-sheet`, `--snackbar-duration` (JS hardcodes 5000, js:231), `--fab-offset`, `--topbar-height-large`, `--space-nav-pill` (raw 52px at css:446), `--row-height-min` (raw 56px), `--touch-target`, `--actionbar-height`, `--z-header`, `--z-content`, the whole `--space-1..7` scale (raw px used — values agree), `--text-title-*` (28px role never rendered), `--color-status-*`. |
| S1-21 | gallery | Menu "closes on outside touch or Escape" (`overlay-system.md:28`) — **not implemented**: the Escape handler only closes sheet/dialog (js:207-220); no outside-click close. |
| S1-22 | docs | KPI number documented "in a state color" + "▲ glyph" (`data-display-system.md:21`) but rendered in **ink** with an SVG trend icon (css:334, html:337). |
| S1-23 | docs | Header "icon-expand search pattern" claimed as a gallery demonstration (`input-system.md:12,43`) — not implemented (top bar has static icon buttons only). |
| S1-24 | docs | Underline segmented control documented "2px divider + 4px primary indicator" and "slides 300ms" (`component-contracts.md:42,47`) vs implemented **1px container divider + 2px primary underline, no transition** (css:303,309-311). |
| S1-25 | docs | Skeleton row documented as "44px tile + two lines + trailing amount block" (`empty-loading-error-states.md:19`) vs flat 56px strips (css:557). |
| S1-26 | tokens | `font.sans`/`font.mono` JSON values are prose and omit fallback entries (`-apple-system`, generic families) vs the literal CSS stacks — the only JSON records not machine-consumable as values. |

### 3.4 Notes (9)

| ID | Area | Finding (short) |
|---|---|---|
| S1-27 | structure | 29-file contract **PASS**: exact count/names, flat, no extras, all >200 B, download copy identical, credential scan clean. |
| S1-28 | tokens | Value parity + consumed-token documentation **PASS**; the verification report's "148 ↔ 170 (triads resolve), zero value mismatches" claim is independently reproduced (11 type records = 33 props; 148 + 22 = 170). |
| S1-29 | coverage | The five headline contrast corrections are real and rendered (button #964E33, secondary #057B7C, gold #644D1C/#F6ECCF, operational #3E5C76, nav active #964E33); **#CC785C never pairs with white button text** (only meta theme-color + ramp docs). Geometry fundamentals verified in captures (48px/12px/600, 36/44 chips, E1–E3 byte-identical, radii, FAB 56). |
| S1-30 | docs | gold.500 non-text ratio cited 3.36:1 for "white/canvas"; on canvas it is **3.19:1** (still ≥3:1). |
| S1-31 | docs | Two motion values exist only in prose/code: sheet height snap **320ms** (documented, no token — source `BottomSheet.jsx:150`) and spinner **0.8s** (implemented, undocumented). |
| S1-32 | docs | Header veil `rgba(250,249,245,0.88)` + `blur(12px)` (css:24-26, 407-409) vs the prohibited "glassmorphism" — the package documents it as the system's single blur exception (surface-system.md:42); the run's prohibition has no stated exception. **Coordinator decision required.** |
| S1-33 | tokens | Destructive fill = negative.500 `#C9322A` (inherited, D-03, 5.29:1) while the required system names "negative main `#B42318`" (used by the package as text/icon role). Whether filled destructive actions should move to #B42318 is a **coordinator decision** (both pass AA). |
| S1-34 | gallery | Prohibited scan clean: no placeholders, no emoji-as-icons (only ✅/❌ in doc tables, ↔ in an evidence note), no gradients, no neon/colored shadows, no count-up, no springs, no page slides, no off-palette colors in code, zero remote resources (network capture `[]`; the two "URL" matches are the SVG xmlns and the data-URI check glyph). Benign residue: untokenized `rgba(255,255,255,.35)` spinner border, raw `#FFFFFF`s (in-palette), JS RAMPS hardcode 60 in-ramp hexes (evidence chrome, values verified). |
| S1-35 | docs | Small prose inaccuracies: badges "every pairing carries an icon or dot" (third badge row is text-only, html:316-320); buttons prose repeats "0.97 press"; README "148 tokens as custom properties" elides the 170-prop/148-record split. |

---

## 4. Motion matrix (required vs documented vs implemented)

| Use | Required | Documented | Implemented | Verdict |
|---|---|---|---|---|
| press | **80ms** | 120ms (motion-interaction.md:11; button-system.md:28; evidence panel html:705) | 120ms (`--motion-press`; css:126; computed-tokens.txt) | **divergent** |
| fast | **120ms** | 200ms (motion-interaction.md:12; 150ms in input-system.md:22 — contradiction) | 200ms (`--motion-fast`; input/chip) | **divergent** |
| normal | **200ms** | 300ms "base" (motion-interaction.md:13) | 300ms (thumb/segment/navpill) | **divergent** |
| sheet-in | **240ms** | 340ms (motion-interaction.md:14; overlay-system.md:16; evidence panel) | **none** — `.sheet` has no motion; `--motion-sheet` never consumed | **divergent + claimed-not-implemented** |
| sheet-out | **180ms** | 340ms (motion-interaction.md:34) | **none** — instant hide | **divergent + claimed-not-implemented** |
| dialog-in | **160ms** | 200ms scaleIn (overlay-system.md:24; motion-interaction.md:34) | **none** — `.dialog` has no motion; scaleIn keyframes unused | **divergent + claimed-not-implemented** |
| dialog-out | **120ms** | 200ms fade+scale (motion-interaction.md:34) | **none** | **divergent + claimed-not-implemented** |
| scrim | **200ms** | 200ms fade (motion-interaction.md:12,34; overlay-system.md:16) | **none** — `.scrim` has no transition; no token | **claimed-not-implemented** (value matches, fade never runs) |
| snackbar-in | — | 300ms slide+fade (motion-interaction.md:34; overlay-system.md:36) | **none** — snackbarIn keyframes unused | **claimed-not-implemented** |
| snackbar-out | — | 300ms + 250ms exit delay | **none** — instant hide at 5000ms | **claimed-not-implemented** |
| menu open/close | — | 200ms fade/scale + outside/Escape close (overlay-system.md:28) | **none** + no outside/Escape close | **claimed-not-implemented** |
| sheet height snap | — | 320ms (overlay-system.md:16; no token) | **none** | **claimed-not-implemented** |
| ghost-out collapse | — | 300ms (motion-interaction.md:13; component-contracts.md:67) | **none** — ghostOut keyframes unused | **claimed-not-implemented** |
| underline slide | — | 300ms (component-contracts.md:47) | **none** — no transition | **claimed-not-implemented** |
| skeleton pulse | — | 1.5s infinite | 1.5s (css:552) | **pass** |
| snackbar hold | — | 5000ms | 5000ms (js:231, raw; token unconsumed; capture-verified) | **pass** |
| thumb/nav/chip | — (maps to normal 200ms) | 300/300/200 | 300/300/200 | **pass vs package docs** (300ms diverges from required normal) |
| reduced-motion | — | kill-switch both modes | implemented (css:275-290; capture 07) | **pass** |

**Summary:** 0/8 required values implemented; 4 of them are "divergent + claimed-not-implemented"; 6 more documented motion behaviors never run. Only skeleton, snackbar-hold, intra-control transitions and the reduced-motion switch actually execute.

---

## 5. Token parity result

- **CSS custom properties: 170** · **JSON token records: 148** · **Value mismatches: 0** (after one-level `var()` resolution).
- The 148↔170 relationship is the documented triad design: 11 typography records expand to 33 `--text-*-size/line/weight` props (148 + 22 = 170). The verification report's parity claim (`verification-report.md:39`) is reproduced exactly.
- `mismatches` (2, representational only): `font.sans` and `font.mono` — JSON stores prose descriptions that omit `-apple-system` and the generic families; the literal stacks live only in CSS/typography.md.
- `css_only`: none orphaned (triad sub-fields are covered by parent records). `json_only`: none.
- Classification summary in JSON (69 inherited / 74 normalized / 5 corrected = 148) is internally consistent; **6 records' classification tags drift between CSS comments and JSON** (S1-11).

---

## 6. Prohibited-value scan result

| Scan | Result |
|---|---|
| Hex outside source ramps | **0 in rendered code** (gallery css/html/js + design-tokens.css). Off-palette hexes appear only inside deprecated/forbidden documentation sections of design-tokens.json, source-inventory.md, color-system.md, decision-log.md (all with explicit "deprecated/forbidden" framing) — acceptable documentation, not misuse. |
| rgba values | All shadow alphas match the source set `rgba(60,50,40,.04/.06/.10/.16)`; scrim and header veil tokenized as in source. One untokenized new alpha: `rgba(255,255,255,.35)` spinner border (css:174) — white-based, no new hue (note). |
| Raw px fonts < 12px | **1 hit**: 10px evidence-panel ramp labels (css:597) — chrome only (S1-17). |
| Remote URLs | **0 fetchable** — the only matches are the SVG `xmlns` namespace, a `data:` URI check glyph, and provenance text in verification-report.md; `network-remote-resources.txt = []`; console/page-error captures empty. |
| Emoji as icons | **0 in code** (✅/❌ in markdown tables and one ↔ in an evidence note are typographic documentation, not UI icons). |
| TODO/TBD/FIXME/lorem | **0 across all 29 files.** |
| Gradients / neon / glow / colored shadows / count-up / springs / page slides | **0** (all shadows warm `rgba(60,50,40,α)`; easings standard; JS has no number animation). |
| Glassmorphism | `backdrop-filter: blur(12px)` in 2 places (gallery header chrome + `.topbar-scrolled`), inherited from source and documented as the single veil exception — flagged for coordinator ratification (S1-32). |

---

## 7. Top recommendations (repair order)

1. **Retokenize motion to the required system** (S1-01): press 80 / fast 120 / normal 200 / sheet-in 240 / sheet-out 180 / dialog-in 160 / dialog-out 120 / scrim 200, then retime the six gallery transitions. This single change touches `design-tokens.css`, `design-tokens.json`, `motion-interaction.md`, `button-system.md`, `component-contracts.md`, `input-system.md`, and the evidence panel.
2. **Decide implement-vs-retract for overlay motion** (S1-02): the keyframes already exist in `design-tokens.css`; wiring `.sheet/.dialog/.scrim/.snackbar` to the new tokens closes six documents' false claims at once. If not implemented, retract the claims everywhere including the evidence panel.
3. **Fix the false verification claims** (S1-04): coverage-matrix "verified-both" → "specified" for the destructive dialog, search spinner, row/snackbar error variants, sheet snap; correct 4-vs-5 destinations, 3-vs-5 segments; drop or add the large-title demo.
4. **Style the gallery header controls** (S1-05): add `.seg/.seg-sm` chrome styling; delete `has-lead`/`sheet-close`.
5. **Align the drag documentation with self-critique** (S1-03) and sweep the small doc-value errors (S1-06 8.39→8.55; S1-07 150→200; S1-12 14→13; S1-15 48→32; S1-16/S1-13/S1-14 offset/centering wording; S1-09 icon counts; S1-24/S1-25 anatomy values).
6. **Make the cheap contract truths real** (S1-19): aria-busy / aria-pressed / aria-current are one-line JS additions; consume the dead tokens where raw values already equal them (S1-20).
7. **Preserve the verified strengths** (S1-27/28/29): values, contrast table (minus one number), structure, and offline behavior are solid — repair should not disturb them.

---

## 8. Unresolved / needs-coordinator-decision

1. **Overlay motion policy** (S1-01/S1-02/S1-31): implement the required 8-value timing system in the gallery, or keep inherited source timings and re-scope the docs? This decision unblocks three documents, six dead keyframes, the evidence panel, and the timing tokens themselves.
2. **Glassmorphism exception** (S1-32): ratify the documented single scrolled-header veil (source-inherited `PageHeader.jsx:107-110`) against the run's blanket glassmorphism prohibition, or replace with an opaque header. The gallery-header blur (chrome) can go opaque at zero cost.
3. **Destructive fill step** (S1-33): keep inherited `negative.500 #C9322A` for filled destructive actions, or move to the required "main" `#B42318` (both pass AA; the required wording names only the "main" role).
4. **Canonical small values** (S1-08/S1-09/S1-10): choose 20 vs 24px nav icons, the real icon counts (34 sprite / 24 grid vs "26"), and 0.97 vs 0.95 press scale — then fix docs or code to match once, instead of piecemeal.
5. **Sheet drag** (S1-03): specify-only (self-critique position) or implement drag in the gallery?
6. **Dialog placement** (S1-13): "centered" contract vs the implemented 24% top anchor — pick one.

---

*End of report. Machine-readable findings: `package-consistency-audit.json` · throwaway tooling: `audit_tool.py`, `tool-output.json` (both confined to `audits/subagent-1/`).*
