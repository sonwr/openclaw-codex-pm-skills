# Effective Replay Blockers

Use this note when a report says `Replay readiness: READY` but the validator still downgrades the effective replay state to `BLOCKED`.

## What counts as an effective blocker?

The validator keeps both the declared signoff value and the computed effective value.

Effective replay blockers are currently derived from the metadata keys below:

- `blocked_without_regressions`
- `ready_with_regressions`
- `missing_target_refs`
- `missing_artifact_refs`
- `incomplete_evidence_refs`
- `missing_timestamps`

A report can look operationally healthy while still failing replay handoff requirements when checkpoint traceability is incomplete.

## Fast triage order

1. Check `effective_replay_readiness` before trusting the human-written signoff line.
2. Review `effective_replay_readiness_blocker_keys` to see which replay guarantees failed.
3. Review `effective_replay_readiness_blocker_count_by_section` to find the noisiest section first.
4. Inspect `missing_checkpoint_evidence_dimensions_by_section` to see whether the missing proof is target refs, artifact refs, timestamps, or a mix.
5. Fix the highest-volume missing dimension and rerun validation.

## Why this matters

A clean handoff needs more than a PASS/FAIL answer. It needs enough deterministic traceability for a second operator to reproduce the same failing or passing path without guessing.

That is why the validator preserves both:

- the author-declared replay status, and
- the effective replay status computed from the evidence map.

When they differ, automation should trust the effective value and surface the blocker keys in the handoff summary.
