from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTest(SimpleTestCase):
    def test_url_exists(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_url_available_by_name(self):
        res = self.client.get(reverse('pages:home'))
        self.assertEqual(res.status_code, 200)

    def test_template_name(self):
        res = self.client.get('/')
        self.assertTemplateUsed(res, 'home.html')


class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        res = self.client.get('/about/')
        self.assertEqual(res.status_code, 200)

    def test_template_name(self):
        res = self.client.get('/about/')
        self.assertTemplateUsed(res, 'about.html')

    def test_url_available_by_name(self):
        res = self.client.get(reverse('pages:about'))
        self.assertEqual(res.status_code, 200)
