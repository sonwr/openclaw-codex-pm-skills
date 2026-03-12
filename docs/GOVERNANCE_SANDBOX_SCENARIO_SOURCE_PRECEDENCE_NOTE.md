# Governance Sandbox Scenario Source Precedence Note

When `governance-sandbox run --scenario-file <path>` is used, the saved report metadata should keep the resolved file path as the scenario source of record.

Use nested source aliases such as `inputs.source` only for stdin-driven flows (`--scenario-file -`) where no filesystem path exists.

This keeps replay evidence deterministic while still allowing browser forms and piped fixtures to preserve an author-facing source label.
