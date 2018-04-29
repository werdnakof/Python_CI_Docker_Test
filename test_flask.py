import os
import app
import unittest

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'Hello world! You are not a twat!' in rv.data, "wrong phrase"

if __name__ == '__main__':
    unittest.main()
