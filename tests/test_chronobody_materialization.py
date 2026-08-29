import subprocess
import tempfile
import unittest
from pathlib import Path

from alex_runtime.chronobody import parse_registry, verify_materialization


REPO = "the-static-collective/ALEX.2"


def run_git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def init_repo(root: Path, origin: str = "https://github.com/the-static-collective/ALEX.2.git") -> str:
    subprocess.run(["git", "init", str(root)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    run_git(root, "config", "user.email", "chronobody@example.test")
    run_git(root, "config", "user.name", "Chronobody Test")
    run_git(root, "remote", "add", "origin", origin)
    tools = root / "tools"
    tools.mkdir(parents=True, exist_ok=True)
    (tools / "echo.py").write_text("print('ok')\n", encoding="utf-8")
    run_git(root, "add", ".")
    run_git(root, "commit", "-m", "initial body")
    return run_git(root, "rev-parse", "HEAD")


def body_entry(sha: str, *, entrypoint: str = "tools/echo.py"):
    value = {
        "schema": "alex.chronobody-registry/v0",
        "organs": [
            {
                "organ_id": "test-organ",
                "body_time_id": f"test-organ@{sha}",
                "status": "INCUBATING",
                "capabilities": ["test_capability"],
                "source": {
                    "repo": REPO,
                    "branch": "test/body",
                    "sha": sha,
                },
                "runtime": {
                    "contract": "python-json-stdio/v0",
                    "entrypoint": entrypoint,
                },
                "authority": "none",
                "parents": [],
            }
        ],
    }
    return parse_registry(value)[0]


class ChronobodyMaterializationTests(unittest.TestCase):
    def test_clean_exact_sha_matching_origin_is_verified(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sha = init_repo(root)
            result = verify_materialization(body_entry(sha), root)
            self.assertEqual(result.disposition, "VERIFIED")
            self.assertIsNone(result.reason_code)
            self.assertEqual(result.observed_sha, sha)
            self.assertEqual(result.source_repo, REPO)

    def test_wrong_head_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registered_sha = init_repo(root)
            (root / "second.txt").write_text("new generation\n", encoding="utf-8")
            run_git(root, "add", ".")
            run_git(root, "commit", "-m", "next body")
            result = verify_materialization(body_entry(registered_sha), root)
            self.assertEqual(result.disposition, "REFUSED")
            self.assertEqual(result.reason_code, "BODY_SHA_MISMATCH")
            self.assertNotEqual(result.observed_sha, registered_sha)

    def test_dirty_checkout_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sha = init_repo(root)
            (root / "dirty.txt").write_text("uncommitted\n", encoding="utf-8")
            result = verify_materialization(body_entry(sha), root)
            self.assertEqual(result.disposition, "REFUSED")
            self.assertEqual(result.reason_code, "DIRTY_BODY")

    def test_wrong_origin_repo_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sha = init_repo(root, "https://github.com/the-static-collective/not-alex.git")
            result = verify_materialization(body_entry(sha), root)
            self.assertEqual(result.disposition, "REFUSED")
            self.assertEqual(result.reason_code, "SOURCE_REPO_MISMATCH")

    def test_matching_ssh_origin_form_is_verified(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sha = init_repo(root, "git@github.com:the-static-collective/ALEX.2.git")
            result = verify_materialization(body_entry(sha), root)
            self.assertEqual(result.disposition, "VERIFIED")

    def test_missing_entrypoint_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sha = init_repo(root)
            result = verify_materialization(body_entry(sha, entrypoint="tools/missing.py"), root)
            self.assertEqual(result.disposition, "REFUSED")
            self.assertEqual(result.reason_code, "ENTRYPOINT_MISSING")

    def test_non_git_directory_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result = verify_materialization(
                body_entry("1111111111111111111111111111111111111111"),
                root,
            )
            self.assertEqual(result.disposition, "REFUSED")
            self.assertEqual(result.reason_code, "NOT_A_GIT_BODY")


if __name__ == "__main__":
    unittest.main()
