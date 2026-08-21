import os
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


class CLITests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        repo_root = ROOT
        env = dict(os.environ)
        env["PYTHONPATH"] = str(repo_root / "src")
        return subprocess.run(
            [sys.executable, "-m", "change_request_tracker.cli", *args],
            cwd=repo_root,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_demo_command_runs(self) -> None:
        result = self.run_cli("demo")

        self.assertEqual(result.returncode, 0)
        self.assertIn("Aangemaakt:", result.stdout)
        self.assertIn("Ingediend:", result.stdout)
        self.assertIn("In review:", result.stdout)
        self.assertIn("Goedgekeurd:", result.stdout)
        self.assertIn("Gesloten:", result.stdout)
        self.assertIn("Prioriteit aangepast:", result.stdout)
        self.assertIn("Open issues (zonder CLOSED): [2]", result.stdout)
        self.assertIn("Alle issues: [1, 2]", result.stdout)
        self.assertIn("Demo database opgeslagen:", result.stdout)
        self.assertIn("Herladen open issues: [2]", result.stdout)
        self.assertIn("Herladen alle issues: [1, 2]", result.stdout)

    def test_parser_default_db_points_to_dot_issues_json(self) -> None:
        from change_request_tracker.cli import build_parser

        parser = build_parser()
        args = parser.parse_args(["list"])

        self.assertEqual(args.db, ".issues.json")

    def test_demo_command_persists_seeded_data_to_demo_db(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            demo_db_path = Path(tmp) / "demo-issues.json"

            result = self.run_cli("demo", "--demo-db", str(demo_db_path))

            self.assertEqual(result.returncode, 0)
            self.assertTrue(demo_db_path.exists())

            saved_items = json.loads(demo_db_path.read_text(encoding="utf-8"))
            self.assertEqual(len(saved_items), 2)
            self.assertEqual(saved_items[0]["id"], 1)
            self.assertEqual(saved_items[0]["status"], "CLOSED")
            self.assertEqual(saved_items[1]["id"], 2)
            self.assertEqual(saved_items[1]["status"], "DRAFT")
            self.assertEqual(saved_items[1]["priority"], "LOW")

    def test_create_and_list_open_issues(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            db_path = str(Path(tmp) / "issues.json")
            create_result = self.run_cli(
                "--db",
                db_path,
                "create",
                "--title",
                "Bug in export",
                "--description",
                "CSV export mist kolommen",
                "--requester",
                "team-data",
            )
            list_result = self.run_cli("--db", db_path, "list")

        self.assertEqual(create_result.returncode, 0)
        self.assertIn("Issue aangemaakt met id=1", create_result.stdout)
        self.assertEqual(list_result.returncode, 0)
        self.assertIn("id=1", list_result.stdout)
        self.assertIn("status=DRAFT", list_result.stdout)

    def test_list_without_all_hides_closed_issues(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            db_path = str(Path(tmp) / "issues.json")
            self.run_cli(
                "--db",
                db_path,
                "create",
                "--title",
                "Opschonen logbestanden",
                "--description",
                "Cleanup taak toevoegen",
                "--requester",
                "team-platform",
            )
            self.run_cli("--db", db_path, "submit", "1")
            self.run_cli("--db", db_path, "transition", "1", "IN_REVIEW")
            self.run_cli("--db", db_path, "transition", "1", "APPROVED")
            self.run_cli("--db", db_path, "close", "1")

            list_open_result = self.run_cli("--db", db_path, "list")
            list_all_result = self.run_cli("--db", db_path, "list", "--all")

        self.assertEqual(list_open_result.returncode, 0)
        self.assertIn("Geen issues gevonden.", list_open_result.stdout)
        self.assertEqual(list_all_result.returncode, 0)
        self.assertIn("id=1", list_all_result.stdout)
        self.assertIn("status=CLOSED", list_all_result.stdout)
