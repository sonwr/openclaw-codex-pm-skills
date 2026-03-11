from pathlib import Path


def test_readme_mentions_governance_sandbox_web_demo_form_to_card_acceptance() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_WEB_DEMO_FORM_TO_CARD_ACCEPTANCE.md" in readme
    assert "one form-to-card acceptance lane" in readme
