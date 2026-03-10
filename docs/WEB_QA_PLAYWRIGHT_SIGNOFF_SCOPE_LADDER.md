# Web QA Playwright signoff scope ladder

Use this ladder after validation passes but the artifact still needs an honest handoff label.

## Scope ladder

1. **Checkpoint scope** — use when one concrete step, target, and proof artifact already explain the next rerun.
2. **Lane scope** — use when multiple checks in the same lane still point to one stable owner and replay path.
3. **Section scope** — use when the blocker spans a whole scenario section and narrower wording would hide real uncertainty.
4. **Hold scope** — use when validation passed but ownership, replay target, or artifact evidence is still incomplete.

## Quick rule

Prefer the narrowest scope that still keeps the real blocker, owner, and proof artifact visible.

## English note

A passing validator result is not automatically a whole-run signoff. Scope the handoff to the smallest honest rerun boundary.
