# MICRO 29 Foundation Development Brief — Revised

## 0. حالة الوثيقة وقرار النطاق

هذه وثيقة تخطيط منقحة فقط. لا تمثل موافقة على التنفيذ، ولا تغيّر `micro-standard-v2` أو Micro أو Accounting.

**التقسيم المعتمد:** 29 ملفًا أساسيًا/تنفيذيًا + `MANIFEST.json` و`RELEASE.md` كملفي metadata. ستبقى الحزمة كاملة تحت إصدار واحد، لكن Wave 0 تسجل هذا التقسيم وحدود كل ملف قبل أي تغيير.

### الملفات الأساسية الـ29

`README.md`, `accessibility.md`, `button-system.md`, `color-system.md`, `component-contracts.md`, `component-gallery.css`, `component-gallery.html`, `component-gallery.js`, `component-states.md`, `content-guidelines.md`, `coverage-matrix.json`, `data-display-system.md`, `decision-log.md`, `design-tokens.css`, `design-tokens.json`, `empty-loading-error-states.md`, `iconography.md`, `input-system.md`, `motion-interaction.md`, `navigation-shell.md`, `overlay-system.md`, `responsive-geometry.md`, `self-critique.md`, `source-inventory.md`, `spacing-radius-elevation.md`, `surface-system.md`, `typography.md`, `verification-report.md`, `visual-direction.md`.

## 1. قرار النطاق

| الطبقة | ما يدخل فيها | ما لا يدخل فيها |
|---|---|---|
| Foundation Tokens | الأدوار الحالية، الطبقات، typography، spacing/radius/elevation، geometry، RTL، numeric isolation، markers | ألوان جديدة، formulas، sync، auth، صلاحيات فعلية |
| Primitive Contracts | slots والقيم المرئية والحالات والعرض المتجاوب، ومنها Metric، Relation، Row، Lifecycle، Period، SimpleChart frame | معنى البيانات، مصدرها، business actions، سياسة مالية |
| Composition Recipes | Metric/Balance، parts-whole، OperationalRow، Question-led SimpleChart، واختيار Row/Surface/Card/Sheet | شاشات Micro الكاملة، Order/Party semantics، delivery، KPI formulas |
| Gallery/Verification | خمس عينات محايدة في Wave C، وفحصها وتوثيقها وإصدارها في Wave D | Prototype منتج، routes، data writes، منطق تقارير |
| Micro Product | معنى البيانات، مصادرها، المعادلات، سياسة العملية، الصلاحيات والتنفيذ، sync/conflict والشاشات | لا يدخل في الـ29 ولا يُنقل إليه شيء قبل اعتماد Wave D |

## 2. قرارات التوصيات

| الفجوة | القرار | السبب |
|---|---|---|
| Composition recipes غير متعاقد عليها | ACCEPT | تعالج الفجوة الجذرية مباشرة |
| Metric مع context/period | ACCEPT | تجعل القيمة قابلة للمسح والفهم |
| Parts/whole relation | ACCEPT | تضيف معنى دون لون أو بطاقة عامة |
| OperationalRow | ACCEPT | يثبت كثافة هاتفية منظمة |
| Lifecycle pending/unknown/retry/result | ACCEPT | يمنع النجاح الزائف |
| Row/Surface/Card/Sheet rules | ACCEPT | يثبت hierarchy دون cardification |
| Dense mobile scenes | ACCEPT | مطلوب لإثبات الجودة عند 320px |
| Read-to-action handoff | ACCEPT | يربط القراءة بالإجراء بصريًا فقط |
| Warm-Ink/Clay guardrails | ACCEPT | يحافظ على الأدوار الحالية ويمنع الإفراط |
| Question-led SimpleChart contract | ACCEPT | عقد بصري محدود مطلوب قبل العينة |
| SimpleChart gallery specimen | ACCEPT | يضاف في Wave C فقط |
| Documentation evidence | ACCEPT | يجعل النتيجة قابلة لإعادة الإنتاج |
| Advanced financial state semantics | OWNER_DECISION | المعنى المنتجـي لا يُحسم من Foundation |
| KPI summary recipe | DEFER | formula/source/update frequency داخل Micro |
| New palette | REJECT | لا دليل أن اللون سبب الفجوة |
| Generic tables | REJECT | ليست افتراضيًا أفضل للهاتف |
| PermissionState/ToolResult | OWNER_DECISION | نحتاج اعتماد لغة الحدود، دون تنفيذ صلاحيات أو كتابة |

## 3. التطوير الأول

يبدأ التطوير الفعلي بعد Wave 0 فقط، وبالترتيب التالي:

1. عقود Metric/Balance، Relation، OperationalRow، Lifecycle، Period، وQuestion-led SimpleChart.
2. ملكية المعنى وحدود عدم الاستنتاج داخل كل عقد.
3. قواعد Row/Surface/Card/Sheet وaction boundary.
4. خمس عينات محايدة في المعرض.
5. التحقق والتوثيق والإصدار.

لا تتغير الألوان أو الخلفيات أو أدوار Warm-Ink وClay أو semantic roles الحالية.

## 4. عقود المكونات المطلوبة

### 4.1 Metric / Balance

- **الهدف البصري:** قيمة أساسية مع label وcontext وperiod دون تحويل كل قيمة إلى Card.
- **يستخدم:** لقيمة مرئية مؤكدة أو لحالة عرض معروفة. **لا يستخدم:** لنتيجة مجهولة بلا Unknown treatment.
- **Anatomy/slots:** `label`, `value`, `currency/context`, `period`, `comparison?`, `state marker?`, `supporting note?`, `action?`.
- **البيانات المرئية:** نص، رقم، `د.أ`/`دأ` عند الحاجة، فترة، مقارنة، state word؛ لا formula.
- **الحالات:** default/loading/empty/error/unknown/pending/partial عند انطباقها.
- **Hierarchy/roles:** Warm-Ink للقيمة؛ neutral surface للسياق؛ semantic color للحالة فقط؛ Clay ليس افتراضيًا.
- **RTL والأرقام:** العربية أولًا، الأرقام الإنجليزية، tabular numerals، bidi isolation، amount slot ثابت.
- **Responsive/accessibility:** 320/360/390/430 و200% دون clipping أو overflow؛ label/state واضحان؛ اللون ليس الإشارة الوحيدة.
- **Primitive/Micro relation:** يعتمد على typography/amount/state primitives؛ Micro يملك معنى القيمة ومصدرها وفترتها.
- **Semantic ownership:** الـ29 تملك التمثيل البصري والـslots والحالات المرئية؛ Micro يملك معنى البيانات ومصدرها ومعادلاتها وسياسة استخدامها وصلاحيتها.
- **Do not infer:** لا يستنتج formula أو source أو صحة مالية أو أن القيمة KPI أو أن pending نجاح.
- **Acceptance:** تُقرأ القيمة وcontext وperiod وstate من أول نظرة في RTL عند 320px، مع محاذاة amount ثابتة وAA/no-overflow/200% pass.

### 4.2 Parts / Whole Relation

- **الهدف:** إظهار الأجزاء والمجموع عندما توجد علاقة جمع/تغطية حقيقية.
- **يستخدم:** فقط مع `whole` وأجزاء قابلة للتفسير. **لا يستخدم:** للأرقام غير القابلة للجمع أو لعلاقة زخرفية.
- **Anatomy/slots:** `whole`, `part A`, `part B?`, `remaining/ratio?`, `state marker`, `text explanation`.
- **البيانات:** labels وقيم وعلاقة عرضية؛ لا policy مالية.
- **الحالات:** complete/partial/due أو overdue عند اعتماد Micro، unknown/no-data/loading/error.
- **Hierarchy/roles:** Warm-Ink للـwhole؛ neutral bar/border؛ semantic color للحالة فقط.
- **RTL/accessibility/responsive:** الأرقام معزولة؛ علاقة نصية بديلة؛ لا overflow عند 320px/200%.
- **Primitive/Micro relation:** يستخدم bar/marker primitive؛ Micro يملك semantics والقرار المالي.
- **Semantic ownership:** الـ29 تملك slots والعرض والحالات؛ Micro يملك معنى الأجزاء والمجموع ومصدرها.
- **Do not infer:** لا يستنتج أن كل `remainder` دين مسجل، ولا أن العلاقة تعني تحصيلًا أو التزامًا.
- **Acceptance:** لا يظهر relation treatment إلا مع whole/parts واضحين، ويظل المعنى مقروءًا دون اللون أو الشريط وحده.

### 4.3 OperationalRow

- **الهدف:** كثافة تشغيلية منظمة على الهاتف دون جدول أو Card عامة.
- **يستخدم:** لحركة/طلب/طرف/مادة ذات title وcontext وstatus وamount. **لا يستخدم:** للملخصات الكبرى أو العلاقات المعقدة.
- **Anatomy/slots:** `leading marker?`, `title`, `meta`, `status`, `amount`, `secondary amount?`, `trailing action?`, `divider/boundary`.
- **البيانات:** بيانات عرض فقط؛ لا يحدد معنى الحركة أو صلاحية الإجراء.
- **الحالات:** default/pressed/focused/disabled/loading/pending/unknown/error-retry/reversed/partial عند اعتماد semantics.
- **Hierarchy/roles:** title primary، meta muted، amount Warm-Ink/tabular، state semantic + word/marker، border/surface للفصل.
- **RTL/accessibility/responsive:** amount slot ثابت، action صحيح في RTL، التفاف النص دون دفع الرقم؛ 320/360/390/430 و200% دون overflow؛ focus واضح.
- **Primitive/Micro relation:** يعتمد على typography/icon/state/amount؛ Micro يركبه للطلبات والحركات والأطراف والمخزون.
- **Semantic ownership:** الـ29 تملك بنية الصف وحالاته المرئية؛ Micro يملك معنى الحقول ومصدرها وصلاحية الإجراء.
- **Do not infer:** لا يستنتج نوع الطرف أو حالة السجل أو أن action مسموح أو أن amount مستحق.
- **Acceptance:** صف طويل الاسم/meta يبقى قابلًا للمسح عند 320px، مع amount/status/action قابلة للوصول دون لون وحيد.

### 4.4 Lifecycle State

- **الهدف:** منع success زائف أثناء pending أو unknown، وحفظ وضوح retry/result.
- **يستخدم:** لعملية أو نتيجة ذات مراحل. **لا يستخدم:** لزخرفة ثابتة.
- **Anatomy/slots:** `state word`, `marker/icon`, `explanation`, `next action`, `preserved input?`.
- **الحالات:** loading/pending/unknown/failed/retryable/completed أو posted إن قرر Micro/reversed كأثر.
- **Roles:** neutral/info لـpending، error للفشل، success لتأكيد مثبت فقط؛ Warm-Ink للنص.
- **RTL/accessibility/responsive:** رسالة عربية قصيرة؛ marker غير لوني؛ reduced motion؛ لا يختفي action عند 320px/200%.
- **Semantic ownership:** الـ29 تملك العرض والـslots وstate markers؛ Micro يملك lifecycle truth ونقطة التأكيد.
- **Do not infer:** لا يستنتج أن pending أو unknown نجاح، ولا أن failed قابل للإعادة، ولا أن reversed يمحو الأثر.
- **Acceptance:** كل حالة تعرض word + marker + next action، ولا تظهر عينة pending/unknown كنجاح نهائي.

### 4.5 Period / DateRange

- **الهدف:** عرض النطاق الزمني كجزء مفهوم من Metric/Chart دون فرض سياسة زمنية.
- **يستخدم:** للفترة الشهرية/الأسبوعية/اليومية/المخصصة. **لا يستخدم:** لتقرير timezone غير معتمد.
- **Anatomy/slots:** `period label`, `preset`, `custom range`, `validation`, `loading/no-data marker`.
- **Semantic ownership:** الـ29 تملك input/slots/states؛ Micro يملك owner-day/timezone ومصدر البيانات.
- **Do not infer:** لا يستنتج timezone أو أن الفترة تعني KPI أو أن البيانات مكتملة.
- **Roles/RTL/accessibility/responsive:** neutral input، focus واضح، labels عربية، أرقام معزولة، لا overflow عند 320px/200%.
- **Primitive/Micro relation:** input/select/overlay primitives؛ Micro يملك تطبيق النطاق.
- **Acceptance:** preset وcustom وinvalid/loading/no-data مفهومة وقابلة للوصول في RTL.

### 4.6 Question-led SimpleChart

- **الهدف:** عقد بصري محدود لرسم يجيب سؤالًا واضحًا، دون منطق تقارير أو formula.
- **يستخدم:** عندما توجد مقارنة مرئية مفيدة. **لا يستخدم:** لملء مساحة أو لتقرير KPI غير معرف.
- **Anatomy/slots:** `functional question/title`, `primary series`, `secondary series?`, `zero`, `no-data`, `empty`, `loading`, `legend/short interpretation`, `text alternative`.
- **البيانات المرئية:** labels/values/series names وstates؛ لا formula أو query أو source.
- **الألوان:** أدوار الألوان الحالية فقط؛ semantic role عند انطباقها؛ لا إضافة hues ولا black/Clay كافتراض.
- **RTL/accessibility/responsive:** legend وتفسير مقروءان بالعربية؛ بديل نصي؛ zero واضح؛ 320/200% دون clipping؛ reduced motion.
- **Semantic ownership:** الـ29 تملك frame/series slots/labels/states/text alternative؛ Micro يملك السؤال الفعلي ومصدر البيانات والمعادلات وسياسة KPI.
- **Do not infer:** لا يستنتج formula أو source أو trend أو KPI policy أو نجاحًا ماليًا من شكل الرسم.
- **Primitive/Micro relation:** chart frame primitive؛ العينة المحايدة في Wave C؛ report implementation داخل Micro.
- **Acceptance:** كل مثال يملك سؤالًا وظيفيًا وprimary/secondary عند الحاجة، zero، no-data/empty/loading، legend/interpretation، وبديلًا نصيًا.

### 4.7 Container Choice: Row / Surface / Card / Sheet

- **الهدف:** تنوع هرمي هادئ بدل Card لكل شيء.
- **الاستخدام:** Row للبيانات المتكررة؛ Surface للتجميع الهادئ؛ Card لملخص/قرار ذي حدود؛ Sheet لإجراء/تفاصيل مؤقتة مع السياق.
- **لا يستخدم:** Card كحاوية افتراضية أو Sheet لشاشة كاملة بلا سبب.
- **Semantic ownership:** الـ29 تملك قواعد الشكل والـboundary/elevation؛ Micro يملك سبب المهمة وتسلسلها.
- **Do not infer:** لا يستنتج Card أن المحتوى KPI، ولا Sheet أن الإجراء مؤكد، ولا Row أن البيانات قابلة للتنفيذ.
- **Acceptance:** كل عينة تذكر use وanti-use، وتنجح في RTL/320/200% وcontrast/no-color-only.

### 4.8 PermissionState وToolResult — مشروطان بقرار المالك

- **Semantic ownership:** الـ29 تملك العرض المرئي للمنع/المجهول/النتيجة والـslots؛ Micro يملك الصلاحية الفعلية، حماية البيانات، formula، ومتى/هل تُكتب النتيجة.
- **Do not infer:** PermissionState لا يستنتج سياسة صلاحيات؛ ToolResult لا يستنتج أن الحساب يكتب سجلًا ماليًا.
- **قرار الإدخال:** `OWNER_DECISION` قبل إضافة contract أو specimen؛ لا تنفيذ صلاحيات أو كتابة داخل الـ29.

## 5. موجات التطوير

### Wave 0 — حماية وتثبيت baseline (محايدة)

- **الملفات:** جميع ملفات الحزمة الحالية، مع `MANIFEST.json` و`RELEASE.md` كـmetadata.
- **التغيير:** لا تغيير في المحتوى؛ تثبيت baseline، حساب وتسجيل hashes، تثبيت قائمة 29+2، تسجيل حدود كل ملف، وتحديد rollback boundary.
- **لا يتغير:** كل الألوان، الخلفيات، الحدود، التوكنز، الوثائق، المعرض، Micro، Accounting.
- **الاعتماديات:** لا شيء.
- **المخاطر:** baseline ناقص أو hash غير قابل لإعادة الإنتاج.
- **القبول:** manifest للملفات، hash record، file-boundary register، وrollback boundary محفوظة قبل Wave A.
- **Rollback:** إزالة سجل Wave 0 الإداري فقط؛ لا تمس الحزمة.

### Wave A — العقود الأساسية

- **الملفات:** `component-contracts.md`, `data-display-system.md`, `component-states.md`, `empty-loading-error-states.md`, `input-system.md`, `motion-interaction.md`, `typography.md`, `accessibility.md`.
- **التغيير:** عقود Metric/Relation/OperationalRow/Lifecycle/Period وإضافة `Semantic ownership` و`Do not infer` لكل عقد.
- **لا يتغير:** الألوان والخلفيات وCloud Code roles وproduct boundary.
- **الاعتماديات:** Wave 0 وقرارات owner التي تمنع تثبيت semantics.
- **المخاطر:** إدخال policy مالية أو توسيع النطاق.
- **القبول:** كل عقد يملك slots/states/RTL/320/200%/accessibility/ownership/non-inference.
- **Rollback:** أقسام العقود الجديدة كوحدة واحدة.

### Wave B — وصفات التكوين والعقد البصري للرسم

- **الملفات:** `surface-system.md`, `spacing-radius-elevation.md`, `visual-direction.md`, `color-system.md`, `button-system.md`, `overlay-system.md`, `navigation-shell.md`, `iconography.md`, `component-contracts.md`, `data-display-system.md`, `accessibility.md`.
- **التغيير:** Row/Surface/Card/Sheet rules، action boundary، role guardrails، و`Question-led SimpleChart` contract المحدود: السؤال، primary/secondary، zero، no-data/empty/loading، legend/interpretation، text alternative، current colors.
- **لا يتغير:** لا Chart متقدم، لا report logic، لا formula/source/KPI policy، لا palette جديدة.
- **الاعتماديات:** Wave A.
- **المخاطر:** تحويل العقد إلى chart implementation أو إضافة ألوان.
- **القبول:** عقد الرسم بصري فقط، وله ownership/non-inference؛ كل container له use/anti-use.
- **Rollback:** أقسام الوصفات وعقد SimpleChart كوحدة واحدة.

### Wave C — عينات المعرض فقط

- **الملفات التي تتغير تركيبيًا:** `component-gallery.html`, `component-gallery.css`, `component-gallery.js`, `coverage-matrix.json`.
- **التغيير:** خمس عينات محايدة: Metric، Relation، OperationalRow، Lifecycle، Container Choice؛ وعينة SimpleChart وتفاعل فحص الحالات فقط.
- **لا يتغير:** لا شاشة منتج، لا Micro route، لا business data، لا report logic، لا policy، لا توكنز جديدة.
- **الاعتماديات:** Waves 0–B، وموافقة owner على المصطلحات المشروطة.
- **المخاطر:** المعرض يصبح Prototype أو يحاكي تنفيذ Micro.
- **القبول:** العينات تثبت المعايير الخمسة أدناه عند RTL و320/360/390/430 و200% وreduced motion وcontrast/no-overflow.
- **Rollback:** عينات وسلوك المعرض ومصفوفة التغطية كوحدة Wave C.

### Wave D — التحقق والتوثيق والإصدار فقط

- **الملفات التي تتغير:** `verification-report.md`, `README.md`, `RELEASE.md`, `MANIFEST.json`, `source-inventory.md`, `self-critique.md`, `decision-log.md`.
- **مدخلات التحقق:** ملفات المعرض من Wave C؛ لا تُعدّل في Wave D.
- **التغيير:** تسجيل النتائج، تحديث الحدود، توثيق الإصدار وقرار الجاهزية فقط.
- **لا يتغير:** لا تركيبات، لا سلوك، لا CSS/JS للمعرض، لا content examples جديدة.
- **الاعتماديات:** Wave C مكتملة ونتائج الاختبار متاحة.
- **المخاطر:** إصدار غير مستحق أو ادعاء اختبار غير منفذ.
- **القبول:** لا تضارب بين tokens/contracts/gallery/docs؛ كل claim مربوط بدليل؛ حدود device/screen-reader مصرح بها.
- **Rollback:** توثيق وmetadata وrelease record كوحدة واحدة؛ لا يرجع أمثلة Wave C.

## 6. معيار الثراء البصري القابل للقياس

المعرض في Wave C يجب أن يثبت **خمس عينات محايدة**:

1. قيمة مع `label + context + period`.
2. علاقة `parts/whole` مع بديل نصي.
3. `OperationalRow` طويل الاسم والـmeta والحالة والمبلغ.
4. lifecycle من `unknown/pending/retry` دون نجاح زائف.
5. اختيار `Row/Surface/Card/Sheet` مع سبب استخدام وanti-use case.

كل عينة تُقيّم بنعم/لا وبملاحظات دليلية على:

- وضوح الهرمية وقابلية المسح من أول نظرة.
- وضوح الحالة والإجراء التالي.
- ثبات محاذاة المبلغ في RTL وعزل الأرقام.
- عدم التزاحم عند 320px.
- عدم وجود overflow عند 320/360/390/430 و200%.
- عدم الاعتماد على اللون وحده.
- بقاء Warm-Ink وClay والطبقات الحالية دون توسعة لونية.
- focus وcontrast وreduced motion عند انطباقها.

لا تستخدم نتيجة «أجمل/أغنى» كحكم منفرد؛ لا تُقبل العينة إلا إذا اجتازت هذه الشروط القابلة للفحص.

## 7. قائمة قرارات المالك

1. اعتماد تقسيم 29 ملفًا أساسيًا + ملفي metadata قبل Wave 0.
2. اعتماد semantics للحالات المتقدمة (`partial`, `due`, `overdue`, `reversed`, `posted`) قبل تثبيت أمثلة Wave A.
3. اعتماد أن Relation تعرض العلاقة فقط ولا تستنتج أن كل remainder دين مسجل.
4. اعتماد presets الخاصة بـPeriod، مع إبقاء timezone/owner-day داخل Micro.
5. اعتماد اللغة المرئية لـPermissionState وToolResult قبل Wave C إن أريد إدخالهما.
6. اعتماد أسئلة SimpleChart الفعلية فقط داخل Micro؛ الـ29 لا تملك source/formula/KPI policy.

## 8. معيار التوقف

تتوقف الخطة عند جاهزية حزمة الـ29 للتركيب لاحقًا عندما:

- تكون العقود والوصفات واضحة وتحتوي `Semantic ownership` و`Do not infer`.
- تنجح العينات الخمس وعينة SimpleChart في شروط القياس.
- ينجح RTL، 320/360/390/430، 200%، reduced motion، focus، contrast، وno-overflow.
- لا يوجد تضارب بين tokens والعقود والتوثيق والمعرض.
- لا يوجد منطق Micro أو policy مالية أو sync أو صلاحيات تنفيذية داخل الحزمة.
- Wave D يسجل الأدلة ويصدر الإصدار فقط بعد مراجعة المالك.

## 9. قاعدة الإيقاف الحالية

هذه النسخة المنقحة **خطة فقط**. لم تبدأ Wave 0 أو أي Wave أخرى، ولم تُعدّل الحزمة أو Micro أو Accounting، ولم يُكتب كود أو CSS أو JavaScript، ولم يُنشأ Prototype أو Commit أو Branch أو Pull Request.
