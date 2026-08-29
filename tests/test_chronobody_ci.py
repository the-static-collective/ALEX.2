import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "crucible.yml"


class ChronobodyCiTests(unittest.TestCase):
    def test_historical_body_checkouts_do_not_persist_repository_credentials(self):
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        checkout_count = workflow.count("uses: actions/checkout@v4")
        self.assertGreaterEqual(checkout_count, 3)
        self.assertEqual(
            workflow.count("persist-credentials: false"),
            checkout_count,
            "every checkout in the historical-body CI job must drop repository credentials",
        )


if __name__ == "__main__":
    unittest.main()
