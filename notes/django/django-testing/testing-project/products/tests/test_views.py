from django.test import SimpleTestCase, TestCase
from django.urls import reverse, reverse_lazy

from products.models import Product


class TestHomePage(SimpleTestCase):
    def setUp(self):
        """Set up a test response."""
        self.response = self.client.get(reverse_lazy('products:homepage'))

    def test_homepage_status_code(self):
        """Test the response's status code."""
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        """Test the template used."""
        self.assertTemplateUsed(self.response, 'products/index.html')

    def test_homepage_contains_message(self):
        """Test the displayed message in the homepage view."""
        self.assertContains(self.response, 'Welcome to our store')

    def test_homepage_contains_welcome_message(self):
        """Test the displayed message in the homepage view AND status code"""
        self.assertContains(self.response, 'Welcome to our store', status_code=200)


class TestProductsPage(TestCase):
    def setUp(self):
        self.url = reverse('products:product-list')
        self.response = self.client.get(self.url)

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Laptop', price=1000, stock_count=5)
        Product.objects.create(name='Phone', price=800, stock_count=10)

    def test_products_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'products/product_list.html')

    def test_products_context(self):
        self.assertEqual(len(self.response.context['products']), 2)

        self.assertContains(self.response, 'Laptop')
        self.assertContains(self.response, 'Phone')

        self.assertNotContains(self.response, 'No products available')

    def test_products_view_no_products(self):
        Product.objects.all().delete()

        # Re-run the get method
        self.response = self.client.get(self.url)

        self.assertEqual(len(self.response.context['products']), 0)
        self.assertContains(self.response, 'No products available')
