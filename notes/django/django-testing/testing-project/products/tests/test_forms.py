from django.test import TestCase
from django.urls import reverse

from products.models import Product


class ProductFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Set up test data for the Product model."""
        cls.url = reverse('products:product-list')

    def test_create_product_when_submitting_valid_form(self):
        """Test creating a product with valid form data."""
        form_data = {'name': 'Tablet', 'price': 299.99, 'stock_count': 50}
        response = self.client.post(path=self.url, data=form_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name='Tablet').exists())

    def test_create_(self):
        """Test creating a product with invalid form data."""
        form_data = {'name': '', 'price': -100, 'stock_count': -10}
        response = self.client.post(path=self.url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('form' in response.context)

        # Check if the form errors
        form = response.context['form']
        self.assertFormError(
            form=form,
            field='name',
            errors='This field is required.',
        )  # type: ignore
        self.assertFormError(
            form=form, field='price', errors='Price cannot be negative'
        )  # type: ignore
        self.assertFormError(
            form=form, field='stock_count', errors='Stock Count cannot be negative'
        )  # type: ignore

        # Check if the product was created
        self.assertFalse(Product.objects.exists())
