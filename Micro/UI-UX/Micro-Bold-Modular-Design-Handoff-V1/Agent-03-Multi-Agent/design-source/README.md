# مصادر التصميم — قابلة لإعادة التوليد والتحقق

- `design/` — ملفات CSS الثلاثة + screen.js (المصدر الوحيد للأنماط؛ النموذج يُبنى منها)
- `build/` — مولدات الشاشات والأساسات والفهرس والاتجاه الموصى به والـPDF (fixtures.py = المصدر الوحيد للتجهيزات المقفلة)
- `contrast_check.py` — قياس WCAG لكل الأزواج (ALL PAIRS PASS)
- `qa_checks.py` — 97 فحصًا آليًا عبر متصفح لا-رأسي
- `capture_evidence.sh` — التقاط الأدلة المنهجية
- `fix_round2_css.py` — سجل إصلاحات الجولة 2 قابل لإعادة التشغيل

إعادة البناء: `python3 design-source/build/build_screens.py` (يقرأ من مجلد design-source، ويكتب في prototype — المسارات داخلية).
