from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    pass


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_count = models.IntegerField(default=0)

    @property
    def in_stock(self):
        return self.stock_count > 0

    def clean(self):
        if self.price < 0:
            raise ValidationError('Price cannot be negative')
        if self.stock_count < 0:
            raise ValidationError('Stock Count cannot be negative')

    def get_discounted_price(self, discount_percentage: int) -> Decimal:
        return self.price * Decimal(1 - discount_percentage / 100)
