# Playwright signoff blocker language

Use this quick card when a strict-plus report passes validation but still should not be described as signoff-ready.

## Prefer these phrases

- `validator-clean but blocked by missing owner coverage`
- `replay-ready for inspection, not yet signoff-ready`
- `passing artifact with unresolved hotspot owner routing`
- `signoff delayed until the next action names the blocked lane and proof target`

## Avoid these phrases

- `done`
- `fully ready`
- `good to merge`

Those phrases hide the difference between a passing validator result and a genuinely handoff-ready artifact.

## Minimal status line

`PASS, but signoff remains blocked by <owner-gap or hotspot>.`
