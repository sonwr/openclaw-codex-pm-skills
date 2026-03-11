# Governance Sandbox preset-json form start note

Use this note when governance-sandbox work is entering the first web-demo slice and the team needs one narrow, replayable handoff.

## Keep the slice small

Start with one machine-readable preset source:

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run --list-presets-json
```

Then keep the first UI proof limited to:

1. one preset-aware scenario form,
2. one result card,
3. one downloadable report bundle.

## Why this matters

- The preset catalog removes hard-coded stakeholder copy from the first form.
- The first result card stays aligned with the same scenario/report bundle proof.
- PM handoff stays grounded in one deterministic CLI source before broader UI work.

## Minimum PM check

Before widening the web demo, confirm all three are still true:

- the form reads from preset JSON rather than duplicated label text,
- the result card points to one report bundle outcome,
- the replay path still starts from a single CLI command.
