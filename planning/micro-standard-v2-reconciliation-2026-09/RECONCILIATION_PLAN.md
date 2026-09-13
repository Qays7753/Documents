# Reconciliation Plan — Micro Standard v2 Reconciliation Run

**Run:** run-20260914-msv2-reconciliation-01 · branch `micro-standard-v2-reconciliation-final-20260914`.
**Date:** 2026-09-14 (Asia/Amman). **Phase:** 1 — design only; no package edit has occurred yet at the time this plan was first written.
**Inputs:** OWNER_UNIFIED_DECISION_REGISTER.md (U-01…U-20) · REFERENCE_ZAI_FLASH_REPORT.md (primary baseline) · REFERENCE_ZAI_5_3_REPORT.md (cross-check) · the five agent reports in `AGENT_REPORTS/` · the 31 baseline files at Documents/main `864263c`.

## 0. Governing statement

**No Micro-specific product semantics are being added.** Every change below is a general-purpose, reusable visual/interaction contract traceable to the unified decision register. No new color value, timing value, or geometry value is introduced. The 18 approved hex values and 2 disclosed alpha derivatives remain the complete color universe. Micro routes, Micro state words, Micro navigation labels, financial formulas, dark mode, and AI/LLM/chat features remain excluded. Prototype v0 content is not used.

## 1. Conflict resolutions recorded (per the brief: never silently)

| # | Conflict | Resolution | Basis |
|---|---|---|---|
| CF-1 | Agent 1 "state tags can be classified as 12px metadata (no change)" vs Agent 3 "state words are labels → 13px" | **Agent 3 upheld.** State words and nav/segment labels move to 13px. | typography.md's own table assigns "field labels, chips" to the 13px label step; state words are chip-like labels, not metadata. Register U-04. |
| CF-2 | Route-transition timing: Micro uses 260ms; recording it would extend the closed motion basis (Agent 1 caution; Agent 3 condition) | **Bind route transitions to the existing `--motion-normal` 200ms.** Micro's 260ms is not adopted. | Both agents agree; no new timing value rule. |
| CF-3 | Agent 1 "smallest safe set = 13 files, gallery untouched" vs Agent 3/5 "proven gallery contradictions must be fixed" | **Gallery CSS fixed (proven defect class); accessibility.md + color-system.md gain the surface-specific application rule.** Set grows to 17 files. | The Final-City success definition requires internal consistency; the deviations are proven by computed contrast and by the gallery's own comment contradicting its values. The brief permits fixes where "a direct contradiction is proven and documented." |
| CF-4 | Agent 4 substitutes «أضِف قيمة» for the Standard's documented «سجّله» void-chip example in Prototype v1 | **Prototype uses the Standard's own documented example words («سجّله», «غير متاح») and Agent 2's neutral knowledge-state words.** Micro's FAB label «سجّل» (no pronoun) remains forbidden. | The prototype validates the Standard's own contracts; the Standard's example words are the vocabulary under validation. «سجّله» is the package's recorded example (component-contracts.md), not Micro copy. |
| CF-5 | Agent 2 flags U-18 (skeleton-optional) has no home among the brief's ten additions | **One-line rider added to empty-loading-error-states.md**, scoped so the chart loading contract (data-display-system.md, untouched) keeps its recorded skeleton basis. | Register U-18's "ما يدخل الـ29" column explicitly approves this clarification. |

## 2. Planned changes

Legend: GP = general-purpose (reusable across products). All changes are GP unless noted. Baseline SHA-256 values for rollback are in `PRE_FLIGHT_REPORT.md` §3.

---

### C-01 · Knowledge-state presentation contract → `component-states.md`
**Register basis:** U-05, U-11 (and U-20 boundary). **Agents:** 1 (new section), 2 (neutral words, firewall), 3 (conditions), 5 (boundary sentence + marker choice).
**Current wording:** the file has only the outcome matrix (draft…unknown) and interactive states. No knowledge tier exists. `unknown` today means *result*-unknown («غير معروف» — the system cannot confirm what happened).
**Proposed addition** (new section between "State presentation matrix" and "Interactive states"):

> ## Knowledge-state presentation (information quality)
>
> Knowledge states qualify *how well the information itself is known* — they are orthogonal to the outcome matrix above: an entry can carry any outcome state and any knowledge state at once. They never bind Success or Error colors, never render as success/failure, and never collapse into the honest voids (unrecorded → action chip; unavailable → its word; measured zero → "0" — see `component-contracts.md`).
>
> | Knowledge state | Word (example) | Marker (non-color) | Tone binding |
> |---|---|---|---|
> | confirmed / known | «مؤكد» | check | default ink; no qualifier needed when simply known |
> | unconfirmed | «غير مؤكد» | question-mark marker | neutral ink word + marker; never Success/Error |
> | incomplete | «غير مكتمل» | half-filled shape | neutral ink word + marker |
> | needs-review | «بحاجة لمراجعة» | eye marker | neutral ink word + marker |
> | estimated | «تقديري» | tilde (~) approximate marker | neutral ink word + marker; the value itself still renders at its normal size |
> | unknown magnitude | «غير معروف» | question/info marker on neutral ink | same word family as result-unknown, distinct from failure |
>
> Rules: words always render in a text-safe ink; markers carry the non-color signal; tone is neutral (ink-secondary/tertiary or the neutral tint ground) — a knowledge state is not an outcome and must not borrow outcome colors. Words shown are examples and remain product-owned. A knowledge qualifier never shrinks a financial value: an estimated amount still renders at its contractual size (≥15px mono when it is a financial fact), with the knowledge word as a qualifier beside it. Knowledge-unknown (the magnitude is not known) is distinct from result-unknown (the system cannot confirm what happened) and from the honest voids.

**Reason/evidence:** Flash GAP-35/D-11; register U-11 ("تعديل component-states.md وcomponent-contracts.md بإضافة presentation contract فقط"); Agent 2's neutral-word firewall (Micro greps: «بحاجة لمراجعة» 0 collisions; «غير مؤكد» 4/3, «غير مكتمل» 8/6, «تقديري» 37/24 prose hits — flagged as example-only words, none is Micro canonical vocabulary); Agent 3's text-safe-ink condition. **GP: yes** (presentation grammar only). **Dependency:** none. **Rollback:** restore `component-states.md` baseline hash.

### C-02 · Knowledge-state pointer → `component-contracts.md` (one sentence)
**Current:** L28 ends the honest-voids paragraph: "A void is never styled as success, failure, or decoration."
**Proposed:** append one sentence: "Information-quality qualifiers (unconfirmed, incomplete, needs-review, estimated, unknown magnitude) follow the knowledge-state presentation contract in `component-states.md` and never replace a void with an invented value."
**Reason:** cross-file consistency; Agent 1's pointer recommendation. **GP: yes.** **Rollback:** baseline hash.

### C-03 · Operational-row marker clarification → `component-contracts.md`
**Current (L36):** "…an optional state slot (one word + marker)… An optional state edge stripe (≤3px, the state's semantic color) may mark the row's inline-start edge — always paired with the state word in the row. Rows keep inset dividers and never rely on the stripe alone."
**Proposed:** no rewrite of the existing rule (Agent 1: already covered — redo risk). Append one clarifying sentence: "When a row shows a state, the word plus its non-color marker are the primary signal; the stripe and any hue are reinforcement only, and the stripe hue must meet the 3:1 non-text minimum against the row's actual background (see the surface-specific bindings in `accessibility.md`)."
**Reason:** Agent 3 condition (stripe ≥3:1 vs actual background) + Agent 5 endorsement. **GP: yes.** **Rollback:** baseline hash.

### C-04 · Period-control variants → `component-contracts.md` (extend the "Period chip" section)
**Current (L30–32):** chip/segmented presentation, 36/44 geometry, staging, "Time semantics (what ranges exist, defaults) are product-owned; this contract covers presentation only."
**Proposed:** retitle section "Period control" and append: "Two presentation variants are supported: (a) the period chip / segmented row above, and (b) a native month or date input (`<input type="month"|"date">`) for precise selection. The native variant keeps LTR-isolated English-digit entry inside the RTL composition (`dir="ltr"`, bidi isolation), a 13px label, the 44px hit-area floor, and a visible wrapper focus ring; the control's native internals stay out of scope. Both variants state the qualifying range in Arabic with English numerals and anchor to the value or list they qualify."
**Register basis:** U-08 (chip as variant, not mandatory replacement). **GP: yes.** **Rollback:** baseline hash.

### C-05 · Overlay vs in-flow composition guidance → `component-contracts.md` (new short section before the final domain-compositions paragraph)
**Proposed:**

> ## Overlay versus in-flow
>
> Consequential confirmation and destructive deletion use the overlay contracts (Dialog/Sheet with scrim, focus containment, and an independent confirmation path). Continuous explanation, reading, and editing can remain in-flow — expandable sections and layered content are legitimate compositions and must not be converted into overlays wholesale. A surface qualifies for an overlay when the user must not lose context of a consequence; it qualifies for in-flow when the content supports ongoing reading or editing.

**Register basis:** U-17. **GP: yes.** **Rollback:** baseline hash.

### C-06 · AUX behavior addendum → `navigation-shell.md`
**Current:** 3 lines (four destinations, RTL, safe areas, persistent bottom nav, restrained top area, FAB gutter).
**Proposed:** keep the current paragraph and append:

> ## AUX behavior addendum (visual/interaction contract)
>
> - **Route-kind chrome.** Screen families may be classified by interaction depth: surface-like reading/list screens keep the persistent navigation; deep work/flow screens may hide it to protect focus. This is a chrome *behavior* contract — route lists, names, and classification remain product-owned.
> - **Keyboard-driven chrome hiding.** While the software keyboard is open, transient chrome (top bar and bottom navigation) may hide so the working area keeps its height; content, the focused control, its label, and helper/error text never hide. Chrome returns when the keyboard closes.
> - **Safe-area clearance.** Bottom-anchored chrome pads with `env(safe-area-inset-bottom)`; sticky footers and action bars sit above it; the FAB keeps its own gutter and never covers amount or action columns.
> - **Context-label suppression.** A top-bar context label may be suppressed when it would duplicate the screen's own heading; the title area stays stable (no layout jump).
> - **Scroll-border behavior.** A hairline border or elevation tier strengthens under the top bar only after the content actually scrolls, and relaxes at the top.
> - **Route transition guidance.** Route changes use the standard content transition timing (`--motion-normal` 200ms, easing per the motion contract) with no page-wide layout animation; the incoming screen's states (loading/empty/error) render immediately. Under reduced motion, transitions collapse per the motion contract.

**Register basis:** U-10 + register entering item 3; Flash GAP-32 (preserve + document). **No Micro specifics** (no route names, no 116px, no in-grid FAB). **GP: yes.** **Rollback:** baseline hash.

### C-07 · Route-transition row → `motion-interaction.md`
**Current:** timing table has Press/Fast/Normal/Sheet/Dialog/Skeleton/Snackbar rows — no route row.
**Proposed:** add one row `| Route / content transition | 200ms (uses --motion-normal) |` and one sentence in Rules: "Route and content transitions reuse the normal timing; entrances decelerate and there is no page-wide layout animation."
**Basis:** CF-2 resolution (200ms, no new value). **GP: yes.** **Rollback:** baseline hash.

### C-08 · Quiet feedback variant → `component-states.md` (extend the quiet-completion bullet)
**Current (L28):** "Quiet completion returns the control to its quiet surface and shows a check icon plus a past-tense word; the authoritative result is confirmed by wording with a semantic marker, never by color alone."
**Proposed:** append: "Inline/quiet feedback is a valid completion channel: an inline result region (word + marker, `role="status"`/`aria-live` polite) or a quiet result card may confirm an action in place of a Snackbar. The Snackbar remains an optional transient channel — it is not mandatory, and a product may standardize on inline feedback. On warm-tint quiet surfaces the completion marker renders in ink (the semantic check shape carries the meaning); semantic-hue markers require a surface that meets the 3:1 non-text minimum."
**Register basis:** U-07. **GP: yes.** **Rollback:** baseline hash.

### C-09 · Typography floor clarification → `typography.md`
**Current:** label row "field labels, chips"; caption row "the 12px floor; never for financial facts"; hierarchy paragraph "Financial facts never render below 15px; the 12px caption floor carries metadata only."
**Proposed:** caption row use → "non-financial metadata only — the 12px floor; never for labels or financial facts"; hierarchy paragraph → "Labels never render below 13px. Financial facts and amounts never render below 15px; the 12px caption floor carries non-financial metadata only, and the tertiary 13px mono step is non-financial numeric metadata. …"
**Register basis:** U-04. **GP: yes.** **Rollback:** baseline hash.

### C-10 · Icon and RTL adapter guidance → `iconography.md`
**Current:** 3 lines (one outlined 24px family, directional mirror, icons support words).
**Proposed:** append:

> ## Adapter guidance
>
> - **Mirror flags.** Each icon role carries a mirror flag: directional icons (arrows, chevrons, send/return, undo) mirror in RTL; symmetric and object icons never mirror; media controls (play, skip) keep their canonical direction. Mirroring is applied by the consuming adapter, not by re-drawing glyphs.
> - **Semantic icon roles.** Icons bind to roles (create, save, confirm, delete, warn, info, check, close, eye, clock) so a product can swap the glyph library without touching contracts. The Standard does not mandate a production icon library; any outlined, normalized-stroke 24px family that honors the mirror flags satisfies the contract.
> - Icons support words and state markers and never replace important financial wording.

**Register basis:** U-13. **GP: yes.** **Rollback:** baseline hash.

### C-11 · Authority ladder → `README.md`
**Current:** README describes the package as the official visual foundation (L3–5).
**Proposed:** insert after L5 a short section:

> ## Authority ladder
>
> Micro Standard v2 = visual contracts (tokens, classes, states, geometry, accessibility, composition guidance). The Micro runtime token mapping = the carrier that binds implementation variables to these contracts. Micro docs = implementation guidance. Micro domain/application/storage layers = product meaning and persistence. Contracts never encode product meaning; runtime never redefines contract values.

Also append to the Verification boundary section: the package is "29 core files + 2 metadata records (`MANIFEST.json`, `RELEASE.md`)"; `source-inventory.md` remains a core evidence/contract file.
**Register basis:** U-19. **GP: yes.** **Rollback:** baseline hash.

### C-12 · Manifest split correction → `MANIFEST.json`
**Current:** `"file_count": 29` (no split statement).
**Proposed:** replace with `"file_count_total": 31, "core_files": 29, "metadata_files": 2, "metadata_files_list": ["MANIFEST.json", "RELEASE.md"], "split_note": "29 core contract/gallery/evidence files + 2 metadata records"`, and update `updated_by` to record this reconciliation. `source-inventory.md` remains in the 29 core files.
**Basis:** GAP-46; Agent 5 file-count confirmation. **GP: yes** (metadata accuracy). **Rollback:** baseline hash.

### C-13 · U-18 skeleton rider → `empty-loading-error-states.md`
**Current (L9):** "Loading — skeleton that promises the real layout; the section title stays visible; `aria-busy` marks the region."
**Proposed:** "Loading — honest text ("جارٍ التحميل…") or a skeleton that promises the real layout; the skeleton variant is optional and applies where the real layout is stable — it is not a universal requirement. The section title stays visible; `aria-busy` marks the region. (The chart loading contract in `data-display-system.md` keeps its recorded skeleton basis.)"
**Register basis:** U-18. **GP: yes.** **Rollback:** baseline hash.

### C-14 · Surface-specific contrast bindings → `accessibility.md` + `color-system.md`
**Current:** accessibility.md's table records success/surface 3.27 and status/surface 3.25 as non-text marks; the "Consequently" paragraph says low-ratio hues never carry meaning alone. color-system.md's tint grammar is unqualified ("semantic ink" on warm ground).
**Proposed (accessibility.md):** extend the "Consequently" paragraph: "Success `#629987` and Status `#1490FF` meet the 3:1 non-text minimum on the white Surface (3.27 / 3.25) and only marginally on Canvas (3.10 / 3.08 — pair with the word); on Ground `#F5F4ED` and Recessed `#F0EEE6` they fall below 3:1 (2.96 / 2.95 and 2.81 / 2.80) and must not serve as marks there — use a Surface-backed mark or an Info/Error binding instead (Info on Ground 3.51; Error is text-safe at 5.46 / 6.02). Words always render in a text-safe ink."
**Proposed (color-system.md):** append one sentence to the tint grammar: "As an application rule, the success and status hues bind their marks to the white Surface (or Canvas with the word); on Ground/Recessed, marks use Info/Error or neutral ink, with the word in a text-safe ink."
**Basis:** computed values (this run's `scripts/contrast_checks.py`; matches Agent 3's recomputation). **GP: yes.** **Rollback:** baseline hashes.

### C-15 · Gallery deviation fixes → `component-gallery.css` (proven contradiction class)
All fixes keep selectors, layout, and geometry; they change word inks, marker surfaces, font sizes, and one padding. No new color values — only rebindings of approved values. Computed contrasts in parentheses.

| Selector | Current | Proposed | Why |
|---|---|---|---|
| `.tag` | `font-size: var(--text-caption-size)` | `var(--text-label-size)` (13px) | CF-1: state words are labels (U-04) |
| `.tag-positive` | ground bg, `color: success` | `background: var(--vf-surface); border: 1px solid var(--vf-border-soft); color: var(--vf-ink-secondary)` (icon keeps success, 3.27 on surface) | word 2.96 fails on ground; surface-backed mark passes |
| `.tag-review` | ground bg, `color: status` | same pattern as `.tag-positive` (icon keeps status, 3.25 on surface) | word 2.95 fails on ground |
| `.tag-operational` | `color: info` | `color: var(--vf-ink-secondary)` + add `.tag-operational .ic { color: var(--vf-info); }` (3.51 on ground) | word 3.51 < 4.5 AA text; marker stays |
| `.tag-pending` | `color: info` | `color: var(--vf-ink-secondary)` (icon already info) | same |
| `.tag-negative`, `.tag-progress/.tag-ready/.tag-closed/.tag-neutral/.tag-unknown` | — | unchanged | already text-safe (error 5.46; ink families 4.73–8.16) |
| `.btn.btn-complete` + `.ic` | `color: success` on ground | `color: var(--vf-ink)` both (16.72) | success 2.96 fails; ink check shape + past-tense word carry completion (C-08) |
| `.kpi-change` | caption 12px | `font-size: var(--text-body-size)` (15px) | financial fact ≥15px (U-04) |
| `.kpi-change.pos` | `color: success` | `color: var(--vf-ink-secondary)` (7.80) | 3.27 < 4.5 AA text; sign + trend icon keep direction |
| `.pos` / `.op` (row amounts) | success / info text | `color: var(--vf-ink)` (18.43 on surface) | amounts are text: 3.27/3.87 fail AA; sign is the non-color marker; `.neg` stays error (6.02, text-safe) |
| `.t-pos` | `color: success` on ground tile | `color: var(--vf-ink-secondary)` (7.80) | icon 2.96 fails; direction shape carries meaning |
| `.m-pos` | success on ground | `color: var(--vf-ink-secondary)` (7.80) | 2.96 fails |
| `.m-op` | info on soft | `color: var(--vf-ink-secondary)` (5.50 on soft) | 2.48 fails |
| `.navlabel` | caption 12px | `var(--text-label-size)` (13px) | labels ≥13px |
| `.seg button` | caption 12px | `var(--text-label-size)` (13px) | labels ≥13px |
| `.count` | caption 12px | `var(--text-label-size)` (13px), `line-height: 1` | non-financial numeric metadata → tertiary 13 |
| `.bottomnav` | `padding: 4px 12px 6px` | `padding: 4px 12px max(6px, env(safe-area-inset-bottom))` | navigation-shell.md already claims safe areas (D3) |
| `.navitem` | `min-width: 64px` | `min-width: 44px; flex: 1 1 0` + `.navlabel` ellipsis guard (`max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap`) | proven pre-existing 14px overflow at 320px (min-width 64×4 exceeded the demo screen's 254px available width even in baseline); 64px is the nav *height* minimum in tokens, not an item width; 44px keeps the touch floor; measured clean across all 24 combos after the fix |

Also update the state-tag comment block to describe the applied rule. **Rollback:** baseline hash. **Dependency:** re-run gallery verification (Phase 3) because recorded items 3 and 5 depend on these styles.

### C-16 · Run records → `RELEASE.md`, `verification-report.md`, `coverage-matrix.json`, `decision-log.md`, `self-critique.md`
- **RELEASE.md:** append a "What this release adds (run run-20260914-msv2-reconciliation-01)" section: the ten contract additions, the contrast application rule, the gallery consistency fixes, the 29+2 manifest split, Prototype v1 as evidence, and the unchanged foundations.
- **verification-report.md:** append this run's re-verification record (what was actually run — see Phase 3) with explicit limitations preserved verbatim (physical-device and screen-reader testing not performed).
- **coverage-matrix.json:** `updated_by` → this run; add families `knowledge_states`, `aux_behavior`, `period_variants`, `quiet_feedback`, `overlay_vs_inflow`, `type_floor`, `icon_adapter`; extend the `verification` array with this run's checks; keep `requires_separate_testing` unchanged.
- **decision-log.md:** append decisions 15–21 (knowledge states; AUX addendum + 200ms route row; period variants; quiet feedback optional Snackbar; overlay vs in-flow; type floor + gallery label migration; tint application rule + gallery consistency fixes). Append-only; decisions 1–14 untouched.
- **self-critique.md:** update the stale "Tag text at 12px sits at the caption floor" sentence to the clarified floor (tags and nav/segment labels at 13px; 12px reserved for non-financial metadata) and add this run's honest limitations.
**GP: yes** (records). **Rollback:** baseline hashes.

### C-17 · Prototype v1 (new, outside the Standard package)
Built per Agent 4's plan (6 scenes) with CF-4's vocabulary decision: neutral illustrative content; the Standard's own example words for contract demos; knowledge-state words per C-01; visible "Visual validation prototype — not product truth" label; tokens embedded from the post-edit `design-tokens.css` values; RTL, English digits, bidi isolation, reduced motion, no-overflow. Files: `prototype-v1/{README.md, prototype.html, prototype.css, prototype.js, PROTOTYPE_COVERAGE.md, PROTOTYPE_VALIDATION.md}`. **Not part of the 31**; lives in the run folder only.

## 3. Files changed vs untouched

**Changed (17):** component-states.md, component-contracts.md, navigation-shell.md, motion-interaction.md, typography.md, iconography.md, README.md, MANIFEST.json, RELEASE.md, verification-report.md, coverage-matrix.json, decision-log.md, self-critique.md, empty-loading-error-states.md, accessibility.md, color-system.md, component-gallery.css.

**Untouched (14):** button-system.md, surface-system.md, visual-direction.md, spacing-radius-elevation.md, responsive-geometry.md, input-system.md, data-display-system.md, content-guidelines.md, overlay-system.md, design-tokens.css, design-tokens.json (its `updated_by` intentionally unchanged — the file's content is untouched; recorded here per Agent 5), component-gallery.html, component-gallery.js, source-inventory.md.

## 4. Dependencies and ordering

1. Contract edits (C-01…C-14) — independent of each other except C-14 grounds C-15's bindings.
2. Gallery fixes (C-15) — after C-14 (bindings documented first).
3. Re-run gallery verification (headless Chromium) — after C-15; recorded in C-16's verification-report update.
4. Prototype v1 (C-17) — after contract edits (embeds final token/contract state).
5. Run records (C-16) — last, recording actual results.
6. Validation, packaging, upload — after all of the above pass.

## 5. Rollback boundary (whole run)

Every changed file restores to its baseline SHA-256 (PRE_FLIGHT_REPORT §3). The uploaded branch is a single commit on top of `main` `864263c` and reverts as one commit; `main` itself is never touched. The Micro repository is never touched. The context-pack branch is never touched.
