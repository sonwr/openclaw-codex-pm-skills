# Governance Sandbox Scenario + Report Proof Loop

Use this checklist when a governance-sandbox change touches scenario import, markdown/html report output, or the demo-proof surface.

## Why this exists

Scenario-file support and report artifacts are only useful when maintainers can prove the full loop quickly:

1. load a scenario file,
2. generate JSON / markdown / HTML artifacts,
3. confirm the output still reads like a decision-ready handoff,
4. keep the proof reproducible for the next contributor.

## Recommended proof sequence

1. Run the CLI with a checked-in JSON or YAML scenario.
2. Write all report artifacts into a clean temp directory.
3. Verify the JSON payload includes scenario metadata and preset-aware stakeholder responses.
4. Verify the markdown report keeps the proposal, recommendation, risk list, and stakeholder cards scannable.
5. Verify the HTML report still renders a simple hero + card layout that can be screenshotted for public demo updates.
6. Capture the exact command in the PR so another maintainer can replay it without guessing.

## Suggested handoff note

- Scenario file used:
- Command used:
- Artifacts written:
- Validation command:
- Public-facing README/demo surface touched:
- Follow-up gap (if any):
