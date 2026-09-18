# مصفوفة التكامل المالي — Micro (commit 87ebcf2)

> مخرج التدقيق «Layered Financial Management Completeness & Integration Audit» — 2026-09-19. المصدر: تتبع كود كامل (الوكيل 2-b) + تسوية حية (السيناريوهات 1–4). كل خلية ملخصة من أدلة `ملف:سطر` في ملف الوكيل؛ «—» = لا أثر بحكم التصميم.

## 1. القراء الكنونيون (مصادر الحقيقة)

كل الأرقام المعروضة تُشتق من قارئين كنونيين فقط، تستهلكهما كل الأسطح (لا معادلات موازية في الواجهات): **المركز** `readPosition` (`projectFinancialService.ts:375-528`) و**نتيجة الفترة** `readRecordedPeriodResult` (`:558-812`)؛ والكشف `statementService.read` يستهلك القارئ الكنوني فقط (`statementService.ts:131-149`). الرئيسية تستهلك `homeControlCenterService` الذي يعيد استخدام `readPosition` نفسه. فحوص MIC الأربعة عشر (`integrityCheckService.ts:36-53`) شبكة أمان نهائية، ومنها MIC-1 (مطابقة القارئ مع الكشف) وMIC-15 (تفرّد مفاتيح الحتمية) وMIC-16 (فصل مال المالك عن النتيجة).

**المعادلة الحاكمة للكاش:** `recordedCashMinor = walletCashMinor + unallocatedCashMinor` (`projectFinancialService.ts:434-440,507`) — مثبتة رقميًا باختبار EXE-013، ومُتحقق منها حيًا في السيناريوهات الأربعة (بعد التوزيع الصريح: المحافظ = الإجمالي المسجل دائمًا).

## 2. المصفوفة (22+ عملية)

| العملية | Layer | مدخل الواجهة | Writer/Service | Store(s) | الكاش | الإيراد/النتيجة | ذمم عملاء | ذمم موردين | المخزون/التكلفة | مال المالك | القروض/الأصول | العكس/التصحيح | Export/Restore | القراء |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| رصيد البداية | 1 | `/cash/wallet/new`، `/setup`، الاستيراد الافتتاحي | `cashContinuity.openWallet` | `cash-wallets` + استمرارية | + (محفظة) | **«ليس مبيعات ولا مال مالك ولا نتيجة»** (العقد الحاكم) | — | — | مواد افتتاحية بمعرفة معلنة/مجهولة | — | — | عكس موثق للقيد | ضمن اللقطة (30 عائلة) | CashWallets، Home، MIC-2/14 |
| بيع مباشر نقدي | 1 | `/direct-sales/new` + ورقة سريعة | `directSaleService.record` | `direct-sales` | يدخل «غير الموزع» أو نسبة محفظة | بحدث البيع نفسه بتاريخه | partial_debt فقط | — | استهلاك اختياري مربوط بـsaleId | — | — | update/cancel + عكس تخصيصات + عكس تحصيل | نعم | Finance، Statement، Parties، Collect |
| بيع مباشر آجل | 1 | نفس الورقة/المحرر + قرار الفرق الصادق (تخفيض/دين/مراجعة) | `directSaleService.record` (partial_debt) | `direct-sales` | المقبوض فقط | كاملًا بتاريخ البيع | revenue−collected | — | — | — | — | كذلك + تحصيل لاحق بمراجعة واحدة بسقف | نعم | Parties، Collect |
| طلب بعربون | 2 | OrderDetail → collectDeposit | `fulfillmentService.collectDeposit` | `craft-orders` | + (عبر registeredCollections) | **لا إيراد عند القبض** | receivable = قيمة−مقبوض | — | — | — | — | عكس عربون نشط + تسوية عربون ذرّية | نعم | OrderDetail، Finance، Parties |
| تسليم طلب + تحصيل متبقٍ | 2 | `/orders/:id/deliver` (مراجعة قبل الالتزام) | `deliveryReviewService.deliver` | **معاملة واحدة 5 مخازن**: craft-orders + inventory-movements + shortages + cash-wallets + continuity | القبض داخل المعاملة؛ التخصيص بسطر مصدر | `recognizeDeliveryValues` **مرة واحدة** | →0 أو دين مسجل | — | استهلاك التسليم بمفتاح مشتق `${orderId}:deliver:...` | — | — | `reverseDelivery` بحركات مرآة | نعم | OrderDetail، Statement، MIC-13 |
| تحصيل من ورقة التحصيل | 1/2 | `/collect` | `collectionService.collect` → الكاتب المالك | craft-orders أو direct-sales + تخصيص | وجهة صريحة | **لا إيراد** (تحصيل فقط) | ينقص الدين | — | — | — | — | عكس تحصيل مزدوج ذرّي | نعم | Collect، Parties، WalletLedger |
| رد تحصيل | 1/2 | سجل التصحيحات | `collectionReversalService` | الكاتب المالك + استمرارية | − يعود | لا أثر إيراد | يعود الدين | — | — | — | — | هو نفسه المسار الموثق | نعم | السجل + الدفاتر |
| مصروف نقدي | 1 | `/finance/new/operating_expense_cash` | `projectFinancialService.record` | `financial-events` | − (غير موزع أو تغطية محفظة بتخصيص سالب) | − مصروف موزّع | — | — | — | — | — | reverse/edit/delete/restore | نعم | Finance، Statement، Activity |
| مصروف مستحق (التزام) | 1 | `/finance/new/operating_expense_payable` | `projectFinancialService.record` | `financial-events` | — لحين التسديد | − مصروف عند التسجيل | — | + payable (بلا dueOn) | — | — | — | تسديد مقيد بسقف لا يكرر المصروف | نعم | «شو عليّ؟» |
| تسديد التزام | 1 | بطاقة «شو عليّ؟» | `record` (payable_settlement_cash) | `financial-events` | − | **لا مصروف ثانيًا** (دلتا −كاش/−ذمم) | — | − payable | — | — | — | موثق | نعم | FinanceObligationsCard |
| شراء مواد نقدي | 2 | `/suppliers` «سجّل شراء مواد» + مصدر صرف | `supplierPurchaseService.recordPurchase` | `supplier-purchases` + تخصيص اختياري | − paid | **لا شيء** («الشراء لا يصبح COGS تلقائيًا») | — | صفر (مسدد) | الاستلام خطوة منفصلة | — | — | editPurchase موثق + عكس دفعة | نعم | Suppliers، Finance، Statement |
| شراء مواد بالدين | 2 | نفس المحرر | `recordPurchase` | `supplier-purchases` | — (أو − الدفعة الأولية) | لا شيء | — | payable = total−paid | — | — | — | كذلك | نعم | Suppliers («المتبقي»)، Statement |
| دفعة المورد | 2 | `/suppliers/purchase/:id/payment` | `recordPayment` (+ نسبة محفظة بمعاملة ثانية) | `supplier-purchases` + استمرارية | − من غير الموزع أو المحفظة | لا شيء | — | − payable | — | — | — | عكس دفعة (⚠ P2-1: النسبة غير ذرّية ولا تُشفى) | نعم | Suppliers، WalletLedger |
| استلام المخزون | 2 | `/inventory` «استلام شراء» (يملأ من الشراء المرتبط) | `inventoryMaterialService.receivePurchase` | `inventory-movements` | — | — | — | — | purchase_receipt بقيمة ≤ إجمالي الشراء | — | — | عكس حركة بمرآة | نعم | Inventory، «بانتظار الاستلام» |
| استهلاك المواد | 2 | `/inventory` «استهلاك أو استلام نقص» (ربط بطلب/بيع/مشروع) | `inventoryMaterialService.consume` | `inventory-movements` | — | يدخل COGS عبر `derivePeriodCogs` (استهلاك مربوط بطلب نهائي فقط) | — | — | − كمية/قيمة من موضع المادة | — | — | عكس بمرآة (⚠ ازدواج يدوي+تسليم بلا حارس) | نعم | Inventory، ملخص الفترة |
| ضبط المخزون (هدر/نقص/جرد) | 2 | `/inventory` «هدر مادة»/«ضبط جرد» | waste/shortage/adjust | `inventory-movements` + `inventory-shortages` | — | الهدر بخسارة معلنة؛ النقص سجلات لا رصيد سالب | — | — | موثقة بمكوناتها | — | — | عكس مع عكس حدث الخسارة معًا | نعم | Inventory، النتائج |
| تحويل بين المحافظ | 3 | `/cash/transfer` | `cashContinuityService.transfer` | `cash-continuity-entries` (طرفا قيد بمفتاح واحد وtransferId) | **صافي صفر** | — | — | — | — | — | — | عكس يعكس الطرفين معًا | نعم | CashWallets، WalletLedger |
| استثمار المالك | 1 | «أدخل مالًا للمشروع» | حدث owner_investment_cash | `financial-events` | + (غير الموزع أو تخصيص) | **ليس إيرادًا** | — | — | — | + رأس مال | — | عكس موثق | نعم | دفتر المالك، Finance |
| السحب الشخصي | 1 | `/finance/withdraw` (مدخل موحد) | حدث owner_withdrawal_cash أو حركة دفتر (بحسب سياسة) | `financial-events` أو `owner-movements` + استمرارية | − | **ليس مصروفًا** | — | — | — | − رأس مال/حق | — | عكس ذرّي (⚠ P3-1: مسار الدفتر بلا فحص تغطية) | نعم | دفتر المالك، MIC-16 |
| قرض (صادر) + سداد | 3 | `/loans/*` | `loanService.create/recordRepayment` | معاملة [loans + financial-events] | − عند الإقراض / + عند السداد | **ليس إيرادًا ولا مصروفًا** («مالك عند غيرك») | — | — | — | — | الرصيد مشتق لا مخزن | حرس عائلة + عكس/تصحيح | نعم | Loans، Finance، Statement |
| أصل: شراء/إهلاك/تخلص/شطب | 3 | `/assets/*` | `assetService.*` | معاملة [assets + financial-events] | − عند الشراء النقدي فقط | الإهلاك غير نقدي يخصم الربح فقط؛ الشراء ليس مصروفًا | — | — | — | — | دفتر مشتق من الأحداث | تصحيح اقتناء/تراجع إهلاك/تصرف موثقة | نعم | Assets، Statement، MIC-10/11 |
| عربون محتفظ | 3 | تصنيف العربون | حدث deposit_retained_revenue | `financial-events` | **دلتا صفر** (الكاش دخل سابقًا بالقبض) | + إيراد مصنف | — | — | — | — | — | موثق (EXE-013 يثبت ثبات الكاش) | نعم | Finance، Statement |
| التصدير والاستعادة | 1 | الإعدادات | `localTransferService` | لقطة 30 عائلة ذرّية | يُستعاد كما هو | كذلك | كذلك | كذلك | كذلك | كذلك | كذلك | نسخة احتياطية إلزامية قبل الاستبدال + فحص سلامة بعده | **هو المسار** | — |

## 3. إثبات عدم الاحتساب المزدوج (خلاصة الأدلة)

1. **الإيراد مرة واحدة:** عند تسليم الطلب أو بحدث البيع؛ القبض/العربون/التحصيل اللاحق لا يولّدون إيرادًا (EXE-013 يطابق رقميًا).
2. **التخصيص محايد إجماليًا:** +X محفظة = −X غير موزع؛ المُتراجَع يعود لغير الموزع؛ دفعة مورد من محفظة = تخصيص سالب صافيه صفر.
3. **مفاتيح حتمية داخل معاملة الكتابة** لكل كاتب (`writeOneIdempotent` — إصلاح P0 للإرسال المتزامن، مختبر بـ`reentrancyGuards`).
4. **ذرّية متعددة المخازن** لكل عملية مركبة (التسليم 5 مخازن؛ عكس التسليم؛ تسوية العربون؛ حركة المالك؛ القرض؛ الأصل؛ تصنيف العربون).
5. **حرس الافتتاح الثاني** (لا افتتاح محفظة مزدوج) و**منع ابتلاع التوزيع الثاني** (EXE-001) و**حرس التسليم/القرض/المواعيد داخل المعاملة**.
6. **التسديد لا يكرر المصروف؛ تصنيف العربون لا يحرك الكاش؛ النقص سجلات لا أرصدة سالبة.**

**الثغرة الوحيدة المفتوحة:** ازدواج الاستهلاك لطلب واحد (يدوي + ورقة تسليم) — `derivePeriodCogs` يجمعهما ولا حارس يمنعه؛ **والاختبار الحي أثبت أن ورقة التسليم تقترحه افتراضيًا** (3/3 سيناريوهات فيها مواد) — انظر gap-register G-01.

## 4. الربح مقابل الكاش (البنية)

- **الكاش:** معادلة المحافظ+غير الموزع فقط — لا يُشتق من الإيراد أبدًا؛ التحويل صافي صفر؛ القرض/الأصل/الاستثمار تحركات ملك لا نتائج.
- **النتيجة:** `recognizedRevenue + directSaleRevenue − effectiveDirectCost − directSaleCostKnown − operatingExpense − depreciation − writeOff + disposal + retainedDeposit`.
- **القيم الخمس مفصولة بنيويًا:** صفر موثق / غير مسجل / غير متاح / تكلفة ناقصة / تقديرية — لا يُعرض صفر مكان مجهول، ولا رقم وهمي مكان ناقص.
- **الجسر الحسابي غائب:** الفصل والتفسير موجودان بكل مكون (truthLines بالكشف)، لكن لا معادلة تجمع (نتيجة + Δذمم + Δمخزون − سحوبات = Δكاش) — فجوة قيمة موثقة (VALIDATE_DURING_PILOT).
