# 05 — Screen, Navigation, and Feature Catalog

## Screen catalog (57 surfaces)

| ID | Route | Page file | Title (AR) | Kind | Related flows |
| --- | --- | --- | --- | --- | --- |
| SCR-HOME | `/` | pages/Home.tsx | مشروعي الآن | surface | FLW-003, FLW-002 |
| SCR-ORDERS | `/orders` | pages/Orders.tsx | العمل | surface | FLW-008, FLW-006 |
| SCR-ORDER-DETAIL | `/orders/:id` | pages/OrderDetail.tsx | تفاصيل الطلب | surface | FLW-010, FLW-011, FLW-014, FLW-021, FLW-022, FLW-023, FLW-020, FLW-039 |
| SCR-DELIVERY-REVIEW | `/orders/:id/deliver` | pages/DeliveryReview.tsx | مراجعة التسليم | deep | FLW-011, FLW-026, FLW-038 |
| SCR-NEWDRAFT | `/orders/new` | pages/NewDraft.tsx | (تحويل) | deep | FLW-008 |
| SCR-DRAFT-EDITOR | `/orders/draft/:id` | pages/DraftEditor.tsx | طلب من عميل / تصميم مخطط | deep | FLW-008, FLW-009, FLW-045 |
| SCR-COST-EDITOR | `/orders/draft/:id/cost` | pages/CostEditor.tsx | التكلفة | deep | FLW-032, FLW-008 |
| SCR-AGREEMENT-EDITOR | `/orders/draft/:id/agreement` | pages/AgreementEditor.tsx | سجّل ما اتفقت عليه | deep | FLW-009, FLW-010 |
| SCR-DIRECT-SALE-EDITOR | `/direct-sales/new, /direct-sales/:id` | pages/DirectSaleEditor.tsx | تسجيل بيع مباشر / تصحيح بيع مباشر | deep | FLW-005, FLW-006, FLW-007, FLW-013 |
| SCR-SUPPLIERS | `/suppliers` | pages/Suppliers.tsx | الموردون والمشتريات | surface | FLW-029, FLW-031 |
| SCR-SUPPLIER-PURCHASE-EDITOR | `/suppliers/purchase/new, /:id, /:id/payment` | pages/SupplierPurchaseEditor.tsx | سجل شراء / تصحيح شراء | deep | FLW-029, FLW-031 |
| SCR-CASH-WALLETS | `/cash` | pages/CashWallets.tsx | محافظ الكاش | surface | FLW-050, FLW-024 |
| SCR-CASH-WALLET-EDITOR | `/cash/wallet/new` | pages/CashWalletEditor.tsx | محفظة ورصيد بداية | deep | FLW-001, FLW-002 |
| SCR-CASH-OPENING-LATER | `/cash/wallet/:id/opening-later` | pages/CashOpeningLaterEditor.tsx | سجّل رصيد «…» الموثق لاحقًا | deep | FLW-050 |
| SCR-CASH-TRANSFER | `/cash/transfer` | pages/CashTransferEditor.tsx | تحويل بين المحافظ | deep | FLW-050 |
| SCR-CASH-ADJUSTMENT | `/cash/wallet/:id/adjust` | pages/CashAdjustmentEditor.tsx | اضبط كاش {name} | deep | FLW-050 |
| SCR-CASH-REVERSAL | `/cash/entry/:id/reverse` | pages/CashReversalEditor.tsx | تراجع عن هذا الأثر | deep | FLW-020, FLW-050 |
| SCR-CASH-DISTRIBUTION | `/cash/distribute` | pages/CashDistribution.tsx | وزّع الكاش غير الموزع | deep | FLW-015, FLW-050 |
| SCR-CASH-COUNT | `/cash/count` | pages/CashCount.tsx | عدّ اللي في الدرج فعلًا | deep | FLW-050 |
| SCR-WALLET-LEDGER | `/cash/wallet/:id` | pages/WalletLedger.tsx | (اسم المحفظة) | surface | FLW-020, FLW-015 |
| SCR-COLLECT | `/collect` | pages/Collect.tsx | ورقة التحصيل / حصّل من مين عليه إلَي / قبضت من {name} | deep | FLW-012, FLW-015, FLW-010 |
| SCR-INVENTORY | `/inventory` | pages/InventoryMaterials.tsx | المواد والمخزون | surface | FLW-024, FLW-025, FLW-026 |
| SCR-MATERIAL-EDITOR | `/inventory/material/new, /:id/confirm` | pages/MaterialEditor.tsx | أي مادة تسجّل؟ / أكّد رصيد {name} | deep | FLW-024, FLW-025 |
| SCR-INVENTORY-MOVEMENT-EDITOR | `/inventory/movement/:type` | pages/InventoryMovementEditor.tsx | (حركة مادة) | deep | FLW-024, FLW-026, FLW-027, FLW-028 |
| SCR-INVENTORY-REVERSAL | `/inventory/movement/:id/reverse` | pages/InventoryReversalEditor.tsx | تراجع عن حركة المادة | deep | FLW-022, FLW-027 |
| SCR-SCHEDULE | `/schedule` | pages/Schedule.tsx | المواعيد | surface | FLW-011 |
| SCR-SCHEDULE-EDITOR | `/schedule/:id` | pages/ScheduleEditor.tsx | وقت ومدة الموعد | deep | — |
| SCR-FINANCE | `/finance` | pages/Finance.tsx | مالي | surface | FLW-003, FLW-017, FLW-018, FLW-023, FLW-051, FLW-052 |
| SCR-FINANCIAL-EVENT-EDITOR | `/finance/new/:type (8 types)` | pages/FinancialEventEditor.tsx | (إدخال مالي موجّه) | deep | FLW-017, FLW-018 |
| SCR-OWNER-WITHDRAWAL | `/finance/withdraw` | pages/OwnerWithdrawalEditor.tsx | سحب من المشروع لنفسك؟ | deep | FLW-051 |
| SCR-OWNER-ENTITLEMENT | `/finance/owner-entitlement` | pages/OwnerEntitlement.tsx | مال المالك | surface | FLW-051 |
| SCR-G5-DECLARATION | `/finance/g5/declaration` | pages/G5DeclarationEditor.tsx | (تسجيل متوقع) | deep | FLW-052 |
| SCR-PARTIES | `/parties` | pages/Parties.tsx | مين عليه إلَي، وعليّ لمين؟ | surface | FLW-015, FLW-016 |
| SCR-STATEMENT | `/finance/statement` | pages/Statement.tsx | كشف الفترة | surface | FLW-053 |
| SCR-FINANCE-ACTIVITY | `/finance/activity` | pages/FinanceActivity.tsx | آخر ما حدث | surface | FLW-003 |
| SCR-ASSETS | `/assets` | pages/Assets.tsx | الأصول | surface | FLW-033, FLW-034, FLW-035 |
| SCR-ASSET-EDITOR | `/assets/new` | pages/AssetEditor.tsx | شراء للاستخدام الطويل | deep | FLW-033 |
| SCR-ASSET-DETAIL | `/assets/:id` | pages/AssetDetail.tsx | (اسم الأصل) | surface | FLW-033, FLW-034, FLW-035 |
| SCR-LOANS | `/loans` | pages/Loans.tsx | القروض | surface | FLW-036 |
| SCR-LOAN-EDITOR | `/loans/new` | pages/LoanEditor.tsx | أعطيت مالًا يُعاد | deep | FLW-036 |
| SCR-LOAN-DETAIL | `/loans/:id` | pages/LoanDetail.tsx | (اسم المستلف) | surface | FLW-036 |
| SCR-CATALOG | `/catalog` | pages/Catalog.tsx | منتجاتي وخدماتي | surface | FLW-006 |
| SCR-TOOLS | `/tools` | pages/Tools.tsx | أدواتي | surface | FLW-032, FLW-044 |
| SCR-COST-CALCULATOR | `/tools/calculator` | pages/CostCalculator.tsx | حاسبة التكلفة والسعر | deep | FLW-032 |
| SCR-ESTIMATE-DETAIL | `/tools/estimate/:id` | pages/EstimateDetail.tsx | (عنوان التقدير) | surface | FLW-032 |
| SCR-TOOLS-INTEGRITY | `/tools/integrity` | pages/ToolsIntegrity.tsx | فحص سلامة مالي | surface | FLW-044, FLW-041 |
| SCR-PROFILE | `/profile` | pages/Profile.tsx | ملفك وملف مشروعك | surface | FLW-001 |
| SCR-SETTINGS | `/settings` | pages/Settings.tsx | الإعدادات | surface | FLW-004, FLW-040, FLW-041, FLW-042, FLW-047 |
| SCR-SETUP | `/setup` | pages/Setup.tsx | (تأسيس محلي) | setup | FLW-001 |
| SCR-FOUNDATION | `/foundation` | pages/Foundation.tsx | شو عندك هلق؟ | surface | FLW-002, FLW-004 |
| SCR-SHARE-PREVIEW | `/share/preview` | pages/SharePreview.tsx | (معاينة المشاركة) | deep | FLW-053 |
| SCR-NOT-FOUND | `(unmatched)` | pages/NotFound.tsx | (غير موجود) | surface | — |
| SCR-QUICK-ACTION | `(sheet over surfaces)` | components/layout/QuickActionSheet.tsx | سجّل (الورقة السريعة) | sheet | FLW-005, FLW-017, FLW-008, FLW-015 |
| SCR-LOCK-COVER | `(overlay)` | components/security/AppLockGate.tsx | Micro مقفل | overlay | FLW-047 |
| SCR-STARTUP-GATE | `(boot gate)` | app/StartupGate.tsx | جارٍ فتح مشروعك المحلي… | overlay | FLW-001, FLW-046 |
| SCR-PWA-NOTICE | `(runtime notices)` | pwa/PwaRuntimeNotice.tsx + PwaInstallControl.tsx | أنت غير متصل الآن / حدّث الآن | overlay | FLW-043 |
| SCR-FORM-DRAFT-BANNER | `(component)` | components/forms/FormDraftRestoreBanner.tsx | (شريط استرجاع المسودة) | component | FLW-045 |

## Screen details

### SCR-HOME — مشروعي الآن (`/`)

- **File:** `pages/Home.tsx`
- **Kind:** surface
- **Purpose:** Home control center: activity name, local date, one operational priority, four financial facts (recorded cash, receivables, payables, owner capital) + unallocated, today list, away digest, optional modules.
- **Entry points:** Bottom tab 1; App start; Return fallback
- **Primary actions:** راجعها (fact source) · راجع دفتر الناس · انسخ الآن · افتح الإعدادات · افتح أقربها · افتح السجل الكامل
- **Exits:** /orders; /parties; /settings; /profile; /foundation; /finance/activity; fact/module source links
- **Related flows:** FLW-003, FLW-002
- **Services:** SVC-HOME-CONTROL
- **Evidence:** pages/Home.tsx:176 (openFromHome = withFrom(href, '/')); docs/decisions/home-control-center-h01a-decision-v1.md

### SCR-ORDERS — العمل (`/orders`)

- **File:** `pages/Orders.tsx`
- **Kind:** surface
- **Purpose:** Work destination (decision 24): priority-now, drafts, orders, direct sales, daily follow-up.
- **Entry points:** Bottom tab 2
- **Primary actions:** row taps · بدء طلب · إعادة المحاولة (on error)
- **Exits:** /orders/draft/:id; /orders/:id; /direct-sales/:id; /schedule/:id; /orders/draft/new?intent=customer_order
- **Related flows:** FLW-008, FLW-006
- **Services:** SVC-DAILY-FOLLOW-UP, SVC-DIRECT-SALE, SVC-SCHEDULE
- **Evidence:** pages/Orders.tsx:88; pages/Orders.ui.test.tsx

### SCR-ORDER-DETAIL — تفاصيل الطلب (`/orders/:id`)

- **File:** `pages/OrderDetail.tsx`
- **Kind:** surface
- **Purpose:** Full order surface: status, price, collections, deposit decisions, cancellation, delivery, materials, actual time, event log, share.
- **Entry points:** Orders row; DeliveryReview back; Finance/Activity/Statement deep links
- **Primary actions:** راجع التسليم وسجّله · سجّل العربون · سمِّ جهة هذا الطلب · ألغِ الطلب بهذا السبب · احتفظ به رصيدًا / صحِّح التصنيف · حصّل الدين من ورقة التحصيل
- **Exits:** /orders/:id/deliver; /collect?source=order:<id>; /inventory/movement/consume?order=<id>; /share/preview; /tools/estimate/:id
- **Related flows:** FLW-010, FLW-011, FLW-014, FLW-021, FLW-022, FLW-023, FLW-020, FLW-039
- **Services:** SVC-FULFILLMENT, SVC-AGREEMENT, SVC-COLLECTION-REVERSAL, SVC-RETAINED-DEPOSIT, SVC-ACTUAL-TIME, SVC-INVENTORY
- **Evidence:** pages/OrderDetail.tsx:532, 933, 1009, 1596

### SCR-DELIVERY-REVIEW — مراجعة التسليم (`/orders/:id/deliver`)

- **File:** `pages/DeliveryReview.tsx`
- **Kind:** deep
- **Purpose:** Pre-commitment delivery review with money lines, knowledge gaps, suggested consumption (with shortages), optional collect-at-delivery; one atomic confirm.
- **Entry points:** OrderDetail → راجع التسليم وسجّله
- **Primary actions:** single confirm · consume checkboxes · wallet selection · documented price correction
- **Exits:** /orders/:id (withFrom)
- **Related flows:** FLW-011, FLW-026, FLW-038
- **Services:** SVC-DELIVERY-REVIEW, SVC-CASH-CONTINUITY
- **Evidence:** pages/DeliveryReview.tsx:176; application/fulfillment/deliveryReviewService.ts:308-549

### SCR-NEWDRAFT — (تحويل) (`/orders/new`)

- **File:** `pages/NewDraft.tsx`
- **Kind:** deep
- **Purpose:** Legacy redirect shim to /orders/draft/new?intent=… (F-003).
- **Entry points:** legacy links
- **Primary actions:** —
- **Exits:** /orders/draft/new?intent=customer_order|planned_design
- **Related flows:** FLW-008
- **Services:** —
- **Evidence:** pages/NewDraft.tsx:16

### SCR-DRAFT-EDITOR — طلب من عميل / تصميم مخطط (`/orders/draft/:id`)

- **File:** `pages/DraftEditor.tsx`
- **Kind:** deep
- **Purpose:** Pre-domain draft editor (name, catalog item, customer, qty, specs); draft created on first real input; no price/cash effect.
- **Entry points:** FAB → طلب من عميل / مسودة تصميم; Orders rows; Estimate bridge
- **Primary actions:** save/continue · delete draft (unlinked only)
- **Exits:** /orders; /orders/draft/:id/cost; /orders/:id (converted)
- **Related flows:** FLW-008, FLW-009, FLW-045
- **Services:** SVC-DRAFT, SVC-CATALOG
- **Evidence:** pages/DraftEditor.tsx:280-348

### SCR-COST-EDITOR — التكلفة (`/orders/draft/:id/cost`)

- **File:** `pages/CostEditor.tsx`
- **Kind:** deep
- **Purpose:** Cost snapshot editor (materials, work minutes, extras); versioned snapshots; unknowns stay unknown.
- **Entry points:** DraftEditor continue; AgreementEditor «التكلفة…»
- **Primary actions:** لا ينطبق الآن — احتسبه صفرًا · تسجيل الاتفاق
- **Exits:** /orders; /orders/draft/:id; /orders/draft/:id/agreement
- **Related flows:** FLW-032, FLW-008
- **Services:** SVC-COST, SVC-MATERIAL-SUGGESTIONS
- **Evidence:** pages/CostEditor.tsx:329-650

### SCR-AGREEMENT-EDITOR — سجّل ما اتفقت عليه (`/orders/draft/:id/agreement`)

- **File:** `pages/AgreementEditor.tsx`
- **Kind:** deep
- **Purpose:** Record agreement: price (protected from cost), delivery date, deposit, optional party; converts draft → order.
- **Entry points:** CostEditor → تسجيل الاتفاق
- **Primary actions:** احفظ الاتفاق · التكلفة… (when price unavailable)
- **Exits:** /orders/:id; /orders/draft/:id/cost
- **Related flows:** FLW-009, FLW-010
- **Services:** SVC-AGREEMENT, SVC-CASH-CONTINUITY
- **Evidence:** pages/AgreementEditor.tsx:106-276

### SCR-DIRECT-SALE-EDITOR — تسجيل بيع مباشر / تصحيح بيع مباشر (`/direct-sales/new, /direct-sales/:id`)

- **File:** `pages/DirectSaleEditor.tsx`
- **Kind:** deep
- **Purpose:** Direct sale record and correction: item, amount, qty, cost known, credit sale, catalog prefill, revisions.
- **Entry points:** QuickActionSheet receipt; Catalog sell; Orders rows; Activity deep links
- **Primary actions:** سجّل البيع · تم · سجّل استهلاك مواد لهذا البيع · تأكيد إلغاء البيع · إبقاء البيع
- **Exits:** /direct-sales/:id; /inventory/movement/consume?sale=<id>; returnPath
- **Related flows:** FLW-005, FLW-006, FLW-007, FLW-013
- **Services:** SVC-DIRECT-SALE, SVC-CASH-CONTINUITY
- **Evidence:** pages/DirectSaleEditor.tsx:517-531

### SCR-SUPPLIERS — الموردون والمشتريات (`/suppliers`)

- **File:** `pages/Suppliers.tsx`
- **Kind:** surface
- **Purpose:** Supplier purchases surface: records, payments, payables.
- **Entry points:** Tools module; Finance link
- **Primary actions:** سجل شراء مواد · سجل دفعة إضافية (per row) · row open
- **Exits:** /suppliers/purchase/new; /suppliers/purchase/:id/payment; /suppliers/purchase/:id; /finance
- **Related flows:** FLW-029, FLW-031
- **Services:** SVC-SUPPLIER-PURCHASE
- **Evidence:** pages/Suppliers.tsx:90-174

### SCR-SUPPLIER-PURCHASE-EDITOR — سجل شراء / تصحيح شراء (`/suppliers/purchase/new, /:id, /:id/payment`)

- **File:** `pages/SupplierPurchaseEditor.tsx`
- **Kind:** deep
- **Purpose:** Purchase record + correction + payments; material link; receipt bridge.
- **Entry points:** Suppliers surface
- **Primary actions:** عدّل هذا الشراء · سجّل دفعة إضافية · استلم المواد
- **Exits:** /suppliers; /suppliers/purchase/:id/payment; /inventory/movement/receipt?purchase=<id>
- **Related flows:** FLW-029, FLW-031
- **Services:** SVC-SUPPLIER-PURCHASE, SVC-INVENTORY, SVC-FORM-DRAFT
- **Evidence:** pages/SupplierPurchaseEditor.tsx:358-588

### SCR-CASH-WALLETS — محافظ الكاش (`/cash`)

- **File:** `pages/CashWallets.tsx`
- **Kind:** surface
- **Purpose:** Wallets with balances, unallocated badge, all cash actions.
- **Entry points:** Finance → محافظ الكاش
- **Primary actions:** محفظة جديدة · عدّ الصندوق · وزّع الكاش غير الموزع · تحويل بين المحافظ · سجّل رصيدًا موثقًا لاحقًا · اضبط أثرًا · تراجع (per entry)
- **Exits:** /cash/wallet/new; /cash/count; /cash/distribute; /cash/transfer; /cash/wallet/:id; …/opening-later; …/adjust; /cash/entry/:id/reverse; /finance
- **Related flows:** FLW-050, FLW-024
- **Services:** SVC-CASH-CONTINUITY, SVC-PROJECT-FINANCE
- **Evidence:** pages/CashWallets.tsx:156-297

### SCR-CASH-WALLET-EDITOR — محفظة ورصيد بداية (`/cash/wallet/new`)

- **File:** `pages/CashWalletEditor.tsx`
- **Kind:** deep
- **Purpose:** New wallet + opening (known/unknown/zero); unknown ≠ 0.
- **Entry points:** CashWallets; Foundation; CashTransferEditor (أضف محفظة)
- **Primary actions:** save
- **Exits:** returnPath (→ /cash)
- **Related flows:** FLW-001, FLW-002
- **Services:** SVC-CASH-CONTINUITY
- **Evidence:** pages/CashWalletEditor.tsx

### SCR-CASH-OPENING-LATER — سجّل رصيد «…» الموثق لاحقًا (`/cash/wallet/:id/opening-later`)

- **File:** `pages/CashOpeningLaterEditor.tsx`
- **Kind:** deep
- **Purpose:** Complete an unknown opening later as an additive documented event (PA-007).
- **Entry points:** CashWallets row action
- **Primary actions:** save
- **Exits:** /cash; /cash/wallet/:id/adjust (if already known)
- **Related flows:** FLW-050
- **Services:** SVC-CASH-CONTINUITY
- **Evidence:** pages/CashOpeningLaterEditor.tsx:128-137

### SCR-CASH-TRANSFER — تحويل بين المحافظ (`/cash/transfer`)

- **File:** `pages/CashTransferEditor.tsx`
- **Kind:** deep
- **Purpose:** Two-sided transfer (total unchanged).
- **Entry points:** CashWallets
- **Primary actions:** save · أضف محفظة
- **Exits:** /cash; /cash/wallet/new
- **Related flows:** FLW-050
- **Services:** SVC-CASH-CONTINUITY
- **Evidence:** pages/CashTransferEditor.tsx:77

### SCR-CASH-ADJUSTMENT — اضبط كاش {name} (`/cash/wallet/:id/adjust`)

- **File:** `pages/CashAdjustmentEditor.tsx`
- **Kind:** deep
- **Purpose:** Documented adjustment (increase/decrease + reason).
- **Entry points:** CashWallets row
- **Primary actions:** save
- **Exits:** /cash
- **Related flows:** FLW-050
- **Services:** SVC-CASH-CONTINUITY
- **Evidence:** pages/CashAdjustmentEditor.tsx:81

### SCR-CASH-REVERSAL — تراجع عن هذا الأثر (`/cash/entry/:id/reverse`)

- **File:** `pages/CashReversalEditor.tsx`
- **Kind:** deep
- **Purpose:** Reverse a cash entry (single or both transfer legs) keeping original trace.
- **Entry points:** WalletLedger / CashWallets rows
- **Primary actions:** save · افتح الطلب (order-sourced)
- **Exits:** /cash; /orders/:orderId
- **Related flows:** FLW-020, FLW-050
- **Services:** SVC-CASH-CONTINUITY
- **Evidence:** pages/CashReversalEditor.tsx:110-144

### SCR-CASH-DISTRIBUTION — وزّع الكاش غير الموزع (`/cash/distribute`)

- **File:** `pages/CashDistribution.tsx`
- **Kind:** deep
- **Purpose:** Resolve unallocated cash: into wallet or cover payment.
- **Entry points:** CashWallets; Finance
- **Primary actions:** save
- **Exits:** returnPath
- **Related flows:** FLW-015, FLW-050
- **Services:** SVC-PROJECT-FINANCE, SVC-CASH-CONTINUITY
- **Evidence:** pages/CashDistribution.tsx

### SCR-CASH-COUNT — عدّ اللي في الدرج فعلًا (`/cash/count`)

- **File:** `pages/CashCount.tsx`
- **Kind:** deep
- **Purpose:** Drawer count vs record; difference settled as documented adjustment.
- **Entry points:** CashWallets; Finance
- **Primary actions:** سجّل التسوية
- **Exits:** returnPath (→ /cash)
- **Related flows:** FLW-050
- **Services:** SVC-CASH-CONTINUITY
- **Evidence:** pages/CashCount.tsx:73-219

### SCR-WALLET-LEDGER — (اسم المحفظة) (`/cash/wallet/:id`)

- **File:** `pages/WalletLedger.tsx`
- **Kind:** surface
- **Purpose:** Single-wallet ledger with running balance, allocation source links, reversible flags, ?entry= focus.
- **Entry points:** CashWallets row
- **Primary actions:** row source links (افتح…)
- **Exits:** /cash; row.sourceHref
- **Related flows:** FLW-020, FLW-015
- **Services:** SVC-WALLET-LEDGER
- **Evidence:** pages/WalletLedger.tsx:68-162

### SCR-COLLECT — ورقة التحصيل / حصّل من مين عليه إلَي / قبضت من {name} (`/collect`)

- **File:** `pages/Collect.tsx`
- **Kind:** deep
- **Purpose:** Collection sheet: person, remaining (editable), explicit wallet destination; blocks over-collection.
- **Entry points:** FAB → عربون أو تحصيل; Parties rows; OrderDetail link
- **Primary actions:** سجّل القبض · افتح السجل · تم · رجوع
- **Exits:** returnPath (fallback /); outcome.sourceHref
- **Related flows:** FLW-012, FLW-015, FLW-010
- **Services:** SVC-COLLECTION, SVC-CASH-CONTINUITY
- **Evidence:** pages/Collect.tsx:38-41, 145, 205-438

### SCR-INVENTORY — المواد والمخزون (`/inventory`)

- **File:** `pages/InventoryMaterials.tsx`
- **Kind:** surface
- **Purpose:** Materials surface: tracking activation, balances, movements, shortages, waste disposal.
- **Entry points:** Tools module; Finance link; Foundation
- **Primary actions:** فعّل المتابعة · أوقف المتابعة · أكّد الرصيد · سجّل الحل (waste) · movement buttons · إلغاء
- **Exits:** /inventory/material/new; /inventory/movement/receipt|consume|waste; /inventory/movement/:id/reverse; /finance
- **Related flows:** FLW-024, FLW-025, FLW-026
- **Services:** SVC-INVENTORY
- **Evidence:** pages/InventoryMaterials.tsx:299-709

### SCR-MATERIAL-EDITOR — أي مادة تسجّل؟ / أكّد رصيد {name} (`/inventory/material/new, /:id/confirm`)

- **File:** `pages/MaterialEditor.tsx`
- **Kind:** deep
- **Purpose:** Material journey: name, unit, tracking, opening knowledge; confirm-balance mode.
- **Entry points:** Inventory
- **Primary actions:** save
- **Exits:** /inventory
- **Related flows:** FLW-024, FLW-025
- **Services:** SVC-INVENTORY
- **Evidence:** pages/MaterialEditor.tsx

### SCR-INVENTORY-MOVEMENT-EDITOR — (حركة مادة) (`/inventory/movement/:type`)

- **File:** `pages/InventoryMovementEditor.tsx`
- **Kind:** deep
- **Purpose:** Movement editor (receipt/consume/waste/adjust) with source links and shortage decisions; negative stock never hidden.
- **Entry points:** Inventory buttons; Purchase bridge; OrderDetail/SaleEditor consumption links
- **Primary actions:** سجّل نقصًا بدل الاستهلاك · استهلك المتاح · مادة جديدة
- **Exits:** /inventory; /inventory/material/new
- **Related flows:** FLW-024, FLW-026, FLW-027, FLW-028
- **Services:** SVC-INVENTORY
- **Evidence:** pages/InventoryMovementEditor.tsx:213-433

### SCR-INVENTORY-REVERSAL — تراجع عن حركة المادة (`/inventory/movement/:id/reverse`)

- **File:** `pages/InventoryReversalEditor.tsx`
- **Kind:** deep
- **Purpose:** Mirror reversal of a movement (waste+loss pair reversed together).
- **Entry points:** Inventory rows
- **Primary actions:** حفظ التراجع
- **Exits:** /inventory
- **Related flows:** FLW-022, FLW-027
- **Services:** SVC-INVENTORY
- **Evidence:** pages/InventoryReversalEditor.tsx:59-125

### SCR-SCHEDULE — المواعيد (`/schedule`)

- **File:** `pages/Schedule.tsx`
- **Kind:** surface
- **Purpose:** Monthly appointments: capacity layer, recurrence layer, day selection, follow-ups; capacity advisory only.
- **Entry points:** Header context (from Finance/Home links)
- **Primary actions:** حدّد سعة اليوم · إيقاف المواعيد القادمة (reasons) · بدء طلب
- **Exits:** /schedule/:id; /orders; /orders/draft/new?intent=customer_order
- **Related flows:** FLW-011
- **Services:** SVC-SCHEDULE, SVC-RECURRENCE
- **Evidence:** pages/Schedule.tsx:184-261

### SCR-SCHEDULE-EDITOR — وقت ومدة الموعد (`/schedule/:id`)

- **File:** `pages/ScheduleEditor.tsx`
- **Kind:** deep
- **Purpose:** Appointment editor (date/time/duration; new day needs reason).
- **Entry points:** Schedule day
- **Primary actions:** save
- **Exits:** /schedule
- **Related flows:** —
- **Services:** SVC-SCHEDULE
- **Evidence:** pages/ScheduleEditor.tsx:166

### SCR-FINANCE — مالي (`/finance`)

- **File:** `pages/Finance.tsx`
- **Kind:** surface
- **Purpose:** Finance hub: cash card, period result/pulse, G5 decision, corrections & events layers, deposits, assets/loans summaries, owner money, all guided financial actions.
- **Entry points:** Bottom tab 3; /review redirect (legacy)
- **Primary actions:** وزّع على محفظة · عدّ الصندوق · كشف الفترة · فحص سلامة مالي · سجل مصروفًا مدفوعًا · سجل التزامًا لمورد · سدد التزام مصروف · سجل أمانة قُبضت/سُلّمت · سجل هدرًا بلا خروج نقد · سجل سحبًا شخصيًا (implicit)
- **Exits:** /cash/*; /parties; /suppliers; /finance/statement; /tools/integrity; /assets; /loans; /finance/g5/declaration; /finance/owner-entitlement; /finance?layer=corrections; /finance/new/:type (8 types); /finance/activity
- **Related flows:** FLW-003, FLW-017, FLW-018, FLW-023, FLW-051, FLW-052
- **Services:** SVC-PROJECT-FINANCE, SVC-G5, SVC-FINANCIAL-PULSE, SVC-RETAINED-DEPOSIT
- **Evidence:** pages/Finance.tsx:320-1178

### SCR-FINANCIAL-EVENT-EDITOR — (إدخال مالي موجّه) (`/finance/new/:type (8 types)`)

- **File:** `pages/FinancialEventEditor.tsx`
- **Kind:** deep
- **Purpose:** Guided financial-event editor: question sequence, effect preview, allocation review, saved draft → explicit record.
- **Entry points:** Finance quick actions; Foundation
- **Primary actions:** save (جارٍ الحفظ…) · suppliers link
- **Exits:** /finance; /finance?event=<id> (saved focus); /suppliers
- **Related flows:** FLW-017, FLW-018
- **Services:** SVC-PROJECT-FINANCE, SVC-EXPENSE-INTENT, SVC-CASH-CONTINUITY
- **Evidence:** pages/FinancialEventEditor.tsx:36-46, 631, 748, 867

### SCR-OWNER-WITHDRAWAL — سحب من المشروع لنفسك؟ (`/finance/withdraw`)

- **File:** `pages/OwnerWithdrawalEditor.tsx`
- **Kind:** deep
- **Purpose:** Single owner-withdrawal entry (writes ledger movement or generic event by entitlement policy).
- **Entry points:** Finance; OwnerEntitlement
- **Primary actions:** save
- **Exits:** /finance (العودة إلى مالي)
- **Related flows:** FLW-051
- **Services:** SVC-OWNER-ENTITLEMENT, SVC-PROJECT-FINANCE
- **Evidence:** pages/OwnerWithdrawalEditor.tsx:132

### SCR-OWNER-ENTITLEMENT — مال المالك (`/finance/owner-entitlement`)

- **File:** `pages/OwnerEntitlement.tsx`
- **Kind:** surface
- **Purpose:** Owner money ledger: capital, withdrawals, entitlement policies, opening layer, settlements.
- **Entry points:** Finance; Foundation
- **Primary actions:** حفظ التعديل وإنهاء السابقة · حفظ الرصيد الافتتاحي · تأكيد التراجع الموثق · افتح الأصل
- **Exits:** /finance/withdraw; /finance/new/owner_investment_cash; row deepLinks; /finance
- **Related flows:** FLW-051
- **Services:** SVC-OWNER-ENTITLEMENT
- **Evidence:** pages/OwnerEntitlement.tsx:279-1567

### SCR-G5-DECLARATION — (تسجيل متوقع) (`/finance/g5/declaration`)

- **File:** `pages/G5DeclarationEditor.tsx`
- **Kind:** deep
- **Purpose:** Short-cash declaration: direction (تحصيل من عميل / التزام قريب), amount, due date, link, note.
- **Entry points:** Finance G5 card
- **Primary actions:** save · إلغاء
- **Exits:** /finance
- **Related flows:** FLW-052
- **Services:** SVC-G5
- **Evidence:** pages/G5DeclarationEditor.tsx:30-245

### SCR-PARTIES — مين عليه إلَي، وعليّ لمين؟ (`/parties`)

- **File:** `pages/Parties.tsx`
- **Kind:** surface
- **Purpose:** People's ledger: name-level aggregation + search; collect deep links.
- **Entry points:** Finance → دفتر الناس; Home
- **Primary actions:** search · collect per row
- **Exits:** /collect?source=order:<id>|sale:<id>; /finance
- **Related flows:** FLW-015, FLW-016
- **Services:** SVC-PARTY-LEDGER
- **Evidence:** pages/Parties.tsx:38-190

### SCR-STATEMENT — كشف الفترة (`/finance/statement`)

- **File:** `pages/Statement.tsx`
- **Kind:** surface
- **Purpose:** Period statement with separated blocks; every line links to its source; Markdown report; share preview.
- **Entry points:** Finance → كشف الفترة
- **Primary actions:** ولّد ونزّل التقرير · row source links · corrections link
- **Exits:** source openWithReferrer; /finance?layer=corrections; sourceHref ?? /finance
- **Related flows:** FLW-053
- **Services:** SVC-STATEMENT
- **Evidence:** pages/Statement.tsx:220-586

### SCR-FINANCE-ACTIVITY — آخر ما حدث (`/finance/activity`)

- **File:** `pages/FinanceActivity.tsx`
- **Kind:** surface
- **Purpose:** Full activity reader: every registered record with effect word + source link, family/period filters.
- **Entry points:** Finance; Home
- **Primary actions:** row open · رجوع
- **Exits:** row.sourceHref; returnPath
- **Related flows:** FLW-003
- **Services:** SVC-ACTIVITY
- **Evidence:** pages/FinanceActivity.tsx:101-199

### SCR-ASSETS — الأصول (`/assets`)

- **File:** `pages/Assets.tsx`
- **Kind:** surface
- **Purpose:** Assets list with derived book value; unknown life stays unknown.
- **Entry points:** Finance → افتح سجل الأصول
- **Primary actions:** أضف أصلًا (+)
- **Exits:** /assets/new; /assets/:id; /finance
- **Related flows:** FLW-033, FLW-034, FLW-035
- **Services:** SVC-ASSET
- **Evidence:** pages/Assets.tsx:49-81

### SCR-ASSET-EDITOR — شراء للاستخدام الطويل (`/assets/new`)

- **File:** `pages/AssetEditor.tsx`
- **Kind:** deep
- **Purpose:** Asset editor with practical classification (capital asset, cash/payable, long-life question, expense deferral).
- **Entry points:** Assets +
- **Primary actions:** دفعت نقدًا · على الذمم (أدفع لاحقًا) · نعم، عمره طويل · لا، يُستهلك فورًا · لا يُسجَّل مصروفًا هذا الشهر
- **Exits:** /assets/:id (withFrom); /assets
- **Related flows:** FLW-033
- **Services:** SVC-ASSET
- **Evidence:** pages/AssetEditor.tsx:339

### SCR-ASSET-DETAIL — (اسم الأصل) (`/assets/:id`)

- **File:** `pages/AssetDetail.tsx`
- **Kind:** surface
- **Purpose:** Asset detail: book value, proposed/recorded depreciation, corrections, disposal/write-off.
- **Entry points:** Assets rows
- **Primary actions:** سجّل الإهلاك المستحق · صحّح قيمة أو طريقة الاقتناء · عدّل العمر النافع أو بداية الاستخدام · تخلّص من الأصل أو اشطبه · أكّد التراجع · إلغاء · تراجع
- **Exits:** /assets
- **Related flows:** FLW-033, FLW-034, FLW-035
- **Services:** SVC-ASSET
- **Evidence:** pages/AssetDetail.tsx:97-124

### SCR-LOANS — القروض (`/loans`)

- **File:** `pages/Loans.tsx`
- **Kind:** surface
- **Purpose:** Loans issued; outstanding derived from payments; repay via bottom sheet.
- **Entry points:** Finance → افتح سجل القروض
- **Primary actions:** repay sheet (RepaymentSheet) · أضف قرضًا
- **Exits:** /loans/new; /loans/:id; /finance
- **Related flows:** FLW-036
- **Services:** SVC-LOAN
- **Evidence:** pages/Loans.tsx:49-94

### SCR-LOAN-EDITOR — أعطيت مالًا يُعاد (`/loans/new`)

- **File:** `pages/LoanEditor.tsx`
- **Kind:** deep
- **Purpose:** Loan editor: to whom, how much, when, from which wallet.
- **Entry points:** Loans +
- **Primary actions:** save
- **Exits:** /loans/:id (withFrom)
- **Related flows:** FLW-036
- **Services:** SVC-LOAN, SVC-CASH-CONTINUITY, SVC-FORM-DRAFT
- **Evidence:** pages/LoanEditor.tsx:111

### SCR-LOAN-DETAIL — (اسم المستلف) (`/loans/:id`)

- **File:** `pages/LoanDetail.tsx`
- **Kind:** surface
- **Purpose:** Loan detail: principal, payments, history; repay sheet; correct name/amount.
- **Entry points:** Loans rows
- **Primary actions:** صحِّح بيانات القرض (اسم أو مبلغ) · أكّد التراجع · إلغاء · تراجع
- **Exits:** /loans
- **Related flows:** FLW-036
- **Services:** SVC-LOAN
- **Evidence:** pages/LoanDetail.tsx:68-183

### SCR-CATALOG — منتجاتي وخدماتي (`/catalog`)

- **File:** `pages/Catalog.tsx`
- **Kind:** surface
- **Purpose:** Catalog & templates: product/service refs (suggestions only), template components, unit conversions, recurring-margin policy readings.
- **Entry points:** Tools module
- **Primary actions:** إلغاء التعديل · أنشئ نسخة جديدة · أكّد الإيقاف · تراجع · إيقاف (policy) · sell button
- **Exits:** /direct-sales/new?product=<id> (withFrom); /tools (canonical)
- **Related flows:** FLW-006
- **Services:** SVC-CATALOG, SVC-RECURRING-WORK
- **Evidence:** pages/Catalog.tsx:1055

### SCR-TOOLS — أدواتي (`/tools`)

- **File:** `pages/Tools.tsx`
- **Kind:** surface
- **Purpose:** Tools hub: calculator entry, saved estimates, module grid with states; market/delivery placeholder disabled.
- **Entry points:** Bottom tab 4
- **Primary actions:** ابدأ مسودة من هذا التقدير · احذفه · تراجع · إعادة المحاولة · module tiles
- **Exits:** /tools/calculator; /tools/estimate/:id; /settings; /tools/integrity; /inventory; /catalog; /schedule; /suppliers; /parties
- **Related flows:** FLW-032, FLW-044
- **Services:** SVC-COST-ESTIMATE, SVC-INVENTORY, SVC-CATALOG, SVC-SCHEDULE, SVC-SUPPLIER-PURCHASE, SVC-PARTY-LEDGER
- **Evidence:** pages/Tools.tsx:133, 213-336

### SCR-COST-CALCULATOR — حاسبة التكلفة والسعر (`/tools/calculator`)

- **File:** `pages/CostCalculator.tsx`
- **Kind:** deep
- **Purpose:** Pure thinking tool: cost/price calculation with live preview; ?estimate= edit mode.
- **Entry points:** Tools
- **Primary actions:** save · افتح التقدير · ابدأ مسودة من هذا التقدير
- **Exits:** /tools/estimate/:id (withFrom); /orders/draft/new (draft bridge)
- **Related flows:** FLW-032
- **Services:** SVC-COST-ESTIMATE, SVC-MATERIAL-SUGGESTIONS
- **Evidence:** pages/CostCalculator.tsx:576-606

### SCR-ESTIMATE-DETAIL — (عنوان التقدير) (`/tools/estimate/:id`)

- **File:** `pages/EstimateDetail.tsx`
- **Kind:** surface
- **Purpose:** Saved estimate page: inputs, assumptions, result, unknowns, history.
- **Entry points:** Tools; Calculator
- **Primary actions:** ابدأ مسودة من هذا التقدير · عدّل التقدير · delete (تراجع confirm)
- **Exits:** /orders/draft/new?intent=planned_design&estimate=<id>; /tools/calculator?estimate=<id>; /tools
- **Related flows:** FLW-032
- **Services:** SVC-COST-ESTIMATE
- **Evidence:** pages/EstimateDetail.tsx:71-220

### SCR-TOOLS-INTEGRITY — فحص سلامة مالي (`/tools/integrity`)

- **File:** `pages/ToolsIntegrity.tsx`
- **Kind:** surface
- **Purpose:** Read-only financial integrity check (16 checks across money/events/amanah/inventory/assets/loans/deposits).
- **Entry points:** Tools module; Finance; Settings (after restore)
- **Primary actions:** run check · افتح السجل المعني
- **Exits:** per-check path (withFrom); /tools
- **Related flows:** FLW-044, FLW-041
- **Services:** SVC-INTEGRITY-CHECK
- **Evidence:** pages/ToolsIntegrity.tsx:59-196

### SCR-PROFILE — ملفك وملف مشروعك (`/profile`)

- **File:** `pages/Profile.tsx`
- **Kind:** surface
- **Purpose:** Owner & project profile (local identity; no OAuth/sync).
- **Entry points:** Settings → افتح الملف
- **Primary actions:** عدّل ملفك · إلغاء التعديل · إعادة المحاولة
- **Exits:** returnPath (fallback /)
- **Related flows:** FLW-001
- **Services:** SVC-OWNER-PROFILE, SVC-PROFILE, SVC-PREFERENCE
- **Evidence:** pages/Profile.tsx:311-324

### SCR-SETTINGS — الإعدادات (`/settings`)

- **File:** `pages/Settings.tsx`
- **Kind:** surface
- **Purpose:** Settings: profile, work method, actual time, lock card, data export/import/guided import, reset gate, integrity link, theme/backup reminders.
- **Entry points:** Header gear; Foundation
- **Primary actions:** افتح الملف · اختيار ملف البداية · إلغاء · إلغاء — بياناتي تبقى · ابدأ من جديد · امسح وابدأ من جديد · افتح فحص السلامة
- **Exits:** /profile?from=%2Fsettings; /tools/integrity; /setup (reset)
- **Related flows:** FLW-004, FLW-040, FLW-041, FLW-042, FLW-047
- **Services:** SVC-ACTUAL-TIME, SVC-LOCAL-TRANSFER, SVC-GUIDED-IMPORT, SVC-PREFERENCE, SVC-LOCAL-LOCK
- **Evidence:** pages/Settings.tsx:71-90, 196-344, 415-929

### SCR-SETUP — (تأسيس محلي) (`/setup`)

- **File:** `pages/Setup.tsx`
- **Kind:** setup
- **Purpose:** First-use 3-step wizard; draft persisted in localStorage; lock-exempt emergency route.
- **Entry points:** StartupGate redirect; Settings reset
- **Primary actions:** step navigation · ابدأ الإعداد من جديد
- **Exits:** /foundation (replace)
- **Related flows:** FLW-001
- **Services:** SVC-PROFILE, SVC-CASH-CONTINUITY
- **Evidence:** pages/Setup.tsx:144-196

### SCR-FOUNDATION — شو عندك هلق؟ (`/foundation`)

- **File:** `pages/Foundation.tsx`
- **Kind:** surface
- **Purpose:** Always-open front door for declaring the current foundation (cash/owner/suppliers/materials) with per-topic entries.
- **Entry points:** Setup finish; Home
- **Primary actions:** محفظة ورصيد بداية · سجل استثمارًا نقديًا · رصيد سابق لحق المالك · سجل التزامًا لمورد · شراء مواد قائم · تخطَّ وأكمل لاحقًا · ادخل إلى مشروعي
- **Exits:** /cash/wallet/new; /finance/new/owner_investment_cash; /finance/owner-entitlement; /finance/new/operating_expense_payable; /suppliers/purchase/new; /inventory/material/new; /settings?focus=guided-import; /
- **Related flows:** FLW-002, FLW-004
- **Services:** SVC-CASH-CONTINUITY, SVC-OWNER-ENTITLEMENT, SVC-SUPPLIER-PURCHASE, SVC-INVENTORY
- **Evidence:** pages/Foundation.tsx:67-240

### SCR-SHARE-PREVIEW — (معاينة المشاركة) (`/share/preview`)

- **File:** `pages/SharePreview.tsx`
- **Kind:** deep
- **Purpose:** Manual share preview: full editable text before it leaves the device; no auto-send.
- **Entry points:** OrderDetail/Statement via history state
- **Primary actions:** شارك/أرسل النص · انسخ النص · رجوع
- **Exits:** returnPath
- **Related flows:** FLW-053
- **Services:** SVC-SHARE
- **Evidence:** pages/SharePreview.tsx:33-93

### SCR-NOT-FOUND — (غير موجود) (`(unmatched)`)

- **File:** `pages/NotFound.tsx`
- **Kind:** surface
- **Purpose:** 404 boundary with one escape.
- **Entry points:** bad URLs
- **Primary actions:** العودة إلى مشروعي الآن
- **Exits:** /
- **Related flows:** —
- **Services:** —
- **Evidence:** pages/NotFound.tsx:12-13

### SCR-QUICK-ACTION — سجّل (الورقة السريعة) (`(sheet over surfaces)`)

- **File:** `components/layout/QuickActionSheet.tsx`
- **Kind:** sheet
- **Purpose:** FAB bottom sheet: 5 quick actions (sale form, expense form, order, estimate, collection) with receipts and discard guard.
- **Entry points:** FAB on any surface route
- **Primary actions:** تسجيل بيع · تسجيل مصروف · طلب من عميل · مسودة تصميم · عربون أو تحصيل
- **Exits:** /direct-sales/:id; /finance?event=<id>; /orders/draft/new?intent=customer_order; /orders/draft/new?intent=planned_design; /collect
- **Related flows:** FLW-005, FLW-017, FLW-008, FLW-015
- **Services:** SVC-DIRECT-SALE, SVC-PROJECT-FINANCE, SVC-CASH-CONTINUITY, SVC-CATEGORY-SUGGESTIONS
- **Evidence:** components/layout/QuickActionSheet.tsx:52-78, 315, 384, 432-455

### SCR-LOCK-COVER — Micro مقفل (`(overlay)`)

- **File:** `components/security/AppLockGate.tsx`
- **Kind:** overlay
- **Purpose:** Full-screen lock cover over live UI (inert veil; forms survive); unlock input with attempt counting and backoff.
- **Entry points:** idle timeout; visibility loss
- **Primary actions:** افتح (PIN)
- **Exits:** (unlocked app)
- **Related flows:** FLW-047
- **Services:** SVC-LOCAL-LOCK
- **Evidence:** components/security/AppLockGate.tsx:140-202

### SCR-STARTUP-GATE — جارٍ فتح مشروعك المحلي… (`(boot gate)`)

- **File:** `app/StartupGate.tsx`
- **Kind:** overlay
- **Purpose:** Boot gate: first-use redirect to /setup; storage failure recovery screen; loading state.
- **Entry points:** App boot
- **Primary actions:** إعادة المحاولة
- **Exits:** /setup; (app)
- **Related flows:** FLW-001, FLW-046
- **Services:** SVC-PROFILE
- **Evidence:** app/StartupGate.tsx:10-71

### SCR-PWA-NOTICE — أنت غير متصل الآن / حدّث الآن (`(runtime notices)`)

- **File:** `pwa/PwaRuntimeNotice.tsx + PwaInstallControl.tsx`
- **Kind:** overlay
- **Purpose:** Offline honest status card + update approval card (never reloads over dirty forms) + install banner (30-day dismissal).
- **Entry points:** offline event; SW update event; beforeinstallprompt
- **Primary actions:** حدّث الآن · لاحقًا · ثبّت Micro على جهازك
- **Exits:** (card dismiss)
- **Related flows:** FLW-043
- **Services:** SVC-PWA
- **Evidence:** pwa/PwaRuntimeNotice.tsx:55-104; pwa/PwaInstallControl.tsx:40-81

### SCR-FORM-DRAFT-BANNER — (شريط استرجاع المسودة) (`(component)`)

- **File:** `components/forms/FormDraftRestoreBanner.tsx`
- **Kind:** component
- **Purpose:** Explicit restore prompt for transient form drafts.
- **Entry points:** reopen a long form with a saved draft
- **Primary actions:** restore · discard
- **Exits:** (form)
- **Related flows:** FLW-045
- **Services:** SVC-FORM-DRAFT
- **Evidence:** components/forms/FormDraftRestoreBanner.tsx


## Feature catalog (72 features)

| ID | Domain | Title | Status | Screens | Services |
| --- | --- | --- | --- | --- | --- |
| HOM-01 | Home | Home control center (H01-A) | IMPLEMENTED | SCR-HOME | SVC-HOME-CONTROL |
| FIN-01 | Finance | Financial position reading | IMPLEMENTED | SCR-HOME, SCR-FINANCE | SVC-PROJECT-FINANCE |
| FIN-02 | Finance | Guided financial entry (8 event types) | IMPLEMENTED | SCR-FINANCIAL-EVENT-EDITOR, SCR-QUICK-ACTION | SVC-PROJECT-FINANCE, SVC-EXPENSE-INTENT |
| FIN-03 | Finance | Period statement | IMPLEMENTED | SCR-STATEMENT | SVC-STATEMENT |
| FIN-04 | Finance | Activity feed (contract 30) | IMPLEMENTED | SCR-FINANCE-ACTIVITY | SVC-ACTIVITY |
| FIN-05 | Finance | G5: contribution, break-even, short cash | IMPLEMENTED | SCR-FINANCE, SCR-G5-DECLARATION | SVC-G5 |
| FIN-06 | Finance | Owner money separation & entitlements | IMPLEMENTED | SCR-OWNER-ENTITLEMENT, SCR-OWNER-WITHDRAWAL | SVC-OWNER-ENTITLEMENT |
| FIN-07 | Finance | Financial integrity check (MIC) | IMPLEMENTED | SCR-TOOLS-INTEGRITY | SVC-INTEGRITY-CHECK |
| FIN-08 | Finance | Financial pulse (order-only) | IMPLEMENTED | SCR-FINANCE | SVC-FINANCIAL-PULSE |
| ORD-01 | Orders | Order draft creation | IMPLEMENTED | SCR-DRAFT-EDITOR | SVC-DRAFT |
| ORD-02 | Orders | Cost snapshot (versioned, knowledge-honest) | IMPLEMENTED | SCR-COST-EDITOR | SVC-COST |
| ORD-03 | Orders | Agreement recording (price protection) | IMPLEMENTED | SCR-AGREEMENT-EDITOR | SVC-AGREEMENT |
| ORD-04 | Orders | Order lifecycle state machine | IMPLEMENTED | SCR-ORDER-DETAIL | SVC-FULFILLMENT |
| ORD-05 | Orders | Delivery review + atomic recognition | IMPLEMENTED | SCR-DELIVERY-REVIEW | SVC-DELIVERY-REVIEW |
| ORD-06 | Orders | Order cancellation + deposit settlement | IMPLEMENTED | SCR-ORDER-DETAIL | SVC-FULFILLMENT |
| DEP-01 | Deposits | Deposit collection (liquidity) | IMPLEMENTED | SCR-ORDER-DETAIL, SCR-AGREEMENT-EDITOR, SCR-COLLECT | SVC-FULFILLMENT |
| DEP-02 | Deposits | Deposit refund / retain (with allocation reversal) | IMPLEMENTED | SCR-ORDER-DETAIL | SVC-FULFILLMENT |
| DEP-03 | Deposits | Retained deposit classification (owner vs revenue once) | IMPLEMENTED | SCR-ORDER-DETAIL, SCR-FINANCE | SVC-RETAINED-DEPOSIT |
| SAL-01 | Sales | Direct sale (cash/credit/price cut) | IMPLEMENTED | SCR-DIRECT-SALE-EDITOR, SCR-QUICK-ACTION | SVC-DIRECT-SALE |
| SAL-02 | Sales | Sale correction (edit/price cut/cancel) | IMPLEMENTED | SCR-DIRECT-SALE-EDITOR | SVC-DIRECT-SALE |
| DEB-01 | Debt | Collection sheet | IMPLEMENTED | SCR-COLLECT, SCR-PARTIES | SVC-COLLECTION |
| DEB-02 | Debt | Debt registration (explicit) | IMPLEMENTED | SCR-ORDER-DETAIL | SVC-FULFILLMENT |
| DEB-03 | Debt | Collection reversal (compound with allocation) | IMPLEMENTED | SCR-ORDER-DETAIL, SCR-WALLET-LEDGER | SVC-COLLECTION-REVERSAL |
| EXP-01 | Expenses | Expense classification (context + label) | IMPLEMENTED | SCR-FINANCIAL-EVENT-EDITOR | SVC-EXPENSE-INTENT, SVC-CATEGORY-SUGGESTIONS |
| EXP-02 | Expenses | Post-save classification correction (WF-04) | IMPLEMENTED | SCR-FINANCE, SCR-FINANCIAL-EVENT-EDITOR | SVC-PROJECT-FINANCE |
| INV-01 | Inventory | Selective tracking (tracked/untracked) | IMPLEMENTED | SCR-INVENTORY, SCR-MATERIAL-EDITOR | SVC-INVENTORY |
| INV-02 | Inventory | Movements (receipt/consume/waste/adjust) | IMPLEMENTED | SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY |
| INV-03 | Inventory | Shortage ledger (no negative inventory) | IMPLEMENTED | SCR-INVENTORY-MOVEMENT-EDITOR, SCR-INVENTORY | SVC-INVENTORY |
| INV-04 | Inventory | Waste with owner-chosen profit impact | IMPLEMENTED | SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY |
| INV-05 | Inventory | Actual material per order (G6) | IMPLEMENTED | SCR-ORDER-DETAIL | SVC-INVENTORY |
| PUR-01 | Purchases | Supplier purchase record | IMPLEMENTED | SCR-SUPPLIERS, SCR-SUPPLIER-PURCHASE-EDITOR | SVC-SUPPLIER-PURCHASE |
| PUR-02 | Purchases | Payments + reversals + documented edits | IMPLEMENTED | SCR-SUPPLIER-PURCHASE-EDITOR | SVC-SUPPLIER-PURCHASE |
| PUR-03 | Purchases | Purchase→receipt bridge | IMPLEMENTED | SCR-SUPPLIER-PURCHASE-EDITOR, SCR-INVENTORY-MOVEMENT-EDITOR | SVC-INVENTORY |
| DEL-01 | Delivery | External delivery assignment | PLANNED_OR_CONCEPTUAL | — | — |
| DEL-02 | Delivery | Delivery failure/dispute/correction (local) | IMPLEMENTED | SCR-ORDER-DETAIL | SVC-DELIVERY-REVIEW |
| AST-01 | Assets | Asset acquisition (capital, not expense) | IMPLEMENTED | SCR-ASSET-EDITOR | SVC-ASSET |
| AST-02 | Assets | Depreciation (proposal → explicit event) | IMPLEMENTED | SCR-ASSET-DETAIL | SVC-ASSET |
| AST-03 | Assets | Disposal & write-off (separate events) | IMPLEMENTED | SCR-ASSET-DETAIL | SVC-ASSET |
| LOA-01 | Loans | Loan issuance & repayments | IMPLEMENTED | SCR-LOAN-EDITOR, SCR-LOAN-DETAIL | SVC-LOAN |
| CAS-01 | Cash | Wallets + opening knowledge | IMPLEMENTED | SCR-CASH-WALLETS, SCR-CASH-WALLET-EDITOR, SCR-CASH-OPENING-LATER | SVC-CASH-CONTINUITY |
| CAS-02 | Cash | Wallet transfers (two-legged) | IMPLEMENTED | SCR-CASH-TRANSFER, SCR-CASH-REVERSAL | SVC-CASH-CONTINUITY |
| CAS-03 | Cash | Cash count + documented adjustment | IMPLEMENTED | SCR-CASH-COUNT, SCR-CASH-ADJUSTMENT | SVC-CASH-CONTINUITY |
| CAS-04 | Cash | Unallocated cash + explicit allocation | IMPLEMENTED | SCR-CASH-DISTRIBUTION, SCR-CASH-WALLETS | SVC-PROJECT-FINANCE, SVC-CASH-CONTINUITY |
| SCH-01 | Schedule | Appointments + bounded capacity pilot | IMPLEMENTED | SCR-SCHEDULE, SCR-SCHEDULE-EDITOR | SVC-SCHEDULE, SVC-CAPACITY |
| SCH-02 | Schedule | Bounded recurrence (G6-B) | IMPLEMENTED | SCR-SCHEDULE | SVC-RECURRENCE |
| CTA-01 | Agreement context | Agreement source & follow-up (G7-A) | IMPLEMENTED | SCR-ORDER-DETAIL | SVC-AGREEMENT-CONTEXT |
| CTL-01 | Catalog | Catalog items/units/conversions/templates | IMPLEMENTED | SCR-CATALOG | SVC-CATALOG |
| CTL-02 | Catalog | Catalog → direct sale bridge | IMPLEMENTED | SCR-CATALOG, SCR-DIRECT-SALE-EDITOR | SVC-CATALOG, SVC-DIRECT-SALE |
| CTL-03 | Catalog | autoConsumeOnDelivery proposal flag | IMPLEMENTED | SCR-CATALOG, SCR-DELIVERY-REVIEW | SVC-CATALOG, SVC-DELIVERY-REVIEW |
| EST-01 | Costing | Cost calculator + estimates | IMPLEMENTED | SCR-COST-CALCULATOR, SCR-ESTIMATE-DETAIL | SVC-COST-ESTIMATE |
| PAR-01 | Parties | People ledger (name-level, no CRM) | IMPLEMENTED | SCR-PARTIES | SVC-PARTY-LEDGER |
| ACT-01 | Activity | Unified activity reading | IMPLEMENTED | SCR-FINANCE-ACTIVITY | SVC-ACTIVITY |
| SHR-01 | Share | Manual share texts (5 kinds) | IMPLEMENTED | SCR-SHARE-PREVIEW | SVC-SHARE |
| DAT-01 | Data | Verified export (envelope v27) | IMPLEMENTED | SCR-SETTINGS | SVC-LOCAL-TRANSFER |
| DAT-02 | Data | Import with 11 rejection rules | IMPLEMENTED | SCR-SETTINGS | SVC-LOCAL-TRANSFER |
| DAT-03 | Data | Guided opening import (G8.2) | IMPLEMENTED | SCR-SETTINGS | SVC-GUIDED-IMPORT |
| DAT-04 | Data | Reset (start anew) | IMPLEMENTED | SCR-SETTINGS | SVC-LOCAL-TRANSFER |
| SEC-01 | Security | Local app lock (PIN + idle) | IMPLEMENTED | SCR-LOCK-COVER, SCR-SETTINGS | SVC-LOCAL-LOCK |
| SEC-02 | Security | Data-action PIN gate | IMPLEMENTED | SCR-SETTINGS | SVC-LOCAL-LOCK |
| PWA-01 | PWA | Offline runtime + honest status | IMPLEMENTED | SCR-PWA-NOTICE | SVC-PWA |
| PWA-02 | PWA | Install control + update approval | IMPLEMENTED | SCR-PWA-NOTICE | SVC-PWA |
| NAV-01 | Navigation | Referrer & deep-link contract (26) | IMPLEMENTED | — | SVC-NAV-CONTRACT |
| NAV-02 | Navigation | Surface/deep route classification | IMPLEMENTED | — | SVC-NAV-CONTRACT |
| NAV-03 | Navigation | Unsaved-changes guard | IMPLEMENTED | SCR-QUICK-ACTION | SVC-FORM-DRAFT |
| FRM-01 | Input | English digits + DD/MM/YYYY | IMPLEMENTED | — | SVC-ENGLISH-NUMERIC |
| FRM-02 | Input | Form drafts resilience (contract 36) | IMPLEMENTED | SCR-FORM-DRAFT-BANNER | SVC-FORM-DRAFT |
| SET-01 | Setup | First-use wizard | IMPLEMENTED | SCR-SETUP | SVC-PROFILE |
| SET-02 | Setup | Foundation page | IMPLEMENTED | SCR-FOUNDATION | SVC-CASH-CONTINUITY |
| BOT-01 | Assistant | In-product guidance (deterministic) | PARTIALLY_IMPLEMENTED | SCR-FINANCIAL-EVENT-EDITOR, SCR-TOOLS-INTEGRITY | SVC-EXPENSE-INTENT, SVC-INTEGRITY-CHECK |
| BOT-02 | Assistant | Assistant-generated drafts with confirmation | PLANNED_OR_CONCEPTUAL | — | — |
| NET-01 | Network expansion | Market / Delivery / Moderation / Identity (E-00) | PLANNED_OR_CONCEPTUAL | — | — |
| POS-01 | Sales | POS / cart (سلة) | PLANNED_OR_CONCEPTUAL | — | — |

## Feature details

### HOM-01 — Home control center (H01-A)

- **Domain:** Home · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Command center with exactly four financial facts + priority + optional modules; pure view model.
- **Screens:** SCR-HOME · **Services:** SVC-HOME-CONTROL
- **Evidence:** application/home/homeControlCenterService.ts; homeControlCenterModel.test.ts

### FIN-01 — Financial position reading

- **Domain:** Finance · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** recordedCash = unallocated + wallets; receivables, payables, owner capital, amanah, assets, loans, pending retained deposits.
- **Screens:** SCR-HOME, SCR-FINANCE · **Services:** SVC-PROJECT-FINANCE
- **Evidence:** application/finance/projectFinancialService.ts:340-442

### FIN-02 — Guided financial entry (8 event types)

- **Domain:** Finance · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Question-sequence editor with impact preview and allocation review; draft persistence; category label.
- **Screens:** SCR-FINANCIAL-EVENT-EDITOR, SCR-QUICK-ACTION · **Services:** SVC-PROJECT-FINANCE, SVC-EXPENSE-INTENT
- **Evidence:** pages/FinancialEventEditor.tsx; docs/contracts/27-guided-financial-entry-contract.md

### FIN-03 — Period statement

- **Domain:** Finance · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Separated blocks, per-line source links, Markdown export, share preview; canonical reader.
- **Screens:** SCR-STATEMENT · **Services:** SVC-STATEMENT
- **Evidence:** application/finance/statementService.ts; periodResultCanonical.test.ts (TR-01)

### FIN-04 — Activity feed (contract 30)

- **Domain:** Finance · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Unified 'last happened' reader with effect classification and source links.
- **Screens:** SCR-FINANCE-ACTIVITY · **Services:** SVC-ACTIVITY
- **Evidence:** application/activity/activityService.ts; G5Activity.dom.test.tsx

### FIN-05 — G5: contribution, break-even, short cash

- **Domain:** Finance · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Final-orders contribution margin, break-even units ladder, short-cash projection with declarations.
- **Screens:** SCR-FINANCE, SCR-G5-DECLARATION · **Services:** SVC-G5
- **Evidence:** src/domain/g5/policies.ts; application/g5/g5Service.ts

### FIN-06 — Owner money separation & entitlements

- **Domain:** Finance · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Policies with successors, evidence-based calculation, movements with atomic wallet entries, unified overview.
- **Screens:** SCR-OWNER-ENTITLEMENT, SCR-OWNER-WITHDRAWAL · **Services:** SVC-OWNER-ENTITLEMENT
- **Evidence:** src/domain/owner-entitlement/policies.ts (934 lines); tests/owner-entitlement.test.ts

### FIN-07 — Financial integrity check (MIC)

- **Domain:** Finance · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** 16 read-only checks with deep links to fix at source.
- **Screens:** SCR-TOOLS-INTEGRITY · **Services:** SVC-INTEGRITY-CHECK
- **Evidence:** application/finance/integrityCheckService.ts; ToolsIntegrity.ui.test.tsx

### FIN-08 — Financial pulse (order-only)

- **Domain:** Finance · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Order aggregates: collections, registered debt, recognized revenue/cost of final orders; never claims project cash/profit.
- **Screens:** SCR-FINANCE · **Services:** SVC-FINANCIAL-PULSE
- **Evidence:** application/financial-pulse/financialPulseService.ts

### ORD-01 — Order draft creation

- **Domain:** Orders · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Pre-domain drafts (two intents), created on first input, deletable while unlinked.
- **Screens:** SCR-DRAFT-EDITOR · **Services:** SVC-DRAFT
- **Evidence:** application/drafts/draftService.ts; U06.dom.test.tsx

### ORD-02 — Cost snapshot (versioned, knowledge-honest)

- **Domain:** Orders · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Frozen snapshots at boundaries; knowledgeState + gaps; unit cost ceil vector.
- **Screens:** SCR-COST-EDITOR · **Services:** SVC-COST
- **Evidence:** src/domain/craft-order/policies.ts:211; tests/domain/shared.test.ts

### ORD-03 — Agreement recording (price protection)

- **Domain:** Orders · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Draft → order with price protected from cost when knowledge incomplete; optional deposit + schedule.
- **Screens:** SCR-AGREEMENT-EDITOR · **Services:** SVC-AGREEMENT
- **Evidence:** application/agreements/agreementService.ts; agreementPrice.test.ts

### ORD-04 — Order lifecycle state machine

- **Domain:** Orders · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** 10 statuses with guarded transitions; every sensitive transition idempotent.
- **Screens:** SCR-ORDER-DETAIL · **Services:** SVC-FULFILLMENT
- **Evidence:** src/domain/craft-order/policies.ts:31-42

### ORD-05 — Delivery review + atomic recognition

- **Domain:** Orders · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Full review → single atomic commit (transition + consumption + collection); revenue once.
- **Screens:** SCR-DELIVERY-REVIEW · **Services:** SVC-DELIVERY-REVIEW
- **Evidence:** application/fulfillment/deliveryReviewService.ts:308-549; G3Delivery.dom.test.tsx

### ORD-06 — Order cancellation + deposit settlement

- **Domain:** Orders · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Reason-chip cancel; deposit needs_review; refund/retain (partial allowed); impact preview mandated.
- **Screens:** SCR-ORDER-DETAIL · **Services:** SVC-FULFILLMENT
- **Evidence:** src/domain/craft-order/policies.ts:876-1087

### DEP-01 — Deposit collection (liquidity)

- **Domain:** Deposits · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Deposit before delivery = cash linked to order, never revenue; bounded by price.
- **Screens:** SCR-ORDER-DETAIL, SCR-AGREEMENT-EDITOR, SCR-COLLECT · **Services:** SVC-FULFILLMENT
- **Evidence:** src/domain/craft-order/policies.ts:518

### DEP-02 — Deposit refund / retain (with allocation reversal)

- **Domain:** Deposits · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Refund reverses wallet allocations up to amount; retain keeps cash pending classification.
- **Screens:** SCR-ORDER-DETAIL · **Services:** SVC-FULFILLMENT
- **Evidence:** application/fulfillment/fulfillmentService.ts:414-483

### DEP-03 — Retained deposit classification (owner vs revenue once)

- **Domain:** Deposits · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Explicit meaning decision as financial event; partial amounts; reclassification via reverse+replace.
- **Screens:** SCR-ORDER-DETAIL, SCR-FINANCE · **Services:** SVC-RETAINED-DEPOSIT
- **Evidence:** application/finance/retainedDepositService.ts; G4RetainedDeposit.dom.test.tsx

### SAL-01 — Direct sale (cash/credit/price cut)

- **Domain:** Sales · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** First-class capability (decision 23): unknown cost → profit unavailable; credit difference explicit.
- **Screens:** SCR-DIRECT-SALE-EDITOR, SCR-QUICK-ACTION · **Services:** SVC-DIRECT-SALE
- **Evidence:** src/domain/direct-sale/policies.ts; pages/DirectSaleEditor.ui.test.tsx

### SAL-02 — Sale correction (edit/price cut/cancel)

- **Domain:** Sales · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Documented revisions; cancel mirror-reverses wallet allocations (FT-02).
- **Screens:** SCR-DIRECT-SALE-EDITOR · **Services:** SVC-DIRECT-SALE
- **Evidence:** application/direct-sales/directSaleService.ts:217-273

### DEB-01 — Collection sheet

- **Domain:** Debt · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** One honest surface for all receivable sources with explicit wallet destination.
- **Screens:** SCR-COLLECT, SCR-PARTIES · **Services:** SVC-COLLECTION
- **Evidence:** pages/Collect.tsx; G2.dom.test.tsx

### DEB-02 — Debt registration (explicit)

- **Domain:** Debt · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Debt only by explicit registration after delivery; unnamed allowed with warning.
- **Screens:** SCR-ORDER-DETAIL · **Services:** SVC-FULFILLMENT
- **Evidence:** src/domain/craft-order/policies.ts:596

### DEB-03 — Collection reversal (compound with allocation)

- **Domain:** Debt · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Full-match double reversal with honest preview; revenue untouched.
- **Screens:** SCR-ORDER-DETAIL, SCR-WALLET-LEDGER · **Services:** SVC-COLLECTION-REVERSAL
- **Evidence:** application/collections/collectionReversalService.ts; G6.dom.test.tsx

### EXP-01 — Expense classification (context + label)

- **Domain:** Expenses · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** relationship/behavior/purpose/knowledge + free categoryLabel frozen with event; shared-expense share modes.
- **Screens:** SCR-FINANCIAL-EVENT-EDITOR · **Services:** SVC-EXPENSE-INTENT, SVC-CATEGORY-SUGGESTIONS
- **Evidence:** src/domain/financial-event/types.ts:28-52; group1Surfaces.test.tsx

### EXP-02 — Post-save classification correction (WF-04)

- **Domain:** Expenses · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Reverse-and-replace with new context on replacement; original keeps old classification.
- **Screens:** SCR-FINANCE, SCR-FINANCIAL-EVENT-EDITOR · **Services:** SVC-PROJECT-FINANCE
- **Evidence:** application/finance/projectFinancialService.ts:1077-1103; projectFinancialService.category.test.ts

### INV-01 — Selective tracking (tracked/untracked)

- **Domain:** Inventory · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Per-material tracking decision; untracked = cost reference only; untrack dialog with 4 consequences.
- **Screens:** SCR-INVENTORY, SCR-MATERIAL-EDITOR · **Services:** SVC-INVENTORY
- **Evidence:** docs/contracts/28-selective-inventory-tracking-contract.md; group2InventorySurfaces.test.tsx

### INV-02 — Movements (receipt/consume/waste/adjust)

- **Domain:** Inventory · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Guarded directions, source links, moving-average value, mirror reversals.
- **Screens:** SCR-INVENTORY-MOVEMENT-EDITOR · **Services:** SVC-INVENTORY
- **Evidence:** src/domain/inventory-material/policies.ts

### INV-03 — Shortage ledger (no negative inventory)

- **Domain:** Inventory · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Explicit shortage records + consume-available path; MIC-8 WARN; D-027.
- **Screens:** SCR-INVENTORY-MOVEMENT-EDITOR, SCR-INVENTORY · **Services:** SVC-INVENTORY
- **Evidence:** contract 28 S6; inventoryMaterialService.test.ts

### INV-04 — Waste with owner-chosen profit impact

- **Domain:** Inventory · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** wasteProfitImpact choice; known cost → linked loss_non_cash event atomically; reversal reverses both.
- **Screens:** SCR-INVENTORY-MOVEMENT-EDITOR · **Services:** SVC-INVENTORY
- **Evidence:** application/inventory/inventoryMaterialService.ts:1285-1320, 1195-1220

### INV-05 — Actual material per order (G6)

- **Domain:** Inventory · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Derived planned-vs-actual comparison card on order page; never mutates snapshot.
- **Screens:** SCR-ORDER-DETAIL · **Services:** SVC-INVENTORY
- **Evidence:** application/inventory/inventoryMaterialService.ts (readOrderActualMaterialComparison); contract 13

### PUR-01 — Supplier purchase record

- **Domain:** Purchases · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Cash/payable split; truth line: not COGS/expense until consumption; optional material link.
- **Screens:** SCR-SUPPLIERS, SCR-SUPPLIER-PURCHASE-EDITOR · **Services:** SVC-SUPPLIER-PURCHASE
- **Evidence:** application/suppliers/supplierPurchaseService.ts:95-97

### PUR-02 — Payments + reversals + documented edits

- **Domain:** Purchases · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Partial payments, one reversal per later payment, edits guarded by receipts.
- **Screens:** SCR-SUPPLIER-PURCHASE-EDITOR · **Services:** SVC-SUPPLIER-PURCHASE
- **Evidence:** src/domain/supplier-purchase/policies.ts; supplier-purchase-corrections.test.ts

### PUR-03 — Purchase→receipt bridge

- **Domain:** Purchases · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Pre-filled receipt editor, no silent write; bounded by purchase totals.
- **Screens:** SCR-SUPPLIER-PURCHASE-EDITOR, SCR-INVENTORY-MOVEMENT-EDITOR · **Services:** SVC-INVENTORY
- **Evidence:** pages/SupplierPurchaseEditor.tsx:479-484; contract 09 Group-2 appendix

### DEL-01 — External delivery assignment

- **Domain:** Delivery · **Status:** PLANNED_OR_CONCEPTUAL · **Role:** ACT-01
- **Description:** Assign orders to delivery companies with scoped operational data only.
- **Screens:** — · **Services:** —
- **Evidence:** docs/contracts/21-delivery-request-quote-status-privacy-contract.md (CONTRACT ONLY)

### DEL-02 — Delivery failure/dispute/correction (local)

- **Domain:** Delivery · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Documented delivery reversal + mirror consumption reversal + resume with new attempt key.
- **Screens:** SCR-ORDER-DETAIL · **Services:** SVC-DELIVERY-REVIEW
- **Evidence:** application/fulfillment/deliveryReviewService.ts:553-637; projectFinancialService.redelivery.test.ts

### AST-01 — Asset acquisition (capital, not expense)

- **Domain:** Assets · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Cash/payable acquisition with explicit long-use question and effect preview.
- **Screens:** SCR-ASSET-EDITOR · **Services:** SVC-ASSET
- **Evidence:** G4Assets.dom.test.tsx

### AST-02 — Depreciation (proposal → explicit event)

- **Domain:** Assets · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Floor-rounded schedule; recording is always explicit; to-zero keeps asset active.
- **Screens:** SCR-ASSET-DETAIL · **Services:** SVC-ASSET
- **Evidence:** src/domain/asset/policies.ts:133-256

### AST-03 — Disposal & write-off (separate events)

- **Domain:** Assets · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Frozen book value; declared gain/loss; post-disposal corrections locked (AV-08).
- **Screens:** SCR-ASSET-DETAIL · **Services:** SVC-ASSET
- **Evidence:** src/domain/asset/policies.ts:261-330

### LOA-01 — Loan issuance & repayments

- **Domain:** Loans · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Not expense/income; outstanding derived; concurrency-guarded atomic commits.
- **Screens:** SCR-LOAN-EDITOR, SCR-LOAN-DETAIL · **Services:** SVC-LOAN
- **Evidence:** G4Loans.dom.test.tsx; storage/local/loanCommitGuard.ts

### CAS-01 — Wallets + opening knowledge

- **Domain:** Cash · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Declared openings; unknown stamp completable later; never zero silently.
- **Screens:** SCR-CASH-WALLETS, SCR-CASH-WALLET-EDITOR, SCR-CASH-OPENING-LATER · **Services:** SVC-CASH-CONTINUITY
- **Evidence:** contract 10; cashContinuityService.test.ts

### CAS-02 — Wallet transfers (two-legged)

- **Domain:** Cash · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Paired transfer_out/transfer_in with shared id; reversal of one or both legs.
- **Screens:** SCR-CASH-TRANSFER, SCR-CASH-REVERSAL · **Services:** SVC-CASH-CONTINUITY
- **Evidence:** src/domain/cash-continuity/policies.ts:83-108

### CAS-03 — Cash count + documented adjustment

- **Domain:** Cash · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Drawer count vs record; difference settled with reason; reversal-of-reversal refused.
- **Screens:** SCR-CASH-COUNT, SCR-CASH-ADJUSTMENT · **Services:** SVC-CASH-CONTINUITY
- **Evidence:** pages/CashCount.tsx; cashCountMessages.test.ts

### CAS-04 — Unallocated cash + explicit allocation

- **Domain:** Cash · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Unallocated tracked separately; allocation into wallet or covering expense; never changes total.
- **Screens:** SCR-CASH-DISTRIBUTION, SCR-CASH-WALLETS · **Services:** SVC-PROJECT-FINANCE, SVC-CASH-CONTINUITY
- **Evidence:** application/finance/unallocatedDistribution.test.ts; tests/domain/cash-allocation.test.ts

### SCH-01 — Appointments + bounded capacity pilot

- **Domain:** Schedule · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Local-date entries; capacity advisory (G9.1 states); conflict warnings only.
- **Screens:** SCR-SCHEDULE, SCR-SCHEDULE-EDITOR · **Services:** SVC-SCHEDULE, SVC-CAPACITY
- **Evidence:** capacityDecisionService.test.ts; g91/g92/g93 QA docs

### SCH-02 — Bounded recurrence (G6-B)

- **Domain:** Schedule · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Weekly/monthly, 1-12 occurrences, independent entries, cancel stops future only.
- **Screens:** SCR-SCHEDULE · **Services:** SVC-RECURRENCE
- **Evidence:** application/scheduling/recurrenceService.ts; g6b-g7a-qa.md

### CTA-01 — Agreement source & follow-up (G7-A)

- **Domain:** Agreement context · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Source, summary, date with documented change reasons; derived due follow-ups; never creates schedule/reminders.
- **Screens:** SCR-ORDER-DETAIL · **Services:** SVC-AGREEMENT-CONTEXT
- **Evidence:** application/agreements/agreementContextService.ts; follow-up-local-date-acceptance-v1.md

### CTL-01 — Catalog items/units/conversions/templates

- **Domain:** Catalog · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Proposal-only defaults; exact conversions; immutable template revisions.
- **Screens:** SCR-CATALOG · **Services:** SVC-CATALOG
- **Evidence:** src/domain/catalog/policies.ts; catalogService.test.ts

### CTL-02 — Catalog → direct sale bridge

- **Domain:** Catalog · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Sell button prefills editor; recorded values owned by the sale (P-002).
- **Screens:** SCR-CATALOG, SCR-DIRECT-SALE-EDITOR · **Services:** SVC-CATALOG, SVC-DIRECT-SALE
- **Evidence:** pages/Catalog.tsx:1055; G3.dom.test.tsx

### CTL-03 — autoConsumeOnDelivery proposal flag

- **Domain:** Catalog · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Template flag proposing consumption rows inside the single delivery confirmation; never silent.
- **Screens:** SCR-CATALOG, SCR-DELIVERY-REVIEW · **Services:** SVC-CATALOG, SVC-DELIVERY-REVIEW
- **Evidence:** src/domain/catalog/types.ts:131-135; contract 29

### EST-01 — Cost calculator + estimates

- **Domain:** Costing · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Thinking tool with live knowledge-honest preview; zero-effect saves; estimate→draft bridge.
- **Screens:** SCR-COST-CALCULATOR, SCR-ESTIMATE-DETAIL · **Services:** SVC-COST-ESTIMATE
- **Evidence:** U004.dom.test.tsx

### PAR-01 — People ledger (name-level, no CRM)

- **Domain:** Parties · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Aggregation with deep links; repeat names become selectable parties; repeatedOnly filter.
- **Screens:** SCR-PARTIES · **Services:** SVC-PARTY-LEDGER
- **Evidence:** application/parties/partyLedgerService.ts; partyLedgerService.customerName.test.ts

### ACT-01 — Unified activity reading

- **Domain:** Activity · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** 15 families × 8 effect classes × 4 statuses; read-only.
- **Screens:** SCR-FINANCE-ACTIVITY · **Services:** SVC-ACTIVITY
- **Evidence:** application/activity/activityService.ts

### SHR-01 — Manual share texts (5 kinds)

- **Domain:** Share · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Order/collection/delivery/reminder/statement drafts; user edits before sharing; Jordanian phone normalization.
- **Screens:** SCR-SHARE-PREVIEW · **Services:** SVC-SHARE
- **Evidence:** application/share/shareMessageService.ts; contract 33

### DAT-01 — Verified export (envelope v27)

- **Domain:** Data · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** sha256 digest + counts; round-trip re-parse before declaring success.
- **Screens:** SCR-SETTINGS · **Services:** SVC-LOCAL-TRANSFER
- **Evidence:** localTransferService.envelope27.test.ts

### DAT-02 — Import with 11 rejection rules

- **Domain:** Data · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Version-pair allowlist, tamper checks, deep snapshot validation, family orphan rejection, atomic replace.
- **Screens:** SCR-SETTINGS · **Services:** SVC-LOCAL-TRANSFER
- **Evidence:** localTransferService.familyOrphan.test.ts (AI-01)

### DAT-03 — Guided opening import (G8.2)

- **Domain:** Data · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Opening-position file with knowledge grades; empty-store guard; per-record idempotency.
- **Screens:** SCR-SETTINGS · **Services:** SVC-GUIDED-IMPORT
- **Evidence:** guidedOpeningImportService.test.ts; g83-guided-opening-import-qa.md

### DAT-04 — Reset (start anew)

- **Domain:** Data · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Forced verified export + typed name + PIN; atomic empty replace.
- **Screens:** SCR-SETTINGS · **Services:** SVC-LOCAL-TRANSFER
- **Evidence:** pages/Settings.tsx:240-286

### SEC-01 — Local app lock (PIN + idle)

- **Domain:** Security · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** PBKDF2 120k; escalating backoff; emergency routes exempt; not encryption.
- **Screens:** SCR-LOCK-COVER, SCR-SETTINGS · **Services:** SVC-LOCAL-LOCK
- **Evidence:** application/security/localLockService.ts; Settings.lockGate.dom.test.tsx

### SEC-02 — Data-action PIN gate

- **Domain:** Security · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Export/import/reset need one PIN proof per session when lock enabled.
- **Screens:** SCR-SETTINGS · **Services:** SVC-LOCAL-LOCK
- **Evidence:** components/security/DataActionPinGate.tsx; SP-01/DP-04

### PWA-01 — Offline runtime + honest status

- **Domain:** PWA · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Offline card, no sync/no cloud statements, zero network calls, precache + SPA fallback.
- **Screens:** SCR-PWA-NOTICE · **Services:** SVC-PWA
- **Evidence:** pwa/PwaRuntimeNotice.tsx:91-104; vite.config.ts:221-254

### PWA-02 — Install control + update approval

- **Domain:** PWA · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** beforeinstallprompt capture; iOS instructions; 30-day dismissal; update waits (never over dirty forms).
- **Screens:** SCR-PWA-NOTICE · **Services:** SVC-PWA
- **Evidence:** pwa/install.ts:36-44; pwa-install-update-acceptance-v1.md

### NAV-01 — Referrer & deep-link contract (26)

- **Domain:** Navigation · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** ?from single vessel, safe-path validation, canonical fallbacks, closed deep-link vocabulary.
- **Screens:** — · **Services:** SVC-NAV-CONTRACT
- **Evidence:** app/navigationContract.ts; navigationContract.test.ts

### NAV-02 — Surface/deep route classification

- **Domain:** Navigation · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Reader keeps bottom nav; editor hides it for single-action focus; keyboard-aware chrome.
- **Screens:** — · **Services:** SVC-NAV-CONTRACT
- **Evidence:** app/routeClassifier.ts:14-76; routeClassifier.test.ts

### NAV-03 — Unsaved-changes guard

- **Domain:** Navigation · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** 3-option dialog on deep editors; 2-option quiet guard in sheets; dirty bridge to PWA.
- **Screens:** SCR-QUICK-ACTION · **Services:** SVC-FORM-DRAFT
- **Evidence:** components/forms/UnsavedChangesGuard.tsx; U005.dom.test.tsx

### FRM-01 — English digits + DD/MM/YYYY

- **Domain:** Input · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Arabic-Indic input normalized to ASCII; LTR money fields; local-date fields.
- **Screens:** — · **Services:** SVC-ENGLISH-NUMERIC
- **Evidence:** application/input/englishNumeric.ts; englishNumeric.normalize.test.ts

### FRM-02 — Form drafts resilience (contract 36)

- **Domain:** Input · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Separate store, version-gated, explicit restore, defensive coercion (AV-09).
- **Screens:** SCR-FORM-DRAFT-BANNER · **Services:** SVC-FORM-DRAFT
- **Evidence:** application/drafts/formDraftService.ts; formDraftService.test.ts

### SET-01 — First-use wizard

- **Domain:** Setup · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** 3 steps + staged draft + wallet-skip honesty (F-002).
- **Screens:** SCR-SETUP · **Services:** SVC-PROFILE
- **Evidence:** pages/Setup.ui.test.tsx

### SET-02 — Foundation page

- **Domain:** Setup · **Status:** IMPLEMENTED · **Role:** ACT-01
- **Description:** Collapsible honest sections; permanently accessible (owner decisions 4-8).
- **Screens:** SCR-FOUNDATION · **Services:** SVC-CASH-CONTINUITY
- **Evidence:** pages/Foundation.ui.test.tsx

### BOT-01 — In-product guidance (deterministic)

- **Domain:** Assistant · **Status:** PARTIALLY_IMPLEMENTED · **Role:** ACT-05
- **Description:** Guided sequences, impact previews, allocation review, integrity check, suggestions — no AI, no silent writes.
- **Screens:** SCR-FINANCIAL-EVENT-EDITOR, SCR-TOOLS-INTEGRITY · **Services:** SVC-EXPENSE-INTENT, SVC-INTEGRITY-CHECK
- **Evidence:** docs/product/guidance-interaction-policy-v1.md; components/presentation/EventEffectPreview.tsx

### BOT-02 — Assistant-generated drafts with confirmation

- **Domain:** Assistant · **Status:** PLANNED_OR_CONCEPTUAL · **Role:** ACT-05
- **Description:** Approved concept: assistant may prepare drafts requiring explicit confirmation; today's drafts are user-created; no assistant author exists.
- **Screens:** — · **Services:** —
- **Evidence:** docs/product/guidance-interaction-policy-v1.md (policy frame); application/drafts/draftService.ts (user-created drafts implemented)

### NET-01 — Market / Delivery / Moderation / Identity (E-00)

- **Domain:** Network expansion · **Status:** PLANNED_OR_CONCEPTUAL · **Role:** ACT-03
- **Description:** 7 network contracts define future actors, state machines, data classification, money representation — no code.
- **Screens:** — · **Services:** —
- **Evidence:** docs/contracts/18-network-identity-workspace-access-contract.md … 25-network-money-representation-contract.md

### POS-01 — POS / cart (سلة)

- **Domain:** Sales · **Status:** PLANNED_OR_CONCEPTUAL · **Role:** ACT-01
- **Description:** Sector-pilot-gated future capability; not implemented.
- **Screens:** — · **Services:** —
- **Evidence:** docs/decisions/pos-sector-gate-v1.md; deferred-capabilities-execution-plan-v1.md


## Service catalog (48 services)

| ID | Service file | Name | Writes | Summary |
| --- | --- | --- | --- | --- |
| SVC-PROFILE | `application/profile/profileService.ts` | ProfileService | activity-profile | Local setup validation before store write (activityName). |
| SVC-OWNER-PROFILE | `application/owner/ownerProfileService.ts` | OwnerProfileService | owner-profile | Local owner identity (name/email); ensureLocal at boot; no sync. |
| SVC-PREFERENCE | `application/preferences/preferenceService.ts` | PreferenceService | local-preferences | UI preferences only (theme, capacity, workMode, install banner, verified export stamp, backup reminder); never financial. |
| SVC-DRAFT | `application/drafts/draftService.ts` | DraftService | order-drafts | Pre-domain order drafts; create/save/delete (unlinked only); conflict guard expectedUpdatedAt. |
| SVC-FORM-DRAFT | `application/drafts/formDraftService.ts` | FormDraftService | form-drafts | Transient long-form drafts (contract 36): separate store, version-gated, explicit restore, defensive coercion (AV-09); never exported. |
| SVC-AGREEMENT | `application/agreements/agreementService.ts` | AgreementService | craft-orders, cash-continuity-entries, schedule-entries | Draft→order conversion after saved cost snapshot; provisional agreement + optional deposit + schedule atomically (commitOrderFromDraft). |
| SVC-AGREEMENT-CONTEXT | `application/agreements/agreementContextService.ts` | AgreementContextService | craft-orders (context fields) | G7-A local memory: source, follow-up summary/date/reason with change reasons; never schedule/reminder/event. |
| SVC-COST | `application/cost/costService.ts` | CostService | order-drafts (snapshots) | Maps draft cost input to domain calculateCostSnapshot; versioned snapshot save. |
| SVC-COST-ESTIMATE | `application/estimates/costEstimateService.ts` | CostEstimateService | cost-estimates | Standalone estimates: live preview + zero-effect save; delete. |
| SVC-FULFILLMENT | `application/fulfillment/fulfillmentService.ts` | FulfillmentService | craft-orders, cash-continuity-entries | Order lifecycle ops: markReady, resumeAfterReview, deliver, collections, deposit collect/refund/retain, registerRemainingDebt, cancel, assignCustomerName. |
| SVC-DELIVERY-REVIEW | `application/fulfillment/deliveryReviewService.ts` | DeliveryReviewService | craft-orders, inventory-movements, cash-continuity-entries, schedule-entries | Atomic delivery transaction: review build, commitDelivery (transition+consumption+collection), reverseDelivery with mirror reversals. |
| SVC-COLLECTION | `application/collections/collectionService.ts` | CollectionService | (via owned services), cash-continuity-entries | Collection sheet: receivable sources, routing through owned services, wallet attribution (failure keeps unallocated). |
| SVC-COLLECTION-REVERSAL | `application/collections/collectionReversalService.ts` | CollectionReversalService | craft-orders, cash-continuity-entries | Compound documented reversal of collection + matching allocation; full-match-only; honest preview. |
| SVC-DIRECT-SALE | `application/direct-sales/directSaleService.ts` | DirectSaleService | direct-sales, cash-continuity-entries | Record/update/cancel with revisions; price cut; cancel mirror-reverses wallet allocations. |
| SVC-PROJECT-FINANCE | `application/finance/projectFinancialService.ts` | ProjectFinancialService | financial-events, cash-continuity-entries | General-ledger boundary: readPosition, canonical period result, record/reverse/editEvent/deleteEvent/restoreEvent, distributeUnallocated. |
| SVC-RETAINED-DEPOSIT | `application/finance/retainedDepositService.ts` | RetainedDepositService | financial-events, craft-orders | Pending retained decisions; classify/reclassify via atomic event pairs; events are truth. |
| SVC-CORRECTION-HISTORY | `application/finance/correctionHistoryService.ts` | CorrectionHistoryService | read-only | Read-only «السجل» aggregating 19 correction kinds from 8 stores with signed effects and deep links. |
| SVC-OWNER-ENTITLEMENT | `application/finance/ownerEntitlementService.ts` | OwnerEntitlementService | owner-entitlement-*, owner-movements, cash-continuity-entries | Owner money: policies+successors, evidence-based calculation, records, opening balances, movements (+atomic wallet entries), unified overview. |
| SVC-STATEMENT | `application/finance/statementService.ts` | StatementService + StatementMarkdownService | read-only | Period statement reading with separated blocks + Arabic Markdown rendering; read-only. |
| SVC-INTEGRITY-CHECK | `application/finance/integrityCheckService.ts` | IntegrityCheckService | read-only | 16 read-only consistency checks (MIC-1..13) with statuses PASS/WARN/FAIL; no auto-fix. |
| SVC-EXPENSE-INTENT | `application/finance/expenseRecordIntent.ts` | expandExpenseRecordIntent | read-only | Single pure expansion of expense-recording intent shared by preview and record (fixed/percentage/estimate/defer). |
| SVC-CATEGORY-SUGGESTIONS | `application/finance/expenseCategorySuggestions.ts` | expenseCategorySuggestions | read-only | Read-only suggestions: owner's used tags (newest first) + Jordan seed labels; free input. |
| SVC-FINANCIAL-PULSE | `application/financial-pulse/financialPulseService.ts` | FinancialPulseService | read-only | Order-only aggregates (collections, debt, recognized revenue/cost of final orders); never claims project cash/profit. |
| SVC-G5 | `application/g5/g5Service.ts` | G5Service | short-cash-declarations | G5 decision reader: break-even + short-cash + declarations with bounded links and period-local netting. |
| SVC-HOME-CONTROL | `application/home/homeControlCenterService.ts` | HomeControlCenterService | read-only | Composes position, follow-ups, schedules, activity, direct sales, preferences → view model (pure builder). |
| SVC-DAILY-FOLLOW-UP | `application/follow-up/dailyFollowUpService.ts` | DailyFollowUpService | read-only | Converts orders+drafts into one honest next action per record. |
| SVC-CASH-CONTINUITY | `application/cash/cashContinuityService.ts` | CashContinuityService | cash-wallets, cash-continuity-entries | Wallet lifecycle: opening (known/unknown/later), adjustments, two-legged transfers, reversals; cash only. |
| SVC-WALLET-LEDGER | `application/cash/walletLedgerService.ts` | WalletLedgerService | read-only | Read-only per-wallet ledger with running balance, reversible flags, source deep links. |
| SVC-INVENTORY | `application/inventory/inventoryMaterialService.ts` | InventoryMaterialService | materials, inventory-movements, inventory-shortages, financial-events (loss_non_cash) | Inventory engine: activation, openings, receipts, consumption, shortages, waste (profit choice), adjust, reverse, period waste reading. |
| SVC-MATERIAL-SUGGESTIONS | `application/inventory/materialSuggestions.ts` | readMaterialSuggestions | read-only | D5 shared suggestion source for cost editors (last non-reversed receipt price = known). |
| SVC-SUPPLIER-PURCHASE | `application/suppliers/supplierPurchaseService.ts` | SupplierPurchaseService | supplier-purchases | Purchases, payments, documented edits, payment reversals; receipt-guarded. |
| SVC-ASSET | `application/assets/assetService.ts` | AssetService | assets, financial-events | Single writer of asset events: acquisition (atomic), depreciation proposal→event, contract revisions, disposal, write-off, corrections (active only). |
| SVC-LOAN | `application/loans/loanService.ts` | LoanService | loans, financial-events | Loans: create (+event), repayments (+events), reversals, corrections (atomic reverse+replace), concurrency guard. |
| SVC-CATALOG | `application/catalog/catalogService.ts` | CatalogService | catalog-items, measurement-units, direct-conversions, catalog-templates | Catalog CRUD: items, units, conversions, templates (+revisions); proposals only. |
| SVC-SCHEDULE | `application/scheduling/scheduleService.ts` | ScheduleService | schedule-entries | Operational timing only: capacity, month overview, timing updates, postpone, delivery reconciliation. |
| SVC-RECURRENCE | `application/scheduling/recurrenceService.ts` | ScheduleRecurrenceService | schedule-recurrences, schedule-entries | G6-B bounded recurrence (weekly/monthly, 1-12); independent entries; cancel stops future only. |
| SVC-CAPACITY | `application/scheduling/capacityDecisionService.ts` | CapacityDecisionService | read-only | Pure capacity decision + Arabic view model (unknown/needs_review/within_limit/over_limit). |
| SVC-ACTUAL-TIME | `application/time/actualTimeService.ts` | ActualTimeService | actual-time-records, local-preferences | Optional actual-time records + reversals; operating mode preference; feeds entitlement evidence. |
| SVC-RECURRING-WORK | `application/recurring-work/recurringWorkService.ts` | RecurringWorkService | allocation-policies | Allocation-policy management + readings (waste/time/material summaries; result = directMargin − amount). |
| SVC-PARTY-LEDGER | `application/parties/partyLedgerService.ts` | PartyLedgerService | read-only | Name-level aggregation (orders, sales, purchases, payable events); repeatedOnly; deep links. |
| SVC-ACTIVITY | `application/activity/activityService.ts` | ActivityService | read-only | Read-only unified feed (contract 30) with family/effect/status classification. |
| SVC-SHARE | `application/share/shareMessageService.ts` | ShareMessageService | read-only | Manual Arabic share texts (5 kinds) + Jordanian phone normalization. |
| SVC-LOCAL-LOCK | `application/security/localLockService.ts` | LocalLockService | local-security | Device lock: enable/unlock/disable, PBKDF2 verify, idle tracking, escalating backoff. |
| SVC-LOCAL-TRANSFER | `application/transfers/localTransferService.ts` | LocalTransferService | snapshot stores (30 of 32) | Export/import/reset: envelope v27 with digest+counts; 11 rejection rules; migrations with no invented history; atomic replace. |
| SVC-GUIDED-IMPORT | `application/transfers/guidedOpeningImportService.ts` | GuidedOpeningImportService | (snapshot stores) | Opening-position import: validation, empty-store guard, per-record idempotency, atomic replace. |
| SVC-ENGLISH-NUMERIC | `application/input/englishNumeric.ts` | englishNumeric | read-only | Input boundary: Arabic-Indic/Persian digit normalization, money/quantity parsing, LTR formatting. |
| SVC-PWA | `pwa/register.ts + install.ts` | PWA runtime | read-only | SW registration (prompt), update gating (dirty-forms refusal), install control, offline notice. |
| SVC-NAV-CONTRACT | `app/navigationContract.ts + routeClassifier.ts + useReturnNavigation.ts` | Navigation contract | read-only | ?from vessel, safe paths, canonical fallbacks, deep-link vocabulary, route classification. |

## Navigation contract summary

- 4 bottom tabs («مشروعي الآن» / «العمل» / «مالي» / «أدواتي») + central FAB «سجّل»
  (QuickActionSheet with 5 daily-repeat actions — decision 23-b).
- Reader surfaces keep the bottom nav; deep editors hide it for single-action focus and are
  protected by the unsaved-input guard (`app/routeClassifier.ts` — "القارئ سطح، والمحرر عمق").
- Every multi-context route carries `?from` (validated safe internal path; loop-protected);
  canonical fallbacks are registered per deep path (`app/navigationContract.ts:141-198`).
- Deep-link parameters are a closed, defensively parsed vocabulary (unknown values → `null`).
