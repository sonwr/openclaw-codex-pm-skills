# Web QA signoff scope status line

Use this note when a run is valid enough to hand off, but the public signoff must stay tightly scoped to the evidence that actually passed.

## Recommended status line

`Signoff scope: keep the public PASS scoped to <section/check ids> + <artifact refs> until the broader rerun lands.`

## When to use it

- a replay-ready subset passed, but the full rerun is still pending
- one section is clean while another section is still blocked
- evidence capture is complete for the scoped checks, but not for the wider run

## What to include

1. the exact section or check-id scope
2. the artifact refs that justify the scoped PASS
3. the rerun boundary that is still pending

## Example

`Signoff scope: keep the public PASS scoped to F1-F3 + artifacts/home.png until the visual rerun lands.`
