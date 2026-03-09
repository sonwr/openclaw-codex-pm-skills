# Playwright failure recovery handoff

Use this note when a `web-qa-playwright` run fails and you need a fast, reproducible repair order.

## Recovery order

1. Restore stable target refs (`ref=<id>`) first.
2. Reattach checkpoint evidence paths (screenshots, logs, traces) second.
3. Reconcile checkpoint timestamps / execution-log ordering third.
4. Update human-facing recovery fields last (`Classification`, `Recovery owner`, `Recovery plan`, `Next action`).

## Why this order works

- Broken refs make later screenshots ambiguous.
- Missing evidence hides whether the failure actually reproduced.
- Timestamp drift makes step-by-step verification unreliable.
- Recovery prose should describe a stable rerun path, not a moving target.

## Copy/paste repair loop

```bash
python3 scripts/validate_web_qa_report.py \
  --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md \
  --playwright-interactive-profile
```

If you are triaging a failing report instead of the PASS fixture, keep the same profile and fix exactly one broken layer before rerunning.

## Handoff checklist

- Did every failed checkpoint keep a stable target ref?
- Did every failed/asserted step keep an evidence artifact path?
- Are timestamps monotonic and execution-log counts still aligned?
- Does `Next action:` point to explicit failed check ids?
- Are `Recovery owner:` and `Recovery plan:` filled only after the replay path is stable?

This follows the same priorities as Playwright-interactive work: stability first, reproducibility second, step-by-step verification third, failure recovery last.
