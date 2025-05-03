from decimal import Decimal

from django.db import IntegrityError
from django.test import TestCase

from products.models import Product


class ProductModelTest(TestCase):
    # def setUp(self) -> None:
    #     """Set up a test product instance."""
    #     self.product = Product.objects.create(
    #         name='Test Product', price=100.00, stock_count=10
    #     )
    #     print('Setting up test data...')

    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(
            name='Test Product', price=100.00, stock_count=10
        )
        print('Setting up test data...')

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

    # NOTE: Commented because the validation was moved to forms.py file
    # def test_negative_price_validation(self):
    #     """Test that a negative price raises a ValidationError."""
    #     self.product.price = Decimal(-10)

    #     with self.assertRaises(ValidationError):
    #         self.product.clean()

    # NOTE: Commented because the validation was moved to forms.py file
    # def test_negative_stock_count(self):
    #     """Test that a negative stock count raises a ValidationError."""
    #     self.product.stock_count = -10

    #     with self.assertRaises(ValidationError):
    #         self.product.clean()

    def test_negative_price_constraint(self):
        """Test that a negative price raises an IntegrityError."""
        self.product.price = Decimal(-100)

        with self.assertRaises(IntegrityError):
            self.product.save()

    def test_zero_price_constraint(self):
        """Test that a zero price raises an IntegrityError."""
        self.product.price = Decimal(0)

        with self.assertRaises(IntegrityError):
            self.product.save()

    def test_negative_stock_count_constraint(self):
        """Test that a negative stock count raises an IntegrityError."""
        self.product.stock_count = -100

        with self.assertRaises(IntegrityError):
            self.product.save()

    def test_zero_stock_count_constraint(self):
        """Test that a zero stock count raises an IntegrityError."""
        self.product.stock_count = 0

        with self.assertRaises(IntegrityError):
            self.product.save()
