# Django Models and Database Interaction

## 1. Django Models

**Theory:**

- Django models are Python classes that define the structure of your database tables.
- Each model maps to a single database table.
- Django's ORM (Object-Relational Mapper) allows you to interact with the database using Python code.

**Key Concepts:**

- **Fields:** Model attributes that represent database columns (e.g., CharField, IntegerField, TextField).
- **Model Class:** Defines the table structure and behavior.
- **ORM:** Translates Python code into SQL queries.

**Example:**

```py
from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=200)
        description = models.TextField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        stock = models.IntegerField()

        def __str__(self):
            return self.name
```

**Explanation:**

- This code defines a Product model with four fields: name, description, price, and stock.
- The `__str__` method defines how the model object is represented as a string.

## 2. Database Migrations

**Theory:**

- Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
- Django tracks these changes and generates SQL queries to update the database.

**Steps:**

- **Make Migrations:** `python manage.py makemigrations` (creates migration files based on model changes)
- **Apply Migrations:** `python manage.py migrate` (applies the migrations to the database)

**Importance:**

- Essential for keeping your database schema in sync with your models.
- Allows for version control of your database schema.

## 3. Database Interaction (CRUD Operations)

**Theory:**

- Django's ORM provides a Pythonic way to perform CRUD (Create, Read, Update, Delete) operations on your database.

**Examples:**

```py
def run():
    # CREATE
    product = Product(name="Laptop", description="Powerful laptop", price=1200.00, stock=10)
    product.save()

    # READ
    products = Product.objects.all() # Get all products
    product = Product.objects.get(id=1) # Get product with id 1
    products = Product.objects.filter(price__gt=1000) # Get products with price greater than 1000

    # UPDATE
    product = Product.objects.get(id=1)
    product.price = 1300.00
    product.save()

    # DELETE
    product = Product.objects.get(id=1)
    product.delete()
```

**Explanation:**

- `Product.objects.all():` Retrieves all Product objects from the database.
- `Product.objects.get(id=1):` Retrieves the Product object with id equal to 1.
- `Product.objects.filter(price\_\_gt=1000):` Retrieves Product objects with price greater than 1000.
- `product.save():` Saves the Product object to the database.
- `product.delete():` Deletes the Product object from the database.

## 4. Django Admin Interface:

**Theory:**

- Django provides a built-in admin interface for managing your models.
- It's automatically generated based on your models.

**Steps:**

- **Create a Superuser:** `python manage.py createsuperuser`
- **Register Models:** In `myapp/admin.py`, register your models:

```py
from django.contrib import admin
from .models import Product

admin.site.register(Product)
```

- **Access the Admin Interface:**
  - Go to `http://127.0.0.1:8000/admin/` in your browser.
  - Log in with the superuser credentials.
