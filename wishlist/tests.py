from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from .models import Wishlist
from products.models import Product, Category


class TestViewWishlist(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="test",
            password="password123"
        )

    def test_wishlist_page(self):
        # Test Wishlist page renders correctly
        self.client.login(username="test", password="password123")
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')


class TestAddToWishlist(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="test",
            password="password123"
        )

        # Create the category
        self.category = Category.objects.create(
            name='test_category',
            friendly_name='Test Category'
        )

        # Create the product
        self.product = Product.objects.create(
            category=self.category,
            sku='12345',
            name='Test Product',
            description='Test description',
            materials='Test materials',
            price='12.34',
            id='1'
        )

    def test_add_to_wishlist(self):
        # Add to wishlist
        self.client.login(username='test', password='password123')
        response = self.client.post(reverse('wishlist'), {
            'user':self.user.username,
            'product':self.product,
            'date_added':date.today,
        })
        self.assertEqual(response.status_code, 200)


class TestRedirectViews(TestCase):
    # Tests when a user is not logged in

    def test_add_to_wishlist_unauthorised(self):
        response = self.client.get('/wishlist/')
        self.assertEqual(response.status_code, 302)
