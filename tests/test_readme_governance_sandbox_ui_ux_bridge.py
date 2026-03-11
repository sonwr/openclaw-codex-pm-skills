from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReadmeGovernanceSandboxUiUxBridgeTests(unittest.TestCase):
    def test_readme_mentions_governance_sandbox_ui_ux_bridge_note(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("docs/GOVERNANCE_SANDBOX_UI_UX_PRO_MAX_BRIDGE.md", readme)
        self.assertTrue((ROOT / "docs" / "GOVERNANCE_SANDBOX_UI_UX_PRO_MAX_BRIDGE.md").exists())


if __name__ == "__main__":
    unittest.main()
