# WEB_QA Playwright signoff alias scope rule

Use this note when a validator-passing artifact has owner aliases but the signoff sentence still risks sounding broader than the actual replay scope.

## When to use it

Use this rule when all of the following are true:

- the validator passes,
- owner aliases are present,
- and the handoff needs to stay lane-scoped, section-scoped, or rerun-scoped instead of sounding whole-run ready.

## Scope wording rule

1. Name the narrowest replay scope first (`checkpoint`, `lane`, or `section`).
2. Name the owner alias second.
3. Name the proof artifact or rerun target third.
4. Avoid broad words like `complete`, `fully ready`, or `done` unless the whole report actually supports that claim.

## Compact sentence pattern

`PASS for <scope>; <owner alias> owns the next rerun or repair step against <target/artifact>.`

## Quick examples

- `PASS for checkout lane; qa-frontend owns the next rerun against payment-confirmation screenshot evidence.`
- `PASS for accessibility section; qa-a11y owns the next repair loop against keyboard-nav replay notes.`

## Exit check

If the sentence still sounds like the entire run is signoff-ready, shrink the scope wording before posting the handoff.
