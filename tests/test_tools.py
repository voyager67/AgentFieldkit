"""Regression tests for AgentFieldkit's library tooling."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skills import parse_frontmatter  # noqa: E402


class FrontmatterTests(unittest.TestCase):
    def test_valid_frontmatter(self):
        data, error = parse_frontmatter("---\nname: demo-skill\ndescription: A demo.\n---\n\n# Demo\n")
        self.assertIsNone(error)
        self.assertEqual(data["name"], "demo-skill")
        self.assertEqual(data["description"], "A demo.")

    def test_missing_frontmatter(self):
        data, error = parse_frontmatter("# Just markdown\n")
        self.assertIsNone(data)
        self.assertIn("frontmatter", error)

    def test_duplicate_key_is_rejected(self):
        data, error = parse_frontmatter("---\nname: a\nname: b\ndescription: x\n---\n\nBody\n")
        self.assertIsNone(data)
        self.assertIn("duplicate", error)


class LibraryTests(unittest.TestCase):
    def test_index_matches_skill_directories(self):
        index = json.loads((ROOT / "skills-index.json").read_text(encoding="utf-8"))
        skill_dirs = [p for p in (ROOT / "skills").iterdir() if p.is_dir() and (p / "SKILL.md").is_file()]
        self.assertEqual(index["skill_count"], len(skill_dirs))
        self.assertEqual({x["name"] for x in index["skills"]}, {p.name for p in skill_dirs})

    def test_validator_succeeds(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_skills.py")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)

    def test_single_skill_package_has_expected_root(self):
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp) / "packages"
            result = subprocess.run([
                sys.executable, str(ROOT / "scripts" / "package_chatgpt.py"),
                "--skill", "failure-forensics", "--output", str(out),
            ], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
            archive = out / "failure-forensics.zip"
            self.assertTrue(archive.exists())
            with zipfile.ZipFile(archive) as zf:
                self.assertIn("failure-forensics/SKILL.md", zf.namelist())

    def test_installer_dry_run_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "not-created"
            result = subprocess.run([
                sys.executable, str(ROOT / "scripts" / "install_skills.py"),
                "--agent", "generic", "--destination", str(destination),
                "--skill", "failure-forensics", "--dry-run",
            ], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
            self.assertIn("planned", result.stdout)
            self.assertFalse(destination.exists())

    def test_installer_preserves_existing_skill_by_default(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "skills"
            existing = destination / "failure-forensics"
            existing.mkdir(parents=True)
            marker = existing / "LOCAL_EDIT.txt"
            marker.write_text("keep this local file", encoding="utf-8")
            result = subprocess.run([
                sys.executable, str(ROOT / "scripts" / "install_skills.py"),
                "--agent", "generic", "--destination", str(destination),
                "--skill", "failure-forensics",
            ], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
            self.assertIn("skipped", result.stdout)
            self.assertEqual(marker.read_text(encoding="utf-8"), "keep this local file")


if __name__ == "__main__":
    unittest.main()
