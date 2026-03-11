# GOVERNANCE_SANDBOX_SCENARIO_REPORT_QUICKSTART

Use this quickstart when the workstream is about governance-sandbox scenario inputs plus markdown/html/json report proof.

## Fast path

1. Prepare one reusable scenario fixture (`.json` or `.yaml`) with:
   - scenario name/title
   - decision context/summary
   - proposal text
   - stakeholder presets (`dao`, `delegates`, `contributors`, `investors`, `community`)
2. Generate one report bundle from the same fixture:

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run \
  --scenario-file examples/scenario-report-bundle.yaml \
  --report-dir artifacts/demo
```

3. Confirm the bundle produced all three artifacts:
   - `artifacts/demo/*.json`
   - `artifacts/demo/*.md`
   - `artifacts/demo/*.html`
4. Keep the proof loop honest: same scenario fixture, same output directory, same artifact triad.

## Pass signal

Call the slice ready only when one scenario file can be replayed into a stable JSON + Markdown + HTML bundle without manual edits.

## Hold signal

Hold the handoff if any of these are missing:
- scenario metadata in the output,
- preset-backed stakeholder import,
- markdown/html artifact generation,
- stable artifact naming for replay.
