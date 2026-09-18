#!/usr/bin/env python3
"""
Micro Bold Modular — Agent 03 contrast verification tool.
Computes WCAG 2.x contrast ratios for all operational color pairs of C1/C2/C3
(light + dark). Writes JSON evidence + markdown tables for foundation boards.
"""
import json, sys, os

def srgb(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def lum(hexcolor):
    hexcolor = hexcolor.lstrip('#')
    r, g, b = (int(hexcolor[i:i+2], 16) for i in (0, 2, 4))
    return 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b)

def ratio(fg, bg):
    l1, l2 = lum(fg), lum(bg)
    if l1 < l2:
        l1, l2 = l2, l1
    return round((l1 + 0.05) / (l2 + 0.05), 2)

# ---- Palette definitions (values chosen, then verified here) ----
PALETTES = {
  "c1-warm-bold": {
    "light": {
      "canvas": "#FAF6F1", "surface": "#FFFFFF", "group": "#F4ECE3",
      "ink": "#231A14", "ink2": "#6D5E52", "inkFaint": "#7A6A5C",
      "brand.fill": "#D96A45", "brand.deep": "#A03A1D",
      "onBrand": "#2B130A",
      "trust": "#1F5E8C", "trustTint": "#E3EEF6",
      "pos": "#1E6E42", "posTint": "#E6F2EA", "posOn": "#0F3320",
      "neg": "#B32318", "negTint": "#FBEAE7", "negOn": "#3A0C07",
      "att": "#8A5300", "attTint": "#FAEEDA", "attOn": "#2E1D00",
      "focus": "#A03A1D", "fieldBorder": "#937F6C", "navSurface": "#FFFFFF"
    },
    "dark": {
      "canvas": "#1E1712", "surface": "#291F18", "group": "#33271E",
      "ink": "#F4EBE1", "ink2": "#C4B2A3", "inkFaint": "#A08D7E",
      "brand.fill": "#E58254", "brand.deep": "#F09A6F",
      "onBrand": "#2B130A",
      "trust": "#7FB3DA", "trustTint": "#22333F",
      "pos": "#6FC492", "posTint": "#1B3226", "posOn": "#DFF3E6",
      "neg": "#F09A8C", "negTint": "#3B1D17", "negOn": "#FBE7E3",
      "att": "#E5B96A", "attTint": "#332711", "attOn": "#F8ECD2",
      "focus": "#E58254", "fieldBorder": "#83705B", "navSurface": "#241B15"
    }
  },
  "c2-confident-bold": {
    "light": {
      "white": "#FFFFFF",
      "canvas": "#F5F6F8", "surface": "#FFFFFF", "group": "#EDF0F3",
      "ink": "#16202B", "ink2": "#5B6B7A", "inkFaint": "#5D6F80",
      "brand.fill": "#D96A45", "brand.deep": "#A03A1D",
      "onBrand": "#2B130A",
      "trust": "#174E77", "trust.fill": "#174E77", "trustDeep": "#0F3A5C",
      "trustTint": "#E4EDF5",
      "pos": "#1E6E42", "posTint": "#E6F2EA", "posOn": "#0F3320",
      "neg": "#B32318", "negTint": "#FBEAE7", "negOn": "#3A0C07",
      "att": "#8A5300", "attTint": "#FAEEDA", "attOn": "#2E1D00",
      "focus": "#174E77", "fieldBorder": "#8593A1", "navSurface": "#FFFFFF"
    },
    "dark": {
      "white": "#FFFFFF",
      "canvas": "#131A21", "surface": "#1B242D", "group": "#232E39",
      "ink": "#EAF0F5", "ink2": "#AEBECB", "inkFaint": "#8DA0B0",
      "brand.fill": "#E58254", "brand.deep": "#F09A6F",
      "onBrand": "#2B130A",
      "trust": "#6FA8D6", "trust.fill": "#2C5E88", "trustDeep": "#9CC3E2",
      "trustTint": "#1D3245",
      "pos": "#6FC492", "posTint": "#1B3226", "posOn": "#DFF3E6",
      "neg": "#F09A8C", "negTint": "#3B1D17", "negOn": "#FBE7E3",
      "att": "#E5B96A", "attTint": "#332711", "attOn": "#F8ECD2",
      "focus": "#6FA8D6", "fieldBorder": "#5F7285", "navSurface": "#18202A"
    }
  },
  "c3-dynamic-modular": {
    "light": {
      "workText": "#FFFFFF", "financeText": "#FFFFFF", "toolsText": "#FFFFFF", "marketText": "#FFFFFF",
      "canvas": "#F4F3F0", "surface": "#FFFFFF", "group": "#ECEAE5",
      "ink": "#1F1C19", "ink2": "#63594F", "inkFaint": "#73675E",
      "brand.fill": "#D96A45", "brand.deep": "#A03A1D",
      "onBrand": "#2B130A",
      "trust": "#1F5E8C", "trustTint": "#E3EEF6",
      "work": "#6E3B85", "workTint": "#F0E8F5",
      "finance": "#0E6B6B", "financeTint": "#E2F1F1",
      "tools": "#44515E", "toolsTint": "#EBEDF0",
      "market": "#9C4460", "marketTint": "#F7E8ED",
      "pos": "#1E6E42", "posTint": "#E6F2EA", "posOn": "#0F3320",
      "neg": "#B32318", "negTint": "#FBEAE7", "negOn": "#3A0C07",
      "att": "#8A5300", "attTint": "#FAEEDA", "attOn": "#2E1D00",
      "focus": "#1F1C19", "fieldBorder": "#8B8478", "navSurface": "#FFFFFF"
    },
    "dark": {
      "workText": "#1F1C19", "financeText": "#1F1C19", "toolsText": "#1F1C19", "marketText": "#1F1C19",
      "canvas": "#1A1815", "surface": "#24211D", "group": "#2C2823",
      "ink": "#F1EDE6", "ink2": "#BCB2A5", "inkFaint": "#9F9184",
      "brand.fill": "#E58254", "brand.deep": "#F09A6F",
      "onBrand": "#2B130A",
      "trust": "#7FB3DA", "trustTint": "#20313C",
      "work": "#C49AD8", "workTint": "#2F2138",
      "finance": "#6FC4C4", "financeTint": "#123030",
      "tools": "#A9B4C0", "toolsTint": "#23272C",
      "market": "#E094AB", "marketTint": "#361C24",
      "pos": "#6FC492", "posTint": "#1B3226", "posOn": "#DFF3E6",
      "neg": "#F09A8C", "negTint": "#3B1D17", "negOn": "#FBE7E3",
      "att": "#E5B96A", "attTint": "#332711", "attOn": "#F8ECD2",
      "focus": "#E58254", "fieldBorder": "#7A6E5F", "navSurface": "#201D19"
    }
  }
}

# ---- Pair specs: (name, fg, bg, requirement)  requirement: normal 4.5 / large 3.0 / ui 3.0 ----
def pairs_for(mode):
    P = []
    def add(name, fg, bg, req):
        P.append((name, fg, bg, req))
    # Core reading pairs
    add("ink on canvas (body)", "ink", "canvas", 4.5)
    add("ink on surface (body)", "ink", "surface", 4.5)
    add("ink on group (body)", "ink", "group", 4.5)
    add("ink2 on surface (secondary)", "ink2", "surface", 4.5)
    add("ink2 on canvas (secondary)", "ink2", "canvas", 4.5)
    add("ink2 on group (secondary)", "ink2", "group", 4.5)
    add("inkFaint on surface (timestamps 12.5px)", "inkFaint", "surface", 4.5)
    add("inkFaint on canvas", "inkFaint", "canvas", 4.5)
    # Brand
    add("onBrand on brand.fill (button text)", "onBrand", "brand.fill", 4.5)
    add("brand.deep on surface (brand text)", "brand.deep", "surface", 4.5)
    add("brand.deep on canvas (brand text)", "brand.deep", "canvas", 4.5)
    add("brand.deep on brand.fill? (never used)", "brand.deep", "brand.fill", 99)  # informational only
    # Trust
    add("trust on surface (link/nav text)", "trust", "surface", 4.5)
    add("trust on canvas", "trust", "canvas", 4.5)
    add("trust on trustTint", "trust", "trustTint", 4.5)
    # Semantic text pairs
    add("pos on surface", "pos", "surface", 4.5)
    add("pos on posTint", "pos", "posTint", 4.5)
    add("posOn on posTint (dark ink on tint chip)", "posOn", "posTint", 4.5)
    add("neg on surface", "neg", "surface", 4.5)
    add("neg on negTint", "neg", "negTint", 4.5)
    add("negOn on negTint (dark ink on tint chip)", "negOn", "negTint", 4.5)
    add("att on surface", "att", "surface", 4.5)
    add("att on attTint", "att", "attTint", 4.5)
    add("attOn on attTint (dark ink on tint chip)", "attOn", "attTint", 4.5)
    # Hero number on fill (large text 40px bold -> 3.0, but we target 4.5)
    add("onBrand on brand.fill (hero number, large)", "onBrand", "brand.fill", 3.0)
    if mode == "light":
        add("ink on brand.fill (hero focus outline, light)", "ink", "brand.fill", 3.0)
    else:
        add("onBrand on brand.fill (hero focus outline, dark)", "onBrand", "brand.fill", 3.0)
    # UI / boundaries
    add("fieldBorder on surface (>=3 ui)", "fieldBorder", "surface", 3.0)
    add("focus on surface (focus ring >=3)", "focus", "surface", 3.0)
    add("focus on canvas (focus ring >=3)", "focus", "canvas", 3.0)
    # Nav
    add("ink on navSurface (nav label)", "ink", "navSurface", 4.5)
    add("ink2 on navSurface (inactive tab)", "ink2", "navSurface", 3.0)
    add("brand.fill on navSurface (active tab icon, ui)", "brand.fill", "navSurface", 3.0)
    return P

EXTRA = {
  "c2-confident-bold": {
    "light": [("white on trust.fill (hero text/chip bg, filter chip)","white","trust.fill",4.5)],
    "dark": [("white on trust.fill (hero text/chip bg, filter chip)","white","trust.fill",4.5)]
  },
  "c3-dynamic-modular": {
    "light": [("moduleText on work module (plate/topzone/focus)","workText","work",4.5),
               ("moduleText on finance module","financeText","finance",4.5),
               ("moduleText on tools module","toolsText","tools",4.5),
               ("moduleText on market module","marketText","market",4.5),
               ("work on surface","work","surface",4.5),("work on workTint","work","workTint",4.5),
               ("finance on surface","finance","surface",4.5),("finance on financeTint","finance","financeTint",4.5),
               ("tools on surface","tools","surface",4.5),("tools on toolsTint","tools","toolsTint",4.5),
               ("market on surface","market","surface",4.5),("market on marketTint","market","marketTint",4.5)],
    "dark":  [("moduleText on work module (plate/topzone/focus)","workText","work",4.5),
               ("moduleText on finance module","financeText","finance",4.5),
               ("moduleText on tools module","toolsText","tools",4.5),
               ("moduleText on market module","marketText","market",4.5),
               ("work on surface","work","surface",4.5),("work on workTint","work","workTint",4.5),
               ("finance on surface","finance","surface",4.5),("finance on financeTint","finance","financeTint",4.5),
               ("tools on surface","tools","surface",4.5),("tools on toolsTint","tools","toolsTint",4.5),
               ("market on surface","market","surface",4.5),("market on marketTint","market","marketTint",4.5)]
  }
}

def check(direction):
    result = {"direction": direction, "light": [], "dark": [], "failures": []}
    for mode in ("light", "dark"):
        pal = PALETTES[direction][mode]
        plist = pairs_for(mode) + EXTRA.get(direction, {}).get(mode, [])
        for name, fgk, bgk, req in plist:
            fg, bg = pal[fgk], pal[bgk]
            r = ratio(fg, bg)
            # req 99 = informational
            ok = True if req == 99 else (r >= req)
            entry = {"pair": name, "fg": fg, "bg": bg, "ratio": r, "req": req, "pass": ok}
            result[mode].append(entry)
            if not ok:
                result["failures"].append(f"[{direction}/{mode}] {name}: {fg} on {bg} = {r}:1 (need {req}:1)")
    return result

def main():
    out_dir = "/home/z/my-project/repos/Micro-Bold-Modular-Design-Handoff-V1/agent-runs/agent-03-multi-agent/tokens"
    os.makedirs(out_dir, exist_ok=True)
    all_results = {}
    total_fail = 0
    for d in PALETTES:
        res = check(d)
        all_results[d] = res
        total_fail += len(res["failures"])
    with open(os.path.join(out_dir, "contrast-evidence.json"), "w", encoding="utf-8") as f:
        json.dump({"palettes": PALETTES, "results": all_results}, f, ensure_ascii=False, indent=2)
    for d, res in all_results.items():
        md = [f"# Contrast Evidence — {d}\n"]
        for mode in ("light", "dark"):
            md.append(f"\n## {mode.capitalize()}\n")
            md.append("| Pair | Foreground | Background | Ratio | Required | Result |")
            md.append("|---|---|---|---:|---:|---|")
            for e in res[mode]:
                req = "info" if e["req"] == 99 else f"{e['req']}:1"
                md.append(f"| {e['pair']} | `{e['fg']}` | `{e['bg']}` | **{e['ratio']}:1** | {req} | {'PASS' if e['pass'] else '**FAIL**'} |")
        with open(os.path.join(out_dir, f"{d}-contrast.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(md))
    if total_fail:
        print(f"FAILURES ({total_fail}):")
        for d, res in all_results.items():
            for line in res["failures"]:
                print("  " + line)
        sys.exit(1)
    else:
        print("ALL PAIRS PASS")

if __name__ == "__main__":
    main()
