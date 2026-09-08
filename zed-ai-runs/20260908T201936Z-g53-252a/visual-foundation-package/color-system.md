# Color System

The color system is the source's strongest asset: six full 50–900 ramps, nine warm neutrals, and a documented separation discipline. Every value below is inherited verbatim from `tailwind.config.source.js:22–158` (cross-checked against `source-tokens.json` and `SOP_VISUAL_ONLY.md §4`). What this document changes is not the values but the **pairing contracts** — five measured WCAG corrections that keep the source palette while fixing which steps may carry text. All ratios are WCAG 2.1, computed in `agents/sub3/contrast-results.json` (62 pairs) and independently reproduced by the design-system critic.

## The five families and their roles

| Family | Ramp | Identity role |
|---|---|---|
| **Primary** (terracotta) | `#FBF3EF → #5A2C1D` | Brand identity. Filled primary actions (700), selected states, identity tints (100), brand marks. Owns the warm hue exclusively. |
| **Accent** (teal) | `#E3F5F5 → #022425` | Interaction: focus, links, secondary filled actions (600), selected checks, dropdown selection. |
| **Positive** (green) | `#E4F2EA → #0A311B` | Semantic income/positive state. Filled variant 500; text 600. |
| **Negative** (crimson) | `#FBE7E6 → #4B0E06` | Semantic expense/negative state and destructive intent. Filled 500; text 600. |
| **Operational** (steel blue) | `#E8EEF3 → #111E25` | Semantic cool operational state. Filled 600; text 600. |
| **Gold** (rare) | `#F6ECCF → #1F1809` | Rare return/highlight state. Graphics 500/300; text 600 on white, 700 on tint. |

Semantic renames (normalized, per `SOURCE_AUDIT_NOTES.md:27–29`): `income → positive`, `expense → negative`, `withdrawal → operational`, `returns → gold`. Values are untouched; the old names survive only in the alias map (`design-tokens.json → aliases`).

## Ramp-step discipline

The source implies a step logic but never states it; the rendered references contradict it in places. This package states it explicitly and enforces it in the gallery:

| Steps | sanctioned use | forbidden use |
|---|---|---|
| 50 | semantic row/badge background | — |
| 100 | icon-chip backgrounds, selected surfaces | text backgrounds for 400+ text |
| 200 | graphic fills (positive fill, snackbar action) | — |
| 300 | graphic fills (gold fill) | — |
| 400 | mid graphic fills (negative fill) | text-bearing fills |
| 500 | identity color, positive/negative filled buttons (5.02/5.29 with white) | **never body text on white (gold 3.36:1); never white text on primary/accent/operational 500** |
| 600 | text-bearing fills for accent/operational; text/icon on white for all semantics | — |
| 700 | text-bearing fills for primary; strong text on tints (gold 700) | — |
| 800 | pressed states of 700 fills | — |
| 900 | deepest emphasis (rarely needed) | — |

## Neutrals

| Token | Value | Role |
|---|---|---|
| `color.canvas` | `#FAF9F5` | app background |
| `color.recessed` | `#F0EEE6` | ivory recess, KPI tint, skeleton base |
| `color.surface` | `#FFFFFF` | cards, sheets, inputs, nav |
| `color.border-soft` | `#EAE6DC` | field borders, quiet separators |
| `color.divider` | `#DAD5C8` | strong row separators, sheet handle |
| `color.ink` | `#1F1E1D` | headings, key numbers, snackbar bg |
| `color.ink-strong` | `#33322E` | body text |
| `color.ink-secondary` | `#6E6A60` | secondary text, inactive nav |
| `color.disabled` | `#B7B2A6` | disabled surfaces, placeholders |

All neutrals are warm greige; blue-grey neutrals (`#F4F7F9`, `#E4EAEE`, `#647680`) are explicitly forbidden by `accounting-color-identity.html:95–97`. The source's `text`/`txt`/`ink` parallel trees collapse into this single set (see alias map).

## On-colors and measured pairings

Every text-bearing pairing below was computed. **Bold** rows are the five corrections; everything else is inherited.

| Pairing | Ratio | AA (4.5) | Verdict |
|---|---:|---|---|
| ink / canvas · surface · recessed | 15.80 · 16.64 · 14.33 | ✅ | AAA — headings/body anywhere |
| ink-strong / canvas · surface · recessed | 12.18 · 12.83 · 11.05 | ✅ | AAA body |
| ink-secondary / surface · canvas · recessed | 5.39 · 5.12 · 4.64 | ✅ | captions and labels pass on all three |
| **white on primary.700 `#964E33`** | **6.11** | ✅ | **corrected primary-button fill** |
| white on primary.500 `#CC785C` | 3.28 | ❌ | identity color restricted to non-text graphics, large text |
| white on primary.600 `#B4613F` | 4.45 | ❌ | pressed step for graphics only |
| **white on accent.600 `#057B7C`** | **5.08** | ✅ | **corrected secondary-button fill** |
| white on accent.500 `#079FA0` | 3.24 | ❌ | accent 500 restricted to icons/focus borders |
| white on positive.500 `#2E7D57` | 5.02 | ✅ | inherited positive filled button |
| white on negative.500 `#C9322A` | 5.29 | ✅ | inherited destructive filled button |
| **white on operational.600 `#3E5C76`** | **7.01** | ✅ | **corrected operational fill (500 was 4.39)** |
| **gold.600 `#8A6927` text on white** | **5.08** | ✅ | **corrected gold text on white (500 was 3.36)** |
| **gold.700 `#644D1C` on gold.50 tint** | **6.80** | ✅ | **corrected gold badge text (500 was 2.85 — failed even 3:1)** |
| positive.600 on positive.50 | 5.62 | ✅ | badge/row text (source 500 was 4.34) |
| negative.600 on negative.50 | 5.53 | ✅ | badge/row text |
| operational.600 on operational.50 | 5.99 | ✅ | badge/row text |
| accent.600 on accent.50 | 4.51 | ✅ | selected dropdown/ready badge text |
| ink-secondary on recessed | 4.64 | ✅ | closed-badge text |
| **primary.700 nav label on surface** | **6.11** | ✅ | **corrected active-nav color (500 was 3.28 at 12px)** |
| ink-secondary inactive nav | 5.39 | ✅ | **corrected inactive (disabled `#B7B2A6` was 2.11)** |
| white on ink (snackbar) | 16.64 | ✅ | AAA |
| primary.200 on ink (snackbar action) | 10.68 | ✅ | AAA |
| disabled on surface | 2.11 | — | WCAG 1.4.3 exempts inactive controls |
| accent.500 focus border on surface | 3.24 | ≥3.0 ✅ | passes 1.4.11 non-text contrast |

## Status roles

The three source status colors are ramp references, not new colors: `status.progress = gold.400 #C99100`, `status.ready = accent.500 #079FA0`, `status.closed = ink-secondary #6E6A60`. Status badges pair them with their family's 50-step tint and 600/700-step text (progress uses gold.700 text — the corrected pairing).

## Scrim and overlays

`color.scrim = rgba(31,30,29,0.4)` — ink at 40% over any surface; tokenized from four identical inline usages in the source. Sheets, dialogs, and menus share it. The scrolled header uses `rgba(250,249,245,0.88)` + `blur(12px)`.

## Prohibited misuse

1. Never place `primary.500`/`accent.500`/`operational.500` under white body-size text.
2. Never use `gold.500` as text anywhere; gold text is 600 (white bg) or 700 (tint bg). Gold is rare — at most one gold element per composition.
3. Never use semantic colors as decoration, or more than two semantic families in one composition (multi-series data visualization excepted).
4. Never mix cold blue-grey neutrals, navy `#023852`, orange `#FE8801`, or generic blues `#1F6FE8` into any surface — the source documents these as forbidden.
5. Never use terracotta for amounts or data meaning; it is identity chrome only.
6. Never add a new color without a unique role, an on-color, a tint, interaction states, contrast evidence, and a gallery demonstration.
7. Never pair a border and a shadow on the same element (except the documented nav top border, which carries no shadow).
8. Never rely on color as the only state signal — pair with sign, icon, or label.

## Legacy values retired

`#DC2E2F` (off-palette destructive red), `#E0A200` (off-palette gold fill), the `0 −4px 24px` sheet shadow, and the untokenized presentation values `#ECE9E4` / `rgba(33,36,39,.08)` are deprecated with evidence in `decision-log.md`. They must not re-enter the system.
