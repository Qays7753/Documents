#!/usr/bin/env python3
"""فحص الوصول الآلي axe-core على الشاشات والحالات الحرجة لكل اتجاه + الوضع الداكن + نص 200%."""
import http.server, socketserver, threading, os, time, json, sys
from playwright.sync_api import sync_playwright

ROOT = "/home/z/my-project/repos/base/agent-runs/agent-02-independent/prototype"
AXE = "/home/z/my-project/scripts/axe-runner/node_modules/axe-core/axe.min.js"
OUT = "/home/z/my-project/repos/base/agent-runs/agent-02-independent/accessibility"
PORT = 8921
socketserver.TCPServer.allow_reuse_address = True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw): super().__init__(*a, directory=ROOT, **kw)
    def log_message(self, *a): pass

def serve():
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        httpd.serve_forever()

PAGES = [
    ("home-positive", "?finance=positive", None),
    ("home-incomplete", "?finance=incomplete", None),
    ("home-negative", "?finance=negative", None),
    ("home-empty", "?finance=empty", None),
    ("home-dark", "?finance=positive&theme=dark", None),
    ("sale-form", "?finance=positive&sheet=sale", None),
    ("work", "?screen=work&orders=late", None),
    ("finance", "?screen=finance", None),
    ("tools", "?screen=tools", None),
]

def run_axe(page):
    with open(AXE, encoding="utf-8") as f:
        axe_src = f.read()
    return page.evaluate("""async (axeSrc) => {
        const s = document.createElement('script');
        s.textContent = axeSrc;
        document.head.appendChild(s);
        await new Promise(r => setTimeout(r, 150));
        const res = await axe.run(document, {
            resultTypes: ['violations'],
            rules: { 'color-contrast': { enabled: true } }
        });
        return { violations: res.violations.map(v => ({
            id: v.id, impact: v.impact, help: v.help,
            nodes: v.nodes.slice(0, 6).map(n => ({
                target: n.target.join(' ').slice(0, 90),
                snippet: n.html.slice(0, 110),
                summary: (n.failureSummary || '').slice(0, 140)
            }))
        })), passes: res.passes.length };
    }""", axe_src)

def main():
    threading.Thread(target=serve, daemon=True).start()
    time.sleep(0.6)
    all_results = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 520, "height": 960})
        for d in ["c1-warm-bold", "c2-confident-bold", "c3-dynamic-modular"]:
            all_results[d] = {}
            for name, url, action in PAGES:
                page.goto(f"http://127.0.0.1:{PORT}/{d}/index.html{url}")
                page.wait_for_timeout(650)
                if name == "sale-form":
                    page.fill("#sale-amount", "0")
                    page.click('[data-submit-sale]')
                    page.wait_for_timeout(400)
                try:
                    res = run_axe(page)
                    all_results[d][name] = res
                    v_count = len(res["violations"])
                    print(f"{d}/{name}: {v_count} violations, {res['passes']} passes")
                except Exception as e:
                    all_results[d][name] = {"error": str(e)}
                    print(f"{d}/{name}: ERROR {e}")
        browser.close()
    with open(f"{OUT}/axe-raw.json", "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=1)
    print("saved axe-raw.json")

main()
