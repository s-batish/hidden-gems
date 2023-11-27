from django.test import TestCase, Client
from .models import Product, Category


class TestProductsPage(TestCase):
    # Test Products page renders correctly
    def test_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')


class TestProductDetailPage(TestCase):
    # Create a category and product
    def setUp(self):
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

    # Test Product Detail page renders correctly
    def test_product_detail_page(self):
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')


# class TestAddProduct(TestCase):
#     def setUp(self):
#         # Create the category
#         self.category = Category.objects.create(
#             name='test_category',
#             friendly_name='Test Category'
#         )

#         # Create the product
#         self.product = Product.objects.create(
#             category=self.category,
#             sku='12345',
#             name='Test Product',
#             description='Test description',
#             materials='Test materials',
#             price='12.34',
#             id='1'
#         )