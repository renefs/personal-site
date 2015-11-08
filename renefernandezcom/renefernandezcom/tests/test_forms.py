from django.test import TestCase
from renefernandezcom.forms import ContactForm


class FormTests(TestCase):

    def test_invalid_form(self):
        form_data = {'name': 'something', 'email': 'blublue', 'message': 'text'}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        form_data = {'name': 'something',
                     'email': 'fake@email.com',
                     'message': 'text',
                     'captcha_0': 'dummy-value',
                     'captcha_1': 'PASSED'}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

