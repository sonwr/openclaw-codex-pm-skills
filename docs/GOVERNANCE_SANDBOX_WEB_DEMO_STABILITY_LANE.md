# governance-sandbox web demo stability lane

Use this note when the first governance-sandbox web demo already has one scenario form and one result-card/report-download path, but you need to decide whether the next pass should stay on stability instead of adding UI scope.

## Keep the next pass in the stability lane when

- the same scenario file should reproduce the same result-card copy and report bundle paths,
- browser-proof checkpoints already exist but still need retry/recovery wording,
- the UI already proves one believable action and the risk is flaky replay, not missing surface area,
- widening the UI would hide a weaker scenario-import or report-download contract.

## Fast check

1. Reopen the scenario-file proof loop first.
2. Confirm the result card still points to one report bundle or download target.
3. Keep the Playwright pass scoped to the same form -> result-card -> report-download path.
4. Only widen the UI after the deterministic replay note and failure-recovery cue are both current.
