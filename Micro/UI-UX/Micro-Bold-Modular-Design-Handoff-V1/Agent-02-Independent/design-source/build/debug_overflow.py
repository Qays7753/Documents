#!/usr/bin/env python3
"""حدد العناصر التي تتجاوز عرض 312px داخل التطبيق عند 320+200%."""
import http.server, socketserver, threading, time, json
from playwright.sync_api import sync_playwright

ROOT = "/home/z/my-project/repos/base/agent-runs/agent-02-independent/prototype"
PORT = 8914
socketserver.TCPServer.allow_reuse_address = True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw): super().__init__(*a, directory=ROOT, **kw)
    def log_message(self, *a): pass

def serve():
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=serve, daemon=True).start()
time.sleep(0.5)

with sync_playwright() as p:
    browser = p.chromium.launch()
    pg = browser.new_page(viewport={"width": 700, "height": 950})
    pg.goto(f"http://127.0.0.1:{PORT}/c1-warm-bold/index.html?text=200")
    pg.wait_for_timeout(500)
    pg.click('.cbtn[data-action="viewport"][data-val="320"]')
    pg.wait_for_timeout(400)
    wide = pg.evaluate("""() => {
        const out = [];
        const limit = 316;
        document.querySelectorAll('.app *').forEach(el => {
            const r = el.getBoundingClientRect();
            if (r.width > limit || r.right > limit + 4) {
                out.push({
                    tag: el.tagName, cls: (el.className.baseVal !== undefined ? el.className.baseVal : el.className || '').toString().slice(0, 60),
                    w: Math.round(r.width), right: Math.round(r.right), text: (el.textContent || '').trim().slice(0, 30)
                });
            }
        });
        return out.slice(0, 40);
    }""")
    print(json.dumps(wide, ensure_ascii=False, indent=1))
    browser.close()
