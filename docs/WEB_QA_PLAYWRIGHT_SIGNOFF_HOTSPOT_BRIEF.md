# WEB_QA_PLAYWRIGHT_SIGNOFF_HOTSPOT_BRIEF

Use this when strict-plus validation already surfaced the hottest blocked lane and you need a compact signoff-ready brief before rerun handoff.

## Four-line brief

1. **Hotspot lane** — name the section or checkpoint with the highest blocker weight.
2. **Owner** — name the role or team expected to rerun or repair it.
3. **Proof target** — point to the artifact path, checkpoint id, or target ref they should touch first.
4. **Exit signal** — state the signal that would let the report graduate from validator-clean to handoff-ready.

## Copy-ready pattern

`Hotspot: <lane/checkpoint> remains the top blocker. Owner: <role/team>. First proof target: <artifact/target>. Exit signal: <rerun or recovery proof>.`

## Use it when

- validation passes but the report still needs a shortest-path rerun brief,
- hotspot metadata exists across JSON fields but is not yet handoff-readable,
- a reviewer wants one signoff sentence before opening deeper replay docs.
