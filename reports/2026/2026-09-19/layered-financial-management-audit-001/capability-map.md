# خريطة القدرات والطبقات — Micro (commit 87ebcf2)

> هذا الملف مخرج التدقيق «Layered Financial Management Completeness & Integration Audit» — 2026-09-19. مصدره تحليل معماري القراءة-فقط (الوكيل 2-a) مدعومًا بالاختبار الحي. اقتباسات الكود بأسلوب `ملف:سطر`.

## 1. منهجية الجرد

جُردت القدرات من: مسارات `app/MicroRouter.tsx:105-187` (59 عنصر Route)، شريط التنقل الخماسي الثابت `app/navigation.ts:15-21`، صفحات `pages/` (54 صفحة غير اختبارية)، خدمات التطبيق في `application/` (34 مجلدًا)، ووحدات domain في `src/domain/` (14 وحدة). «الطبقة» وفق فرضية التدقيق: 1=مالية أساسية، 2=تشغيل منظم، 3=مالية متقدمة مبسطة، وبنية/عرضية لما يشغّل كل الطبقات.

**تصحيحان مصطلحيان مهمان للأرقام:** المخازن الفعلية 32 (رقم المخطط 35 ليس عدد المخازن — `storage/local/types.ts:38`)، ولقطة التصدير تغطي 30 عائلة (إصدار المظروف 27 ليس عدد العائلات)؛ تُستثنى `form-drafts` و`local-security` عمدًا (المسودات سريرية والقفل خارج النسخ عمدًا).

## 2. جرد القدرات حسب الطبقة (القدرة → المدخل → الكاتب → المخازن)

### الطبقة 1 — الإدارة المالية الأساسية (≈16 قدرة)

| # | القدرة | المدخل (Route/UI) | Writers / الخدمات | Stores المكتوبة |
|---|---|---|---|---|
| 1 | الإعداد الأول (اسم + محفظة اختيارية + موقف افتتاحي صادق) | `/setup` (`StartupGate.tsx:67`) | `profiles.save` + `cashContinuity.openWallet` (`Setup.tsx:150-171`) | `activity-profile`, `cash-wallets`, `cash-continuity-entries` |
| 2 | صفحة الأساس (موقف افتتاحي لاحق) | `/foundation` | قراءة فقط | — |
| 3 | البيع المباشر السريع (نقدي) | «سجّل بيعًا» الرئيسية → QuickSaleForm | `directSales.record` (`QuickSaleForm.tsx:123-137`) | `direct-sales` (+ استمرارية عند نسبة المحفظة) |
| 4 | البيع الآجل السريع (دين الزبون) | نفس الورقة، مفتاح الآجل (`QuickSaleForm.tsx:258-292`) | `directSales.record` بـ`partial_debt` | `direct-sales` |
| 5 | محرر/تصحيح البيع المباشر | `/direct-sales/new`, `/direct-sales/:id` | `directSaleService.record/update/cancel` | `direct-sales`, `cash-continuity-entries` |
| 6 | المصروف/الالتزام/التسديد/الأمانات/الهالك | `/finance/new/:type` | `projectFinancialService.record` | `financial-events`, `cash-continuity-entries` |
| 7 | الكاش الأساسي (محفظة/درج) | `/cash`, `/cash/wallet/new`, `opening-later` | `cashContinuityService.openWallet/adjust` | `cash-wallets`, `cash-continuity-entries` |
| 8 | توزيع الكاش غير الموزع | `/cash/distribute` | `distributeUnallocated` (`projectFinancialService.ts:1104`) | `cash-continuity-entries` |
| 9 | عدّ الصندوق (تسوية موثقة) | `/cash/count` | تسوية موثقة | `cash-wallets`, `cash-continuity-entries` |
| 10 | دفتر الناس (ذمم قراءة) | `/parties` | قراءة تجميعية فقط — لا CRM ولا مخازن جديدة | — (قراءة) |
| 11 | عليّ للموردين التشغيلية | بطاقة «شو عليّ؟» + `/finance/new/operating_expense_payable` | `projectFinance.record` | `financial-events` |
| 12 | ورقة التحصيل (طلبات + بيع آجل) | «عربون أو تحصيل» → `/collect` | `collectionService.collect` يوجّه للكاتب المالك (`collectionService.ts:145-184`) | `craft-orders` أو `direct-sales` |
| 13 | نتيجة الفترة + الكشف + نطاق المقارنة | `/finance?view=period` + `/finance/statement` | قراءة كنونية `readRecordedPeriodResult` + `statementService` | — (قراءة) |
| 14 | مال المالك (رأس مال/حق/سحب) | `/finance/owner-entitlement`, `/finance/withdraw` | `ownerEntitlementService` + `projectFinancialService` (مدخل موحد بحارس تقاطعي) | `owner-entitlement-*`, `owner-movements`, `financial-events` |
| 15 | التصحيح/التراجع الموثق | المحررات + `/cash/entry/:id/reverse` + سجل التصحيحات | `commitFinancialEventCorrection/Replacement` | `financial-events`, `cash-continuity-entries` |
| 16 | التصدير/الاستيراد الكامل | الإعدادات ← «البيانات والنسخ الاحتياطي» | `localTransferService.createVerifiedExport/confirmImport` | لقطة 30 عائلة |
| — | الاستيراد الافتتاحي الموجّه | `?focus=guided-import` | `guidedOpeningImportService` (نظام فارغ فقط) | ملف+محافظ+مواد |
| — | القارئ الكامل للنشاط | «آخر ما حدث» | `activityService` (قراءة 15 عائلة) | — (قراءة) |

### الطبقة 2 — التشغيل المنظم (≈12 قدرة)

| # | القدرة | المدخل | الكاتب | المخازن |
|---|---|---|---|---|
| 1 | الطلبات الكاملة (مسودة→اتفاق→تنفيذ→تسليم) | `/orders/*` | `fulfillmentService` + `deliveryReviewService` (مراجعة قبل الالتزام) | `craft-orders`, `order-drafts`, `cost-estimates` |
| 2 | عربون/تحصيل الطلبات والتسوية الذرّية | OrderDetail | `commitDepositRefundSettlement` | `craft-orders` + `cash-*` |
| 3 | تكلفة الطلب CostSnapshot | محرر التكلفة | لقطة مجمدة عند الاتفاق (مواد/وقت/بنود + ثقة) | `craft-orders` |
| 4 | المواعيد والتكرار | `/schedule` | `scheduleService` + حرس تعارض | `schedule-entries`, `schedule-recurrences` |
| 5 | قرار السعة | ضمن الجدولة | `capacityDecisionService` (صادق في المجهول) | — (قراءة) |
| 6 | الموردون والمشتريات والدفعات | `/suppliers/*` | `supplierPurchaseService` (كتابة ذرّية) | `supplier-purchases` |
| 7 | المواد والمخزون + تفعيل مؤرخ + نقص موثق | `/inventory/*` | `inventoryMaterialService` (قرار ٩: سجل تفعيل) | `materials`, `inventory-movements`, `inventory-shortages`, `inventory-activations` |
| 8 | الفعلي مقابل المخطط (variance) | OrderDetail | `readOrderActualMaterialComparison` | — (قراءة) |
| 9 | الكتالوج (منتجاتي وخدماتي) | `/catalog` | مرجع بلا أثر مالي | `catalog-items`, `measurement-units` |
| 10 | قوالب المكونات/yield | الكتالوج | تخطيط فقط | `catalog-templates` |
| 11 | المتابعة والمتأخرات | «الأهم الآن»/«اليوم» | `dailyFollowUpService` | — (قراءة) |
| 12 | ربط الشراء بالاستلام | `/inventory` «استلام شراء» | `receivePurchase` (يملأ القيمة/الكمية من الشراء) | `inventory-movements` + ربط `purchaseId` |

### الطبقة 3 — المالية المتقدمة المبسطة (≈13 قدرة)

| # | القدرة | المدخل | الكاتب | ملاحظات التكامل |
|---|---|---|---|---|
| 1 | المحافظ المتعددة والتحويلات | `/cash/wallet/new`, `/cash/transfer` | `cashContinuityService.transfer` (طرفا قيد بمفتاح واحد) | صافي صفر على الإجمالي — مثبت حيًا |
| 2 | القروض (الصادرة فقط) | `/loans/*` | `loanService` + `commitLoanRecord` ذرّي | «مالك عند غيرك» — لا مسار اقتراض (فجوة) |
| 3 | الأصول والإهلاك | `/assets/*` | `assetService` + معاملات ذرّية | إهلاك غير نقدي معلن؛ لا تسجيل يوم الشراء بحكم التصميم |
| 4 | العربون المحتفظ | ضمن التسليم | تصنيف عربون موثق | دلتا صفر كاش (EXE-013) |
| 5 | متوقعات الكاش القصيرة (G5) | «قرار الكاش» | `g5Service` | تصريحات مالك + أرصدة مؤرخة؛ «غير متاح» عند نقص التواريخ |
| 6 | التغطية والتعادل | ملخص الفترة | domain/g5 | **OVERBUILT_OR_PREMATURE** |
| 7 | سياسات هامش الأعمال المتكررة | سياسات المالية | domain/recurring-margin | **OVERBUILT_OR_PREMATURE** |
| 8 | الوقت الفعلي | OrderDetail | `actualTimeService` | COMPLETE_BUT_DISCONNECTED |
| 9 | المؤشرات والتنبيهات | الرئيسية | من البيانات الحالية فقط | — |
| 10 | ربحية أسماء الأعمال | ملخص الفترة | تجميع بالاسم لا بمرجع الكتالوج | PARTIAL |
| 11 | الميزانيات/الأهداف | — | — | **MISSING_GROWTH_CAPABILITY** (لا وجود) |
| 12 | هامش حماية السعر | الحاسبة/التقديرات | أداة بلا أثر | — |
| 13 | سلامة الحسابات (14 فحص MIC) | `/tools/integrity` | قراءة فقط | — |

### بنية/عرضية (≈8): القفل/PIN (خارج اللقطة عمدًا)، المشاركة اليدوية (4 أنواع رسائل واتساب)، السوق (إعلان صادق — FUTURE_SCOPE)، المزامنة (خارج النطاق المعلن — FUTURE_SCOPE)، طريقة العمل، الحاسبة/التقديرات، وضع القائمة الميت (PARTIAL)، SET-003 تفعيل/تعطيل القدرات (PARTIAL).

## 3. خريطة اعتماد الطبقات

```
الطبقة 3 (محافظ متعددة/قروض/أصول/G5)
   ▲ قراءة فقط من المالية· لا كتابة تعتمد عليها
الطبقة 2 (طلبات/موردون/مخزون/مواعيد)
   ▲ تعتمد على L1 في الإيراد/الذمم/الكاش — مبرر ومتصل بالكامل
الطبقة 1 (بيع/مصروف/كاش/ذمم/نتيجة/مالك/تصدير)
   = مستقلة كتابةً 100% (مثبتة) · قراءتها تقترن بـ12 مصدرًا في صفحة المالية (كل-أو-لا شيء)
```

- **استقلال كتابة الطبقة 1:** كتابات L1 لا تلمس مخازن L2/L3 أبدًا (`directSales.record` → `direct-sales` فقط؛ المصروف → `financial-events`؛ الكاش → مخازن الكاش). رحلة L1 الكاملة اشتغلت حيًا بمشروع بلا أي قدرة اختيارية.
- **اعتماد قراءة مقيد بالعرض:** `Finance.tsx:177-231` يقرأ 12 مصدرًا (منها أصول/قروض/مخزون) — يعمل بغيابها لكن أي فشل قراءة يحجب الصفحة كاملة.
- **لا اعتماد غير مبرر لكتابة L1 على المتقدم.**
- **الترقية لا تنشئ Writers موازية:** تفعيل المخزون بعد مبيعات = سجل تفعيل مؤرخ (`inventory-activations`) بلا backfill؛ حالة التكلفة القديمة تظهر بصدق عبر `cogsStatus`.
- **الكاتبان التاريخيان لمال المالك** موحّدان بمدخل واحد + حارس تكرار تقاطعي (`ownerEntitlementService.ts:196-247`) — النموذج المحروس الوحيد؛ **ثنائية بيع/طلب بلا حرس تقاطعي** (خطر إدخال بشري).
- **ثلاثية مصادر معرفة التكلفة** (costMinor يدوي / CostSnapshot / استهلاك) موحدة عرضيًا بـ`cogsStatus`.

## 4. جدول التصنيف النهائي (كل قدرة → التصنيف → المسوغ)

| القدرة | التصنيف | المسوغ المختصر |
|---|---|---|
| الإعداد الأول | COMPLETE_AND_INTEGRATED | 3 خطوات، إلزامي وحده الاسم، مسودة محروسة |
| صفحة الأساس | COMPLETE_AND_INTEGRATED (بقراءة مقترنة) | اختيارية لكنها تقرأ مخازن L2 |
| البيع المباشر (نقدي/آجل) + تصحيحه | COMPLETE_AND_INTEGRATED | كاتب واحد، idempotencyKey، تعارض مراجعات |
| المصاريف/الالتزامات/التسديد/أمانات/هالك | COMPLETE_AND_INTEGRATED | 17 نوع حدث موحد بمحرر موجّه واحد |
| الكاش الأساسي + توزيع + عدّ صندوق | COMPLETE_AND_INTEGRATED | غير الموزع شريط صريح |
| دفتر الناس | COMPLETE_AND_INTEGRATED | قراءة تجميعية بلا مخازن جديدة |
| ورقة التحصيل | COMPLETE_AND_INTEGRATED | توجيه للكاتب المالك |
| نتيجة الفترة + الكشف + النطاق | COMPLETE_AND_INTEGRATED | صدق resultStatus |
| مال المالك + السحب الموحد | COMPLETE_AND_INTEGRATED | حارس تكرار تقاطعي |
| التصحيح/التراجع الموثق | COMPLETE_AND_INTEGRATED | استبدال/تراجع بأثر محفوظ |
| التصدير/الاستيراد الكامل | COMPLETE_AND_INTEGRATED | مظروف تحقق + بوابة رمز + نسخة احتياطية إلزامية |
| الاستيراد الموجّه | COMPLETE_AND_INTEGRATED | نظام فارغ فقط + معاينة |
| القارئ الكامل | COMPLETE_AND_INTEGRATED | قراءة موحدة 15 عائلة |
| الطلبات الكاملة | COMPLETE_AND_INTEGRATED | عقود مختبرة + مراجعة تسليم قبل الالتزام |
| عربون/تحصيل/تسوية | COMPLETE_AND_INTEGRATED | ذرّية `commitDepositRefundSettlement` |
| CostSnapshot | COMPLETE_AND_INTEGRATED | لقطة مجمدة بلا إعادة ربط |
| المواعيد والتكرار | COMPLETE_AND_INTEGRATED | حرس تعارض |
| قرار السعة | COMPLETE_AND_INTEGRATED | صادق في المجهول (متقدم لكن محروس) |
| الموردون والمشتريات | COMPLETE_AND_INTEGRATED | كتابات ذرّية |
| المواد والمخزون + تفعيل مؤرخ | COMPLETE_AND_INTEGRATED | النقص سجلات لا رصيد سالب |
| الفعلي مقابل المخطط | COMPLETE_AND_INTEGRATED | مقارنة بمعرفة معلنة |
| الكتالوج | COMPLETE_AND_INTEGRATED | مرجع بلا أثر مالي (زر الرئيسية لا يخفى — انظر SET-003) |
| قوالب المكونات/yield | COMPLETE_BUT_DISCONNECTED | تخطيط فقط بلا أثر مالي بالتصميم |
| المتابعة والمتأخرات | COMPLETE_AND_INTEGRATED | «اليوم»/«الأهم الآن» بروابط عميقة |
| المحافظ المتعددة والتحويلات | COMPLETE_AND_INTEGRATED | مثبت حيًا (صافي صفر) |
| القروض (الصادرة) | COMPLETE_AND_INTEGRATED | ذرّي؛ لا مسار اقتراض = فجوة نمو منفصلة |
| الأصول والإهلاك | COMPLETE_AND_INTEGRATED | إهلاك غير نقدي معلن |
| العربون المحتفظ | COMPLETE_AND_INTEGRATED | قرار موثق معلق ظاهر |
| متوقعات الكاش القصيرة | COMPLETE_AND_INTEGRATED | سجل منفصل + تراجع |
| التغطية والتعادل (G5) | OVERBUILT_OR_PREMATURE | تصنيف fixed/variable/mixed فوق نضج الجمهور |
| سياسات الهامش المتكرر | OVERBUILT_OR_PREMATURE | سلاسل إصدارات مؤسسية لمستخدم فردي |
| الوقت الفعلي | COMPLETE_BUT_DISCONNECTED | يغذي سياسة actual_time فقط |
| طريقة العمل | COMPLETE_AND_INTEGRATED | تفضيل عرضي |
| المؤشرات والتنبيهات | COMPLETE_AND_INTEGRATED | من البيانات الحالية فقط |
| ربحية المنتجات (mix) | PARTIAL | بالاسم لا بمرجع كتالوج |
| الميزانيات/الأهداف | MISSING_GROWTH_CAPABILITY | لا وجود (بحث شامل) |
| حاسبة/تقديرات | COMPLETE_AND_INTEGRATED | أداة بلا أثر + جسر مسودة |
| سلامة الحسابات | COMPLETE_AND_INTEGRATED | قراءة فقط بلا إصلاح تلقائي |
| القفل/PIN | COMPLETE_AND_INTEGRATED | خارج اللقطة عمدًا |
| المشاركة اليدوية | COMPLETE_AND_INTEGRATED | محرر يحرس المدخلات |
| السوق | FUTURE_SCOPE | إعلان صادق بلا وظيفة |
| المزامنة/الأجهزة | FUTURE_SCOPE | خارج النطاق المعلن |
| القرض المأخوذ (اقتراض) | MISSING_GROWTH_CAPABILITY | لا مسار تسجيل (اكتشاف السيناريو 4 الحي) |
| SET-003 تفعيل/تعطيل القدرات | PARTIAL | منفذ لـorders فقط؛ suppliers بلا أي تنفيذ (مؤكد حيًا) |
| قائمة ورقة التسجيل (وضع menu) | PARTIAL | سطح ميت بلا مستدعي حي |
| PWA/offline الميداني | UNVERIFIED | REAL_DEVICE_QA_NOT_PERFORMED |

**عدّ التصنيفات:** COMPLETE_AND_INTEGRATED=33 · COMPLETE_BUT_DISCONNECTED=2 · PARTIAL=4 · OVERBUILT_OR_PREMATURE=2 · MISSING_GROWTH_CAPABILITY=2 · FUTURE_SCOPE=2 · UNVERIFIED=1 · MISSING_ESSENTIAL=0.

## 5. جودة Progressive Disclosure

الإفصاح التدريجي منضبط التصميم: الإعداد 3 خطوات؛ الأساس دائم الظهور؛ القدرات الاختيارية مطوية؛ الأدوات المتقدمة خلف «المزيد»/«العمق». مواطن الخلل: (1) سطحا G5 متقدمان في مسار العرض الافتراضي لملخص الفترة؛ (2) مقعد «السوق» الثابت في شريط التنقل (كلفة تنقل غير مبررة)؛ (3) وعد الإعدادات لتعطيل القدرات أوسع من التنفيذ؛ (4) قائمة ورقة التسجيل وضع menu سطح ميت.

## 6. مخاطر البيانات عند التوسع

1. ازدواج تسجيل البيعة بيعًا وطلبًا (بشري غير محروس).
2. إتاحة المالية كل-أو-لا شيء على 12 قراءة.
3. تجزئة معرفة التكلفة عبر 3 مصادر (موحدة عرضيًا).
4. حارس مال المالك بالمبلغ-المطلق-والتاريخ (إيجابيات كاذبة محتملة؛ تكرار بمبالغ مختلفة لا يُكتشف).
5. `disabledCapabilities` حارس عرضي لا عزل تشغيلي (المسارات العميقة تعمل).
6. الاستيراد الكامل يستبدل كل شيء (محروس بمعاينة/PIN/نسخة احتياطية — يبقى خطرا معلنًا).
7. مخطط 35 بلا هجرات حذف (توافق خلفي ملتزم ومختبر).
