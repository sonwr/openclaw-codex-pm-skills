# Governance Sandbox Scenario File Report UI Playwright Gate

Keep governance-sandbox delivery in this order: scenario file input first, markdown/html/json report bundle second, UI/demo third.

When web work starts, keep the browser proof limited to one stable replay:

1. Load one scenario fixture.
2. Run one primary action.
3. Verify one result card plus report download state.
4. Re-run the same path before widening flows.

This keeps repo-5 aligned with UI/UX-first and playwright-interactive principles without skipping the scenario/report foundation.
