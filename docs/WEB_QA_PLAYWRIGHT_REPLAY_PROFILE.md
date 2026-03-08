# Web QA Playwright replay profile

This note explains how the repository's `web-qa-playwright` validator profile maps to practical browser-testing discipline.

## Why this exists

Interactive browser QA tends to drift unless reports are:

- stable enough to replay,
- explicit about failure state,
- and strict about evidence capture.

The repo's strict replay profile is intentionally opinionated so CI can reject reports that are hard to audit later.

## Applied principles

These rules align with Playwright-style interactive testing guidance:

1. **Stability first** — keep deterministic checkpoints, timestamps, and explicit PASS/FAIL tokens.
2. **Reproducibility first** — require concrete artifact paths and target refs so another reviewer can follow the same trail.
3. **Stepwise verification** — keep checklist counts, execution log steps, and signoff numbers in sync.
4. **Failure recovery visibility** — when a check fails, capture classification, evidence, owner, and recovery plan.

## What the strict replay profile enforces

When contributors use the stricter replay aliases (`--playwright-interactive-profile`, `--deterministic-replay-profile`, `--strict-replay-profile`, or `--ci-replay-profile`), validation expects:

- normalized checkpoint timestamps,
- monotonic checkpoint order,
- explicit checkpoint status tokens,
- artifact references for failures and evidence capture,
- target refs for replayable UI targeting,
- signoff metadata that matches the checklist outcome.

## Recommended report-writing loop

1. Capture the test scope (`URL`, viewport, account).
2. Execute checks in numbered order without skipping the execution log.
3. Attach screenshot/log/trace references inline as soon as they are created.
4. For failed checks, record classification + recovery details before signoff.
5. Re-run the validator before publishing the report to CI or PR comments.

## Practical use

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_plus_pass.md \
  --ci-replay-profile \
  --json
```

Use the JSON payload when downstream automation needs machine-readable gating, and keep the markdown report readable enough for human triage.


JSON payloads also expose `active_profile_preset` (`strict-plus`, `playwright-interactive-profile`, `deterministic-replay-profile`, `strict-replay-profile`, or `ci-replay-profile`) so downstream CI can branch on one stable preset label instead of recomputing it from several booleans.
