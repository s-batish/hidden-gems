from django.test import TestCase
from django.urls import reverse
from .models import Review
from products.models import Product, Category
from django.contrib.auth.models import User
from datetime import date


class TestAddReview(TestCase):
    # Test cases for leaving a review for a logged in user
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
        )

    def test_add_review(self):
        # Add a review
        self.client.login(username='test', password='password123')
        response = self.client.post(reverse(
            'product_detail', args=[self.product.id]), {
            'author': self.user.username,
            'product': self.product,
            'created_on': date.today,
            'body': 'Great product'
        })
        self.assertEqual(response.status_code, 200)
