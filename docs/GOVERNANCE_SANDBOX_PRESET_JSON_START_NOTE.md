# GOVERNANCE_SANDBOX_PRESET_JSON_START_NOTE

Use `run --list-presets-json` when a governance-sandbox scenario form, review bot, or demo setup needs the preset catalog without scraping prose from the README.

Quick replay:

```bash
PYTHONPATH=src python3 -m governance_sandbox.cli run --list-presets-json
```

Minimum expectation:
- one machine-readable object keyed by preset name
- a human-readable label per preset
- a short summary that explains the stakeholder trait in UI copy
- the underlying stance, concern, and mitigation fields

Keep this export in the proof loop whenever scenario import UX or preset choosers change.
