# Web QA Playwright replay lane audit

Use this note when strict-plus validation already passed, but the report still feels risky to rerun or hand off.

## Quick lane audit

1. Confirm the named hotspot lane matches the largest remaining blocker count.
2. Confirm the hotspot checkpoints listed in JSON also appear in the narrative handoff.
3. Confirm the next action sentence names the repair target, not only the symptom.
4. Confirm owner and artifact references exist for the same failed lane.
5. Confirm the rerun target is narrow enough to avoid reopening unrelated passing checks.

## Good handoff signal

A replay lane is audit-ready when a reviewer can answer all of these in under a minute:

- Which lane is blocked?
- Which checkpoints prove it?
- Who owns the repair?
- What is the next rerun scope?

If any answer is missing, treat the report as validation-pass but handoff-incomplete.
