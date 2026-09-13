# Micro Standard v2 — ZAI Execution Handoff

هذه الحزمة هي **مصدر handoff الحالي الوحيد** لمرحلة تنفيذ Micro Standard v2 عبر ZAI. الغرض منها توحيد نقطة القراءة والقرارات والحدود، ومنع التقاط ملفات تاريخية أو قرارات ملغاة بالخطأ.

## نقطة الحقيقة التنفيذية

يقرأ المنفذ حزمة `micro-standard-v2/` من فرع التطوير الذي سيُنشأ من `main` الحالي في مستودع `Qays7753/Documents`.

النقطة المؤكدة وقت إعداد هذه الحزمة:

- Repository: `https://github.com/Qays7753/Documents`
- Branch baseline: `main`
- Main commit: `dfa8bf7d7f7a2c01f256d4c77d359c8a5770d60b`
- Package path: `micro-standard-v2/`
- Package inventory: 29 core files + `MANIFEST.json` + `RELEASE.md` = 31 files
- Execution branch: ينشئ المنفذ فرعًا جديدًا من `main` ولا يعمل على `main`.

## ترتيب سلطة المصادر

1. `micro-standard-v2/` الحالي من نقطة `main`.
2. `OWNER_APPROVED_DECISIONS.md` في هذه الحزمة.
3. `EXECUTION_PROCEDURE.md` في هذه الحزمة.
4. تقرير ZAI Flash المرفق في `reference/zai-review/` كدليل وتحليل، لا كقرارات تلقائية.
5. Brand Book والأصول في `reference/brand-assets/` كمرجع للعلامة فقط، لا كمصدر تلقائي لأدوار UI.
6. Prototype v0 في `reference/prototype-v0/` كدليل تركيب فقط، وليس مصدر حقيقة ولا مادة نقل إلى Micro.

## ما لا يجوز اعتباره مصدرًا

لا تستخدم أي ملف خارج هذه الحزمة أو داخل `reference/history/` كمصدر قرار. لا تعُد إلى branch أو commit تاريخي غير منشور، ولا تلتقط قيمًا من اقتراحات قديمة. لا ترفع أي قرار أقدم أو ملغى إلى التنفيذ.

## حدود التنفيذ

هذه الحزمة مخصصة لتطوير Standard فقط. لا تعديل على Micro أو Accounting، ولا منطق منتج، ولا formulas، ولا data sources، ولا posting/reversal، ولا sync، ولا permissions، ولا delivery behavior، ولا Dark Mode، ولا bulk file moves أو structural refactoring.

إذا ظهر احتياج إلى إعادة تنظيم بنية أو نقل ملفات جماعي، يتوقف المنفذ قبل التنفيذ وتبدأ بوابة Structure/Architecture/Code Organization Scan read-only وفق تعليمات المشروع.

## التسلسل

يبدأ المنفذ بـWave 0 baseline وrollback، ثم ينفذ الموجات المعتمدة واحدةً واحدة، ويوقف العمل بعد كل موجة لتسليم diff وhashes والاختبارات والقيود. لا Push أو Merge إلى `main` قبل موافقة المالك.
