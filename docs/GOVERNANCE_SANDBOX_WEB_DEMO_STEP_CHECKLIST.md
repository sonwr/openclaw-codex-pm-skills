# Governance Sandbox web demo step checklist

Use this when the governance-sandbox web slice changes the scenario form, run action, or result-card proof.

## Goal

Keep the first web demo deterministic, reviewable, and easy to recover when a browser checkpoint fails.

## Steps

1. Start with one scenario fixture that already proves scenario-file input plus report output.
2. Fill only the minimum form fields needed to trigger a believable governance run.
3. Verify the result card shows recommendation plus at least one stakeholder response.
4. Verify report download or artifact-path proof stays visible from the same result card.
5. Capture the exact rerun path before widening the UI scope.

## Hold conditions

- The form requires hidden setup that is not visible to reviewers.
- The result card does not expose a report artifact or replay path.
- The browser proof depends on flaky timing instead of stable checkpoints.
