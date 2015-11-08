f__author__ = 'rene'

from django.core.urlresolvers import reverse
from django.test import TestCase, Client


#Hack. Reverse not working ok for redirects? WHY? WHYYYYYYYY?
def build_test_url(url):
    return 'https://testserver:80'+url


class ViewsTestCase(TestCase):
    #client = None

    #def setUp(self):
    #    # Every test needs a client.
    #    self.client = Client()

    def test_home(self):
        #Simple get
        client = Client()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
