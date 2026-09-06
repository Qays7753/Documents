# 09 — Gaps, Conflicts, and Recommendations

20 registered gaps/conflicts. Nothing was fixed during this analysis task
(read-only mandate); each gap carries severity, user impact, financial risk, evidence, and a
recommendation for a later implementation phase. Planned-by-design items are *not* defects —
they are recorded so the future state stays honest.

| ID | Title | Severity | Status |
| --- | --- | --- | --- |
| GAP-01 | No conversational/AI assistant | low | PLANNED_OR_CONCEPTUAL |
| GAP-02 | Supplier offers / market not implemented | info | PLANNED_OR_CONCEPTUAL |
| GAP-03 | External delivery assignment not implemented | info | PLANNED_OR_CONCEPTUAL |
| GAP-04 | Docs staleness: deferred-capabilities plan marks implemented items as not executed | medium | CONFLICTING |
| GAP-05 | Contract numbering collision (18-23 used twice) | low | CONFLICTING |
| GAP-06 | No party entity: names are not merged or deduplicated | low | NOT_FOUND |
| GAP-07 | reviseOrderCost domain policy not wired to any page | medium | PARTIALLY_IMPLEMENTED |
| GAP-08 | Deep-link vocabulary closed but page-local params outside it | low | CONFLICTING |
| GAP-09 | No automated browser QA in CI | low | NOT_FOUND |
| GAP-10 | Single-user only; no employee/partner access | info | PLANNED_OR_CONCEPTUAL |
| GAP-11 | No sync / multi-device | medium | PLANNED_OR_CONCEPTUAL |
| GAP-12 | POS / cart deferred behind sector pilot | info | PLANNED_OR_CONCEPTUAL |
| GAP-13 | Taxes / payroll / legal fees out of scope | info | NOT_FOUND |
| GAP-14 | Multi-currency question open (EX-O13) | low | PLANNED_OR_CONCEPTUAL |
| GAP-15 | Open owner questions in network contracts (EX-O09/O10/O11/O14) | low | PLANNED_OR_CONCEPTUAL |
| GAP-16 | C2 'Review' composite memo not implemented (by design) | info | PLANNED_OR_CONCEPTUAL |
| GAP-17 | Statement share depends on Web Share availability | low | IMPLEMENTED |
| GAP-18 | Duplicated contract 04 sync states not surfaced in UI | info | PLANNED_OR_CONCEPTUAL |
| GAP-19 | Only one CI workflow; no scheduled/nightly run | low | NOT_FOUND |
| GAP-20 | Loan detail lacks schedule/interest modeling | info | NOT_FOUND |

## Details

### GAP-01 — No conversational/AI assistant

- **Severity:** low
- **User impact:** Guidance exists (guided entry, previews, integrity check, suggestions) but there is no question-and-answer assistant; the approved concept of an assistant preparing drafts for confirmation is not implemented.
- **Financial risk:** None (no silent writes possible by design).
- **Status:** PLANNED_OR_CONCEPTUAL
- **Evidence:** No LLM/AI deps in apps/prototype-web/package.json; grep ai/llm/chatgpt: nothing; docs/product/guidance-interaction-policy-v1.md; docs/product/deferred-capabilities-execution-plan-v1.md (deciding AI rejected)
- **Recommendation:** If wanted, implement assistant drafts strictly as FormDraft envelopes requiring explicit confirmation (BOT-02 future state); never let it write financial events directly.

### GAP-02 — Supplier offers / market not implemented

- **Severity:** info
- **User impact:** Owners cannot receive supplier offers; Tools shows a disabled «السوق والتوصيل» placeholder.
- **Financial risk:** None today; future rule already contracted (offers are announcements, never commitments).
- **Status:** PLANNED_OR_CONCEPTUAL
- **Evidence:** pages/Tools.tsx:133,337; docs/contracts/20-market-need-response-listing-moderation-contract.md
- **Recommendation:** Keep placeholder honest; implement only after E-00 expansion decision; verify approved rule at build time.

### GAP-03 — External delivery assignment not implemented

- **Severity:** info
- **User impact:** No courier assignment/tracking; delivery is customer-handover only.
- **Financial risk:** None today.
- **Status:** PLANNED_OR_CONCEPTUAL
- **Evidence:** docs/contracts/21-delivery-request-quote-status-privacy-contract.md (contract only); grep deliveryCompany: docs only
- **Recommendation:** Future state per contract 21-N; keep scope privacy matrix when built.

### GAP-04 — Docs staleness: deferred-capabilities plan marks implemented items as not executed

- **Severity:** medium
- **User impact:** A reader of docs only would wrongly conclude inventory/corrections are unimplemented; risk of wrong re-planning.
- **Financial risk:** None (code is the truth).
- **Status:** CONFLICTING
- **Evidence:** docs/product/deferred-capabilities-execution-plan-v1.md lists «مخزون واستهلاك… غير منفذ» while application/inventory + contract 28 are fully implemented; todo.md open item
- **Recommendation:** Update the deferred plan + todo.md statuses in a docs-only change; decision-18-accounting already records similar gating drift.

### GAP-05 — Contract numbering collision (18-23 used twice)

- **Severity:** low
- **User impact:** Ambiguous references (e.g. 'contract 21' is both guided-opening-import and delivery-request).
- **Financial risk:** None.
- **Status:** CONFLICTING
- **Evidence:** docs/contracts/ contains 35 files: local line 18-23* and network line 18-23
- **Recommendation:** Key traceability on filenames, not numbers (as this atlas does); consider renumbering the network line in a docs-only PR.

### GAP-06 — No party entity: names are not merged or deduplicated

- **Severity:** low
- **User impact:** Same person typed differently ('أبو أحمد' vs 'ابو احمد') stays two ledger rows; no editing/merging of party names.
- **Financial risk:** Low: receivable totals still correct per name; aggregation readability suffers.
- **Status:** NOT_FOUND
- **Evidence:** application/parties/partyLedgerService.ts (name-level only, PA-010); Conflict B (approved: no forced party)
- **Recommendation:** Consider a rename/merge correction path for party names (documented, like other corrections) in a future iteration.

### GAP-07 — reviseOrderCost domain policy not wired to any page

- **Severity:** medium
- **User impact:** Cost revision after agreement requires the documented needs_review path (spec revision) — the dedicated 'modify agreement' surface (problem §5-18) awaits an owner decision.
- **Financial risk:** None (safe default: knowledge-honest review path exists).
- **Status:** PARTIALLY_IMPLEMENTED
- **Evidence:** docs/operations/decision-18-accounting.md (agent must not build it alone); src/domain/craft-order/policies.ts:470 (exists, unwired)
- **Recommendation:** OWNER_DECISION_REQUIRED (already tracked as problem §5-18): choose 'modify agreement' price review vs cancellation-only.

### GAP-08 — Deep-link vocabulary closed but page-local params outside it

- **Severity:** low
- **User impact:** ?source (Collect), ?intent/?estimate/?product/?entry/?order/?sale are defensively parsed per page but not part of contract 26's closed vocabulary list.
- **Financial risk:** None.
- **Status:** CONFLICTING
- **Evidence:** app/navigationContract.ts:15-39 (vocabulary); pages/Collect.tsx:38-41 (?source); docs/contracts/26 §deep-link dictionary (reserves many names)
- **Recommendation:** Fold page-local params into the contract vocabulary (or document them as page-local by design) in a docs-only change.

### GAP-09 — No automated browser QA in CI

- **Severity:** low
- **User impact:** UI journeys rely on DOM tests + manual browser evidence; CI covers build + unit/DOM.
- **Financial risk:** Low.
- **Status:** NOT_FOUND
- **Evidence:** .github/workflows/ci.yml (10 steps; no browser step); docs/quality/* manual QA evidence
- **Recommendation:** Consider a lightweight Playwright smoke (setup→sale→offline reload) as a future CI step.

### GAP-10 — Single-user only; no employee/partner access

- **Severity:** info
- **User impact:** Owners cannot delegate any recording to staff.
- **Financial risk:** None today; network roles are contracted but unbuilt.
- **Status:** PLANNED_OR_CONCEPTUAL
- **Evidence:** ARCHITECTURE.md (no Auth/no multi-user); docs/contracts/18-network-identity-workspace-access-contract.md
- **Recommendation:** Keep out of local scope; revisit with E-00 expansion.

### GAP-11 — No sync / multi-device

- **Severity:** medium
- **User impact:** Data lives on one browser profile; moving devices requires export/import; contract 04 defines the future sync states honestly.
- **Financial risk:** Low (verified export/import path exists).
- **Status:** PLANNED_OR_CONCEPTUAL
- **Evidence:** docs/contracts/04-limited-sync-contract.md (target states local_only→pending_sync→synced); grep network calls: zero
- **Recommendation:** Planned phase per deferred plan step 12; keep honest 'no sync in this version' copy until then.

### GAP-12 — POS / cart deferred behind sector pilot

- **Severity:** info
- **User impact:** Fast repeat retail sales are handled by direct sales + catalog; no cart.
- **Financial risk:** None.
- **Status:** PLANNED_OR_CONCEPTUAL
- **Evidence:** docs/decisions/pos-sector-gate-v1.md
- **Recommendation:** Respect the gate: only after Group 5 + sector pilot evidence.

### GAP-13 — Taxes / payroll / legal fees out of scope

- **Severity:** info
- **User impact:** No tax lines; salary-like costs only via entitlement policies.
- **Financial risk:** None by scope decision.
- **Status:** NOT_FOUND
- **Evidence:** docs/product/deferred-capabilities-execution-plan-v1.md (needs Jordanian source)
- **Recommendation:** Await Jordanian regulatory source before design.

### GAP-14 — Multi-currency question open (EX-O13)

- **Severity:** low
- **User impact:** JOD only.
- **Financial risk:** None today.
- **Status:** PLANNED_OR_CONCEPTUAL
- **Evidence:** docs/contracts/25-network-money-representation-contract.md (EX-O13 open)
- **Recommendation:** OWNER_DECISION_REQUIRED (tracked in network line; future state only).

### GAP-15 — Open owner questions in network contracts (EX-O09/O10/O11/O14)

- **Severity:** low
- **User impact:** Future-state parameters (48h no-quote default, routing semantics, contact channel, end-customer consent) undecided.
- **Financial risk:** None today.
- **Status:** PLANNED_OR_CONCEPTUAL
- **Evidence:** contracts 21-N/24-N EX markers
- **Recommendation:** Recorded for the future expansion; not blocking any current flow.

### GAP-16 — C2 'Review' composite memo not implemented (by design)

- **Severity:** info
- **User impact:** Review exists as financial pulse + per-order cards (current two-level composite); the C2 memo proposed a pilot redesign only.
- **Financial risk:** None.
- **Status:** PLANNED_OR_CONCEPTUAL
- **Evidence:** docs/decisions/review-finance-c2-decision-v1.md (PROPOSED memo)
- **Recommendation:** Reopen only on repeated measurable pilot confusion (per the decision itself).

### GAP-17 — Statement share depends on Web Share availability

- **Severity:** low
- **User impact:** On browsers without Web Share, owner falls back to copy-text.
- **Financial risk:** None (text is user-edited first).
- **Status:** IMPLEMENTED
- **Evidence:** pages/SharePreview.tsx (share/copy buttons); lib/textDelivery.ts
- **Recommendation:** Acceptable; keep the editable preview as the guard.

### GAP-18 — Duplicated contract 04 sync states not surfaced in UI

- **Severity:** info
- **User impact:** UI never claims sync; honest local-only copy everywhere (compliant).
- **Financial risk:** None.
- **Status:** PLANNED_OR_CONCEPTUAL
- **Evidence:** docs/contracts/04-limited-sync-contract.md (future states); pwa/PwaRuntimeNotice.tsx
- **Recommendation:** None needed now; implement states with the sync phase.

### GAP-19 — Only one CI workflow; no scheduled/nightly run

- **Severity:** low
- **User impact:** Regressions caught on PRs/pushes only.
- **Financial risk:** None.
- **Status:** NOT_FOUND
- **Evidence:** .github/workflows/ci.yml (push+PR triggers only)
- **Recommendation:** Optionally add a weekly main-branch run.

### GAP-20 — Loan detail lacks schedule/interest modeling

- **Severity:** info
- **User impact:** Loans track principal and repayments only; no interest or installment schedule (out of scope by contract 29).
- **Financial risk:** None by design.
- **Status:** NOT_FOUND
- **Evidence:** src/domain/loan/types.ts (no interest fields); contract 29
- **Recommendation:** Keep out of scope unless owner requests interest tracking.


## Recommendations priority (analysis opinion, not implemented)

1. **Docs hygiene (low effort, removes contradictions):** update the deferred-capabilities plan
   statuses (GAP-04), renumber or disambiguate contract numbers 18–23 (GAP-05), and fold
   page-local params into the navigation contract vocabulary (GAP-08).
2. **Owner decision pending (§5-18):** the 'modify agreement' price-review surface — the domain
   policy `reviseOrderCost` exists but is deliberately unwired pending the owner's answer
   (GAP-07). Do not build it without that decision.
3. **Later iterations:** party-name merge/rename correction path (GAP-06); browser smoke in CI
   (GAP-09).
4. **Keep as-is:** planned network expansion, POS gate, sync phase — already honestly
   represented in the UI (disabled placeholder, no-sync copy).
