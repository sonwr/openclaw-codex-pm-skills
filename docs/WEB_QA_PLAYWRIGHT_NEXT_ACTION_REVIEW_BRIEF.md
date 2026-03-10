# Web QA Playwright next-action review brief

Use this note when a failing report already has a `Next action:` line, but a reviewer still needs a faster human-readable handoff.

## What the brief should answer

1. Which failed checks are covered right now?
2. Which failed checks are still missing from the handoff?
3. Does the next action already mention target refs, artifacts, or a rerun cue?
4. Who should review the handoff before rerunning the flow?

## Recommended brief format

```text
Next-action review brief
- Covered failed checks: F2, F3
- Missing failed checks: none
- Replay support: targets=yes, artifacts=no, rerun=yes
- Reviewer cue: confirm the missing replay dimensions before rerun
```

## Fast interpretation rules

- If `Missing failed checks` is not `none`, fix the `Next action:` line first.
- If replay support is partial, add the missing target refs or artifact refs before asking for rerun approval.
- If the report already names a recovery owner, route the brief to that owner instead of inventing a new reviewer.
- Keep the brief shorter than the full signoff block so it can fit into PR comments or chat updates.

## When to use it

- Before a rerun request in a PR thread
- During incident-style QA handoff between operators
- When the strict report is valid, but the reviewer wants a compact summary instead of scanning all metadata
