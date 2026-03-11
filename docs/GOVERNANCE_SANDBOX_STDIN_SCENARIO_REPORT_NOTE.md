# Governance Sandbox stdin scenario report note

Keep the narrow replay path honest:

1. Pipe one JSON or YAML scenario into stdin.
2. Generate the paired JSON, Markdown, and HTML report artifacts in the same run.
3. Reopen the same artifact bundle when writing PM handoff copy.

This keeps stdin import proof coupled to report-bundle proof instead of splitting them across separate demos.
