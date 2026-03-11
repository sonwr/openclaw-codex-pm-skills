# web qa playwright html heading escape check

Use this note when a generated HTML report looks visually fine but still needs one safety check before signoff.

- Treat report titles and hero headings as untrusted text until the rendered HTML proves they are escaped.
- Verify both the document `<title>` and the visible `<h1>` stay readable without injecting raw markup.
- Keep the check inside the smallest reproducible fixture before widening the replay lane.
