import unittest
from pathlib import Path

class TestCalculator(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(Path("calculator.html").exists())

    def test_ui_elements(self):
        content = Path("calculator.html").read_text()
        self.assertIn('id="display"', content)
        self.assertIn('onclick="calculate()"', content)
        self.assertIn('onclick="clearDisplay()"', content)
        self.assertIn('Cortex Engine', content)

if __name__ == "__main__":
    unittest.main()
