# Governance Sandbox scenario trait alias note

When a scenario file uses a stakeholder map, prefer keeping the stakeholder name as the map key and use one preset field per entry.

Accepted preset aliases for map-style stakeholder entries:

- `preset`
- `trait_preset`
- `trait`
- `persona`
- `group`
- `role`

Use this when you want JSON/YAML scenario files to stay readable while still mapping to the built-in governance stakeholder presets.
