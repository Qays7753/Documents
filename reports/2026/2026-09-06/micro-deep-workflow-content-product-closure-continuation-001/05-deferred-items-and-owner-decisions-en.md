# 05 — Deferred Items and Owner Decisions

Nothing in this list blocks release. Each item is documented with evidence and a proposed decision path. No irreversible guess was implemented on any of them.

## 1. NEEDS_OWNER_DECISION — FC-02: direct in-place edit of a financial event

**The conflict.** The assignment's contract 2 specifies two correction paths for an old financial event:
- (a) direct edit that mutates the event while preserving history **inside the same event** (old/new values, changed fields, actor, timestamp, reason, affected period, linked records);
- (b) a current-period corrective reversal (linked, idempotent).

The repository already carries an approved decision — **decision C1 (correction boundary)** — that explicitly forbids silent in-place mutation of financial history and mandates **atomic reverse-and-replace**: a reversal event plus a replacement event in one transaction, original values preserved verbatim, reason required, double-reversal prevented. That is what Micro implements (EventsLayer → `projectFinancialService` atomic correction), and this run strengthened it with the FC-03 cross-month period warning and its dom test.

**Why it was not "fixed".** Implementing path (a) on top of path (b) would create two competing correction semantics in one ledger — exactly the "second financial truth engine" the product forbids — and would require rewriting the correction boundary the repository has documented as approved. Choosing between them is a genuine owner decision, not an engineering gap.

**Evidence anchors.** `docs/decisions` correction boundary (C1); `EventsLayer.tsx` correction surface; `projectFinancialService.ts` atomic correction; `EventsLayer.familyGuard.dom.test.tsx` (this run's FC-03 test).

**Proposed decision path for the owner.** Keep the atomic reverse-and-replace as the only correction semantic (recommended — it is implemented, tested, and preserves the audit trail by construction), and record contract 2 path (a) as satisfied-by-design: the "history inside the event" requirement is met by the linked reversal + replacement pair, which is stronger than in-place history. If the owner instead insists on literal in-place edits, it is a schema-level change (revision list on the event, readers honoring revisions) and should be scoped as its own project.

## 2. Deferred P3 items (documented, safe to defer)

| ID | Item | Evidence | Why deferred | Proposed next step |
| --- | --- | --- | --- | --- |
| FC-06 | Deposit refund does not mirror a manual wallet attribution (refund covers the unallocated default) | `fulfillmentService` refund path vs compound reversal in `OrderDetail` | Edge case: only reachable when the owner manually re-attributed unallocated cash to a specific wallet before refunding a deposit; the compound reversal surface already handles the common path | Extend the refund path to consume `wallet_allocation` metadata when present; add an adversarial test mirroring the compound-reversal suite |
| AV-07 | `needs_review` nextAction text promises «ألغِ موثقًا» but the cancel surface is hidden at that status (cancel is exposed only for pre-delivery statuses) | `craft-order/policies.ts` reverseDelivery sets `nextAction`; `OrderDetail.tsx` preDeliveryStatuses gate | Status-machine policy decision: whether cancellation should be allowed at needs_review (with deposit/collection guards) or the nextAction text should change | Owner picks one; smallest fix is rewording the nextAction to «راجع الطلب — أعِد التنفيذ أو اكمل التسليم» until cancellation policy changes |
| AV-08 | Depreciation reversal after disposal resurrects the disposed asset's book value (+3000 in the adversarial repro) | asset service reversal guards | Requires an explicit invariant (no depreciation reversal after disposal) plus a domain test | One-line domain guard + one test; candidate for the next hygiene pass |
| AV-09 | `FinancialEventEditor` localStorage draft restore lacks the defensive coercion other editors have (garbage in storage could render a broken form) | contrast `FinancialEventEditor` vs `DirectSaleEditor` restore paths | Defense-in-depth only; no known reachable corruption path (drafts are version-guarded at write) | Copy the coercion helper from `DirectSaleEditor`; one dom test with a corrupted draft |
| WF-04 | Expense category label not correctable after save (EventsLayer edit form covers amount/date/note/counterparty only) | `EventsLayer` edit fields; Statement promises «صنّفها من محرر المصروف» | The promise is honest for unclassified expenses (the editor does offer classification on creation); correction of classification after the fact is a feature request | Extend `FinancialEditInput` with expenseContext on the atomic replacement; add a dom test |

## 3. Test-count deltas and known non-blocking observations

- Prototype suite: 794 (baseline) → 818 (final). The stopped run contributed +21 (idempotency, loan guard, family guard, waste, deposit, characterization pins); this continuation added +5 (AV-04 ×2, AV-05 import forgery, AV-06, FC-03) and repaired 3 fixture sites without weakening any negative test.
- Domain suite: 277 → 278 (AV-05).
- The >500 kB main-chunk build warning is pre-existing (present at baseline; documented in prior reports). Code-splitting remains a recommended P3 performance follow-up, not a regression.
- The density cap raise for Orders (77→79) is recorded with the repo's ratchet convention (dated, justified, canonical labels only). No other cap moved.

## 4. Recovery artifacts (local, not part of the repositories)

- Branch `recovery/deep-closure-partial-work-2026-09-06` — points at the stopped run's last commit `c29ad39` (the uncommitted work itself was preserved in the working tree and is now committed on the continuation branch).
- Offline bundles: `/home/z/my-project/micro-closure-baseline-recovery.bundle` (baseline, from the stopped run) and `/home/z/my-project/micro-closure-recovery-continuation.bundle` (all refs at continuation start).
- These exist outside both repositories and contain no secrets.
