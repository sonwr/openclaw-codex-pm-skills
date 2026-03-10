# WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_CUE

Use this quick cue when validation passes but the handoff still feels vague.

## Ask three questions

1. **Who owns the next action?** Name a role, team, or directly responsible operator.
2. **What proof must they touch first?** Point to the failed lane, target ref, or artifact path.
3. **What outcome closes the loop?** State the replay/rerun condition that would make the report handoff-ready.

## Copy-ready pattern

`Owner: <role/team> should rerun <lane/checkpoint> using <target/artifact> and confirm <expected recovery signal>.`

## When to use it

- Validation is green, but `Next action:` still sounds generic.
- Owner coverage exists in fragments across the report, but not in one sentence.
- A reviewer needs a compact owner-first handoff before merge or rerun.
