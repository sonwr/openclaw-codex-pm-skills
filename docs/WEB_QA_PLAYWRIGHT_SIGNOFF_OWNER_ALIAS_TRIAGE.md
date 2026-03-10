# Playwright signoff owner-alias triage

Use this note when validation passes but signoff wording still mixes owner aliases, lane names, and unresolved failed checks.

## Quick rule

1. Name the failing lane first.
2. Use one owner alias per lane.
3. Keep unresolved checks visible in the same sentence.
4. Avoid calling the run fully signoff-ready if owner coverage is partial.

## Compact pattern

`Owner alias <alias> should take the next rerun/repair handoff for <lane>; unresolved checks remain <ids>.`

## When to stop

If the sentence needs more than one alias for the same lane, route the handoff through the fuller owner-sequence docs instead of compressing it further.
