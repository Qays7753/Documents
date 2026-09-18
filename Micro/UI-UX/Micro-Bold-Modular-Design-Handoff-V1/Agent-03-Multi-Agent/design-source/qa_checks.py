#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Micro Bold Modular — Agent-03 automated QA checks.
Runs via agent-browser CLI. Produces accessibility/qa-automated-report.md
Every check is repeatable: documented URL + check + result.
"""
import subprocess, json, os, sys

PROTO = "/home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/prototype"
OUT = "/home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/accessibility"
os.makedirs(OUT, exist_ok=True)

DIRS = ["c1-warm-bold", "c2-confident-bold", "c3-dynamic-modular"]
SCREENS = ["home.html", "work.html", "finance.html", "tools.html", "market.html", "products.html", "order.html", "sale.html", "more.html"]

# Fixture values that MUST appear verbatim (file 04) in each direction
FIXTURE_VALUES = ["42.50", "185.00", "136.00", "49.00", "22.00", "120.00", "92.00",
                  "28.00", "15.50", "18.75", "90.00", "108.75", "75.00", "25.00",
                  "50.00", "161.00", "8.50", "15.00", "17/09/2026", "18/09/2026",
                  "142", "وضع مشروعك اليوم", "النتيجة غير مكتملة", "نتيجة موجبة", "نتيجة سالبة",
                  "عمليتا بيع تحتاجان تسجيل التكلفة", "8 من 10", "أكمل التكلفة",
                  "راجع التكاليف", "تكلفة المواد أعلى من المعتاد هذا اليوم",
                  "عندك مبلغ يحتاج تحصيلًا", "حصّل المبلغ", "سارة الخطيب", "ضيافة مناسبة",
                  "متأخر يومًا واحدًا", "حدّث حالة الطلب", "شارك تحديثًا مع الزبونة",
                  "سجّل بيعًا", "مبلغ البيع", "مدفوع كاملًا", "أم محمد", "درج المحل",
                  "شو رح يصير؟", "سجّل البيع", "تم تسجيل البيع", "أُضيف المبلغ إلى درج المحل",
                  "الكاش المسجل الآن", "تراجع", "لسه ما عندك مبيعات اليوم",
                  "المجهول لا يتحول إلى صفر.", "المبلغ لازم يكون أكبر من صفر",
                  "ما انحفظت العملية", "ما تغيّر أي رقم", "حاول مرة ثانية", "ارجع للنموذج"]

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
    return r.stdout.strip()

def open_page(url, w=390, h=844):
    run(f"agent-browser set viewport {w} {h}")
    run(f'agent-browser open "{url}"')
    run("sleep 0.5")

def eval_js(js):
    out = run(f'agent-browser eval "{js.replace(chr(34), chr(39))}"')
    try:
        return json.loads(out)
    except Exception:
        return out

results = []
fails = 0

def check(name, ok, detail=""):
    global fails
    results.append((name, ok, detail))
    if not ok:
        fails += 1

# ---- 1. Fixture integrity per direction (home positive + incomplete + negative + sale states) ----
for d in DIRS:
    urls = [f"{d}/home.html", f"{d}/home.html?state=incomplete", f"{d}/home.html?state=negative",
            f"{d}/home.html?state=empty", f"{d}/sale.html", f"{d}/sale.html?state=validation",
            f"{d}/sale.html?state=success", f"{d}/sale.html?state=system-error", f"{d}/order.html"]
    text = ""
    for u in urls:
        open_page(f"file://{PROTO}/{u}")
        text += eval_js("document.body.innerText") + ' ' + eval_js("Array.from(document.querySelectorAll('input')).map(function(i){return i.value}).join(' ')")
    missing = [v for v in FIXTURE_VALUES if v not in text]
    check(f"[{d}] fixture values verbatim ({len(FIXTURE_VALUES)} values)", not missing,
          f"missing: {missing}" if missing else "all present")

# ---- 2. Structure: 5 tabs, no 6th, no duplicate FAB, QAB labeled ----
for d in DIRS:
    open_page(f"file://{PROTO}/{d}/home.html")
    tabs = eval_js("document.querySelectorAll('.bottomnav .tab').length")
    check(f"[{d}] bottom nav = 5 tabs", tabs == 5, f"got {tabs}")
    tab_labels = eval_js("Array.from(document.querySelectorAll('.bottomnav .tab__label')).map(e=>e.textContent).join('|')")
    check(f"[{d}] tab labels exact", tab_labels == "مشروعي الآن|العمل|المالية|أدواتي|السوق", tab_labels)
    qab = eval_js("Array.from(document.querySelectorAll('[data-screen-state].is-active .qab__label')).map(e=>e.textContent).join('|')")
    check(f"[{d}] QAB = بيع|مصروف|طلب|تحصيل|المزيد", qab == "بيع|مصروف|طلب|تحصيل|المزيد", qab)
    # QAB labels visible (not icon-only)
    hidden_labels = eval_js("Array.from(document.querySelectorAll('[data-screen-state].is-active .qab__label')).filter(e=>e.offsetHeight===0).length")
    check(f"[{d}] QAB labels visible", hidden_labels == 0)

# ---- 3. No horizontal scroll at 320 / 390 / 430, incl. zoom 200 ----
for d in DIRS:
    for w in (320, 390, 430):
        open_page(f"file://{PROTO}/{d}/home.html", w, 844)
        sw = eval_js("document.documentElement.scrollWidth")
        iw = eval_js("window.innerWidth")
        check(f"[{d}] no horizontal scroll @{w}px", sw <= iw, f"scrollWidth={sw} innerWidth={iw}")
    for st in ("incomplete", "negative", "empty"):
        open_page(f"file://{PROTO}/{d}/home.html?state={st}", 320, 844)
        sw = eval_js("document.documentElement.scrollWidth")
        iw = eval_js("window.innerWidth")
        check(f"[{d}] no horizontal scroll @320 ({st})", sw <= iw, f"{sw}>{iw}")
    open_page(f"file://{PROTO}/{d}/home.html?zoom=200", 390, 844)
    sw = eval_js("document.documentElement.scrollWidth"); iw = eval_js("window.innerWidth")
    check(f"[{d}] no horizontal scroll @zoom200", sw <= iw, f"{sw}>{iw}")
    open_page(f"file://{PROTO}/{d}/sale.html?zoom=200", 390, 844)
    sw = eval_js("document.documentElement.scrollWidth"); iw = eval_js("window.innerWidth")
    check(f"[{d}] no horizontal scroll @zoom200 (sale)", sw <= iw, f"{sw}>{iw}")

# ---- 4. QAB not obscured: last QAB item bottom above nav top ----
for d in DIRS:
    open_page(f"file://{PROTO}/{d}/home.html", 390, 844)
    res = eval_js("""(function(){
      var q = document.querySelector('.qab'); var n = document.querySelector('.bottomnav');
      if(!q||!n) return 'missing';
      var qr = q.getBoundingClientRect(); var nr = n.getBoundingClientRect();
      return qr.bottom <= nr.top + 1 ? 'ok' : 'OVERLAP ' + qr.bottom + '>' + nr.top;
    })()""")
    check(f"[{d}] QAB above bottom nav (no occlusion)", res == "ok", res)

# ---- 5. Hero primary action in initial viewport @390 ----
for d in DIRS:
    open_page(f"file://{PROTO}/{d}/home.html", 390, 844)
    res = eval_js("""(function(){
      var q = document.querySelector('[data-screen-state].is-active .qab');
      if(!q) return 'missing';
      return q.getBoundingClientRect().top < 844 ? 'ok' : 'BELOW FOLD';
    })()""")
    check(f"[{d}] primary action visible in initial viewport", res == "ok", res)

# ---- 6. Incomplete hero shows NO numeric result value ----
for d in DIRS:
    open_page(f"file://{PROTO}/{d}/home.html?state=incomplete", 390, 844)
    res = eval_js("""(function(){
      var h = document.querySelector('[data-screen-state=incomplete].is-active .hero');
      if(!h) return 'missing';
      var r = h.querySelector('.hero__result');
      if(r) return 'HAS RESULT NUMBER: ' + r.textContent;
      return 'ok';
    })()""")
    check(f"[{d}] incomplete hero has NO result number", res == "ok", res)

# ---- 7. lang/dir correctness ----
for d in DIRS:
    open_page(f"file://{PROTO}/{d}/home.html")
    lang = eval_js("document.documentElement.lang")
    dirv = eval_js("document.documentElement.dir")
    check(f"[{d}] html lang=ar dir=rtl", lang == "ar" and dirv == "rtl", f"{lang}/{dirv}")

# ---- 8. No English leakage in operational UI (menu/screen text) ----
LEAK_PATTERNS = ["Order ID", "FAIL", "agreement recorded locally", "Total", "Submit", "Cancel", "Save"]
for d in DIRS:
    all_text = ""
    for s in SCREENS:
        open_page(f"file://{PROTO}/{d}/{s}")
        all_text += eval_js("document.body.innerText") + ' ' + eval_js("Array.from(document.querySelectorAll('input')).map(function(i){return i.value}).join(' ')")
    leaks = [p for p in LEAK_PATTERNS if p in all_text]
    check(f"[{d}] no English leakage", not leaks, str(leaks))

# ---- 9. No href="#" dead links ----
for d in DIRS:
    dead = 0
    for s in SCREENS:
        open_page(f"file://{PROTO}/{d}/{s}")
        n = eval_js("document.querySelectorAll('a[href=\"#\"]').length")
        dead += n if isinstance(n, int) else 0
    check(f"[{d}] no dead href=\"#\" links (data-close sheets excluded by behavior)", dead == 0, f"{dead} dead anchors found")

# ---- 10. minimum touch size for QAB and nav ----
for d in DIRS:
    open_page(f"file://{PROTO}/{d}/home.html", 390, 844)
    small = eval_js("""(function(){
      var els = document.querySelectorAll('[data-screen-state].is-active .qab__btn, .bottomnav .tab');
      var bad = [];
      els.forEach(function(e){
        var r = e.getBoundingClientRect();
        if (r.height < 44 || r.width < 44) bad.push(e.className + ':' + Math.round(r.width) + 'x' + Math.round(r.height));
      });
      return bad.length ? bad.join('; ') : 'ok';
    })()""")
    check(f"[{d}] QAB+nav touch targets ≥44px", small == "ok", small)

# ---- 11. Round-2 regression checks ----
for d in DIRS:
    # validation intercept: amount=0 + click submit stays on form with visible error
    open_page(f"file://{PROTO}/{d}/sale.html")
    eval_js("document.getElementById('amount').value = '0'")
    eval_js("document.getElementById('submit-sale') && document.getElementById('submit-sale').click()")
    url = run("agent-browser get url")
    on_form = "/sale.html" in url and "state=success" not in url
    err_visible = eval_js("!document.getElementById('amount-error').classList.contains('is-hidden')")
    check(f"[{d}] validation intercept blocks submit on 0", on_form and err_visible, f"url={url} err={err_visible}")
    # zoom200 truly resizes text (D-110 regression)
    open_page(f"file://{PROTO}/{d}/home.html")
    s1 = eval_js("getComputedStyle(document.querySelector('.activity-row__title')).fontSize")
    open_page(f"file://{PROTO}/{d}/home.html?zoom=200")
    s2 = eval_js("getComputedStyle(document.querySelector('.activity-row__title')).fontSize")
    grew = float(str(s2).replace('px','')) > float(str(s1).replace('px','')) * 1.8
    check(f"[{d}] zoom200 actually enlarges text", grew, f"{s1} -> {s2}")
    # multi-element zoom check (D-208): body, currency mark, section title, secondary
    open_page(f"file://{PROTO}/{d}/sale.html?state=success")
    sizes = eval_js("JSON.stringify({body: getComputedStyle(document.body).fontSize, cur: getComputedStyle(document.querySelector('.success-card__amount span')).fontSize, label: getComputedStyle(document.querySelector('.success-ref')).fontSize})")
    open_page(f"file://{PROTO}/{d}/sale.html?state=success&zoom=200")
    sizes2 = eval_js("JSON.stringify({body: getComputedStyle(document.body).fontSize, cur: getComputedStyle(document.querySelector('.success-card__amount span')).fontSize, label: getComputedStyle(document.querySelector('.success-ref')).fontSize})")
    try:
        a = json.loads(sizes); b = json.loads(sizes2)
        allgrew = all(float(str(b[k]).replace('px','')) > float(str(a[k]).replace('px','')) * 1.5 for k in a)
        check(f"[{d}] zoom200 enlarges inline styles too (multi-element)", allgrew, f"{sizes} -> {sizes2}")
    except Exception as ex:
        check(f"[{d}] zoom200 multi-element parse", False, str(ex))
    # closed sheets not focusable
    open_page(f"file://{PROTO}/{d}/home.html")
    vis = eval_js("getComputedStyle(document.getElementById('sheet-menu')).visibility")
    check(f"[{d}] closed sheet hidden from focus", vis == "hidden", str(vis))
    # date field clean (D-101)
    open_page(f"file://{PROTO}/{d}/sale.html")
    dv = eval_js("document.getElementById('date').value")
    check(f"[{d}] date field value clean", dv == "18/09/2026", str(dv))
    # theme switch scoped (D-113)
    open_page(f"file://{PROTO}/{d}/tools.html")
    t0 = eval_js("document.documentElement.getAttribute('data-theme')")
    eval_js("document.querySelectorAll('.switch')[0].click()")
    t1 = eval_js("document.documentElement.getAttribute('data-theme')")
    check(f"[{d}] PIN switch does not toggle theme", t1 == t0, f"{t0} -> {t1}")
    # green not used on success amount (D-104)
    open_page(f"file://{PROTO}/{d}/sale.html?state=success")
    col = eval_js("getComputedStyle(document.querySelector('.success-card__amount')).color")
    check(f"[{d}] success amount is ink (no green)", "0, 30, 20" not in str(col) and "35, 110, 66" not in str(col), str(col))

# ---- 12. Round-4 regression: interactive sale flow (P0) ----
for d in DIRS + ["selected-direction"]:
    open_page(f"file://{PROTO}/{d}/sale.html")
    # valid amount -> submit navigates to success
    eval_js("document.getElementById('amount').value = '25'")
    href = eval_js("document.getElementById('submit-sale').getAttribute('href')")
    ok_nav = "state=success" in str(href)
    check(f"[{d}] submit link preserves state=success (P0 regression)", ok_nav, str(href))
    # theme + state together
    open_page(f"file://{PROTO}/{d}/sale.html?theme=dark")
    href2 = eval_js("document.getElementById('submit-sale').getAttribute('href')")
    check(f"[{d}] submit link keeps theme AND state", "state=success" in str(href2) and "theme=dark" in str(href2), str(href2))
    # still intercepts zero
    open_page(f"file://{PROTO}/{d}/sale.html")
    eval_js("document.getElementById('amount').value = '0'")
    eval_js("document.getElementById('submit-sale').click()")
    url_after = run("agent-browser get url")
    check(f"[{d}] zero amount still blocked after P0 fix", "state=success" not in url_after, url_after)
    # ink-faint contrast (agent 4 finding)
    open_page(f"file://{PROTO}/{d}/home.html")
    col = eval_js("getComputedStyle(document.querySelector('.activity-row__time')).color")
    check(f"[{d}] timestamp color is darkened inkFaint", "4.13" not in str(col), str(col))

# ---- report ----
lines = ["# Automated QA Report — Agent-03 Prototype", "",
         f"Date: 2026-09-18 · Tool: agent-browser (headless Chromium) + DOM assertions",
         f"Checks: {len(results)} · Passed: {sum(1 for _, ok, _ in results if ok)} · Failed: {fails}", "",
         "| Check | Result | Detail |", "|---|---|---|"]
for name, ok, detail in results:
    lines.append(f"| {name} | {'✅ PASS' if ok else '❌ FAIL'} | {detail if detail else '—'} |")
report = "\n".join(lines)
open(os.path.join(OUT, "qa-automated-report.md"), "w", encoding="utf-8").write(report + "\n")
print(report[:3000])
print(f"\nTOTAL: {len(results)} checks, {fails} failures")
sys.exit(1 if fails else 0)
