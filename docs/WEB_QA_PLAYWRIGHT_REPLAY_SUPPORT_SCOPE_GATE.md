# WEB_QA Playwright Replay Support Scope Gate

Use this card after strict-plus validation passes but the report is still blocked.

## Goal

Decide whether the next rerun can stay **lane-scoped** or should expand to a wider section replay.

## Keep the rerun lane-scoped when all three are true

1. **Failed checks are named** — the blocked lane already lists the exact failed check ids.
2. **Stable refs exist** — the next action names the target refs/screens/sections that must be revisited.
3. **Fresh proof is attached** — screenshots, traces, or JSON evidence already show why the lane is blocked.

## Expand beyond the lane when any one is true

- Failed checks are missing, merged, or only implied.
- Target refs changed, drifted, or were never captured in the report.
- Evidence is stale, partial, or comes from a different replay profile/run.
- The blocker crosses adjacent sections (for example functional and visual both depend on the same broken setup step).

## Copy-ready decision lines

- **Lane-scoped rerun** — Replay support is complete enough to keep the next rerun inside the blocked lane only.
- **Section-wide rerun** — Replay support is incomplete, so broaden the rerun until failed checks, stable refs, and proof artifacts line up again.

## Fast audit

- Failed check ids present?
- Next action names the exact lane/target?
- Evidence artifact is fresh for this run?

If any answer is **no**, do not call the retry lane-scoped yet.
