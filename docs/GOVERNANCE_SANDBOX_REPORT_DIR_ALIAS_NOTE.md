# Governance Sandbox report-dir alias note

Use `--report-dir <dir>` when one scenario replay should produce a reusable JSON/Markdown/HTML bundle together.

Quick proof loop:

1. Start from one JSON or YAML scenario file.
2. Run `gov-sandbox run --scenario-file <file> --report-dir <dir>`.
3. Confirm the named bundle plus `report.json`, `report.md`, and `report.html` aliases all exist.
4. Reopen the markdown or HTML report before widening scope.

This keeps scenario input proof and report bundle proof coupled in one reproducible command.
