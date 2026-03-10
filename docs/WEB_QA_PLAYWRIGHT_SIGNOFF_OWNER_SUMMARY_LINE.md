# Web QA Playwright signoff owner summary line

Use this when validation already passes but the report still needs a one-line owner-aware handoff.

## When to use it

Use this note after `python3 -m unittest discover -s tests` stays green and the report metadata already exposes failed-check owner coverage.
It helps distinguish a validator-clean artifact from a handoff-ready signoff sentence.

## Summary line template

`Signoff owner summary: <owner or unowned> owns <failed checks>; next action covers <covered checks>; unresolved <remaining checks>.`

## Fill rules

- Prefer the dominant recovery owner first.
- If some failed checks have no owner, say `unowned` explicitly.
- Keep failed-check ids visible in the sentence.
- Mention whether the next action already covers all failed checks or only a subset.

## Example

`Signoff owner summary: qa-runtime owns F3,F4; next action covers F3; unresolved F4.`
