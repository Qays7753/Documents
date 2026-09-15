# Prototype design decisions

## Design read

This artifact is a review-only Arabic-first RTL phone prototype for five Micro-like scenes. It is intentionally close to the final Standard, with low visual variance, low motion, high operational information density, no external assets, and maximum source fidelity.

## Positioning

The narrative role is operational review rather than marketing. The viewing distance is a 10cm phone. The visual temperature is quiet, warm, and authoritative. The capacity check assumes 320–430px widths and long Arabic labels.

## System choices

The prototype reuses the final Standard's warm canvas, ground, recessed layer, white surface, border, Warm-Ink, Clay, Clay interactive, info/status/success/error, typography, numeric isolation, 48px controls, 12px controls radius, 20px sheet radius, and restrained motion durations. It does not generate a new palette, define a new token, or introduce a new contract.

Composition uses Surface for bounded summaries, OperationalRow for repeated work, Sheets for temporary context, and neutral chart/relationship blocks only where the scene asks a question. The four official destinations remain Home, Finance, Orders, and Tools; Detail is a local review scene reachable from Home.

## Explicit role decisions

Clay appears on identity/create and chosen period controls. Warm-Ink carries primary values and commitment boundaries. Info/status/success/error markers are paired with words and are not used as product truth. Financial values are labelled illustrative or demo. Tools visibly separate analysis from financial record writing.

## Intentional omissions

No production routing, authentication, backend, database, external API, real formula, data source, financial policy, permission, sync, delivery behavior, posting, correction, or record-writing action is included.
