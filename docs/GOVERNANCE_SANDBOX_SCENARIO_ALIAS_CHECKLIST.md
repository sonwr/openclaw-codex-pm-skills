# Governance Sandbox Scenario Alias Checklist

Use this checklist when a `governance-sandbox` change touches scenario-file alias loading and report artifacts at the same time.

## What to verify

1. Run the smallest scenario import that uses alias keys such as `title`, `summary`, `proposal_text`, `participants`, `group`, or `trait`.
2. Confirm the JSON output still exposes the normalized `scenario.name`, `scenario.context`, and stakeholder `preset` fields.
3. Write at least one markdown or HTML report artifact from the same scenario fixture.
4. Check that the report heading, metadata, and stakeholder sections still match the normalized JSON payload.
5. Only call the handoff replay-ready after the scenario import and report artifact proofs both pass.

## Minimal proof command

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run   --scenario-file examples/scenario.yaml   --report-dir artifacts/demo
```

## Suggested handoff sentence

Validator PASS and scenario alias normalization still matches the generated report bundle, so the fixture is safe for a focused report-review handoff.
