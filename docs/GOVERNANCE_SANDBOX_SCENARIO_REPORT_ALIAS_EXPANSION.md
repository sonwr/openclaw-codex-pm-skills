# GOVERNANCE_SANDBOX_SCENARIO_REPORT_ALIAS_EXPANSION

Use this note when governance-sandbox scenario imports add new metadata aliases and you want the proof loop to stay short.

## What to verify

1. Load the scenario from one file or stdin.
2. Confirm proposal aliases still map into the JSON output.
3. Confirm stakeholder preset aliases still resolve into named trait groups.
4. Confirm report-summary aliases appear in markdown/html artifacts.
5. Re-run the smallest CLI test slice before widening the proof bundle.

## Minimal proof command

```bash
PYTHONPATH=src python3 -m unittest tests/test_cli.py
```

## Handoff note

When the alias works, keep the review note narrow: `scenario import aliases now flow through JSON + markdown/html reports with the same report bundle proof.`
