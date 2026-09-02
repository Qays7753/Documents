# SA-5 — Transfer Architecture & Critical Review (Final Rank + One Coherent Architecture)

- **Task ID:** SA-5 (Transfer Architect and Critical Reviewer, sub-agent of Zman→Micro gap analysis)
- **Date:** 2026-09-03
- **Inputs reviewed (in full):**
  - `/home/z/my-project/worklog.md` (parent + SA-1..SA-4 entries)
  - `subagents/01-zman-capability-map.md` (SA-1: ZC-01..ZC-24)
  - `subagents/02-micro-gap-comparison.md` (SA-2: MG-01..MG-21 + 10 false-gap warnings)
  - `subagents/03-workflow-mobile-ux.md` (SA-3: UX-01..UX-09 + cross-cutting patterns + UX rejections)
  - `subagents/04-financial-data-integrity.md` (SA-4: FI-01..FI-10 + IC-1..IC-16 mapping + MIC-1..MIC-9 proposal)
- **Repos (strictly read-only, untouched):** Zman `main` @ `bdd63ab` (`/home/z/my-project/repos/zman`, app under `artifacts/zman-app`); Micro `main` @ `4db6a5f` (`/home/z/my-project/repos/micro`, app under `apps/prototype-web/client`, domain under `src/domain`). Both commit hashes re-verified with `git log`.
- **Methodology:** challenge-first. Every contested verdict from the four reports was re-verified directly in code before being confirmed or overturned; new evidence gathered by me is cited with exact paths below (§1.6 evidence log). Inferences are labeled `INFERENCE`. This report is the final authority for the ranked set; where prior reports disagree, the resolution here is binding for downstream work.
- **Terminology:** product name is "Zman" (repo `zman-app`); money: Zman fils (3 decimals), Micro JOD minor (2 decimals); Micro schema `30` / export `22` (re-verified: `apps/prototype-web/client/src/storage/local/types.ts:27,31`).

---

## 1. Critical review findings

### 1.1 SA-1 (Zman capability map) — confirmed issues

SA-1's catalogue is factually solid (I re-verified its riskiest claims — see §1.6). Its **rankings**, however, are a different matter:

1. **Copied assumption — SA-1 ranked transfer candidates source-side only.** The §6 shortlist ("most relevant for Micro transfer") ranks by Zman-side richness, not by adapted value in Micro. Three of its top five do not survive contact with Micro's domain:
   - **#1 ZC-07 selective inventory** → automation core is a hard reject (SA-3/SA-4 agree; my verification below).
   - **#4 ZC-06 conversion/reversal** → hard reject (F-005, append-only corrections).
   - **#5 ZC-01 SmartFinanceForm** → pattern already present in Micro: the 5-action QuickActionSheet is the mode selector, and the FinancialEventEditor's «الأثر المعروف» decision card is the effect-hint pattern (verified `QuickActionSheet.tsx:57-79`, `FinancialEventEditor.tsx`). SA-1's claim "Micro has separate editors per financial event; the mode + impact hint pattern transfers directly" ignores that Micro *has* the pattern at both the transitory and deep levels. **Overturned as a gap; one sub-element survives** (draft persistence — see §1.4, new finding).
   - ZC-18 (write-off dual-entry) flagged HIGH — **overturned**: Micro's single reversible waste movement is the stronger design (SA-3 UX-09, SA-4 FI-07); the only transferable residue is *visibility* of waste in the money-reading surface.
2. **The ranking conflation itself is the finding.** A "transfer-relevant design reference" (ZC-07 is genuinely the richest reference) is not a "transfer candidate". This single confusion is the root of contradictions #1 and #3 below. Correction issued: rank only by adapted Micro value.
3. **Minor overstatement:** ZC-08 "Micro has a full CostCalculator/estimates domain; transferable elements: … pre-delivery stock warning" — the stock warning presupposes the tracked-component linkage Micro rejects. Kept only as an estimate-grade *informational* note at most; not registered as a transfer item.

### 1.2 SA-2 (Micro baseline & gap comparison) — confirmed issues

1. **MG-07 «Period result / P&L» MICRO-WEAKER bundles a real gap with three non-gaps.** Its four sub-claims: (a) on-screen-only, no exportable artifact — **REAL GAP** (verified: `pages/Statement.tsx` contains no download/share/export logic; the only "export" is the full-store JSON backup in Settings); (b) no balance-sheet view — **DESIGN BOUNDARY, must not be "fixed"**: Micro's model is delta-based, not double-entry; fabricating an equity/equation claim would create false comfort and collide with the bounded-profit boundary (SA-4 FI-08 says the same; I concur and make it binding); (c) no cross-period retained-result view — **NOT A GAP** (`INFERENCE` from `statementService.read(from,to)` + Statement quick-ranges + custom range: arbitrary periods, including long ones, are already readable); (d) no depreciation/capital line — by design until contract. **Resolution: the actual gap is the export artifact only** → TR-03. Correction issued to MG-07's framing.
2. **MG-20 global search «adapt (low priority)» — overturned to defer.** Micro has per-surface search (Parties), bounded local volumes, and TR-05's activity layer answers "find the recent thing". A cross-record search surface adds chrome without persona evidence. Verdict: not in the transfer set; Pilot observation item (see TR-16).
3. **MG-11 audit log (MICRO-DIFFERENT, medium confidence) — scope reduction confirmed and accepted.** The derived activity read model (TR-05) shows creates/revisions/corrections by their record fields; it is *not* an audit log (in-place updates without a revision record are invisible — e.g. draft edits). For a single-owner local app this is the right trade (corrections — the sensitive ops — are fully documented with reasons and previews); a true write-log becomes a prerequisite only if the deferred multi-device sync capability is ever built, and then as part of *its* contract, not this transfer. Resolution recorded.
4. **MG-14 snippets (adapt, low) — left unresolved by SA-3/SA-4 (no dossier, no contract).** Settled here: P2, gated on owner/persona validation (TR-10), with a hard guard: snippets never prefill prices (MG-14's own open question — made binding).
5. **Confirmed and praised:** the 10 false-gap warnings all survived my spot-checks; the classification counts are consistent; MG-13/MG-08/MG-12 remain the real gap spine. SA-2's open questions are all resolved in §2.

### 1.3 SA-3 (workflow & UX) — confirmed issues

1. **UX-03's invariant list (a)–(g) and SA-4's MIC-1..MIC-9 overlap but disagree in content.** SA-3's (a) "wallet balances = Σ entries per wallet" is a tautology at read time (the balance *is* derived from entries — not a check); SA-4's MIC-2 (see §1.4 item 1 below) is a false invariant as worded. Reconciled into one corrected list in §2.2.
2. **UX-06 tier-1 claim verified precisely:** Home's «ما تغير مؤخرًا» = orders + drafts + financial events (linked *generically* to `/finance`) + schedules; direct sales and corrections are missing from the block (verified `homeControlCenterService.ts:398-423` — directSales appear only in the away-section last-activity math). Tier-1 enrichment is cheap and real. Tier-2 reader needs an explicit owner nod on Home clutter — kept P2 (TR-05).
3. **UX-02's "Micro has no inventory deactivation flow" (INFERENCE) — verified true** (no deactivation UI/contract anywhere in `pages/InventoryMaterials.tsx` / storage types). The stated-consequences dialog stays a *reserved pattern*.
4. **UX-04 «skip feed pagination» — confirmed** (local scale; Micro's collapsible layers already paginate honestly via «السجل كاملًا (N حدثًا)»).
5. **UX-07 priority split (P1 docs / P2 helpers) is sound; I keep it but split into two transfer items** (TR-08 laws, TR-09 helpers) so the ranked set has single-priority entries.
6. **No over-complexity found in SA-3's proposals themselves** — its dossiers consistently strip Zman machinery (reject modal-create, reject pagination, reject More-sheet). One flag: UX-01's "complete" tier (tag management sheet + per-tag trend) is deferred correctly; v1 stays one field + one reading block (binding in TR-04).

### 1.4 SA-4 (financial integrity) — confirmed issues

1. **MIC-2 is a false invariant as worded** — the most consequential defect in the four reports. SA-4 proposes "cash position consistency — readPosition vs Σ cash-continuity entries vs Σ event cashDeltas". Verified against the actual model (`projectFinancialService.ts:362-397`): recorded cash is composed of **order collections + financial-event cashDeltas − supplier purchases paid + direct-sale cash − allocations to wallets**, and cash-continuity entries additionally include wallet openings, adjustments, transfer pairs and reversals. Event cashDeltas and wallet entries are **not 1:1 comparable**; a check built as worded would false-FAIL constantly (or be tuned into meaninglessness). **Correction issued** — replaced by structural cash checks: unallocated cash ≥ 0 read-back, per-wallet balance ≥ 0 read-back, transfer pairing, reversal-reference validity (new MIC-2′, §2.2).
2. **MIC-5's formula is incomplete.** "order.collectedMinor == Σ active collection events" omits deposit events and refunds. Verified: `OrderEventType` includes `deposit_collected`, `deposit_refunded`, `collection_recorded`, `collection_reversed` with `reversesEventId` (`craft-order/types.ts:96-115`), and `settleDeposit` reduces `collectedMinor` only on refund — **retain keeps `collectedMinor` and zeroes `receivableMinor`, creating no revenue** (`craft-order/policies.ts:814-855`). Corrected formula in §2.2.
3. **FI-04's premise "Micro just shipped import/restore" — verified true** (`localTransferService.ts:1007 validateSnapshot`, `:2144 replaceSnapshot`, wired into Settings' sensitive-data area). This settles contradiction #5 (§1.5) in favor of **P0**.
4. **FI-01's migration plan is sound and verified feasible** (no `categoryLabel` exists today — grep of `src/domain/financial-event/types.ts` returns nothing; `ExpenseClassification` details layer exists at `FinancialEventEditor.tsx:354-377,448`; the `amanahDeltaMinor ?? 0` migration precedent cited by SA-4 is real). One addition: bundle the schema-31 decision with TR-10 (snippets, if validated) to avoid a second bump — see §4.
5. **FI-07's "double-reporting waste + loss_non_cash" soft-warning — excluded from the suite v1.** Without a linkage field there is no reliable signal; a naive co-occurrence count would cry wolf. Recorded as a future linkage idea only (§6).
6. **FI-03 confirmed with one sharpening:** `resultMinor` null-on-unknown is itself a cross-checkable state (all surfaces must show the same "غير متاح + أسباب") — SA-4 said this; I make it an explicit acceptance criterion of TR-01.

### 1.5 Contradiction resolutions (binding)

1. **Selective inventory (SA-1 #1 vs SA-3 reject-core/adapt-edges vs SA-4 FI-02 P0-reject).**
   **Resolution: the automation core transfers NOTHING; three edge contracts transfer as P2.**
   Evidence, both sides re-verified by me: Zman auto-deducts on delivery and tolerates negative stock with a warning note (`artifacts/zman-app/src/features/inventory/actions.ts:269` "⚠️ الرصيد قبل الخصم … أقل من المطلوب — رصيد سالب بعد الخصم"); opening stock enters at zero cost; untrack soft-deletes history (dialog verified `CatalogClient.tsx:334,631,677`). Micro enforces non-negative inventory at write, consumption-as-evidence, purchase≠COGS, and reversals-not-deletes (verified `inventory-material/types.ts:29-32`, `policies.ts`, `SupplierPurchaseEditor.tsx:303` «لن يحوله Micro إلى تكلفة بيع أو مخزون حتى المرحلة التالية»).
   Why SA-1 was wrong to rank it #1: it conflated reference richness with transfer value; the four hard conflicts (estimate-effects, evidence bypass, negative tolerance, unknown→zero) mean the core is untransferable *in principle*, not merely deprioritized.
   What transfers (TR-07): (a) purchase→receipt bridge (`?purchase=` prefill — the deliberate, one-tap-away version of automation); (b) zero-stock quiet strip in `/inventory` (verified absent today); (c) the stated-consequences dialog law, reserved for any future deactivation contract. SA-4's "P0" on FI-02 is a *boundary decision priority*, not an implementation priority — accepted as a hard rejection recorded at the top of the Reject tier.

2. **Period result / P&L «MICRO-WEAKER» (SA-2 MG-07) vs Micro's deliberate bounded-profit discipline.**
   **Resolution: the gap is the export artifact (TR-03, P1) plus the single-reading discipline (TR-01, P0); the bounded-profit boundary and the absence of a balance-sheet equation are design boundaries that must NOT be "fixed".**
   The export must carry the truth lines verbatim and word a null result as «غير متاح — بيانات ناقصة» (never 0); a position *summary* may list components but must never claim an accounting equation («قراءة مكوّنات، لا ميزانية محاسبية»). Sub-claims (c) cross-period view and (d) depreciation line are non-gaps (§1.2 item 1). SA-2 itself warned of this in its inverse warning; my resolution makes it binding.

3. **Order→sale conversion (SA-1 #4 vs SA-3/SA-4 reject).**
   **Resolution: SA-1 is overturned; reject confirmed.** Micro recognizes revenue on the order at `delivered`/`settled` and treats collections as cash-only facts (F-005; verified `craft-order/policies.ts` `settleDeposit` retain path creates no revenue and `collectionService.ts:194-204` routes every collection through the single `distributeUnallocated` path). Zman's deposit-reclassification exists *only because* Zman books revenue as a sale row (reclassify comment verified `finance/actions.ts:1550-1552`). Porting it would create a second revenue path and mutate past cash events — both violations. The two *laws* SA-3 extracted (explicit cash-effect copy incl. the negative case; documented inverse for every financial action) are kept inside TR-08.

4. **Assets & depreciation (SA-2 ZAMAN-ONLY gated / SA-3 reject-gated / SA-4 adapt-gated P2).**
   **Final stance: REJECT from the transfer set as it stands; preserved as a pre-designed pattern bank that activates ONLY when the owner approves a Micro specialized contract** (family, straight-line-only?, disposal, partial months, restatement policy — the «لا نخمن قواعدها» rule, verified `docs/decisions/remaining-capabilities-review-v1.md` «مؤجل بعقد متخصص | أصول، إهلاك، قروض، أجور، ضرائب، إرجاع جزئي، توقعات»).
   Gating condition (all must hold): (i) owner decision that asset spreading is needed for the persona; (ii) a Micro asset contract naming method, life conventions, disposal, restatement; (iii) depreciation expressed only as a declared non-cash reduction with its own knowledge state through the existing `loss_non_cash` hook — never as monthly events, never folding into operatingExpense; (iv) schema/export major bump with import migration. Until then the only Micro-honest mitigation is a reading-layer note flagging large one-off costs (`INFERENCE` — Pilot observation, not a build item). Not P2: it is not merely "not required for the first implementation" — it is not buildable without a new Micro decision.

5. **Integrity suite priority (SA-3 P1 "becomes P0 post-import" vs SA-4 P0).**
   **Resolution: P0.** SA-3's own trigger condition is already satisfied: import/restore is shipped and user-reachable on main (verified `localTransferService.ts:2144 replaceSnapshot` + Settings wiring), local-first means there is no server-side DBA to catch corruption, and FI-03's cross-check is hollow without a surface that reports drift to the owner. Cost is low (read-only, schema-free). SA-3's placement resolution (primary أدواتي + مالي doorway) is adopted unchanged — it matches Micro's identity (thinking/verification tool; CashCount precedent).

6. **Write-off dual-entry (SA-1 ZC-18 HIGH vs SA-3 UX-09 / SA-4 FI-07).**
   **Resolution: reject the dual-entry mechanics AND its immutability; keep Micro's reversible waste movement; transfer only the visibility row** (waste surfaced where money is read — «هدر مخزون — بلا خروج نقد» rows, TR-06). SA-4 labeled FI-07 "direct — already covered" while SA-3 said "reject (mechanics) + adapt (visibility)"; the substance is identical — Micro's design is the compliant one, and Zman's م-5 no-reverse gap is exactly what Micro must never import. Recorded as a resolved wording discrepancy, with SA-3's framing adopted.

### 1.6 New evidence gathered in this review (spot-check log)

All paths repo-relative; every item was checked by me in this session:

| # | Claim verified | Evidence |
|---|---|---|
| 1 | Micro main @ `4db6a5f`; schema 30 / export 22 | `git log`; `apps/prototype-web/client/src/storage/local/types.ts:27,31` |
| 2 | Settlement statuses incl. `cancelled_pending/refunded/retained`; `needs_review` gating | `src/domain/craft-order/types.ts:83-91`; `policies.ts:814-855` |
| 3 | Retain keeps `collectedMinor`, zeroes `receivableMinor`, creates no revenue | `src/domain/craft-order/policies.ts:814-855,875-885` |
| 4 | Inventory movements carry `purchaseId/orderId/reversesMovementId/wasteContext`; WasteContext kinds | `src/domain/inventory-material/types.ts:10-32` |
| 5 | Cash allocations carry optional `sourceRef{Id,Kind,LineId}` (kinds sale/expense/collection/order); entry types incl. `reversal` with `reversesEntryId` | `src/domain/cash-continuity/types.ts:13-53` |
| 6 | Recorded-cash composition (proves MIC-2-as-worded false): collections + events − supplier purchases paid + sales − allocations; wallet entries additionally include openings/transfers/adjustments | `application/finance/projectFinancialService.ts:362-397` |
| 7 | Home recent block = orders+drafts+events(generic /finance)+schedules; directSales/corrections missing | `application/home/homeControlCenterService.ts:398-437` |
| 8 | Statement has no export/download/share logic (gap real) | `pages/Statement.tsx` (no matches for download/Blob/share/export) |
| 9 | QuickActionSheet = exactly 5 actions; quick expense = amount+note+wallet only (no classification) | `components/layout/QuickActionSheet.tsx:57-79,109-117` |
| 10 | **No in-form draft persistence in any editor** (only `micro.setup-draft.v1` in Setup, removed on completion); UnsavedChangesGuard arms `beforeunload` but persists nothing | grep `localStorage` over `apps/prototype-web/client/src` (hits only `pages/Settings.tsx:211`, `pages/Setup.tsx`); `components/forms/UnsavedChangesGuard.tsx:112` |
| 11 | No zero-stock/low-stock strip; no inventory deactivation flow (SA-3 INFERENCE confirmed) | grep `pages/InventoryMaterials.tsx`, storage types |
| 12 | Financial-event reversal is never itself reversible | `src/domain/financial-event/policies.ts:271-300` («لا يمكن التراجع عن سجل تراجع سابق») |
| 13 | Amanah over-release guarded at application layer (F-006), read-time amanahMinor accumulation | `application/finance/projectFinancialService.ts:187,833`; `tests` F-006 suites |
| 14 | `resultMinor` null when any direct sale has unknown cost; status `incomplete`/`recorded_only` | `application/finance/projectFinancialService.ts:618-639` |
| 15 | `ExpenseClassification` progressive-disclosure layer exists (host for the tag field); per-intent idempotency key | `pages/FinancialEventEditor.tsx:354-377,448,126` |
| 16 | EventsLayer with `?event=` focus deep link exists | `pages/Finance.tsx:88,955` |
| 17 | Deep-route registry + canonical fallbacks incl. `/finance/statement → /finance` (new routes must register here) | `app/routeClassifier.ts:16-42`; `app/navigationContract.ts:122-149` |
| 18 | Import path shipped and user-reachable | `application/transfers/localTransferService.ts:1007,2131-2144`; Settings wiring |
| 19 | Zman IC-13 compares 3 profit sources × 2 periods | `artifacts/zman-app/src/features/finance/integrityCheck.ts:1240+` |
| 20 | Zman BOM blob download; 6 report types; DRAFT_KEYS localStorage drafts; negative-stock note; deposit reclassify comment; untrack dialog | `reports/page.tsx:181-182`; `reports/actions.ts:91`; `SmartFinanceForm.tsx:339-359`; `inventory/actions.ts:269`; `finance/actions.ts:1550-1552`; `catalog/CatalogClient.tsx:334,631,677` |

### 1.7 Missing-capability scan across ZC-01..ZC-24

Walked the full catalogue against everything registered by SA-2/SA-3/SA-4. Outcome:

- **Registered by prior reports (confirmed adequate):** ZC-02 (MG-01/UX-01/FI-01), ZC-07 (MG-02/UX-02/FI-02), ZC-09 (FI-03), ZC-16 (MG-08/UX-03/FI-04), ZC-06 (MG-05/UX-08/FI-05), ZC-10 (MG-10/UX-05/FI-06), ZC-15 (MG-13/UX-04/FI-08), ZC-18 (UX-09/FI-07), ZC-11 (FI-09), ZC-19/activities (MG-11/12/UX-06), ZC-20 snippets (MG-14), ZC-14 dashboard (MG-15 reject), ZC-21 WhatsApp (MG-19 reject), ZC-22 auth (MG-16/21 reject), ZC-23 backup (MG-18 reverse gap), ZC-24 (UX-07), ZC-12/13/17/04/05/08 (reverse gaps / sufficient).
- **One genuinely missing capability found (new, registered as TR-11): in-form draft persistence for deep editors.** Zman's SmartFinanceForm persists per-mode drafts to localStorage and offers restore (`SmartFinanceForm.tsx:339-359`, DRAFT_KEYS) — the guard against phone-browser refresh/crash mid-entry. Micro has UnsavedChangesGuard (navigation only, `beforeunload` warn — `UnsavedChangesGuard.tsx:112`) and record-level drafts for orders, but **no editor persists unsaved input** (evidence log #10); only Setup keeps a persisted draft (`micro.setup-draft.v1` — proving Micro knows the pattern). Low cost, real offline-first value. P2.
- **Folded, not missing:** ZC-01 (pattern present — §1.1) and ZC-03 unified payments feed (its *complete money feed* ambition is covered by TR-05's unified activity reader; its UNION-ALL pagination is a server-scale solution SA-3 correctly skipped). Both recorded explicitly so nothing silently depends on an unexamined item.
- **Deliberately excluded from the register:** ZC-21 WhatsApp templates (never-build list covers templates *and* automation; sharing is served by TR-03's export/share artifact).

---

## 2. Resolved open decisions

### 2.1 Managed category catalog vs free-tag vocabulary (UX-01/FI-01/MG-01)

**Resolution: free-tag vocabulary with a derived read list — no managed catalog, no new write-path store in v1.**

- The field: optional `categoryLabel` (≤80 chars, trimmed, internal whitespace collapsed) on `OperatingExpenseContext`, frozen per event like the note; suggestions in the editor come from DISTINCT labels over existing events (orphan-merge is inherent to derivation — SA-4's correct offline insight: derivation *replaces* lazy enrollment).
- Why not Zman's managed catalog: Zman's catalog + CRUD modal was a repair for a seeded server-side system already polluted (4 spelling variants of "owner salary", م-11 duplicates). Micro starts clean; a second vocabulary source adds a store, a management surface, and a drift problem (Zman's renames split history) with no offsetting value at this scale.
- Rename/merge (if ever requested) must be per-event documented replacement (`commitFinancialEventReplacement`), never a silent history rewrite — deferred behind Pilot evidence.
- Hard boundaries (binding): the label never influences `sharedProjectShare`, deltas, or any allocation (G3); quick-expense in the sheet stays field-free (verified the sheet is amount+note+wallet today — keep it).

### 2.2 The integrity invariant list (MIC sanity-check against Micro's actual domain)

SA-4's MIC-1..MIC-9 with my corrections; final list **MIC-1..MIC-10** (≤10 owner-legible checks, per SA-3's guardrail):

| ID | Check | Notes / corrections vs SA-4 |
|---|---|---|
| MIC-1 | Period-result cross-surface consistency (Finance period view vs Statement result line vs canonical function) | Requires TR-01 designation first. Null is a value: all surfaces must agree on «غير متاح + أسباب». Drift > 0 → FAIL. |
| MIC-2′ | **Cash structure (corrected — replaces SA-4's MIC-2):** (a) unallocated cash ≥ 0 read-back; (b) per-wallet balance ≥ 0 read-back; (c) every `transfer_out` has a matching `transfer_in` (same transferId, opposite delta); (d) every cash `reversal` references an existing, not-yet-reversed entry | SA-4's wording ("readPosition vs Σ entries vs Σ event cashDeltas") compared incomparable streams — false invariant (§1.4 item 1). The recorded-cash identity itself is true by construction and is NOT a check. |
| MIC-3 | Correction/reversal balance across all five families (financial events `correctionOfEventId`; cash `reversesEntryId`; inventory `reversesMovementId`; order collection events `reversesEventId`; supplier payment reversals + purchase revisions) — every reversal references an existing active original; a reversal is never itself reversed | Domain-verified: `financial-event/policies.ts:271-300`. |
| MIC-4 | Allocation `sourceRef{Id,Kind,LineId}` integrity — every referenced source record exists | Reuse `localTransferService` import-verifier relations at runtime (field existence verified `cash-continuity/types.ts:38-53`). |
| MIC-5′ | Order/sale collection consistency (**formula corrected**): `collectedMinor == Σ deposit_collected + Σ collection_recorded(not reversed) − Σ collection_reversed − Σ deposit_refunded`; direct-sale collected == its allocations | SA-4's formula omitted deposit events/refunds; retained deposits keep `collectedMinor` (verified `craft-order/policies.ts:814-855`). |
| MIC-6 | Pending deposit decisions: `cancelled_pending` + `depositSettlement needs_review` → WARN («قرار معلق، ليس خطأ») | Status names verified (`craft-order/types.ts:83-91`). |
| MIC-7 | Amanah ≥ 0 read-back | Write guard is application-layer (F-006) — import/corruption can bypass it, which is exactly why the read-back exists. |
| MIC-8 | Inventory: positions ≥ 0 read-back; reversal refs valid + single-use; consumption/waste `orderId`/`purchaseId` reference existing records | Fields verified (`inventory-material/types.ts:29-32`). |
| MIC-9 | Knowledge honesty: final orders' `resultStatus` vs snapshot knowledgeGaps; direct sales with unknown cost (informational count) | Verified null-on-unknown logic (`projectFinancialService.ts:618-639`). |
| MIC-10 | Retained-deposit visibility (INFO): count + total of `cancelled_retained` deposits — «قرار موثق، ليس إيرادًا بعد» | New — ties the FI-05 open decision to a surface without inventing accounting. |

Excluded from v1: the waste-vs-`loss_non_cash` double-report warning (no linkage field → no reliable signal; §1.4 item 5) and any archived-wallet check (no archive path exists — IC-5 analog N/A).

### 2.3 Activity-reader route placement (UX-06 «مزيد» reader)

**Resolution: `/finance/activity` (مالي family), route kind `surface` (reader keeps nav), entry from Home's «مزيد» text-action and a Finance truth-section text-action; `?from` return; canonical fallback `/finance`.**
Rationale: the question it answers is «شو صار اليوم/هالأسبوع؟» across money+work records — a reading task, not a thinking/calculation task, so it belongs to the finance reading family, not أدواتي (whose identity is «احسب قبل أن تلتزم») and not a new seat. Contract-26 additions required in the same change (route is surface-kind so no `deepFlowPatterns` entry, but the canonical fallback map needs the row).

### 2.4 Statement export format (MG-13 / UX-04 / FI-08)

**Resolution: Arabic Markdown file with UTF-8 BOM (Zman-proven: blob at `reports/page.tsx:181-182`), filename `micro-statement-<from>-<to>.md` with English digits and DD/MM/YYYY range, truth lines included verbatim; `navigator.share` text variant optional when the API exists; PDF explicitly deferred to the documents pipeline.**
Rationale: WhatsApp/email sharing of a `.md` file preserves structure and the BOM guarantees Arabic renders on Windows/Excel-adjacent tools; plain TXT loses the block/table structure accountants scan; PDF adds a rendering dependency for zero persona gain now. Content rules from FI-08 are binding: every money line carries its knowledge state; null result exports as «غير متاح — بيانات ناقصة» with reasons; amanah wording preserved; NO "صافي الربح النهائي"; NO balance-equation claim; header states generated-at + period + «قراءة من السجل المحلي».

### 2.5 Retained deposits (held but neither revenue, liability, nor amanah) — the owner's decision question

**Do NOT invent a new event type. Do not "fix" anything.** The decision question to put to the owner (formulated, not answered):

> «عند إلغاء طلب والاحتفاظ بعربونه (حالة "cancelled_retained"): ماذا يعني لك هذا المبلغ؟
> (١) مبلغ عاد إليك شخصيًا (رأس مال/سحب)؟
> (٢) إيراد مشروع عن فترة الإلغاء؟
> (٣) حالة معلنة معلّقة تظل ظاهرة حتى قرار لاحق؟
> اليوم يسجّل Micro القرار بلا أي أثر مالي — أي تغيير يحتاج عقدًا متخصصًا (نوع حدث جديد أو بعد دلتا جديد) قبل أي بناء.»

Interim rules (binding): statement/deposits layer wording «عربون محتفظ به — قرار موثق، ليس إيرادًا بعد» (SA-4's wording, confirmed); MIC-10 surfaces the totals as INFO. Verified basis: `settleDepositRetain` keeps `collectedMinor`, zeroes `receivableMinor`, writes a `deposit_retained` event, touches no revenue (`craft-order/policies.ts:814-885`).

### 2.6 Loan-out receivables (FI-09)

**Resolution: reject now — confirmed.** The principle (asset-not-expense) is already Micro's for business debts (order `debt`, sale `partial_debt`, parties ledger). A cash loan made from project money is unrepresentable today, and forcing it through `owner_withdrawal_cash` (corrupts owner capital) or `operating_expense_*` (corrupts profit) is the real hazard — mitigated immediately by a wording-only hint in the editor (folded into TR-08's effect-copy law: on the owner-withdrawal and expense editors, one line «قرض شخصي؟ لا يسجل هنا» style copy; no new type, no schema change).
Future contract requirements (if the owner ever decides): `FinancialEventType "loan_out_cash"` + sixth delta dimension `receivableDeltaMinor` (mirror of amanah: cash −1 / receivable +1, profit and owner untouched; repayment reverses both), parties-ledger reading, reversal through the existing correction model, schema + export major bump with `?? 0` legacy defaults, import validation extension. This is an independent Micro scope decision, never a Zman transfer.

---

## 3. Final ranked transfer set

Tiers: **P0** essential to professional completeness or financial safety · **P1** high-value workflow/discoverability · **P2** valuable, not required for the first implementation · **Reject** do not transfer.

### P0 — financial safety spine

| ID | Capability | Verdict | Micro name (plain Arabic) | Owning tab/screen | What transfers (adapted) | Dependencies | One-line rationale |
|---|---|---|---|---|---|---|---|
| TR-01 | Single period-result function + runtime cross-check (ZC-09 / FI-03) | adapt | «قراءة الفترة الواحدة» (internal discipline, no new screen) | مالي (application layer: `projectFinancialService`) | Designate `readRecordedPeriodResult` as THE canonical period-result function; every surface (Finance period view, Statement, Home facts) consumes or cross-checks it; public-surface test locks it | none | Two independent read paths can drift today; one honest reading is Micro's core promise — schema-free, cheap, makes the bounded-profit boundary enforceable. |
| TR-02 | Integrity self-check suite (ZC-16 / FI-04 / UX-03) | adapt | «فحص سلامة مالي» | أدواتي → `/tools/integrity` (surface route) + مالي truth-section doorway | Read-only CheckResult service (MIC-1..MIC-10, §2.2) + surface page with PASS/WARN/FAIL cards, per-record deep links, suggested fix as text-action; auto-suggest run after import/restore | **TR-01** (MIC-1) | Import/restore already shipped + local-first means only the app can catch corruption; makes correctness observable to a non-accountant owner. |

### P1 — high-value workflow / discoverability

| ID | Capability | Verdict | Micro name | Owning tab/screen | What transfers | Dependencies | One-line rationale |
|---|---|---|---|---|---|---|---|
| TR-03 | Statement export artifact (ZC-15 / FI-08 / UX-04) | adapt | «شارك الكشف» | مالي → `/finance/statement` (action group) + Finance period-layer footer action | Markdown+BOM download over the existing `StatementReading` (truth lines verbatim, knowledge states, corrections digest, position summary without equation); optional `navigator.share` text | TR-01 (sequence: export must reflect the canonical reading) | The one true MICRO-WEAKER gap: an artifact the owner can hand an accountant/family; zero writes, offline Blob. |
| TR-04 | Expense category tags (ZC-02 / FI-01 / UX-01) | adapt | «تصنيفي للمصاريف» | مالي → `FinancialEventEditor` secondary layer (inline field) + `/finance/statement` grouping block | Optional `categoryLabel` on `OperatingExpenseContext` + derived suggestion list (trim/collapse) + per-tag statement grouping + optional EventsLayer tag filter; **schema 30→31, export 22→23** | TR-03 for the statement block surface (field itself independent) | Answers «شو صار على البنزين؟» without touching a single delta or allocation boundary. |
| TR-08 | Written interaction laws (ZC-24 / UX-07 doc tier) | adapt (docs) | «قوانين الأثر والثبات» (design-contract update, no screen) | cross-cutting: docs/contracts + review gates | Effect-explaining copy as a review gate (incl. «لا حركة نقدية» negative case + loan-hint wording); header anti-jitter law; status-driven action matrix for OrderDetail documented; teaching empty states rule | none | Nearly free; protects every future group from re-importing Zman's pre-contract mistakes. |

### P2 — valuable, not required for the first implementation

| ID | Capability | Verdict | Micro name | Owning tab/screen | What transfers | Dependencies | One-line rationale |
|---|---|---|---|---|---|---|---|
| TR-05 | Unified recent-activity layer (ZC activities / MG-11+12 / UX-06) | adapt | «آخر ما صار» (Home block) + «سجل كل ما صار» (reader) | مشروعي الآن (Home block, cap 5–7) + `/finance/activity` reader | Tier 1: enrich Home read model (add direct sales, corrections, wallet entries; event rows link with `?event=` focus). Tier 2: full read-only reader over existing stores with per-kind rows and deep links | none (tier 2 needs owner nod on Home clutter + contract-26 fallback row) | One answer to «شو صار اليوم؟» without a sixth seat or a dashboard. |
| TR-06 | Waste visibility in money reading (ZC-18 residue / UX-09) | adapt | «هدر مخزون — بلا خروج نقد» rows | مالي → EventsLayer / truth strip (read-model join from `/inventory`) | Read-only rows for inventory waste movements (amount + source link, dash convention, never styled as cash expense) | rides TR-05's read model (same join) | Losses must be visible where money is read; Micro's reversible waste mechanics stay untouched. |
| TR-07 | Inventory edge contracts (ZC-07 residue / UX-02) | adapt | «استلم هذه المواد في المخزون» + zero-stock strip | مالي → `/suppliers/purchase/:id` (text-action bridge) + `/inventory` (strip) | Purchase→receipt bridge via `?purchase=` prefill (contract-26 vocabulary addition); quiet zero-stock strip; stated-consequences dialog law reserved for any future deactivation | none (bridge needs deep-link vocab + canonical fallback entry) | The honest version of Zman's automation: one deliberate tap, never silent. |
| TR-09 | Small interaction helpers (ZC-24 / UX-07 helper tier) | adapt | «تراجع ٥ ثوانٍ» + لصق المبالغ | cross-cutting (components/forms + application/input) | 5-second undo-delete for non-financial deletes only (estimates, future snippets — local writes make restore real); currency-label stripping («د.أ»/JOD/دينار) in the paste path of `englishNumeric` | TR-08 (laws first) | Cheap phone-craft parity; explicitly forbidden on financial records. |
| TR-10 | Reusable notes library (ZC-20 / MG-14) | adapt (gated) | «ملاحظاتي المتكررة» | أدواتي → new module (local non-financial store, CostEstimate precedent) | Title/body/category + copy-to-clipboard; optional «استخدم في» prefill for order specifications/agreement notes — **never prices** | owner/persona validation; ideally bundle its store decision with TR-04's schema-31 bump | Real daily friction for repetitive crafts, but unvalidated for this persona — build only after the owner confirms. |
| TR-11 | In-form draft persistence (NEW — ZC-01 DRAFT_KEYS residue) | adapt | «مسودة محفوظة» (restore banner) | cross-cutting: deep editors (`FinancialEventEditor`, cash/inventory/schedule editors) | Per-editor localStorage draft written on change, offered back on reopen (create-only, like Zman); Setup's `micro.setup-draft.v1` is the in-repo precedent | none (not schema; not order drafts — those are records) | Phone browsers refresh; today a mid-form crash loses everything the guard cannot save. |

### Reject — do not transfer (evidence + reason)

| ID | Capability (source) | Reason (binding) |
|---|---|---|
| TR-12 | Selective inventory automation core — auto-deduct on delivery, auto-capitalization, negative stock, zero-cost opening stock, untrack-with-history-delete (ZC-07) | Four hard Micro violations: estimates creating inventory effects; explicit-evidence bypass (contracts 11/13); non-negative invariant; missing≠zero. Micro already implements optional selection and immutable written cost stricter (`inventory-material/policies.ts`, `SupplierPurchaseEditor.tsx:303`). Edges live in TR-07. |
| TR-13 | Order→sale conversion + deposit reclassification + forfeit-as-revenue (ZC-06) | Second revenue path vs F-005; reclassifying past cash events violates append-only corrections; auto forfeit-as-revenue violates collection≠profit and the no-guessing rule for retained deposits. Micro's three-option settlement + CorrectionPreview are stronger (`craft-order/policies.ts:814-885`). Laws preserved in TR-08. |
| TR-14 | Assets & depreciation NOW (ZC-10) | «مؤجل بعقد متخصص — لا نخمن قواعدها» (verified `remaining-capabilities-review-v1.md`). Reject from the transfer set; pattern bank + gating condition recorded (§1.5-4). The `loss_non_cash` hook stays the only future entry point. |
| TR-15 | Loan-out receivables NOW (ZC-11) | Needs a sixth delta dimension + new event type = an independent Micro contract, not a transfer (§2.6). Wording hint folded into TR-08. |
| TR-16 | Global cross-record search (MG-20) + ZC-01 SmartFinanceForm as a whole + ZC-03 unified feed/pagination | Search: bounded volumes, per-surface search exists, TR-05 covers recent-item finding — Pilot observation only. SmartForm: pattern already present (QuickActionSheet modes + effect card); only draft persistence transfers (TR-11). Unified feed: folded into TR-05; UNION-ALL cursor pagination is a server-scale solution with no local-scale value. |
| TR-17 | Dashboard/analytics panels (ZC-14), auth/passcode/idle-lock (ZC-22), WhatsApp templates+automation (ZC-21), partial JSON backup (ZC-23), write-off dual-entry+immutability (ZC-18 mechanics), fils/ar-JO numerals & modal-create (ZC-24 residues) | Identity conflict with decision-first Home (MG-15); platform refusals — no auth/no cloud (MG-16/21, README/current-state §5); never-build list (MG-19); reverse gap — Micro's export/import is full+verified (MG-18); Micro's reversible waste is the compliant design (§1.5-6); Micro's numeric/deep-editor contracts are systemic rules (Group 6 item 5). |

**Coherence checks (passed):** nothing in P0 depends on an unaccepted P2 (TR-02 depends only on TR-01); nothing rejected is silently depended on — ZC-07's edges are explicitly accepted as TR-07; ZC-06's laws live in TR-08; ZC-18's visibility lives in TR-06; ZC-01's draft pattern lives in TR-11; ZC-03's feed ambition lives in TR-05; ZC-24's laws live in TR-08/TR-09.

---

## 4. Final transfer architecture

### 4.1 Reused from Micro as-is (zero modification)

- The **write path** (page → application service → domain → `PrototypeLocalStore` → IndexedDB) and its atomic `commit*` transactions — every accepted item either reads through it or adds a payload field through it; none adds a second write path.
- **Corrections system** (reversal/replacement records, reasons, `CorrectionPreview`, 11-kind history) — TR-04's label corrections, if ever requested, reuse `commitFinancialEventReplacement`.
- **`?from` navigation + contract 26** — every new surface (TR-02 `/tools/integrity`, TR-05 `/finance/activity`) registers a canonical fallback; TR-07 adds `?purchase=` to the closed deep-link vocabulary; nothing else changes.
- **Statement reading** (`statementService.read`) — TR-03 is a presentation function over it; TR-04's grouping block extends its read model.
- **QuickActionSheet** — untouched (5 actions, transitory philosophy preserved; no tag field in the sheet).
- **Bounded-profit discipline** — TR-01 *strengthens* it (null is a cross-checked value); TR-03 *exports* it (truth lines verbatim); nothing claims a final number.

### 4.2 What is adapted and where it lands

| Capability | Tab | Screen / surface | Data contract summary |
|---|---|---|---|
| TR-01 single result | مالي | none (application layer) | Pure-function designation + cross-check; zero records, zero schema. |
| TR-02 integrity suite | أدواتي (+ مالي doorway) | `/tools/integrity` surface route; Tools module-state row; Finance truth-section text-action | `CheckResult[] {id: MIC-*, titleAr, status, detailAr, offendingIds?, deepLinks?}` — read-only service over existing stores/read models; last-run as derived cache, not a store. |
| TR-03 statement export | مالي | `/finance/statement` action group + period-layer footer action | Markdown+BOM Blob from `StatementReading`; filename `micro-statement-<from>-<to>.md`; no writes, outside schema/export registries. |
| TR-04 category tags | مالي | `FinancialEventEditor` secondary `<details>` layer (inline field) + statement grouping block + optional EventsLayer filter | `OperatingExpenseContext += categoryLabel?: string|null` (≤80, trimmed); suggestions = derived DISTINCT list; **schema 30→31, export 22→23**, null default on import, no backfill. |
| TR-08 laws | cross-cutting | docs/contracts + review gates | Documentation: effect-copy rule (incl. loan hint + «لا حركة نقدية» case), header anti-jitter, OrderDetail action matrix, teaching empty states. |
| TR-05 activity layer | مشروعي الآن + مالي | Home block (cap 5–7) + `/finance/activity` reader (surface) | Unified derived read model over orders/drafts/events/sales/corrections/cash entries (one service, fixture-tested); rows deep-link via existing params (`?event=`, `/orders/:id`, `/cash/wallet/:id`). |
| TR-06 waste rows | مالي | EventsLayer / truth strip | Read-model join: waste movements → «هدر مخزون — بلا خروج نقد» rows with source links. |
| TR-07 inventory edges | مالي | `/suppliers/purchase/:id` text-action + `/inventory` strip | `?purchase=` prefill on `/inventory/movement/receipt` (contract-26 vocabulary + canonical fallback); zero-stock strip; dialog pattern reserved. |
| TR-09 helpers | cross-cutting | components/forms + application/input | 5s undo-delete component (non-financial deletes only); paste-stripping helper. |
| TR-10 snippets | أدواتي | new module (if validated) | Local non-financial store (CostEstimate precedent) + copy action; no price prefill, ever. |
| TR-11 draft persistence | cross-cutting | deep editors | Per-editor localStorage draft keys (Setup precedent `micro.setup-draft.v1`); create-only restore offer. |

### 4.3 What remains separate / deferred

- **Assets & depreciation** — reject-now, gated behind the owner-approved Micro contract; SA-4's FI-06 mechanics sketch (read-time depreciation, sweep, restatement policy, soft source link) is preserved verbatim as the pattern bank for that contract.
- **Loan-out receivables** — reject-now; future contract needs the sixth delta dimension (§2.6).
- **Retained-deposits classification** — owner decision question formulated (§2.5); until answered: documented decision, MIC-10 INFO, statement wording rule.

### 4.4 Dependency graph (build order)

```
TR-01 (canonical function) ──► TR-02 (MIC-1 uses it) ──► TR-03 (export reflects the canonical reading)
                                                        │
TR-04 (tags: schema 31 / export 23) ◄── bundle decision with TR-10 (snippets store, if validated)
        └─ statement grouping block rides TR-03's surface
TR-08 (laws) ──► TR-09 (helpers follow the laws)
TR-05 (activity: tier 1 free-standing; tier 2 needs owner nod) ──► TR-06 (waste rows join the same read model)
TR-07 (inventory edges) — free-standing (contract-26 vocabulary addition)
TR-11 (draft persistence) — free-standing
```

Statement export before category grouping (TR-03 → TR-04's block): the grouping block is a read-model extension of the same statement surface, so building the export first fixes the surface and format conventions (BOM, truth lines, knowledge states) the grouping must match.

### 4.5 Migration / compatibility statement

- **Only TR-04 (and optionally TR-10) touch the store:** schema **30→31**, export **22→23**; import migration defaults `categoryLabel → null` for older snapshots (pattern proven: `amanahDeltaMinor ?? 0`); no backfill — legacy null = «غير مصنّف», already surfaced honestly; lockstep: `normalizeExpenseContext` assertions, `validateSnapshot` extension, public-surface test, new editor/statement tests.
- **TR-01/TR-02/TR-03/TR-05/TR-06/TR-09/TR-11: schema-free** (TR-11 uses localStorage, not the store; TR-02's last-run is a derived cache). TR-02/TR-05 add routes → contract-26 canonical-fallback rows; TR-07 adds one deep-link vocabulary entry. These are contract-doc changes, not migrations.
- **TR-14/TR-15 (future, gated):** each is a major schema/export bump with import migration when its contract is approved.
- All accepted items honor: single write path, atomic `commit*`, per-intent idempotency keys (new stores get unique indexes — TR-10), import accepts older versions, no silent history rewrite, estimates never create effects, missing never zero.

### 4.6 How Micro's identity is preserved

- **Decision-first Home:** TR-05 enriches the *existing* bounded block (same visual weight, cap 5–7) and moves the full list to a separate reader; no panels, no analytics on Home.
- **Bounded profit:** TR-01 makes «غير متاح» a cross-checked first-class state; TR-03 exports the honesty (truth lines) instead of replacing it with an accountant-style P&L; nothing ever prints «صافي الربح النهائي».
- **Five seats:** no new seat; TR-02 lives under أدواتي (thinking-tool identity), TR-05's reader under the مالي family; discoverability via Tools module-states row + Finance text-actions (the «everything else» role Tools already owns).
- **Offline-first:** every accepted item is pure local read/write — export is a local Blob, integrity checks read local stores, drafts are localStorage; zero network, zero cloud, zero auth.

---

## 5. Implementation sequence and acceptance criteria

Order = dependency graph (§4.4). Per item: what "done" means + design-level test scenarios.

1. **TR-01 — canonical period-result function**
   - Done: `readRecordedPeriodResult` is the only producer of period-result numbers; Finance period view, Statement, and Home facts consume or cross-check it; a public-surface test locks the read API; no page contains inline period arithmetic.
   - Tests: (a) same store fixture → identical result line on Finance/Statement/Home; (b) fixture with an unknown-cost direct sale → all three surfaces render the same «غير متاح» + reasons (null never renders 0 anywhere); (c) regression: bounded-status flags unchanged (`recorded_only`/`incomplete`).
2. **TR-02 — «فحص سلامة مالي»**
   - Done: read-only service produces MIC-1..MIC-10; `/tools/integrity` surface renders PASS/WARN/FAIL cards with per-record deep links and text-action fix paths; Tools module-state row + Finance truth-section doorway; post-import auto-suggestion; zero new stores; last-run cached as derived data.
   - Tests: (a) clean fixture → all PASS, green banner; (b) seeded corruption (orphan sourceRef, unbalanced reversal, negative amanah, drifting statement line) → each surfaces as the designed WARN/FAIL with the right offending record link; (c) `cancelled_pending` + `needs_review` fixture → WARN (not FAIL); (d) `cancelled_retained` fixture → INFO line with totals; (e) run after import → suggested automatically; (f) zero writes (store snapshot hash unchanged before/after run).
3. **TR-03 — «شارك الكشف»**
   - Done: statement action group downloads `micro-statement-<from>-<to>.md` (UTF-8 BOM) with all blocks, source labels, corrections digest, truth lines verbatim; optional `navigator.share` when available; works offline; empty data → honest artifact.
   - Tests: (a) export of a known fixture matches the on-screen reading line-for-line; (b) null result → «غير متاح — بيانات ناقصة» + reasons, never 0; (c) artifact contains NO balance-equation claim and NO final-profit wording (wording review gate); (d) BOM present; filename digits English; range DD/MM/YYYY.
4. **TR-04 — «تصنيفي للمصاريف»** (schema 31 / export 23)
   - Done: optional tag field in the editor's details layer with derived suggestions (trim + collapse); tag visible on event rows; statement grouping block (collapsed by default); optional EventsLayer filter; import migration defaults null; no delta/allocation effect anywhere.
   - Tests: (a) tagged expense → deltas identical to untagged twin; (b) free-typed " بنزين " and "بنزين" → one vocabulary entry; (c) import of an export-22 file → labels null, statement still groups legacy as «غير مصنّف»; (d) round-trip export 23 → import → labels preserved; (e) shared-expense with tag → share math unchanged.
5. **TR-08 — laws documentation**
   - Done: effect-copy rule (incl. loan hint + negative-cash case), header law, OrderDetail action matrix, teaching-empty-state rule written into the design/product docs and referenced as a review checklist.
   - Tests: review-gate smoke: every money button on a new surface ships with a before-effect line (checklist item).
6. **TR-05 — activity layer**
   - Tier 1 done: Home block shows direct sales, corrections (labeled «تصحيح»), wallet entries; event rows link `/finance?layer=events&event=<id>`; cap 5–7.
   - Tier 2 done: `/finance/activity` reader over the unified read model with per-kind second lines, dash-for-non-cash, deep links, canonical fallback.
   - Tests: (a) fixture with one record of each kind → correct row per kind, correct link target; (b) correction row shows net effect dash/amount without implying cash; (c) read-model drift guard: one service, fixture-tested (same list on Home and reader within cap).
7. **TR-06 — waste visibility rows**
   - Done: waste movements appear in EventsLayer/truth strip as «هدر مخزون — بلا خروج نقد» with amount + link to `/inventory`.
   - Tests: waste fixture → row present, never counted in cash-in/out totals; reversal of waste → row disappears/updates per active-movement rule.
8. **TR-07 — inventory edges**
   - Done: «استلم هذه المواد في المخزون» text-action on supplier purchase records → receipt editor prefilled `?purchase=`; zero-stock quiet strip; `?purchase` in the closed vocabulary + canonical fallback.
   - Tests: (a) bridge hidden/disabled with honest copy when inventory not activated; (b) prefilled editor still requires explicit save (no auto-write); (c) strip lists only zero-quantity materials, quiet styling.
9. **TR-09 — helpers**
   - Done: 5s undo-delete used for estimate delete (and snippets if built) with local restore; paste stripping in `englishNumeric`.
   - Tests: delete→undo within 5s → record restored byte-identical; paste "12.50 د.أ" → 12.50; paste Arabic-Indic digits → normalized (already) — combined cases.
10. **TR-10 — snippets (only if owner validates; bundle the store decision with TR-04's bump)**
    - Done: أدواتي module with list/copy/create/edit/delete (undo-delete per TR-09); optional «استخدم في» prefill for order specifications text only.
    - Tests: copy puts body on clipboard; prefill fills text fields only — never price/cost fields; unique indexes + operation keys on the new store.
11. **TR-11 — draft persistence**
    - Done: participating editors persist a draft on change and offer restore on reopen (create mode only); discard clears the key; drafts never auto-save records.
    - Tests: fill → reload → banner offers restore → restored values equal; save → key cleared; edit mode → no draft offered (Zman rule); no interaction with UnsavedChangesGuard flow (guard still governs navigation).

---

## 6. Residual risks and open questions for the owner

**Risks (with mitigations):**
1. Integrity-suite false positives eroding trust — every check must be derived from a tested domain rule (not heuristics); deliberate states render as WARN/INFO (unknown openings, needs_review, retained deposits).
2. Export wording drift across future groups — TR-03's content rules are binding and review-gated; the artifact header states it is a reading, not a ledger.
3. Tag vocabulary drift splitting per-tag totals — accepted and documented (Zman parity); rename/merge deferred as documented corrections.
4. Tier-2 activity reader vs Home decision-first tension — capped block + separate reader + owner nod before building.
5. Read-model drift across 6+ stores for TR-05/TR-06 — single derived service, fixture tests (SA-3's mitigation, kept).
6. Bridge (TR-07) pressuring premature inventory use — text-action only, honest copy, no primary button.
7. Undo-delete misapplied to financial records — forbidden by TR-08's law; review gate.
8. Snippets built without persona validation — gated (TR-10) — do not build unless the owner confirms.
9. Draft persistence doubling state (guard vs draft) — drafts restore *input*, guard governs *navigation*; never auto-commit.

**Open questions for the owner (decision register):**
1. Retained deposits — the formulated question (§2.5). Nothing changes until answered; MIC-10 keeps it visible.
2. Category curation — is derived-only vocabulary enough, or do you want rename/merge later (documented corrections)?
3. Snippets — do you reuse repetitive specification text enough to want «ملاحظاتي المتكررة»? (Gate TR-10.)
4. Loan-out tracking — do you lend project cash to people? (Pilot evidence; contract per §2.6 if yes.)
5. Activity reader tier 2 — approve the `/finance/activity` reader or keep Home-only enrichment?
6. One-tap order closure — a Zman-trained habit («أغلق الطلب») to monitor in Pilot; do not build preemptively.
7. Export format acceptance — will your accountant/lender actually read Markdown? (If not, the documents pipeline PDF becomes the follow-up, not a format change.)
8. After device QA/import on real hardware: recalibrate MIC severities on real data.
9. (Observation only) large one-off purchase visibility — would a reading-layer note suffice until the asset contract decision?

---

## 7. Structured finding blocks (FINAL set)

```
finding_id: TR-01
capability_name: Single canonical period-result function + runtime cross-surface cross-check
source_product: Zman
comparison_classification: MICRO-WEAKER
zaman_evidence: artifacts/zman-app/src/features/finance/pnl.ts (computeOperatingPnl, LOCKED-6); integrityCheck.ts:1240+ (IC-13 — 3 sources × 2 periods, verified this review)
micro_evidence: application/finance/projectFinancialService.ts:433-639 (readRecordedPeriodResult); application/finance/statementService.ts (independent computation); application/home/homeControlCenterService.ts (position facts)
user_problem: two independent result read paths can drift and no runtime guard exists; the owner could see different numbers on Finance vs Statement
workflow_summary: designate one canonical function; all period-result surfaces consume or cross-check it; null-on-unknown is itself the cross-checked value
screen_and_navigation_summary: no new screen — application-layer discipline + public-surface test
financial_and_data_effect: zero writes; zero schema/export impact; strengthens the bounded-profit boundary (missing ≠ zero preserved)
transfer_recommendation: adapt — architecture only (the Zman formula is not copyable; the single-function + drift-check pattern is)
micro_destination: مالي (application layer: projectFinancialService)
priority: P0
confidence: high
risks: over-strict comparison crying wolf (limit cross-check to fields both models derive); statementService refactor scope (consume vs cross-check — start with cross-check)
open_questions: none material
```

```
finding_id: TR-02
capability_name: User-facing financial integrity self-check («فحص سلامة مالي»)
source_product: Zman
comparison_classification: ZAMAN-ONLY
zaman_evidence: artifacts/zman-app/src/features/finance/integrityCheck.ts (IC-1..IC-16); reports/components/IntegrityCheckReportPanel.tsx; reports/actions.ts (runFinancialIntegrityCheckAction)
micro_evidence: no integrity surface; structural equivalents verified: storage/local/IndexedDbLocalStore.ts (unique indexes, atomic commit*), application/transfers/localTransferService.ts:1007,2144 (import verifier + replaceSnapshot — shipped, user-reachable), application/finance/correctionHistoryService.ts, pages/CashCount.tsx (precedent)
user_problem: when a number "looks off" the owner has no one-tap verification of Micro's boundaries, reversal balance, or source integrity — trust is design-implied, never demonstrated
workflow_summary: Tools (or Finance doorway) → «افحص الآن» → overall PASS/WARN/FAIL banner + ≤10 Arabic check cards with per-record deep links and text-action fix paths; read-only; suggested after import/restore
screen_and_navigation_summary: أدواتي → /tools/integrity (surface route, keeps nav) + Tools module-state row + مالي truth-section text-action; canonical fallback /tools
financial_and_data_effect: zero writes; no new stores (last-run = derived cache); invariants per corrected MIC-1..MIC-10 (§2.2)
transfer_recommendation: adapt — interaction pattern + honesty copy wholesale; invariant set re-derived from Micro's domain with corrections (MIC-2′, MIC-5′, MIC-10 new)
micro_destination: أدواتي → /tools/integrity + مالي doorway
priority: P0
confidence: high
risks: false positives eroding trust (derive from tested rules; deliberate states = WARN/INFO); scope creep into auto-fix (forbidden — read-only)
open_questions: exact check wording sign-off; run-on-every-Finance-open vs on-demand (recommend on-demand + post-import suggestion)
```

```
finding_id: TR-03
capability_name: Statement export artifact («شارك الكشف»)
source_product: Zman
comparison_classification: MICRO-WEAKER
zaman_evidence: artifacts/zman-app/src/app/(app)/reports/page.tsx:170-202 (BOM Blob download — verified); reports/actions.ts:90-433 (downloadReport, 6 types)
micro_evidence: pages/Statement.tsx (no export logic — verified this review); application/finance/statementService.ts (StatementReading read model); localTransferService (JSON backup only)
user_problem: the owner cannot hand an accountant/lender/family a period document — every Micro reading is on-screen
workflow_summary: /finance/statement → «شارك الكشف» → Markdown+BOM file (or navigator.share text) mirroring the on-screen reading including truth lines verbatim
screen_and_navigation_summary: action group on the existing statement surface + Finance period-layer footer action; no new route
financial_and_data_effect: pure read → Blob; zero writes; outside schema 30/export 22; null result exports as «غير متاح — بيانات ناقصة»; NO final-profit wording; NO balance-equation claim
transfer_recommendation: adapt — export-the-read-model (Zman pattern), not a reports page
micro_destination: مالي → /finance/statement
priority: P1
confidence: high
risks: wording drift violating the bounded-profit boundary (binding content rules + review gate); Markdown readability for recipients (PDF later via documents pipeline)
open_questions: include insights export in v1 (recommend: no — statement only, one-slice rule)
```

```
finding_id: TR-04
capability_name: Expense category tags («تصنيفي للمصاريف»)
source_product: Zman
comparison_classification: MICRO-DIFFERENT
zaman_evidence: artifacts/zman-app/src/features/finance/components/SmartFinanceForm.tsx (category select/custom 883-936); finance/actions.ts:2639-2790 (lazy enrollment + CRUD); finance/queries.ts:902 (orphan-merge)
micro_evidence: src/domain/financial-event/types.ts:30-36 (OperatingExpenseContext — no label, verified); pages/FinancialEventEditor.tsx:354-377,448 (ExpenseClassification details layer — host verified); pages/Statement.tsx (grouping target)
user_problem: «شو صار على البنزين هذا الشهر؟» — Micro asks truth-context questions but keeps no named vocabulary, so grouping is manual note-reading
workflow_summary: optional tag field inside the existing details layer with derived suggestions (trim/collapse) → per-tag grouping block in the statement (collapsed by default) → optional EventsLayer tag filter
screen_and_navigation_summary: inline field (surface type 5) + reading block; no new page; no managed catalog in v1
financial_and_data_effect: label frozen on the event like the note; zero effect on the five deltas, sharedProjectShare, or resultMinor; schema 30→31 / export 22→23 with null-default import migration, no backfill
transfer_recommendation: adapt — free-tag vocabulary with derived read list (resolution §2.1); Zman's catalog CRUD NOT copied
micro_destination: مالي → /finance/new/operating_expense_* (field) + /finance/statement (block)
priority: P1
confidence: high
risks: label drift splitting totals (accepted, documented); future recurring-rules temptation (forbidden); statement clutter (block collapsed by default)
open_questions: rename/merge tooling after Pilot (only as documented corrections)
```

```
finding_id: TR-05
capability_name: Unified recent-activity layer («آخر ما صار» / «سجل كل ما صار»)
source_product: Zman
comparison_classification: MICRO-INCOMPLETE
zaman_evidence: artifacts/zman-app/src/app/(app)/activities/page.tsx (feed + deep links, verified); dashboard/queries.ts (getRecentActivities)
micro_evidence: application/home/homeControlCenterService.ts:398-437 (recentChanges — orders/drafts/events(generic)/schedules; directSales+corrections missing — verified); components/finance/EventsLayer.tsx (?event focus — verified); pages/Finance.tsx:88,955
user_problem: «شو صار اليوم/هالأسبوع؟» across orders, sales, expenses, corrections requires visiting 4+ surfaces
workflow_summary: tier 1 enriches Home's existing block (add direct sales, corrections, wallet entries; ?event= focused links; cap 5–7); tier 2 adds a full read-only reader at /finance/activity
screen_and_navigation_summary: Home inline block + surface-kind reader under the مالي family; canonical fallback /finance; never a seat or dashboard
financial_and_data_effect: pure derived read model over existing stores; corrections rows labeled «تصحيح» with net effect shown honestly (dash for non-cash); zero writes
transfer_recommendation: adapt — the question transfers, the surface does not
micro_destination: مشروعي الآن (block) + مالي → /finance/activity (reader)
priority: P2
confidence: high (tier 1); medium (tier 2 — owner nod on Home clutter)
risks: Home clutter vs decision-first principle (cap + same visual weight + «مزيد»); read-model drift across 6+ stores (one service, fixture tests)
open_questions: tier-2 approval; corrections as rows (recommend: yes, labeled)
```

```
finding_id: TR-06
capability_name: Waste visibility in the money reading («هدر مخزون — بلا خروج نقد»)
source_product: Zman
comparison_classification: MICRO-SUFFICIENT (mechanics) — visibility residue only
zaman_evidence: artifacts/zman-app/src/features/finance/components/PaymentsTab.tsx:410-427 (gray read-only write-off cards in the payments feed)
micro_evidence: src/domain/inventory-material/types.ts:10-32 (waste + wasteContext); pages/InventoryMaterials.tsx (waste only visible in inventory log); application/finance/projectFinancialService.ts:272-290 (waste as reading line)
user_problem: an owner scanning «السجل والأثر» never sees that material value evaporated — waste lives only in /inventory
workflow_summary: read-only join surfaces waste movements as rows in the EventsLayer/truth strip with amount + source link and the dash-for-non-cash convention
screen_and_navigation_summary: EventsLayer extension (مالي); no new route
financial_and_data_effect: zero writes; pure read-model join; never styled as cash expense
transfer_recommendation: adapt (visibility only) — ZC-18's dual-entry mechanics and immutability are REJECTED (Micro's reversible waste is the compliant design)
micro_destination: مالي → EventsLayer / truth strip
priority: P2
confidence: high
risks: labeling must never imply cash left (dash + «بلا خروج نقد»)
open_questions: also in Home recent block via TR-05 tier 1 (recommend: yes)
```

```
finding_id: TR-07
capability_name: Inventory edge contracts (purchase→receipt bridge + zero-stock strip)
source_product: Zman
comparison_classification: MICRO-DIFFERENT
zaman_evidence: artifacts/zman-app/src/app/(app)/catalog/CatalogClient.tsx:626-679 (stated-consequences untrack dialog — verified); features/inventory/InventoryScreen.tsx (low-stock banner); SmartFinanceForm.tsx (stock-aware picker)
micro_evidence: pages/InventoryMovementEditor.tsx:307 (receipt purchaseId select; ?order= prefill precedent); pages/SupplierPurchaseEditor.tsx:303 («لن يحوله إلى مخزون»); pages/InventoryMaterials.tsx (no zero-stock strip, no deactivation — verified)
user_problem: the deliberate receipt of already-recorded purchases takes too many steps, and zero-stock materials are invisible in the overview
workflow_summary: text-action «استلم هذه المواد في المخزون» on the purchase record → receipt editor prefilled ?purchase= (explicit save still required); quiet zero-stock strip; stated-consequences dialog law reserved for future deactivation
screen_and_navigation_summary: contextual text-action + strip; ?purchase joins the closed deep-link vocabulary; canonical fallback /inventory
financial_and_data_effect: prefill only — no auto-write; inventory effects still require the owner's explicit movement record (purchase≠COGS preserved)
transfer_recommendation: adapt (edges only) — the automation core is REJECTED (TR-12)
micro_destination: مالي → /suppliers/purchase/:id (bridge) + /inventory (strip)
priority: P2
confidence: high (rejection of core); medium (bridge value — owner validation)
risks: bridge pressuring premature inventory use (text-action, honest copy)
open_questions: «لم يُستلم بعد» state on purchase summary (supplier-purchase domain check needed)
```

```
finding_id: TR-08
capability_name: Written interaction laws (effect-copy, header stability, action matrix, teaching empty states)
source_product: Zman
comparison_classification: MICRO-SUFFICIENT (pattern-level)
zaman_evidence: artifacts/zman-app/docs/DESIGN_SYSTEM_V2_1_CONTRACT.md (§3.5, §8, §9); HEADER_AND_HOME_V2_2 + HEADER_CONCEPT_V2_3 (one-row header, anti-jitter)
micro_evidence: components/layout/MicroAppShell.tsx (stable header); pages/SupplierPurchaseEditor.tsx:298-308 (effect copy precedent); pages/OrderDetail.tsx (status-driven actions, undocumented)
user_problem: none open today; the risk is regression — future groups re-introducing modal-create, conditional headers, or unexplained money buttons
workflow_summary: codify Micro's existing (stronger) patterns as written review-gate laws: effect-before-action copy incl. the «لا حركة نقدية» negative case and a loan-hint line; header anti-jitter; OrderDetail action matrix; teaching empty states
screen_and_navigation_summary: cross-cutting documentation; no screen
financial_and_data_effect: none (wording + review gates)
transfer_recommendation: adapt (documentation) — rejects Zman's modal-create, fils display, ar-JO numerals
micro_destination: cross-cutting — docs/contracts + docs/product design-system update
priority: P1
confidence: high
risks: contract drift if not enforced in review (same PR-gate ritual Zman uses)
open_questions: fold into one design-system doc update (recommended)
```

```
finding_id: TR-09
capability_name: Small interaction helpers (5s undo-delete for non-financial deletes; paste-tolerant money input)
source_product: Zman
comparison_classification: MICRO-SUFFICIENT (pattern-level)
zaman_evidence: artifacts/zman-app/src/lib/undo-delete.ts (timer-commits pattern); src/lib/money.ts (parseJodToFils strips د.أ/JOD/دينار)
micro_evidence: components/forms/EnglishNumberInput.tsx:78 (normalizeAsciiDigits on change — digit parity already); application/input/englishNumeric.ts (no currency-label stripping); Tools estimate delete (two-step confirm today)
user_problem: minor friction: destructive non-financial deletes lack a grace window; pasting a formatted amount fails
workflow_summary: 5s undo-delete for estimates (and snippets if built) with true local restore; currency-label stripping helper in the paste path
screen_and_navigation_summary: cross-cutting components/forms + application/input
financial_and_data_effect: none on financial records — undo-delete is FORBIDDEN there (corrections path is stronger)
transfer_recommendation: adapt — Zman's online-guard complexity drops away (local writes restore for real)
micro_destination: cross-cutting
priority: P2
confidence: high
risks: misapplication to financial records (law forbids; review gate)
open_questions: none material
```

```
finding_id: TR-10
capability_name: Reusable notes library («ملاحظاتي المتكررة»)
source_product: Zman
comparison_classification: ZAMAN-ONLY
zaman_evidence: artifacts/zman-app/src/features/snippets/*; app/(app)/snippets/SnippetsClient.tsx (title/body/category, copy-to-clipboard)
micro_evidence: no snippet store in storage/local/types.ts (verified — no vocabulary anywhere); CostEstimate precedent for non-financial thinking-tool stores; Tools identity «احسب قبل أن تلتزم»
user_problem: repeatedly typing the same order specifications or follow-up phrases with no reuse
workflow_summary: أدواتي module → list grouped by category → copy-to-clipboard; optional «استخدم في» prefill for order specification/agreement notes (text only, never prices)
screen_and_navigation_summary: Tools module + module-state row; deep editor for create/edit
financial_and_data_effect: zero financial/inventory effects (thinking-tool store); unique indexes + operation keys on the new store; ideally bundled with TR-04's schema-31 bump
transfer_recommendation: adapt (gated on owner validation)
micro_destination: أدواتي → new module
priority: P2
confidence: high (classification); medium (value — needs persona validation)
risks: prefill weakening per-order truth discipline (binding guard: never autofill prices); build-without-validation
open_questions: does the persona reuse repetitive text enough? (owner decision)
```

```
finding_id: TR-11
capability_name: In-form draft persistence for deep editors (NEW — carried by no prior report)
source_product: Zman
comparison_classification: MICRO-INCOMPLETE
zaman_evidence: artifacts/zman-app/src/features/finance/components/SmartFinanceForm.tsx:339-359 (DRAFT_KEYS localStorage drafts + restore banner — verified)
micro_evidence: grep over apps/prototype-web/client/src — localStorage used ONLY by Setup (micro.setup-draft.v1, removed on completion: pages/Settings.tsx:211) and Settings; UnsavedChangesGuard.tsx:112 arms beforeunload but persists nothing; order drafts are records (not affected)
user_problem: a browser refresh or crash mid-entry (phone browsers do this) silently loses everything in a financial/cash/inventory editor — the guard warns, it cannot restore
workflow_summary: per-editor localStorage draft written on change; restore banner on reopen (create mode only, Zman rule); discard clears; save clears; never auto-commits a record
screen_and_navigation_summary: cross-cutting across deep editors (FinancialEventEditor, cash/inventory/schedule editors)
financial_and_data_effect: none until the owner explicitly saves; drafts are input, not records; not in schema/export
transfer_recommendation: adapt — Setup's own persisted draft is the in-repo precedent
micro_destination: cross-cutting — deep editors
priority: P2
confidence: medium (value clear; editor-by-editor rollout)
risks: dual-state confusion with UnsavedChangesGuard (drafts restore input; guard governs navigation); stale-draft confusion (banner states the date)
open_questions: which editors opt in first (recommend the financial-event editor — longest form)
```

```
finding_id: TR-12
capability_name: Selective inventory automation core (auto-deduct, auto-capitalization, negative stock, zero-cost opening, untrack-with-delete)
source_product: Zman
comparison_classification: MICRO-DIFFERENT
zaman_evidence: artifacts/zman-app/src/features/inventory/actions.ts:196-368,269 (deductForDelivery; negative allowed with note — verified); catalog/CatalogClient.tsx:626-679 (untrack soft-deletes history); finance/actions.ts:200-287 (auto-capitalization); ACCOUNTING_RULES §9
micro_evidence: src/domain/inventory-material/policies.ts (assertInventoryRemainsNonNegative; consumption-as-evidence); application/finance/projectFinancialService.ts:224-301 (derivePeriodCogs evidence model); pages/SupplierPurchaseEditor.tsx:303; docs/contracts/11,13
user_problem: none in Micro's model — the automation would CREATE problems (estimate-driven inventory effects, silent deductions, unknown→zero openings)
workflow_summary: n/a — rejected
screen_and_navigation_summary: n/a
financial_and_data_effect: rejection preserves: explicit evidence, purchase≠COGS, non-negative positions, missing≠zero
transfer_recommendation: reject — hard boundary decision (recorded at top of Reject tier); edges accepted as TR-07
micro_destination: n/a
priority: Reject
confidence: high
risks: a future "one-tap suggested consumption" re-introducing the violation if silent — allowed only as an explicit suggestion requiring a real write
open_questions: none for the reject
```

```
finding_id: TR-13
capability_name: Order→sale conversion + deposit reclassification + forfeit-as-revenue
source_product: Zman
comparison_classification: MICRO-SUFFICIENT
zaman_evidence: artifacts/zman-app/src/features/finance/actions.ts:1441-1638 (convertOrderToSale — reclassify verified 1550-1552), 2020-2232 (forfeitDeposit)
micro_evidence: src/domain/craft-order/policies.ts:368-449 (revenue on order at delivered/settled), 814-885 (settleDeposit — retain keeps collectedMinor, no revenue — verified); application/collections/collectionService.ts:194-204 (single distributeUnallocated path)
user_problem: none — the Zman flow solves a bookkeeping problem (revenue-as-sale double-counting) Micro does not have
workflow_summary: n/a — rejected
screen_and_navigation_summary: n/a
financial_and_data_effect: rejection preserves: F-005 revenue-once, append-only corrections (no cash-event mutation), collection≠profit, no-guessing on retained deposits
transfer_recommendation: reject — laws (cash-effect copy, documented inverses) preserved in TR-08
micro_destination: n/a
priority: Reject
confidence: high
risks: none from rejection; risk only if partially ported (reclassify-style fix tools)
open_questions: retained-deposit classification decision (§2.5) remains an owner question, not a transfer
```

```
finding_id: TR-14
capability_name: Assets & depreciation (NOW)
source_product: Zman
comparison_classification: ZAMAN-ONLY
zaman_evidence: artifacts/zman-app/src/features/depreciation/* (read-time depreciation, sweep, prompt modal); ACCOUNTING_RULES §10
micro_evidence: docs/decisions/remaining-capabilities-review-v1.md («مؤجل بعقد متخصص … لا نخمن قواعدها» — verified); src/domain/financial-event/types.ts (loss_non_cash hook only); no asset store anywhere
user_problem: real but rare for the persona (machine/oven purchases cannot spread cost); period result overstated for asset-heavy crafts
workflow_summary: n/a — rejected now; pattern bank + gating condition recorded (§1.5-4)
screen_and_navigation_summary: future (post-contract): مالي deep editor + /finance/assets reading surface with two-section honesty
financial_and_data_effect: future contract must express depreciation only as declared non-cash reduction with knowledge state via loss_non_cash machinery; schema major bump when built
transfer_recommendation: reject (now) — gated future via owner-approved Micro specialized contract
micro_destination: n/a (future design sketch preserved from FI-06)
priority: Reject
confidence: high
risks: premature build = the exact «نخمن قواعدها» violation; dual-profit-label confusion if styled as expense
open_questions: the contract itself (straight-line only?, disposal, partial months, restatement) — owner-level
```

```
finding_id: TR-15
capability_name: Loan-out receivables (cash loans made from project money)
source_product: Zman
comparison_classification: ZAMAN-ONLY (for loans made; MICRO-SUFFICIENT for business debts)
zaman_evidence: artifacts/zman-app/src/features/finance/db.ts:68-69 (receivable, receivable_payment); PROMPT_RECEIVABLES.md
micro_evidence: craft-order SettlementStatus debt; direct-sale partial_debt; application/parties/partyLedgerService.ts; financial-event types (no loan-out type — verified); current-state.md §5 (no new slices)
user_problem: a cash loan made today is unrepresentable — recording it as owner_withdrawal or expense corrupts owner capital / profit truth
workflow_summary: n/a — rejected now; wording-only hint folded into TR-08
screen_and_navigation_summary: n/a
financial_and_data_effect: future contract needs FinancialEventType loan_out_cash + receivableDeltaMinor sixth dimension (mirror of amanah), schema/export major bump with ?? 0 legacy defaults
transfer_recommendation: reject (now) — independent Micro scope decision, never a transfer
micro_destination: n/a
priority: Reject
confidence: high (classification); medium (persona need — INFERENCE: home-business owners do lend cash)
risks: mis-recording loans under existing types today (mitigated by TR-08 hint)
open_questions: does the Pilot persona need loan tracking? (owner decision)
```

```
finding_id: TR-16
capability_name: Global cross-record search (defer) — plus ZC-01 SmartForm-as-a-whole and ZC-03 unified feed/pagination (folded)
source_product: Zman
comparison_classification: MICRO-WEAKER (search); MICRO-SUFFICIENT (smart-entry pattern; feed at local scale)
zaman_evidence: artifacts/zman-app/src/features/dashboard/components/GlobalSearch.tsx; SmartFinanceForm.tsx (mode selector + hints); queries.ts getPayments (UNION ALL cursor pagination)
micro_evidence: pages/Parties.tsx (per-surface search); components/layout/QuickActionSheet.tsx:57-79 (5-action mode selector — verified); pages/FinancialEventEditor.tsx (effect card); EventsLayer («السجل كاملًا» pagination)
user_problem: finding an old record requires knowing its surface — bounded at persona scale (hundreds of records, INFERENCE)
workflow_summary: n/a — deferred/folded: recent-item finding served by TR-05; mode+hint pattern already Micro's; draft persistence survives as TR-11
screen_and_navigation_summary: n/a
financial_and_data_effect: none
transfer_recommendation: reject (now — Pilot observation for search); reject (pattern already present) for ZC-01; skip pagination (server-scale)
micro_destination: n/a
priority: Reject
confidence: medium (search deferral is a judgment call on persona evidence)
risks: none material; revisit search if Pilot shows cross-surface hunting
open_questions: Pilot observation only
```

```
finding_id: TR-17
capability_name: Rejected platform/identity items — dashboard panels, auth/passcode/idle-lock, WhatsApp templates+automation, partial JSON backup, write-off dual-entry+immutability, fils/ar-JO numerals + modal-create
source_product: Zman
comparison_classification: NOT-A-TRANSFER-CANDIDATE (auth/WhatsApp); MICRO-DIFFERENT with identity conflict (dashboard); MICRO-SUFFICIENT/reverse gap (backup); MICRO-SUFFICIENT (write-off mechanics)
zaman_evidence: features/dashboard/components/*; src/middleware.ts + auth/IdleLock.tsx; src/lib/whatsapp.ts; src/components/shared/BackupModal.tsx (export-only, no restore — verified SA-1); inventory/actions.ts adjustStock (immutable write-off)
micro_evidence: pages/Home.tsx (decision-first «الأهم الآن»); README + current-state.md §1/§5 (no auth/no cloud); docs/decisions/remaining-capabilities-review-v1.md never-build row (WhatsApp automation — verified); localTransferService (full verified export/import); inventory reversible waste
user_problem: none — each rejection is either a platform refusal, an identity conflict, a reverse gap, or a weaker mechanical design
workflow_summary: n/a
screen_and_navigation_summary: n/a
financial_and_data_effect: rejections preserve decision-first Home, offline-first local-only posture, verified restorable backup, traceable corrections
transfer_recommendation: reject (all)
micro_destination: n/a
priority: Reject
confidence: high
risks: none
open_questions: idle-lock revisited only if Pilot shows shared-device usage (MG-21 open question preserved)
```

---

*End of SA-5 report. Built from the four prior sub-agent reports plus independent re-verification in both read-only clones (zman @ bdd63ab, micro @ 4db6a5f). Neither product repo was modified; only this report file and the worklog entry were written.*
