# ZAI Flash Next-Step Source Brief

## Goal

Perform one read-only comparative audit to explain why Accounting and the current Micro experience feel more visually alive and richer than Micro Standard v2, with special attention to black/Warm-Ink overuse and missing semantic color treatment for financial and operational states.

## Source authority

1. Current Micro Standard v2 at the verified final commit `f64e8616d031e7e825a66ef96de0a1344963ce68` on branch `micro-standard-v2-foundation-development` in `Qays7753/Documents`. Treat this as the visual foundation being evaluated; do not modify it.
2. Micro as the product/domain reference. Read it to understand real operational and financial situations, not to copy its implementation or assume all current behavior is correct.
3. Accounting as visual benchmark only. Read it to identify hierarchy, layering, density, relationships, and semantic color use; do not copy its code, brand, screens, or business logic.
4. Prototype v0 and its owner review as latest evidence of how Standard v2 currently composes into Micro-like scenes. Treat its documented issues as evidence to verify, not as instructions to repair.

## Required review questions

- Why do Accounting and Micro feel more beautiful, rich, and alive than Standard v2?
- Which parts of that difference are caused by composition, information relationships, density, layering, and product context rather than tokens?
- Where is Warm-Ink/black correctly used for commitment, primary value, or dangerous action, and where is it overused as a default visual treatment?
- Which financial and operational states need semantic color, tint, marker, edge, or chart role so that profit, loss, attention, pending, unknown, retryable, success, failure, and review are distinguishable without color-only dependence?
- Which missing color cases belong in Standard contracts/roles, which belong in Micro composition, and which require product policy?
- What must be preserved exactly, what is missing, and what should not be added?

## Scope boundary

Read-only analysis only. No code, no prototype repair, no token edits, no Standard edits, no Micro edits, no Accounting edits, no GitHub push/merge, no new palette, no dark mode, no generic dashboard/card gallery, and no product policy invention.

## Required output

Return one evidence-based report with: root-cause diagnosis; confirmed/inferred/owner-decision classifications; black/Warm-Ink audit; semantic color/state matrix; comparison of Standard vs Micro vs Accounting; file-level recommendations for Standard only; composition recommendations for Micro only; product decisions; preserve/fix/defer/out-of-scope classification; risks; acceptance criteria; and a minimum safe next wave. Stop after the report.
