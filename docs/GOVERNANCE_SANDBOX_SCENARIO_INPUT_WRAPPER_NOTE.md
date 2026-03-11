# governance-sandbox scenario_input wrapper note

Use `scenario_input` when one JSON/YAML file needs an explicit top-level envelope around proposal, stakeholders, and report metadata before replaying `governance-sandbox` report generation.

Keep the replay proof small:

1. Put the actual scenario payload under `scenario_input`.
2. Re-run `python3 -m unittest tests/test_validate_web_qa_report.py tests/test_validate_web_qa_report_cli.py` if the PM handoff or validator guidance changes alongside the scenario note.
3. Only claim progress when the imported scenario still produces a believable report artifact path.
