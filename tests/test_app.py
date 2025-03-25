import unittest
import sys
import os

# Add the src directory to the path so we can import the app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_endpoint(self):
        response = self.app.get('/')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, CI/CD World!')


if __name__ == '__main__':
    unittest.main()
