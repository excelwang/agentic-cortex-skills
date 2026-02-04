import os
import subprocess
import unittest
import shutil
from pathlib import Path

class TestPersonaReadiness(unittest.TestCase):
    """
    Integration test verifying that each persona's readiness check reports the correct evidence.
    """
    def setUp(self):
        self.tmp_path = Path("./tmp_readiness_env")
        if self.tmp_path.exists():
            shutil.rmtree(self.tmp_path)
        self.tmp_path.mkdir(parents=True)
        # Note: ready_check.py checks for these directories
        (self.tmp_path / "tickets" / "active").mkdir(parents=True)
        (self.tmp_path / "tickets" / "backlog").mkdir(parents=True)
        # We don't create specs here to test the False case

    def tearDown(self):
        if self.tmp_path.exists():
            shutil.rmtree(self.tmp_path)

    def test_architect_readiness(self):
        script_path = Path("skills/architectural-design/scripts/ready_check.py").absolute()
        
        # 1. Test when specs dir is missing
        result = subprocess.run(["python3", str(script_path)], cwd=self.tmp_path, capture_output=True, text=True)
        self.assertIn("[SPECS_DIR:False]", result.stdout)

        # 2. Test when specs dir exists but files are missing
        (self.tmp_path / "specs").mkdir()
        result = subprocess.run(["python3", str(script_path)], cwd=self.tmp_path, capture_output=True, text=True)
        self.assertIn("[SPECS_DIR:True]", result.stdout)
        self.assertIn("[ARCH:False]", result.stdout)

        # 3. Test when specs exist
        (self.tmp_path / "specs" / "01-ARCHITECTURE.md").touch()
        result = subprocess.run(["python3", str(script_path)], cwd=self.tmp_path, capture_output=True, text=True)
        self.assertIn("[ARCH:True]", result.stdout)

    def test_executor_readiness(self):
        script_path = Path("skills/code-implementation/scripts/ready_check.py").absolute()
        result = subprocess.run(["python3", str(script_path)], cwd=self.tmp_path, capture_output=True, text=True)
        self.assertIn("REPORT: [ACTIVE:False]", result.stdout)

        (self.tmp_path / "tickets" / "active" / "TICKET-1.md").touch()
        result = subprocess.run(["python3", str(script_path)], cwd=self.tmp_path, capture_output=True, text=True)
        self.assertIn("[ACTIVE:True]", result.stdout)

    def test_judge_readiness(self):
        script_path = Path("skills/code-review/scripts/ready_check.py").absolute()
        subprocess.run(["git", "init"], cwd=self.tmp_path, capture_output=True)
        result = subprocess.run(["python3", str(script_path)], cwd=self.tmp_path, capture_output=True, text=True)
        self.assertIn("REPORT: [GIT_DIFF:False]", result.stdout)

if __name__ == "__main__":
    unittest.main()
