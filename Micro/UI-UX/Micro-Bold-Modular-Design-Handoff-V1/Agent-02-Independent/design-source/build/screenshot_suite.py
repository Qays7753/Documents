#!/usr/bin/env python3
"""حزمة لقطات الأدلة الكاملة: كل الاتجاهات × الشاشات × الحالات × العروض."""
import http.server, socketserver, threading, os, time, sys
from playwright.sync_api import sync_playwright

ROOT = "/home/z/my-project/repos/base/agent-runs/agent-02-independent/prototype"
OUT = "/home/z/my-project/repos/base/agent-runs/agent-02-independent/screenshots"
PORT = 8920
socketserver.TCPServer.allow_reuse_address = True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw): super().__init__(*a, directory=ROOT, **kw)
    def log_message(self, *a): pass

def serve():
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        httpd.serve_forever()

DIRS = {
    "c1-warm-bold": "C1-Warm-Bold",
    "c2-confident-bold": "C2-Confident-Bold",
    "c3-dynamic-modular": "C3-Dynamic-Modular",
}

# (اسم الملف، مسار معلمات، تفاعلات إضافية قبل اللقطة)
SHOTS = [
    ("01-home-positive",        "?finance=positive", None),
    ("02-home-incomplete",     "?finance=incomplete", None),
    ("03-home-negative",       "?finance=negative", None),
    ("04-home-empty",          "?finance=empty", None),
    ("05-home-positive-dark",  "?finance=positive&theme=dark", None),
    ("06-home-320",            "?finance=positive&viewport=320", None),
    ("07-home-430",            "?finance=positive&viewport=430", None),
    ("08-home-text200",        "?finance=positive&text=200", None),
    ("09-sale-form",           "?finance=positive&sheet=sale", None),
    ("10-sale-validation",     "?finance=positive&sheet=sale", "validation"),
    ("11-sale-success",        "?finance=positive&sheet=sale", "success"),
    ("12-system-error",        "?finance=positive&savefail=on&sheet=sale", "syserr"),
    ("13-work-late",           "?screen=work&orders=late", None),
    ("14-order-detail",        "?orders=late&sheet=order", None),
    ("15-finance",             "?screen=finance", None),
    ("16-tools",              "?screen=tools", None),
    ("17-market",             "?screen=market", None),
    ("18-account-menu",        "?finance=positive", "account"),
    ("19-more-sheet",          "?finance=positive", "more"),
    ("20-reduced-motion",      "?finance=positive&motion=reduced", None),
]

def shoot(page, d, code, name, url, action, dark=False):
    page.goto(f"http://127.0.0.1:{PORT}/{d}/index.html{url}")
    page.wait_for_timeout(700)
    if action == "validation":
        page.fill("#sale-amount", "0")
        page.click('[data-submit-sale]')
        page.wait_for_timeout(500)
    elif action == "success":
        page.fill("#sale-amount", "25.00")
        page.click('[data-submit-sale]')
        page.wait_for_timeout(1400)
    elif action == "syserr":
        page.fill("#sale-amount", "25.00")
        page.click('[data-submit-sale]')
        page.wait_for_timeout(1500)
    elif action == "account":
        page.click(".logo-btn")
        page.wait_for_timeout(600)
    elif action == "more":
        page.click('.qab-btn[data-open="more"]')
        page.wait_for_timeout(600)
    page.screenshot(path=f"{OUT}/{code}-{name}.png")
    print(f"  {code}-{name}")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 520, "height": 960}, device_scale_factor=2)
        for d, code in DIRS.items():
            os.makedirs(OUT, exist_ok=True)
            print(f"== {code} ==")
            for name, url, action in SHOTS:
                shoot(page, d, code, name, url, action)
        # لوحات الأسس + المقارنة + العرض الكامل
        for d, code in DIRS.items():
            page.goto(f"http://127.0.0.1:{PORT}/{d}/foundations.html")
            page.wait_for_timeout(900)
            page.screenshot(path=f"{OUT}/{code}-21-foundations.png", full_page=True)
            print(f"  {code}-21-foundations")
            page.goto(f"http://127.0.0.1:{PORT}/{d}/index.html?finance=positive")
            page.wait_for_timeout(700)
            page.screenshot(path=f"{OUT}/{code}-22-home-fullscroll.png", full_page=True)
            print(f"  {code}-22-home-fullscroll")
        page.goto(f"http://127.0.0.1:{PORT}/index.html")
        page.wait_for_timeout(1800)
        page.screenshot(path=f"{OUT}/23-comparison-page.png", full_page=True)
        print("  23-comparison-page")
        browser.close()

threading.Thread(target=serve, daemon=True).start()
time.sleep(0.6)
main()
print("DONE")
