# Governance Sandbox stdin report status note

Keep stdin-driven governance-sandbox replays in the same proof lane as file-based runs:

- feed one JSON or YAML scenario through stdin,
- generate one JSON/Markdown/HTML report bundle,
- and mention the shared bundle status in the maintainer handoff.

This keeps scenario-input proof and report-output proof readable even when the scenario path is `stdin`.
