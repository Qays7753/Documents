# Content Guidelines

This package is **product-neutral**. All labels below are examples of tone and structure, replaceable by the receiver's domain — the visual system never depends on any of them (per `VISUAL_ONLY_BOUNDARY.md`: no product wording, route names, calculations, or workflows carried from the source).

## Neutral label set

Use generic, role-describing labels wherever the source used product copy: `Primary action`, `Secondary action`, `Save`, `Confirm`, `Cancel`, `Try again`, `Add record`, `Selected`, `Filter`, `Search`, `Positive state`, `Negative state`, `Warning`, `Information`, `Confirmed`, `Disabled`, `Empty state`, `No results`, `Record`, `Item`, `Total`. Never infer a business domain from the source's accounting vocabulary; never ship source product terms (invoice, ledger, register, drawer, jar names) in neutral output.

## Voice and tone

Calm, direct, verb-first. Buttons are verbs ("Save", "Retry"); titles are nouns ("Records"); empty states guide ("Records you add will appear here"); errors explain the fix, not the fault ("This number looks invalid — enter digits only"). Sentence case everywhere, including labels and nav items. No exclamation marks, no emoji, no marketing adjectives. Arabic copy (when the receiver localizes): verb-first buttons, correct singular/dual/plural counters, natural register — the source's plural-correctness rule (raw SOP §5) carries over.

## Numbers

Digits only — **never currency symbols or codes** (raw SOP §0.2/§11: `12,400` correct, `12,400 JOD` wrong) · thousands separator `,` · signs `+` and `−` (U+2212, never ASCII hyphen) prefixed in the state color · dates `DD/MM/YYYY` · times `HH:MM` 24-hour · all in mono tabular, end-aligned, bidi-isolated in RTL. Numbers in prose use the same digits; never spell amounts in mixed scripts inside a numeric field.

## Mixing scripts and directions

Arabic UI text with embedded Latin numerals/dates is the default composition: wrap numeric runs in `.bidi-isolate` spans, keep fields `dir="ltr"` where numerals are edited, and never let a trailing sign detach from its digits. English/Latin labels may use light positive tracking (≤ 0.05em) at 12–13px only; Arabic never receives letter spacing of any kind.

## Truncation and overflow

Titles truncate with ellipsis at one line; two-line clamps where the hierarchy allows; never mid-word breaks (line-clamp over hard cuts, raw SOP §8.4). Long values in rows shrink the mono size before truncating the sign. Buttons never truncate — shorten the label instead.

## Semantic state copy

State words are short and unambiguous: `Paid`, `Pending`, `Closed`, `Active`, `Overdue`, `Cancelled` — each maps to exactly one badge pairing. A state that needs a paragraph is a message, not a badge. Pair every state word with its icon/dot; the receiver supplies real state machines, this package supplies the visual contract.

## Iconography and content pairing

Icons accompany text where meaning benefits (rows, badges, errors), never as decoration alone. Icon-only controls require `aria-label`s. One glyph per concept across the whole product — no two icons for "delete".

## Gallery neutrality rule

The gallery's compositions use the neutral set exclusively: generic titles ("Recent records"), neutral amounts (`+1,200`, `−450`), and no domain nouns. The evidence panel is the only place hex values, token names, and contrast ratios appear — never inside the phone-like frames.
