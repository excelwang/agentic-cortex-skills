import unittest
from pathlib import Path

class TestFairCalc(unittest.TestCase):
    def test_requirements(self):
        f = Path("calculator.html")
        self.assertTrue(f.exists())
        txt = f.read_text()
        self.assertIn("ERROR", txt)
        self.assertIn("Fair Test Calculator", txt)

if __name__ == "__main__":
    unittest.main()
