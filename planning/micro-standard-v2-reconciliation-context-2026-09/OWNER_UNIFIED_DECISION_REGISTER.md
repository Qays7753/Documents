# Micro Unified Decision Register v1

## الهدف

هذا السجل يوحّد قرارات تقريرَي ZAI 5.3 وZAI 5.3 Flash، ويحدد ما يجب تثبيته داخل Micro Standard v2 وما يجب أن يبقى تنفيذًا أو معنىً داخل Micro. لا يبدأ أي تنفيذ قبل اعتماد هذا السجل.

## قاعدة القرار العليا

Micro Standard هو مصدر العقود البصرية العامة. Micro هو مصدر التنفيذ، المعنى، الكلمات، البيانات، السياسات، والأنماط التشغيلية الخاصة بالمنتج. ما هو قابل لإعادة الاستخدام عبر منتجات وشاشات متعددة يمكن أن يصبح عقدًا في Standard. ما يعتمد على معنى Micro أو بياناته أو مساراته يبقى في Micro.

## القرارات الموحدة

| المعرّف | القرار الموحد | ما يدخل الـ29 | ما يبقى في Micro | الحالة |
|---|---|---|---|---|
| U-01 Palette and mapping | اعتماد قيم Standard للأدوار المشتركة عبر Runtime Token Mapping، مع عدم حذف قيم Micro القديمة قبل اكتمال الاختبارات. | تثبيت أسماء الأدوار وقواعد عدم إدخال palette جديدة. لا نضيف قيم Micro الخاصة إلى الـ29 تلقائيًا. | `--vf-*` mapping، aliases، twins، dark mapping، وإزالة القيم القديمة لاحقًا بعد الاستقرار. | معتمد مبدئيًا، والتنفيذ يحتاج W0/W2 |
| U-02 Teal and Micro-only colors | لا يعود Teal لون هوية أو اختيار أو نجاح. الروابط تستخدم Ink ثانويًا مع underline حتى يعتمد link-ink مستقل. ألوان التحذير/السحب/الأدوار الخاصة لا تدخل Standard إلا إذا ثبت أنها عقد عامة. | توثيق أن link-ink غير معتمد وأن الألوان الخاصة امتدادات منتجية. | قرار كل role خاص، ثم mapping أو تقاعده داخل Micro. | معتمد |
| U-03 Dark Mode | نجهز Micro ليكون Dark-ready عبر semantic mapping وفصل tokens واختبارات parity، لكن لا نضيف Dark Mode إلى الـ29 ولا نفعّله ضمن أول دمج Light. | يبقى Standard Light-only؛ يضاف فقط توضيح أن Dark امتداد خارج الحزمة. | ThemeContext و`.dark` كطبقة مستقلة، feature flag، واختبارات Dark في موجة لاحقة. | معتمد |
| U-04 Type floor | 13px حد labels، و12px للـmetadata غير المالي فقط، والمبالغ والحقائق المالية لا تقل عن 15px. | تثبيت السلم العام وحدود الحقائق المالية. | تطبيق tokens تدريجيًا على Micro، دون mass rewrite. | معتمد |
| U-05 State words and markers | كلمات الحالات الحالية في Micro تبقى كما هي مبدئيًا. نضيف marker غير لوني وstate mapping مركزيًا. لا نعيد تسمية Micro تلقائيًا. | عقد عام للـword + marker + color، وعقد Knowledge States عام بلا كلمات منتجية مفروضة. | قاموس Micro الحالي، mapping الكلمات إلى الحالات، والهجاء بعد مراجعة سياقية. | معتمد |
| U-06 Row edge stripe | اعتماد marker وedge stripe اختياري بحد أقصى 3px، ودائمًا مع كلمة الحالة. | تثبيت Row slot وstripe contract. | Row primitive وتطبيقه تدريجيًا على الصفوف. | معتمد |
| U-07 Feedback | اعتماد inline/quiet feedback في Micro، وعدم إعادة Snackbar كافتراضي. Snackbar يبقى عقدًا اختياريًا غير مفعل. | إضافة variant يوضح أن inline completion بديل شرعي، ولا يُفرض Snackbar. | Notice/quiet completion وrole=status وreceipt/outcome cards. | معتمد |
| U-08 Period | الإبقاء على month input وquick ranges في Micro لأن semantics الفترة منتجية. يمكن دعم Period Chip كـvariant، وليس استبدالًا إلزاميًا. | توضيح variant في period contract. | `period-controls` وتقرير متى يستخدم chip أو native input. | معتمد |
| U-09 FAB and navigation | يبقى FAB Micro الحالي labeled/in-grid إذا اجتاز clearance والاختبارات. تبقى تسميات Micro الحالية: «مشروعي الآن / العمل / مالي / أدواتي»، و«سجّل» FAB لا وجهة خامسة. | توضيح أن Navigation labels وFAB geometry يمكن أن تكون product-owned variants. | BottomNav، route labels، FAB geometry، واختبارات route/chrome. | معتمد |
| U-10 Reader chrome | صفحة القراءة/التفاصيل = surface مع chrome، وصفحة التحرير/العملية = deep بلا chrome، بعد مراجعة الاستثناءات. | عقد route-kind/chrome behavior عام. | routeClassifier وقرار عائلة كل route، مع اختبارات. | معتمد |
| U-11 Knowledge States | نضيف عقدًا عامًا لحالات unconfirmed/unknown/incomplete/needs-review/estimated، دون فرض كلمات Micro أو معنى مالي جديد. | تعديل `component-states.md` و`component-contracts.md` بإضافة presentation contract فقط. | State adapter، كلمات Micro، ومنطق تحديد الحالة. | تعديل محدود مطلوب في الـ29 بعد اعتماد |
| U-12 Orthography | لا نعيد كتابة كلمات Micro الآن. نثبت قاموس Micro الحالي ونوثق الاختلافات، ثم نوحّد لاحقًا بعد مراجعة معنى كل سياق. | لا نثبت كلمات Micro داخل Standard؛ نضيف قاعدة أن الكلمات أمثلة/مملوكة للمنتج. | `activityLabels` والصفحات وtests. | معتمد |
| U-13 Icon implementation | لا نستبدل Lucide بالـ43-glyph registry دفعة واحدة. نستخدم Lucide مع mirror flags وقواعد RTL، ويظل Registry مرجعًا تعاقديًا. | توضيح icon role/mirror contract. | Icon adapter وقواعد الاستخدام والاختبارات. | معتمد |
| U-14 Page splitting | لا bulk refactor. كل صفحة كبيرة تفصل لاحقًا في موجة منفصلة بعد primitives، مع اختبار وrollback. | لا تعديل في الـ29. | Micro structure waves per page/family. | معتمد |
| U-15 Sort | لا نضيف sort لمجرد وجود gap. يؤجل حتى حاجة منتج واضحة على شاشة محددة. | لا تعديل. | Feature decision لاحق. | معتمد |
| U-16 Charts | لا تدخل الرسوم كمنطق أو بيانات إلى الـ29. نحتفظ بعقد chart floors: one question, data/zero/no-data/loading, text alternative. | العقد العام موجود؛ لا chart library ولا business questions. | أول chart question-led في Feature Pattern بعد قرار المنتج. | معتمد |
| U-17 Overlay vs in-flow | confirmation/deletion/high consequence = Dialog/Sheet؛ الشرح والتحرير المستمر = in-flow. لا نحول كل شيء إلى overlay. | توضيح composition guidance العام. | قرار كل surface؛ QuickAction and feature layers. | معتمد |
| U-18 Loading | نحافظ على honest text loading في البداية. Skeleton variant ممكن لاحقًا فقط حيث تكون البنية ثابتة وتثبت فائدته. | توضيح أن skeleton optional، وليس قبولًا عامًا لكل شاشة. | ScreenState and feature-specific loading. | معتمد |
| U-19 Documentation authority | Standard = visual contracts؛ Micro mapping = runtime implementation؛ Micro docs = guidance؛ domain/application/storage = meaning and persistence. | تعديل authority wording والـmanifest/README عند الحاجة. | docs sync guard وsource matrix. | معتمد |
| U-20 Micro feature patterns | نرفع إلى Standard العقود العامة للتركيب فقط، لا نرفع منطق Micro. تبقى correction lifecycle، decision cards، fact triad، integrity checks، scheduling، party ledger، forms protection كMicro-owned patterns. | يمكن إضافة pattern slots/guidance عامة إلى العقود، دون كلمات أو routes أو business policy. | `patterns/` وfeature modules وتفاصيل المنتج. | معتمد |

## ما يدخل تطوير الـ29 في Final Copy القادمة

### يدخل كعقود عامة قابلة لإعادة الاستخدام

1. Knowledge-state presentation contract: word/marker/tone/unknown boundary، بلا كلمات Micro الإلزامية.
2. Row marker and edge-stripe contract، مع non-color requirement.
3. AUX behavior addendum: route-kind chrome, keyboard-hide, safe areas, context suppression, transition row.
4. Period control variants: chip and native-input variant، مع بقاء time semantics خارج Standard.
5. Inline/quiet feedback variant، مع إبقاء Snackbar اختياريًا.
6. Overlay versus in-flow composition guidance.
7. Type floor clarification: 13px labels, 12px non-financial metadata, 15px financial facts.
8. Icon mirror/RTL adapter guidance، دون فرض مكتبة محددة.
9. Documentation authority and manifest count correction.
10. Guard/verification wording التي تمنع claims غير المنفذة.

### يبقى مثبتًا في الـ29 دون إعادة فتحه

Palette الحالية، Light-first، action ladder، save/create/commit roles، Warm-Ink boundaries، selection edge، state matrix core، honest void categories، value zone، row slots، period semantics boundary، overlay rules، RTL، English digits، bidi isolation، geometry، motion، accessibility، no new palette، Prototype boundary، and no business logic.

## ما لا يدخل الـ29

لا تدخل الكلمات الخاصة بـMicro، أسماء routes، «مشروعي الآن» كقيمة عالمية، QuickActionSheet sale/expense behavior، correction posting meaning، charts questions، sort decisions، calendar implementation، table anatomy الخاصة ببيانات Micro، domain formulas، storage behavior، sync، permissions، Dark Mode tokens، أو AI Assistant.

## خطة التنفيذ الموحدة بعد الاعتماد

| الموجة | الهدف | مكان العمل |
|---|---|---|
| W0 | اعتماد السجل وإنشاء mapping table وbaseline/rollback | Documents + Micro branch metadata، بلا سلوك |
| W1 | Guards وCSS hygiene وإصلاحات مؤكدة منخفضة الخطر: warn chip، dead tooltip، duplication، boundary guards | Micro فقط |
| W2 | Runtime Token Mapping وz/scrim aliases وpalette adoption بعد D-01 | Micro فقط، مع إبقاء aliases القديمة |
| W3 | Button/Status/Row/Amount/Field/Sheet/Dialog/ScreenState primitives مع pilot surfaces | Micro فقط |
| W4 | AUX stabilization وفصل QuickActionSheet عن Feature forms مع الحفاظ على drafts/idempotency | Micro فقط |
| W5 | Feature Patterns وscreen adoption: finance value-zone، periods، order rows، correction، scheduling، tools، filters | Micro فقط |
| W6 | Standard revision منفصلة، فقط للعقود العامة التي ثبتت فائدتها بعد التنفيذ | Documents/الـ29 |
| Dark future | Dark Mode مستقل بعد استقرار Light، لا يدخل W2 أو W3 | Micro فقط |

## بوابة عدم الضرر

لا يسمح أي موجة بما يلي: حذف Micro القديم قبل وجود mapping؛ نسخ كود Prototype؛ إدخال كلمات Micro في Standard كسياسة عامة؛ إدخال business meaning إلى primitive؛ تعديل domain/application/storage؛ bulk moves؛ تغيير مالي أو formula؛ إضافة hex جديد؛ تفعيل Dark Mode ضمن Light migration؛ أو دمج إلى `main` قبل اختبارات الموجة ومراجعة المالك.

## الحكم

نعم، يمكن جعل الـ29 أقوى وأكثر ثراءً، لكن ليس عبر نقل كل تفاصيل Micro إليها حرفيًا. الطريق الصحيح هو رفع **العقود العامة القابلة لإعادة الاستخدام** إلى الـ29، وإبقاء Micro-specific patterns داخل Micro مع توثيقها ومصادرها. بهذه الطريقة يصبح Standard أساسًا مستقبليًا حقيقيًا، ولا يتحول إلى نسخة Micro مقفلة أو يعيد مشاكل palette والخلط بين الهوية والمنتج.

لا يبدأ التنفيذ قبل اعتماد هذا السجل وReconciliation Brief مشتق منه.
