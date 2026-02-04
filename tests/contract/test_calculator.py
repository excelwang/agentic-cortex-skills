import unittest
from pathlib import Path

class TestSandboxCalc(unittest.TestCase):
    def test_isolated_path(self):
        f = Path("tests/integration/outputs/calculator.html")
        self.assertTrue(f.exists(), "Calculator must be in tests/integration/outputs/")
        txt = f.read_text()
        self.assertIn("ERROR", txt)
        self.assertIn("Sandbox Calculator", txt)

    def test_root_cleanliness(self):
        # Ensure no leak in root
        self.assertFalse(Path("calculator.html").exists(), "Root should be clean of test artifacts")

if __name__ == "__main__":
    unittest.main()
