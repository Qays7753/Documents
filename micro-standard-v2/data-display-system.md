# Data Display System

Direct values come first. Numeric hierarchy is hero 28 / primary 24 / secondary 15 / tertiary 13 (the 30/20/15 emphasis ladder realized in tabular mono); amounts are end-aligned and bidi-isolated, and rows use a stable trailing amount slot. Relationship bars appear only when parts genuinely sum to a whole.

## Financial value zone

Every primary value composition exposes label, value, currency unit, period, and optional delta slots (see `component-contracts.md`). Honest voids are first-class presentations: unrecorded → action chip; unavailable → the word "غير متاح"; measured zero → "0" with its label. A void never masquerades as success, failure, or decoration.

## Charts — question-led, semantic, honest

Charts are simple and answer one visible question stated in the title (e.g., "أي الأيام بدون مبيعات؟"). Rules:

- Semantic colors show outcome or category; black is not the default for every series, and Terracotta never becomes a data, success, or failure color.
- A chart must have a readable label and a text alternative (a sentence or list carrying the same answer) whenever the visual comparison matters.
- A measured zero bar renders as a visible baseline mark (2px, full radius) with its label so zero is never confused with a missing day.
- No-data renders as a word + icon state ("لا بيانات" + document icon) in the chart frame — not an empty frame, not a zero-filled chart.
- Loading renders as skeleton bars promising the real layout, with the question title already visible.
- Period context ("آخر 30 يوم") is part of the chart header, bound to the data shown.
