from django.test import TestCase


class TestBagPage(TestCase):
    # Test Bag page renders correctly
    def test_bag_page(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
