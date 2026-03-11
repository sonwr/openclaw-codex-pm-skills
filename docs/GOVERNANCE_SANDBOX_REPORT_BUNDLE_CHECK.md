# governance-sandbox report bundle check

Use this quick check before calling a governance-sandbox scenario handoff ready.

## What to confirm

1. The scenario input can be replayed from a committed JSON or YAML file.
2. The generated bundle includes JSON, Markdown, and HTML outputs for the same run.
3. The report title and scenario tags match the scenario metadata.
4. The recommendation, major risks, and stakeholder cards all describe the same proposal.
5. The saved bundle path is stable enough to link from a PR, issue, or demo note.

## Suggested command

```bash
python3 -m governance_sandbox.cli run \
  --scenario-file examples/scenarios/treasury_rehearsal.yaml \
  --report-dir artifacts/governance-demo
```

## Ready-to-handoff cue

Call the bundle ready only when one scenario file produces one reusable JSON/Markdown/HTML proof set without manual file renaming.
