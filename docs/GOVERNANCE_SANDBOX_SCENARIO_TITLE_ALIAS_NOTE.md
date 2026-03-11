# Governance Sandbox Scenario Title Alias Note

Use this note when a governance-sandbox scenario fixture needs a short, replay-friendly naming pass before report output review.

## Keep one naming lane visible

Prefer a scenario fixture that keeps:

- one scenario display name (`name`, `title`, or `scenario_name`),
- one scenario context (`context` or `decision_context`),
- and one report-facing title (`report.title`, `report_heading`, or `report_title`).

That keeps scenario-file input reviewable before reopening the generated JSON/Markdown/HTML bundle.

## Why this matters

When scenario authors use different naming aliases, PM and reviewer handoff should still preserve one obvious path:

1. identify the scenario by name,
2. identify the decision context,
3. verify the report title that downstream reviewers will actually read.

## Minimum replay check

- Open the scenario fixture.
- Confirm the scenario name alias resolves to one stable label.
- Confirm the report title alias resolves to one reviewer-facing heading.
- Re-run the same scenario through the report bundle flow.

If those three checks still read clearly together, the naming layer is good enough for a small pre-merge pass.
