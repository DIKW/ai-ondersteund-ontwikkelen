import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


class CLITests(unittest.TestCase):
    def test_demo_command_runs(self) -> None:
        repo_root = ROOT
        env = dict(os.environ)
        env["PYTHONPATH"] = str(repo_root / "src")

        result = subprocess.run(
            [sys.executable, "-m", "change_request_tracker.cli", "demo"],
            cwd=repo_root,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("Aangemaakt:", result.stdout)
        self.assertIn("Ingediend:", result.stdout)
