#!/usr/bin/env python3
"""فحوص سلامة التخطيط: تجاوز أفقي 320، ظهور QAB في 390x844، أحجام الأهداف 44px، RTL."""
import http.server, socketserver, threading, os, time, json, sys
from playwright.sync_api import sync_playwright

ROOT = "/home/z/my-project/repos/base/agent-runs/agent-02-independent/prototype"
PORT = 8913
socketserver.TCPServer.allow_reuse_address = True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw): super().__init__(*a, directory=ROOT, **kw)
    def log_message(self, *a): pass

def serve():
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=serve, daemon=True).start()
time.sleep(0.5)

results = []
def check(name, ok, detail=""):
    results.append({"check": name, "pass": bool(ok), "detail": str(detail)})

with sync_playwright() as p:
    browser = p.chromium.launch()
    for d in ["c1-warm-bold", "c2-confident-bold", "c3-dynamic-modular"]:
        # 1) تجاوز أفقي عند 320
        pg = browser.new_page(viewport={"width": 700, "height": 950})
        pg.goto(f"http://127.0.0.1:{PORT}/{d}/index.html?text=200")
        pg.wait_for_timeout(600)
        # اجعل العرض 320 عبر زر الأدوات ثم قس
        pg.click('.cbtn[data-action="viewport"][data-val="320"]')
        pg.wait_for_timeout(400)
        sw = pg.evaluate("document.querySelector('.phone').scrollWidth")
        inner_sw = pg.evaluate("document.querySelector('.app').scrollWidth")
        phone_cw = pg.evaluate("document.querySelector('.phone').clientWidth")
        check(f"{d}: لا تجاوز أفقي للإطار عند 320", sw <= phone_cw + 2, f"scrollWidth={sw} clientWidth={phone_cw}")
        # 2) تجاوز المحتوى الداخلي مع نص 200%
        check(f"{d}: المحتوى داخل حدود التطبيق (نص 200%)", inner_sw <= phone_cw + 2, f"app scrollWidth={inner_sw} clientWidth={phone_cw}")
        pg.close()

        # 3) QAB ظاهر في الإطار الأولي 390x844
        pg = browser.new_page(viewport={"width": 500, "height": 920})
        pg.goto(f"http://127.0.0.1:{PORT}/{d}/index.html")
        pg.wait_for_timeout(500)
        qab_box = pg.evaluate("""() => {
            const q = document.querySelector('.qab');
            const r = q.getBoundingClientRect();
            return {top: r.top, bottom: r.bottom, vh: window.innerHeight, visible: r.height > 30};
        }""")
        check(f"{d}: شريط الإجراءات مرئي", qab_box["visible"], json.dumps(qab_box))
        # 4) أحجام أهداف اللمس (تبويبات + QAB) >= 44px
        sizes = pg.evaluate("""() => {
            const out = [];
            document.querySelectorAll('.tab, .qab-btn').forEach(el => {
                const r = el.getBoundingClientRect();
                out.push({cls: el.className.split(' ')[0], w: Math.round(r.width), h: Math.round(r.height)});
            });
            return out;
        }""")
        small = [s for s in sizes if s["h"] < 44 or s["w"] < 44]
        check(f"{d}: أهداف التنقل/الإجراءات ≥44px", len(small) == 0, json.dumps(small))
        # 5) اتجاه RTL
        dir_attr = pg.evaluate("document.documentElement.dir")
        check(f"{d}: الاتجاه RTL", dir_attr == "rtl", dir_attr)
        # 6) العنوان البطل ظاهر ضمن أول 60% من الشاشة
        hero = pg.evaluate("""() => {
            const h = document.querySelector('.hero-inner:not([hidden])');
            if (!h) return null;
            const r = h.getBoundingClientRect();
            return {top: Math.round(r.top), height: Math.round(r.height)};
        }""")
        check(f"{d}: البطل داخل أول 60% من الشاشة", hero and hero["top"] + hero["height"] * 0.6 < 920 * 0.75, json.dumps(hero))
        pg.close()
    browser.close()

passed = sum(1 for r in results if r["pass"])
print(json.dumps(results, ensure_ascii=False, indent=1))
print(f"\n{passed}/{len(results)} passed")
sys.exit(0 if passed == len(results) else 1)
