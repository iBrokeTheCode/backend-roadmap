from django.test import SimpleTestCase
from django.urls import reverse_lazy


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
