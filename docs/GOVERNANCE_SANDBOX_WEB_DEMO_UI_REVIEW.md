# Governance sandbox web demo UI review

Use this note when the governance-sandbox workstream is expanding the first web demo beyond raw form wiring and you need a compact review loop that stays aligned with UI/UX Pro Max and Playwright-interactive principles.

## Review loop

1. Keep the first slice narrow: one scenario input form, one result card, one clearly visible report-download action.
2. Prefer obvious hierarchy: intro/context at the top, one primary action per card, calm spacing, and readable labels.
3. Preserve reproducibility: use stable scenario fixtures plus report artifact names that can be rechecked after each UI pass.
4. Verify step-by-step in the browser: input, submit, result card render, report artifact visibility, and recovery path after failure.
5. If the UI fails validation, repair the smallest broken slice first and rerun the same proof path before widening scope.

## Keep visible in proof

- scenario source used for the run
- generated report basename or artifact bundle path
- primary recommendation/result card state
- markdown/html download or handoff visibility
- next repair owner when the browser proof fails
