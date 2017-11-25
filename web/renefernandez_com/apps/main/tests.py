from django.test import TestCase, Client


# Create your tests here.
from django.urls import reverse


class HomeTestCase(TestCase):
    client = None

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_home(self):
        # Simple get
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
