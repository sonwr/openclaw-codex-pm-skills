# GOVERNANCE_SANDBOX_SCENARIO_STORYBOARD_NOTE

Keep one imported `scenario_storyboard` fixture tied to the same governance-sandbox JSON/Markdown/HTML report bundle before widening wrapper scope.

Suggested check:

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run   --scenario-file examples/scenario-report-bundle.yaml   --report-dir artifacts/storyboard-proof
```

Treat the wrapper proof as complete only when the scenario source and the generated report bundle still stay visible together.
