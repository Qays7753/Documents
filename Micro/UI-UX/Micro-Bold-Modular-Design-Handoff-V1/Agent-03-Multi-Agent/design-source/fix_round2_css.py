#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round-2 fix batch 1: px→rem fonts, sheet visibility, focus contrast,
size floors, negative hero variants, C2 warm share, C3 energy reduction,
success de-greening, order remaining color. Applies to design/c1|c2|c3.css."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DESIGN = os.path.join(HERE, "design")

def to_rem(m):
    px = float(m.group(1))
    rem = px / 16.0
    txt = f"{round(rem, 5):g}"
    return f"font-size: {txt}rem"

PX_TO_REM = re.compile(r"font-size: ([0-9.]+)px")

COMMON = [
    # D-112: closed sheets not focusable
    (".sheet:not(.sheet--open) { transform: translateY(102%); }", None),  # marker
    # size floors (D-109)
    ("font-size: 0.71875rem", "font-size: 0.75rem"),          # nav labels 11.5 -> 12
    (".tab__label { font-size: 0.75rem; font-weight: 500; }", None),
]

def patch(path, rules):
    s = open(path, encoding="utf-8").read()
    for old, new in rules:
        if new is None:
            continue
        if old not in s:
            print(f"  !! not found in {os.path.basename(path)}: {old[:70]}")
        else:
            s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)
    print(f"patched {os.path.basename(path)}")

# ---------- C1 ----------
def fix_c1():
    p = os.path.join(DESIGN, "c1.css")
    s = open(p, encoding="utf-8").read()
    s = PX_TO_REM.sub(to_rem, s)
    rules = [
        # D-112 sheet visibility
        (".sheet--open { transform: translateY(0); }",
         ".sheet--open { transform: translateY(0); visibility: visible; transition: transform .28s cubic-bezier(.2,.8,.25,1), visibility 0s; }"),
        ("padding: 10px 18px calc(20px + env(safe-area-inset-bottom)); max-width: 430px; margin-inline: auto; transform: translateY(102%); transition: transform .28s cubic-bezier(.2,.8,.25,1); max-height: 78dvh; overflow-y: auto;",
         "padding: 10px 18px calc(20px + env(safe-area-inset-bottom)); max-width: 430px; margin-inline: auto; transform: translateY(102%); visibility: hidden; transition: transform .28s cubic-bezier(.2,.8,.25,1), visibility 0s .28s; max-height: 78dvh; overflow-y: auto;"),
        # D-109 floors
        (".tab__label { font-size: 0.71875rem; font-weight: 500; }", ".tab__label { font-size: 0.75rem; font-weight: 600; }"),
        (".ostep__label { font-size: 0.71875rem; font-weight: 600; color: var(--ink2); white-space: nowrap; }",
         ".ostep__label { font-size: 0.75rem; font-weight: 600; color: var(--ink2); white-space: nowrap; }"),
        (".tag { display: inline-flex; align-items: center; gap: 4px; font-size: 0.71875rem;", ".tag { display: inline-flex; align-items: center; gap: 4px; font-size: 0.75rem;"),
        (".type-chip { font-size: 0.71875rem;", ".type-chip { font-size: 0.75rem;"),
        (".metric-row__value .cur { font-size: 0.75rem; color: var(--ink2); font-weight: 500; }", ".metric-row__value .cur { font-size: 0.8125rem; color: var(--ink2); font-weight: 500; }"),
        (".stage-chip { display: inline-flex; align-items: center; gap: 5px; border-radius: var(--r-chip); padding: 3px 11px; font-size: 0.78125rem;",
         ".stage-chip { display: inline-flex; align-items: center; gap: 5px; border-radius: var(--r-chip); padding: 3px 11px; font-size: 0.8125rem;"),
        (".late-chip { display: inline-flex; align-items: center; gap: 5px; margin-inline-start: auto; color: var(--neg); background: var(--neg-tint); border-radius: var(--r-chip); padding: 3px 10px; font-size: 0.78125rem;",
         ".late-chip { display: inline-flex; align-items: center; gap: 5px; margin-inline-start: auto; color: var(--neg); background: var(--neg-tint); border-radius: var(--r-chip); padding: 3px 10px; font-size: 0.8125rem;"),
        # D-115 negative hero: serious light surface + red frame
        (".hero__actions { margin-top: 16px; display: flex; gap: 10px; position: relative; }",
         ".hero__actions { margin-top: 16px; display: flex; gap: 10px; position: relative; }\n.hero--neg { background: var(--surface); color: var(--ink); border: 2px solid var(--neg); border-inline-start: 6px solid var(--neg); }\n.hero--neg::after { display: none; }\n.hero--neg .hero__result { color: var(--neg); }\n.hero--neg .hero__reason { color: var(--ink); }\n.hero--neg .hero__label { color: var(--ink2); }\n.hero--neg .hero__mini .m-value { color: var(--ink); }\n.hero--neg .hero__mini .m-label { color: var(--ink2); }"),
        # D-111 focus on hero in dark: on-brand
        (".hero :focus-visible, .btn--primary:focus-visible { outline-color: var(--ink); }",
         ".hero :focus-visible, .btn--primary:focus-visible { outline-color: var(--ink); }\n[data-theme=\"dark\"] .hero :focus-visible { outline-color: var(--on-brand); }"),
        # D-104 success de-green: system trust treatment
        (".success-card__badge { width: 58px; height: 58px; border-radius: 50%; background: var(--pos-tint); color: var(--pos); display: grid; place-items: center; margin-inline: auto; }",
         ".success-card__badge { width: 58px; height: 58px; border-radius: 50%; background: var(--trust-tint); color: var(--trust); border: 2px solid var(--trust); display: grid; place-items: center; margin-inline: auto; }"),
        (".success-card__amount { font-size: 2.375rem; font-weight: 700; color: var(--pos); margin-top: 6px; font-variant-numeric: tabular-nums; }",
         ".success-card__amount { font-size: 2.375rem; font-weight: 700; color: var(--ink); margin-top: 6px; font-variant-numeric: tabular-nums; }"),
        (".success-impact { margin-top: 1rem; background: var(--pos-tint); border-radius: var(--r-control); padding: 13px 16px; display: flex; align-items: center; justify-content: space-between; gap: 10px; }",
         ".success-impact { margin-top: 1rem; background: var(--trust-tint); border: 2px solid var(--trust); border-radius: var(--r-control); padding: 13px 16px; display: flex; align-items: center; justify-content: space-between; gap: 10px; }"),
        (".success-impact__label { font-size: 0.84375rem; font-weight: 600; color: var(--pos-on); }",
         ".success-impact__label { font-size: 0.84375rem; font-weight: 600; color: var(--ink); }"),
        (".success-impact__value { font-size: 1.5rem; font-weight: 700; color: var(--pos); font-variant-numeric: tabular-nums; }",
         ".success-impact__value { font-size: 1.5rem; font-weight: 700; color: var(--ink); font-variant-numeric: tabular-nums; }"),
        (".success-impact--flash { animation: impact-flash 1.6s ease-out 1; }\n@keyframes impact-flash { 0% { box-shadow: 0 0 0 0 color-mix(in srgb, var(--pos) 55%, transparent); } 60% { box-shadow: 0 0 0 10px color-mix(in srgb, var(--pos) 0%, transparent); } 100% { box-shadow: 0 0 0 0 transparent; } }",
         ".success-impact--flash { animation: impact-flash 1.6s ease-out 1; }\n@keyframes impact-flash { 0% { box-shadow: 0 0 0 0 color-mix(in srgb, var(--trust) 55%, transparent); } 60% { box-shadow: 0 0 0 10px color-mix(in srgb, var(--trust) 0%, transparent); } 100% { box-shadow: 0 0 0 0 transparent; } }"),
        (".reduce-motion .success-impact--flash { box-shadow: 0 0 0 3px var(--pos); }", ".reduce-motion .success-impact--flash { box-shadow: 0 0 0 3px var(--trust); }"),
        # D-106 order remaining -> trust
        (".amount-row--remaining .amount-row__value { color: var(--neg); }", ".amount-row--remaining .amount-row__value { color: var(--trust); }"),
        # D-118 sizes
        (".top-chip { display: inline-flex; align-items: center; gap: 6px; min-height: 34px; padding: 4px 12px;", ".top-chip { display: inline-flex; align-items: center; gap: 6px; min-height: 40px; padding: 6px 14px;"),
        (".switch { margin-inline-start: auto; width: 52px; height: 30px;", ".switch { margin-inline-start: auto; width: 56px; height: 34px;"),
        (".switch::after { content: \"\"; position: absolute; top: 3px; inset-inline-start: 3px; width: 24px; height: 24px;", ".switch::after { content: \"\"; position: absolute; top: 3px; inset-inline-start: 3px; width: 28px; height: 28px;"),
        (".switch--on::after { inset-inline-start: 25px; }", ".switch--on::after { inset-inline-start: 25px; }"),
    ]
    for old, new in rules:
        if old not in s:
            print(f"  !! c1 not found: {old[:80]}")
        else:
            s = s.replace(old, new)
    open(p, "w", encoding="utf-8").write(s)
    print("c1.css patched")

# ---------- C2 ----------
def fix_c2():
    p = os.path.join(DESIGN, "c2.css")
    s = open(p, encoding="utf-8").read()
    s = PX_TO_REM.sub(to_rem, s)
    rules = [
        (".sheet--open { transform: translateY(0); }",
         ".sheet--open { transform: translateY(0); visibility: visible; transition: transform .28s cubic-bezier(.2,.8,.25,1), visibility 0s; }"),
        ("padding: 10px 18px calc(20px + env(safe-area-inset-bottom)); max-width: 430px; margin-inline: auto; transform: translateY(102%); transition: transform .28s cubic-bezier(.2,.8,.25,1); max-height: 78dvh; overflow-y: auto;",
         "padding: 10px 18px calc(20px + env(safe-area-inset-bottom)); max-width: 430px; margin-inline: auto; transform: translateY(102%); visibility: hidden; transition: transform .28s cubic-bezier(.2,.8,.25,1), visibility 0s .28s; max-height: 78dvh; overflow-y: auto;"),
        (".tab__label { font-size: 0.71875rem; font-weight: 500; }", ".tab__label { font-size: 0.75rem; font-weight: 600; }"),
        (".ostep__label { font-size: 0.71875rem; font-weight: 600; color: var(--ink2); white-space: nowrap; }",
         ".ostep__label { font-size: 0.75rem; font-weight: 600; color: var(--ink2); white-space: nowrap; }"),
        (".tag { display: inline-flex; align-items: center; gap: 4px; font-size: 0.71875rem;", ".tag { display: inline-flex; align-items: center; gap: 4px; font-size: 0.75rem;"),
        (".type-chip { font-size: 0.71875rem;", ".type-chip { font-size: 0.75rem;"),
        (".metric-row__value .cur { font-size: 0.75rem; color: var(--ink2); font-weight: 500; }", ".metric-row__value .cur { font-size: 0.8125rem; color: var(--ink2); font-weight: 500; }"),
        (".stage-chip { display: inline-flex; align-items: center; gap: 5px; border-radius: var(--r-chip); padding: 3px 11px; font-size: 0.78125rem;",
         ".stage-chip { display: inline-flex; align-items: center; gap: 5px; border-radius: var(--r-chip); padding: 3px 11px; font-size: 0.8125rem;"),
        (".late-chip { display: inline-flex; align-items: center; gap: 5px; margin-inline-start: auto; color: var(--neg); background: var(--neg-tint); border-radius: var(--r-chip); padding: 3px 10px; font-size: 0.78125rem;",
         ".late-chip { display: inline-flex; align-items: center; gap: 5px; margin-inline-start: auto; color: var(--neg); background: var(--neg-tint); border-radius: var(--r-chip); padding: 3px 10px; font-size: 0.8125rem;"),
        # D-115: C2 negative hero stays navy + red bottom bar
        (".hero__actions { margin-top: 16px; display: flex; gap: 10px; }",
         ".hero__actions { margin-top: 16px; display: flex; gap: 10px; }\n.hero--neg::before { content: \"\"; position: absolute; inset-block-end: 0; inset-inline: 0; height: 5px; background: var(--neg); }\n.hero--neg .hero__result { color: #FFFFFF; }"),
        # D-108: hero action terracotta
        (".hero .btn--ink", ".hero .btn--hero"),
        # D-107: filter chip dark contrast
        (".filter-chip--on { background: var(--trust); color: #FFFFFF; }", ".filter-chip--on { background: var(--trust-fill); color: #FFFFFF; }"),
        # D-104 success de-green
        (".success-card__badge { width: 58px; height: 58px; border-radius: var(--r-chip); background: var(--pos-tint); color: var(--pos); display: grid; place-items: center; margin-inline: auto; }",
         ".success-card__badge { width: 58px; height: 58px; border-radius: var(--r-chip); background: var(--trust-tint); color: var(--trust); border: 2px solid var(--trust); display: grid; place-items: center; margin-inline: auto; }"),
        (".success-card__amount { font-size: 2.375rem; font-weight: 700; color: var(--pos); margin-top: 6px; font-variant-numeric: tabular-nums; }",
         ".success-card__amount { font-size: 2.375rem; font-weight: 700; color: var(--ink); margin-top: 6px; font-variant-numeric: tabular-nums; }"),
        (".success-impact { margin-top: 1rem; background: var(--pos-tint); border-radius: var(--r-control); padding: 13px 16px; display: flex; align-items: center; justify-content: space-between; gap: 10px; }",
         ".success-impact { margin-top: 1rem; background: var(--trust-tint); border: 2px solid var(--trust); border-radius: var(--r-control); padding: 13px 16px; display: flex; align-items: center; justify-content: space-between; gap: 10px; }"),
        (".success-impact__label { font-size: 0.84375rem; font-weight: 600; color: var(--pos-on); }",
         ".success-impact__label { font-size: 0.84375rem; font-weight: 600; color: var(--ink); }"),
        (".success-impact__value { font-size: 1.5rem; font-weight: 700; color: var(--pos); font-variant-numeric: tabular-nums; }",
         ".success-impact__value { font-size: 1.5rem; font-weight: 700; color: var(--ink); font-variant-numeric: tabular-nums; }"),
        (".success-impact--flash { animation: impact-flash 1.6s ease-out 1; }\n@keyframes impact-flash { 0% { box-shadow: 0 0 0 0 color-mix(in srgb, var(--pos) 55%, transparent); } 60% { box-shadow: 0 0 0 10px color-mix(in srgb, var(--pos) 0%, transparent); } 100% { box-shadow: 0 0 0 0 transparent; } }",
         ".success-impact--flash { animation: impact-flash 1.6s ease-out 1; }\n@keyframes impact-flash { 0% { box-shadow: 0 0 0 0 color-mix(in srgb, var(--trust) 55%, transparent); } 60% { box-shadow: 0 0 0 10px color-mix(in srgb, var(--trust) 0%, transparent); } 100% { box-shadow: 0 0 0 0 transparent; } }"),
        (".reduce-motion .success-impact--flash { box-shadow: 0 0 0 3px var(--pos); }", ".reduce-motion .success-impact--flash { box-shadow: 0 0 0 3px var(--trust); }"),
        (".amount-row--remaining .amount-row__value { color: var(--neg); }", ".amount-row--remaining .amount-row__value { color: var(--trust); }"),
        # D-108 warm share elements
        (".market-hero .icon { width: 2.5rem; height: 2.5rem; color: var(--trust); }", ".market-hero .icon { width: 2.5rem; height: 2.5rem; color: var(--brand-deep); }"),
        (".tool-group__title { font-size: 0.8125rem; font-weight: 700; color: var(--trust);", ".tool-group__title { font-size: 0.8125rem; font-weight: 700; color: var(--trust);"),
        (".top-chip { display: inline-flex; align-items: center; gap: 6px; min-height: 34px; padding: 4px 12px;", ".top-chip { display: inline-flex; align-items: center; gap: 6px; min-height: 40px; padding: 6px 14px;"),
        (".switch { margin-inline-start: auto; width: 52px; height: 30px;", ".switch { margin-inline-start: auto; width: 56px; height: 34px;"),
        (".switch::after { content: \"\"; position: absolute; top: 3px; inset-inline-start: 3px; width: 24px; height: 24px;", ".switch::after { content: \"\"; position: absolute; top: 3px; inset-inline-start: 3px; width: 28px; height: 28px;"),
        # btn--hero definition (terracotta action inside navy hero)
        (".btn--ink { background: var(--ink); color: var(--canvas); }",
         ".btn--ink { background: var(--ink); color: var(--canvas); }\n.btn--hero { background: var(--brand); color: var(--on-brand); }"),
    ]
    for old, new in rules:
        if old not in s:
            print(f"  !! c2 not found: {old[:80]}")
        else:
            s = s.replace(old, new)
    open(p, "w", encoding="utf-8").write(s)
    print("c2.css patched")

# ---------- C3 ----------
def fix_c3():
    p = os.path.join(DESIGN, "c3.css")
    s = open(p, encoding="utf-8").read()
    s = PX_TO_REM.sub(to_rem, s)
    rules = [
        (".sheet--open { transform: translateY(0); }",
         ".sheet--open { transform: translateY(0); visibility: visible; transition: transform .28s cubic-bezier(.2,.8,.25,1), visibility 0s; }"),
        ("padding: 10px 18px calc(20px + env(safe-area-inset-bottom)); max-width: 430px; margin-inline: auto; transform: translateY(102%); transition: transform .28s cubic-bezier(.2,.8,.25,1); max-height: 78dvh; overflow-y: auto;",
         "padding: 10px 18px calc(20px + env(safe-area-inset-bottom)); max-width: 430px; margin-inline: auto; transform: translateY(102%); visibility: hidden; transition: transform .28s cubic-bezier(.2,.8,.25,1), visibility 0s .28s; max-height: 78dvh; overflow-y: auto;"),
        (".tab__label { font-size: 0.71875rem; font-weight: 600; }", ".tab__label { font-size: 0.75rem; font-weight: 700; }"),
        (".ostep__label { font-size: 0.71875rem; font-weight: 700; color: var(--ink2); white-space: nowrap; }",
         ".ostep__label { font-size: 0.75rem; font-weight: 700; color: var(--ink2); white-space: nowrap; }"),
        (".tag { display: inline-flex; align-items: center; gap: 4px; font-size: 0.71875rem;", ".tag { display: inline-flex; align-items: center; gap: 4px; font-size: 0.75rem;"),
        (".type-chip { font-size: 0.71875rem;", ".type-chip { font-size: 0.75rem;"),
        (".metric-row__value .cur { font-size: 0.75rem; color: var(--ink2); font-weight: 500; }", ".metric-row__value .cur { font-size: 0.8125rem; color: var(--ink2); font-weight: 500; }"),
        (".stage-chip { display: inline-flex; align-items: center; gap: 5px; border-radius: var(--r-chip); padding: 3px 11px; font-size: 0.78125rem;",
         ".stage-chip { display: inline-flex; align-items: center; gap: 5px; border-radius: var(--r-chip); padding: 3px 11px; font-size: 0.8125rem;"),
        (".late-chip { display: inline-flex; align-items: center; gap: 5px; margin-inline-start: auto; color: var(--neg); background: var(--neg-tint); border: 2px solid var(--neg); border-radius: var(--r-chip); padding: 3px 10px; font-size: 0.78125rem;",
         ".late-chip { display: inline-flex; align-items: center; gap: 5px; margin-inline-start: auto; color: var(--neg); background: var(--neg-tint); border: 2px solid var(--neg); border-radius: var(--r-chip); padding: 3px 10px; font-size: 0.8125rem;"),
        # D-115: negative hero light + red
        (".hero__actions { margin-top: 16px; display: flex; gap: 10px; position: relative; }",
         ".hero__actions { margin-top: 16px; display: flex; gap: 10px; position: relative; }\n.hero--neg { background: var(--surface); color: var(--ink); border: 2px solid var(--neg); box-shadow: inset 0 -6px 0 var(--neg-tint); }\n.hero--neg::after { display: none; }\n.hero--neg .hero__result { color: var(--neg); }\n.hero--neg .hero__reason { color: var(--ink); }\n.hero--neg .hero__label { color: var(--ink2); }\n.hero--neg .hero__mini .m-value { color: var(--ink); }\n.hero--neg .hero__mini .m-label { color: var(--ink2); }"),
        # D-111: topzone + dark hero focus
        (".hero :focus-visible { outline-color: var(--ink); }",
         ".hero :focus-visible { outline-color: var(--ink); }\n.topzone :focus-visible { outline-color: var(--module-text); }\n[data-theme=\"dark\"] .hero :focus-visible { outline-color: var(--on-brand); }"),
        # D-104 success de-green
        (".success-card__badge { width: 58px; height: 58px; border-radius: var(--r-chip); background: var(--pos-tint); color: var(--pos); border: 2px solid var(--pos); display: grid; place-items: center; margin-inline: auto; }",
         ".success-card__badge { width: 58px; height: 58px; border-radius: var(--r-chip); background: var(--trust-tint); color: var(--trust); border: 2px solid var(--trust); display: grid; place-items: center; margin-inline: auto; }"),
        (".success-card__amount { font-size: 2.375rem; font-weight: 700; color: var(--pos); margin-top: 6px; font-variant-numeric: tabular-nums; }",
         ".success-card__amount { font-size: 2.375rem; font-weight: 700; color: var(--ink); margin-top: 6px; font-variant-numeric: tabular-nums; }"),
        (".success-impact { margin-top: 1rem; background: var(--pos-tint); border: 2px solid var(--pos); border-radius: var(--r-control); padding: 13px 16px; display: flex; align-items: center; justify-content: space-between; gap: 10px; }",
         ".success-impact { margin-top: 1rem; background: var(--trust-tint); border: 2px solid var(--trust); border-radius: var(--r-control); padding: 13px 16px; display: flex; align-items: center; justify-content: space-between; gap: 10px; }"),
        (".success-impact__label { font-size: 0.84375rem; font-weight: 700; color: var(--pos-on); }",
         ".success-impact__label { font-size: 0.84375rem; font-weight: 700; color: var(--ink); }"),
        (".success-impact__value { font-size: 1.5rem; font-weight: 700; color: var(--pos); font-variant-numeric: tabular-nums; }",
         ".success-impact__value { font-size: 1.5rem; font-weight: 700; color: var(--ink); font-variant-numeric: tabular-nums; }"),
        (".success-impact--flash { animation: impact-flash 1.6s ease-out 1; }\n@keyframes impact-flash { 0% { box-shadow: 0 0 0 0 color-mix(in srgb, var(--pos) 55%, transparent); } 60% { box-shadow: 0 0 0 10px color-mix(in srgb, var(--pos) 0%, transparent); } 100% { box-shadow: 0 0 0 0 transparent; } }",
         ".success-impact--flash { animation: impact-flash 1.6s ease-out 1; }\n@keyframes impact-flash { 0% { box-shadow: 0 0 0 0 color-mix(in srgb, var(--trust) 55%, transparent); } 60% { box-shadow: 0 0 0 10px color-mix(in srgb, var(--trust) 0%, transparent); } 100% { box-shadow: 0 0 0 0 transparent; } }"),
        (".reduce-motion .success-impact--flash { box-shadow: 0 0 0 3px var(--pos); }", ".reduce-motion .success-impact--flash { box-shadow: 0 0 0 3px var(--trust); }"),
        (".amount-row--remaining .amount-row__value { color: var(--neg); }", ".amount-row--remaining .amount-row__value { color: var(--trust); }"),
        # D-116: finance + tools section plates -> tint (energy reduction)
        (".section__title { font-size: 0.8125rem; font-weight: 700; color: var(--module-text); background: var(--module); display: inline-flex; align-items: center; gap: 7px; border-radius: var(--r-chip); padding: 6px 14px; align-self: flex-start; }",
         ".section__title { font-size: 0.8125rem; font-weight: 700; color: var(--module-text); background: var(--module); display: inline-flex; align-items: center; gap: 7px; border-radius: var(--r-chip); padding: 6px 14px; align-self: flex-start; }\nhtml[data-module=finance] .section__title, html[data-module=tools] .section__title { background: var(--module-tint); color: var(--module); border: 2px solid var(--module); }"),
        (".fin-hero { background: var(--surface); border: 2px solid var(--finance); border-radius: var(--r-card); padding: 18px; }",
         ".fin-hero { background: var(--surface); border: 2px solid var(--ink); border-radius: var(--r-card); padding: 18px; }"),
        (".tool-group__title { font-size: 0.8125rem; font-weight: 700; color: var(--module-text); background: var(--tools); display: inline-flex; padding: 5px 14px 5px 10px; border-end-start-radius: var(--r-chip); }",
         ".tool-group__title { font-size: 0.8125rem; font-weight: 700; color: var(--tools); background: var(--tools-tint); border: 2px solid var(--tools); display: inline-flex; padding: 4px 14px 4px 10px; border-end-start-radius: var(--r-chip); }"),
        (".top-chip { display: inline-flex; align-items: center; gap: 6px; min-height: 34px; padding: 4px 12px;", ".top-chip { display: inline-flex; align-items: center; gap: 6px; min-height: 40px; padding: 6px 14px;"),
        (".switch { margin-inline-start: auto; width: 52px; height: 30px;", ".switch { margin-inline-start: auto; width: 56px; height: 34px;"),
        (".switch::after { content: \"\"; position: absolute; top: 2px; inset-inline-start: 2px; width: 22px; height: 22px;", ".switch::after { content: \"\"; position: absolute; top: 3px; inset-inline-start: 3px; width: 28px; height: 28px;"),
        (".switch--on::after { inset-inline-start: 24px; }", ".switch--on::after { inset-inline-start: 25px; }"),
    ]
    for old, new in rules:
        if old not in s:
            print(f"  !! c3 not found: {old[:80]}")
        else:
            s = s.replace(old, new)
    open(p, "w", encoding="utf-8").write(s)
    print("c3.css patched")

fix_c1(); fix_c2(); fix_c3()
