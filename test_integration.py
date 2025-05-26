import unittest
import os
import sqlite3
from app import app
from db import init_db

class TestIntegration(unittest.TestCase):
    def setUp(self):
        if os.path.exists('items.db'):
            os.remove('items.db')
        init_db()
        self.client = app.test_client()

    def test_add_and_get_items(self):
        self.client.post('/items', json={'name': 'Orange'})
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Orange', response.get_json())

if __name__ == '__main__':
    unittest.main()
