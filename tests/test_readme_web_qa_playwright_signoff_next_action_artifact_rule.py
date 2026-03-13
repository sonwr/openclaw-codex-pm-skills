from pathlib import Path


def test_readme_mentions_web_qa_playwright_signoff_next_action_artifact_rule() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/WEB_QA_PLAYWRIGHT_SIGNOFF_NEXT_ACTION_ARTIFACT_RULE.md" in readme
