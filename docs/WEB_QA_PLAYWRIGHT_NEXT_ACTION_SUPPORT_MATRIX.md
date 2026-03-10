# Web QA Playwright next-action replay support matrix

Use this quick matrix after strict or strict-plus validation when the report already names failed checks but the rerun handoff still feels incomplete.

## Support levels

- `target_and_artifact_refs` — next action already includes stable target refs and proof artifacts; rerun can usually start immediately.
- `target_refs_only` — operator knows where to act, but still needs fresh proof capture instructions.
- `artifact_refs_only` — proof exists, but the operator still needs stable target refs before replay.
- `none` — next action is still prose-only; treat it as a repair note, not a replay-ready handoff.

## Recommended operator response

- `target_and_artifact_refs` → keep the failed check ids, rerun only the named lane, and verify fresh proof replaces the old artifact.
- `target_refs_only` → preserve the target refs and add the first artifact to capture before handoff.
- `artifact_refs_only` → preserve the proof path and add stable target refs before rerun.
- `none` → rewrite the next action with failed check ids, target refs, artifact refs, and a rerun cue.

## Fast phrasing guide

- `target_and_artifact_refs` → "rerun F2 on ref=e12 and refresh `artifacts/f2.png`"
- `target_refs_only` → "rerun F2 on ref=e12 and capture a new failure screenshot"
- `artifact_refs_only` → "reproduce F2, confirm the failing target ref, and refresh `artifacts/f2.png`"
- `none` → "rerun F2 on the failing target, capture fresh proof, and update the handoff with stable refs"
