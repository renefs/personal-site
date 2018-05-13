# coding=utf-8
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


class SetLangTestCase(TestCase):
    client = None

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_english(self):
        # Simple post
        response = self.client.post(reverse('set_language'), data={'language': 'en'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to my personal website.", status_code=200)

    def test_spanish(self):
        # Simple post
        response = self.client.post(reverse('set_language'), data={'language': 'es'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenido a mi página personal", status_code=200)