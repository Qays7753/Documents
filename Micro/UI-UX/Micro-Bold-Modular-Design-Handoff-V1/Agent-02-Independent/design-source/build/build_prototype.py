#!/usr/bin/env python3
"""
build_prototype.py — يولّد صفحات الاتجاهات من قالب واحد مشترك.
يضمن التطابق الحرفي للمحتوى بين C1/C2/C3 (قاعدة المقارنة العادلة)
مع اختلاف الهوية البصرية فقط (styles.css + tokens لكل اتجاه).
"""
import json, os, sys

BASE = "/home/z/my-project/repos/base/agent-runs/agent-02-independent"
sys.path.insert(0, "/home/z/my-project/scripts")

DIRS = {
    "c1-warm-bold": {
        "label": "C1 — Warm Bold",
        "title": "C1 — Warm Bold",
        "thesis": ("عائلة تيراكوتا/مرجانية حيوية تقود الهوية وتمنح طاقة البدء، فوق حياد دافئ "
                   "بلا غرق بيجي، مع ثقة زرقاء ثانوية منضبطة — دفء منزلي لا تنازل فيه عن "
                   "الجدية المالية."),
        "adjectives": ["دافئ", "حيوي", "قريب", "واضح", "جسور"],
        "mood": ("دفء المخابز المنزلية الأردنية دون رومانسية ريفية؛ طاقة سوق الشارع الصباحي؛ "
                 "لطف بصري بلا نعومة طفولية."),
        "blocklogic": ("حقل البطل هو الحقل المهيمن الوحيد ويأخذ لون الحالة (أخضر/أحمر/كهرماني) — "
                       "الكتل الأخرى أدعم وأهدأ: إشارات ناعمة للقسم الوظيفي، وحشو لوني مشبع فقط حول الأزرار الأولية."),
        "iconnote": "أساس Lucide بحد 2px، وزن أعلى قليلًا (2.1) في التنقل النشط والإجراءات.",
        "darknote": ("داكن قهوة إسبريسو مع تيراكوتا أفتح للوهج، وأخضر/أحمر معدلان للتباين على الأسطح الداكنة؛ "
                     "الحقل الداكن ليس انعكاسًا بل إعادة معايرة."),
        "strengths": [
            "قرب فوري من المستخدم المنزلي الأردني (دفء بلا ريفية).",
            "حقل الحالة الملون يجيب «كيف وضعي؟» في ثوانٍ.",
            "الأسقف الاستدارية تخفض رهبة الأدوات المالية.",
        ],
        "risks": [
            "خطر الانزلاق نحو جمالية توصيل الطعام/السوق الحرفي (يُراقب في التقييم).",
            "الدافئ الزائد قد يُضعف إحساس «نظام تشغيل جاد» في جلسات المالية الطويلة.",
            "فرضية أن التيراكوتا «أردني» تحتاج اختبار مستخدم حقيقي.",
        ],
        "hypotheses": "هل يقرأ المستخدم التيراكوتا كـ«علامتي» أم كـ«تنبيه»؟ يُختبر بالنقر والاستدعاء.",
        "swatch_roles": ["brand", "trust", "positive", "attention", "negative"],
    },
    "c2-confident-bold": {
        "label": "C2 — Confident Bold",
        "title": "C2 — Confident Bold",
        "thesis": ("أزرق-تيل عميق يحمل الثقة والسياق النشط، ولون علامة دافئ يحمل حصراً طاقة "
                   "الإنشاء والبدء، على كانفس محايد أنظف وأسطح بيضاء منضبطة — انضباط رقمي "
                   "معماري بلا برود بنكي."),
        "adjectives": ["واثق", "دقيق", "مضبوط", "معماري", "حي"],
        "mood": ("دقة العدة المالية المحمولة؛ وضوح اللوحات المعمارية؛ حسم أدوات الدفع الحديثة دون تقليد هوية أي منتج."),
        "blocklogic": ("شريط حالة معماري أعلى بطاقة النتيجة يعلن الحالة بلونها؛ خطوط بداية سميكة "
                       "(5px) تؤطر المعنى بدل ملء الشاشة؛ اللون الدافئ محجوز لأزرار الإنشاء."),
        "iconnote": "أساس Lucide بحد 2px حاد الأداء؛ النشط بحد 2.4 وحاوية نغمية تيل.",
        "darknote": ("ليل بترولي عميق مع تيل أفتح للسياق النشط، وتيراكوتا مضيئة لأزرار الإنشاء؛ "
                     "الأسطح ترتفع بالنغمية لا بالحدود الزائدة."),
        "strengths": [
            "أعلى انضباط رقمي: قراءة مالية مريحة في الجلسات الطويلة.",
            "فصل صارم بين أدوار الثقة/الإنشاء/الحالة يمنع الخلط.",
            "بنية معمارية تتوسع جيدًا إلى شاشات المستقبل (السوق والتوصيل).",
        ],
        "risks": [
            "خطر «واجهة مالية عالمية مصقولة» رغم التيل الدافئ — يحتاج فحص هوية.",
            "هدوء المالية قد يُقرأ أحيانًا كفتور إن لم تُضبط طاقة الرئيسية.",
            "فرضية أن التيل يُميّز Micro عن «الأزرق المصرفي» تحتاج تحققًا من المستخدم.",
        ],
        "hypotheses": "هل يربط المستخدم الأزرق-التيل بالثقة أو بالبنوك؟ يُختبر بأسئلة الثقة بعد المهام.",
        "swatch_roles": ["brand", "trust", "positive", "attention", "negative"],
    },
    "c3-dynamic-modular": {
        "label": "C3 — Dynamic Modular",
        "title": "C3 — Dynamic Modular",
        "thesis": ("أعلى تعبير مقبول لـMicro: بنية مكشوطة بحدود حبر وظلال إزاحة للتفاعلي فقط، "
                   "كتل لونية قوية تعرّف المهمة والحالة، ولهجات سياقية منضبطة للمناطق — "
                   "واجهة تبدو نشطة قبل أول لمسة، دون تشتت قوس قزح."),
        "adjectives": ["جريء", "مركّب", "نشط", "صريح", "متماسك"],
        "mood": ("وضوح اللافتات الطباعية؛ متانة مواد التغليف؛ طاقة قطع البناء القابلة للتركيب — نظام وحدات لا لوحة زخرفية."),
        "blocklogic": ("كل منطقة تحمل لهجة شريط واحدة (بنفسجي/تيل/حبر/أرجواني) على علامة قسم صغيرة + "
                       "شريط التبويب النشط؛ حقل البطل كتلة صلبة بشبكة موديولارية داخلية؛ "
                       "الظلال القاسية للعناصر التفاعلية فقط — الأرقام تُقرأ على ورق هادئ."),
        "iconnote": ("أساس Lucide بوزن أثقل (2.3–2.6) يوازي سمك الحدود؛ النشط بحد أعلى وحاوية معبأة. "
                     "خط العرض Noto Kufi Arabic (البديل الواحد المصرح به): هندسي موديولاري يخدم الاتجاه، "
                     "مرخّص OFL، مستضاف ذاتيًا، وللمتن فقط IBM Plex Sans Arabic حفاظًا على القراءة."),
        "darknote": ("ورق داكن بحدود فاتحة (انقلاب الحبر) وظلال سوداء أعمق؛ اللهجات السياقية تُعاير للوهج؛ "
                     "الأخضر المالي يبقى المعنى الوحيد للإيجابية."),
        "strengths": [
            "أعلى تمايز فوري بين المناطق والحالات قبل القراءة.",
            "فيزياء ضغط «ختم» ملموسة تُشعرك أن الواجهة حية.",
            "أقرب تعبير مباشر للاتجاه الأب Bold Modular Micro.",
        ],
        "risks": [
            "خطر التشتت البصري/قوس قزح إن توسعت اللهجات — مراقبة صارمة للعدد.",
            "حدود الحبر الكثيفة قد ترفع الضجيج في شاشات المالية الطويلة.",
            "فرضية أن «النشاط المرئي قبل اللمس» يرفع الثقة المالية تحتاج اختبارًا.",
        ],
        "hypotheses": "هل يبدو النظام «منتجًا واحدًا متماسكًا» أم «تطبيقات متجاورة»؟ يُختبر بمهمة تنقل سريعة.",
        "swatch_roles": ["brand", "trust", "positive", "attention", "negative", "zone-work", "zone-tools", "zone-market"],
    },
    "selected-direction": {
        "label": "الموصى به (مبدئيًا)",
        "title": "Selected — Candidate Design System",
        "thesis": "الاتجاه الموصى به مبدئيًا بعد تطبيق مصفوفة التقييم — قيد اعتماد المالك واختبار المستخدم.",
        "adjectives": ["واثق", "حي", "دافئ", "منضبط", "متماسك"],
        "mood": "مرجع المزاج موثق في تقرير التوصية.",
        "blocklogic": "موثق في design-system-candidate/.",
        "iconnote": "أساس Lucide أحادي العائلة.",
        "darknote": "موثق في design-system-candidate/.",
        "strengths": ["موثق في تقرير التقييم."],
        "risks": ["موثق في تقرير التقييم."],
        "hypotheses": "موثق في تقرير التقييم.",
        "swatch_roles": ["brand", "trust", "positive", "attention", "negative"],
    },
}

ROLE_LABELS = {
    "brand": ("Brand Warm — العلامة الدافئة", "هوية، إنشاء/بدء، لحظات مختارة"),
    "trust": ("Trust Blue — الثقة", "معلومات، سياق نشط، تنقل، موثوقية"),
    "positive": ("Positive Green — الإيجابي المالي", "نتيجة موجبة مكتملة فقط"),
    "attention": ("Attention Amber — الانتباه", "غير مكتمل، انتباه، مراجعة معلقة"),
    "negative": ("Negative Red — السالب", "نتيجة سالبة، خطر، خطأ مدمّر"),
    "zone-work": ("Zone — العمل", "لهجة سياقية لمنطقة العمل"),
    "zone-tools": ("Zone — أدواتي", "لهجة سياقية لمنطقة الأدوات"),
    "zone-market": ("Zone — السوق", "لهجة سياقية لمنطقة السوق المستقبلية"),
}

def main():
    with open(f"{BASE}/design-source/app-template.html") as f:
        app_tpl = f.read()
    with open(f"{BASE}/design-source/board-template.html") as f:
        board_tpl = f.read()
    with open(f"{BASE}/design-source/contrast-data.json") as f:
        contrast = json.load(f)

    for dir_id, meta in DIRS.items():
        dpath = f"{BASE}/prototype/{dir_id}"
        if not os.path.isdir(dpath):
            print(f"skip {dir_id} (folder missing)")
            continue
        tokens_css = ""
        # اقرأ tokens من المستودع (المصدر) أو من مجلد الاتجاه إن وُجد (المطوّر)
        tpath = f"{BASE}/tokens/{dir_id}.tokens.css"
        if not os.path.exists(tpath):
            tpath = f"{dpath}/tokens.css"
        if not os.path.exists(tpath):
            print(f"skip {dir_id} (no tokens css yet — يُبنى في Gate 6)")
            continue
        with open(tpath, encoding="utf-8") as f:
            tokens_css = f.read()

        # ---- index.html ----
        html = (app_tpl
                .replace("{{TITLE}}", meta["title"])
                .replace("{{DIR_LABEL}}", meta["label"])
                .replace("{{DIR_ID}}", dir_id)
                .replace("{{TOKENS_CSS}}", tokens_css))
        with open(f"{dpath}/index.html", "w", encoding="utf-8") as f:
            f.write(html)

        # ---- foundations.html ----
        tjson = f"{BASE}/tokens/{dir_id}.tokens.json"
        if not os.path.exists(tjson):
            tjson = f"{dpath}/tokens.json"
        if not os.path.exists(tjson):
            print(f"skip foundations for {dir_id} (no tokens json)")
            continue
        with open(tjson) as f:
            tokens = json.load(f)

        adjectives = "\n      ".join(f"<li>{a}</li>" for a in meta["adjectives"])
        strengths = "\n      ".join(f"<li>{s}</li>" for s in meta["strengths"])
        risks = "\n      ".join(f"<li>{r}</li>" for r in meta["risks"])

        # swatches
        sw = []
        for role in meta["swatch_roles"]:
            lbl, use = ROLE_LABELS[role]
            for mode in ("light", "dark"):
                m = tokens["modes"][mode]
                r = m.get(role)
                if not r:
                    continue
                mode_lbl = "فاتح" if mode == "light" else "داكن"
                sw.append(
                    f'<div class="swatch"><div class="swatch-fill" style="background:{r["fill"]}"></div>'
                    f'<div class="swatch-meta"><b>{lbl} · {mode_lbl}</b>'
                    f'fill {r["fill"]}<br>text {r["text"]}<br>{use}</div></div>'
                )
        neutrals_l = tokens["modes"]["light"]
        for k, lbl in [("canvas", "Canvas — القاعدة"), ("surface", "Surface — السطح"), ("ink", "Dark Ink — الحبر")]:
            v = neutrals_l[k]
            sw.append(f'<div class="swatch"><div class="swatch-fill" style="background:{v}"></div>'
                      f'<div class="swatch-meta"><b>{lbl} · فاتح</b>{v}</div></div>')
        swatches = "\n      ".join(sw)

        # contrast rows
        rows = []
        for p in contrast.get(dir_id, []):
            okc = "✅" if p["pass"] else "❌"
            rows.append(f'<tr><td><code>{p["fg"]}</code></td><td><code>{p["bg"]}</code></td>'
                       f'<td>{p["use"]}</td><td class="ok">{p["ratio"]:.2f}:1 {okc}</td></tr>')
        contrast_rows = "\n      ".join(rows)

        numnote = "IBM Plex Mono tabular" if dir_id != "c3-dynamic-modular" else "IBM Plex Mono tabular (وKufi للعناوين)"
        board = (board_tpl
                 .replace("{{DIR_LABEL}}", meta["label"])
                 .replace("{{DIR_ID}}", dir_id)
                 .replace("{{TOKENS_CSS}}", tokens_css)
                 .replace("{{THESIS}}", meta["thesis"])
                 .replace("{{ADJECTIVES}}", adjectives)
                 .replace("{{MOOD}}", meta["mood"])
                 .replace("{{BLOCKLOGIC}}", meta["blocklogic"])
                 .replace("{{ICONNOTE}}", meta["iconnote"])
                 .replace("{{DARKNOTE}}", meta["darknote"])
                 .replace("{{NUMNOTE}}", numnote)
                 .replace("{{SWATCHES}}", swatches)
                 .replace("{{CONTRAST_ROWS}}", contrast_rows)
                 .replace("{{STRENGTHS}}", strengths)
                 .replace("{{RISKS}}", risks))
        with open(f"{dpath}/foundations.html", "w", encoding="utf-8") as f:
            f.write(board)
        print(f"built {dir_id}: index.html + foundations.html")

if __name__ == "__main__":
    main()
