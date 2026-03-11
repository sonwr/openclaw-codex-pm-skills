# Governance sandbox report priority bundle note

Use this note when a PM skill needs to keep governance-sandbox work scoped to the first real delivery lane.

## Priority order

1. import one scenario file (`.json` or `.yaml`)
2. generate one Markdown/HTML/JSON report bundle
3. expand trait presets only after the import-plus-report loop is stable
4. widen the web demo only after the report bundle is reviewable

## Why

The first believable governance-sandbox milestone is not a broader UI surface. It is one replayable scenario-to-report loop that reviewers can rerun without reconstructing inputs by hand.

## Handoff

If a task mixes scenario parsing, report output, preset growth, and UI work together, split it so the scenario-file plus report-bundle lane lands first.
