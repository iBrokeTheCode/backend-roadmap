# Generated by Django 5.2 on 2025-05-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='product',
            constraint=models.CheckConstraint(condition=models.Q(('price__gt', 0)), name='price_greater_than_zero'),
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.CheckConstraint(condition=models.Q(('stock_count__gt', 0)), name='stock_count_greater_than_zero'),
        ),
    ]
