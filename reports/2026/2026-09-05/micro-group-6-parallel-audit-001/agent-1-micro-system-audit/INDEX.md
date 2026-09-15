# Group 6 / Agent 1 — Micro System Integrity, Quality, Performance, Security, and Release Audit (Parallel, Isolated Branch)

Program: Micro release-quality audit — parallel track A (system integrity).
Agent: Agent 1 — Principal Micro System Auditor and Release Owner.
Agent 2 (Zman→Micro transfer reconciliation) runs independently; its branch and report folders were not touched.

Baseline: Micro `main @ ad9fc13` (Groups 1–5 present, PR #153 merged, CI green run 33948024196).
Delivery: **isolated audit branch only** — `agent/group-6-micro-system-audit` @ `c1ae93e`, pushed, PR #154 opened for review, **not merged** — awaiting the controlled integration step after Agent 2's report is available.

## Contents
- `en/agent-1-micro-system-audit-report-en.md` — mission, method, baseline gate, scope, verdict, disposition, limitations
- `en/agent-1-findings-and-remediation-en.md` — full findings register (P0–P3): evidence, reproduction, contract, risk, fix, regression test, disposition
- `en/agent-1-financial-invariants-en.md` — the ten product/financial invariants verified against code with evidence, plus adversarial test results
- `en/agent-1-ux-performance-security-ci-en.md` — UX/RTL/mobile, performance, security/privacy, code-quality and CI findings and dispositions
- `en/agent-1-test-evidence-en.md` — test matrix, gate table, adversarial coverage matrix, CI evidence
- `proposed-ci-hardening.patch` — AR-01/AR-03 CI hardening (tag-triggered runs + artifact upload, bounded audit retry, concurrency, timeout, PR whitespace check) — the push token lacks `workflow` scope, so the workflow file itself is unchanged on the branch; apply this patch with a workflow-scoped token

## Key facts
- Five read-only specialist audits (financial truth, data/persistence, UX/RTL/mobile, security/performance, adversarial release) synthesized by Agent 1; no specialist modified files.
- **P0: none found.** The domain core (8-column delta table, mirrored reversals, atomic multi-store commits, frozen cost snapshots, import validation) held under every adversarial probe.
- **P1: 8 findings — all fixed on the branch** with 18 new adversarial/regression tests: FT-01 (period attribution after delivery reversal + re-delivery), FT-02 (direct-sale cancel left wallet allocations in place), FT-03 (general event editor desynced asset/loan/deposit family records; MIC-11 never recognized loan restores), DP-01 (envelope counts never compared on import), UX-01 (PIN inputs discarded Arabic-Indic digits), SP-01/DP-04 (lock bypass via exempted `/settings` export), AR-01/AR-02 (release mechanics + canonical docs stale by three merged groups).
- Gates re-run fresh on the branch: typecheck ×2 clean · lint 0 errors / 37 warnings (ceiling unchanged) · format clean (app directory now included) · text-density 52/52 routed pages · design-guards clean · domain 277/277 (23 files) · prototype **784/784 (123 files, was 766/120)** · production PWA build · secret scan clean (working tree + tracked files).
- CI on the branch: run `33960263084` — **success**.
- Recovery safety: local snapshot branch `recovery/group-6-audit-baseline-2026-09-05` (not pushed) + full offline bundle; worktree clean; no stashes; no worktrees.
- Git reconciliation: Groups 1–5 branches remain reachable from remote (history preserved); no branch or tag deleted; no force-push; no history rewrite; no merge to `main`.

## Status statement
This is an **audit branch awaiting controlled integration**, not a closed product. The final integration step must reconcile Agent 1 and Agent 2 branches, merge selected fixes to `main`, run final CI, and only then clean merged branches after proof of reachability.
