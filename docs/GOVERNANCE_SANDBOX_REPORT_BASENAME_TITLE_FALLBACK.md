# Governance Sandbox Report Basename Title Fallback

Use this note when a governance-sandbox scenario already defines a report title but does not set an explicit report basename.

## Rule

- Prefer `report.basename` when present.
- Otherwise derive the bundle basename from `report.title` or the resolved scenario report title.
- Keep the filename slug-safe and deterministic.

## Why it helps

This keeps JSON, Markdown, and HTML report bundles reviewer-friendly without forcing every scenario author to duplicate the same naming string in two metadata fields.

## Quick check

1. Run a scenario with `--report-dir`.
2. Confirm the emitted files use the title-derived slug.
3. Confirm explicit `report.basename` still overrides the fallback.
