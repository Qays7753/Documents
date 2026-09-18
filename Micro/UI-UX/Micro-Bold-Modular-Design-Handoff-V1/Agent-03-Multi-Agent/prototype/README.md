# Micro Bold Modular — النموذج التفاعلي (Agent-03 Multi-Agent)

نموذج تصميمي تفاعلي ثابت (Static HTML/CSS/JS) بدون خادم ولا بيانات حقيقية — عربي RTL بالكامل.

## التشغيل (خطوة واحدة)

افتح `index.html` في أي متصفح حديث مباشرة (نقر مزدوج — يعمل من `file://` دون أي تثبيت أو إنترنت؛ الخطوط والأيقونات مضمّنة محليًا).

أو من الطرفية:

```bash
cd agent-runs/agent-03-multi-agent/prototype
python3 -m http.server 8080   # اختياري — ثم افتح http://localhost:8080
```

## البنية

- `index.html` — مركز التحكم: الاتجاهات الثلاثة، المقارنة، الاتجاه الموصى به، وحزمة الفحص (QA Harness).
- `compare/` — مقارنة الاتجاهات جنبًا إلى جنب (نفس الشاشة/الحالة/الوضع).
- `c1-warm-bold/` / `c2-confident-bold/` / `c3-dynamic-modular/` — تسع شاشات لكل اتجاه + `screen.css` مستقل تمامًا + `screen.js`. **لا تُشارك أي أنماط بين الاتجاهات.**
- `selected-direction/` — الاتجاه الموصى به بعد التطوير + `design-system.html` (نظام التصميم المرشّح).
- `assets/fonts/` — IBM Plex Sans Arabic محليًا (woff2) — أرقام موحدة العرض (tabular) افتراضيًا.

## الشاشات في كل اتجاه

home (4 حالات: موجبة/غير مكتملة/سالبة/فارغة + قائمة الشعار) · work · finance · tools (فيها الوضع الليلي) · market · products · order (طلب متأخر) · sale (نموذج/تحقق/نجاح/خطأ نظام) · more.

## روابط عميقة (كل فحص قابل للتكرار)

```
screen.html?state=positive|incomplete|negative|empty|form|validation|success|system-error
          &theme=light|dark   &zoom=200   &motion=reduce   &sheet=menu
```

أمثلة:
- `c1-warm-bold/home.html?state=incomplete&theme=dark`
- `c3-dynamic-modular/sale.html?state=success`
- `c2-confident-bold/home.html?zoom=200&motion=reduce`

## حدود النموذج (تصنيف صادق)

- نطاق التصميم: مسار «سجّل بيعًا» كامل؛ نماذج مصروف/طلب/تحصيل وسجلات تفصيلية وAsk Micro والنقل والتوصيل خارج النطاق وتفتح ورقة تصنّف نفسها بصدق.
- «عرض العملية» و«كل السجل» تفتح ورقة توضيحية لا شاشة كاملة (خارج النطاق).
- قيم مساندة غير محددة في التجهيزات (حالة C المساندة، عملاء العرض) مركّبة من الـOrchestrator وموثّقة في rationale — لا تمس أي قيمة مقفلة.
- الطلب المتأخر: «حدّث حالة الطلب» يقدّم المرحلة في سكة الطلبات كعرض توضيحي للحالة، ويعود بالتحديث عند إعادة التحميل.

## محاكاة الأعراض والفحص

- **320/390/430px:** من حزمة الفحص في `index.html` أو صفحة المقارنة (iframe معزول).
- **الوضع الليلي:** من أدواتي ← الإعدادات (المسار الرسمي — IA-D04)، أو `?theme=dark` من حزمة الفحص.
- **تكبير 200%:** `?zoom=200` (كل النصوص بـrem).
- **الحركة المخفَّضة:** `?motion=reduce` أو تفعيل prefers-reduced-motion في النظام.
