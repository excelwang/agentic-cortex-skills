import unittest
from pathlib import Path

class TestReadmeFooter(unittest.TestCase):
    def test_footer_exists(self):
        readme_path = Path("README.md")
        self.assertTrue(readme_path.exists())
        content = readme_path.read_text()
        self.assertIn("VERSION: 1.0.0", content)
        self.assertIn("BUILD: LATEST", content)

if __name__ == "__main__":
    unittest.main()
