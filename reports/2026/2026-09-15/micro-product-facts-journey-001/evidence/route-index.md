# Evidence: Route and surface index (from code, origin/main @ f21f777)
Source: apps/prototype-web/client/src/app/MicroRouter.tsx (56 `<Route>` elements) + app/routeClassifier.ts (29 deep patterns + setup)
Format: route -> page component -> chrome (S=surface/bottom-nav visible, D=deep/hidden, R=redirect)

/setup -> Setup -> setup-kind (no chrome)
/foundation -> Foundation -> S
/ -> Home -> S
/orders -> Orders -> S
/orders/new -> NewDraft -> R (to /orders/draft/new?intent=...)
/orders/draft/:id -> DraftEditor -> D (id="new" covers creation)
/orders/draft/:id/cost -> CostEditor -> D
/orders/draft/:id/agreement -> AgreementEditor -> D
/orders/:id -> OrderDetail -> S (reader)
/orders/:id/deliver -> DeliveryReview -> D (only entry: OrderDetail ready button)
/direct-sales/new -> DirectSaleEditor -> D
/direct-sales/:id -> DirectSaleEditor -> D
/schedule -> Schedule -> S
/schedule/:id -> ScheduleEditor -> D
/finance -> Finance -> S (?view=position|period, ?layer=events|corrections, ?event=)
/finance/new/:type -> FinancialEventEditor -> D (8 general event types)
/finance/withdraw -> OwnerWithdrawalEditor -> D (only entry: owner ledger)
/finance/owner-entitlement -> OwnerEntitlement -> D
/finance/g5/declaration -> G5DeclarationEditor -> D
/finance/statement -> Statement -> S
/finance/activity -> FinanceActivity -> S
/review -> Redirect -> R (to /finance)
/cash -> CashWallets -> S
/cash/wallet/new -> CashWalletEditor -> D
/cash/wallet/:id -> WalletLedger -> S (reader)
/cash/wallet/:id/opening-later -> CashOpeningLaterEditor -> D
/cash/wallet/:id/adjust -> CashAdjustmentEditor -> D
/cash/transfer -> CashTransferEditor -> D
/cash/distribute -> CashDistribution -> D (?mode=cover&to=)
/cash/count -> CashCount -> D
/cash/entry/:id/reverse -> CashReversalEditor -> D
/collect -> Collect -> D (?source=order:|sale:, ?from=)
/suppliers -> Suppliers -> S
/suppliers/purchase/:id -> SupplierPurchaseEditor -> D (new = create)
/suppliers/purchase/:id/payment -> SupplierPurchaseEditor -> D
/inventory -> InventoryMaterials -> S
/inventory/material/new -> MaterialEditor -> D
/inventory/material/:id/confirm -> MaterialEditor -> D (confirm mode)
/inventory/movement/:type -> InventoryMovementEditor -> D (receipt|consume|waste|adjust)
/inventory/movement/:id/reverse -> InventoryReversalEditor -> D
/catalog -> Catalog -> S (Home permanent unit + Tools module row)
/tools -> Tools -> S
/tools/calculator -> CostCalculator -> D
/tools/estimate/:id -> EstimateDetail -> D
/tools/integrity -> ToolsIntegrity -> S (reader)
/assets -> Assets -> S
/assets/new -> AssetEditor -> D
/assets/:id -> AssetDetail -> S (reader)
/loans -> Loans -> S
/loans/new -> LoanEditor -> D
/loans/:id -> LoanDetail -> S (reader)
/parties -> Parties -> S (read-only aggregation)
/share/preview -> SharePreview -> D (only entry: OrderDetail share)
/settings -> Settings -> S (?focus=guided-import)
/profile -> Profile -> S
(default) -> NotFound

Bottom navigation (app/navigation.ts:13-18): مشروعي الآن / | العمل /orders | [FAB «سجّل» -> QuickActionSheet] | مالي /finance | أدواتي /tools

QuickActionSheet actions: تسجيل بيع (in-sheet), تسجيل مصروف (in-sheet), طلب من عميل -> /orders/draft/new?intent=customer_order, مسودة تصميم -> /orders/draft/new?intent=planned_design, عربون أو تحصيل -> /collect?from=...

IndexedDB stores (32, db micro-prototype-local, schema 35 / export 27): activity-profile, owner-profile, local-preferences, order-drafts, craft-orders, direct-sales, schedule-entries, schedule-recurrences, financial-events, supplier-purchases, cash-wallets, cash-continuity-entries, materials, inventory-movements, inventory-activations, inventory-shortages, catalog-items, measurement-units, direct-conversions, catalog-templates, actual-time-records, short-cash-declarations, owner-entitlement-policies, owner-entitlement-records, owner-entitlement-opening-balances, owner-movements, allocation-policies, cost-estimates, assets, loans, form-drafts, local-security (last two outside export snapshot).

Note for next phase (screenshots conversation): deep editor routes (D) hide the bottom bar; screenshots of those surfaces will show a back-only chrome. Read-only reader surfaces (S) keep the bottom bar.
