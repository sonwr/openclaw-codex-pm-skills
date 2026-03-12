# Governance Sandbox Inputs Source Alias Note

Use this note when a governance-sandbox scenario comes from stdin or an `inputs` wrapper and the human still needs the original source label preserved in the generated report metadata.

Keep the proof narrow:

1. import one scenario file or stdin payload,
2. preserve one human-readable `source` / `scenario_source` alias from the `inputs` block when stdin is used,
3. regenerate the same JSON + Markdown + HTML report bundle before widening the work.

This keeps scenario-file-first progress auditable even when the transport path is stdin and the original scenario name would otherwise disappear.
