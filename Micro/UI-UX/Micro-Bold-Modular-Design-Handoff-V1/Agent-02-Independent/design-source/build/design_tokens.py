#!/usr/bin/env python3
"""
Micro Bold Modular — Agent 02 Independent
Design tokens single source of truth + WCAG 2.2 contrast gate.

Emits:
  tokens/<dir>.tokens.json
  tokens/<dir>.tokens.css
  accessibility/contrast-results.md
  design-source/contrast-data.json
Fails loudly (exit 1) if any required pair misses its minimum.
"""
import json, os, sys

BASE = "/home/z/my-project/repos/base/agent-runs/agent-02-independent"

# ---------- WCAG relative luminance / contrast ----------
def _srgb(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def lum(hexstr):
    h = hexstr.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return 0.2126 * _srgb(r) + 0.7152 * _srgb(g) + 0.0722 * _srgb(b)

def ratio(fg, bg):
    l1, l2 = lum(fg), lum(bg)
    if l1 < l2:
        l1, l2 = l2, l1
    return (l1 + 0.05) / (l2 + 0.05)

def mix(h1, h2, t):
    """blend two hexes; t=0 -> h1"""
    a = [int(h1.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)]
    b = [int(h2.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)]
    return '#' + ''.join(f'{round(a[i]+(b[i]-a[i])*t):02x}' for i in range(3))

# ---------- Token definitions ----------
ROLES = ["brand", "trust", "positive", "attention", "negative"]
# الكنكة الدافئة المستعارة من C1 للاتجاه المختبر (لحظات النجاح فقط)
WARM_ACCENT = {
    "light": {"fill": "#BE4A20", "onfill": "#FFFFFF", "text": "#A03E18", "soft": "#F9E7DB", "onsoft": "#8F3715"},
    "dark": {"fill": "#DE7B4B", "onfill": "#2B0F04", "text": "#F0A276", "soft": "#3C2417", "onsoft": "#F6C3A0"},
}

DIRECTIONS = {
    "c1-warm-bold": {
        "label": "C1 — Warm Bold",
        "modes": {
            "light": {
                "canvas": "#FBF4EC", "surface": "#FFFFFF", "surface2": "#F7EBDD",
                "group": "#F3E5D3", "ink": "#2B1A10", "ink2": "#5E4B39", "ink3": "#74604B",
                "border": "#E7D6C1", "borderStrong": "#8F7355",
                "brand": {"fill": "#C94E1F", "onfill": "#FFFFFF", "text": "#A63812",
                          "soft": "#F9E2D2", "onsoft": "#7C2E0C", "border": "#C94E1F"},
                "trust": {"fill": "#1D6E9C", "onfill": "#FFFFFF", "text": "#155C86",
                          "soft": "#E1EDF5", "onsoft": "#114F73", "border": "#1D6E9C"},
                "positive": {"fill": "#217A4B", "onfill": "#FFFFFF", "text": "#186638",
                          "soft": "#E3F2E6", "onsoft": "#14592F", "border": "#217A4B"},
                "attention": {"fill": "#8F6A0B", "onfill": "#FFFFFF", "text": "#7A5A08",
                          "soft": "#FAEFD2", "onsoft": "#654906", "border": "#8F6A0B"},
                "negative": {"fill": "#B3261E", "onfill": "#FFFFFF", "text": "#A01D16",
                          "soft": "#FBE8E4", "onsoft": "#8C1812", "border": "#B3261E"},
                # hero field = warm apricot-coral block, espresso ink text (C1 signature)
                "hero": {"fill": "#E5763C", "on": "#2B1408", "on2": "#471C07"},
            },
            "dark": {
                "canvas": "#20140E", "surface": "#2B1D14", "surface2": "#35241A",
                "group": "#3B2819", "ink": "#F9EFE3", "ink2": "#D2BCA5", "ink3": "#AB9379",
                "border": "#4C3423", "borderStrong": "#9A7550",
                "brand": {"fill": "#E5763C", "onfill": "#2B1408", "text": "#F5A268",
                          "soft": "#47271411", "onsoft": "#F5C9A4", "border": "#B96A3F"},
                "trust": {"fill": "#7CC4E4", "onfill": "#0A2432", "text": "#8CCAE8",
                          "soft": "#1D334116", "onsoft": "#A9D9EE", "border": "#3F7396"},
                "positive": {"fill": "#5FBF85", "onfill": "#0A2415", "text": "#74D096",
                          "soft": "#1D3A2612", "onsoft": "#9BE0B4", "border": "#3E7A56"},
                "attention": {"fill": "#E3B95F", "onfill": "#241A04", "text": "#E6C274",
                          "soft": "#3A2E10", "onsoft": "#F1D68C", "border": "#8A6E2E"},
                "negative": {"fill": "#F0988A", "onfill": "#2B0B06", "text": "#F4A396",
                          "soft": "#3C1D16", "onsoft": "#F7B8AD", "border": "#9C4A3C"},
                "hero": {"fill": "#E58A54", "on": "#2B1408", "on2": "#54230D"},
            },
        },
    },
    "c2-confident-bold": {
        "label": "C2 — Confident Bold",
        "modes": {
            "light": {
                "canvas": "#F0F4F5", "surface": "#FFFFFF", "surface2": "#EDF3F4",
                "group": "#E6EEF0", "ink": "#0F242E", "ink2": "#44606B", "ink3": "#5A747F",
                "border": "#D6E0E4", "borderStrong": "#66808B",
                "brand": {"fill": "#BE4A20", "onfill": "#FFFFFF", "text": "#A03E18",
                          "soft": "#F9E7DB", "onsoft": "#8F3715", "border": "#BE4A20"},
                "trust": {"fill": "#0F6570", "onfill": "#FFFFFF", "text": "#0C525C",
                          "soft": "#E0EEF0", "onsoft": "#0A4750", "border": "#0F6570"},
                "positive": {"fill": "#1D7A50", "onfill": "#FFFFFF", "text": "#15633E",
                          "soft": "#E2F2E8", "onsoft": "#115634", "border": "#1D7A50"},
                "attention": {"fill": "#8A6112", "onfill": "#FFFFFF", "text": "#75530E",
                          "soft": "#FAF1D8", "onsoft": "#614609", "border": "#8A6112"},
                "negative": {"fill": "#B3261E", "onfill": "#FFFFFF", "text": "#A01D16",
                          "soft": "#FBE9E6", "onsoft": "#8C1812", "border": "#B3261E"},
                # hero field = deep petrol trust block with white text (C2 signature)
                "hero": {"fill": "#0F5A66", "on": "#FFFFFF", "on2": "#C3DEE3"},
            },
            "dark": {
                "canvas": "#0B151A", "surface": "#13232A", "surface2": "#182B33",
                "group": "#1D3039", "ink": "#EEF5F7", "ink2": "#B7C9D0", "ink3": "#8FA6AE",
                "border": "#2C454F", "borderStrong": "#54707B",
                "brand": {"fill": "#DE7B4B", "onfill": "#2B0F04", "text": "#F0A276",
                          "soft": "#3C2417", "onsoft": "#F6C3A0", "border": "#9C5A34"},
                "trust": {"fill": "#3FA3B2", "onfill": "#06272C", "text": "#74CBD7",
                          "soft": "#153740", "onsoft": "#A5DCE5", "border": "#3F7E8A"},
                "positive": {"fill": "#5FBF85", "onfill": "#062413", "text": "#74D096",
                          "soft": "#16351F", "onsoft": "#9BE0B4", "border": "#3E7A56"},
                "attention": {"fill": "#DDB75F", "onfill": "#231A03", "text": "#E4C175",
                          "soft": "#372D0F", "onsoft": "#F0D489", "border": "#8A6E2E"},
                "negative": {"fill": "#F0988A", "onfill": "#2B0B06", "text": "#F4A396",
                          "soft": "#371D16", "onsoft": "#F7B8AD", "border": "#9C4A3C"},
                "hero": {"fill": "#12525E", "on": "#FFFFFF", "on2": "#BFDDE3"},
            },
        },
    },
    "c3-dynamic-modular": {
        "label": "C3 — Dynamic Modular",
        "modes": {
            "light": {
                "canvas": "#F5F3ED", "surface": "#FFFFFF", "surface2": "#EFECE2",
                "group": "#E9E5D9", "ink": "#191410", "ink2": "#4F483A", "ink3": "#665F4E",
                "border": "#D9D3C3", "borderStrong": "#17120D",
                "brand": {"fill": "#6C2BD9", "onfill": "#FFFFFF", "text": "#5B22B8",
                          "soft": "#EFE8FB", "onsoft": "#4A1B99", "border": "#6C2BD9"},
                "trust": {"fill": "#0E7480", "onfill": "#FFFFFF", "text": "#0A5F6A",
                          "soft": "#E2F1F3", "onsoft": "#085159", "border": "#0E7480"},
                "positive": {"fill": "#23804C", "onfill": "#FFFFFF", "text": "#186636",
                          "soft": "#E4F2E6", "onsoft": "#14592D", "border": "#23804C"},
                "attention": {"fill": "#8F6A0B", "onfill": "#FFFFFF", "text": "#755708",
                          "soft": "#FAF0D5", "onsoft": "#614505", "border": "#8F6A0B"},
                "negative": {"fill": "#BB2A1D", "onfill": "#FFFFFF", "text": "#9E1F14",
                          "soft": "#FBE9E5", "onsoft": "#8C1810", "border": "#BB2A1D"},
                # C3 zone accents (home / work / tools / market)
                "zone-work": {"fill": "#0E7480", "onfill": "#FFFFFF", "text": "#0A5F6A"},
                "zone-tools": {"fill": "#9A3B12", "onfill": "#FFFFFF", "text": "#7F300E"},
                "zone-market": {"fill": "#A81E5F", "onfill": "#FFFFFF", "text": "#8C1A51"},
                # hero = brand violet block with white (C3 signature)
                "hero": {"fill": "#5B2CC8", "on": "#FFFFFF", "on2": "#D9CCF6"},
            },
            "dark": {
                "canvas": "#14110D", "surface": "#1E1A14", "surface2": "#252017",
                "group": "#2A2418", "ink": "#F5F1E6", "ink2": "#C8BEA8", "ink3": "#9E937D",
                "border": "#3B3425", "borderStrong": "#F0EAD9",
                "brand": {"fill": "#7C4EE0", "onfill": "#FFFFFF", "text": "#BBA1F7",
                          "soft": "#2C1F4E", "onsoft": "#D2C1FA", "border": "#6E4CC4"},
                "trust": {"fill": "#2FB3C0", "onfill": "#04262A", "text": "#7FD3DD",
                          "soft": "#123640", "onsoft": "#A7E3EA", "border": "#2E7A84"},
                "positive": {"fill": "#5FBF85", "onfill": "#062413", "text": "#7BD39A",
                          "soft": "#17351F", "onsoft": "#9BE0B4", "border": "#3E7A56"},
                "attention": {"fill": "#DDB75F", "onfill": "#231A03", "text": "#E6C274",
                          "soft": "#372D0F", "onsoft": "#F1D68C", "border": "#8A6E2E"},
                "negative": {"fill": "#F0988A", "onfill": "#2B0B06", "text": "#F4A396",
                          "soft": "#371D16", "onsoft": "#F7B8AD", "border": "#9C4A3C"},
                "zone-work": {"fill": "#2FB3C0", "onfill": "#04262A", "text": "#7FD3DD"},
                "zone-tools": {"fill": "#D08A5C", "onfill": "#26110A", "text": "#DFA87E"},
                "zone-market": {"fill": "#E26AA8", "onfill": "#2B0A1C", "text": "#EC93BE"},
                "hero": {"fill": "#6D3BD8", "on": "#FFFFFF", "on2": "#E9E2FC"},
            },
        },
    },
    "selected-direction": {
        "label": "Selected — Candidate DS (C3 refined)",
        "modes": {
            "light": {
                "canvas": "#F5F3ED", "surface": "#FFFFFF", "surface2": "#EFECE2",
                "group": "#E9E5D9", "ink": "#191410", "ink2": "#4F483A", "ink3": "#665F4E",
                "border": "#D9D3C3", "borderStrong": "#17120D",
                "brand": {"fill": "#5B2CC8", "onfill": "#FFFFFF", "text": "#5B22B8",
                          "soft": "#EFE8FB", "onsoft": "#4A1B99", "border": "#5B2CC8"},
                "trust": {"fill": "#0E7480", "onfill": "#FFFFFF", "text": "#0A5F6A",
                          "soft": "#E2F1F3", "onsoft": "#085159", "border": "#0E7480"},
                "positive": {"fill": "#23804C", "onfill": "#FFFFFF", "text": "#186636",
                          "soft": "#E4F2E6", "onsoft": "#14592D", "border": "#23804C"},
                "attention": {"fill": "#8F6A0B", "onfill": "#FFFFFF", "text": "#755708",
                          "soft": "#FAF0D5", "onsoft": "#614505", "border": "#8F6A0B"},
                "negative": {"fill": "#BB2A1D", "onfill": "#FFFFFF", "text": "#9E1F14",
                          "soft": "#FBE9E5", "onsoft": "#8C1810", "border": "#BB2A1D"},
                "zone-work": {"fill": "#0E7480", "onfill": "#FFFFFF", "text": "#0A5F6A"},
                "zone-tools": {"fill": "#9A3B12", "onfill": "#FFFFFF", "text": "#7F300E"},
                "zone-market": {"fill": "#A81E5F", "onfill": "#FFFFFF", "text": "#8C1A51"},
                "hero": {"fill": "#5B2CC8", "on": "#FFFFFF", "on2": "#D9CCF6"},
            },
            "dark": {
                "canvas": "#14110D", "surface": "#1E1A14", "surface2": "#252017",
                "group": "#2A2418", "ink": "#F5F1E6", "ink2": "#C8BEA8", "ink3": "#9E937D",
                "border": "#3B3425", "borderStrong": "#F0EAD9",
                "brand": {"fill": "#7C4EE0", "onfill": "#FFFFFF", "text": "#BBA1F7",
                          "soft": "#2C1F4E", "onsoft": "#D2C1FA", "border": "#6E4CC4"},
                "trust": {"fill": "#2FB3C0", "onfill": "#04262A", "text": "#7FD3DD",
                          "soft": "#123640", "onsoft": "#A7E3EA", "border": "#2E7A84"},
                "positive": {"fill": "#5FBF85", "onfill": "#062413", "text": "#7BD39A",
                          "soft": "#17351F", "onsoft": "#9BE0B4", "border": "#3E7A56"},
                "attention": {"fill": "#DDB75F", "onfill": "#231A03", "text": "#E6C274",
                          "soft": "#372D0F", "onsoft": "#F1D68C", "border": "#8A6E2E"},
                "negative": {"fill": "#F0988A", "onfill": "#2B0B06", "text": "#F4A396",
                          "soft": "#371D16", "onsoft": "#F7B8AD", "border": "#9C4A3C"},
                "zone-work": {"fill": "#2FB3C0", "onfill": "#04262A", "text": "#7FD3DD"},
                "zone-tools": {"fill": "#D08A5C", "onfill": "#26110A", "text": "#DFA87E"},
                "zone-market": {"fill": "#E26AA8", "onfill": "#2B0A1C", "text": "#EC93BE"},
                "hero": {"fill": "#6D3BD8", "on": "#FFFFFF", "on2": "#E9E2FC"},
            },
        },
    },
}

# soft fills that carry alpha in hex8 -> flatten onto surface for measurement
def flatten(hexcolor, base):
    h = hexcolor.lstrip("#")
    if len(h) == 8:
        a = int(h[6:8], 16) / 255.0
        return mix("#" + h[0:6], base, a)
    return "#" + h[0:6]

def build_pairs(dir_id, spec):
    """Return list of {fg,bg,use,min} for every operational pair."""
    pairs = []
    for mode, m in spec["modes"].items():
        pre = f"[{mode}] "
        base_surface = m["surface"]
        # neutrals
        pairs += [
            (m["ink"], m["canvas"], pre + "نص أساسي على الخلفية", 4.5),
            (m["ink"], m["surface"], pre + "نص أساسي على السطح", 4.5),
            (m["ink2"], m["surface"], pre + "نص ثانوي على السطح", 4.5),
            (m["ink3"], m["surface"], pre + "نص خافت على السطح", 4.5),
            (m["borderStrong"], m["surface"], pre + "حد الضوابط على السطح", 3.0),
        ]
        # hero block
        pairs += [
            (m["hero"]["on"], m["hero"]["fill"], pre + "نص البطل الأساسي على حقل البطل", 4.5),
            (m["hero"]["on2"], m["hero"]["fill"], pre + "نص البطل الثانوي على حقل البطل", 4.5),
        ]
        # semantic roles
        for role in ROLES:
            r = m.get(role)
            if not r:
                continue
            soft = flatten(r["soft"], base_surface)
            pairs += [
                (r["text"], m["surface"], pre + f"نص {role} على السطح", 4.5),
                (r["onfill"], r["fill"], pre + f"نص على تعبئة {role}", 4.5),
                (r["onsoft"], soft, pre + f"نص على تعبئة {role} الناعمة", 4.5),
                (r["fill"], m["surface"], pre + f"تعبئة {role} مقابل السطح (حدود مكون)", 3.0),
            ]
        # C3 zones
        for zname in ("zone-work", "zone-tools", "zone-market"):
            z = m.get(zname)
            if z:
                pairs += [
                    (z["text"], m["surface"], pre + f"نص منطقة {zname} على السطح", 4.5),
                    (z["onfill"], z["fill"], pre + f"نص على تعبئة {zname}", 4.5),
                ]
        # الكنكة الدافئة للاتجاه المختبر فقط
        if dir_id == "selected-direction":
            wa = WARM_ACCENT[mode]
            soft = flatten(wa["soft"], base_surface)
            pairs += [
                (wa["text"], m["surface"], pre + "نص الكنكة الدافئة على السطح", 4.5),
                (wa["onfill"], wa["fill"], pre + "نص على تعبئة الكنكة الدافئة", 4.5),
                (wa["onsoft"], soft, pre + "نص على تعبئة الكنكة الناعمة", 4.5),
                (wa["fill"], m["surface"], pre + "تعبئة الكنكة مقابل السطح (حدود مكون)", 3.0),
            ]
    return [(fg, bg, use, mn) for fg, bg, use, mn in pairs]

def main():
    os.makedirs(f"{BASE}/tokens", exist_ok=True)
    os.makedirs(f"{BASE}/accessibility", exist_ok=True)
    os.makedirs(f"{BASE}/design-source", exist_ok=True)

    all_rows = []
    failures = []
    contrast_data = {}

    for dir_id, spec in DIRECTIONS.items():
        rows = []
        for fg, bg, use, mn in build_pairs(dir_id, spec):
            r = ratio(fg, bg)
            ok = r >= mn
            rows.append({"fg": fg, "bg": bg, "use": use, "min": mn, "ratio": round(r, 2), "pass": ok})
            if not ok:
                failures.append(f"{dir_id}: {use} {fg} on {bg} = {r:.2f} < {mn}")
        all_rows.append((dir_id, spec["label"], rows))
        contrast_data[dir_id] = rows

        # tokens.json
        with open(f"{BASE}/tokens/{dir_id}.tokens.json", "w") as f:
            json.dump({"direction": dir_id, "label": spec["label"], "modes": spec["modes"],
                       "pairs": rows}, f, ensure_ascii=False, indent=2)
        # tokens.css
        css = [f"/* {spec['label']} — Design Tokens (generated by design_tokens.py) */"]
        for mode, m in spec["modes"].items():
            sel = ":root" if mode == "light" else '[data-theme="dark"]'
            if mode == "light":
                css.append(f":root, [data-theme=\"light\"] {{")
            else:
                css.append(f"[data-theme=\"dark\"] {{")
            for k in ("canvas", "surface", "surface2", "group", "ink", "ink2", "ink3", "border", "borderStrong"):
                css.append(f"  --c-{k}: {m[k]};")
            for role in ROLES + [z for z in m if z.startswith("zone-")]:
                r = m.get(role)
                if r:
                    css.append(f"  --c-{role}-fill: {r['fill']};")
                    css.append(f"  --c-{role}-onfill: {r['onfill']};")
                    css.append(f"  --c-{role}-text: {r['text']};")
                    if "soft" in r:
                        css.append(f"  --c-{role}-soft: {r['soft']};")
                        css.append(f"  --c-{role}-onsoft: {r['onsoft']};")
            css.append(f"  --c-hero-fill: {m['hero']['fill']};")
            css.append(f"  --c-hero-on: {m['hero']['on']};")
            css.append(f"  --c-hero-on2: {m['hero']['on2']};")
            if dir_id == "selected-direction":
                wa = WARM_ACCENT[mode]
                css.append(f"  --c-warm-fill: {wa['fill']};")
                css.append(f"  --c-warm-onfill: {wa['onfill']};")
                css.append(f"  --c-warm-text: {wa['text']};")
                css.append(f"  --c-warm-soft: {wa['soft']};")
                css.append(f"  --c-warm-onsoft: {wa['onsoft']};")
            css.append("}")
        with open(f"{BASE}/tokens/{dir_id}.tokens.css", "w") as f:
            f.write("\n".join(css) + "\n")

    # contrast-results.md
    md = ["# نتائج قياس التباين — WCAG 2.2", "",
          "**Agent 02 — Independent | الأداة: `design_tokens.py` (نسبة التباين وفق WCAG 2.2 نسبة الإضاءة النسبية)**", "",
          "الحد الأدنى: نص عادي 4.5:1 — نص كبير/حدود مكونات 3:1. التعبئات الناعمة ذات الشفافية تُسطَّح على السطح المقصود قبل القياس.", ""]
    for dir_id, label, rows in all_rows:
        n_pass = sum(1 for r in rows if r["pass"])
        md.append(f"## {label} (`{dir_id}`)")
        md.append("")
        md.append(f"**{n_pass}/{len(rows)} زوجًا ناجحًا.**")
        md.append("")
        md.append("| المقدمة | الخلفية | الاستخدام | الحد | النسبة | النتيجة |")
        md.append("|---|---|---|---:|---:|---|")
        for r in rows:
            md.append(f"| `{r['fg']}` | `{r['bg']}` | {r['use']} | {r['min']:.1f} | **{r['ratio']:.2f}:1** | {'✅' if r['pass'] else '❌'} |")
        md.append("")
    with open(f"{BASE}/accessibility/contrast-results.md", "w") as f:
        f.write("\n".join(md) + "\n")

    with open(f"{BASE}/design-source/contrast-data.json", "w") as f:
        json.dump(contrast_data, f, ensure_ascii=False, indent=1)

    if failures:
        print("CONTRAST GATE FAILURES:")
        for f_ in failures:
            print("  FAIL", f_)
        sys.exit(1)
    total = sum(len(rows) for _, _, rows in all_rows)
    print(f"ALL PASS: {total} pairs across 3 directions x 2 modes.")

if __name__ == "__main__":
    main()
