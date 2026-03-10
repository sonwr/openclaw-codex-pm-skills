# Web QA Playwright rerun vs repair split

Use this card after the validator passes but the handoff still feels blocked.

## Pick **rerun** when

- the failed lane already names a stable target,
- the proof artifact is still usable,
- the next action can stay lane-scoped,
- and a second run is likely to confirm or clear the issue.

## Pick **repair** when

- the target is unstable or ambiguous,
- the proof artifact is missing or weak,
- multiple blocked lanes compete for attention,
- or the next action needs implementation work before replay.

## One-line check

If the next step is mostly **run the same thing again with clearer scope**, choose rerun.
If the next step is mostly **change the page, selector, fixture, or ownership data first**, choose repair.
