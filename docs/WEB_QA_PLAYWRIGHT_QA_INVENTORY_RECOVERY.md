# Web QA Playwright QA inventory recovery

Use this note when a strict-plus report fails because the QA inventory drifted away from the checkpoint map or `Next action:` handoff.

## What this doc is for

This is a compact recovery guide for the three most common mapping failures:

1. missing `Checks:` mappings in `## QA inventory`
2. partial QA inventory coverage (some checks mapped, some missing)
3. `Next action:` handoff that does not reference every failed check id

## Recovery order

1. **Restore `Checks:` markers first.**
   - Every QA inventory line should expose the checkpoint ids that validate it.
   - If the run is supposed to satisfy `--require-qa-inventory-check-refs`, expect full coverage (`qa_inventory_missing_check_ref_count == 0`).
2. **Confirm checkpoint ids stay deterministic.**
   - Keep the canonical 5/3/2 split for `functional`, `visual`, and `off_happy` checks when using the documented sample fixtures.
   - Do not rename ids during a mapping-only repair.
3. **Repair failed-check handoff next.**
   - `Next action:` must reference every failed check id before the report can be treated as replay-ready.
4. **Re-run JSON validation last.**
   - Use the same strict-plus profile so the repaired mapping and handoff fields are validated together.

## Fast triage cues

- `qa_inventory_check_ref_coverage_rate < 1.0` → at least one QA inventory item still lacks checkpoint coverage.
- `next_action_failed_check_coverage_rate < 1.0` → at least one failed check is still missing from the replay handoff.
- `missing_checkpoint_target_ref_ids` or `missing_checkpoint_artifact_ref_ids` present → the report still lacks replay-ready checkpoint evidence even if inventory mappings were restored.

## Copyable verification command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## Suggested repair note

> Restored QA inventory `Checks:` mappings, kept checkpoint ids stable, and confirmed `Next action:` references every failed check id required for strict-plus replay triage.
