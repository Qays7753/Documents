# Micro Standard v2 Overall Review Prototype

## Purpose

This is a **review-only, standalone prototype** that composes the owner-reviewed Micro Standard v2 foundation into five local Micro-like scenes. It is not production code, not a transfer into Micro, and not a redesign of the Standard.

The prototype uses deterministic demo data and local browser behavior only. It has no backend, authentication, remote API, database, accounting engine, synchronization, delivery implementation, or record-writing behavior.

## Source of truth

The visual source of truth is the final package in `Qays7753/Documents`, `micro-standard-v2/`, at commit `f64e8616d031e7e825a66ef96de0a1344963ce68`. Micro is used only as a product-domain reference. Accounting is used only as a visual benchmark for richness, hierarchy, surface layering, and operational density. Neither reference was modified or copied as implementation.

## Scenes

| Scene | Review focus |
|---|---|
| Home | Official navigation context, monthly/default period, period switching, attention, quick actions, role distinction. |
| Finance | Metric/Balance, Parts/Whole, question-led chart, text alternative, explicit state samples. |
| Orders | OperationalRow, long Arabic wrapping, stable RTL amount slot, status marker, detail/sheet boundary. |
| Transaction/detail | Value/context, neutral party relationship, lifecycle cycling, confirmation boundary, reversed audit-effect wording. |
| Tools | Local illustrative analysis with inputs, assumptions, deterministic result, and explicit separation from financial records. |

## Local interaction model

The four official destinations are switchable locally. The detail scene is reachable from Home. Period presets and a custom-range sheet are local. Sheets open and close locally. Lifecycle states cycle through unknown, pending, retryable, result, and reversed-as-an-audit-effect. The chart alternative text can be shown. Tools expose inputs and a local recalculation affordance; the independent review found that the current input change is not reflected in the displayed result, and this issue remains intentionally unfixed in the delivered prototype.

## Visual decisions

The prototype reuses the final Standard roles: warm canvas and surfaces, Clay identity/create, Clay interactive for chosen/current, Warm-Ink for commitment/value, current semantic colors, English tabular numerals, bidi isolation, phone-first spacing, RTL, and reduced-motion CSS. No new palette, token, contract, or source-package file was created.

## Run locally

From this folder, run:

```bash
python3 -m http.server 4183 --bind 127.0.0.1
```

Open `http://127.0.0.1:4183/index.html`. The prototype has no external runtime dependency.

## Review status

The prototype is **not production-ready**. Browser/headless evidence is labelled as such. No physical Samsung device and no physical screen-reader test were performed. The independent self-critique is in `MICRO_STANDARD_V2_PROTOTYPE_SELF_CRITIQUE.md`.
