# Governance sandbox top-level proposal copy markdown note

Keep the scenario-file lane tolerant of compact fixtures that place `proposal_copy_markdown` at the top level when the goal is to prove one imported proposal plus one regenerated report bundle quickly.

## Why it matters

- Workshop fixtures sometimes arrive as a flat proposal copy plus stakeholder list.
- The smallest scenario-file proof should not require wrapping proposal text inside a nested `proposal` object.
- This keeps phase-one work focused on scenario-file import plus report generation before broader preset or web-demo scope.
