from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CheckConstraint, Q


class User(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_count = models.IntegerField(default=0)

    @property
    def in_stock(self):
        return self.stock_count > 0

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(price__gt=0),
                name='price_greater_than_zero',
                violation_error_message='Price must be greater than zero',
            ),
            CheckConstraint(
                check=Q(stock_count__gt=0),
                name='stock_count_greater_than_zero',
                violation_error_message='Stock Count must be greater than zero',
            ),
        ]

    def clean(self):
        if self.price < 0:
            raise ValidationError('Price cannot be negative')
        if self.stock_count < 0:
            raise ValidationError('Stock Count cannot be negative')

    def get_discounted_price(self, discount_percentage: int) -> Decimal:
        return Decimal(self.price) * (1 - Decimal(discount_percentage) / Decimal(100))
