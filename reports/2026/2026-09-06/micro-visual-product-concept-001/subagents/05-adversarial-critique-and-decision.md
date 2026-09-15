# 05 — Adversarial Critique & Integration Decision

Delivery: `micro-visual-product-concept-001` · Stage 1 · Sub-agent 5 of 5 · 2026-09-06
Role: adversarial critique of en/00, en/01 and reports 01–04; scored ranking; decision for the Stage 2 HTML review artifact. New contrast figures below were computed for this report (WCAG 2.x). No other file touched; no git commands run.

## 1. Generic-UI risk when the recommendations compose

The patterns are adopt-grade individually; the risk is composition. On the home seat, R1 + R2 + R4 + R9 produce *hero + grouped list bands + list* — the exact rhythm of a generic task-dashboard.

- **Report 01 R9** is the generic "smart task list" home; without provenance, three action rows are any SaaS widget. Fix (binding): every attention row carries a one-line *why-line* naming its generating event, and the band header states the owner question, not a label. Report 02's mitigation ("band headers carry question copy") is currently an adjective — make it a rule: question sentence + row count, 34px band, no icons.
- **Report 01 R2** is one chip away from the banking feed Report 01 itself rejects (P3). Guard: every ledger row carries the cause line, never amount+chip alone.
- **Report 02 H1** residual risk is its own "band sameness → settings-list feel". The 88px money column, start-edge spine, and tonal trio must apply to *every* band; optional decoration degenerates into a list app.

## 2. Vibe-coding / decorative overreach

- Adjectives without numbers: R7 "readable at arm's length" (fix: chip text ≥13px, height ≥32px); R4 "quiet omission when empty" (fix: band not rendered; never a zero-count row or placeholder).
- Implementability: all 14 Report 03 motion patterns are transform/opacity + one scroll listener — feasible in a self-contained artifact. H2's ">25% whitespace pull-up" is authoring-time composition, not runtime JS. Nothing needs external assets, hover, or desktop.

## 3. Contradictions, with resolutions

1. **Touch vs density.** H1 rows 52px and H3 rows 48px vs Report 04's floors (≥56px finance, 64px amount rows, 12px dense gaps). Resolution: 64/56 adopted; H1's fold budget recomputes to ≈6–7 rows — caps hold. H3's 12px meta also breaks Report 02's own 13px caption floor.
2. **Chrome heights.** Report 02 top chrome 52px vs Report 03 #14 (64dp↔40dp). Resolution: 64/40 on collapsing screens, 52 on static app bars — state explicitly. H4's 168px plateau is irreconcilable with the stable shell → H4 is out.
3. **Scrim numbers.** Report 03: 40%/60%; Report 02 tokens: .44/.55. Token table wins; correct 03's note. Report 04 never answered 03's dark-mode `#b4613f` press check — still open.
4. **Pattern language.** Chart 4 "unknown segment hatched" vs §6 matrix (hatch = pending/syncing; dashed = unknown). Resolution: unknown chart segments are dashed-outline.
5. **Chip vocabulary.** R7's «معلّق / مُزامن / مزامنة» vs §6's verified «قيد الانتظار / محدّث / جارٍ المزامنة». The S-verified register is canonical.
6. **Conflict semantics.** R7 makes تعارض a quiet chip; §6 makes it `role="alert"` + effect-preview. Resolution: conflict is never a quiet chip — alert row.
7. **Stream-as-home.** H3's thesis collides with Report 01 P3's own reject logic (home as transaction list = banking clone). Resolution: H3 demoted; borrowed node dots (عمل timeline only) must be full-opacity — the .35-alpha rail/dots fail 3:1 non-text contrast.
8. **Split neutral tokens (worst defect).** Report 02 §2.4 proposes ink `#2b201a` / muted `#6b5d54` / canvas `#f8f4f0` / band `#ffffff`; Report 04 §2 "verified" a *different* set (`#1f1a17` / `#5c5148` on `#faf7f4`). Both claim binding. Resolution: Stage 2 adopts ONE set — re-audit 02's set (its pairs pass: ink/canvas 14.49, muted/band 6.33) or re-express 02's roles with 04's verified hexes. Never mix.

## 4. Missing dimensions Stage 2 will need

- **Verified zero vs unknown:** no report distinguishes genuine `0.00 د.أ` (with محدّث chip) from «قيمة غير محددة بعد». Mandatory.
- **Empty states:** day-one home/ledger/receivables copy (S7 onboarding) unspecified beyond R4.
- **Search/filter:** five seats include no search; where customer/order/ledger search lives is undefined.
- **Nested sheets:** effect-preview → confirm focus handoff unspecified (single-sheet trap/restore only).
- **Settings vertical logic:** only «تقليل الحركة» placement exists; no أدواتي row inventory.
- **Top Focus Shell content:** motion specified; which seats collapse and what the compact bar shows is not.
- **Offline queue truth:** how offline entries render in the ledger; how the artifact demonstrates sync truth.
- **Small-type floors:** 11px Arabic tab labels (02 §2.2) sit below every other text floor — raise to ≥12px.
- **Long-name collision:** at 320px the 88px money column + chips leaves ≈150px for names; ellipsis exists, chip-vs-name wrap order does not.

## 5. Color-role violations lurking in the art-direction report

Computed for this report:

- **H1 spine / H2 keystone: `#cc785c` on `#f4e4db` = 2.65:1 — fails the 3:1 non-text floor** where the spine touches the hero tint. Fix: spine/keystone ink is `#964e33` on soft slabs (4.94); `#cc785c` only against canvas/band.
- **Thin margin:** `#cc785c`/`#079fa0` graphic ink was verified on `#faf7f4` (3.07/3.04) but on Report 02's actual canvas `#f8f4f0` computes to **2.99/2.96 — fail**; H3's teal node dots fail there. Verdicts are canvas-dependent — re-compute against the final set.
- **Report 01 §5 "accent family (#079fa0/#057b7c/soft) for all state chips"** invites `#079fa0` fills with white text (3.24 FAIL). Bind: chip = `#e3f5f5` fill + `#057b7c` text (4.51), or `#057b7c` fill + white (5.08).
- **Warning pair `#a86a12` on `#f9eedb` = 3.86:1 — fails normal-text AA** at 13px chips. Report 04 never audited the semantic soft pairs; success 4.59 and danger 4.81 pass; warning must darken.
- **Report 03 row 12** uses a terracotta highlight for errors — brand color must not encode danger; use `#b23a31`/`#f7e3e1`. (Row 10's quiet-completion tint is fine — change, not error.)
- Unknown-delta dashed border at ink 24% ≈1.6:1 is tolerable only because text carries meaning; raise to ink 40%.

## 6. Weak mobile behavior

- No hover dependency anywhere — press is color-only, long-press has «⋯». Good.
- R4's horizontal obligations band: horizontal scroll is weak and low-discoverability on RTL mobile; prefer vertical rows with expand, or snap + partial-peek as a hard condition.
- **RTL gesture collision:** edge-back and row-swipe reveal both drag rightward. Report 03 implies 24dp edge-zone exclusivity but never states it — state it.
- H4's sticky plateau fails small viewports by its own admission (rejected).

## 7. Scored ranking

Weights: differentiation 25% · calm-trust 20% · density 15% · RTL 15% · 320px 10% · implementability 15%.

| Hypothesis | Diff (25) | Calm (20) | Density (15) | RTL (15) | 320px (10) | Impl (15) | **Weighted** |
|---|---|---|---|---|---|---|---|
| **H1 السجل الدافئ / Warm Ledger** | 6 — band rhythm risks settings-list genericism; spine + money column + question headers save it | 8 — ledger order is inherently calm; warm, not empty | 8 — 1 hero + 3 bands holds ≈6–7 rows at 64/56px floors | 9 — spine and column on the start edge; pure `border-inline-start` | 9 — full-width bands, reflow-safe | 9 — trivial CSS, no sticky tricks | **7.90** |
| **H2 الحرفة الهادئة / Quiet Craft** | 7 — carved slabs distinctive, but read premium-lifestyle, not financial ops | 8 — genuinely calm | 3 — starves سجّل/مالي (own admission) | 7 — nothing start-edge-native | 4 — inset slabs lose 32px+ at 320px (own admission) | 8 — easy | **6.45** |
| **H3 التيار المالي / Financial Stream** | 8 — time-composition rare in finance | 4 — endless feed implies unfinished motion; banking-clone collision | 7 — 10–11 rows only via 48px rows violating touch floors | 7 — right rail natural; node clutter | 6 — acceptable | 6 — sticky headers + rail fiddly | **6.40** |
| **H4 المنضدة / The Counter** | 5 — sticky summary header is common | 7 — calm | 4 — plateau eats the viewport | 5 — sticky + RTL safe-area edge cases (own admission) | 2 — <50% content on 568px (own admission) | 4 — fragile | **4.80** |

## 8. Decision recommendation

**No hypothesis wins as-is; use the group-2 precedent: winner + selective adoption.**

- **Main direction of the HTML review: H1 «السجل الدافئ» / The Warm Ledger** — its composition is the owner's mental model, and the only hypothesis that survives every hard floor simultaneously.
- **Compact rejected-direction previews: H2 and H3.** H2 shows what maximum calm costs in density; H3 shows what time-composition buys and its banking-clone collision. H4 gets no preview — its failure is structural (chrome consumption at 320px).
- **Borrowings kept (per Report 02):** H2's concentric hero (outer R20 / padding 8 / inner R12) and H3's node dots inside the عمل timeline only, at full-opacity token colors.

**Three binding conditions on the winner:**

1. **One numeric authority pass.** Reconcile the neutral tokens (3.8); re-compute every `#cc785c`/`#079fa0` graphic use against the final canvas (2.99/2.96 margins fail); spine/keystone becomes `#964e33` on soft slabs; adopt 64/56px rows and 64/40dp chrome; tab labels ≥12px; darken the warning pair; answer the dark-mode `#b4613f` check.
2. **Anti-generic composition contract.** Band headers are owner questions with row counts; R9 rows carry why-lines; money column, spine and tonal trio apply to all bands; quiet omission = band absent; max 2 cards/viewport stays binding; verified zero distinct from unknown.
3. **Pattern-language corrections.** Canonical chip register; conflict as alert row, never quiet chip; dashed = unknown, hatch = pending/syncing everywhere including charts; error feedback uses danger tokens, never terracotta; one offline truth source; 24dp edge-zone exclusivity between back-swipe and row-swipe.

Stage 2 can build the review artifact from H1 + these conditions without re-opening Stage 1.

*End of report — Stage 1, sub-agent 5 of 5.*
