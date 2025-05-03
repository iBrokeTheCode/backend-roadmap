from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase

from products.models import Product


class ProductModelTest(TestCase):
    def setUp(self) -> None:
        """Set up a test product instance."""
        self.product = Product.objects.create(
            name='Test Product', price=100.00, stock_count=10
        )

    def test_in_stock_property(self):
        """Test the in_stock property."""
        self.assertTrue(self.product.in_stock)

        self.product.stock_count = 0
        self.assertFalse(self.product.in_stock)

    def test_get_discounted_price(self):
        """Test the get_discounted_price method."""
        self.assertEqual(self.product.get_discounted_price(0), 100)
        self.assertEqual(self.product.get_discounted_price(10), 90)
        self.assertEqual(self.product.get_discounted_price(50), 50)

    def test_negative_price_validation(self):
        """Test that a negative price raises a ValidationError."""
        self.product.price = Decimal(-10)

        with self.assertRaises(ValidationError):
            self.product.clean()

    def test_negative_stock_count(self):
        """Test that a negative stock count raises a ValidationError."""
        self.product.stock_count = -10

        with self.assertRaises(ValidationError):
            self.product.clean()
