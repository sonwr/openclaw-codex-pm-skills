# OpenClaw PM Five-Repo Recheck + Validate Note

Before publishing the five-line report, recheck the repositories in the fixed order and keep the same gate visible in each pass:

1. `openclaw-codex-pm-skills`
2. `prompt-regression-min`
3. `awesome-agent-skills-ko`
4. `oss-launchpad-cli`
5. `governance-sandbox`

Rules:

- Repos 4 and 5 are mandatory in every run.
- Count progress only when a real small slice changed.
- Commit and push only after local validation passes for that repo.
- If validation fails, hold commit/push and keep the one-line status explicit about the reason.
