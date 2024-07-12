from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):

    def test_home_page_location(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_home_page_view(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home.html')
