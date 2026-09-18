#!/usr/bin/env python3
"""Smoke test: افتح الاتجاهات الثلاثة، سجّل أخطاء الكونسول، وخذ لقطات أولية."""
import http.server, socketserver, threading, os, sys, time
from playwright.sync_api import sync_playwright

ROOT = "/home/z/my-project/repos/base/agent-runs/agent-02-independent/prototype"
PORT = 8912
OUT = "/home/z/my-project/shots"
os.makedirs(OUT, exist_ok=True)

socketserver.TCPServer.allow_reuse_address = True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw): super().__init__(*a, directory=ROOT, **kw)
    def log_message(self, *a): pass

def serve():
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=serve, daemon=True).start()
time.sleep(0.6)

dirs = ["c1-warm-bold", "c2-confident-bold", "c3-dynamic-modular"]
errors = []

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 480, "height": 900})
    page.on("console", lambda m: errors.append(f"[{m.type}] {m.text}") if m.type in ("error",) else None)
    page.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
    page.on("response", lambda r: errors.append(f"[404] {r.url}") if r.status == 404 else None)

    for d in dirs:
        page.goto(f"http://127.0.0.1:{PORT}/{d}/index.html?finance=positive")
        page.wait_for_timeout(900)
        page.screenshot(path=f"{OUT}/smoke-{d}-home.png")
        # فتح التبويبات
        for tab in ["work", "finance", "tools", "market"]:
            page.click(f'.tab[data-tab="{tab}"]')
            page.wait_for_timeout(350)
        page.click('.tab[data-tab="home"]')
        page.wait_for_timeout(300)
        # فتح نموذج البيع
        page.click('.qab-btn[data-open="sale"]')
        page.wait_for_timeout(500)
        page.screenshot(path=f"{OUT}/smoke-{d}-sale.png")
        page.click('.sheet-close')
        page.wait_for_timeout(300)
        # لوحة الأسس
        page.goto(f"http://127.0.0.1:{PORT}/{d}/foundations.html")
        page.wait_for_timeout(700)
        page.screenshot(path=f"{OUT}/smoke-{d}-board.png", full_page=True)
        print(f"OK {d}")

    # صفحة المقارنة
    page.goto(f"http://127.0.0.1:{PORT}/index.html")
    page.wait_for_timeout(1500)
    page.screenshot(path=f"{OUT}/smoke-compare.png", full_page=True)
    print("OK compare")
    browser.close()

print("\n=== CONSOLE ERRORS ===")
if errors:
    for e in errors[:30]: print(e)
    sys.exit(1)
print("none")
