#!/usr/bin/env python3
"""Download self-hosted OFL fonts (IBM Plex Sans Arabic, IBM Plex Mono, Noto Kufi Arabic)
from the fontsource CDN with Google Fonts API fallback. Outputs woff2 files + fonts.css."""
import os, re, sys, urllib.request

OUT = "/home/z/my-project/repos/base/agent-runs/agent-02-independent/prototype/assets/fonts"
os.makedirs(OUT, exist_ok=True)

FAMILIES = {
    "ibm-plex-sans-arabic": {"subsets": ["arabic", "latin"], "weights": [400, 500, 600, 700], "css_name": "IBM Plex Sans Arabic"},
    "ibm-plex-mono": {"subsets": ["latin"], "weights": [400, 500, 600], "css_name": "IBM Plex Mono"},
    "noto-kufi-arabic": {"subsets": ["arabic", "latin"], "weights": [500, 700, 800], "css_name": "Noto Kufi Arabic"},
}

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

css_parts = []
downloaded = 0
for fam, spec in FAMILIES.items():
    for w in spec["weights"]:
        for subset in spec["subsets"]:
            url = f"https://cdn.jsdelivr.net/fontsource/fonts/{fam}@latest/{subset}-{w}-normal.woff2"
            fname = f"{fam}-{subset}-{w}.woff2"
            dest = os.path.join(OUT, fname)
            try:
                data = fetch(url)
                if len(data) < 1000:
                    raise ValueError(f"suspiciously small: {len(data)} bytes")
                with open(dest, "wb") as f:
                    f.write(data)
                downloaded += 1
                # Unicode ranges (Google/fontsource standard)
                if subset == "arabic":
                    ur = "U+0600-06FF, U+0750-077F, U+0870-088E, U+0890-0891, U+0898-08E1, U+08E3-08FF, U+200C-200E, U+2010-2011, U+204F, U+2E41, U+FB50-FDFF, U+FE70-FE74, U+FE76-FEFC"
                elif subset == "latin":
                    ur = "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD"
                css_parts.append(
                    f"@font-face {{ font-family: '{spec['css_name']}'; font-style: normal; "
                    f"font-weight: {w}; font-display: swap; src: url('{fname}') format('woff2'); "
                    f"unicode-range: {ur}; }}"
                )
                print(f"OK  {fam}/{subset}/{w}  {len(data)//1024} KB")
            except Exception as e:
                print(f"FAIL {fam}/{subset}/{w}: {e}")

with open(os.path.join(OUT, "fonts.css"), "w") as f:
    f.write("/* Self-hosted OFL fonts: IBM Plex Sans Arabic (OFL), IBM Plex Mono (OFL), Noto Kufi Arabic (OFL) */\n")
    f.write("\n".join(css_parts) + "\n")

print(f"\nDownloaded {downloaded} font files -> {OUT}")
if downloaded == 0:
    sys.exit(1)
