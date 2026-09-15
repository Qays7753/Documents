# Micro Standard v2 — Prompt التنفيذ المرحلي الآمن

أنت تعمل على تطوير حزمة **Micro Standard الحالية فقط**. هذه مهمة تنفيذ مرحلية، لكن لا يجوز تنفيذ الموجات كلها دفعة واحدة. نفّذ موجة واحدة فقط، تحقّق منها، سلّم تقريرها، ثم توقف حتى يراجع المالك النتيجة ويعطي موافقة صريحة على الموجة التالية.

## 1. الهدف

تطوير حزمة `micro-standard-v2` حتى تصبح Foundation بصرية ومكوّناتية قادرة على إنتاج واجهات Micro غنية ومهنية لاحقًا، مع الحفاظ على جمال الأساس الحالي وعدم إعادة بناء Micro أو نسخ Accounting.

نحن لا نعيد تصميم المنتج، ولا نبني شاشات Micro كاملة، ولا ننقل منطق Micro إلى Foundation. نحن نطوّر التوكنز والعقود والوصفات والأمثلة المحايدة والتحقق داخل حزمة الـStandard فقط.

## 2. مصادر الحقيقة

المصدر التنفيذي الحالي:

`https://github.com/Qays7753/Documents/tree/main/micro-standard-v2`

المستندات المعتمدة لهذه المهمة:

- `MICRO29FoundationDevelopmentBrief—Revised.md`
- `MICRO_29_FOUNDATION_WAVE_PLAN_REVISED.csv`
- هذا الـPrompt.

استخدم مستودع Micro وAccounting فقط عند الحاجة للتحقق من دليل أو سياق سبق اعتماده. لا تعدّل أيًا منهما ولا تنسخ منهما كودًا أو شاشات أو هوية أو منطقًا.

إذا وجدت أي Skill أو تقرير تاريخي أو تعليمات قديمة تتعارض مع هذه المصادر الحالية، فاعتبرها منهج مراجعة فقط، واتبع القيم والقرارات الحالية في الحزمة وهذا الـPrompt. لا تُعد أي Palette أو اتجاه بصري قديم.

## 3. نطاق الملفات

اعتمد التقسيم التالي:

- **29 ملفًا أساسيًا/تنفيذيًا:** كل الملفات الحالية في الحزمة باستثناء `MANIFEST.json` و`RELEASE.md`.
- **ملفا metadata:** `MANIFEST.json` و`RELEASE.md`.

الحزمة كلها إصدار واحد، لكن لا يجوز أن توسّع ملفات metadata نطاق التصميم أو تدخل سياسة منتج.

لا تنشئ ملفات تصميم موازية خارج الخطة. إذا احتجت سجلات أو تقارير تنفيذ، ضعها في مجلد تسليم/staging منفصل خارج `micro-standard-v2/`، ولا تجعلها جزءًا من الحزمة المنشورة إلا إذا نصت Wave D على ذلك.

## 4. قيود لا يجوز خرقها

لا تغيّر القيم أو الأدوار التالية:

- `#D97757` = هوية/إنشاء/FAB.
- `#C96442` = اختيار/حالي/حافة أو خط تفاعلي.
- `#141413` = Warm-Ink للقيمة الأساسية والنص الأولي وإجراء الالتزام وفق العقود الحالية.
- `#FAF9F5`, `#F5F4ED`, `#F0EEE6`, `#FFFFFF` = الخلفية والطبقات والأسطح الحالية.

لا تضف ألوانًا جديدة، ولا توسّع الأسود أو Clay كحل عام، ولا تغيّر Light Mode أو RTL أو الهاتف الرأسي أو Numeric Bidi Isolation أو سلم الأرقام الحالي إلا إذا أثبت فحص قبول وجود خطأ حقيقي، وعندها توقف واطلب قرار المالك.

لا تدخل داخل الحزمة: formulas، مصادر البيانات، سياسات المحاسبة أو الضرائب، معنى الدين، صلاحيات فعلية، auth، sync، conflict resolution، delivery behavior، أو business actions التي تكتب سجلات.

كل عقد بصري جديد يجب أن يحتوي بوضوح على:

- `Semantic ownership`: الـFoundation يملك التمثيل والـslots والحالات المرئية؛ Micro يملك المعنى والمصدر والمعادلة والسياسة والصلاحية.
- `Do not infer`: ما الذي لا يجوز للعقد استنتاجه.

## 5. حماية المستودع ومسار العمل

لا تعمل مباشرة على `main`. أنشئ فرعًا مخصصًا مثل:

`micro-standard-v2-foundation-development`

احتفظ بنسخة baseline وrollback قبل أي تغيير. لا تنفذ bulk file moves أو إعادة تنظيم مجلدات أو تغييرًا معماريًا غير مطلوب. إذا ظهر أن التنفيذ يحتاج structural refactoring أو تغييرًا خارج نطاق الحزمة، توقف وسجله بدل تنفيذه.

بعد كل موجة:

1. شغّل فحوص التحقق المناسبة.
2. راجع `git diff --stat` و`git diff --check` و`git status`.
3. سجّل الملفات المتغيرة وhashes والاختبارات والقيود.
4. أنشئ تقرير موجة مستقلًا.
5. توقف ولا تنتقل إلى الموجة التالية حتى موافقة المالك الصريحة.

لا ترفع إلى `main` ولا تفتح Pull Request ولا تدمج أي فرع دون موافقة لاحقة.

## 6. Wave 0 — حماية وتثبيت baseline فقط

ابدأ بـWave 0 ولا تنفذ Wave A في نفس التشغيل.

Wave 0 لا تغيّر محتوى أي ملف داخل `micro-standard-v2/`. نفّذ فقط ما يلي في مساحة staging/rollback خارج الحزمة المنشورة:

- جرد الملفات الفعلية.
- تثبيت قائمة 29 ملفًا أساسيًا + ملفي metadata.
- حساب SHA-256 لكل ملف.
- إنشاء `file-boundary register` يوضح دور كل ملف وحدود تغييره.
- إنشاء `rollback manifest` ونسخة baseline كاملة خارج الحزمة.
- التحقق أن الحزمة بقيت دون تغير في المحتوى.

يجب تسليم:

- `WAVE_0_BASELINE_REPORT.md`
- `WAVE_0_BASELINE_MANIFEST.json`
- نسخة baseline/rollback في مجلد تسليم منفصل.

بعد ذلك توقف وانتظر مراجعة المالك. لا تبدأ Wave A تلقائيًا.

## 7. Wave A — العقود الأساسية

لا تبدأها إلا بعد موافقة المالك على نتيجة Wave 0.

حدّث فقط العقود والإرشادات اللازمة للعناصر التالية:

- `Metric/Balance` مع label وvalue وcontext وperiod وcomparison الاختياري وunknown.
- `Parts/Whole Relation` بصيغة عرض محايدة.
- `OperationalRow` مع title وmeta وstatus وamount وaction وfixed amount slot.
- `Lifecycle State` للحالات pending وunknown وretry وresult دون نجاح زائف.
- `Period/DateRange` بصيغة بصرية شهرية/أسبوعية/يومية/مخصصة دون فرض timezone أو owner-day.
- أمثلة typography وamount وdate وstatus وbidi isolation.
- قواعد accessibility للحالات والبدائل النصية.

الملفات الأساسية المستهدفة هي:

`component-contracts.md`, `data-display-system.md`, `component-states.md`, `empty-loading-error-states.md`, `input-system.md`, `motion-interaction.md`, `typography.md`, `accessibility.md`.

لا تنفذ في Wave A:

- `PermissionState` أو `ToolResult` كعقود نهائية دون قرار المالك.
- semantics نهائية لـ`partial`, `due`, `overdue`, `posted`, `reversed` إذا لم تكن معتمدة.
- أي formula أو policy أو product copy غير معتمد.

معيار Wave A: كل عقد يذكر slots وstates وRTL و100%/130%/200% و320/360/390/430 وaccessibility وSemantic ownership وDo not infer، وتبقى الحزمة بلا منطق Micro.

بعد التحقق، سلّم تقرير Wave A وتوقف.

## 8. Wave B — وصفات التكوين وعقد SimpleChart

لا تبدأها إلا بعد موافقة المالك على Wave A.

حدّث:

`surface-system.md`, `spacing-radius-elevation.md`, `visual-direction.md`, `color-system.md`, `button-system.md`, `overlay-system.md`, `navigation-shell.md`, `iconography.md`, `component-contracts.md`, `data-display-system.md`, `accessibility.md`.

أضف وصفات واضحة لاختيار:

- Row للبيانات المتكررة.
- Surface للتجميع الهادئ.
- Card فقط لملخص أو قرار ذي حدود واضحة.
- Sheet لإجراء أو تفاصيل مؤقتة مع الحفاظ على السياق.

أضف `Question-led SimpleChart` كعقد بصري محدود فقط، ويشمل:

- سؤال الرسم أو عنوانه الوظيفي.
- primary/secondary series عند الحاجة.
- zero وno-data وempty وloading.
- legend أو interpretation مختصر.
- text alternative.
- الأدوار الحالية فقط، دون ألوان جديدة.
- Semantic ownership وDo not infer.

لا تضف report logic أو formula أو source أو KPI policy أو Chart implementation متقدم.

معيار Wave B: لكل container use وanti-use، وكل chart يجيب سؤالًا واضحًا وله بديل نصي وحالات صادقة، دون تغيير القيم البصرية الحالية.

بعد التحقق، سلّم تقرير Wave B وتوقف.

## 9. Wave C — عينات المعرض فقط

لا تبدأها إلا بعد موافقة المالك على Wave B.

عدّل تركيبيًا فقط:

`component-gallery.html`, `component-gallery.css`, `component-gallery.js`, `coverage-matrix.json`.

أضف:

**خمس عينات تركيبية أساسية:**

1. Metric مع label وcontext وperiod.
2. Parts/Whole Relation مع بديل نصي.
3. OperationalRow طويل الاسم والـmeta والحالة والمبلغ.
4. Lifecycle من unknown/pending/retry دون نجاح زائف.
5. Container Choice يوضح Row/Surface/Card/Sheet مع use وanti-use.

وأضف **عينة SimpleChart مستقلة**، لأن لها متطلبات no-data وzero وtext alternative مختلفة.

تفاعل JavaScript يقتصر على فحص الحالات والعرض، ولا يحتوي routes أو writes أو formulas أو business actions.

### فحوص Wave C الإلزامية

اختبر العينات عند:

- 100% baseline.
- 130% practical stress.
- 200% maximum inspection.
- 320px و360px و390px و430px.
- RTL.
- Reduced Motion.
- Focus وcontrast وno horizontal overflow.
- النص العربي الطويل والأرقام الإنجليزية والعزل الرقمي.

لا تدّعِ اختبار جهاز Samsung فعلي أو قارئ شاشة فعلي إذا لم يُجرَ الاختبار بالفعل.

معيار القبول: كل عينة قابلة للمسح، لا يوجد تداخل أو clipping، amount slot ثابت، الحالة لا تعتمد على اللون، والـgallery لا تتحول إلى شاشة Micro أو نسخة من Accounting.

بعد التحقق، سلّم لقطات/سجل فحص وتقرير Wave C وتوقف.

## 10. Wave D — التحقق والتوثيق والإصدار فقط

لا تبدأها إلا بعد موافقة المالك على Wave C.

في Wave D فقط حدّث:

`verification-report.md`, `README.md`, `RELEASE.md`, `MANIFEST.json`, `source-inventory.md`, `self-critique.md`, `decision-log.md`.

لا تغيّر `component-gallery.html/css/js` في Wave D. هذه الملفات تدخل كمدخلات تحقق فقط.

وثّق:

- نتائج 100%/130%/200%.
- نتائج 320/360/390/430 وRTL وReduced Motion وcontrast وno-overflow.
- ما تم اختباره وما لم يتم اختباره.
- روابط العقود بالعينات.
- حدود Micro Product وFoundation.
- قرار الجاهزية أو عدم الجاهزية.
- 29+2 inventory وhash reference فقط.

لا تعلن الإصدار جاهزًا للتركيب داخل Micro إلا بعد اجتياز كل بوابات Wave D ومراجعة المالك.

## 11. التسليم الإلزامي في كل موجة

لكل موجة سلّم:

- تقريرًا باسم واضح يذكر الموجة والحالة.
- قائمة الملفات المتغيرة.
- diff summary.
- نتائج الاختبارات.
- hashes عند الحاجة.
- ما لم يتم اختباره.
- المخاطر المتبقية.
- rollback boundary.
- قرارًا صريحًا: `PASS / PASS WITH LIMITATIONS / BLOCKED`.

## 12. قاعدة التوقف النهائية

توقف فورًا إذا:

- ظهر تعارض بين الحزمة الحالية وقرار المالك.
- احتجت إلى تغيير لون أو خلفية أو typography base.
- احتجت إلى إدخال منطق Micro أو policy مالية.
- احتجت إلى نقل ملفات أو إعادة تنظيم بنية المستودع.
- أصبح المعرض Prototype منتجًا.
- لم تستطع إثبات الاختبار عند 100% أو 130% أو 200% أو مقاسات الهاتف المطلوبة.
- احتجت إلى ادعاء اختبار جهاز فعلي أو قارئ شاشة دون دليل.

**ابدأ بـWave 0 فقط. سلّم نتيجة Wave 0 وتوقف حتى يراجعها المالك.**
