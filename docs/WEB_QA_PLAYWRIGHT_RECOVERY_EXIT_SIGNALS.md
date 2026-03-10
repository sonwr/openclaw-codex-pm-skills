# Web QA Playwright recovery exit signals

Use this note when a blocked rerun is almost done and you need a fast final check before marking the report replay-ready again.

## Exit in READY mode only when all of these are true

1. The failed-check ids named in `Next action:` have a fresh rerun note.
2. The affected checkpoints now include a stable target ref, verification wording, and at least one artifact path.
3. The section hotspot count is lower than before, or explicitly explained if unchanged.
4. The recovery owner handoff no longer asks for missing evidence, missing chronology, or missing `Checks:` coverage.
5. The rerun summary can fit in one deterministic sentence: check id -> repaired signal -> proof artifact.

## Stay BLOCKED when any of these remain true

- The rerun still depends on a vague selector or manual memory.
- A checkpoint was updated without a matching artifact or timestamp.
- The signoff section says READY but the hotspot block still reports unresolved blockers.
- The failed-check ids in `Next action:` do not match the repair notes.
- The section status is cleaner, but the owner handoff still cannot say what to rerun first.

## Copyable handoff line

`Exit READY only after failed-check ids, repaired checkpoint refs, and fresh proof artifacts all agree in the rerun summary.`
