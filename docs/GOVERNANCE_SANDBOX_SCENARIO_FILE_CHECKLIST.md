# GOVERNANCE_SANDBOX_SCENARIO_FILE_CHECKLIST

Use this when governance-sandbox work is still prioritizing scenario-file input plus markdown/html/json report output before the web demo expands.

## Checklist
- Keep one JSON fixture and one YAML fixture for the same proposal shape.
- Verify the run works with `--scenario-file` and without extra inline flags.
- Generate `report.json`, `report.md`, and `report.html` from one deterministic command.
- Keep report metadata visible: scenario source, generated timestamp, artifact paths, and report basename.
- Prefer small scenario aliases that reduce manual CLI typing without weakening reproducibility.
- Delay broader UI polish until the scenario-file/report bundle loop is stable.

## Done signal
A maintainer can rerun one command, inspect the three report artifacts, and confirm the scenario file is the single source of truth.
