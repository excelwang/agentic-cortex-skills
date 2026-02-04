import unittest
from pathlib import Path

class TestShadowCalc(unittest.TestCase):
    def test_requirements(self):
        f = Path("calculator.html")
        self.assertTrue(f.exists())
        txt = f.read_text()
        self.assertIn("ERROR", txt)
        self.assertIn("Shadow Calculator", txt)

if __name__ == "__main__":
    unittest.main()
