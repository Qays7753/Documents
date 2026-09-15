# تدقيق حقائق المنتج ورحلات الاستخدام — Micro (قراءة فقط)

**التاريخ:** 2026-09-15 (آسيا/عمّان)
**المرجع المفحوص:** `Qays7753/Micro` @ `origin/main` = `f21f777d3b4df874806061755dff5fc956ca4cf3` (2026-09-15 11:01:58 +0000 — «Merge Brand Activation and corrected Launch Splash»)
**طريقة الفحص:** قراءة كود ثابتة (read-only) + استعلامات GitHub API موثقة. لم تُشغَّل الاختبارات ولم يُنفَّذ التطبيق تفاعليًا.
**حدود الكتابة:** لم تُنفَّذ أي كتابة على مستودع Micro أو على مجلد لقطات الشاشة. الكتابة الوحيدة هي هذا التقرير وحجته في مستودع Documents على الفرع `audit/micro-product-facts-journey-20260915`.
**ملاحظة مسارات:** كل المسارات في هذا التقرير نسبية إلى `apps/prototype-web/client/src/` ما لم تُسبَق بـ `src/domain/` أو `docs/`.

---

## Executive summary

- الشريط السفلي الحالي **أربعة مقاعد وزر وسطي**، لا خمسة: «مشروعي الآن» (`/`) · «العمل» (`/orders`) · **FAB «سجّل»** (يفتح `QuickActionSheet` بخمسة أفعال، اثنان منها — البيع والمصروف — يُكملان داخل الورقة نفسها) · «مالي» (`/finance`) · «أدواتي» (`/tools`) — `VERIFIED` (`app/navigation.ts:13-18`).
- جرد المسارات من الكود: **56 عنصر `<Route>`** (بينها تحويلان: `/review` → `/finance` و`/orders/new` → `/orders/draft/new?intent=…` + NotFound)، و**52 صفحة**، و**32 مخزن IndexedDB** في قاعدة `micro-prototype-local` (مخطط 35 / تصدير 27) — `VERIFIED`.
- لا يوجد Auth ولا سحابة ولا مزامنة: البيانات محلية بالكامل، مع تصدير/استيراد ذرّي وقفل PIN محلي اختياري وبوابة إقلاع تحوّل أول فتح إلى `/setup` — `VERIFIED`.
- نموذج المال: «الكاش المسجل» = كاش غير موزع + محافظ؛ التحصيل والمصروف والشراء لا تلمس المحافظ تلقائيًا بل تنتظر «تخصيصًا» (allocation) صريحًا؛ 17 نوع حدث مالي بمصفوفة Deltas واحدة (`src/domain/financial-event/policies.ts:275-306`) — `VERIFIED`.
- فرضية «أدواتي = أدوات مستقلة بلا أثر مالي رسمي تلقائي»: **مؤكدة في الكود** — الحاسبة تكتب مخزن `cost-estimates` فقط، وفحص السلامة بلا أي كتابة (13 فحصًا MIC)، والجسر الوحيد يدوي معلن (تقدير → مسودة `intent=planned_design`) — `VERIFIED`.
- فرضية «السوق»: **مستقبل موثق فقط** — لا مسار ولا مخزن ولا كود؛ صف معطّل في أدواتي («السوق والتوصيل» — غير متاح في هذه المرحلة) — `VERIFIED`.
- فرضية «Delivery خدمة تشغيلية علوية مرتبطة بالطلبات»: **ليست الوضع الحالي** — التسليم في الكود خطوة داخل دورة الطلب فقط (`/orders/:id/deliver`، مدخلها الوحيد زر «راجع التسليم وسجّله» من تفاصيل طلب في حالة `ready`)؛ الخدمة العلوية (أيقونة سيارة في الترويسة) موثقة مستقبلًا في عقود E-00 فقط — `VERIFIED`.
- «الموردون» في الكود = دفتر التزامات شراء مواد داخلي (ما عليك لمن تشتري منه) بلا أي مفهوم سوق أو موردين خارجيين — `VERIFIED`.
- وُجدت **ستة تناقضات وثائق–كود** أبرزها: تضارب موضع «السوق»/المقعد الخامس في أربعة مواضع (مع تعليقي كود متقادمين)، تقادم `current-state.md` §40 (يصف PR #159 بأنه مفتوح وهو مدموج منذ 2026-09-13)، وتعبير «كم عندي الآن» الموعود في وثيقة التوزيع غير موجود إطلاقًا في الواجهة.
- مخاطر مؤكدة: اختيار **أول سجل افتراضيًا** في `InventoryMovementEditor` عند غياب معاملات العمق (خطر إسناد استهلاك/هدر لطلب أو بيع خاطئ)، ونص صفحة الفحص يقول «ستّة عشر فحصًا» بينما الخدمة تنفذ 13.
- مسار لقطات الشاشة المحدد أعاد **404** → `SCREENSHOT_SOURCE_UNVERIFIED`؛ لم تُفحص أي لقطة التزامًا بحدود هذا التدقيق.
- لم تُنفَّذ أي كتابة على Micro أو لقطات الشاشة؛ التقرير في Documents على فرع مخصص مع PR واحد **غير مدموج**.

---

## Verified baseline

| البند | القيمة الموثقة | التصنيف | الدليل |
|---|---|---|---|
| `origin/main` SHA الكامل | `f21f777d3b4df874806061755dff5fc956ca4cf3` | `VERIFIED` | `git log -1 --date=iso origin/main` |
| تاريخ الرأس | 2026-09-15 11:01:58 +0000 | `VERIFIED` | نفس الأمر |
| عنوان آخر commit | «Merge Brand Activation and corrected Launch Splash» | `VERIFIED` | نفس الأمر |
| حالة النسخة المحلية | نظيفة تمامًا: `## main...origin/main` بلا أي تعديل | `VERIFIED` | `git status --short --branch` |
| PR #159 | **مدموج**: «Micro hardening, exact values, architecture, and UI closure» — merged_at `2026-09-13T08:52:12Z` — merge_commit `c0469e265f24c70427eb7826dee717be117cff87` | `VERIFIED` | GitHub API `/repos/Qays7753/Micro/pulls/159` |
| الفروع البعيدة | `origin/main` (الرأس + `origin/HEAD`)، `origin/jules-15390500015238590867-77e56821`، `origin/agent/group1-traceability-finalize`، `origin/task/direct-sale`، وثلاثة فروع `keep/…` أرشيفية | `VERIFIED` | `git branch -r --sort=-committerdate` |
| مستودع Documents | الفرع الافتراضي `main` @ `f919982c692e5ba78cf3284a4240c45f66be91c6`؛ صلاحية `push: true` مؤكدة بالتوكن قبل أي كتابة | `VERIFIED` | GitHub API `/repos/Qays7753/Documents` |
| مسار اللقطات | `planning/micro-brand-assets-motion-splash-resume-2026/screenshots` على `main` = **404** (المجلد `planning/` يحوي ثلاثة مجلدات أخرى فقط) | `SCREENSHOT_SOURCE_UNVERIFIED` | GitHub API contents |
| طريقة الفحص | قراءة ثابتة للكود والعقود والاختبارات؛ لم تُشغَّل الاختبارات ولا التطبيق | `NOT_EXECUTED` لكل سلوك ديناميكي غير مغطى باختبار مقروء | — |

**حدّ مهم:** رأس `main` الحالي (`f21f777`) يقع بعد آخر موضع توثقه `docs/operations/current-state.md` (§40 يصف الرأس عند `4af025d` ويقول إن PR #159 «مفتوح وغير مدمج») — راجع القسم 14.

---

## Current shell and navigation

### المقاعد والعناصر الحالية (كما هي في الكود — لا كما في الفرضية)

| العنصر | التسمية العربية الظاهرة | المسار/المعرّف الداخلي | الوظيفة الحالية | يفتح | تصنيف الدليل | الدليل |
|---|---|---|---|---|---|---|
| مقعد 1 | مشروعي الآن | `/` | مركز تحكم «ماذا عليّ اليوم؟»: الأهم الآن، اليوم، حقائق مسجلة، وحدات مالي/منتجاتي/مسارات مرتبطة، آخر ما حدث | `Home` | `VERIFIED` | `app/navigation.ts:14`، `pages/Home.tsx:135-489` |
| مقعد 2 | العمل | `/orders` | الطلبات + المبيعات المباشرة + المسودات + مقطع المواعيد الدائم (قسم الطلبات مخفي حتى أول طلب محفوظ — القرار ٢٤) | `Orders` | `VERIFIED` | `app/navigation.ts:15`، `pages/Orders.tsx:112-295`، `Orders.ui.test.tsx:108,117` |
| الزر الوسطي (FAB) | سجّل | `QuickActionSheet` | ورقة أفعال عند الطلب: «ماذا تريد أن تسجّل؟» بخمسة أفعال (جدول تالٍ)؛ تُحمَّل كسولًا وتُجلب مسبقًا عند الخمول | ورقة فوق السطح الحالي | `VERIFIED` | `components/layout/BottomNav.tsx:29-32`، `components/layout/QuickActionSheet.tsx:55-81`، `app/MicroAppShell.tsx:50-56` |
| مقعد 3 | مالي | `/finance` | تبويبان: «الوضع الآن» و«شو صار خلال الفترة»؛ نبضة، قرار الكاش، مال المالك، بطاقات الموقف، طبقة أفعال، سجل الأحداث والتصحيحات | `Finance` | `VERIFIED` | `app/navigation.ts:16`، `pages/Finance.tsx:292-314` |
| مقعد 4 | أدواتي | `/tools` | حاسبة التكلفة، تقديراتي المحفوظة، فحص سلامة مالي، حالة الوحدات، مدخل النسخ الاحتياطي | `Tools` | `VERIFIED` | `app/navigation.ts:17`، `pages/Tools.tsx:170-234` |
| ترس الإعدادات (الترويسة) | الإعدادات | `/settings` | متاح من كل المسارات (بما فيها `/setup`) عبر `requestNavigation` مع حارس التغييرات غير المحفوظة | `Settings` | `VERIFIED` | `components/layout/AppHeader.tsx`، `app/MicroAppShell.tsx:96` |
| مبدّل المظهر (الترويسة) | تفعيل المظهر الفاتح / تفعيل المظهر الداكن | `ThemeContext` | الفاتح افتراضي؛ الداكن اختيار صريح محفوظ؛ لا يتبع النظام أبدًا | — | `VERIFIED` | `contexts/ThemeContext.tsx:20-25`، `App.tsx:15` |
| تسمية السياق (الترويسة) | متغيرة: «المواعيد»، «محافظ الكاش»، «المواد والمخزون»، «الموردون والمشتريات»، «دفتر الناس»، «أدواتي»، «الإعدادات»، «ملف المالك»، «مراجعة التسليم»، «الأصول»، «القروض»، «ورقة التحصيل»، «بيع مباشر»، «الكتالوج»، «معاينة المشاركة»، «صفحة الأساس»، «مايكرو» احتياطًا | `getNavigationLabel()` | تُخفى حين يكرر h1 التسمية نفسها (`/finance`، `/schedule`، `/settings`، `/inventory`، `/suppliers`، `/cash`)؛ «تأسيس محلي» فوق `/setup` | — | `VERIFIED` | `app/navigation.ts:20-48`، `app/MicroAppShell.tsx:26-33` |
| شاشة الإقلاع | جارٍ فتح مشروعك المحلي… | `BrandLaunchSplash` | مرة واحدة لكل تحميل صفحة؛ تُفك بعد استقرار بوابة الإقلاع وانتهاء الحركة (سقف صلب 4000ms؛ `prefers-reduced-motion` → علامة ثابتة) | — | `VERIFIED` | `components/brand/BrandLaunchSplash.tsx:29-110`، `app/MicroRouter.tsx:82-90` |
| غطاء القفل | «Micro مقفل» + «رمز القفل» | `AppLockGate` (`local-security`) | يغطي المحتوى على كل المسارات عدا `/setup` و`/settings` عند تفعيل القفل وتجاوز مدة الخمول؛ تأخيرات تصعيدية 3/10/30 ثانية | — | `VERIFIED` | `components/security/AppLockGate.tsx:26-201` |
| إشعارات PWA | «أنت غير متصل الآن» / «تحديث Micro جاهز» / «ثبّت Micro على جهازك» | `PwaRuntimeNotice` / `PwaInstallControl` | داخل `<main>` لا الترويسة؛ التحديث محجوب فوق نماذج متسخة | — | `VERIFIED` | `app/MicroAppShell.tsx:99-100`، `pwa/register.ts:52-118` |
| سلوك لوحة المفاتيح | — | `data-keyboard-open` | إخفاء الترويسة والشريط السفلي معًا عند فتح لوحة المفاتيح (فرق ارتفاع >120px) | — | `VERIFIED` | `app/MicroAppShell.tsx:62-69` |

### أفعال الزر الوسطي (QuickActionSheet)

| الفعل | التسمية الظاهرة | الوصف الحرفي | التتمة | الهدف | تصنيف الدليل | الدليل |
|---|---|---|---|---|---|---|
| بيع سريع | تسجيل بيع | «احفظ بيعًا مباشرًا من دون إنشاء طلب.» | **داخل الورقة** (QuickSaleForm): المبلغ إلزامي وحده؛ تكلفة اختيارية («لا أعرف الآن — الربح «غير متاح» لا صفر»)؛ آجل باسم زبون؛ وجهة قبض (الدرج افتراضيًا أو «غير موزع») | إيصال «سُجّل بيع» + «افتح السجل» → `/direct-sales/{id}` | `VERIFIED` | `components/layout/QuickActionSheet.tsx:55-81`، `components/layout/QuickSaleForm.tsx:160-298` |
| مصروف سريع | تسجيل مصروف | «سجّل مصروفًا مدفوعًا في لحظته، من أي مكان.» | **داخل الورقة** (QuickExpenseForm): المبلغ إلزامي؛ بند اختياري؛ وجهة صرف؛ تصنيف سريع اختياري | إيصال «سُجّل مصروف» + «افتح السجل» → `/finance?event={id}` | `VERIFIED` | `components/layout/QuickExpenseForm.tsx:118-204` |
| طلب | طلب من عميل | «ابدأ مسودة طلب واتفاق أولي.» | تنقّل (بلا إنشاء مسودة — تُنشأ عند أول إدخال حقيقي) | `/orders/draft/new?intent=customer_order` | `VERIFIED` | `app/MicroAppShell.tsx:76-79` |
| تقدير | مسودة تصميم | «ابدأ مسودة تصميم قبل أن تتحول إلى اتفاق.» | تنقّل | `/orders/draft/new?intent=planned_design` | `VERIFIED` | `app/MicroAppShell.tsx:80-83` |
| تحصيل | عربون أو تحصيل | «ورقة تحصيل: مين عليه إلك وكم قبضت — بالوجهة التي تختارها.» | تنقّل مع حفظ مصدر الرجوع | `/collect?from={السطح الحالي}` | `VERIFIED` | `app/MicroAppShell.tsx:84-88` |

**قواعد ظهور الكروم العام:** التصنيف في `app/routeClassifier.ts` — `/setup` نوع `setup` (بلا كروم)؛ **29 نمط محرر عميق** من نوع `deep` تخفي الشريط (كل المحررات المالية والطلبية والمخزنية والأصول والقروض والحاسبة والتقدير والتسليم والتحصيل والمشاركة)؛ وكل ما عداها «أسطح قراءة» يبقى فيها الشريط (بما فيها تفاصيل الطلب ودفتر المحفظة و`/tools/integrity` و`/finance/statement` و`/finance/activity`). اختبار مزامنة `app/routeKnowledgeSync.test.ts` يفرض تطابق الجداول الأربعة — `VERIFIED`.

**الرجوع والروابط العميقة:** `withFrom()` يضيف `from` للمسارات الداخلية الآمنة فقط؛ `resolveReturnPath` يعتمد `from` الصالح غير-الذاتي وإلا الوجهة القانونية لكل بادئة (حماية من الحلقات). القيم `focus` المعلنة في العقد: `guided-import` و`capacity` و`recurrence` مستهلكة فعلًا؛ أما **`export` و`today` و`priority` فمعلنة ولا يستهلكها أي سطح** (روابط صامتة خاملة) — `VERIFIED` (`app/navigationContract.ts:40-47,117-197`؛ استهلاك فعلي: `pages/Settings.tsx:160-169`، `pages/Schedule.tsx:93`). المسار القديم `/review` يحوّل إلى `/finance` بلا 404 — `VERIFIED` (`app/MicroRouter.tsx:157-160`).

**ملاحظة مقعد خامس:** تعليقات متقادمة داخل `components/layout/BottomNav.tsx:2-3` و`components/layout/AppHeader.tsx:39` ما زالت تقول «المقعد الخامس شاغر معلن للسوق» بينما الشريط الفعلي يعرض «أدواتي» في الموضع الرابع — تعارض داخلي موثق في القسم 12.

---

## Route and screen inventory

جرد كامل من `app/MicroRouter.tsx` (56 عنصر `<Route>`). «القسم الحالي» = البيت التنقلي الذي يُفتح منه السطح عادةً. «يكتب» = مخازن IndexedDB أو أذونات تُنشأ فعليًا.

| الشاشة/السطح | المسار | القسم الحالي | نقطة الدخول | يقرأ | يكتب | الحالة | الدليل |
|---|---|---|---|---|---|---|---|
| Setup (التأسيس) | `/setup` | التأسيس | بوابة الإقلاع (لا ملف → تحويل إجباري) | مسودة إعداد سابقة (`form-drafts`) | `activity-profile` + اختياريًا `cash-wallets` و`cash-continuity-entries` | منفذ | `pages/Setup.tsx:72-424` |
| Foundation (صفحة الأساس) | `/foundation` | التأسيس/مشروعي الآن | نهاية Setup؛ رابط دائم من وحدة «مالي» في Home (القرار ٧) | محافظ، أحداث، مشتريات، مواد | لا شيء مباشرة (بوابات لمحررات أخرى) | منفذ | `pages/Foundation.tsx:27-247` |
| Home | `/` | مشروعي الآن | مقعد 1 | نموذج مركز التحكم (طلبات/أحداث/مبيعات/مواعيد/تفضيلات) | لا شيء | منفذ | `pages/Home.tsx:135-489` |
| Orders (العمل) | `/orders` | العمل | مقعد 2 | طلبات، مسودات، مبيعات مباشرة، مواعيد | لا شيء | منفذ | `pages/Orders.tsx:112-349` |
| NewDraft (محول نية) | `/orders/new` | العمل | توافق قديم | — | — | محوّل فقط → `/orders/draft/new?intent=customer_order\|planned_design` | `pages/NewDraft.tsx:14-17` |
| DraftEditor (محرر المسودة) | `/orders/draft/:id` (`id="new"` يغطي الإنشاء) | العمل/عمق | FAB «طلب من عميل»/«مسودة تصميم»؛ من Home والطلبات | مسودة، كتالوج، تقدير مصدر | `order-drafts` (تُنشأ عند أول إدخال) | منفذ | `pages/DraftEditor.tsx:195-286` |
| CostEditor (احسب التكلفة) | `/orders/draft/:id/cost` | عمق-عمل | زر «احسب التكلفة» في المحرر | مسودة، مواد، مشتريات (مقترحات) | نسخ CostSnapshot على المسودة | منفذ | `pages/CostEditor.tsx:288-317,618-650` |
| AgreementEditor (تسجيل الاتفاق) | `/orders/draft/:id/agreement` | عمق-عمل | زر «تسجيل الاتفاق» (بعد نسخة تكلفة صالحة) | مسودة، محافظ، دفتر الناس (مقترحات أسماء) | `craft-orders` + `schedule-entries` + `order-drafts` (ربط) + اختياريًا `cash-continuity-entries` (تخصيص عربون) | منفذ | `pages/AgreementEditor.tsx:217-231`، `application/agreements/agreementService.ts:115-190` |
| OrderDetail | `/orders/:id` | العمل/قارئ | صفوف الطلبات؛ روابط من Home/Collect/Parties | طلب كامل + خدمات | عبر لوحاته (قبض/إلغاء/عربون/وقت فعلي) | منفذ | `pages/OrderDetail.tsx` |
| DeliveryReview (مراجعة التسليم) | `/orders/:id/deliver` | عمق-عمل | **حصرًا** زر «راجع التسليم وسجّله» من OrderDetail في حالة `ready` | طلب، مواد، حركات | ذرّية: `craft-orders` + `inventory-movements` + `inventory-shortages` + اختياري `cash-continuity-entries` | منفذ | `pages/DeliveryReview.tsx:202-485`، `application/fulfillment/deliveryReviewService.ts:322-563` |
| DirectSaleEditor | `/direct-sales/new` و`/direct-sales/:id` | عمق-عمل | «تسجيل بيع مباشر» (العمل/Home)؛ FAB (نموذج الورقة)؛ صف كتالوج `?product=` | كتالوج، محافظ | `direct-sales` + اختياري `cash-continuity-entries` (تخصيص) | منفذ | `pages/DirectSaleEditor.tsx:628-970` |
| Schedule (المواعيد) | `/schedule` | العمل/قارئ | مقطع دائم في العمل؛ وحدة Home الشرطية | مواعيد، طلبات، سعة | لا شيء | منفذ | `pages/Schedule.tsx:202-330` |
| ScheduleEditor | `/schedule/:id` | عمق-مواعيد | صفوف المواعيد | موعد، طلب مرتبط | `schedule-entries` (تأجيل بسبب إلزامي) | منفذ | `pages/ScheduleEditor.tsx:112-331` |
| Finance (مالي) | `/finance` (`?view=`، `?layer=`، `?event=`) | المالية | مقعد 3؛ `/review` يحوّل إليها | موقف مالي، أحداث، G5، مالك، نبضة، عربونات، تصحيحات، هدر، أصول، قروض | لا شيء في الصفحة؛ طبقة الأحداث تكتب (عكس/تعديل/حذف/استرجاع) | منفذ | `pages/Finance.tsx:158-176,292-758` |
| FinancialEventEditor | `/finance/new/:type` (8 أنواع عامة) | عمق-مالي | طبقة أفعال مالي؛ Home؛ Foundation؛ دفتر المالك | محافظ، التزامات قائمة، أمانات | `financial-events` (+`cash-continuity-entries` لتغطية مصروف من محفظة) | منفذ | `pages/FinancialEventEditor.tsx:40-53,548-601` |
| OwnerWithdrawalEditor | `/finance/withdraw` | عمق-مالي | **حصرًا** زر «اسحب لنفسك» من دفتر المالك | نظرة مال المالك | `owner-movements` أو `financial-events` (`owner_withdrawal_cash`) | منفذ | `pages/OwnerWithdrawalEditor.tsx:24-28,93-113` |
| OwnerEntitlement (دفتر المالك) | `/finance/owner-entitlement` | عمق-مالي | بطاقات مالي؛ بطاقة Home «مال المالك المسجل» | سياسات/سجلات/افتتاحيات/حركات | السياسات الأربع + السجلات + الحركات + عكسها | منفذ | `pages/OwnerEntitlement.tsx:112-141,590-720` |
| G5DeclarationEditor (متوقع قريب) | `/finance/g5/declaration` | عمق-مالي | «أعلن تحصيلًا أو التزامًا قريبًا» في مالي | خيارات ربط | `short-cash-declarations` | منفذ | `pages/G5DeclarationEditor.tsx:85-117` |
| Statement (كشف الفترة) | `/finance/statement` | المالية/قارئ | رابطان من مالي | كشف + Markdown | تنزيل ملف فقط | منفذ | `pages/Statement.tsx:167-248` |
| FinanceActivity (القارئ الكامل) | `/finance/activity` | المالية/قارئ | «افتح السجل الكامل» (Home/مالي) | قارئ نشاط موحد | لا شيء | منفذ | `pages/FinanceActivity.tsx:163-189` |
| CashWallets (محافظ الكاش) | `/cash` | المالية/قارئ | طبقة أفعال مالي | محافظ + مدخلات + موقف | لا شيء (بوابة) | منفذ | `pages/CashWallets.tsx:52-70` |
| CashWalletEditor | `/cash/wallet/new` | عمق-مالي | محافظ الكاش؛ طريق Home «سجّله»؛ صفحة الأساس | — | `cash-wallets` + `cash-continuity-entries` (افتتاحي) | منفذ | `pages/CashWalletEditor.tsx` |
| CashOpeningLaterEditor | `/cash/wallet/:id/opening-later` | عمق-مالي | محافظ ذات افتتاحي مجهول | محفظة + مدخلات | `cash-continuity-entries` (افتتاحي موثق لاحقًا) | منفذ | `pages/CashOpeningLaterEditor.tsx:75` |
| WalletLedger (دفتر المحفظة) | `/cash/wallet/:id` | المالية/قارئ | «السجل» لكل محفظة | قارئ دفتر | لا شيء (يشير للعكس) | منفذ | `pages/WalletLedger.tsx:45-56` |
| CashTransferEditor | `/cash/transfer` | عمق-مالي | محافظ (يتطلب ≥2) | نظرة المحافظ | `cash-continuity-entries` (زوج `transfer_out`/`transfer_in`) | منفذ | `application/cash/cashContinuityService.ts:240-288` |
| CashAdjustmentEditor | `/cash/wallet/:id/adjust` | عمق-مالي | «ضبط بسبب» | محفظة | `cash-continuity-entries` (`cash_adjustment` بسبب إلزامي) | منفذ | `cashContinuityService.ts:207-238` |
| CashCount (عدّ الصندوق) | `/cash/count` | عمق-مالي | محافظ؛ طريق مالي | نظرة المحافظ | `cash_adjustment` (فرق العدّ) | منفذ | `pages/CashCount.tsx:86-119` |
| CashDistribution (وزّع غير الموزع) | `/cash/distribute` (`?mode=cover&to=`) | عمق-مالي | شريط مالي؛ تنبيه التغطية؛ محافظ | محافظ + موقف | `cash-continuity-entries` (`allocation`) | منفذ | `pages/CashDistribution.tsx:104-135` |
| CashReversalEditor | `/cash/entry/:id/reverse` | عمق-مالي | «تراجع» من دفتر المحفظة/المدخلات | مدخل | `reversal` (أحادية الاتجاه) | منفذ | `cashContinuityService.ts:290-346` |
| Collect (ورقة التحصيل) | `/collect` (`?source=order:\|sale:`) | عمق-مالي | FAB؛ صفوف ديون Home؛ زرا OrderDetail؛ صفوف Parties | مصادر قابلة للتحصيل + محافظ | على السجل المصدر (طلب/بيع) + اختياري `allocation` | منفذ | `pages/Collect.tsx`، `application/collections/collectionService.ts:69-125` |
| Suppliers (الموردون والمشتريات) | `/suppliers` | المالية/قارئ | طريق وأفعال مالي | مشتريات + ملخص | لا شيء | منفذ | `pages/Suppliers.tsx:27-38` |
| SupplierPurchaseEditor | `/suppliers/purchase/:id` و`/suppliers/purchase/:id/payment` (`new` = إنشاء) | عمق-مالي | أزرار الموردين | مشتريات، مواد (ربط استلام) | `supplier-purchases` (شراء/دفعة/تعديل موثق/عكس دفعة) | منفذ | `pages/SupplierPurchaseEditor.tsx:40-41,240-351` |
| InventoryMaterials (المواد والمخزون) | `/inventory` | المالية/قارئ | طبقة أفعال مالي؛ وحدة Home الشرطية | مواد + حركات + تفعيلات + نقص | لا شيء (بوابة) | منفذ | `pages/InventoryMaterials.tsx` |
| MaterialEditor | `/inventory/material/new` و`/inventory/material/:id/confirm` | عمق-مخزون | «مادة جديدة»؛ «تأكيد رصيد» | مواد | `materials` + `inventory-movements` (افتتاحي/تأكيد) | منفذ | `pages/MaterialEditor.tsx:241-467` |
| InventoryMovementEditor | `/inventory/movement/:type` (receipt/consume/waste/adjust) | عمق-مخزون | أزرار المخزون؛ `?order=`/`?sale=`/`?purchase=` عميقة | مواد، طلبات، مبيعات، مشتريات | `inventory-movements` (+`inventory-shortages`) وحدث `loss_non_cash` للهدر المؤثر | منفذ | `pages/InventoryMovementEditor.tsx:601-777` |
| InventoryReversalEditor | `/inventory/movement/:id/reverse` | عمق-مخزون | «تراجع» بكل صف حركة | حركة | حركة عكسية مرآة (+عكس حدث الخسارة للهدر) | منفذ | `pages/InventoryReversalEditor.tsx:42-62` |
| Catalog (منتجاتي وخدماتي) | `/catalog` | مشروعي الآن (وحدة دائمة) + أدواتي (صف حالة) | وحدة Home «منتجاتي وخدماتي»؛ صف أدواتي؛ العمل؛ محرر المسودة | فهرس + وحدات + قوالب + سياسات + قراءات | `catalog-items`/`measurement-units`/`direct-conversions`/`catalog-templates`/`allocation-policies` | منفذ | `pages/Catalog.tsx:771-966` |
| Tools (أدواتي) | `/tools` | أدواتي | مقعد 4 | تقديرات، حالة وحدات | لا شيء (بوابة) | منفذ | `pages/Tools.tsx:170-234` |
| CostCalculator (حاسبة التكلفة والسعر) | `/tools/calculator` | عمق-أدوات | بطاقة أدواتي؛ `?estimate=` للتعديل | مواد (مقترحات قراءة فقط) | `cost-estimates` فقط | منفذ | `pages/CostCalculator.tsx:215-605` |
| EstimateDetail | `/tools/estimate/:id` | عمق-أدوات | صفوف تقديراتي | تقدير واحد | حذف فقط (`cost-estimates`) | منفذ | `pages/EstimateDetail.tsx:47-263` |
| ToolsIntegrity (فحص سلامة مالي) | `/tools/integrity` | أدواتي/قارئ | صف أدواتي؛ طريق مالي؛ خطوة ما بعد الاستيراد | 16 قارئ مالي/تشغيلي | **لا شيء — قراءة صرفة** | منفذ | `pages/ToolsIntegrity.tsx:63-111` |
| Assets (الأصول) | `/assets` | المالية/قارئ | طبقة «الأصول» في مالي | نظرة أصول | لا شيء | منفذ | `pages/Assets.tsx:29-39` |
| AssetEditor | `/assets/new` | عمق-مالي | «سجّل أصلًا» | — | `assets` + `financial-events` (`asset_purchase_cash\|payable`) ذرّية | منفذ | `application/assets/assetService.ts:161-199` |
| AssetDetail | `/assets/:id` | المالية/قارئ | صفوف الأصول | أصل + أحداثه | إهلاك/تصحيح استحواذ/تعديل عقد/بيع/شطب/عكس إهلاك | منفذ | `pages/AssetDetail.tsx:175-471` |
| Loans (القروض) | `/loans` | المالية/قارئ | طبقة «القروض» في مالي | نظرة قروض | سداد عبر RepaymentSheet | منفذ | `pages/Loans.tsx:102-112` |
| LoanEditor | `/loans/new` | عمق-مالي | «سجّل قرضًا» (قرض **تعطيه**) | محافظ (وسم) | `loans` + `financial-events` (`loan_outgoing_cash`) | منفذ | `application/loans/loanService.ts:97-103` |
| LoanDetail | `/loans/:id` | المالية/قارئ | صفوف القروض | قرض + أحداثه | عكس سداد/تصحيح | منفذ | `pages/LoanDetail.tsx:84-111` |
| Parties (دفتر الناس) | `/parties` | المالية/قارئ | طريق مالي «افتح دفتر الناس» | طلبات+مبيعات+مشتريات+التزامات | **لا شيء — قراءة مجمعة** | منفذ | `application/parties/partyLedgerService.ts:65-216` |
| SharePreview (معاينة المشاركة) | `/share/preview` | عمق-عمل | **حصرًا** «شارك رسالة مع الزبون» من OrderDetail | حالة history عابرة | لا شيء (نص/نسخ فقط) | منفذ | `pages/SharePreview.tsx:17-107` |
| Settings (الإعدادات) | `/settings` (`?focus=guided-import`) | الإعدادات | ترس الترويسة؛ من Foundation وأدواتي | كل المخازن + تفضيلات + أمان | تصدير/استيراد/ابدأ من جديد + تفضيلات + قفل | منفذ | `pages/Settings.tsx:50-639` |
| Profile (ملف المالك) | `/profile` | مشروعي الآن/الإعدادات | رابط «ملف المالك» في رأس Home؛ صف الإعدادات | مالك + ملف + محافظ + تفضيلات | `owner-profile`/`activity-profile` | منفذ | `pages/Profile.tsx:183-335` |
| تحويل المراجعة القديمة | `/review` | — | رابط خارجي قديم | — | — | تحويل إلى `/finance` | `app/MicroRouter.tsx:157-160` |
| NotFound | (افتراضي) | — | أي مسار غير معروف | — | — | «هذه الصفحة ليست جزءًا من هذا الإصدار» | `pages/NotFound.tsx:9-17` |

**أوراق/حوارات تمثل أفعالًا كبرى (ليست مسارات):** QuickActionSheet (بيع/مصروف داخل الورقة)؛ لوحات عربون OrderDetail (`OrderDepositPanels`: ردّ/احتفاظ/تصنيف)؛ لوحة عكس القبضة المزدوجة (تحصيل + تخصيصه)؛ RepaymentSheet للقروض (مركّبة في `Loans.tsx:103` و`LoanDetail.tsx:307`)؛ ActualTimePanel (وقت فعلي)؛ UnsavedChangesGuard (حوار التغييرات غير المحفوظة)؛ حوار تجاهل ورقة سجّل المتسخة — `VERIFIED`.

---

## Capability inventory

«المالك المرشح» تحليل فقط (الفرضية قيد الاختبار) — لا نقل ولا إعادة تسمية مقترحة هنا. المرشح من: `مشروعي الآن` / `العمل` / `المالية` / `أدواتي` / `السوق` / `Delivery` / `الإعدادات` / `غير واضح`.

| القدرة | نقطة البدء | المالك الحالي في الكود | مصدر الحقيقة | يقرأ | ينشئ/يغيّر | أثر مالي/مخزني/تقريري | قابل للتصحيح؟ | المالك المرشح | الحالة | الدليل |
|---|---|---|---|---|---|---|---|---|---|---|
| دورة الطلب (مسودة→اتفاق→تكلفة→تنفيذ→تسليم→تسوية/دين) | FAB/العمل | `agreements`/`fulfillment`/`drafts` | `craft-orders` + `order-drafts` | كتالوج، مواد | طلبات + مواعيد + حركات استهلاك | إيراد يُعترف به مرة عند التسليم؛ العربون كاش غير موزع | إلغاء موثق + تراجع تسليم + عكس قبضة | `العمل` | `VERIFIED` | `src/domain/craft-order/policies.ts:33-44`، `deliveryReviewService.ts:322-563` |
| البيع المباشر | FAB (ورقة) أو `/direct-sales/new` | `direct-sales` | `direct-sales` | كتالوج (`?product=`) | سجل بيع مستقل | كاش غير موزع + «لي عند العملاء» عند الآجل؛ ربح «غير متاح» بلا تكلفة | تعديل مراجعات + إلغاء يعكس التخصيصات | `العمل` | `VERIFIED` | `src/domain/direct-sale/policies.ts:35-52`، `directSaleService.ts:76-241` |
| التسليم | OrderDetail (`ready`) | `fulfillment/deliveryReview` | `craft-orders` + `inventory-movements` | طلب، مواد، قوالب | استهلاك + نقص + قبض اختياري ذرّي | لا حدث مالي؛ يُعترف بالإيراد هنا | «تراجع موثق عن التسليم» | `العمل` | `VERIFIED` | `pages/DeliveryReview.tsx`، `G3Delivery.dom.test.tsx:162-219` |
| التحصيل والذمم | `/collect` | `collections` | السجلات المصدر (طلب/بيع) | مصادر قابلة للتحصيل | قبض على المصدر + تخصيص اختياري | لا إيراد («التحصيل ليس إيرادًا») | عكس قبضة (من الطلب، مزدوج مع تخصيصه) | `المالية` (ورقة يفتحها FAB) | `VERIFIED` | `collectionService.ts:69-241` |
| المصروف | ورقة FAB أو `/finance/new/operating_expense_*` | `finance/projectFinancialService` | `financial-events` | محافظ، التزامات | حدث مصروف نقدي/ذمة | كاش− أو ذمة+؛ تصنيف اختياري بلا أثر رقمي | عكس/تعديل/حذف/استرجاع | `المالية` | `VERIFIED` | `QuickExpenseForm.tsx`، `FinancialEventEditor.tsx:548-601` |
| محافظ الكاش والتخصيص | `/cash` وشجنتها | `cash/cashContinuityService` | `cash-wallets` + `cash-continuity-entries` | — | افتتاحي/تحويل/ضبط/عكس/عدّ/تخصيص | التخصيص لا يغير الإجمالي | عكس موثق أحادي | `المالية` | `VERIFIED` | `cashContinuityService.ts:84-346` |
| مال المالك (رأس مال/حق/سحب) | `/finance/owner-entitlement` | `finance` + `owner-entitlement` | `owner-*` + أحداث | نظرة موحدة | سياسات/سجلات/افتتاحيات/حركات | منفصل عن الربح صراحةً | عكس موثق | `المالية` | `VERIFIED` | `pages/OwnerEntitlement.tsx:606-699` |
| الموردون والمشتريات | `/suppliers` | `suppliers/supplierPurchaseService` | `supplier-purchases` | مواد (جسر استلام) | شراء/دفعة/تعديل/عكس | الكاش عبر paidMinor في الصيغة؛ لا COGS تلقائي | تعديل موثق + عكس دفعة | `المالية` | `VERIFIED` | `supplierPurchaseService.ts:89-187` |
| المخزون والهدر | `/inventory` | `inventory/inventoryMaterialService` | `materials` + `inventory-movements` | مشتريات | افتتاحي/استلام/استهلاك/هدر/ضبط/نقص | قيمة الهدر المؤثر → `loss_non_cash` ذرّي | عكس حركة مرآة | `المالية` (بيت) مع جسر عمل | `VERIFIED` | `inventoryMaterialService.ts:502-1316` |
| الكتالوج ومراجع العمل | وحدة Home الدائمة + `/catalog` | `catalog/catalogService` | `catalog-items` + وحدات + قوالب | مواد | مراجع واقتراحات P-002 | لا شيء عند الكتابة؛ الاقتراحات لا تصير قيمًا مسجلة | إيقاف يبقي التاريخ | `مشروعي الآن` | `VERIFIED` | `catalogService.ts:117-429`، `P-002` |
| الحاسبة والتقديرات | `/tools/calculator` | `estimates/costEstimateService` | `cost-estimates` | مواد (مقترحات) | تقديرات فقط | **لا شيء** (اختبارات تؤكد) | حذف حر | `أدواتي` | `VERIFIED` | `costEstimateService.ts:2-161`، `U004.dom.test.tsx` |
| جسر التقدير→مسودة | زر معلن في أدواتي/التقدير/الحاسبة | `drafts` | `order-drafts` (`sourceEstimateId`) | تقدير | مسودة `planned_design` بقيم مقترحة | **لا شيء** (0 أحداث/0 كاش مؤكد بالاختبار) | المسودة قابلة للحذف بحرية | زر في `أدواتي` ينتج مسودة `العمل` | `VERIFIED` | `DraftEditor.tsx:64-90` |
| فحص سلامة مالي | `/tools/integrity` | `finance/integrityCheckService` | قراءة فقط | 16 قارئًا | **لا شيء** | تقرير في الذاكرة | إعادة تشغيل = قراءة جديدة | `أدواتي` | `VERIFIED` | `ToolsIntegrity.ui.test.tsx:49-74` |
| سياسات التوزيع وقراءة الهامش | داخل `/catalog` | `recurring-work/recurringWorkService` | `allocation-policies` | طلبات/حركات/وقت فعلي | سياسات «قراءة تفسيرية مؤرخة» | **لا أثر مالي عند الكتابة** | إيقاف F-082 + خليفة موثق | `المالية` (تكشف حاليًا داخل الكتالوج) | `VERIFIED` | `recurringWorkService.ts:152-498` |
| المواعيد والسعة | `/schedule` | `scheduling/scheduleService` | `schedule-entries` + `schedule-recurrences` | طلبات | مواعيد التسليم تُنشأ مع كل اتفاق ذرّيًا | لا شيء ماليًا | تأجيل بسبب إلزامي | `العمل` | `VERIFIED` | `scheduleService.ts:312-518` |
| دفتر الناس | `/parties` | `parties/partyLedgerService` | تجميع حي بالاسم | طلبات/مبيعات/مشتريات/التزامات | **لا شيء** | قراءة فقط | — | `المالية` | `VERIFIED` | `partyLedgerService.ts:65-216` |
| المتوقعات G5 | `/finance/g5/declaration` | `g5/g5Service` | `short-cash-declarations` | خيارات ربط | توقعات | **لا حركة كاش** | عكس موثق | `المالية` | `VERIFIED` | `g5Service.ts:305-429` |
| كشف الفترة والقراءات | `/finance/statement` | `finance/statementService` | قراءة مشتقة | أحداث/طلبات/مبيعات | تنزيل ملف | قراءة فقط | — | `المالية` | `VERIFIED` | `statementService.ts` |
| الأصول | `/assets` | `assets/assetService` | `assets` + أحداث | — | استحواذ/إهلاك/بيع/شطب | كاش عند الشراء النقدي وعائد البيع؛ ليس مصروفًا | تصحيح استحواذ + عكس إهلاك | `المالية` | `VERIFIED` | `assetService.ts:161-466` |
| القروض (تعطيها) | `/loans` | `loans/loanService` | `loans` + أحداث | محافظ (وسم) | إقراض/سداد | كاش− عند الإقراض، كاش+ عند السداد | عكس سداد + تصحيح | `المالية` | `VERIFIED` | `loanService.ts:97-235` |
| المشاركة اليدوية | `/share/preview` | `share/shareMessageService` | حالة history عابرة | طلب | **لا شيء** | نص فقط بلا أرقام خاصة | — | `العمل` | `VERIFIED` | `SharePreview.tsx:17-107` |
| الوقت الفعلي | ActualTimePanel في OrderDetail | `time/actualTimeService` | `actual-time-records` | طلب | سجلات وقت | لا شيء مباشر (يغذي القراءات) | عكس موثق | `العمل` | `VERIFIED` | `actualTimeService.ts:101-184` |
| القفل المحلي والتصدير/الاستيراد/البدء من جديد | `/settings` | `security` + `transfers` | `local-security` + ملف snapshot | كل المخازن | استبدال كامل عند الاستيراد | حماية بيانات لا أثر مالي | النسخة الاحتياطية إلزامية قبل البدء من جديد | `الإعدادات` | `VERIFIED` | `pages/Settings.tsx:309-451` |
| ملف المالك والمشروع | رأس Home + الإعدادات | `identity`/`profileService` | `owner-profile` + `activity-profile` | محافظ/تفضيلات | هوية واسم | لا شيء | قابل للتعديل | `مشروعي الآن` | `VERIFIED` | `Profile.tsx:183-335` |

---

## Setup and Settings impact matrix

### مصفوفة الإعدادات وأسئلة التأسيس

| الإعداد/السؤال | الخيارات الحالية | موقع التخزين | الأثر الموثق | يظهر/يخفي قدرة؟ | قابل للتعديل لاحقًا؟ | أثره على البيانات القائمة | الحالة | الدليل |
|---|---|---|---|---|---|---|---|---|
| اسم المشروع (Setup خطوة 1) | نص حر | `activity-profile` (`local-profile`) | إلزامي وحده؛ يفعّل الدخول للأساس | لا | نعم (من الملف) | لا | `VERIFIED` | `pages/Setup.tsx:72-184` |
| محفظة نقد افتراضية (خطوة 2) | اسم («الدرج» افتراضيًا) أو تخطٍّ | `cash-wallets` + `cash-continuity-entries` | إنشاء محفظة درج | لا | نعم (إضافة محافظ من مالي) | لا | `VERIFIED` | `Setup.tsx:317-336` |
| الموقف الافتتاحي (خطوة 3) | «أعرف الرقم» / «ما بعرف الآن» / «بدأت من الصفر» | `opening_balance` فقط عند معرفة >0 | مجهول لا يُحفظ صفرًا أبدًا؛ طريق لاحق موثق | لا | نعم (`opening-later`) | لا | `VERIFIED` | `Setup.tsx:147-184` |
| مسودة الإعداد | حفظ تلقائي + عرض استرجاع صريح | `form-drafts` (`setup:new`) | استعادة واعية أو بدء جديد | لا | — | تُهمل بعد الإتمام | `VERIFIED` | `Setup.ui.test.tsx:109-269` |
| كتل صفحة الأساس | كاش/رأس مالك/ديون/مواد/ملف جاهز | عبر المحررات العميقة | «ما تخطّاه يظهر طريقًا لا صفرًا» | لا | دائم الوصول (القرار ٧) | لا | `VERIFIED` | `pages/Foundation.tsx:27-247` |
| قفل التطبيق المحلي | تفعيل برمز 4-8 أرقام + خمول (يدوي/1/5/10/30 د) | `local-security` (خارج snapshot التصدير) | غطاء AppLockGate + بوابة PIN للتصدير/الاستيراد/البدء من جديد | **نعم** — يحجب الاستيراد/التصدير/التصفير حتى التفعيل | نعم (تعطيله يحتاج الرمز؛ لا استرداد بلا رمز) | لا أثر على بيانات الأعمال؛ يبقى بعد «ابدأ من جديد» | `VERIFIED` | `pages/Settings.tsx`، `localLockService.ts:101-107` |
| تقرير التشخيص المحلي | نسخ فقط | `localStorage: micro.diagnostics.v1` (≤25 مدخلًا/48KB) | لا شيء (حلقة أحداث) | لا | — | لا | `VERIFIED` | `localDiagnosticsService.ts:44` |
| «دقة المال: قرشان للدينار» | إعلان عرض فقط | لا شيء | لا شيء موثق سوى العرض | لا | لا | لا | `VERIFIED` (عرض فقط) | `pages/Settings.tsx` (P-001) |
| تذكير النسخة الاحتياطية | إطفاء/تفعيل | `local-preferences.backupReminderEnabled` | يتحكم بسطر الحقيقة في Home فقط | لا | نعم | لا | `VERIFIED` | `Settings.tsx` (O-001) |
| سطر الثبات (Persistence) | عرض حالة المتصفح | لا شيء (قراءة حية) | إعلام فقط | لا | لا (تحكم المتصفح) | لا | `VERIFIED` | `Settings.tsx` (P-01) |
| تصدير محلي مُتحقق | زر تصدير | ملف `micro-local-YYYY-MM-DD.json` + `lastVerifiedExportAt` | نسخة تحقق ذهابًا وإيابًا | لا | قابل للتكرار | لا (قراءة فقط) | `VERIFIED` | `localTransferService.ts` |
| استيراد محلي | ملف JSON + معاينة + بوابة حماية | استبدال snapshot كامل | يستبدل كل مخازن الأعمال؛ يحفظ `form-drafts` و`local-security` | لا | قابل للتكرار | **استبدال كامل** | `VERIFIED` | `Settings.tsx:383-451` |
| إدخال موقف افتتاحي (موجّه) | ملف بداية | استبدال snapshot (فقط فوق لقطة فارغة) | تأسيس دفعة واحدة (كاش+مواد)؛ idempotent | لا | أحادي التصميم | استبدال عند التأكيد | `VERIFIED` | `SettingsGuidedOpeningSection.tsx` |
| ابدأ من جديد | تصدير إجباري → كتابة العبارة → PIN | تفريغ كل المخازن | تصفير كامل مع نسخة احتياطية مُتحققة إلزامية؛ القفل يبقى | لا | نهائي | **مسح كل شيء عدا القفل والمسودات** | `VERIFIED` | `localTransferService.ts:226-274` |
| طريقة العمل المعتادة | لم أحدد/المادة أولًا/الوقت أولًا/معًا + تتبع وقت | `local-preferences` | «ترتيب عرض الأدوات» فقط — لا يغير سجلًا ولا رقمًا | لا | نعم | لا | `VERIFIED` | `preferenceService.ts` |
| المظهر | فاتح/داكن | `local-preferences.theme` | فاتح افتراضي؛ لا يتبع النظام | لا | نعم | لا | `VERIFIED` | `ThemeContext.tsx:20-25` |

### القوائم الأربعة المطلوبة

1. **إعدادات بأثر موثق:** قفل PIN (بوابة التصدير/الاستيراد/التصفير + غطاء الخمول)؛ استيراد/تصدير (استبدال/ملف)؛ ابدأ من جديد؛ تذكير النسخة (سطر حقيقة Home)؛ المظهر؛ طريقة العمل (ترتيب أدوات المحرر)؛ تفعيل تتبع الوقت (يظهر ActualTimePanel).
2. **إعدادات تُجمع بلا أثر موثق:** «دقة المال: قرشان للدينار» (عرض فقط)؛ سطر الثبات (قراءة متصفح) — كلاهما إعلاني بلا أثر تنفيذي.
3. **قدرات تعمل بلا إعداد واضح:** تفعيل المخزون (يتم من داخل `/inventory` بقرار مؤرخ لا من Setup)؛ الكتالوج (سطح دائم بلا تفعيل)؛ المواعيد (تنشأ تلقائيًا مع كل اتفاق)؛ سياسات التوزيع (تُنشأ داخل الكتالوج بلا مكان إعدادات)؛ أمانات/أصول/قروض (مداخل من مالي فقط).
4. **تغييرات تحتاج قرار مالك:** موضع «السوق» عند بنائه (تعارض التوثيق — القسم 12)؛ هل يبقى «أدواتي» مقعدًا رابعًا دائمًا أم مؤقتًا؛ توحيد مصادر كتابة المصروف/الافتتاحي/السحب (قسم 12)؛ تصرف الافتراض «أول سجل» في محرر الحركات؛ مصير مسودات المشاركة غير المستخدمة.

---

## Entry and return flows

لا يوجد Auth إطلاقًا (لا دخول/خروج/سحابة)؛ «القفل» حماية جهاز محلية اختيارية فقط — `VERIFIED`.

| السيناريو | البداية الفعلية | الخطوات الفعلية | البيانات المحفوظة | غير المحفوظ | Auth؟ | رجوع/استعادة آمن؟ | الحالة | الدليل |
|---|---|---|---|---|---|---|---|---|
| أول فتح إطلاقًا | Splash ثم بوابة الإقلاع «جارٍ فتح مشروعك المحلي…» | لا ملف → تحويل استبدالي إلى `/setup` | لا شيء بعد | كل شيء | لا | نعم (توجيه أمامي فقط) | `VERIFIED` | `app/StartupGate.tsx:60-67` |
| إتمام Setup | `/setup` | اسم (إلزامي) → محفظة (اختياري) → موقف افتتاحي (اختياري) → «احفظ وافتح صفحة الأساس» | `activity-profile` + اختياريًا محفظة وافتتاحي؛ تُهمل المسودة | لا أثر مالي | لا | نعم → `/foundation` ثم `/` | `VERIFIED` | `Setup.tsx:147-184` |
| تخطٍّ/Setup جزئي | رابط التخطي في الخطوة 2 أو زرا الخروج في الأساس | يحفظ الاسم فقط وينتقل إلى Home؛ المتروك يظهر «طريقًا» لا صفرًا | `activity-profile` فقط | لا محفظة/رأس مال | لا | نعم | `VERIFIED` | `Setup.tsx:317-336`، `Foundation.tsx:234-244` |
| مقاطعة أثناء الكتابة | أي خطوة/محرر | حفظ تلقائي لمسودة النموذج + عرض استرجاع صريح عند العودة | `form-drafts` | لا أثر مالي قط | لا | نعم (استعادة واعية أو تجاهل) | `VERIFIED` | `Setup.tsx:83-145`، `UnsavedChangesGuard.tsx:36-192` |
| العودة اليومية | Splash (مرة لكل تحميل) → جاهز → Home | قراءة نموذج مركز التحكم | كل IndexedDB | — | لا | نعم | `VERIFIED` | `StartupGate.tsx:70-71` |
| عودة بعد ≥7 أيام | Home + بطاقة «أثناء غيابك» | ملخص آخر يوم تسجيل + ديون فات موعدها + عمر النسخة | قراءة فقط | — | لا | نعم | `VERIFIED` | `homeControlCenterService.ts:412-489` |
| فتح بلا اتصال (PWA) | Service Worker في إنتاج آمن | «أنت غير متصل الآن»؛ التطبيق يعمل من المحلي | `local-preferences` (إخفاء لافتة التثبيت 30 يومًا) | إشعارات الجلسة | لا | نعم — التحديث محجوب فوق نماذج متسخة | `VERIFIED` | `pwa/register.ts:52-118` |
| تغيير الإعدادات لاحقًا | ترس الترويسة من أي مسار | المظهر/طريقة العمل/القفل/التذكير كلها قابلة للتعديل | حسب الجدول أعلاه | — | PIN للأفعال المدمرة | نعم (زر رجوع يحترم `from`) | `VERIFIED` | `Settings.tsx:50-66` |
| استيراد/استعادة | `/settings` → «استيراد» | معاينة («لم نغير بياناتك بعد») → بوابة PIN → استبدال ذرّي + فحص سلامة | كل مخازن الـsnapshot من الملف | `form-drafts` و`local-security` لا يُمسان | بوابة PIN | نعم (لا ملف في الملف → `/setup`) | `VERIFIED` | `Settings.tsx:383-451` |
| البدء من جديد | `/settings` → «ابدأ من جديد» | PIN → تصدير مُتحقق إجباري (فشله يوقف كل شيء) → كتابة العبارة حرفيًا → PIN → تفريغ | ملف النسخة فقط | كل شيء آخر (القفل يبقى) | بوابة PIN ×2 | نعم بالتصميم | `VERIFIED` | `localTransferService.ts:226-274` |
| مغادرة محرر متسخ (تنقل داخلي) | أي محرر عميق | حوار «تعديلات غير محفوظة»: «ابقَ في الصفحة» (افتراضي) / «احفظ واستمر» / «اخخر دون حفظ» | نتيجة الحفظ عند اختياره | المدخل المتروك | لا | نعم (الأقل تدميرًا افتراضيًا) | `VERIFIED` | `UnsavedChangesGuard.tsx:211-302` |
| مغادرة محرر متسخ (رجوع المتصفح/إغلاق تبويب) | sentinel تاريخ + `beforeunload` | نفس الحوار / موجه المتصفح الأصلي | — | المدخل المتروك | لا | نعم | `VERIFIED` | `UnsavedChangesGuard.tsx:62-124` |
| العودة من الشاشات العميقة | محررات وصلت بـ`?from=` | زر الرجوع = `resolveReturnPath` (from صالح غير-ذاتي وإلا الوجهة القانونية) | — | — | لا | نعم (حماية حلقات) | `VERIFIED` | `useReturnNavigation.ts:10-21` |
| رابط `/review` قديم | مسار موجود | تحويل إلى `/finance` (المراجعة صارت نبضة) | — | — | لا | نعم (لا 404) | `VERIFIED` | `MicroRouter.tsx:157-160` |
| فشل التخزين عند الإقلاع | شاشة خطأ مفصلة | «Micro مفتوح في نافذة أخرى» / ترقية فاشلة / نسخة قديمة + «إعادة المحاولة» (reload) | البيانات لا تُمس | — | لا | نعم | `VERIFIED` | `StartupGate.tsx:11-34` |
| انهيار عرض | ErrorBoundary | «تعذر فتح هذا السطح» + معرّف حادثة محلي | مدخل تشخيص | — | لا | نعم | `VERIFIED` | `ErrorBoundary.tsx:54-77` |

---

## Current user journeys

عدد النقرات `NOT_MEASURED` حيث لا يثبته كود/اختبار — لم يُخترع أي عدد.

| الرحلة | البداية | الشاشات/المسارات | النقرات | الحقول الإلزامية | القرارات | الحالة النهائية | التصحيح/العكس | مشكلة مؤكدة | الحالة | الدليل |
|---|---|---|---|---|---|---|---|---|---|---|
| 1. دورة طلب كاملة | FAB «طلب من عميل» | `/orders/draft/new` → `/orders/draft/:id` → `/cost` → `/agreement` → `/orders/:id` (تنفيذ/جاهز) → `/orders/:id/deliver` → `/collect?source=order:` | `NOT_MEASURED` | وصف القطعة + كمية؛ نسخة تكلفة صالحة؛ سعر >0 + موعد تسليم | عربون (0..السعر) ووجهته؛ إقرار تحت سعر الحماية؛ خيارات استهلاك لكل مادة؛ قبض عند التسليم أم دين | settled (أو delivered ثم دين) | تعديل سعر بسبب؛ تراجع قبضة؛ تراجع تسليم؛ إلغاء موثق | أطول مسار سعيد ≥6 شاشات؛ التصحيحات خلف فتحة «تصحيحات موثقة» | `VERIFIED` | `DraftEditor`→`DeliveryReview` كما في القسم 4 |
| 2. بيع مباشر نقدي | FAB «تسجيل بيع» | داخل الورقة → إيصال → (اختياري) `/direct-sales/{id}` | `NOT_MEASURED` | المبلغ فقط | تكلفة معروفة؟ وجهة القبض | بيع فعّال؛ كاش في محفظة/غير موزع؛ ربح أو «غير متاح» | تعديل مراجعات؛ إلغاء يعكس التخصيص | لا | `VERIFIED` | `QuickSaleForm.tsx:160-298` |
| 3. بيع مباشر آجل | FAB أو `/direct-sales/new` | نموذج → لوحة الفرق → «الباقي عليه» → إيصال → لاحقًا `/collect?source=sale:` من Parties | `NOT_MEASURED` | المبلغ + اسم الزبون (لظهور الدين بالدفتر) | «خفّضتُ السعر»/«الباقي عليه»/«يحتاج مراجعة» | partial_debt في «لي عند العملاء» | تعديل البيع؛ تحصيل من الورقة | دين بلا اسم لا يظهر في دفتر الناس (يظهر في صف البيع فقط) | `VERIFIED` | `DirectSaleEditor.tsx:847-904` |
| 4. تسليم طلب جاهز | OrderDetail (`ready`) | `/orders/:id/deliver` → مراجعة (مال/مخزون/خيارات) → «أكّد التسليم» | **نقرة واحدة للتنفيذ** (مثبت بالاختبار) | لا شيء عدا التأكيد (سبب فقط عند تغيير السعر) | فعل كل مادة (4 خيارات)؛ قبض اختياري | delivered (settled تلقائيًا إن سُدد) — استهلاك + نقص ذرّيًا، **بلا حدث مالي** | «تراجع موثق عن التسليم» (يصلح المخزون مرآةً والكاش لا يُمس) | لا — مراجعة قبل الالتزام مفعلة | `VERIFIED` | `G3Delivery.dom.test.tsx:162-219` |
| 5. تحصيل دين | OrderDetail أو Parties أو Home | `/collect?source=order:\|sale:` → مبلغ + وجهة → نتيجة | `NOT_MEASURED` | مبلغ ≤ المستحق + وجهة صريحة | جزئي مسموح | دين ينقص؛ debt→paid عند الصفر | «تراجع عن قبضة» من الطلب (مزدوج مع تخصيصه) | العكس غير معروض من شاشة نتيجة التحصيل — يجب العودة للطلب | `VERIFIED` | `OrderDetail.tsx:1086-1282` |
| 6. تسجيل مصروف | FAB «تسجيل مصروف» | داخل الورقة → إيصال → `/finance?event=` | `NOT_MEASURED` | المبلغ | وجهة الصرف؛ تصنيف سريع | حدث `operating_expense_cash`؛ كاش− (غير موزع) | عكس/تعديل من طبقة الأحداث في مالي | مصدر كتابة ثانٍ كامل للمصروف في `/finance/new/…` (ازدواج مدخل) | `VERIFIED` | `QuickExpenseForm.tsx:61-102` |
| 7. شراء مورد + دفعة | `/suppliers` | `/suppliers/purchase/new` → لاحقًا `/suppliers/purchase/:id/payment` | `NOT_MEASURED` | اسم المورد + الإجمالي | ربط مادة اختياري + كمية متوقعة | `supplier-purchases`؛ الكاش يتأثر بالمدفوع فقط؛ لا COGS | تعديل موثق + عكس دفعة | الشراء لا ينشئ حركة مخزون (جسر استلام يدوي لاحق) | `VERIFIED` | `supplierPurchaseService.ts:89-187` |
| 8. حركة مخزون + هدر | `/inventory` | `/inventory/movement/consume\|waste` → حفظ | `NOT_MEASURED` | مادة + كمية + بيان (وسبب للهدر) | هدف الاستهلاك؛ سياق الهدر (5)؛ «يؤثر على الربح؟» | حركة بقيمتها من الرصيد؛ هدر مؤثر → `loss_non_cash` ذرّي | عكس حركة (يعكس حدث الخسارة معه) | **المحرر يختار أول سجل افتراضيًا** عند غياب المعاملات — خطر إسناد خاطئ | `VERIFIED` | `InventoryMovementEditor.tsx:129-155,601-777` |
| 9. إلغاء طلب بعربون | OrderDetail → «تصحيحات موثقة» | لوحة الإلغاء (سبب اختياري) → لوحة العربون (ردّ/احتفاظ) → تصنيف المحتفظ | `NOT_MEASURED` (≥3 تفاعلات عبر لوحتين) | سبب التسوية عند الردّ/التصنيف | ردّ (كامل/جزئي) أو احتفاظ أو إبقاء «يحتاج مراجعة»؛ تصنيف المحتفظ: مال مالك/إيراد | cancelled + تسوية موثقة | إعادة تصنيف موثقة | قبض غير العربون على طلب ملغى **بلا مسار عكس** (يُحذّر قبل الإلغاء) | `VERIFIED` | `OrderDetail.tsx:868-999`، `OrderDepositPanels.tsx:112-414` |
| 10. مراجعة مالية (كشف/فترة) | مقعد «مالي» | `/finance` → `/finance/statement` (أو نتيجة الفترة/المؤشرات) | `NOT_MEASURED` | لا شيء | اختيار نطاق الشهر | قراءة فقط + تنزيل ملف | — | تعارض تسمية: تبويب «الوضع الآن» لا «كم عندي الآن» الموعودة وثائقيًا | `VERIFIED` | `Finance.tsx:292-314`، `Statement.tsx` |
| 11. مال المالك (سحب) | `/finance` → «مال المالك» | `/finance/owner-entitlement` → «اسحب لنفسك» → `/finance/withdraw` | `NOT_MEASURED` | مبلغ (+سبب ضمني بالمسار) | من أي طبقة (حق/افتتاحي/رأس مال) — **يقرر النظام تقنيًا والمالك لا يرى التفريق** | حركة مالك أو حدث سحب؛ كاش− | عكس موثق من الدفتر | المدخل الوحيد للسحب هو الدفتر (لا دخول مباشر من مالي) | `VERIFIED` | `OwnerWithdrawalEditor.tsx:1-5,69-123` |
| 12. مادة برصيد بداية | `/inventory` → «مادة جديدة» | `/inventory/material/new` → أسئلة موجهة → حفظ | `NOT_MEASURED` | اسم + وحدة (+كمية إن «معلوم») | تتبع كمية أم تكلفة فقط؛ رصيد معلوم/مجهول/صفر مؤكد؛ قيمة معروفة؟ | `materials` + حركة افتتاحية (أو لا شيء عند صفر مؤكد) | «تأكيد رصيد» لاحقًا يسجل الفرق؛ عكس الحركة | صفر مؤكد لا يكتب حركة (حالة معرفة لا صف) — متسق | `VERIFIED` | `MaterialEditor.tsx:341-467` |

---

## Operation-to-effect map

«سجل رسمي» = يكتب في دفتر الأعمال المعتمد (أحداث مالية / سجلات مصدر). «أداة فقط» = بلا أثر مالي/مخزني رسمي.

| العملية | تبدأ من | تقرأ | تكتب | الأسطح المتأثرة | سجل رسمي أم أداة؟ | مصدر الكتابة | التصحيح/العكس | الحالة | الدليل |
|---|---|---|---|---|---|---|---|---|---|
| اتفاق + عربون | `/orders/draft/:id/agreement` | مسودة، تكلفة، محافظ | `craft-orders` + `schedule-entries` + تخصيص اختياري | العمل، Home، مالي (كاش غير موزع) | رسمي (سجل مصدر) | AgreementService واحد | إلغاء موثق + تسويات عربون | `VERIFIED` | `agreementService.ts:115-190` |
| بيع مباشر | ورقة FAB أو `/direct-sales/new` | كتالوج (اختياري) | `direct-sales` + تخصيص اختياري | العمل، مالي، Home، Parties | رسمي (سجل مصدر) | DirectSaleService (+ورقة FAB كتابة موازية) | تعديل مراجعات + إلغاء مرآة | `VERIFIED` | `directSaleService.ts:76-241` |
| تسليم | `/orders/:id/deliver` | طلب، مواد، قوالب | `craft-orders` + `inventory-movements` + `inventory-shortages` + تخصيص اختياري | العمل، المخزون، مالي (إيراد الفترة) | رسمي (لا حدث مالي؛ إيراد مشتق) | DeliveryReviewService ذرّي idempotent | تراجع موثق عن التسليم | `VERIFIED` | `deliveryReviewService.ts:322-657` |
| تحصيل | `/collect` | مصادر مستحقة | على السجل المصدر + تخصيص | مالي، Parties، Home | رسمي (ليس إيرادًا) | CollectionService | عكس قبضة مزدوج من الطلب | `VERIFIED` | `collectionService.ts:145-241` |
| تسجيل دين | OrderDetail بعد التسليم | طلب | حدث `debt_registered` على الطلب | «لي عند العملاء»، Parties | رسمي | fulfillmentService | تحصيل لاحق | `VERIFIED` | `fulfillmentService.ts:320-337` |
| مصروف | ورقة FAB **أو** `/finance/new/operating_expense_*` | محافظ، التزامات | `financial-events` (+تغطية تخصيص) | مالي كامل، Home | رسمي | **مصدران** (QuickExpenseForm + FinancialEventEditor) | عكس/تعديل/حذف/استرجاع | `VERIFIED` | كما في القسم 9 |
| شراء مورد | `/suppliers/purchase/new` | مواد (ربط) | `supplier-purchases` | الموردين، مالي (ذمم/كاش بالمدفوع) | رسمي (دفتر مستقل؛ لا COGS) | SupplierPurchaseService | تعديل موثق | `VERIFIED` | `supplierPurchaseService.ts:89-147` |
| دفعة مورد | `/suppliers/purchase/:id/payment` | شراء | دفعة على الشراء | نفسها + كاش غير موزع | رسمي | نفس الخدمة | عكس دفعة | `VERIFIED` | `supplierPurchaseService.ts:149-187` |
| حركة مخزون (استلام/استهلاك/ضبط) | `/inventory/movement/:type` | مواد، طلبات، مشتريات | `inventory-movements` | المخزون، قراءات الكتالوج | رسمي (قيمة لا كاش) | InventoryMaterialService | عكس مرآة | `VERIFIED` | `inventoryMaterialService.ts:805-875` |
| هدر | `/inventory/movement/waste` | مواد | حركة + `loss_non_cash` عند «يؤثر» | المخزون، نتيجة الفترة | رسمي | نفس الخدمة (ذرّي مع الحركة) | عكس الحركة يعكس الخسارة | `VERIFIED` | `inventoryMaterialService.ts:1275-1316` |
| سحب مالك | `/finance/withdraw` | نظرة المالك | `owner-movements` **أو** `financial-events` | مالي، دفتر المالك | رسمي | **مساران** (حسب وجود سياسة حق) | عكس موثق | `VERIFIED` | `OwnerWithdrawalEditor.tsx:93-113` |
| إدخال رأس مال | `/finance/new/owner_investment_cash` (+مداخل Foundation/Home/الدفتر) | — | `financial-events` | مالي، Home، الدفتر | رسمي | **ثلاثة مسارات** تراكمية (حدث/حركة إرجاع/تصنيف عربون محتفظ) | عكس حدث | `VERIFIED` | `ownerEntitlementPresentation.ts:64-67` |
| شراء أصل | `/assets/new` | — | `assets` + حدث استحواذ ذرّي | مالي (طبقة الأصول)، الموقف | رسمي | AssetService | تصحيح استحواذ (عكس+استبدال) | `VERIFIED` | `assetService.ts:161-290` |
| إقراض/سداد قرض | `/loans/new` + RepaymentSheet | محافظ (وسمًا) | `loans` + أحداث كاش | مالي (طبقة القروض) | رسمي | LoanService + **RepaymentSheet مركّب في سطحين** | عكس سداد/تصحيح | `VERIFIED` | `loanService.ts:97-235` |
| تحويل بين المحافظ | `/cash/transfer` | محافظ | زوج transfer | دفترا المحفظتين | رسمي | CashContinuityService | عكس الزوج | `VERIFIED` | `cashContinuityService.ts:240-288` |
| ضبط/عدّ/تخصيص/عكس كاش | `/cash/...` | محافظ/موقف | `cash_adjustment`/`allocation`/`reversal` | المحافظ، مالي | رسمي | CashContinuityService (+Count يكتب ضبطًا — **مصدران للضبط**) | العكس أحادي الاتجاه | `VERIFIED` | `cashContinuityService.ts:207-346` |
| تصنيف عربون محتفظ | OrderDetail | طلب + أحداث | حدث تصنيف + تحديث الطلب | مالي، كشف الفترة | رسمي | RetainedDepositService (المحرر العام محجوب عائليًا) | إعادة تصنيف موثقة | `VERIFIED` | `retainedDepositService.ts:85-204` |
| توقع G5 | `/finance/g5/declaration` | خيارات ربط | `short-cash-declarations` | «قرار الكاش» | **أداة توقع رسمية بلا حركة كاش** | G5Service | عكس موثق | `VERIFIED` | `g5Service.ts:305-429` |
| حفظ تقدير | `/tools/calculator` | مواد (مقترحات) | `cost-estimates` فقط | أدواتي | **أداة فقط** | CostEstimateService (كاتب وحيد) | حذف حر | `VERIFIED` | `costEstimateService.ts:96-161` |
| حاسبة (معاينة حية) | `/tools/calculator` | — | لا شيء | — | **أداة فقط** | — | — | `VERIFIED` | `costEstimateService.ts:39-79` |
| فحص السلامة | `/tools/integrity` | 16 قارئًا | **لا شيء** | — | **أداة فقط (قراءة صرفة)** | — | إعادة تشغيل | `VERIFIED` | `integrityCheckService.ts` |
| سياسة توزيع | داخل `/catalog` | قراءات | `allocation-policies` | قراءات الكتالوج | **أداة تكوين رسمية بلا أثر مالي فوري** (تشكل قراءات لاحقة) | RecurringWorkService | إيقاف + خليفة | `VERIFIED` | `recurringWorkService.ts:152-272` |
| مشاركة نص | `/share/preview` | حالة عابرة | لا شيء | — | أداة فقط | — | — | `VERIFIED` | `SharePreview.tsx` |

---

## Three-section hypothesis test

الفرضية تحت الاختبار (لا تحت الإقرار): «مشروعي الآن → العمل → المالية» كأقسام، «أدواتي» أدوات مستقلة بلا أثر مالي رسمي تلقائي، «السوق» سوق مستقبلية مستقلة، «Delivery» خدمة تشغيلية علوية مرتبطة بالطلبات.

| القدرة | مالك واحد واضح؟ | المالك الحالي | القسم المرشح | التداخل | خطر التضخيم/التكرار | تصنيف الخلاصة | الدليل |
|---|---|---|---|---|---|---|---|
| دورة الطلب والتسليم | نعم | العمل (`craft-orders`) | `العمل` | لا | لا | `VERIFIED` — ملكية نظيفة | `MicroRouter.tsx`، `craft-order/policies.ts` |
| البيع المباشر | نعم | العمل (`direct-sales`) | `العمل` | مدخلان (ورقة FAB + محرر كامل) بلا تكرار بيانات | منخفض | `VERIFIED` | `directSaleService.ts` |
| التحصيل والذمم | نعم | المالية (`collections`) فوق سجلات العمل | `المالية` | يفتح من FAB ومن العمل ومن Home | منخفض (كتابة واحدة) | `VERIFIED` | `collectionService.ts` |
| المصروف | **لا** — مصدرا كتابة | المالية | `المالية` | ورقة FAB + محرر عميق بصنف كامل | **متوسط** — مساران بخيارات مختلفة | `VERIFIED` (ازدواج موثق) | `QuickExpenseForm` vs `FinancialEventEditor` |
| المحافظ والتخصيص | نعم | المالية (`cash-continuity`) | `المالية` | التخصيص يُستدعى من 5 أسطح (خدمة واحدة) | منخفض | `VERIFIED` | `projectFinancialService.ts:966-1036` |
| مال المالك | نعم | المالية (`owner-entitlement`) | `المالية` | 3 مسارات لزيادة رأس المال | متوسط | `VERIFIED` | `ownerEntitlementPresentation.ts:64-67` |
| الموردون والمشتريات | نعم | المالية (`supplier-purchases`) | `المالية` | لا | لا | `VERIFIED` | `supplierPurchaseService.ts` |
| المخزون والهدر | نعم | المالية بيتًا (`inventory`) | `المالية` | جسور عمل (استهلاك طلب/بيع) | منخفض | `VERIFIED` | `inventoryMaterialService.ts` |
| الكتالوج ومراجع العمل | نعم | مخازن كتالوج؛ مدخل دائم من Home | `مشروعي الآن` | يُفتح كذلك من العمل وأدواتي (حالة الوحدات) | منخفض | `VERIFIED` | `homeControlCenterService.ts:366-371` |
| الحاسبة والتقديرات والفحص | نعم | أدواتي | `أدواتي` | مقترحات مواد تقرأ من المخزون (قراءة فقط) | لا | `VERIFIED` | `costEstimateService`، `integrityCheckService` |
| سياسات التوزيع وقراءة الهامش | **لا** — مالُية المعنى داخل سطح كتالوج | `recurring-work` | `المالية` (مقترح تحليلي) | كتالوج يستضيف قراءة مالية | **متوسط** | `INFERRED` (الموضع الحالي غير مطابق للمعنى) | `Catalog.tsx:406-449` |
| المواعيد | نعم | العمل (`scheduling`) | `العمل` | مقطع دائم داخل العمل + مسار مستقل | منخفض | `VERIFIED` | `Orders.tsx:235-295` |
| التسليم كخدمة عليا | **لا — غير منفذ** | خطوة طلب فقط | `Delivery` مستقبلًا | لا شيء حاليًا | — | `VERIFIED` (كوضع حال) | `MicroRouter.tsx:107`، `expansion/E-00` |
| السوق | **لا — غير منفذ** | لا شيء | `السوق` مستقبلًا | — | — | `VERIFIED` (كوضع حال) | `Tools.tsx:134` |

### خلاصات (خمس كحد أقصى)

1. **ما يصلح مدخلًا/فعلًا في «مشروعي الآن»:** الحقائق الأربع (الكاش/لي عند العملاء/عليّ للموردين/مال المالك) كطرق لا أرقام فقط؛ وحدة «منتجاتي وخدماتي» الدائمة؛ «الأهم الآن» و«اليوم»؛ صفحة الأساس — كلها منفذة فعلًا وممتلكة معنى البيت الأول.
2. **ما تملكه «العمل» بوضوح:** دورة الطلب كاملة (مسودة/اتفاق/تكلفة/تنفيذ/تسليم)، البيع المباشر (مدخلان لنفس القدرة)، المواعيد — تملك نظيفة بلا تداخل كتابة.
3. **ما تملكه «المالية» بوضوح:** كل الكاش والذمم والتزامات الموردين ومال المالك والأصول والقروض والقراءات والتصحيحات — أقوى بيت اكتمالًا؛ نقطة الضعف الوحيدة ازدواج مدخلات (مصروف/سحب/رأس مال) وسياسات توزيع تسكن الكتالوج.
4. **ما لا ينتمي لأي قسم حاليًا:** «السوق» و«Delivery» كخدمة عليا — لا كود لهما؛ إبقاؤهما خارج أي تصميم حالي هو الصادق الوحيد حتى قرار المالك.
5. **ما يحتاج تأكيد المالك:** موضع «السوق» المستقبلي مقابل مقعد «أدواتي» (تعارض التوثيق)، ومصير ازدواج مصادر الكتابة، والافتراض «أول سجل» في محرر الحركات، واعتماد «كم عندي الآن» تسميةً من عدمه.

---

## Suppliers vs Market vs Delivery vs My Tools

| المفهوم | التنفيذ الموثق في origin/main | المسارات | الآثار الرسمية | توثيق فقط | الحالة | الدليل |
|---|---|---|---|---|---|---|
| الموردون الداخليون | دفتر التزامات شراء مواد لما يشتريه المالك: `SupplierPurchase` (اسم حر + إجمالي/مدفوع/ذمة + دفعات ومراجعات)؛ جسر استلام اختياري (`materialId` + كمية متوقعة) يستهلكه جانب المخزون لاحقًا؛ **لا مفهوم موردين خارجيين/سوق** | `/suppliers`، `/suppliers/purchase/:id`، `/suppliers/purchase/:id/payment` | الكاش يتأثر بالمدفوع ضمن صيغة «الكاش المسجل»؛ الذمم في «عليّ للموردين»؛ لا COGS تلقائي | لا | `VERIFIED` — منفذ ومكتمل النطاق المعلن | `src/domain/supplier-purchase/types.ts:40-63`، `supplierPurchaseService.ts:103-105` |
| السوق (Market) | **لا تنفيذ**: لا مسار ولا مخزن ولا كود؛ صف «السوق والتوصيل» في أدواتي معطّل hardcoded (`not_available`) | لا شيء (زر معطّل يشير إلى `/tools`) | لا شيء | نعم — `docs/expansion/` (README/DECISIONS/E-00 حتى E-00.14، MARKET-DELIVERY-OWNER-IA-CONTRACT) توثق قرارًا وتصميمًا فقط؛ current-state §8.1: «التوسعة ليست قدرة منفذة بعد» | `VERIFIED` (كوضع حال) | `Tools.tsx:134,338`، `docs/expansion/README.md` |
| Delivery | **خطوة دورة طلب فقط**: `/orders/:id/deliver` (مراجعة قبل الالتزام؛ الالتزام يكتب استهلاكًا ونقصًا وقبضًا اختياريًا ذرّيًا بلا حدث مالي)؛ مدخلها الوحيد زر الطلب الجاهز؛ لا خدمة توصيل عليا ولا أيقونة سيارة في الترويسة | `/orders/:id/deliver` (حصرًا من `/orders/:id`) | إيراد الفترة يُعترف به عند التأكيد؛ استهلاك المخزون؛ لا كاش تلقائي | **نعم للخدمة العلوية**: عقد E-00.14 §1 يرسم «رمز السيارة في AppBar يفتح قسم التوصيل» مستقبلًا | `VERIFIED` — الفرضية «خدمة علوية» ليست الوضع الحالي | `OrderDetail.tsx:573`، `AppHeader.tsx:38-57`، `docs/expansion/MARKET-DELIVERY-OWNER-IA-CONTRACT.md` |
| أدواتي | وجهة مستقلة (المقعد الرابع): حاسبة عميقة + تفصيل تقدير + فحص سلامة (سطح) + حالة وحدات + مدخل نسخ احتياطي → الإعدادات | `/tools`، `/tools/calculator`، `/tools/estimate/:id`، `/tools/integrity` | **لا أثر مالي/مخزني/تقريري تلقائي إطلاقًا**؛ الكتابة الوحيدة مخزن `cost-estimates`؛ الجسر الوحيد يدوي معلن (تقدير→مسودة) | لا | `VERIFIED` — الفرضية مؤكدة | `costEstimateService.ts:2-3`، `U004.dom.test.tsx:117-135`، `ToolsIntegrity.ui.test.tsx:49-74` |

---

## Discoverability and overlap findings

الأنواع المسموحة: hard to discover / no clear entry / wrong-unclear section / duplicate capability / overlapping name / multiple write sources / lost context.

| النوع | الخلاصة | نقطة البدء | نقطة الوصول | السبب | النقرات | تصنيف الخلاصة | الدليل |
|---|---|---|---|---|---|---|---|
| multiple write sources | المصروف له مصدرا كتابة كاملان: ورقة FAB (سياق ثابت مبسط) ومحرر `/finance/new/operating_expense_*` (تصنيف مشاركة كامل) | ورقة FAB أو مالي | مساران | قرار تصميمي للسرعة مقابل العمق | — | `VERIFIED` | `QuickExpenseForm.tsx:61-102` vs `FinancialEventEditor.tsx:548-601` |
| multiple write sources | المحفظة + الرصيد الافتتاحي من ثلاثة مداخل: Setup، محرر محفظة جديد، مكمل الافتتاحي لاحقًا | التأسيس أو مالي | 3 مسارات | رحلة تأسيس موزعة | — | `VERIFIED` | `Setup.tsx:158`، `cashContinuityService.ts:113-205` |
| multiple write sources | السحب مساران (حركة مالك عند وجود سياسة / حدث عام otherwise)؛ رأس المال ثلاثة مسارات تراكمية | دفتر المالك | 2-3 مسارات | طبقات مال المالك | — | `VERIFIED` | `OwnerWithdrawalEditor.tsx:93-113` |
| multiple write sources | الضبط يُكتب من محرر الضبط ومن عدّ الصندوق؛ سداد القرض من RepaymentSheet مركّب في سطحين | مالي | 2×2 | تصميم مقصود | — | `VERIFIED` | `CashCount.tsx:101-109`، `Loans.tsx:103`+`LoanDetail.tsx:307` |
| hard to discover | مراجعة التسليم لا تُفتح إلا من زر «راجع التسليم وسجّله» داخل تفاصيل طلب في حالة `ready` — لا مدخل من قائمة العمل ولا المواعيد ولا Home | OrderDetail | مسار واحد | قرار «مراجعة قبل التزام» | — | `VERIFIED` | `OrderDetail.tsx:573` |
| hard to discover | سحب المالك مدخله الوحيد داخل دفتر المالك (لا زر سحب من مالي مباشرة) | `/finance` → دفتر المالك | مسار واحد عميق | الدمج الموحد للدفتر | — | `VERIFIED` | `OwnerEntitlement.tsx:639` |
| wrong/unclear section | سياسات التوزيع وقراءة الهامش المباشر — معنى مالي — تسكن سطح الكتالوج (منتجاتي وخدماتي) | الكتالوج | `/catalog` | نشأت مع قراءة المراجع | — | `INFERRED` | `Catalog.tsx:406-449`، `CatalogReadingsSection.tsx` |
| no clear entry | `statementShareDraft` (مشاركة كشف) بلا مستدعٍ إنتاجي — اختبارات فقط؛ `collectionShareDraft` مستورد ميت في OrderDetail | — | لا شيء | بقايا قدرات | — | `VERIFIED` | `shareMessageService.ts:118-131`، `OrderDetail.tsx:36` |
| no clear entry | قيم `focus` المعلنة `export`/`today`/`priority` في عقد التنقل لا يستهلكها أي سطح (روابط خاملة صامتة) | روابط عميقة | — | عقد أوسع من الاستهلاك | — | `VERIFIED` | `navigationContract.ts:40-47` |
| no clear entry | سبب حركة مالك `owner_draw` وسياسة `fixed_shift` مدعومان في النطاق/الخدمة ولا تعرضهما أي واجهة | — | لا شيء | استُبدلا بمسارات أخرى | — | `VERIFIED` | `ownerEntitlementPresentation.ts:42-67` |
| overlapping name | «المراجعة» القديمة vs «مراجعة التسليم» vs «فحص سلامة مالي» — ثلاث قراءات بأسماء متقاربة والمسار `/review` يحوّل إلى مالي | مالي | — | اندماج المراجعة في النبضة | — | `VERIFIED` | `MicroRouter.tsx:157-160` |
| overlapping name | تسمية الوثائق «كم عندي الآن» لسؤال مالي غير موجودة في الواجهة؛ الموجود «الوضع الآن» و«الكاش المسجل» | مالي/Home | — | وعد توزيع لم ينفذ حرفيًا | — | `VERIFIED` (فجوة تسمية) | `Finance.tsx:302`، `redistribution-v1 §2.3` |
| lost context | عكس القبضة لا يظهر من شاشة نتيجة التحصيل — يجب العودة إلى تصحيحات الطلب | ورقة التحصيل | — | عمد (مصدر السجل) | — | `VERIFIED` | `OrderDetail.tsx:1086-1282` |
| lost context (خطر) | محرر حركة المخزون يختار **أول** مادة/طلب/بيع/مرجع/قالب افتراضيًا عند غياب معاملات العمق — إسناد خاطئ صامت محتمل | `/inventory/movement/:type` | — | افتراض الرقم الأول | — | `VERIFIED` (خطر) | `InventoryMovementEditor.tsx:129-155` |
| duplicate capability (نص–سلوك) | صفحة الفحص تقول «ستّة عشر فحصًا» والخدمة تنفذ 13 (MIC-3/5/6 محجوزة) | أدواتي | — | معرفات محجوزة | — | `VERIFIED` | `ToolsIntegrity.tsx:66`، `integrityCheckService.ts:7-8` |
| hard to discover (تعليقات متضاربة) | تعليقا `BottomNav.tsx:2-3` و`AppHeader.tsx:39` يقولان «المقعد الخامس شاغر للسوق» بينما الشريط يعرض «أدواتي» — مضللة لأي مطور/وكيل قادم | الشريط | — | تقادم تعليقات | — | `VERIFIED` | نفس الملفين |

---

## Owner decisions required

أسئلة لا يستطيع الكود الإجابة عنها (10 كحد أقصى):

| القرار المطلوب | لماذا لا يقرر الكود | الخيارات الواقعية | أثر المنتج/التنقل |
|---|---|---|---|
| 1. مصير مقعد «السوق» عند بنائه: هل يدخل الشريط الخامس أم يبقى خارجًا؟ | أربعة مواضع موثقة متضاربة (redistribution §2.2: شاغر للسوق؛ قرار ٢٤: يملأ الخانة الخامسة؛ EX-D10/E-00.14 أقدم: داخل الشريط؛ الكود الحالي: خارج الشريط مع تعليق «مبدأ المالك ٥.٤» غير موثق كنص) | (أ) السوق مقعد خامس عند بنائه ويبقى أدواتي رابعًا · (ب) السوق خارج الشريط (أيقونة/مدخل آخر) وأدواتي دائم · (ج) إعادة ترتيب كاملة بقرار معماري | يحدد شكل الشريط وسقف الوجهات للسنوات القادمة |
| 2. اعتماد «مبدأ المالك ٥.٤» (أدواتي مقعدًا) نصًا موثقًا في المستودع | الكود يستشهد به والوثائق لا تحويه كمبدأ مرقم؛ يظهر فقط في product-source-of-truth §3 وتقرير تنفيذ | (أ) إضافته لقرارات المالك · (ب) دمجه في settled-findings · (ج) تركه خارج المستودع (مرفوض حوكمةً) | حوكمة القرارات ومسار أي وكيل قادم |
| 3. هل تبقى سياسات التوزيع وقراءة الهامش داخل الكتالوج أم تنتقل للمالية؟ | الكود يضعها في الكتالوج بلا أثر مالي؛ معناها تخصيص مالي | (أ) تبقى مع المرجع (قراءة عند السياق) · (ب) تنقل للمالية مع رابط من المرجع · (ج) سطح مستقل | بنية «المالية» وعمق الكتالوج |
| 4. توحيد مصادر كتابة المصروف (ورقة FAB مقابل المحرر العميق) | المسارين يكتبان نفس النوع بخيارات مختلفة — قرار تجربة لا يستطيع الكود حسمه | (أ) إبقاء الاثنين بفروق معلنة · (ب) ترقية الورقة تدريجيًا · (ج) حصر التصنيف الكامل بالمحرر | سرعة اليومي مقابل دقة التصنيف |
| 5. الافتراض «أول سجل» في محرر حركات المخزون | الكود يفترض أول مادة/طلب/بيع عند غياب المعامل — سياسة إدخال تحتاج قرار مالك | (أ) إلغاء الافتراض وإجبار الاختيار · (ب) إبقاؤه مع تأكيد أوضح | خطر إسناد استهلاك/هدر لسجل خاطئ |
| 6. اعتماد تسمية «كم عندي الآن» لتبويب مالي أو إسقاط الوعد الوثائقي | الوثيقة تعدها والواجهة لا تحويها؛ التسمية قرار لغوي للمالك | (أ) اعتمادها · (ب) إبقاء «الوضع الآن» وتحديث الوثيقة | اتساق الوعد اللغوي |
| 7. هل يصبح Setup صفحة واحدة قابلة للطي (القرار ٤) أم يُقر تعليقه صراحةً لصالح المعالج الثلاثي الحالي + صفحة الأساس؟ | الكود الحالي معالج ٣ خطوات والقرار ٤ يرفض المعالجات — لا يوجد توثيق إعادة فتح | (أ) توثيق الإبطال رسميًا · (ب) العودة لتصميم القرار ٤ | شكل أول تجربة تأسيس |
| 8. مصير قدرات المشاركة غير المستخدمة (كشف/قبضة) | كود مكتمل بلا مدخل — بناء مدخل أو حذف قرار منتج | (أ) إضافة مدخلات · (ب) إزالة الكود الميت | نظافة الكود مقابل ميزة مستقبلية |
| 9. نموذج جسر الشراء→المخزون: هل يبقى الاستلام يدويًا اختياريًا (الوضع الحالي) أم يصبح تلقائيًا عند الربط؟ | العقد يقول «حتى يُنفَّذ الاستهلاك» — سياسة تشغيل | (أ) يدوي دائمًا · (ب) اقتراح استلام تلقائي قابل للرفض | دقة المخزون مقابل سرعة الشراء |
| 10. أولويات إصلاح التوثيق المتقادم (current-state §40، جرد F-081/F-083، تعليقا الشريط، نص الـ16 فحصًا) | كلها إصلاحات توثيق بلا خلاف كودي — الترتيب قرار مالك | ترتيب حر (مقترح: current-state أولًا لأنه «المصدر الحي») | صحة أي عمل وكيل قادم |

---

## Evidence and limitations

**المرجع المفحوص:** Micro `origin/main` = `f21f777d3b4df874806061755dff5fc956ca4cf3` — 2026-09-15 11:01:58 +0000 («Merge Brand Activation and corrected Launch Splash»). النسخة المحلية نظيفة قبل الفحص وبعده (`git status` بلا أي تعديل).

**الملفات والاختبارات المستخدمة (الأساسية):** `app/MicroRouter.tsx`، `app/navigation.ts`، `app/navigationContract.ts`، `app/routeClassifier.ts`، `app/StartupGate.tsx`، `app/useReturnNavigation.ts`؛ `components/layout/{MicroAppShell,AppHeader,BottomNav,QuickActionSheet}.tsx`؛ `components/security/AppLockGate.tsx`؛ `components/brand/BrandLaunchSplash.tsx`؛ `components/forms/UnsavedChangesGuard.tsx`؛ صفحات `pages/*.tsx` (52 صفحة)؛ خدمات `application/*` (مالية/كاش/تحصيل/موردون/مخزون/تسليم/اتفاقات/مبيعات/مواعيد/أطراف/تقديرات/كتالوج/أمان/هوية/تفضيلات/تشخيص/مشاركة/وقت)؛ نطاقات `src/domain/*` (أبرزها `financial-event/policies.ts` و`craft-order/policies.ts` و`owner-entitlement/policies.ts` و`direct-sale/policies.ts` و`inventory-material/policies.ts` و`cash-continuity/types.ts` و`supplier-purchase/types.ts`)؛ `storage/local/indexedDbStores.ts` و`types.ts`؛ اختبارات مقروءة (لم تُشغَّل): `G3Delivery.dom.test.tsx`، `R1.orderDetailVoid.test.tsx`، `U001/U004/U005.dom.test.tsx`، `Orders.ui.test.tsx`، `Setup.ui.test.tsx`، `ToolsIntegrity.ui.test.tsx`، `QuickActionSheet.guard.test.tsx`، `navigationContract.test.ts`، `routeKnowledgeSync.test.ts`؛ وثائق: `AGENTS.md`، `README.md`، `docs/00-document-index.md`، `docs/operations/current-state.md` (رؤوس الأقسام + §2/§8.1)، `docs/operations/micro-thinking-charter-v1.md`، `docs/operations/agent-handoff-protocol-v1.md`، `docs/product/{problem-statement-v5,owner-decisions-v1,capability-redistribution-v1}.md`، `docs/inventory/00-summary.md`، `docs/contracts/{01,05}.md`، `docs/expansion/` (فهرسة وقراءة انتقائية).

**ما لم يُفحص عمدًا (مع التصنيف):**
- لقطات الشاشة: `SCREENSHOT_SOURCE_UNVERIFIED` — المسار المحدد أعاد 404؛ لم تُفتح أي لقطة (حدّ هذا التدقيق).
- تشغيل التطبيق والاختبارات فعليًا: `NOT_EXECUTED` — كل السلوكيات الديناميكية مستندة إلى قراءة الكود والاختبارات المكتوبة فقط.
- اختبار جهاز فعلي/Android/iOS/PWA ميداني: `NOT_EXECUTED` (خارج نطاق).
- بقية الوثائق خارج القائمة أعلاه (تقارير الجرد التفصيلية 01-09، سيناريوهات، أبحاث): قراءة انتقائية حسب الحاجة فقط.
- سجلات الاستخدام الفعلية/تكرار الاستعمال: غير موجودة أصلًا (لا قياس استخدام في الكود) — أي حكم تكراري يستحق `OWNER_CONFIRMATION_REQUIRED`.

**كتابات لم تحدث:** لم تُنفَّذ **أي** كتابة على مستودع Micro (لا commit ولا push ولا تعديل ملف؛ `git status` نظيف) ولا على مجلد لقطات الشاشة (لم يُفتح أصلاً لعدم وجوده). الكتابة الوحيدة: هذا التقرير وحجته في مستودع Documents على فرع `audit/micro-product-facts-journey-20260915` بـPR واحد غير مدموج.

**تناقضات موثقة بين الكود وcurrent-state ووثائق المنتج:**

| # | التناقض | التفصيل | التصنيف |
|---|---|---|---|
| C1 | مقعد «السوق» الخامس | وثيقة التوزيع §2.2: «المقعد الخامس شاغر للسوق»؛ قرار المالك ٢٤: «يملأ السوق الخانة الخامسة»؛ عقود التوسعة الأقدم (EX-D10/E-00.14): السوق داخل الشريط؛ **الكود**: أدواتي رابع والسوق خارج الشريط، مع تعليقي كود متقادمين (`BottomNav.tsx:2-3`، `AppHeader.tsx:39`) ما زالا يقولان «الخامس شاغر للسوق» | `VERIFIED` — تعارض وثائق–كود وداخلي-كود |
| C2 | Setup معالج ٣ خطوات vs القرار ٤ «صفحة واحدة قابلة للطي، المعالج مرفوض» | الكود: معالج خطوات؛ تصميم القرار ٤ تحقق جزئيًا في صفحة الأساس؛ لا توثيق لإعادة فتح القرار رغم نصه الحاكم | `VERIFIED` — فجوة حوكمة |
| C3 | «كم عندي الآن» | موعودة في وثيقة التوزيع كتسمية سؤال مالي؛ **صفر مطابقات** في الواجهة؛ الموجود «الوضع الآن»/«الكاش المسجل» | `VERIFIED` — وعد لم ينفذ حرفيًا |
| C4 | تقادم current-state §40 | يقول إن PR #159 «مفتوح وغير مدمج» وإن main عند `4af025d`؛ الواقع: PR #159 **مدموج** 2026-09-13 (`c0469e2`) والرأس `f21f777` أبعد بـ~20 commit (موجة العلامة/السبلاش) — يخالف قاعدة §7 في الوثيقة نفسها (التحديث بنفس الـPR) | `VERIFIED` |
| C5 | تقادم جرد المستودع (docs/inventory) | الجدول «غير قابل للوصول» (F-077…F-083) صار كله غير صحيح: F-077/078/079/080/082 صارت **موصلة** من الواجهة، وF-081/F-083 **حُذفتا من الكود** أصلًا | `VERIFIED` |
| C6 | تقادم code-facts-v1 | يقول «لا يوجد بيع في النظام» و29 مسارًا ومخطط 26؛ الكود: بيع مباشر منفذ، 56 مسارًا، مخطط 35 | `VERIFIED` |

**حالة فتح الـPR (توثيق صادق):** فرع التقرير دُفع بنجاح إلى Documents، لكن إنشاء الـPR عبر API تعطّل بسبب توكن الوصول الدقيق (fine-grained PAT) الذي يملك صلاحية كتابة المحتويات (Contents: Write) ولا يملك صلاحية «Pull requests: Write» — الخطأ الموثق: HTTP 403 «Resource not accessible by personal access token» عبر REST وGraphQL معًا. لم يُنشأ أي PR ولن يُ ادّعى إنشاؤه. لإنشاء الـPR بنقرة واحدة:
`https://github.com/Qays7753/Documents/compare/main...audit/micro-product-facts-journey-20260915?expand=1`

**ملفات الحجة المرفقة:** [`baseline-commands.txt`](evidence/baseline-commands.txt) · [`repo-access-and-pr159.txt`](evidence/repo-access-and-pr159.txt) · [`route-index.md`](evidence/route-index.md)

**قيود منهجية إضافية:** (1) عدد النقرات `NOT_MEASURED` في كل الرحلات إلا ما أثبته اختبار مقروء (التسليم: نقرة تنفيذ واحدة). (2) «تكرار الاستخدام» غير قابل للاستدلال — أي ترتيب أولويات يجدر به `OWNER_CONFIRMATION_REQUIRED`. (3) خمس متخصصات قراءة (قشرة/تنقل، مالية، مسارات عمل، أدوات، مراجع مستقل) بمنهجية قراءة ثابتة فقط؛ المراجع المستقل أعاد التحقق من عينة موسعة من الادعاءات ولم يجد ادعاءً غير مدعوم، لكن التغطية ليست إثباتًا رياضيًا لكل سطر. (4) صيغة المال الموثقة أعلاه مقروءة من `projectFinancialService.ts:392-424` ولم تُختبر رقميًا.

AUDIT_COMPLETE — OWNER_DECISIONS_REQUIRED
NO_MICRO_OR_SCREENSHOT_WRITES_PERFORMED
DOCUMENTS_REPORT_BRANCH_PUSHED — PR_CREATION_BLOCKED_TOKEN_SCOPE
OWNER_ACTION_REQUIRED — CREATE_PR_VIA_COMPARE_URL_OR_GRANT_PULL_REQUESTS_WRITE

