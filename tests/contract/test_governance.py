import os
import unittest

class TestGovernance(unittest.TestCase):
    def test_specs_exist(self):
        """Verify that the critical specification files exist."""
        required_specs = [
            "specs/01-ARCHITECTURE.md",
            "specs/20-QUALITY_ASSURANCE.md"
        ]
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
        
        for spec in required_specs:
            spec_path = os.path.join(project_root, spec)
            self.assertTrue(os.path.exists(spec_path), f"Missing required spec: {spec}")

if __name__ == '__main__':
    unittest.main()
