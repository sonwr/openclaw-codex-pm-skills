# Governance Sandbox scenario report verification lane

When improving `governance-sandbox`, keep the smallest reliable proof loop explicit:

1. Load one JSON or YAML scenario file.
2. Generate the JSON, Markdown, and HTML report artifacts in one run.
3. Re-open the emitted paths from the CLI payload before calling the slice done.
4. For UI work, keep one primary result card and one stable download path above the fold.
5. For browser verification, prefer step-by-step checks, reproducible selectors, and rerunnable recovery notes over one-shot happy-path claims.

This lane keeps scenario-file support and report generation improvements tied to replayable evidence instead of vague status updates.
