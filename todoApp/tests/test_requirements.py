import os
import unittest


class TestRequirements(unittest.TestCase):
    def test_flask_present(self):
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        requirements_path = os.path.join(current_script_dir, "..",
                                         "requirements.txt")
        with open(requirements_path) as f:
            requirements = f.read()
        self.assertIn('Flask==3.2.1', requirements)

    def test_sqlalchemy_present(self):
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        requirements_path = os.path.join(current_script_dir, "..",
                                         "requirements.txt")
        with open(requirements_path ) as f:
            requirements = f.read()
        self.assertIn('SQLAlchemy==2.0.24', requirements)

    def test_jinja_present(self):
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        requirements_path = os.path.join(current_script_dir, "..",
                                         "requirements.txt")
        with open(requirements_path ) as f:
            requirements = f.read()
        self.assertIn('Jinja2==3.1.2', requirements)

if __name__ == '__main__':
    unittest.main()

