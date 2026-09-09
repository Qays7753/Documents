# Repair Acceptance Audit — Subagent 5 (Task R4-e)

**Target:** `repos/Documents/zed-ai-runs/20260908T222534Z-g53-5538/visual-foundation-package-staging/` (exactly 29 files)
**Role:** wave-2 completeness-and-handoff auditor — read-only; the package was never modified by this audit.
**Date:** 2026-09-09 · **Machine-readable companion:** `repair-acceptance-audit.json` (same directory)

---

## 1. Methodology

1. **Read all 29 files** (docs, tokens, gallery HTML/CSS/JS, coverage matrix, decision log, verification report) — ~6,000 lines total.
2. **Independent structural verification** — exact 29-file set, flat layout, file sizes, secret/placeholder/emoji/forbidden-hex scans, JSON parse + classification sums, JSON↔CSS token parity recomputed from scratch (155 tokens ↔ 177 custom properties, `var()` resolved).
3. **Git evidence (read-only):** `git status --porcelain` on the source pack (empty), `git ls-tree -r HEAD … | sha1sum` → `74386cd…` (matches the recorded baseline), HEAD = `45d5b57`, staging tree untracked.
4. **Live gallery exercise (agent-browser, headless Chromium, `file://`):** 390 default, then 320/360/430, LTR+RTL, 100/130/200% text scale, reduced motion. Exercised: six-state button cycle incl. triple-click guard; filter stage → cancel (Escape) → discard; reopen → staged=applied; stage → apply → commit (count/summary/filtering/sort); filter-to-empty → no-results → Clear; drag-to-dismiss and expand snap (synthetic PointerEvents); dialog centering + real close; real undo (DOM restore); metric update (immediate numbers, 200ms bar, live aria-label); chevron feedback mid-flight; error recovery (empty submit, input preserved, guarded save); rail computed styles + peek; FAB geometry/fill; focus restore on sheet/dialog/menu/filter triggers; scroll lock; ARIA semantics; mirror registry; safe-area CSS.
5. **Coverage-matrix cross-check:** every family anchor + `data-*` hook (39 selectors) resolved live; every family's state claims exercised or inspected.
6. **Coordinator evidence spot-check:** the 67/0 deterministic log re-inspected entry-by-entry; overflow/text-scale/focus/reduced-motion/behavior captures; the 21 render screenshots (md5-compared).
7. **Adversarial framing:** every finding below cites file+line, selector, or a live eval output; re-verified findings the coordinator claimed; hunted specifically for claims whose evidence trail is broken and for behaviors that break *after* the assertion window.

---

## 2. Repair checklist A–I (end-to-end evidence)

| # | Repair | Verdict | Contract | Tokens | Gallery evidence (live) | Gaps |
|---|---|---|---|---|---|---|
| **A** | Button save-state system | **satisfied** | `button-system.md` §"The six interaction states"; `component-contracts.md` §1 | primary.700 #964E33 → pressed 800; disabled #B7B2A6 no shadow; destructive #B42318; 80ms press; dual-ring 2px/±offset | `#buttons` frame 2: one strip, six labeled states + "states of the same action over time" note. Live: fills computed #964E33/#783B28/#B7B2A6/#B42318; triple-click → single cycle (aria-busy, disabled, label "Save" persists, spinner in fixed 20px slot, no layout shift); +1.6s check + "Saved"; +800ms reset + snackbar; dual-ring live (white inset −4 on primary, accent 2px offset 2 on ghost); reduced motion preserves meaning | NL-02: live completion window renders disabled grey (`.btn:disabled` 0,2,0 beats `.btn-complete` 0,1,0) instead of the documented positive.50 tint; static sample shows the documented look; check glyph still green |
| **B** | Statuses in context | **satisfied** | `data-display-system.md` §"Status badges (in context)"; R-22 | tag pairings (50-tint + 600/700 text + icon) | 11 families — badges family removed; statuses render as tags under row titles with icon+text (7 statuses live); pairing reference in evidence panel; ready/moved 1.04:1 tint proximity documented as known limit with mandatory icon+text mitigation | — |
| **C** | Filter control + staged sheet | **partial** | `component-contracts.md` §3; `overlay-system.md` §filter sheet; R-08/R-29 | 36/44 trigger, count badge primary.700, 240/180 sheet + 200 scrim, safe-area footer | Staging real (parent unchanged while staged); Escape discards (sheet truly hidden, focus restored, scroll unlocked); Apply commits (count 3, summary, rows filtered, aria-expanded false, focus restored); reopen stages from applied (verified twice); sort reorders live; no-results ↔ Clear restores 7 rows; drag mechanism verified (follow, >130 dismiss, −50 expand) | **BLK-01 (blocking):** `js:408` passes `btn.closest(".screen")` into `fireSnackbar()` → "Filters cleared" snackbar never renders **and the whole family screen is hidden 5s after Clear** (reproduced on #filtering and #empty; display:none, offsetParent null). NL-01: aria-expanded stays true after cancel paths |
| **D** | Metric compositions | **satisfied** | `component-contracts.md` §6; R-09/R-14/R-32 | 8px track (proposed, documented), operational.600 + positive.500 segments | 620,000+230,400=850,400 and 470,400+380,000=850,400 across the update cycle; numbers swap synchronously, widths transition 200ms, aria-label live; single flat card (no white-in-white); one column at 320 (measured); reserved value on operational pairing | — |
| **E** | Row grid | **satisfied** | `component-contracts.md` §7; R-10 | 44 tile / minmax(0,1fr) / flex-none trail; divider inset 72px; `.num` bidi-isolated | Long Arabic: line-clamp 2, `white-space: normal`, break-word, 42px (wraps, never ellipsis-only); wrapped qualifiers; trailing amounts/dates/actions; RTL: amount at left, tile at right; chevron nudge translateX(3px)+accent mid-flight, RTL mirror rule present; one divider rule in both lists; real undo restores the exact node at position | — |
| **F** | Icon inventory | **satisfied** | `iconography.md` §registry + §mirroring; R-11 | 20/24px, stroke 1.8 (1.5–2.5), currentColor | 43 symbols = 43 labeled cells; 7 mirror flags (delivery, back/prev, forward, collect in, pay out, return, share) matching the registry; all 21 required operational actions traced; loading = CSS spinner; no emoji (scan); 4 proposed-grammar glyphs flagged | — |
| **G** | Motion layer | **satisfied** | `motion-interaction.md`; R-01…R-03/R-07/R-12…R-15/R-28–29 | 80/120/200/240/180/160/120/200 + 1.5s skeleton — **all computed live** | Press .08s, sheet .24s in/.18s out, scrim .2s, dialog .16/.12, snackbar .2/.12, menu .12, bar .2s; guard, drag-to-dismiss, expand snap, rail snap x + pan-x pan-y + peek, chevron feedback, local insert/remove, immediate numbers, recovery at control, real undo, Escape stack, scroll lock, focus restore, reduced motion 1e-05s with state meaning; no bounce/spring/glow/count-up/page-slide/skeleton-wave | NL-06 `.chip{transition:all}` (S3-18 unfixed); NL-08 focus-jump scroll nuance on R-29 |
| **H** | Arabic/RTL/device | **satisfied** | `responsive-geometry.md`; `accessibility.md`; R-16/R-17/R-26/R-27 | rem scale 16/20.8/32; env(safe-area-*); 44px floor | 320/360/430 × LTR/RTL no overflow; 320+200% no overflow (button 48→108); 130% 20.8px root; long Arabic wraps; bidi isolate + dir=ltr; all key states demonstrated; safe area on 4 surfaces + FAB margin; touch targets measured 44 (chip 36+::after −4); 0 unlabeled icon-only controls; Arabic font fallback documented | NL-05: top bar not consuming `.safe-area-top` in the gallery demo (doc lists it) |
| **I** | Cross-file consistency | **satisfied** | README file map; token JSON meta; coverage matrix | 155↔177 parity **reproduced independently** (11 composite type records → 33 props; zero value mismatches; fonts prose by design) | 39/39 coverage anchors resolve; 34 D + 33 R = 67 decisions; prohibited hex/emoji/remote: none; git source integrity verified; unresolved items explicit (D-33/D-34 + §6) | NL-07 D-series counts prose ambiguity |

---

## 3. Acceptance check results (20 checks)

| ID | Category | Requirement | Status |
|---|---|---|---|
| AC-01 | structure | exactly 29 files, flat, exact names, >200 B | **pass** |
| AC-02 | hygiene | no credentials/secrets/placeholders | **pass** |
| AC-03 | gallery | offline: zero resources, zero console/page errors, no modules | **pass** |
| AC-04 | tokens | 155 JSON ↔ 177 CSS, zero mismatches, sums consistent | **pass** (independently reproduced) |
| AC-05 | tokens | mandated motion system actually wired | **pass** (computed live) |
| AC-06 | gallery | six button states together, labeled as states, live cycle | **pass** |
| AC-07 | gallery | filter staging semantics end-to-end incl. Clear | **fail** — BLK-01 |
| AC-08 | gallery | real undo with DOM restore | **pass** |
| AC-09 | gallery | drag-to-dismiss, expand snap, dialog real close, focus restore | **pass** |
| AC-10 | gallery | metric bar + immediate numbers + live aria | **pass** |
| AC-11 | a11y | 44px targets, accessible names, ARIA state semantics | **pass** (aria-expanded staleness noted) |
| AC-12 | a11y | dual-ring on light+dark; inputs keep ring | **pass** |
| AC-13 | a11y | 320–430 × LTR/RTL; 100/130/200%; reduced motion | **pass** |
| AC-14 | docs | every documented state exists in the gallery (R-31) | **pass** (39/39 anchors) |
| AC-15 | verification | coordinator evidence supports report claims | **partial** (broken motion capture; 3 duplicate screenshots) |
| AC-16 | hygiene | no unsupported "verified" claims | **partial** (Clear-filters path; two defective evidence artifacts) |
| AC-17 | structure | source pack integrity | **pass** (git hash matches) |
| AC-18 | handoff | unresolved + human-review items explicit | **pass** |
| AC-19 | handoff | README try-it flows work without breakage | **fail** — the advertised filter/no-results/Clear flow self-destructs |
| AC-20 | docs | geometry/copy agree across all files | **pass** (nits logged) |

---

## 4. Coverage honesty

**Claims checked: 86** (75 family state entries + 11 cross-cutting in `coverage-matrix.json`, plus the verification report's evidence claims). **Confirmed: 81.**

Discrepancies (all with evidence):

1. **`no-results-on-empty` / "Clear filters restores (verified)"** — restore is real, but BLK-01 destroys the family screen 5 s later and never shows the snackbar. The 67-check gate and browser verification both sampled before the timer fired.
2. **`filter-control` / aria-expanded "verified-both"** — stale `true` after every discard path (js resets it only in `applyFilters()`).
3. **verification-report §2 "Computed motion tokens … PASS"** — the backing capture (`audits/coordinator/computed-repaired-system.txt`) contains only `TypeError: r.getPropertyValue is not a function`. The claim is true (I re-verified 80/120/200/240/180/160/120/200 live), but the recorded evidence does not support it.
4. **"Render evidence (21 screenshots)"** — `button-loading-390.png`, `button-completion-390.png`, `metric-updated-390.png` share md5 `342724d6…` (byte-identical) — three claimed behavior renders are one image.
5. **responsive-geometry.md safe-area list** includes the top bar; the gallery topbar does not consume `.safe-area-top`.

---

## 5. Blocking vs non-blocking issues

**Blocking (must be empty for publish):**

- **BLK-01** — `component-gallery.js:408`: `fireSnackbar(btn.closest(".screen"), "Filters cleared")` passes the family screen as the snackbar element. Clicking any **Clear filters** button (in the Filtering no-results state or the Empty family's no-results demo) (a) never shows the "Filters cleared" snackbar, and (b) **5 seconds later hides the entire family screen** — the Filtering (or Empty) frame vanishes (`hidden=true` → `display:none`, verified `frameStillVisible: false`). Reproduced twice from clean reloads. This breaks the README-advertised flow ("filter-to-empty swaps in the no-results state; Clear restores 7 rows") and falsifies the coverage claim beyond the assertion window. Fix: `fireSnackbar(mainSnack, "Filters cleared", null, null, btn.closest(".screen"))`; re-verify with an assertion taken **≥6 s after** Clear — immediate sampling is exactly how this survived both gates.

**Non-blocking:**

1. **NL-01** — filter trigger `aria-expanded` stays `true` after Cancel/Escape/scrim/drag close (js:348/390).
2. **NL-02** — live quiet-completion renders disabled grey (`rgb(183,178,166)`), not the documented positive.50 tint — `.btn:disabled` (0,2,0) beats `.btn-complete` (0,1,0) while the button stays disabled through the 800 ms window. Affects the loading button and the recovery save. Check glyph still positive.600.
3. **NL-03** — broken motion-token evidence capture (claim independently verified true).
4. **NL-04** — 3 of 21 render screenshots byte-identical.
5. **NL-05** — top-bar `.safe-area-top` not consumed by the gallery demo (utility ships).
6. **NL-06** — `.chip { transition: all }` (wave-1 S3-18) remains, contradicting the one-property motion principle.
7. **NL-07** — decision-log D-series counts prose mixes decision/token-level counting (cosmetic, inherited).
8. **NL-08** — R-29 scroll preservation: programmatic `focus()` can scroll the page when an overlay opens from a distant screen (gallery-only pattern; document or `preventScroll`).
9. **NL-09** — `.frame-tall` 560px min-height leaves rest-state blank in the overlays frame (space hosts open overlays — acceptable staging).

---

## 6. Handoff verdict and conditions

**Verdict: NOT READY TO PUBLISH AS-IS** — one blocking defect (one-line fix + re-verification). Everything else the package claims was independently reproduced and holds: 29/29 files, offline, token parity, source integrity, motion system, six-state button, staged filtering, real undo, metric sums, RTL/text-scale/320 coverage, dual-ring focus, explicit unresolved/human-review lists.

**Conditions for publish:**

1. Fix **BLK-01** and re-run browser verification with **delayed assertions** (≥6 s after Clear-filters); fix NL-01 in the same pass.
2. Regenerate (or annotate) the two defective evidence artifacts — the computed-tokens capture and the three duplicate screenshots.
3. Record NL-02 and NL-05…NL-09 as known-notes (or fix); none blocks handoff.
4. Human-QA items remain as declared in verification-report §6 (fonts, on-device safe areas, screen readers, drag feel, brand ratification of D-01/R-19/R-01 timing).

**Why the gates missed BLK-01:** both the deterministic gate and the browser script asserted *immediately* after the Clear click. The defect fires on a 5-second timer — the same "attribute-level vs truth-level" failure mode the package's own self-critique.md §1 warns about, resurfacing one layer deeper. The lesson for the verification layer: **assert after the longest timer in the system, not after the click.**
