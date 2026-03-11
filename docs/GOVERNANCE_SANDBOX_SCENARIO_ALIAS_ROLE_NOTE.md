# Governance Sandbox Scenario Alias Role Note

Use this note when a governance-sandbox scenario import change adds or reviews another stakeholder preset alias such as `role` alongside `preset`, `group`, `trait`, or `persona`.

## Keep the scope narrow

- Prove one alias path at a time.
- Reuse an existing scenario fixture when possible.
- Keep the same proof tied to generated markdown/html report output so the alias change stays user-visible.

## Minimum replay loop

1. Run one JSON or YAML scenario that uses the alias.
2. Confirm the rendered response carries the expected preset.
3. If reports are involved, regenerate markdown/html artifacts from the same scenario file.
4. Rerun the repo validator before handoff.

## Handoff rule

Do not describe an alias expansion as complete unless the scenario import, the simulated preset, and the report bundle still line up in one deterministic replay path.
