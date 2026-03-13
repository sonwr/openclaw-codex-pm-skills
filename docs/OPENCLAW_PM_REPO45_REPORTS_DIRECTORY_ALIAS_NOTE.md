# OPENCLAW PM repo-4/repo-5 reports_directory alias note

Keep repo 4 handoff wording and repo 5 implementation work aligned around one shared idea: a scenario file can point at the generated report bundle directory with `reports_directory` without breaking the existing JSON/Markdown/HTML validation loop.

Use it only as a naming convenience. The discipline stays the same:

- prove one imported scenario file,
- regenerate one JSON/Markdown/HTML bundle into the named directory,
- rerun validation,
- then write the short repo-4/repo-5 status line.
