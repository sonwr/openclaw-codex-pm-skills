# Governance Sandbox report slug alias note

Use this note when a Governance Sandbox scenario fixture should drive one compact report bundle basename without repeating separate JSON, Markdown, and HTML output names.

## Rule

- Prefer `report.slug` inside the scenario file when one URL-safe basename should drive the generated bundle.
- Keep the proof narrow: one scenario file, one `--report-dir`, and one generated JSON/Markdown/HTML bundle.
- Reopen the saved artifact paths after generation so the bundle naming stays visible in review notes.
