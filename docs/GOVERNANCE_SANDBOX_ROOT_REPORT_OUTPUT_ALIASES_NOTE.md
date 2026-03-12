# Governance Sandbox Root Report Output Aliases Note

Use this note when a governance-sandbox scenario should stay copy-paste friendly at the root level while still generating the default JSON + Markdown + HTML report trio.

## Keep the slice small

- Prefer one scenario file.
- Keep one proposal plus a small stakeholder set.
- Use one report bundle path per artifact.

## Root-level alias trio

- `report_json_output`
- `report_md_output`
- `report_html_output`

These aliases let a scenario file declare reviewer-visible report paths without nesting a separate `report.outputs.files` block first.

## Proof loop

1. Add the three root-level aliases to one JSON or YAML scenario.
2. Run the smallest CLI replay that emits all three artifacts.
3. Confirm the generated report bundle paths are visible in the JSON payload before widening README or demo work.
