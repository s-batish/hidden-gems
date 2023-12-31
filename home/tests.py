from django.test import TestCase


class TestHomePage(TestCase):
    # Tests home page renders correctly
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
