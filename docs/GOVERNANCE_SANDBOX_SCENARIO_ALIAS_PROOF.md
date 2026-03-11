# GOVERNANCE_SANDBOX_SCENARIO_ALIAS_PROOF

Use this quick proof when governance-sandbox changes scenario-file parsing or report metadata naming.

## Focus
- Keep stakeholder preset aliases deterministic: `preset`, `group`, `trait`, `persona`.
- Keep report summary aliases deterministic: `summary`, `brief`, `report_summary`.
- Validate with one scenario file that produces JSON plus markdown/html reports from the same input.

## Replay check
```bash
python3 -m unittest tests/test_cli.py
```

If the parser accepts the scenario aliases and the report bundle stays green, the handoff is safe to expand.
