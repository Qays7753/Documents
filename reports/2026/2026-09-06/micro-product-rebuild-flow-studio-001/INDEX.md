# INDEX — Stable Identifier Catalog (Flow Studio delivery)

Baseline: Micro `main` @ `4af025d38f04dfb36ee645a4f9ca3345e362bf5b` · Atlas @ `622af98` · analysis date 2026-09-07.
Imported Atlas identifiers are unchanged from the Atlas INDEX; new namespaces are disjoint and never reuse an existing ID.

## New namespaces in this delivery

| Collection | Count | ID pattern | Examples |
| --- | --- | --- | --- |
| Target features | 17 | `FTR-001`…`FTR-017` | FTR-001 Login, FTR-005 Product-to-Sale, FTR-015 Assistant (FUTURE), FTR-017 Cashboxes |
| Target flows | 17 | `FLW-T01`…`FLW-T17` | FLW-T04 direct sale, FLW-T05 product-to-sale, FLW-T08 deposit lifecycle |
| Canvas nodes | 183 | `NODE-T##-##` (+ `NODE-P*` when derived) | NODE-T05-11 (delivery revenue-once node) |
| Canvas edges | 208 | `EDGE-T##-##` (+ `EDGE-P*` when derived) | EDGE-T05-14 (cancel path) |
| Target screens | 17 | `SCR-T01`…`SCR-T17` | SCR-T03 «موقفي الآن», SCR-T12 delivery review |
| Screen contracts | 17 | `CTR-T01`…`CTR-T17` | CTR-T04 direct-sale contract |
| Wireframes | 17 | `WFR-T01`…`WFR-T17` | WFR-T03 position board |
| Personas | 2 | `PERS-*` | PERS-01 owner-operator |
| Domains | 14 | `DOM-*` | DOM-ORDERS, DOM-CASH |
| Financial boundaries | 12 | `FB-01`…`FB-12` | FB-07 deposit-liquidity rule |
| Migration notes | 6 | `MIG-001`…`MIG-006` | MIG-002 ACT-01 collision handling |
| Dependencies | 18 | `DEP-001`…`DEP-018` | DEP-007 FTR-005 → FTR-017 |
| Build phases | 15 | `PHASE-00`…`PHASE-14` | PHASE-08 orders/deposits/delivery |
| Acceptance criteria | 42 | `AC-001`…`AC-042` | AC-011 = SCN-01 contract |
| Notes (seed) | 5 | `NOTE-001`…`NOTE-005` | NOTE-001 the Dashboard-first owner note |
| Versions (seed) | 1 | `VER-001` | baseline import snapshot record |
| Audit log (seed) | 3 | `LOG-001`…`LOG-003` | import / seed / validate |

## Imported (immutable) from the Atlas — counts and ID patterns unchanged

| Collection | Count | Pattern |
| --- | --- | --- |
| Actors | 7 | `ACT-01…07` |
| Permissions | 20 | `PRM-001…020` |
| Entities | 31 | `ENT-*` |
| Screens | 57 | `SCR-*` |
| Features | 72 | domain-prefixed (`HOM/FIN/ORD/DEP/SAL/DEB/EXP/INV/PUR/DEL/AST/LOA/CAS/SCH/CTA/CTL/EST/PAR/ACT/SHR/DAT/SEC/PWA/NAV/FRM/SET/BOT/NET/POS`) |
| Services | 48 | `SVC-*` |
| Flows | 53 | `FLW-001…053` |
| Flow steps | 192 | `FLW-*-SNN` |
| States | 57 | `ST-*` |
| Transitions | 28 | `TRN-001…028` |
| Scenarios | 14 | `SCN-01…14` |
| Gaps | 20 | `GAP-01…20` |
| Decisions | 22 | `DEC-*` |
| Traceability rows | 30 | `TRC-01…30` |
| Atlas diagrams | 26 | `DGM-01…26` (+201 `DGM-*-N*` nodes) |

**Identifier note (MIG-002):** the Atlas already contained `ACT-01` in two collections (actor «المالك» and feature
«Unified activity reading»). This workspace preserves both IDs unchanged; references are typed per collection and
the global registry keys are `collection:id`, so no silent merge or reuse occurs.

## Status mapping (Atlas → studio)

| Atlas status | Studio status | Layer |
| --- | --- | --- |
| `IMPLEMENTED` | `CURRENT_STATE` | CURRENT |
| `PARTIALLY_IMPLEMENTED` | `CURRENT_STATE` (partial flag) | CURRENT |
| `PLANNED_OR_CONCEPTUAL` | `FUTURE_EXPANSION` | FUTURE |
| `NOT_FOUND` | `CURRENT_STATE` (documented absence) | CURRENT |
| `CONFLICTING` / `UNVERIFIABLE_FROM_REPOSITORY` | `UNVERIFIABLE` | CURRENT |

Original Atlas labels are preserved verbatim in each object's `atlasStatus`.
Authored target content ships as `OWNER_PROPOSAL` + `approvalState: DRAFT` — nothing is pre-approved.

## Examples

| File | Content |
| --- | --- |
| `examples/login-feature-card.json` | FTR-001 full build card |
| `examples/dashboard-feature-card.json` | FTR-003 full build card |
| `examples/sales-entry-feature-card.json` | FTR-004 full build card |
| `examples/product-to-sale-target-flow.json` | FLW-T05 + 19 nodes + 22 edges + financial contract |
| `examples/owner-review-package-example.json` | machine-readable review package example |
| `examples/owner-review-package-example.md` | human-readable Arabic review package example |
