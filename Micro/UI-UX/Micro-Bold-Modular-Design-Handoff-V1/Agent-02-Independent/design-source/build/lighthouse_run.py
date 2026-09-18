#!/usr/bin/env python3
"""تشغيل Lighthouse على الاتجاهات الثلاثة عبر Chromium من Playwright (CDP)."""
import json, subprocess, threading, time, http.server, socketserver, os
from playwright.sync_api import sync_playwright

ROOT = "/home/z/my-project/repos/base/agent-runs/agent-02-independent/prototype"
OUT = "/home/z/my-project/repos/base/agent-runs/agent-02-independent/accessibility"
PORT = 8922
CDP = 9333
socketserver.TCPServer.allow_reuse_address = True

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw): super().__init__(*a, directory=ROOT, **kw)
    def log_message(self, *a): pass

def serve():
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=serve, daemon=True).start()
time.sleep(0.5)

results = {}
with sync_playwright() as p:
    browser = p.chromium.launch(args=[f"--remote-debugging-port={CDP}"])
    for d in ["c1-warm-bold", "c2-confident-bold", "c3-dynamic-modular"]:
        url = f"http://127.0.0.1:{PORT}/{d}/index.html?finance=positive"
        out_json = f"/tmp/lh-{d}.json"
        cmd = [
            "npx", "--prefix", "/home/z/my-project/scripts", "lighthouse", url,
            f"--port={CDP}", "--output=json", f"--output-path={out_json}",
            "--only-categories=performance,accessibility,best-practices,seo",
            "--quiet", "--chrome-flags=--headless=new"
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180, cwd="/home/z/my-project/scripts")
        try:
            with open(out_json) as f:
                data = json.load(f)
            cats = data.get("categories", {})
            results[d] = {k: round(v.get("score", 0) * 100) for k, v in cats.items() if isinstance(v, dict)}
            # أخطاء الوصول إن وجدت
            audits = data.get("audits", {})
            a11y_fails = [a for a in audits.values() if a.get("score") is not None and a["score"] < 1 and "categories" in json.dumps(a.get("score", ""))]
            print(d, results[d])
        except Exception as e:
            print(d, "ERROR", e, r.stdout[-300:], r.stderr[-300:])
    browser.close()

with open(f"{OUT}/lighthouse-scores.json", "w") as f:
    json.dump(results, f, indent=1)
print("saved lighthouse-scores.json")
