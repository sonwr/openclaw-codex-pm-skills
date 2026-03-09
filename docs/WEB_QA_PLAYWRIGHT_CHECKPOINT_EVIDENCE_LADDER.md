# Web QA Playwright checkpoint evidence ladder

Use this note when an interactive browser run needs deterministic proof at each checkpoint.

## Goal

Keep every checkpoint replayable by storing evidence in a fixed order instead of relying on memory or prose-only notes.

## Evidence ladder

1. **Stable target reference first**
   - Capture the UI target ref (`aria`/stable ref) before clicking or typing.
   - If the ref changes mid-run, record the new ref and note the reason.
2. **Action record second**
   - Log one action per checkpoint.
   - Keep action language literal enough that another operator can replay it.
3. **Verification third**
   - Record the observable state change that proves the action succeeded.
   - Prefer exact labels, URLs, visible text, or enabled/disabled states over interpretation.
4. **Artifact path fourth**
   - Attach the screenshot, trace, or exported JSON path that proves the checkpoint state.
   - If no artifact exists, mark the checkpoint as blocked instead of hand-waving.
5. **Recovery note last**
   - If something drifted, explain the smallest repair step needed before rerun.

## Repair order when a checkpoint fails

1. Re-establish the correct page/profile/session.
2. Repair missing target refs.
3. Repair missing artifact paths.
4. Repair chronology/timestamps.
5. Re-run only the failed checkpoint before broad replay.

## Operator rule of thumb

If a checkpoint cannot answer **what target, what action, what proof, what artifact** in under a few seconds, it is not replay-ready yet.
