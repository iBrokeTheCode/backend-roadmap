from unittest.mock import patch

from django.test import SimpleTestCase, TestCase
from django.urls import reverse, reverse_lazy
from requests.exceptions import RequestException

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


class TestGetPostView(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up test data for the test suite."""
        cls.post_url = reverse('products:get-post')  # URL for the view being tested.
        cls.endpoint_url = (
            'https://jsonplaceholder.typicode.com/posts/1'  # Mocked external API URL.
        )

    @patch('products.views.requests.get')
    def test_post_view_success(self, mock_get):
        """Test the 'get-post' view for a successful API call."""
        mock_get.return_value.status_code = 200  # Mock API response status code.
        return_data = {
            'userId': 1,
            'id': 1,
            'title': 'Test Title',
            'body': 'Test Body',
        }  # Mock API response data.
        mock_get.return_value.json.return_value = return_data  # Mock API response JSON.

        response = self.client.get(self.post_url)  # Send GET request to the view.
        self.assertEqual(
            response.status_code, 200
        )  # Assert response status code is 200.
        self.assertJSONEqual(
            response.content, return_data
        )  # Assert response JSON matches mocked data.

        mock_get.assert_called_once_with(
            self.endpoint_url
        )  # Verify API was called once with correct URL.

    @patch('products.views.requests.get')
    def test_post_view_fail(self, mock_get):
        """Test the 'get-post' view for a failed API call."""
        mock_get.side_effect = RequestException  # Mock API call to raise an exception.
        response = self.client.get(self.post_url)  # Send GET request to the view.

        self.assertEqual(
            response.status_code, 503
        )  # Assert response status code is 503.

        mock_get.assert_called_once_with(
            self.endpoint_url
        )  # Verify API was called once with correct URL.
