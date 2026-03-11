from pathlib import Path


def test_readme_mentions_governance_sandbox_web_demo_ui_ux_playwright_handoff() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "docs/GOVERNANCE_SANDBOX_WEB_DEMO_UI_UX_PLAYWRIGHT_HANDOFF.md" in readme
    assert "ui-ux-pro-max layout rules and Playwright stability checks" in readme
