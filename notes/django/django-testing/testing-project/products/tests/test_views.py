from django.test import SimpleTestCase, TestCase
from django.urls import reverse, reverse_lazy

from products.models import Product, User


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
        """Set up a test response."""
        self.url = reverse('products:product-list')
        self.response = self.client.get(self.url)

    @classmethod
    def setUpTestData(cls):
        """Set up test data for the product list view."""
        Product.objects.create(name='Laptop', price=1000, stock_count=5)
        Product.objects.create(name='Phone', price=800, stock_count=10)

    def test_products_uses_correct_template(self):
        """Test the template used for the product list view."""
        self.assertTemplateUsed(self.response, 'products/product_list.html')

    def test_products_context(self):
        """Test the context data passed to the template."""
        self.assertEqual(len(self.response.context['products']), 2)

        self.assertContains(self.response, 'Laptop')
        self.assertContains(self.response, 'Phone')

        self.assertNotContains(self.response, 'No products available')

    def test_products_view_no_products(self):
        """Test the product list view when no products are available."""
        Product.objects.all().delete()

        # Re-run the get method
        self.response = self.client.get(self.url)

        self.assertEqual(len(self.response.context['products']), 0)
        self.assertContains(self.response, 'No products available')


class TestProfilePage(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up test data for the profile view."""
        cls.profile_url = reverse('products:profile')
        cls.login_url = reverse('products:login')

    def test_profile_view_redirects_for_anonymous_users(self):
        """Test that anonymous users are redirected to the login page."""
        response = self.client.get(self.profile_url)
        expected_url = f'{self.login_url}?next={self.profile_url}'

        self.assertRedirects(response, expected_url)

    def test_profile_view_accessible_for_authenticated_users(self):
        """Test that authenticated users can access the profile view."""
        User.objects.create_user(username='username', password='password')  # Create
        self.client.login(username='username', password='password')  # Login

        response = self.client.get(self.profile_url)
        self.assertContains(response, 'username')
