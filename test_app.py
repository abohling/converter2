from urllib import response
from app import app
from unittest import TestCase


class TestRoute(TestCase):
    def test_intake_form(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Currency Converter</h1>', html)
