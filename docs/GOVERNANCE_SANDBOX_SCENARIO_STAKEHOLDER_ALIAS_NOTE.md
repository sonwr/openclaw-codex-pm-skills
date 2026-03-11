# Governance Sandbox scenario stakeholder alias note

Keep mapping-style scenario fixtures readable by allowing each stakeholder object to override the outer map key with `stakeholder`.

- Use it when YAML/JSON generators already emit stable ids as map keys.
- Pair it with `role`, `group`, `trait`, `persona`, or `cohort` so the same fixture still resolves a built-in preset.
- Validate with one replayable scenario-file run before widening report or web-demo scope.
