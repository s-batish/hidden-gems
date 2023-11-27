from django.test import TestCase
from .models import Contact


class TestContactPage(TestCase):
    # Test Contact page renders correctly
    def test_our_classes_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
