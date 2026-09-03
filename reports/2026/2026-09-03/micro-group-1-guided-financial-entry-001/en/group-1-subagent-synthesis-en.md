# Group 1 Sub-Agent Synthesis — SA-1 through SA-5 Findings and Conflict Resolution

| | |
|---|---|
| **Report ID** | micro-group-1-guided-financial-entry-001 (sub-agent synthesis) |
| **Date** | 2026-09-03 |
| **Program** | Group 1 of the six-group Zman→Micro transfer program |
| **Decision order used to resolve conflicts** | this Group 1 prompt > live Micro code & contracts > gap-analysis design (zaman-to-micro-gap-analysis-001) > Zman reference (journey only) |

## 1. Roles and mandates

| Agent | Mandate | Key outputs |
|---|---|---|
| SA-1 | Micro repository & domain investigator (read-only) | Full inventory: financial-event model, period-result read paths and consumers, entry surfaces, allocation model, store/migration lockstep list, write path, navigation/contract-26 mechanics, test patterns, docs governance, density/token constraints |
| SA-2 | Zman guided-entry & behavior analyst (read-only) | Exact journey documentation with verbatim Arabic copy and file:line citations; draft-persistence pattern; integrity-check UX; wallet/owner/opening journeys; anti-copy list of Zman mechanisms conflicting with Micro's truth rules |
| SA-3 | Financial truth & migration reviewer | Verdicts on category placement, delta invariance, migration safety, canonical result, each MIC check; **found a pre-existing export/import defect** (transfer/transfer-reversal rejection); strengthened the canonical cross-check (full-object equality + invocation spy); final prioritized test list |
| SA-4 | Arabic RTL mobile UX reviewer | Field-order corrections (wallet before date), register rules (colloquial hints vs MSA effect copy), anti-jitter fixed-height preview mandate, review-card label:value rows (bidi safety), chip spec (44px, 160px cap, ellipsis), integrity-page layout budget + lean copy set, density ledger with exact cap recommendations, two complete 18-field screen contracts |
| SA-5 | Adversarial QA & integration reviewer (pre-commit) | Re-ran all gates independently; financial-truth, navigation, schema, UI, test-quality, docs and secrets audits; verdict **FIX REQUIRED** with 1 major + 3 minors + 6 notes — all actionable findings fixed pre-merge |

## 2. Findings that changed the design (adopted)

1. **Label length measured post-normalization (SA-3 Gap 1):** domain and import both measure the 80-char limit after trim/collapse — prevents import being stricter than the domain.
2. **Import-side blank normalization (SA-3 Gap 2):** `prepareImport` normalizes blank/whitespace labels to `null` inside `expenseContext` (the `amanahDeltaMinor ?? 0` precedent).
3. **D-025 transfer-pair defect (SA-3, deepened by SA-5):** operationKey is one deposit unit; the validator (and MIC-2) accept only the two documented coupled pairs; reversal-of-reversal rejected (SA-5 finding 4); regression tests added. This was a pre-existing defect that blocked verified exports of any store containing a transfer.
4. **MIC-2 severity demotion (SA-3):** negative wallet balance (legitimate owner-draw overdraft) and negative unallocated are WARN, not FAIL — mirroring the product's own existing semantics.
5. **MIC-9 window guard (SA-3):** the invalid-window branch must not count as a knowledge-honesty failure.
6. **MIC-4 canonicalization rules (SA-3):** compare `amanahDeltaMinor ?? 0`; contexts canonicalized; per-event try/catch (domain throw = FAIL with id, never a crashed run); reversal compared on deterministic fields only.
7. **Canonical cross-check strengthening (SA-3):** full-object deep-equality + invocation spy — a competing implementation either drifts (fails equality) or stops calling the canonical reader (fails the spy).
8. **Attribution-failure honesty before navigation (SA-3):** the editor stays mounted with the honest note and record link; SA-5 then fixed the post-save dirty-guard disarm.
9. **UX mandates (SA-4):** field order amount → wallet → date; «وجهة الصرف» label with the question as hint (vocabulary parity with the sheet); category FIRST inside the details layer; review card as label:value rows; fixed-height preview region; MSA register for effect copy with the combined negative clause; two-note guidance set; «أدوات»→«أدوات عمل» seed; chip spec; integrity-page budget and copy set; three new density registrations on first measurement day.
10. **SA-5 pre-merge fixes:** stale-settlement WARN (major) + reversal context comparison + post-save guard token + reversal-of-reversal rejection + preview height + unknown-opening WARN copy + MIC-9 windowing.

## 3. Conflicts and resolutions

| Conflict | Positions | Resolution (authority applied) |
|---|---|---|
| Quick-sheet category chips | Gap analysis: «keep the sheet field-free»; prompt Scenario A: «optionally chooses بنزين» in the quick path | **Prompt wins** — one optional single-tap chip row after the fields, before the effect line; amount remains the only mandatory input (the fast path stays fast; the sheet's transitory philosophy is untouched) |
| Suggestion source | Gap analysis: derived-only; prompt: «initial suggestions may include … بنزين، رواتب، …» | **Hybrid** — derived labels first, then seed constants, presentation-only (documented as decision 2 in the implementation report) |
| `/tools/integrity` route kind | SA-1 noted the calculator precedent is a DEEP route; gap analysis specifies `surface` | **Surface** (keeps bottom nav — a reader, matching the Tools seat identity); canonical fallback registered in contract 26 |
| Effect-copy register | Prompt's examples are colloquial («الكاش بينقص»); SA-4: MSA for effect lines, colloquial for hints | **SA-4's split** — grounded in the codebase's established copy system; questions stay colloquial, effect/truth lines MSA |
| Statement grouping depth | Design: nested details per tag; SA-4: one details level + button-toggled rows | **SA-4's structure** (matches the page's own `StatementLineRow` idiom; avoids three-level nesting) |
| Drafts in/out of scope | Prompt: optional («if implemented within the existing safe scope»); gap analysis P2 recommends the financial editor first | **Included**, scoped to the editor's create mode, input-only, explicit restore, never auto-commits — the cheapest risk-adjusted answer to Scenario I's refresh case |
| Multi-project allocation wording | Prompt example: «مشروع أ: 60% / مشروع ب: 40%»; Micro model: project share vs outside-project remainder | **Micro truth preserved and explained** — the review card labels the remainder «الباقي خارج حصة المشروع — بيت أو نشاط آخر»; mapping documented in the contracts report §5 |
| Transfer-pair fix scope | Could be deferred as "pre-existing"; SA-3/SA-5: it breaks verified exports of any transfer-containing store and sits inside this group's integrity/round-trip surface | **Fixed in-group** with decision-log record D-025 + regression tests (the round-trip test matrix of this group is the natural home) |
| Finance doorway cap | SA-4 ledger predicted 181→182 needing a decision record; actual measurement: the doorway string lands in a pre-existing counter blind spot, set unchanged | **No cap change** (measured set identical); blind spot documented as D-026 with the counter fix deferred — measurement beats prediction, and the honest record beats a silent assumption either way |

## 4. Independent verification layer

SA-5 re-ran the entire gate suite independently before the verdict (typecheck, lint, 231 domain + 606→607 prototype tests, density, tokens, build, targeted suites: 168/168), diffed `record()` against HEAD line-by-line for all event types, adversarially probed the pair rules and MIC false-positive space, and audited the diff for secrets/scope (clean). All actionable findings were fixed and the full gate re-run before commit — the merged state is the post-fix state.

## 5. Synthesis verdict

The five roles produced one coherent implementation: SA-1 grounded it in the live code, SA-2 supplied the journey without the mechanisms, SA-3 hardened the financial/migration contracts and found a real latent defect, SA-4 made it work on a 360px one-handed RTL phone, and SA-5 forced it to survive adversarial review before merge. No unresolved conflicts remain; every deviation from the design contract is documented with its authority and rationale in the implementation report's decisions register.
