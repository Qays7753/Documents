# 10 — Owner Review and Decision Register

## Decisions already approved and verified as implemented

20 of
22 registered decisions are implemented and evidenced (see report 08).
The owner is **not** asked to re-decide any of them; this register exists for traceability.

## Open owner-decision items (recorded, not blocking)

- **GAP-07 — reviseOrderCost domain policy not wired to any page** (medium): OWNER_DECISION_REQUIRED (already tracked as problem §5-18): choose 'modify agreement' price review vs cancellation-only.
- **GAP-14 — Multi-currency question open (EX-O13)** (low): OWNER_DECISION_REQUIRED (tracked in network line; future state only).
- **GAP-15 — Open owner questions in network contracts (EX-O09/O10/O11/O14)** (low): Recorded for the future expansion; not blocking any current flow.

## Planned/conceptual decisions awaiting future phases

- **DEC-POS — POS sector gate** — status PLANNED_OR_CONCEPTUAL; source: docs/decisions/pos-sector-gate-v1.md
- **DEC-25 — Decision 25 — multi-activity profiles direction** — status PLANNED_OR_CONCEPTUAL; source: docs/decisions/25-multi-activity-core-profiles-v1.md

## Standing guidance for future decisions

- Any future doc that conflicts with the current contract-to-code table must update contract +
  decision log + tests together (the repository's own reading rule in
  `docs/implementation/02-domain-contract-coverage.md`).
- The five financial boundaries are non-negotiable invariants for any new capability.
- External-party features (supplier offers, delivery companies) must enter only through the
  E-00 expansion contracts with their privacy and money-representation rules
  (announced amounts are never expenses or commitments).

## No new decisions required by this analysis

This atlas introduced **no new OWNER_DECISION_REQUIRED items**: all findings either match
approved decisions, or were already tracked (§5-18 / EX-O*). Items to watch are listed above
under "Open owner-decision items".
