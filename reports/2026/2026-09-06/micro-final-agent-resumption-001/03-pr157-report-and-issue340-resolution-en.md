# 03 — PR #157 and Issue #340 Resolution

## 1. Reproducing the root cause

### 1.1 What failed

PR #157's CI run [`33994629352`](https://github.com/Qays7753/Micro/actions/runs/33994629352) failed in the `checks` job, "Verify domain and prototype" step, on two date-dependent DOM tests:

- **G2** (`G2.dom.test.tsx`, Statement surface): `screen.getByText("قبض البيع المباشر")` — not found.
- **G5** (`G5Activity.dom.test.tsx`, FinanceActivity surface): `screen.findByText("بنزين")` — not found, because the activity surface was empty for the displayed range `06/09/2026`–`12/09/2026`.

### 1.2 Why it failed (verified, not guessed)

Both suites seed records at **fixed dates** (G2 seeds 2026-09-02 events; G5 seeds a 2026-09-01 expense «بنزين») while the pages under test derive their default **«هذا الأسبوع»** (this week) range from the **real system clock** via `localDateInAmman()`. The PR #157 CI run executed after the **Amman week rollover (2026-09-06 01:00 UTC+3)** — Sunday morning local time starts a new week — so "this week" became 06/09–12/09 and the fixed seed dates (01/09–05/09) fell **outside** the default range. The surfaces correctly rendered an empty state; the tests then failed to find their assertions.

This run reproduced the conditions exactly: the resumption executed on 2026-09-06 (post-rollover) and the un-pinned tests would fail identically — the fix makes them deterministic.

### 1.3 The fix (commit `4643704`)

```ts
vi.useFakeTimers({ now: new Date(NOW), toFake: ["Date"] });  // NOW matches the seed clock
```

- Applied in `G2.dom.test.tsx` and `G5Activity.dom.test.tsx` (both suites), and **proactively** in the Finance period-view describe of `group2InventorySurfaces.test.tsx` (the same defect class — would have broken at the October week rollover).
- Only the `Date` timer is faked; everything else (events, rAF) stays real.
- **No assertions deleted** (both key assertions verified present and passing: G2 line 299 `قبض البيع المباشر`; G5 lines 90/118 `بنزين` plus the negative range assertion on line 122).
- **No fixtures changed, no empty state accepted.** The user-facing date behavior is untouched — only the tests' notion of "today" is pinned to their seed data.
- Verified green post-rollover in this session: 28/28 targeted tests.

## 2. REPORT.md resolution

PR #157's `REPORT.md` (+97 lines) was reviewed. The interrupted run had already produced a corrected, expanded replacement (+197 lines, included in commit `4643704`). This resumption:

- Verified its generation context (generated from `main` @ `1601fd9`, the PR #156 merge — the correct commit), non-empty, no secrets, no machine-local paths.
- Found and fixed two factual inaccuracies: it recommended `pnpm test:domain` / `pnpm test:prototype`, which do not exist — corrected to `pnpm test` / `pnpm prototype:test` (commit `bfc41f9`).
- Verified baseline claims (23/278 domain, 125/818 prototype at the baseline commit; pnpm 9.15.9; React 19.2.1; schema 35 / export 27; 37-warning lint ceiling) against the repository.

**Decision:** the corrected report is included in PR #158 (merged). PR #157 is **closed unmerged** — its valid content is superseded by the verified version; merging it unchanged would have shipped a report whose CI context is a failure.

## 3. Issue #340 — recorded discrepancy

- `GET https://api.github.com/repos/Qays7753/Micro/issues/340` → **404**.
- The issue list confirms the repository contains **no issues at all** (only pull requests #141–#158).
- The assignment's reference to "`docs: generate repository analysis report #340`" therefore does not correspond to any real issue. **No issue number was invented**: the actual references are PR #157, its CI run `33994629352`, and the superseding PR #158. This is stated explicitly in the PR #157 closing comment and in this report.

## 4. PR #157 final disposition

- **State:** closed (not merged), with a public diagnostic comment: https://github.com/Qays7753/Micro/pull/157#issuecomment-5558581291
- The comment records the diagnosis, the fix location, the report supersession, and the issue #340 discrepancy.
- The stale unrelated PR #141 was left untouched (out of scope).
