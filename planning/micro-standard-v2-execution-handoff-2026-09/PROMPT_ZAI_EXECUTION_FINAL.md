# Prompt تنفيذ Micro Standard v2 عبر ZAI Flash

## 0. طبيعة المهمة

أنت تعمل بصفتك **قائد تنفيذ بصري وتقني منضبط** لحزمة Micro Standard v2. هذه ليست مراجعة نظرية قصيرة، وليست مراجعة كود عامة، وليست إعادة بناء Micro. المطلوب هو قراءة الحزمة الحالية كاملة، تنفيذ الدلتا المعتمدة فقط داخل Standard، التحقق منها بموجات واضحة، ثم إنشاء Prototype HTML تفاعلي مستقل يعرض كل التغييرات للمراجعة البصرية التقريبية، ورفع كل المخرجات إلى مستودع Documents وفق سياسة الرفع أدناه.

لا تتخذ قرارات لونية بديلة من عندك. لا تعُد إلى Palette قديمة. لا تنقل أنماطًا أو كودًا من Accounting. لا تعتبر Brand Book أو تقرير ZAI قرارًا أعلى من قرارات المالك المثبتة في هذا النص وفي مجلد handoff.

## 1. مصادر العمل ونقطة الحقيقة

المستودع:

`https://github.com/Qays7753/Documents`

حزمة Standard الحالية:

`https://github.com/Qays7753/Documents/tree/main/micro-standard-v2`

نقطة `main` المؤكدة وقت إعداد الأمر:

`dfa8bf7d7f7a2c01f256d4c77d359c8a5770d60b`

مجلد handoff الحالي:

`https://github.com/Qays7753/Documents/tree/micro-standard-v2-zai-execution-handoff-20260913/planning/micro-standard-v2-execution-handoff-2026-09`

اقرأ قبل لمس أي ملف:

1. `README.md`
2. `OWNER_APPROVED_DECISIONS.md`
3. `EXECUTION_PROCEDURE.md`
4. `GITHUB_UPLOAD_POLICY.md`
5. `PREVIOUS_WAVE_BOUNDARIES.md`
6. `REFERENCE_INDEX.md`

ثم اقرأ كل الملفات الحالية داخل `micro-standard-v2/`. الحزمة الحالية هي 29 ملفًا أساسيًا + `MANIFEST.json` + `RELEASE.md` = 31 ملفًا.

استخدم تقرير `MICRO_STANDARD_COMPREHENSIVE_UIUX_REVIEW.md` كدليل تشخيصي بعد فحص الملفات الحالية بنفسك. استخدم Brand Book وحزمة الأصول لفهم العلامة والشعار فقط، وليس لتحويل كل ألوان الشعار إلى UI tokens. استخدم Prototype v0 كدليل مشاكل تركيبية فقط، ولا تنسخه ولا تنقله إلى Micro.

لا تستخدم branch أو commit تاريخيًا غير منشور مثل `micro-standard-v2-foundation-development` أو `f64e8616...` كمصدر عمل. يجب أن تبدأ من `main` الحالي الذي تتحقق منه وقت التنفيذ.

## 2. النتيجة المطلوبة

يجب أن تنتج المهمة أربعة أنواع من النتائج:

1. **تطوير مضبوط لحزمة Standard الحالية**، مع تعديل الملفات التي تحتاج تعديلًا فعليًا فقط بعد قراءة الـ29 ملفًا كلها.
2. **تقرير كامل للتنفيذ** يوضح لكل ملف من الـ29: لم يتغير، تغير، سبب التغيير، الموجة، والاختبارات المرتبطة به.
3. **Prototype HTML تفاعلي مستقل** بعد اكتمال وتحقق Standard، يعرض جميع التغييرات البصرية التي تم تنفيذها.
4. **رفع سحابي كامل** لكل الملفات والتقارير والـPrototype إلى Documents، مع رابط الفرع والـcommit والـrun folder وhashes ودليل أن `main` لم يتغير.

لا يعني نطاق الـ29 أن تعدل كل ملف. اقرأ كل الملفات، ثم عدّل الدلتا فقط. ممنوع التعديل الشامل لمجرد توحيد الأسلوب.

## 3. قرارات الهوية والألوان — غير قابلة لإعادة التفاوض

احفظ الاتجاه الحالي كما هو: Light-only، warm light surfaces، عربي RTL، phone-first، أرقام إنجليزية مع numeric bidi isolation، وضوح من النظرة الأولى، وطبقات دافئة منضبطة.

| اللون | الدور المسموح | ممنوع استخدامه في |
|---|---|---|
| `#D97757` | هوية Micro، إنشاء، إضافة، FAB | القيم المالية، chart fills، status، ربح/خسارة، ملء البطاقات أو الشاشات |
| `#C96442` | selected/current/pressed edge، underline، وحافة الاختيار | تعبئة كل الأزرار، success/error، ربح/خسارة |
| `#141413` | القيمة المالية الأساسية، الالتزام الواضح، الاعتماد الكبير، والخطر المبرر | خلفية افتراضية لكل العناصر، الزخرفة، chart شامل |
| `#F5F4ED` | Warm Tint للحفظ والتأكيد العادي | لا يُعامل كدليل نجاح مالي وحده |
| الألوان الدلالية الحالية | success/error/info/pending/review/status | لا تستبدل بألوان الهوية ولا تعتمد على اللون وحده |

### عقود الإجراءات

**إنشاء/إضافة:** استخدم `#D97757` في FAB أو زر إنشاء واضح. لا يحمل قيمة مالية ولا يصبح لونًا عامًا لكل الالتزامات.

**حفظ/تأكيد عادي:** لا تستخدم surface أسود ممتلئًا. استخدم Warm Tint الحالي `#F5F4ED` مع نص وأيقونة `#141413`. عند الضغط يظهر edge واضح من `#C96442`. لا يتحول الزر إلى success قبل أو بمجرد الضغط. بعد نجاح فعلي، تظهر كلمة نجاح وعلامة دلالية، ولا يعتمد الإثبات على اللون وحده.

**اعتماد كبير/حذف نهائي/تعديل عالي العواقب:** استخدم `#141413` كسطح ممتلئ عند الحاجة إلى لحظة توقف واضحة، مع نص أبيض، وكلمة تصف النتيجة، ورمز مناسب، وشرح مختصر للعاقبة، ومسار تأكيد مستقل.

### قرارات مرفوضة

لا تدخل `#964E33` أو `#5F3120` إلى Tokens أو أزرار أساسية. لا تستخدم `#B79C86` أو `#8C7A66` كألوان واجهة؛ هما من مرجع الشعار فقط. لا تضف Palette جديدة. لا تعتمد Teal جديدًا في هذه المهمة. لا تفتح Dark Mode. لا تعيد Terracotta إلى لون بيانات أو نجاح أو خسارة.

## 4. الفصل بين Standard وMicro

Standard يملك الشكل والـtokens والعقود والـslots والحالات المرئية وقواعد التركيب المحايدة. Micro يملك data وmeaning وformula وpolicy وpermissions وroutes وsync وposting/reversal وقرار متى تظهر الحالة.

ممنوع إدخال formulas أو مصادر بيانات أو سياسات محاسبية أو ضرائب أو posting/reversal أو صلاحيات أو auth أو sync أو conflict resolution أو delivery behavior داخل Standard أو Prototype.

## 5. الوكلاء الفرعيون الخمسة

استخدم خمسة وكلاء فرعيين متكاملين. يمكنهم تحليل المصادر بالتوازي، لكن لا يسمح لأي وكيل فرعي بكتابة تغييرات متعارضة مباشرة. الوكيل الرئيسي يدمج الخطة ويملك القرار التنفيذي.

### الوكيل 1 — Source and Boundary Auditor

يتحقق من `main` الحالي، يجرد الـ31 ملفًا، يقارن الملفات الحالية بالتقارير التاريخية، يحدد ما هو موجود فعلًا، ويمنع تكرار موجات سابقة أو استخدام branch غير منشور. يسلم source map وboundary map قبل أي تعديل.

### الوكيل 2 — Contracts and Token Truthing

يفحص `design-tokens.css` و`design-tokens.json` و`color-system.md` و`button-system.md` و`component-contracts.md` وملفات الحالات والوصول. يحدد أقل تغييرات لازمة لتثبيت الفرق بين الإنشاء، الحفظ العادي، الالتزام العالي، الخطر، success، error، pending، unknown، وreview، دون إضافة قيم لونية جديدة.

### الوكيل 3 — Gallery and Composition Implementer

يفحص ويحدث Gallery والعينات المحايدة فقط. يثبت أن Warm-Ink لا يملأ كل شيء، وأن الحفظ العادي Warm Tint، وأن Terracotta للإنشاء، وأن selected/current له إشارة واضحة، وأن الرسوم لا تصبح سوداء أو Terracotta بالكامل. يمنع تحويل Gallery إلى Micro product أو Accounting copy.

### الوكيل 4 — Interactive Prototype Builder

لا يبدأ قبل اكتمال وتحقق Standard. يبني Prototype HTML مستقلًا يستهلك tokens والعقود النهائية، ويعرض كل التغييرات والتفاعلات المطلوبة دون منطق منتج أو بيانات حقيقية أو routes إنتاجية.

### الوكيل 5 — QA, Accessibility, Responsive and Upload Auditor

يفحص التباين والـfocus والـpressed والـdisabled والـloading والـreduced motion وRTL والتكبير والـoverflow، ويراجع أن كل حالة لا تعتمد على اللون وحده. يتحقق من hashes والملفات والرفع إلى GitHub، ولا يسمح بإعلان النجاح قبل اكتمال upload proof.

## 6. التسلسل التنفيذي الإلزامي

### Wave 0 — Baseline وRollback

أنشئ فرع عمل جديدًا من `main` الحالي. لا تعدل محتوى `micro-standard-v2/` في هذه الموجة. أنشئ جردًا للـ29 + metadata، نسخة baseline كاملة، نسخة rollback كاملة، hashes، file-boundary register، وWave 0 report.

تحقق من أن `main` لم يتغير. توقف إذا لم تستطع إثبات نقطة البداية أو rollback.

### Wave A — Contracts and Token Truthing

بعد نجاح Wave 0، عدّل فقط العقود والـtokens التي تحتاجها الدلتا. يجب أن تصبح أدوار الإجراءات قابلة للتنفيذ، لا مجرد وصف عام:

- create/add/FAB؛
- ordinary save/confirm؛
- pressed save؛
- high-consequence commit/destructive confirmation؛
- success/error/pending/unknown/review؛
- amount/value/context/period/slot؛
- color independence and non-color signals.

لا تضف لونًا خامًا جديدًا. إذا احتجت semantic alias، اربطه بقيمة حالية موجودة ولا تخترع hex جديدًا. لا تغير Light Mode أو RTL أو numeric isolation أو geometry الأساسية دون دليل اختبار واضح.

سلّم diff وreport وhashes وtests وrollback boundary. إذا فشلت البوابة، توقف.

### Wave B — Gallery and Component Composition

بعد نجاح Wave A، حدّث العينات اللازمة داخل `component-gallery.html` و`component-gallery.css` و`component-gallery.js` والملفات المرتبطة فقط. يجب أن تظهر على الأقل:

- FAB/إنشاء بـ`#D97757`؛
- ordinary save/confirm بـWarm Tint `#F5F4ED` ونص/أيقونة `#141413`؛
- pressed save مع edge `#C96442`؛
- high-consequence/destructive confirmation بـ`#141413`؛
- primary values واضحة دون أسطح سوداء كثيرة؛
- selected/current والـsegments والـchips دون تعبئة سوداء تلقائية؛
- success/error/pending/unknown/review بلون دلالي وكلمة وشكل؛
- row/metric/value/period/amount slots؛
- chart question-led مع no-data وzero وloading وtext alternative؛
- sheets/dialogs والـbottom navigation والـoverflow إذا كانت ضمن العقد الحالية.

لا تضف routes أو writes أو formulas أو business actions. نفّذ التفاعل المحلي الضروري للعرض فقط.

### Wave C — Verification and Documentation

بعد نجاح A وB، حدّث الوثائق والـmanifest وverification فقط حسب الملفات المتغيرة فعلًا. وثّق ما تغير وما لم يتغير، واربط العقود بالعينات، وميز بين اختبار browser/local وأي اختبار device فعلي.

### Wave P — Interactive HTML Prototype

بعد اكتمال Standard والتحقق منه، أنشئ Prototype HTML مستقلًا تحت run folder، وليس داخل `micro-standard-v2/`.

يجب أن يغطي Prototype كل تغيير بصري تم تنفيذه، وليس شاشة واحدة مختصرة فقط. الحد الأدنى للمشاهد:

1. شاشة/مشهد إنشاء وإضافة وFAB.
2. مشهد ordinary save/confirm مع Warm Tint.
3. مشهد pressed وloading وquiet completion.
4. مشهد high-consequence confirmation والحذف النهائي.
5. مشهد قيمة مالية مع context وperiod وcurrency slot.
6. مشهد OperationalRow مع amount slot وstatus وoverflow.
7. مشهد selected/current وsegments/chips.
8. مشهد success/error/pending/unknown/review مع كلمة ورمز وشكل.
9. مشهد chart question-led مع zero/no-data/loading وtext alternative.
10. مشهد sheet/dialog وbottom navigation وoverflow عند الحاجة.

التفاعل المطلوب محلي فقط: الضغط، تبديل الحالة، فتح وإغلاق sheet/dialog، loading، quiet completion، وتغيير period أو state illustrative. لا data source حقيقي، لا formula، لا posting، لا write، لا routes إنتاجية، ولا اعتماد على remote assets.

يجب أن يكون Prototype عربي RTL، يعمل في 320/360/390/430px، ويمكن فحصه عند 100/130/200%، ويحترم reduced motion، ولا يحتوي horizontal overflow. يجب أن يرفق:

- ملف HTML قابل للتحميل؛
- CSS/JS محليان عند الحاجة؛
- `PROTOTYPE_README.md`؛
- `PROTOTYPE_COVERAGE.md` يربط كل مشهد بملف Standard والعقد الذي يمثله؛
- `PROTOTYPE_VALIDATION.md` يذكر الاختبارات والقيود؛
- لقطات للمشاهد الرئيسية عند الإمكان.

أي مشكلة تظهر في Prototype تسجل كمشكلة تركيبية مستقلة أولًا. لا تعدل Standard تلقائيًا بسبب Prototype.

## 7. الاختبارات الإلزامية

بعد كل Wave وبعد Prototype، نفذ ما ينطبق من الاختبارات التالية:

- `git diff --check`؛
- JSON parse وmanifest consistency؛
- file inventory وchanged-file proof؛
- 320/360/390/430px؛
- RTL والعربية والأرقام الإنجليزية وnumeric bidi isolation؛
- 100/130/200%؛
- focus/pressed/disabled/loading/quiet completion؛
- reduced motion؛
- contrast للحدود والنصوص والأسطح؛
- no horizontal overflow؛
- FAB لا يغطي amount column؛
- لا تظهر أسطح Warm-Ink كثيرة بلا مبرر داخل viewport واحد؛
- الحالات لا تعتمد على اللون وحده؛
- charts لا تصبح سوداء بالكامل ولا Terracotta بالكامل؛
- لا تدّعِ physical Samsung أو screen-reader testing إذا لم يُنفذ فعليًا.

يجب أن يخرج كل Wave بحالة صريحة: `PASS` أو `PASS WITH LIMITATIONS` أو `BLOCKED`.

## 8. قواعد التوقف الصارمة

توقف فورًا وسجل السبب إذا:

- احتجت إلى تغيير `#D97757` أو `#C96442` أو `#141413` أو الأسطح الأساسية؛
- احتجت إلى إضافة لون جديد؛
- ظهر تعارض بين قرار المالك وBrand Book أو تقرير ZAI؛
- احتجت إلى Dark Mode؛
- احتجت إلى Micro logic أو policy أو formulas؛
- احتجت إلى bulk file moves أو structural refactoring؛
- لم تستطع إثبات rollback؛
- لم تستطع إثبات أن `main` لم يتغير؛
- فشل Prototype في تمثيل تغييرات Standard؛
- فشل الرفع إلى GitHub.

إذا ظهر structural refactoring أو bulk file moves، لا تنفذه. ابدأ أولًا Structure/Architecture/Code Organization Scan read-only، ثم توقف لمراجعة المالك.

## 9. GitHub والرفع السحابي

اقرأ `GITHUB_UPLOAD_POLICY.md` واتبعها حرفيًا.

القيم التي سيملؤها المستخدم يدويًا:

```text
GITHUB_REPOSITORY: https://github.com/Qays7753/Documents
GITHUB_ACCESS_TOKEN: <USER_WILL_PASTE_A_SHORT_LIVED_RESTRICTED_TOKEN_HERE>
TARGET_BASE_BRANCH: main
TARGET_WORK_BRANCH: micro-standard-v2-execution-20260913
RUN_ID: <CREATE_A_UNIQUE_RUN_ID>
```

لا تطبع التوكن، ولا تكتبه في الملفات، ولا تضعه في screenshots أو reports، ولا تعيده في المحادثة. لا ترفع إلى `main`، لا force-push، لا delete branch، لا change repository settings، ولا merge أو open pull request.

ارفع المخرجات تحت:

`planning/micro-standard-v2-execution-handoff-2026-09/runs/<RUN_ID>/`

وارفع Prototype تحت:

`planning/micro-standard-v2-execution-handoff-2026-09/runs/<RUN_ID>/prototype-v0.1/`

يجب رفع كل Wave report وchanged-file list وdiff summary وhashes وtests وlimitations وrollback boundary. في النهاية ارفع:

- نسخة Standard النهائية أو patch كامل قابل للتطبيق؛
- Prototype HTML وCSS/JS وREADME/COVERAGE/VALIDATION؛
- `FINAL_RUN_MANIFEST.json`؛
- `FINAL_RUN_README.md`؛
- صور المشاهد الرئيسية عند الإمكان.

بعد الرفع أعد في المحادثة وفي `FINAL_RUN_README.md` رابط المستودع، اسم الفرع، commit SHA، run folder، inventory، حالة main، وحالة token exposure. إذا فشل الرفع، لا تدّعِ اكتمال المهمة؛ اذكر الفشل وقدم الملفات كحل بديل.

## 10. شكل التقرير النهائي

أعد التقرير كاملًا داخل نص المحادثة، وأرفقه كملف Markdown قابل للتحميل. يجب أن يحتوي على:

1. ملخص ما نُفذ.
2. نقطة البداية والـbaseline والـrollback.
3. جدول كل ملفات الـ29: changed/unchanged/deferred وسبب الحالة.
4. جدول الألوان والأدوار وما تم اختباره.
5. تفاصيل كل Wave وحالتها.
6. تفاصيل Prototype ومشاهد التغطية.
7. نتائج الاختبارات حسب المقاس والتكبير والحالة.
8. ما لم يُختبر فعليًا.
9. المشاكل المتبقية، مفصولة إلى Standard أو Prototype أو Micro composition.
10. الروابط والـcommit والـrun folder وhashes.
11. تأكيد صريح أن Micro وAccounting و`main` لم تتغير.
12. تأكيد صريح أن Access Token لم يُخزن أو يُكشف.

لا تعلن أن Standard جاهز للنقل إلى Micro إلا بعد تسليم Standard وPrototype ونجاح التحقق ومراجعة المالك.

## 11. أول رد مطلوب منك قبل التنفيذ

قبل أن تعدل أي ملف، أعد خطة preflight قصيرة داخل المحادثة تتضمن:

- commit وbranch اللذين قرأتهما؛
- جرد الـ31 ملفًا؛
- الملفات المتوقع تعديلها والملفات المتوقع عدم تعديلها؛
- خطة Waves؛
- خطة Prototype؛
- خطة الرفع؛
- أي تعارض أو غموض وجدته.

بعد تأكيد أن preflight مكتمل، ابدأ Wave 0 فقط. لا تنفذ التعديل قبل baseline وrollback. لا تخترع قرارًا غير موجود في هذا النص.
