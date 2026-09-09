# Self-Critique

An honest review of this package by its own standards — including the repair run's own findings against its predecessor. The original run claimed coherence and verification; the repair wave proved several of those claims were attribute-level, not pixel-level, and this document records both what the repair fixed and what genuinely remains imperfect or human work. No claims of visual perfection are made anywhere; this is where that honesty is enforced.

## What the original run got wrong (and the repair fixed)

1. **Motion was documented, not implemented.** Every overlay duration in the original docs (sheet 340ms, dialog 200ms, scrim 200ms) was dead text — the CSS had no transitions; the JS toggled `hidden`. The verification passed because it asserted attributes, not rendered state. The repair wires real transitions to the mandated timing system (R-01/R-02) and the rebuilt verification asserts computed transition properties and post-close hidden states.
2. **Closed overlays stayed on screen.** `display:flex` defeated `[hidden]` on the dialog and snackbar — Escape "worked" while the dialog kept floating there. The repair adds the global `[hidden]` guard and transition-aware close sequencing (R-03).
3. **Verified-but-absent states.** The coverage matrix claimed "verified-both" for states that were not in the DOM (destructive dialog pairing, search loading spinner, sheet expanded snap, five-destination nav). The repair rebuilds coverage against the real DOM (R-31) — every ✅ maps to a selector.
4. **A11y claims that did not survive a real Tab press.** Inputs suppressed their own focus ring; chips measured a 36px hit box while docs claimed 44; the FAB overlapped the nav; safe areas were documented in five places and implemented nowhere. All fixed (R-04, R-26, R-18, R-17).

The uncomfortable lesson: five independent audits and 48 deterministic checks did not catch these because the checks asked "is the attribute set?" instead of "is the thing true?". The repair's verification layer now asks the second question.

## What is genuinely strong

1. **Measured, not asserted — twice over.** 62 WCAG pairs from the original run, independently reproduced, re-verified by the repair wave; every geometry claim traces to a source line; every behavior claim now traces to a live browser assertion or a computed style. The decision log carries 67 classified decisions.
2. **The source direction survived two runs.** Six ramps, nine neutrals, the elevation ladder, the 4px grid, the type scale, and the component anatomy are inherited; every correction moves pairings within the existing ramps. The identity color finally *appears* (FAB, icon-only identity actions) instead of living only in a meta tag.
3. **The interaction layer is now real.** The filter sheet stages and commits; drag-to-dismiss works; undo restores DOM nodes; the loading guard blocks double submits; the bar moves while numbers land immediately; focus travels into overlays and back to triggers; the rail snaps without hijacking vertical scroll.
4. **The audit chain is reproducible.** Original five-audit wave, repair four-audit wave, twelve report artifacts, four verification scripts, one shared worklog — a receiver can rerun the pipeline and compare.

## What a senior reviewer would still flag

1. **The primary button is darker than the source's mockups** — the standing D-01 judgment call, now accompanied by a second one: the destructive fill deepened from the 500 to the 600 step (R-19). Both are measured, source-adjacent, and reversible by a receiver who disagrees.
2. **Fonts remain the weakest link.** The gallery renders in fallback stacks; Arabic joining density, mono rhythm, and heading texture are approximations until IBM Plex is bundled.
3. **The four "proposed grammar" icons** (bag, truck, return, sort) have no source precedent. They follow the source's stroke/cap/join grammar and are flagged in the registry, but a reviewer may reasonably want source-library equivalents.
4. **Ready vs moved tints measure 1.04:1 apart** — the same pale pill. Structure (distinct icons + text) carries the difference, and the limit is documented, but a colorblind user gets no chromatic help there.
5. **The 200% text-scale experience is usable, not optimized** — parts stack, rows grow, the filter sheet scrolls; nothing clips, but the layouts were tuned at 100%. On-device text-scale QA remains human work.
6. **Drag-to-dismiss is verified with synthetic pointer events** in a headless browser, not a finger. Thresholds are ported from the source component, but feel is a device property.

## Where the package could be wrong

- A team shipping the literal `#CC785C` button or `#C9322A` destructive fill inherits two visible changes; both compatibility impacts are stated per-decision.
- The dual-ring contract (inset surface ring on dark fills) is a defensible reading of WCAG 2.4.7/1.4.11, not the only one; a team using thick outer rings instead should re-measure.
- The timing system is run-mandated, not source-derived; a team with motion-capture evidence for the 340ms sheet may legitimately revert R-01 — the decision records what changed and why.
- Zebra rows + inset dividers is one reading of the source's §7.7; a reviewer could collapse zebra to dividers-only without violating any rule.

## What remains human work (declared, not claimed)

On-device safe-area insets and keyboards · real IBM Plex rendering and subsetting · screen-reader walkthroughs (roles, labels, and live regions are DOM-verified, not audibly tested) · Arabic copy quality by a native reviewer · finger-feel of drag thresholds and snap · acceptance of the corrected pairings as brand decisions · the two unresolved records (D-33 investor-mode exclusion, D-34 brand-asset recoloring) · subjective taste on the terracotta's depth and the FAB's restored lightness.

## Scoring the package

The original package claimed coherence and measurement and delivered both at the token layer while over-claiming at the behavior layer; this repair closes that gap. What is claimed now: the package is complete (29/29), coherent across files, measured, offline-verified at four widths in two directions at three text scales with reduced motion, source-preserving, behavior-honest (every documented interaction is exercisable), and free of credentials, placeholders, and product assumptions. Those claims are backed by files, numbers, computed styles, and browser assertions rather than adjectives — and the places where they are not (fonts, on-device feel, screen readers) are listed above instead of hidden.
