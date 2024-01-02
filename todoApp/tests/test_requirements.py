import unittest

class TestRequirements(unittest.TestCase):
    def test_flask_present(self):
        with open('./requirements.txt') as f:
            requirements = f.read()
        self.assertIn('Flask==3.0.0', requirements)

    def test_sqlalchemy_present(self):
        with open('./requirements.txt') as f:
            requirements = f.read()
        self.assertIn('SQLAlchemy==2.0.24', requirements)

    def test_jinja_present(self):
        with open('./requirements.txt') as f:
            requirements = f.read()
        self.assertIn('Jinja2==3.1.2', requirements)

if __name__ == '__main__':
    unittest.main()

