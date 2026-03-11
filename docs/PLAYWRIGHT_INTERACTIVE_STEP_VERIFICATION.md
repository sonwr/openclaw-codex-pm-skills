# Playwright interactive step verification

Use this note when a browser-driven workflow must stay reproducible across retries.

## Core loop

1. Lock one replay preset (`--playwright-interactive-profile` or equivalent).
2. Keep the same target refs and artifact names between attempts.
3. Verify each step before moving on: page loaded, target visible, action applied, evidence captured.
4. If a step fails, record the blocker and restart from the last verified checkpoint instead of improvising a new flow.

## Evidence checklist

- command used
- profile/preset used
- target page or fixture
- verified step reached
- failure point if any
- next recovery action

## When to stop

Stop the loop when the same blocker repeats with the same preset and evidence. Handoff should include the failing checkpoint and the smallest reproducible rerun command.
