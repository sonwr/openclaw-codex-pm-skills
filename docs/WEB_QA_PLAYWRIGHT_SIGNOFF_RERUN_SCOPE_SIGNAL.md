# Web QA Playwright signoff rerun scope signal

Use this note after strict-plus validation passes but a blocked lane still needs a rerun handoff.

## Green
- The next action names one blocked lane or one checkpoint cluster.
- The rerun target is explicit (`section`, `checkpoint`, or stable ref group).
- The artifact or fixture to reopen is named in the handoff.

## Yellow
- The lane is known, but the rerun scope could still expand unless the owner keeps it narrow.
- The handoff names the lane but not the proof artifact.
- Replay support exists, but the stable target still needs confirmation.

## Red
- The handoff asks for a rerun without naming the blocked lane.
- The requested rerun would silently expand into whole-run replay.
- The artifact lacks enough evidence to tell whether rerun or repair is the better next move.

## Recommended status line
> Validation passed, but keep the next rerun scoped to the named blocked lane until the target artifact and proof cue are both explicit.
