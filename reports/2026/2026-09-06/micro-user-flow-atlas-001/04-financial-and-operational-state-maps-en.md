# 04 — Financial and Operational State Maps

## State inventory

57 states across the order, settlement, deposit, sale, event-correction,
inventory, asset, loan, purchase, wallet, G5, lock, and result-status machines.

| ID | Entity | State | Arabic label | Meaning | Evidence |
| --- | --- | --- | --- | --- | --- |
| ST-ORD-DRAFT | CraftOrder | draft | مسودة | Pre-agreement record; no financial effect. | src/domain/craft-order/policies.ts:45-56 |
| ST-ORD-PROV | CraftOrder | provisional_agreement | اتفاق مبدئي | Agreement recorded (price + optional deposit); resume target after needs_review. | ALLOWED_TRANSITIONS |
| ST-ORD-CONFIRMED | CraftOrder | confirmed | مؤكد | Execution agreed; resume target after needs_review. | ALLOWED_TRANSITIONS |
| ST-ORD-PROGRESS | CraftOrder | in_progress | قيد التنفيذ | Work ongoing. | ALLOWED_TRANSITIONS |
| ST-ORD-READY | CraftOrder | ready | جاهز | Ready for delivery review. | ALLOWED_TRANSITIONS |
| ST-ORD-DELIVERED | CraftOrder | delivered | تم التسليم | Revenue recognized once; collectable remainder; reversible (documented). | policies.ts:425-441 |
| ST-ORD-SETTLED | CraftOrder | settled | تمت التسوية | Terminal: fully paid; delivery reversal still possible (requires delivered/settled). | ALLOWED_TRANSITIONS (empty) |
| ST-ORD-POSTPONED | CraftOrder | postponed | مؤجل | Paused; resumable to provisional_agreement/confirmed. | ALLOWED_TRANSITIONS |
| ST-ORD-CANCELLED | CraftOrder | cancelled | ملغى | Terminal: receivable zeroed; deposit settlement may be pending. | ALLOWED_TRANSITIONS (empty) |
| ST-ORD-REVIEW | CraftOrder | needs_review | يحتاج مراجعة | Post delivery-reversal or spec revision; result nulled; blocks general ops until documented correction; cancellable when safe (AV-07). | ALLOWED_TRANSITIONS; cancelOrder |
| ST-SET-UNPAID | CraftOrder.settlementStatus | unpaid | غير مدفوع | Nothing collected. | types.ts:86-94 |
| ST-SET-PARTIAL | CraftOrder.settlementStatus | partially_paid | مدفوع جزئيًا | Some collection (incl. deposit). |  |
| ST-SET-PAID | CraftOrder.settlementStatus | paid | مدفوع | Fully collected. |  |
| ST-SET-DEBT | CraftOrder.settlementStatus | debt | دين | Explicit registered debt after delivery. | policies.ts:596 |
| ST-SET-CANCELLED | CraftOrder.settlementStatus | cancelled | ملغى | Cancelled without deposit. |  |
| ST-SET-CANCEL-PENDING | CraftOrder.settlementStatus | cancelled_pending | ملغى — عربون معلّق | Cancelled with unrefunded/unretained deposit. | policies.ts:898 |
| ST-SET-CANCEL-REFUNDED | CraftOrder.settlementStatus | cancelled_refunded | ملغى — رُدّ العربون | Deposit fully refunded. |  |
| ST-SET-CANCEL-RETAINED | CraftOrder.settlementStatus | cancelled_retained | ملغى — احتُفظ بالعربون | Deposit retained (classified or pending meaning). |  |
| ST-DEP-NULL | CraftOrder.depositSettlement | null | (لا قرار) | No cancellation deposit decision required. |  |
| ST-DEP-REFUND | CraftOrder.depositSettlement | refund_deposit | رد العربون | Decision: refund (full or partial explicit amount). | types.ts:17 |
| ST-DEP-RETAIN | CraftOrder.depositSettlement | retain_deposit | الاحتفاظ بالعربون | Decision: retain (full or partial; meaning classification follows). |  |
| ST-DEP-REVIEW | CraftOrder.depositSettlement | needs_review | يحتاج مراجعة | Pending decision (safe default after cancellation with deposit). | policies.ts:898-900 |
| ST-SALE-ACTIVE | DirectSale | active | سجل نشط | Counts in revenue/cash/receivables. | direct-sale types |
| ST-SALE-CANCELLED | DirectSale | cancelled | ملغى | Excluded; allocations mirror-reversed. | cancelDirectSale |
| ST-SALE-FULL | DirectSale.collectionStatus | collected_in_full | قُبض كاملًا | No receivable. | types.ts:33 |
| ST-SALE-PARTIAL-DEBT | DirectSale.collectionStatus | partial_debt | جزء دين | Explicit credit remainder. |  |
| ST-SALE-PARTIAL-REVIEW | DirectSale.collectionStatus | partial_needs_review | جزء يحتاج مراجعة | Owner has not decided the difference's meaning. |  |
| ST-EVT-ACTIVE | FinancialEvent | active | سارٍ | Counts in totals (not reversed, not a reversal). | reversedEventIds filter, policies.ts:431-437 |
| ST-EVT-REVERSED | FinancialEvent | reversed | معكوس | A reversal event references it; original record untouched. | createFinancialReversal policies.ts:393-428 |
| ST-EVT-REVERSAL | FinancialEvent | reversal (correctionType=reverse) | سجل تراجع | Negates a source event; itself never reversible. | policies.ts:399-400 |
| ST-INV-UNTRACKED | Material | untracked | غير متابَع | Cost reference only; movements refused. | types.ts: tracking |
| ST-INV-TRACKED | Material | tracked | متابَع | Movements mutate quantity/value. |  |
| ST-INV-OPEN-UNCONFIRMED | Material.opening | unconfirmed | غير مؤكد | Quantity shows «غير محدد», never zero. | contract 28 S2 |
| ST-MOV-ACTIVE | InventoryMovement | active | سارية | Counts in position. |  |
| ST-MOV-REVERSED | InventoryMovement | reversed | معكوسة | Mirror movement exists; original kept. | inventoryMaterialService.reverse |
| ST-SHORT-OPEN | InventoryShortage | open | نقص مفتوح | Badge + MIC-8 WARN. |  |
| ST-SHORT-RESOLVED | InventoryShortage | resolved | نقص محسوم | Explicitly resolved. |  |
| ST-AST-ACTIVE | AssetRecord | active | نشط | Corrections allowed; depreciation proposals available. | types.ts:13 |
| ST-AST-DISPOSED | AssetRecord | disposed | متخلَّص منه | Frozen book value; corrections locked (AV-08). |  |
| ST-AST-WRITTEN-OFF | AssetRecord | written_off | مشطوب | Non-cash loss taken; locked. |  |
| ST-AST-FULLY-DEP | AssetDepreciationProposal | fully_depreciated | مستهلك جدوليًا بالكامل | Book value zero, asset remains active and in use. | policies.ts:247 |
| ST-LOA-OPEN | LoanRecord | open | قرض قائم | Outstanding derived from active repayments. | loan policies |
| ST-LOA-SETTLED | LoanRecord | settled | مسدَّد | Fully repaid; history preserved. |  |
| ST-PUR-UNPAID | SupplierPurchase | unpaid | غير مدفوع | Full payable. | supplier-purchase types |
| ST-PUR-PARTIAL | SupplierPurchase | partially_paid | مدفوع جزئيًا | Some effective payments. |  |
| ST-PUR-PAID | SupplierPurchase | paid | مدفوع | Effective paid ≥ total. |  |
| ST-WAL-KNOWN | CashWallet | opening known | رصيد بداية معروف | Declared opening. | cash-continuity types |
| ST-WAL-UNKNOWN | CashWallet | opening unknown | رصيد غير محدد | Stamp; completable later; never zero. |  |
| ST-G5-DECLARED | ShortCashDeclaration | declaration | متوقع مسجَّل | Feeds projection. | g5 types |
| ST-G5-REVERSED | ShortCashDeclaration | reversed (kind=reversal) | متوقع معكوس | Documented mirror of original. |  |
| ST-LOCK-OFF | LocalSecurityRecord | no lock | بلا قفل | No record; no gates. | localLockService |
| ST-LOCK-LOCKED | LocalSecurityRecord | locked | مقفل | Idle window exceeded; cover shown. |  |
| ST-LOCK-UNLOCKED | LocalSecurityRecord | unlocked | مفتوح | Activity heartbeat keeps it open. |  |
| ST-RES-FINAL | CraftOrder.resultStatus | final | نهائي | Profit indicator allowed (knowledge known). | types.ts |
| ST-RES-ESTIMATED | CraftOrder.resultStatus | estimated | تقديري | Honest estimate flag. |  |
| ST-RES-INCOMPLETE | CraftOrder.resultStatus | incomplete | غير مكتمل | Mandatory gaps block final result. |  |
| ST-RES-REVIEW | CraftOrder.resultStatus | review_required | يتطلب مراجعة | needs_review/cancelled state. |  |

## State transitions

28 transitions with actor, trigger, guard, and user-visible feedback.

| ID | Entity | From | To | Trigger | Actor | Guard | User-visible feedback | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRN-001 | CraftOrder | draft | provisional_agreement | AgreementEditor save (agreement with price after cost snapshot) | ACT-01 | saved cost snapshot required (missing_cost) | Order created; deposit optional at this step | ALLOWED_TRANSITIONS |
| TRN-002 | CraftOrder | provisional_agreement | confirmed | startExecution | ACT-01 | idempotency key | status_changed event | ALLOWED_TRANSITIONS |
| TRN-003 | CraftOrder | confirmed | in_progress | execution start | ACT-01 | idempotency | status_changed event | ALLOWED_TRANSITIONS |
| TRN-004 | CraftOrder | in_progress | ready | markReady | ACT-01 | idempotency | delivery review becomes available | ALLOWED_TRANSITIONS |
| TRN-005 | CraftOrder | ready | delivered | commitDelivery (single confirm) | ACT-01 | atomic: transition + consumption + optional collection | revenue recognized once; auto-settle if zero receivable | ALLOWED_TRANSITIONS |
| TRN-006 | CraftOrder | delivered | settled | auto at zero receivable / collectRemaining | ACT-06 | receivable = 0 | two explicit events | ALLOWED_TRANSITIONS |
| TRN-007 | CraftOrder | delivered|settled | needs_review | reverseDelivery (documented reason) | ACT-01 | delivered/settled + delivery event found + no prior reversal | revenue voided; consumption mirror-reversed; cash stays | reverseDelivery policies.ts:814+ |
| TRN-008 | CraftOrder | needs_review | provisional_agreement|confirmed | resumeAfterReview | ACT-01 | documented review path | walks back to a resumable status | ALLOWED_TRANSITIONS |
| TRN-009 | CraftOrder | any pre-delivery (incl. needs_review) | cancelled | cancelOrder with reason | ACT-01 | refuses delivered/settled/cancelled; AV-07 safe-completion for needs_review | cancelled (+pending deposit decision if deposit>0) | cancelOrder policies.ts:876-924 |
| TRN-010 | CraftOrder | postponed | provisional_agreement|confirmed | resume | ACT-01 | idempotency | status_changed | ALLOWED_TRANSITIONS |
| TRN-011 | CraftOrder.depositSettlement | needs_review | refund_deposit | settleDepositRefund (explicit amount) | ACT-01 | amount ≤ pending; allocation reversal bounded | cash back; cancelled_refunded when nothing pending | policies.ts:1014 |
| TRN-012 | CraftOrder.depositSettlement | needs_review | retain_deposit | settleDepositRetain | ACT-01 | explicit | cash stays; classification pending | policies.ts:1032 |
| TRN-013 | CraftOrder | cancelled (pending) | cancelled_refunded / cancelled_retained | settlement completion (nothing pending) | ACT-01 | partial amounts keep pending state | final cancel state | Conflict E comment policies.ts |
| TRN-014 | FinancialEvent | active | reversed | reverse / editEvent / deleteEvent | ACT-01 | reason; no double reversal; family guards (AV-03); amanah limit (F-006) | reversal event with negated deltas; original untouched | createFinancialReversal policies.ts:393-428 |
| TRN-015 | DirectSale | active | cancelled | cancel (documented) | ACT-01 | not already cancelled | excluded from revenue; allocations mirror-reversed | cancelDirectSale + FT-02 |
| TRN-016 | DirectSale.collectionStatus | partial_debt|partial_needs_review | collected_in_full | later collection or price cut | ACT-01 | collected = revenue | no outstanding | resolveCollection / applyPriceCut |
| TRN-017 | InventoryMovement | active | reversed | reverse (reason) | ACT-01 | mirror movement; waste+loss pair reversed together | position restored | inventoryMaterialService.ts:1195-1220 |
| TRN-018 | InventoryShortage | open | resolved | resolveShortage | ACT-01 | explicit | badge cleared | contract 28 S6 |
| TRN-019 | AssetRecord | active | disposed | applyAssetDisposal (proceeds, reason) | ACT-01 | active asset; book value frozen | asset_disposal_cash event; declared gain/loss | asset policies.ts:261-279 |
| TRN-020 | AssetRecord | active | written_off | applyAssetWriteOff | ACT-01 | bookValue > 0 | asset_writeoff event (non-cash loss) | policies.ts:296-310 |
| TRN-021 | LoanRecord | open | settled | repayment reaching outstanding | ACT-01 | payment ≤ outstanding; no payments after settled | history preserved | loan policies |
| TRN-022 | SupplierPurchase | unpaid→partially_paid→paid | (payment ladder) | recordPayment / edit / reversePayment | ACT-01 | effective paid = payments − reversals (S2-01) | status derived | supplier-purchase policies |
| TRN-023 | CashWallet | opening unknown | opening known | recordOpeningBalanceLater | ACT-01 | additive documented event (PA-007) | stamp lifted atomically | cashContinuityService |
| TRN-024 | ShortCashDeclaration | declaration | reversed | reverseDeclaration | ACT-01 | one reversal per declaration; mirrors original | projection updated | g5 policies |
| TRN-025 | AppLock | unlocked | locked | idle window exceeded / visibility lost | ACT-06 | lock record exists; /setup & /settings exempt | cover overlay (inert veil) | AppLockGate.tsx:33-100 |
| TRN-026 | AppLock | locked | unlocked | correct PIN | ACT-01 | PBKDF2 verify; backoff windows after failures | app resumes with preserved state | localLockService.unlock |
| TRN-027 | Material | tracked | untracked | untrackMaterial | ACT-01 | dialog announces 4 consequences (S7) | movements refused from now | contract 28 S1/S7 |
| TRN-028 | ImportPreview | prepared | confirmed | confirmImport (PIN-gated) | ACT-01 | all validations passed; storage ok | atomic replace + integrity check | localTransferService.confirmImport |

## Reading notes

- The order machine's `ALLOWED_TRANSITIONS` (src/domain/craft-order/policies.ts:31-42) routes the
  forward path مسودة→اتفاق مبدئي→مؤكد→قيد التنفيذ→جاهز→تم التسليم→تمت التسوية, with `postponed`
  and `needs_review` as side states and `settled`/`cancelled` terminal. Cancellation is a separate
  policy function (`cancelOrder`, policies.ts:876) that refuses delivered/settled orders and is
  allowed from any pre-delivery state including `needs_review` (AV-07).
- Deposit settlement is its own machine (needs_review → refund/retain → classification → final
  cancelled_* states) — the safe default after any cancellation with a deposit is *pending*,
  never an automatic classification (Conflict E).
- Financial events have no `status` field: correction state is structural (a linked reversal
  event); readers filter `correctionType !== "reverse" && !reversed.has(id)`.
- Inventory can never be negative: the shortage ledger replaces negative balances (D-027).
- Full state diagrams: see the interactive atlas diagrams DGM-09..DGM-16.
