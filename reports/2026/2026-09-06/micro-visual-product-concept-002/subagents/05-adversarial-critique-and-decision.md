# 05 — Adversarial Critique, Integration Rulings, and Pre-Build Decision

**Delivery:** `micro-visual-product-concept-002`
**Task ID:** 2-e · **Agent:** Sub-agent 5 — Adversarial Senior Design Critic and Integration Judge
**Date:** 2026-09-06
**Basis (honesty label):** Critique of the four specialist reports (01–04), the source intake (`en/00-SOURCE-INTAKE-REPORT.md`), and the lessons register (`en/01-current-work-lessons.md`), checked against `Micro-Target-State-Design-Report.md` §4.0–§4.5 as ground truth. **No new research is claimed.** The only new measurements in this report are WCAG 2.x contrast recomputations (method identical to reports 02/04; arithmetic not reproduced per row) for pairs the four reports left unmeasured or disputed; every other claim cites a specific report, section, or table row.

---

## 1. Findings register

| # | Report | Finding (with citation) | Severity | Required fix |
|---|---|---|---|---|
| F-01 | 02 | H-B motion spec includes a "shell figure count-tween 200ms" (§3.2, Motion row) — an animated money counter, explicitly forbidden by 03 §5 (Forbidden motion register: "Animated counters"). H-C adds "number roll 250ms" and "bar fill 300ms / flow-draw 350ms" (§3.3, Motion row) — the 300/350ms values breach 03 §3's hard cap ("travel > 280ms forbidden"). | **Blocker** (if either preview animates) | 03's motion register is binding for all three directions; H-B/H-C previews render static (02 §6 already concedes this for H-C — extend it to H-B). |
| F-02 | 02 vs 04 | Three different dark canvases and two different light canvases coexist: 02 §2.2 light `#faf6f2` / dark `#332d27`; H-B proposes dark `#2b2620` (§3.2, Background row); 04 §2.2 recommends light `#ffffff` / dark `#1c1815`. No single token set can be built from these. | **Blocker** | One neutral token set, centrally registered before synthesis (ruling R-A, §2 below). |
| F-03 | 04 | §2.2 re-roles the dark canvas token `#332d27` as **light-theme ink**. This is a clever token economy but blurs C-05's "deliberate dark mappings" story: the same hex is simultaneously the dark canvas and the light body ink, which reviewers of the dark frames will misread. | Major | Reject the cross-theme re-role; adopt 02's dedicated light ink `#221c18`; `#332d27` stays dark-theme-only (ruling R-A). |
| F-04 | 02 vs 03 | Focus ring colors conflict: 02 §2.3 (Semantic layer) specifies focus `#057b7c` light / `#8fd5d6` dark; 03 §2.7 specifies `#964e33` light / `#8fd5d6` dark. The success mark is `#057b7c`-family (03 §2.5) — under 02's value, focus and success share a hue, risking the C-06 distinctness 03's own OQ-3 worries about. | Major | Adopt `#964e33` light / `#8fd5d6` dark (ruling R-B). |
| F-05 | 02 | H-B and H-C type scales sit below 04's Arabic floors: H-B rows 14px, captions 12px (§3.2); H-C rows 14px, captions 12px (§3.3); H-A's "Minimum 12px anywhere" and 12px overline (§3.1) also breach 04 §1.1's "minimum Arabic body 15px, caption floor 13px". | Major | 04's floors bind all frames including direction previews; H-A overline moves 12→13px (ruling R-F). |
| F-06 | 02 | §3.1 Motion row: "Reduced motion: 100ms crossfade; sheets fade in place" — reduced motion implemented as *shortened* motion, contradicting 03's full-alternative model (instant swaps + compensation; §2.2–§2.8 and §4). | Major | 03 owns reduced-motion semantics (ruling R-D). |
| F-07 | 02 | Comparison table §4 claims "competitor ledger apps (card-dashboard style) look like H-B" — unsupported (no visual inspection occurred anywhere in this delivery) and **contradicted by 01** §2.1, whose evidence describes Khatabook/OkCredit as name-first *list* rows, i.e. closer to H-A than H-B. | Major | Strike the claim; H-A's distinctiveness rests on glossary-native grammar alone, which is sufficient. |
| F-08 | 02 | H-C's in-flow bar colors on tinted zones fail the 3:1 non-text minimum: `#079fa0` on `#e3f5f5` = **2.88:1**, `#cc785c` on `#e3f5f5` = **2.91:1** (computed for this report; unmeasured in 02). | Major | Bars only on white/dark canvas, or bars on tinted zones must switch to text-role strokes — moot if H-C remains a static preview (ruling R-C). |
| F-09 | 02/04 | Unmeasured pairing in the recommended direction: 13px action words `#057b7c` on the proposed `#faf6f2` canvas (02 §3.1 Row anatomy). 02 measured `#057b7c` on white, `#f4e4db`, and `#e3f5f5` only. Recomputed here: **4.73:1 — passes**, but with thin margin. | Minor | Tool-verify at build; fallback is `#964e33` (5.69:1 on `#faf6f2`). |
| F-10 | 03 | Internal inconsistency: dark keypad press tint is `#cc785c` 16% (§2.3) while dark row/chip press is `#d59172` 16% (§2.4, §2.7) — the same interaction class carries two dark tints. | Minor | Unify dark press tint to `#d59172` 16% (ruling R-E). |
| F-11 | 02 vs 03 vs 04 | Three incompatible uses of dark `#cc785c`: 02's positional mapping makes it the dark *pressed* value (§2.1); 04 §2.2 measures it as dark *secondary text* on the near-black canvas (5.38:1); 03 uses it as a keypad press tint (F-10). | Major | Ruling R-E fixes the role. |
| F-12 | 03 | OQ-2 explicitly asks report 04 to confirm the dark pressed mapping; 04 contains no pressed-state section and never answers. Open questions routed to a silent addressee. | Minor | Resolved by ruling R-E; synthesis must close every open question with an owner. |
| F-13 | 01/03 | 01 OQ-6 (CorrectionPreview: modal vs bottom sheet) is never reconciled; 03 §2.2 silently decides — dialog, center scale 0.96→1, scrim 0.44, static interior lists. An implicit decision masquerading as an open question. | Minor | Ratify 03's dialog treatment (ruling R-J); close 01 OQ-6 as answered. |
| F-14 | All | Missing compositions the HTML review will need and **no report provides**: search/filter (دفتر الناس name search, `/parties?focus=` filters); Settings vertical list; CashCount / CashDistribution (cash closing — §4.0 documents them as deliberate thumb-zone exceptions); PartyDetail / دفتر الناس party ledger (where 01's strongest pattern, per-party dominant balance, lands); WalletLedger; per-screen empty states beyond Home/Orders; assistant entry (Phase 2 AS-1..AS-10); the EN label set for the C-20 LTR toggle; a numeric/Arabic typeface shortlist (01 OQ-2, 02 §3.1, 04 §1.5 all defer it). | **Blocker** (scope) | Publish an explicit coverage list before build: five representative frames + states strip in-scope; the missing surfaces named as out-of-scope or added (ruling 7 and risk RK-05). |
| F-15 | 02 | §1 states "figures legible at arm's length in under 2 seconds" — an acceptance criterion with no measurement method; unverifiable in review. | Minor | Replace with countable proxies already present (34px hero, tnum, fixed column) and delete the seconds figure. |
| F-16 | 01 | The neobank family rows (§2.4) rest on design-agency marketing blogs (lollypop.design, orbix.studio — search 4), not first-party inspection; patterns transfer as if confirmed. 01 is honest about the method (§1) but not about the evidence grade per row. | Minor | Treat §2.4 citations as plausibility, not findings; the affected recommendations (R-02, R-06) survive on target-state contracts anyway. |
| F-17 | 02 | Hero figure color is never specified (§3.1 type scale lists size/weight only; §5 Finance spec likewise), while §2.1 makes `#964e33` a conditional figure role — the single most important figure on Finance/Statement is ambiguous. Also, the 2px `#cc785c` rule serves both header structure *and* attention lines (§3.1 Border logic) — one device, two jobs weakens both. | Major | Ruling R-G: hero renders in ink; attention lines switch to the 2px `#964e33` right-edge marker (already present in 02 §5 Finance decision line). |
| F-18 | 02/04 | 320px arithmetic never done for the winning row anatomy: content width 288px minus 88px amount column minus 44px action target minus 8px gap leaves **148px** for Arabic subject + caption; the facts grid's 144px cells must hold label + figure + qualifier («منها أمانات 10.00 د.أ»). 04's long-content matrix (§1.7) tests strings, not this geometry. | Major | Build the 320px frame first as the constraint test; qualifier drops behind tap or wraps inside the cell (ruling 6; risk RK-04). |
| F-19 | 02/03/04 | Semantic state colors unresolved as a system: 02 §2.3 proposes new hexes (`#256b45`/`#b3362e`/`#9a6700`); 03 §2.6 references an undefined "danger role"; 04's charts use fixed roles (`#079fa0`/`#964e33`) and its glyph table makes color tertiary. Distinctness is genuinely weak: `#256b45` vs `#079fa0` = **1.98:1**, `#b3362e` vs `#cc785c` = **1.84:1** (computed here) — 02's own flag confirmed numerically. | Major | Ruling R-H: glyph+label is the state encoding; 02's hexes are admitted only as measured functional tokens for text/icon state roles, never for chart coding. |
| F-20 | Intake | The intake publishes the dark hex list as 7 values but never a positional mapping table; 02 §2.1's "working positional mapping" is an inference presented with confidence. | Minor | Ratified/overridden by ruling R-E; synthesis should publish the final role table once. |

No violations of C-02, C-04, C-07, C-08, C-09, C-11, C-13, C-16, or C-19 were found in any report — all four correctly treat `#b4613f` as press-only with the ≈4.42:1 authority value quoted honestly, keep `#cc785c` free of white text, and honor unknown ≠ zero. C-14 is respected: 02's Finance contextual primary matches the target-state contract ("contextual قرارات أعلى الصفحة", §4.4), and Home demotes every unit to quiet links.

---

## 2. Contradictions and rulings

**R-A — Neutral token set (resolves F-02, F-03).** 02's light set wins for light (`#faf6f2` canvas, `#221c18` ink, `#5c5148` secondary, `#e5dcd6` hairline, `#ffffff` sheets): H-A's warm atmosphere is its differentiator, and 04's `#ffffff` canvas would flatten it toward the generic minimal SaaS list the brief bans. 04's two-tone dark wins for dark (`#1c1815` canvas, `#332d27` elevated surface, `#f4e4db` body ink): it solves dark elevation without new brand hues and every 04 measurement already assumes it; 02's one-color dark would leave sheets separable only by hairline. H-B's `#2b2620` is rejected. Reason: each winner is the option the losing report's own measurements can absorb without remeasurement.

**R-B — Focus and cursor colors (resolves F-04).** Focus ring and NumericSurface active-slot underline = `#964e33` light / `#8fd5d6` dark. Reason: focus must not share a hue with the `#057b7c` success mark or teal action words (C-06); this also closes 03's OQ-3.

**R-C — Motion authority (resolves F-01, F-08).** Report 03's timing scale, named curves, ≤280ms cap, and forbidden register bind **all** directions, including the two rejected previews. 02's per-hypothesis motion rows are illustrative and overridden wherever they conflict (curve `cubic-bezier(0.2,0,0,1)` and 240ms sheet rise are replaced by M-out and 260ms). Reason: 03 is the only report with per-pattern ms/curve spec tables and interruption rules; averaging the two would produce untestable motion.

**R-D — Reduced motion semantics (resolves F-06).** Reduced motion = 03's full alternatives (instant swaps, static marks, focus compensation), never shortened animations. Reason: platform reduce-motion semantics remove motion; accelerating it is not a reduced-motion pattern, and C-18 makes this first-class.

**R-E — Dark `#cc785c` and dark pressed (resolves F-10, F-11, F-12, F-20).** In dark theme, `#cc785c` is a secondary-text/emphasis role on the near-black canvas (04's measured 5.38:1), not the pressed value. Dark pressed = `#332d27` 24% overlay on buttons (03) and `#d59172` 16% tint on rows/keypad. Reason: pressing should darken, mirroring light's `#964e33→#b4613f`; 02's positional "pressed→#cc785c" cannot apply to the light-colored dark primary button without lightening it.

**R-F — Arabic size floors (resolves F-05).** 04 §1.1 floors bind: no Arabic text below 13px anywhere (H-A overline becomes 13/18), body 15px, rows ≥56px. Reason: 04 owns Arabic legibility; H-B's 48px rows and 12px captions are ergonomic non-compliance, and count against it in §3.

**R-G — Hero and emphasis (resolves F-17).** The dominant figure renders in primary ink (`#221c18` light / `#f4e4db` dark), with `#964e33` reserved for the action role, out-deltas, and the right-edge decision marker; header structure keeps the 2px `#cc785c` rule, attention keeps the `#964e33` marker. Reason: C-03 says `#964e33` is never automatic; a resting hero is not an action, and separating structure from attention restores each device's meaning.

**R-H — State encoding (resolves F-19).** 04's glyph+label grammar is the binding state encoding. 02's semantic hexes are admitted as registered functional tokens (measured: 6.43/6.03/4.87 on white) for text/icon state roles only, gated on the pre-build distinctness check (computed 1.98:1/1.84:1 against accent/brand confirms the risk); chart in/out coding stays `#079fa0`/`#964e33`. Reason: shape+label survives palette failure; adding hues to charts would recreate category-color noise 01 §2.8 rejects.

**R-I — Money isolation scope (no conflict, ratification).** 04 §1.4's bidi contract (isolate digits only; unit «د.أ» outside in the RTL flow; whole island nowrap) is **ratified over any literal whole-string reading** of S-2's `bdi dir="ltr"` note. Reason: unit-inside-isolation renders «د.أ 20.00» in RTL — violating C-09's "unit after number" — while 04's contract preserves reading order in both directions. This is the single best catch in the four reports.

**R-J — First paint and CorrectionPreview (resolves F-13, and 01/03's duplicate OQs).** Finance first paint with a local cache renders cached figures + staleness qualifier (04 §4.1's truth line), never a skeleton; skeletons are reserved for genuinely unknown content (first boot, import, large ledgers). CorrectionPreview is a center dialog per 03 §2.2. Reason: local-first truth (C-11/C-12) — pretending not to know what the device knows is the same lie as zero-for-unknown.

---

## 3. Hypothesis ranking

Scoring convention: 1–5, **5 = best** on every criterion; "genericness resistance" means *cannot be mistaken for a template* (5 = safest).

| Criterion | H-A «دفتر هادئ» Calm Ledger | H-B «مكتب المالك» Owner's Desk | H-C «مسار المال» Flow of Money |
|---|---|---|---|
| Distinctiveness for Micro | **5** — ruled grids, 88px ledger column, glossary-native grammar («دفتر/كشف/السجل») | **2** — cockpit/modules is dashboard vocabulary; 02 itself flags it "must be actively de-genericized" | **4** — in/out/held relationship coding maps to Micro's financial language; trend-adjacent |
| Mobile ergonomics | **5** — 56px rows, inputs+primary in bottom 33%, no input above the fold | **3** — 48px rows breach 04's floor; 96–112px persistent shell + module chrome push work down | **2** — 60–72px bar rows cut scan density; 8 motion primitives raise energy past the calm budget |
| RTL naturalness | **5** — subject-right/amount-left mirrors the paper دفتر; fixed LTR column removes bidi fights | **3** — inline label-then-amount fragments decimal alignment; chevron mirroring overhead | **4** — right→left bar fill is native; pill rows break the column |
| Financial trust | **5** — decimal alignment, positional «—», receipts as sentences, countable discipline | **3** — professional, but inline amounts and count-tween undermine number discipline | **3** — honest part-of-total bars, but infographic energy reads younger than "financially serious" |
| Feasibility of an honest HTML review | **4** — hairlines/tnum/sticky headers are plain CSS; risk is flatness if type craft fails | **3** — easy to build, hard to build *distinct*; reviewers will see a 4-card dashboard | **2** — the direction lives in motion that 03 forbids (rolls, 300/350ms) and in bars that fail contrast on tinted zones (F-08); its reduced-motion static form is not the direction |
| Genericness resistance | **4** — not a component-library look; residual risk of "clean SaaS list" if warmth tokens underused | **2** — bordered modules + elevation levels are Material/shadcn adjacency | **3** — not SaaS-generic, but Dribbble-generic risk (L-07) |
| **Total** | **28/30** | **16/30** | **18/30** |

**Narrative.** H-A wins on every criterion and dominates the two that matter most for this product: trust-as-typography and RTL composition. H-B loses for a reason 02 concedes itself — it is the direction a competent generic design system would produce. H-C loses not on idea but on physics: its essence is animated flow, and the binding motion register (03) plus measured bar-contrast failures (F-08) make an *honest* H-C review impossible — a static H-C preview is a different, weaker direction. H-C's idea survives where it is verifiable: as data-viz content inside H-A (04's Charts 3–4 are exactly H-C's relationship bar and segmented row).

---

## 4. Decision recommendation

**Winning direction: H-A «دفتر هادئ» The Calm Ledger**, with 02 §5's five representative frames as the build scope, corrected by the rulings above.

**Merge in from the rejected directions (nothing else):**
- From H-C: the 6px relationship bar with hatched «عربون محفوظ» bracket and the segmented wallet-composition row — as chart *content* inside Finance/OrderDetail (already specified as 04 §3.4/§3.5), never as row anatomy or page structure.
- From H-B: the shell's live status line (12–13px, e.g. «الحالة: مسجل») under the H-A header question, adding 04 §4.1's truth-slot wording. H-B's modules, elevation stack, and inline numbers are explicitly rejected.

**Binding resolutions for the synthesis (numbered, decisive):**
1. Build H-A only; H-B/H-C appear as static single-frame comparisons, type-floor-compliant, zero animation, controls outside the phone frame (C-20).
2. One neutral token set per R-A; `#332d27` never appears in light theme; the synthesis publishes the final role table once and every spec table diffs against it.
3. Motion authority is report 03 in full — curves, durations, forbidden register, reduced-motion alternatives — overriding all motion rows in 02.
4. Bidi contract per R-I (digits-only isolation, unit outside, island nowrap) applies to every money string in the artifact.
5. Focus ring, active-slot underline: `#964e33` light / `#8fd5d6` dark; success mark `#057b7c` on `#e3f5f5` disc (light) / `#8fd5d6` on `#332d27` (dark); semantic hexes per R-H.
6. FAB = 64×48 radius-4 center-slot text FAB, `#964e33` + white label (6.11:1, C-03-compliant as measured and hierarchy-justified), press `#b4613f` transient (C-04); dark FAB `#8fd5d6` bg + `#332d27` label; 04's 56px generic-circle spec is overruled because the five-destination shell (C-16) makes «سجّل» the center destination, not a floating overlay.
7. The review artifact ships light **and** dark for all frames from the start (C-20, C-05), with the coverage list of F-14 published in the artifact header: in-scope = Home, Finance, Orders, Quick Capture, StatementView + a states strip (12 states per 04/03 specs); named out-of-scope = Settings, PartyDetail, cash closing, search, assistant, WalletLedger — each with one line saying why.
8. Every color pairing used in the artifact is tool-measured before build (including F-09's 4.73:1 thin margin); unmeasured pairs are re-assigned per R-H/R-B fallbacks, not eyeballed.
9. Arabic floors per R-F; the 320px frame is built first and must pass 04 §1.7's long-content matrix plus the F-18 row arithmetic before any other width is attempted.
10. The numeric typeface is a build-gate decision: candidate Arabic faces are verified for ASCII-digit locking and tabular figures (04 §1.5), with the two-font fallback (Arabic UI face + Latin tnum digits inside the `bdi` isolate boundary) documented if no single face qualifies.

---

## 5. Pre-build risk register (top 8)

| # | Risk | Mitigation |
|---|---|---|
| RK-01 | Dark-theme convergence (both text roles `#8fd5d6`, both soft roles `#332d27`) makes dark frames cold, teal-dominant, and emphasis-indistinct — the emotional-quality failure mode for "calm". | Two-tone dark per R-A; `#d59172` warm rules/hairlines on every dark frame; emphasis via hairline enclosures; dark frames reviewed against the six-feel criteria explicitly. |
| RK-02 | Unmeasured/thin contrast pairs (F-09, F-08, F-19) slip into the build. | A measured-pairs gate: script all artifact pairings (this report's recomputations included); <4.5 normal / <3.0 non-text triggers the documented fallback. |
| RK-03 | No typeface yet: without tnum + ASCII-digit locking, the 88px ledger column — H-A's core device — silently breaks (misaligned decimals, contextual ٠١٢٣ swapping). | Resolution 10's build gate; two-font fallback; the artifact's spec panel states which path was taken. |
| RK-04 | 320px squeeze breaks rows, facts cells, and long Arabic labels (F-18). | Build 320 first; run 04 §1.7 as a checklist; qualifier text wraps or drops behind tap; action word keeps 44px hit with transparent padding (04 §2.1). |
| RK-05 | Scope hole: the eight missing compositions (F-14) either silently don't exist or get improvised during build — improvisation is where generic patterns return. | Resolution 7's published coverage list; nothing composes ad hoc; if PartyDetail fits the budget it is frame six (01's strongest pattern lands there). |
| RK-06 | Semantic-state distinctness failure (computed 1.98:1/1.84:1) ships color-confusable states. | Side-by-side swatch test in the spec panel (outside the phone); fallback is shape-encoded states per R-H. |
| RK-07 | Countable calm reads as cold/empty: hairline-only pages, 0-radius surfaces, typographic-only states, no imagery. | Warmth tokens are mandatory per frame, not optional: warm canvas, 2px terracotta header rule, `#f4e4db` fills on facts grid/selected rows, teal action words, 3xl hero breathing; a per-frame feel rubric (six target-feel criteria) is checked before a frame is called done. |
| RK-08 | Spec scattering: three canvases, two focus colors, two scrim values, three minimum sizes, two dark press tints across four reports — any one carried into the build produces an inconsistent artifact. | This report's §2 rulings are the single decision source for synthesis (2-f); the token sheet + decisions log is diffed against every spec table before the first HTML line. |

---

## 6. Verdict

**Not ready to build as-is — ready after four fixes, all administrative rather than creative.** The four reports are individually strong and mutually compatible in intent: no report proposes a palette change, banking chrome, POS framing, gamification, or any anti-pattern from the lessons register, and 01's rejection register plus 02's countable rules make generic drift structurally hard. The set fails integration, not imagination: two blockers are token conflicts (F-02, F-14) and one is motion-authority leakage (F-01), each resolvable by adopting one report's ruling instead of averaging two. The direction decision is not close — H-A wins 28/30 with H-C's verifiable ideas already absorbed as 04's chart contracts, and H-B reduced to one status line. Before the Stage-2 HTML review begins, the orchestrator must: (1) publish the unified token sheet per R-A/R-B/R-E; (2) declare 03's motion register binding and re-render 02's motion rows as illustrations; (3) apply 04's Arabic size floors to every frame including previews; (4) publish the coverage list of F-14 so the review is honest about what it does not show. With those four done — plus the build gates of resolutions 8–10 (measured pairs, 320-first, typeface verification) — the combined work is ready to produce an HTML review that is genuinely Micro: a calm ledger, in the owner's language, honest about every number it does not know.

---

*End of report — Task ID 2-e. No other file was modified; no code, prototype, commit, or push was performed.*
