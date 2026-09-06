# 06 — Service Blueprint and Cross-Flow Dependencies

## Diagram atlas

The interactive HTML contains 26 diagrams (system map, actor map, domain
map, navigation map, 4 swimlanes, 8 state machines, 1 service blueprint, 6 critical flows,
cross-flow map, gap map, future-state map). This report documents them and the shared-entity
reuse analysis.

| ID | Title | Category | Nodes |
| --- | --- | --- | --- |
| DGM-01 | System Map — خريطة النظام | system | 8 |
| DGM-02 | Actor & Permission Map — خريطة الفاعلين والصلاحيات | actors | 8 |
| DGM-03 | Domain Map — خريطة المجال | domain | 9 |
| DGM-04 | Screen & Navigation Map — خريطة الشاشات والتنقل | navigation | 13 |
| DGM-05 | Swimlane: Order to Delivery — ممر السباحة: دورة الطلب حتى التسليم | swimlane | 10 |
| DGM-06 | Swimlane: Guided Entry & Correction — ممر السباحة: الإدخال المالي الموجّه والتصحيح | swimlane | 7 |
| DGM-07 | Swimlane: Supplier Purchase & Receipt — ممر السباحة: شراء المورد والاستلام | swimlane | 7 |
| DGM-08 | Swimlane: Backup, Restore & Lock — ممر السباحة: النسخ الاحتياطي والاستعادة والقفل | swimlane | 7 |
| DGM-09 | State: CraftOrder — حالة الطلب | state | 10 |
| DGM-10 | State: Deposit Settlement — حالة تسوية العربون عند الإلغاء | state | 8 |
| DGM-11 | State: DirectSale — حالة البيع المباشر | state | 7 |
| DGM-12 | State: Financial Event Correction — نموذج تصحيح الحدث المالي | state | 7 |
| DGM-13 | State: Inventory Movement & Shortage — حركة المخزون والنقص | state | 8 |
| DGM-14 | State: Asset — حالة الأصل | state | 7 |
| DGM-15 | State: Loan — حالة القرض | state | 6 |
| DGM-16 | State: SupplierPurchase Payments — حالة دفعات الشراء | state | 5 |
| DGM-17 | Service Blueprint: Delivery with Collection — المخطط الخدمي: التسليم مع التحصيل | blueprint | 11 |
| DGM-18 | Critical Flow: Deposit → Delivery → Remainder — التدفق الحرج: عربون → تسليم → متبقٍ | critical | 7 |
| DGM-19 | Critical Flow: Cancel with Deposit — التدفق الحرج: إلغاء طلب فيه عربون | critical | 7 |
| DGM-20 | Critical Flow: Safe Correction — التدفق الحرج: التصحيح الآمن | critical | 7 |
| DGM-21 | Critical Flow: Waste with Choice — التدفق الحرج: الهدر بالخيار | critical | 6 |
| DGM-22 | Critical Flow: Restore Rejection & Success — التدفق الحرج: استعادة النسخة — الرفض والنجاح | critical | 7 |
| DGM-23 | Critical Flow: Negative Inventory Decision — التدفق الحرج: قرار المخزون السالب | critical | 6 |
| DGM-24 | Cross-Flow Entity Reuse Map — خريطة التقاطع بين المسارات | crossflow | 7 |
| DGM-25 | Gap & Contradiction Map — خريطة الفجوات والتناقضات | gap | 9 |
| DGM-26 | Future State Map (Planned Concepts) — الخريطة المستقبلية (مفاهيم مخططة) | future | 7 |

## Diagram notes

### DGM-01 — System Map (خريطة النظام)

Offline-first local architecture: RTL React UI over application services over pure domain policies over one IndexedDB store. Zero network calls.

### DGM-02 — Actor & Permission Map (خريطة الفاعلين والصلاحيات)

Single local human actor; customers/suppliers/couriers are data subjects; deterministic guidance; network roles are contract-only.

### DGM-03 — Domain Map (خريطة المجال)

14 pure domain modules; craft-order engine at the center; 17-type financial-event ledger with 8 signed delta dimensions.

### DGM-04 — Screen & Navigation Map (خريطة الشاشات والتنقل)

4 bottom tabs + central FAB with 5 quick actions; reader=surface (keeps nav), editor=depth (hides nav, guards input); ?from referrer contract.

### DGM-05 — Swimlane: Order to Delivery (ممر السباحة: دورة الطلب حتى التسليم)

Owner×system swimlane of the order lifecycle; revenue recognized once at delivery; exceptions are honest and atomic.

### DGM-06 — Swimlane: Guided Entry & Correction (ممر السباحة: الإدخال المالي الموجّه والتصحيح)

Deterministic guidance previews from the same expansion as save; corrections are atomic reverse-and-replace pairs.

### DGM-07 — Swimlane: Supplier Purchase & Receipt (ممر السباحة: شراء المورد والاستلام)

Supplier is a data subject; purchase = cash/payable only; receipt bridge is pre-filled, bounded, never silent.

### DGM-08 — Swimlane: Backup, Restore & Lock (ممر السباحة: النسخ الاحتياطي والاستعادة والقفل)

Verified export (round-trip), 11 honest import rejection rules, atomic replace; data-exit actions PIN-gated once per session.

### DGM-09 — State: CraftOrder (حالة الطلب)

10-state machine; recognition once at delivered; reversal→needs_review; resume; cancel pre-delivery only.

### DGM-10 — State: Deposit Settlement (حالة تسوية العربون عند الإلغاء)

cancelled_pending → refund/retain (partial allowed) → explicit classification; final state only when nothing pending.

### DGM-11 — State: DirectSale (حالة البيع المباشر)

Revenue at sale date; explicit difference decision; three documented correction kinds; cancel mirror-reverses allocations.

### DGM-12 — State: Financial Event Correction (نموذج تصحيح الحدث المالي)

Reversal events negate sources; originals immutable; reversals never reversed; edit = atomic pair; restore = new copy.

### DGM-13 — State: Inventory Movement & Shortage (حركة المخزون والنقص)

Direction-guarded movements; negative impossible (shortage ledger); waste profit-impact is an explicit owner choice.

### DGM-14 — State: Asset (حالة الأصل)

Acquisition=capital; depreciation proposal→explicit; to-zero stays active; disposal/write-off freeze; post-disposal reversal rejected.

### DGM-15 — State: Loan (حالة القرض)

Loans are neither expense nor owner draw; outstanding derived; corrections atomic; concurrency guard.

### DGM-16 — State: SupplierPurchase Payments (حالة دفعات الشراء)

Status derived from effective payments; initial payment corrected via edit; later payments reversible once each.

### DGM-17 — Service Blueprint: Delivery with Collection (المخطط الخدمي: التسليم مع التحصيل)

User actions vs system actions vs persistence vs financial effect, for the critical delivery-with-collection line.

### DGM-18 — Critical Flow: Deposit → Delivery → Remainder (التدفق الحرج: عربون → تسليم → متبقٍ)

The 100/20/80 path: deposit=liquidity; one full sale at delivery applying deposit once; remainder=cash only.

### DGM-19 — Critical Flow: Cancel with Deposit (التدفق الحرج: إلغاء طلب فيه عربون)

Mandatory impact preview; refund reverses allocations; retention awaits explicit meaning; never auto-classified.

### DGM-20 — Critical Flow: Safe Correction (التدفق الحرج: التصحيح الآمن)

Three owner verbs, one engine: documented reversal (+ replacement) atomic; preview in result language; family events corrected at their surfaces.

### DGM-21 — Critical Flow: Waste with Choice (التدفق الحرج: الهدر بالخيار)

wasteProfitImpact choice stored on movement; known cost ⇒ atomic loss event; unknown cost keeps the choice only; reversal reverses both.

### DGM-22 — Critical Flow: Restore Rejection & Success (التدفق الحرج: استعادة النسخة — الرفض والنجاح)

Parse → allowlist → digest → counts → deep validation; failures reject before preview; success = PIN-gated atomic replace + integrity check.

### DGM-23 — Critical Flow: Negative Inventory Decision (التدفق الحرج: قرار المخزون السالب)

Guard rejects; explicit choice: shortage-only / consume-available+shortage (atomic) / skip; open shortage badge + MIC-8.

### DGM-24 — Cross-Flow Entity Reuse Map (خريطة التقاطع بين المسارات)

Where journeys share entities: orders↔materials↔cash; collections serve orders+sales; events carry deposits/assets/loans; parties read all.

### DGM-25 — Gap & Contradiction Map (خريطة الفجوات والتناقضات)

Docs contradictions, by-design deferrals, and improvement gaps — each with severity and evidence in the register.

### DGM-26 — Future State Map (Planned Concepts) (الخريطة المستقبلية (مفاهيم مخططة))

Contract-only future concepts (E-00): identity/roles, market, delivery, network money — nothing implemented; honest placeholders in current app.


## Service blueprint (delivery with collection — DGM-17)

| Layer | Content |
| --- | --- |
| User-visible actions | Review delivery card (money lines, knowledge gaps, suggested consumption with shortages), choose collect-at-delivery wallet, single confirm |
| System actions | Build review (read-only), guard amount bounds, idempotency key with attempt counter, atomic transaction assembly, schedule reconciliation notice |
| Persistence | `commitOrderDelivery` — one IndexedDB transaction: status transition + consumption movements + optional collection allocation (`sourceRefLineId = deliveryEvent.id`) |
| Financial effects | Revenue recognized ONCE (agreedPrice), deposit applied once inside it, collection is cash only, profit when final knowledge |

## Cross-flow entity reuse

Where journeys join or reuse the same entity (the cross-flow map DGM-24):

- **CraftOrder** is the hub: deposits (FLW-010), delivery+consumption (FLW-011), collections
  (FLW-012/015), cancellation+deposit settlement (FLW-021/023), corrections (FLW-020/039).
- **CashContinuityEntry** is written by orders (collections), sales, expenses (allocations),
  purchases (payments), loans, owner movements, and G5-free — always with source links.
- **FinancialEvent** carries the general ledger: expenses, owner money, amanah, assets, loans,
  deposit classification, waste losses — 17 types, 8 signed delta dimensions.
- **PartyLedgerRow** (derived) reads orders, sales, purchases, and payable events by name.
- **InventoryMovement** links purchases (receipt), orders/sales (consumption), waste contexts.

| Referenced catalog item | Diagram nodes |
| --- | --- |
| BOT-01 | DGM-02-N5, DGM-06-N2 |
| DEL-01 | DGM-26-N4 |
| ENT-ASSET | DGM-03-N6 |
| ENT-CASH-ENTRY | DGM-03-N4, DGM-24-N3 |
| ENT-CRAFT-ORDER | DGM-03-N1, DGM-24-N1 |
| ENT-DIRECT-SALE | DGM-03-N5, DGM-24-N2 |
| ENT-FINANCIAL-EVENT | DGM-03-N2, DGM-24-N4 |
| ENT-INVENTORY-MOVEMENT | DGM-03-N3, DGM-24-N5 |
| ENT-LOAN | DGM-03-N7 |
| ENT-PARTY-LEDGER | DGM-24-N6 |
| ENT-SUPPLIER-PURCHASE | DGM-03-N9 |
| FLW-008 | DGM-05-N3 |
| FLW-010 | DGM-05-N5, DGM-18-N2 |
| FLW-011 | DGM-05-N6, DGM-05-N8, DGM-18-N4 |
| FLW-012 | DGM-18-N5 |
| FLW-017 | DGM-06-N4, DGM-07-N7 |
| FLW-018 | DGM-06-N5 |
| FLW-023 | DGM-19-N6 |
| FLW-026 | DGM-05-N9 |
| FLW-029 | DGM-07-N2, DGM-07-N5 |
| FLW-032 | DGM-05-N4 |
| FLW-040 | DGM-08-N3 |
| FLW-041 | DGM-08-N4, DGM-08-N7, DGM-22-N7 |
| FLW-047 | DGM-08-N1 |
| GAP-01 | DGM-25-N7 |
| GAP-02 | DGM-25-N4 |
| GAP-03 | DGM-25-N5 |
| GAP-04 | DGM-25-N1 |
| GAP-05 | DGM-25-N2 |
| GAP-06 | DGM-25-N9 |
| GAP-07 | DGM-25-N8 |
| GAP-08 | DGM-25-N3 |
| GAP-11 | DGM-25-N6 |
| NET-01 | DGM-26-N2 |
| SCR-COLLECT | DGM-04-N9 |
| SCR-DELIVERY-REVIEW | DGM-04-N8 |
| SCR-FINANCE | DGM-04-N4 |
| SCR-FINANCIAL-EVENT-EDITOR | DGM-04-N11 |
| SCR-HOME | DGM-04-N1 |
| SCR-INVENTORY | DGM-04-N12 |
| SCR-ORDER-DETAIL | DGM-04-N7 |
| SCR-ORDERS | DGM-04-N2 |
| SCR-QUICK-ACTION | DGM-04-N3 |
| SCR-SETTINGS | DGM-04-N10 |
| SCR-TOOLS | DGM-04-N5 |
| ST-AST-ACTIVE | DGM-14-N2 |
| ST-AST-DISPOSED | DGM-14-N6 |
| ST-AST-FULLY-DEP | DGM-14-N4 |
| ST-AST-WRITTEN-OFF | DGM-14-N7 |
| ST-DEP-REFUND | DGM-10-N2 |
| ST-DEP-RETAIN | DGM-10-N3 |
| ST-DEP-REVIEW | DGM-10-N4 |
| ST-EVT-ACTIVE | DGM-12-N1 |
| ST-EVT-REVERSAL | DGM-12-N4 |
| ST-EVT-REVERSED | DGM-12-N3 |
| ST-LOA-OPEN | DGM-15-N2 |
| ST-LOA-SETTLED | DGM-15-N4 |
| ST-MOV-ACTIVE | DGM-13-N4 |
| ST-MOV-REVERSED | DGM-13-N8 |
| ST-ORD-CANCELLED | DGM-09-N9 |
| ST-ORD-CONFIRMED | DGM-09-N3 |
| ST-ORD-DELIVERED | DGM-09-N6 |
| ST-ORD-DRAFT | DGM-09-N1 |
| ST-ORD-POSTPONED | DGM-09-N10 |
| ST-ORD-PROGRESS | DGM-09-N4 |
| ST-ORD-PROV | DGM-09-N2 |
| ST-ORD-READY | DGM-09-N5 |
| ST-ORD-REVIEW | DGM-09-N8 |
| ST-ORD-SETTLED | DGM-09-N7 |
| ST-PUR-PAID | DGM-16-N4 |
| ST-PUR-PARTIAL | DGM-16-N3 |
| ST-PUR-UNPAID | DGM-16-N2 |
| ST-SALE-CANCELLED | DGM-11-N7 |
| ST-SALE-FULL | DGM-11-N4 |
| ST-SALE-PARTIAL-DEBT | DGM-11-N2 |
| ST-SALE-PARTIAL-REVIEW | DGM-11-N3 |
| ST-SET-CANCEL-PENDING | DGM-10-N1 |
| ST-SET-CANCEL-REFUNDED | DGM-10-N7 |
| ST-SET-CANCEL-RETAINED | DGM-10-N8 |
| ST-SHORT-OPEN | DGM-13-N5, DGM-23-N4 |
| ST-SHORT-RESOLVED | DGM-23-N6 |
| SVC-COLLECTION | DGM-24-N7 |
| SVC-CORRECTION-HISTORY | DGM-06-N7 |

## Persistence blueprint

- 32 object stores; snapshot export/import reads/writes 30 of them in single transactions;
  `form-drafts` and `local-security` are deliberately excluded from snapshots.
- Every write path is idempotent with deterministic keys; multi-store changes are atomic
  (`commitOrderDelivery`, `commitOrderDeliveryReversal`, `commitOrderCollectionReversal`,
  `commitDepositRefundSettlement`, `commitInventoryWithEvents`, `commitAssetRecord`,
  `commitLoanRecord`, `commitLoanCorrection`, `commitOwnerMovement`,
  `commitDepositClassification(Correction)`, `commitFinancialEventReplacement`, …).
- Duplicate submission protection: in-transaction duplicate checks
  (`writeOneIdempotent`, IndexedDbLocalStore.ts:699-729) + loan concurrency guard (AV-02).
