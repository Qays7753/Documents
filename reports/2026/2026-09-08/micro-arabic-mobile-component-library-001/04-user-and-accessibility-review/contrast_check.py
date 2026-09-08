#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
contrast_check.py — Agent 04 evidence script
Run: 20260908T133450Z-16d11 · Task 3 (user viewpoint, interaction, a11y, verification)

Purpose
-------
Independently RECOMPUTE every WCAG 2.2 contrast ratio claimed in
02-visual-identity/color-role-map.md (Agent 02), plus the focus-ring
candidates proposed across Agent 01 (brand-atmosphere ring for inputs),
Agent 02 (ink-strong ring) and Agent 03 (brand-ink ring), plus the
alpha composites (press overlay, scrim), plus the QuickActionRail peek
arithmetic of Agent 03's variant-state-matrix.md.

WCAG 2.2 thresholds used:
  4.5:1  normal text               (SC 1.4.3)
  3.0:1  large text (>=24px, or >=18.66px bold) and non-text UI/graphics (SC 1.4.11)
  "LARGE ONLY" verdicts below follow Agent 02's own labelling convention.

Large-text "bold" note: WCAG defines the 14pt-bold threshold as bold weight.
Agent 02 treats 600 as bold-capable; this script flags that interpretation
separately (see report). All ratios are pure math and weight-agnostic.
"""

# --------------------------------------------------------------------------
# 1. Tokens (SPEC §6.3 — exact)
# --------------------------------------------------------------------------
T = {
    "brand-atmosphere": "#CC785C",
    "brand-tint":       "#F7EAE4",
    "brand-ink":        "#964E33",
    "on-brand":         "#FFFFFF",
    "canvas":           "#FAF9F5",
    "surface":          "#FFFFFF",
    "sunken":           "#F0EEE6",
    "ink-strong":       "#1F1E1D",
    "ink":              "#33322E",
    "ink-muted":        "#6E6A60",
    "ink-subtle":       "#767265",
    "ink-disabled":     "#B7B2A6",
    "line-soft":        "#EAE6DC",
    "line-strong":      "#DED9CB",
    "positive":         "#2E7D57",
    "positive-tint":    "#E7EFE7",
    "danger":           "#B42318",
    "danger-tint":      "#F7E7E2",
    "warning":          "#8A6520",
    "warning-tint":     "#F4EDD8",
    "info":             "#3E5C76",
    "info-tint":        "#E8EDF1",
    "ink-45":           "#1F1E1D",   # scrim cast (alpha handled separately)
}
PRESS_OVERLAY = ("#1F1E1D", 0.08)    # press-overlay  8%
SCRIM         = ("#1F1E1D", 0.45)    # scrim         45%


# --------------------------------------------------------------------------
# 2. WCAG relative luminance + ratio + alpha composite
# --------------------------------------------------------------------------
def h2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(h):
    r, g, b = (lin(x) for x in h2rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def cr(fg, bg):
    l1, l2 = lum(fg), lum(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def comp(fg_hex, alpha, bg_hex):
    """Alpha-composite fg over bg, return composite hex."""
    f, b = h2rgb(fg_hex), h2rgb(bg_hex)
    return "#%02X%02X%02X" % tuple(
        round(f[i] * alpha + b[i] * (1 - alpha)) for i in range(3)
    )


def verdict_text(r):
    if r >= 4.5:
        return "PASS"
    if r >= 3.0:
        return "LARGE-ONLY"
    return "FAIL"


def verdict_gfx(r):
    return "PASS" if r >= 3.0 else "FAIL(<3:1)"


def row(fg, bg, claimed, kind="text"):
    r = cr(T[fg], T[bg])
    v = verdict_text(r) if kind == "text" else verdict_gfx(r)
    try:
        delta = abs(r - float(claimed))
        agree = "AGREE" if delta <= 0.02 else "DISAGREE"
    except (TypeError, ValueError):
        delta, agree = None, "n/a"
    return (fg, bg, round(r, 2), claimed, delta, v, agree)


# --------------------------------------------------------------------------
# 3. Every pair claimed in color-role-map.md §4 (text) / §5 (graphics)
#    claimed = the number printed by Agent 02 (None = not claimed there)
# --------------------------------------------------------------------------
TEXT_PAIRS = [
    ("ink-strong", "surface", "16.64"), ("ink-strong", "canvas", "15.80"),
    ("ink-strong", "sunken", "14.33"),
    ("ink", "surface", "12.83"), ("ink", "canvas", "12.18"),
    ("ink", "sunken", "11.05"),
    ("ink-muted", "surface", "5.39"), ("ink-muted", "canvas", "5.12"),
    ("ink-muted", "sunken", "4.64"),
    ("ink-subtle", "surface", "4.81"), ("ink-subtle", "canvas", "4.57"),
    ("ink-subtle", "sunken", "4.14"),
    ("ink-disabled", "surface", "2.11"), ("ink-disabled", "canvas", "2.01"),
    ("brand-ink", "surface", "6.11"), ("brand-ink", "canvas", "5.80"),
    ("brand-ink", "sunken", "5.26"), ("brand-ink", "brand-tint", "5.20"),
    ("ink-strong", "brand-atmosphere", "5.08"),
    ("ink", "brand-atmosphere", "3.92"),
    ("ink-muted", "brand-atmosphere", "1.65"),
    ("on-brand", "brand-ink", "6.11"),
    ("on-brand", "brand-atmosphere", "3.28"),
    ("positive", "surface", "5.02"), ("positive", "canvas", "4.76"),
    ("positive", "sunken", "4.32"), ("positive", "positive-tint", "4.27"),
    ("danger", "surface", "6.57"), ("danger", "canvas", "6.24"),
    ("danger", "sunken", "5.66"), ("danger", "danger-tint", "5.47"),
    ("warning", "surface", "5.30"), ("warning", "canvas", "5.03"),
    ("warning", "warning-tint", "4.53"),
    ("info", "surface", "7.01"), ("info", "canvas", "6.65"),
    ("info", "info-tint", "5.94"),
    ("on-brand", "positive", "5.02"), ("on-brand", "danger", "6.57"),
    ("on-brand", "warning", "5.30"), ("on-brand", "info", "7.01"),
    ("ink-strong", "positive-tint", "14.19"),
    ("ink", "danger-tint", "10.68"), ("ink", "warning-tint", "10.97"),
    ("ink", "info-tint", "10.89"),
    ("ink-muted", "positive-tint", "4.60"),
    # claimed in §3 prose only ("ink on tints 10.7–11.0")
    ("ink", "positive-tint", "10.7"),
]

GRAPHIC_PAIRS = [
    ("brand-atmosphere", "surface", "3.28"),
    ("brand-atmosphere", "canvas", "3.11"),
    ("brand-atmosphere", "brand-tint", "2.78"),
    ("brand-ink", "positive-tint", "5.21"),
    ("positive", "positive-tint", "4.27"),
    ("danger", "danger-tint", "5.47"),
    ("warning", "warning-tint", "4.53"),
    ("info", "info-tint", "5.94"),
    ("line-strong", "surface", "1.41"),
    ("line-soft", "surface", "1.25"),
    ("line-strong", "canvas", "1.34"),
    ("line-soft", "canvas", "1.18"),
    ("surface", "canvas", "1.05"),
    ("sunken", "surface", "1.16"),
    ("sunken", "canvas", "1.10"),
]

# Focus-ring candidates — the three different ring colors proposed by
# Agents 01 (brand-atmosphere for input focus), 02 (ink-strong) and
# 03 (brand-ink). Audited as GRAPHICS against every surface/tint they
# can be drawn over (3:1, SC 1.4.11 / 2.4.11 visibility aid).
RING_SURFACES = ["surface", "canvas", "sunken", "brand-tint", "positive-tint",
                 "danger-tint", "warning-tint", "info-tint", "brand-atmosphere"]
RING_CANDIDATES = ["ink-strong", "brand-ink", "brand-atmosphere"]


# --------------------------------------------------------------------------
# 4. Alpha composites (color-role-map §6 + component-architecture §7 claim)
# --------------------------------------------------------------------------
def composite_audit():
    out = []
    press_surface = comp(*PRESS_OVERLAY, T["surface"])
    press_brandink = comp(*PRESS_OVERLAY, T["brand-ink"])
    press_canvas = comp(*PRESS_OVERLAY, T["canvas"])
    scrim_canvas = comp(*SCRIM, T["canvas"])
    scrim_surface = comp(*SCRIM, T["surface"])
    out.append(("press 8% over surface", press_surface,
                round(cr(T["ink"], press_surface), 2), "ink", "10.96"))
    out.append(("press 8% over surface", press_surface,
                round(cr(T["ink-muted"], press_surface), 2), "ink-muted", "4.61"))
    out.append(("press 8% over brand-ink", press_brandink,
                round(cr(T["on-brand"], press_brandink), 2), "on-brand", "6.69"))
    out.append(("press 8% over canvas", press_canvas,
                round(cr(T["ink-strong"], press_canvas), 2), "ink-strong", None))
    out.append(("scrim 45% over canvas", scrim_canvas,
                round(cr(T["on-brand"], scrim_canvas), 2), "on-brand", "2.96"))
    out.append(("scrim 45% over surface", scrim_surface,
                round(cr(T["on-brand"], scrim_surface), 2), "on-brand", "n/a"))
    return out, (press_surface, press_brandink, press_canvas,
                 scrim_canvas, scrim_surface)


# --------------------------------------------------------------------------
# 5. QuickActionRail peek arithmetic (Agent 03 formula, recomputed)
# --------------------------------------------------------------------------
def rail_peek(widths=(320, 360, 390, 430), tile=88, gap=8, pad=16):
    res = []
    for W in widths:
        # tiles begin at pad; count full tiles whose END fits inside W
        x = pad
        n = 0
        while True:
            end = x + tile
            if end <= W:
                n += 1
                x = end + gap
            else:
                break
        peek = W - (pad + n * tile + (n - 1) * gap + gap)
        res.append((W, n, round(peek, 1)))
    return res


# --------------------------------------------------------------------------
# 6. Print report
# --------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("AGENT 04 — INDEPENDENT CONTRAST RECOMPUTATION (WCAG 2.2)")
    print("tokens: SPEC 6.3 exact · thresholds 4.5:1 normal text / 3:1 large+gfx")
    print("=" * 78)

    print("\n--- TEXT PAIRS (color-role-map.md section 4) -------------------------")
    print(f"{'fg':16}{'bg':18}{'computed':>9} {'claimed':>8} {'d':>6}  verdict        agree")
    dis = 0
    for fg, bg, cl in TEXT_PAIRS:
        r = row(fg, bg, cl, "text")
        if r[6] == "DISAGREE":
            dis += 1
        print(f"{r[0]:16}{r[1]:18}{r[2]:>9} {cl:>8} "
              f"{('%.2f' % r[4]) if r[4] is not None else '  —':>6}  {r[5]:14} {r[6]}")

    print("\n--- GRAPHIC / STRUCTURE PAIRS (color-role-map.md section 5, 3:1) -----")
    print(f"{'fg':16}{'bg':18}{'computed':>9} {'claimed':>8}  verdict        agree")
    for fg, bg, cl in GRAPHIC_PAIRS:
        r = row(fg, bg, cl, "gfx")
        if r[6] == "DISAGREE":
            dis += 1
        print(f"{r[0]:16}{r[1]:18}{r[2]:>9} {cl:>8}  {r[5]:14} {r[6]}")

    print("\n--- FOCUS-RING CANDIDATES vs every drawable surface (3:1, 1.4.11) ---")
    print(f"{'ring color':16}{'over':18}{'ratio':>9}  verdict")
    for ring in RING_CANDIDATES:
        for s in RING_SURFACES:
            r = cr(T[ring], T[s])
            print(f"{ring:16}{s:18}{round(r,2):>9}  {verdict_gfx(r)}")
        print("-" * 60)

    print("\n--- ALPHA COMPOSITES (color-role-map.md section 6) -------------------")
    comp_rows, comps = composite_audit()
    for label, hexc, ratio, fg, cl in comp_rows:
        print(f"{label:26} -> {hexc}   {fg:12} {ratio:>6}  (claimed {cl})")

    print("\n--- QUICKACTIONRAIL PEEK (recomputed, geometry locked) ---------------")
    print("width  full tiles  next-tile peek   spec target")
    for W, n, p in rail_peek():
        tgt = "16px documented exception" if W == 320 else ">=28px"
        ok = "OK" if (W == 320 and p >= 16) or (W != 320 and p >= 28) else "FAIL"
        print(f"{W:>5}  {n:>10}  {p:>13}px   {tgt:28} {ok}")

    print("\n--- SUMMARY -----------------------------------------------------------")
    print(f"text+graphic pairs recomputed : {len(TEXT_PAIRS)+len(GRAPHIC_PAIRS)}")
    print(f"disagreements vs Agent 02     : {dis} (tolerance +/-0.02)")


if __name__ == "__main__":
    main()
