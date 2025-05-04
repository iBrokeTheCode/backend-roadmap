# Testing Database Constraints

## 1. Core Concepts

- **Model Validation (`clean` method):** Django models can have a `clean` method to perform custom validation. This method, along with field-specific validators and `validate_constraints`, are part of the four validation steps called by `full_clean`. The `full_clean` method is automatically invoked when using a **Django model form's** `is_valid()` method. However, the `clean` method and the other validation steps are **not automatically called when you simply call `model.save()`**. This means data that fails model validation can still be saved to the database if `save()` is called directly without first calling `full_clean()`. The `clean` method is useful for catching validation issues early in the Python code, preventing unnecessary database interactions, especially when used with forms.
- **Database Constraints:** These are rules applied at the database level to **enforce data integrity**. Unlike Python-based model validation, database constraints are enforced by the database itself whenever data is inserted or updated, providing a robust guarantee. They are essential because developers might bypass model validation or accidentally remove it.
- **`CheckConstraint`:** A specific type of database constraint in Django that allows you to define **conditional logic** that must be true for data to be saved. `CheckConstraint`s are defined within the **`Meta` inner class** of a Django model in a list or tuple called `constraints`.
- **`Q` object:** Used within a `CheckConstraint` to construct the conditional logic for the constraint. For example, `Q(price__gt=0)` specifies that the price field must be greater than zero. Conditions use field lookup syntax.
- **`Meta` Class:** An inner class within a Django model definition used to attach metadata to the model, such as ordering information or database constraints.
- **`IntegrityError`:** The type of exception raised by Django (which wraps a database error) when an attempt is made to save data that **violates a database constraint**. This is the error to expect and test for when trying to save invalid data after constraints are applied.
- **Migrations:** Database constraints defined in the model's `Meta` class require Django migrations to be applied to the database schema. Running `makemigrations` generates the migration file based on the model changes, and `migrate` applies those changes to the database.
- **`PositiveIntegerField`:** An alternative Django model field type for integer fields that **automatically adds a check constraint** to the database to ensure the value is positive. This can be used instead of manually adding a `CheckConstraint` for positive integer requirements.
- **Testing Constraints:** It is important to add tests for database constraints to ensure they are correctly applied and enforced. Tests involve attempting to create and save model instances with data that should violate the constraint and verifying that an `IntegrityError` is raised using `assertRaises`.

## 2. Resources

- [Testing in Django Tutorial #6 - Testing Database Constraints](https://youtu.be/fP77InM74yc?si=267ZTR7uDYeteXh6)
- [Django Documentation - Validating Objects](https://docs.djangoproject.com/en/5.1/ref/models/instances/#validating-objects)
- [Project Tests](../testing-project/products/tests/test_models.py)

## 3. Practical Steps: Hands-on Guide

1.  **Demonstrate Model Validation Limitation:**

    - Open the Django shell:
      ```bash
      python manage.py shell
      ```
    - Import your model (e.g., `Product`):
      ```python
      from your_app.models import Product
      ```
    - Create a product instance with invalid data (e.g., negative price/stock):
      ```python
      product = Product(name="Test Product", price=-55, stock_count=-2)
      ```
    - Observe that calling `product.clean()` would raise a `ValidationError`:
      ```python
      product.clean() # This would raise ValidationError
      ```
    - However, calling `product.save()` _without_ `clean()` **successfully saves the invalid data** to the database:
      ```python
      product.save() # Invalid data is saved!
      ```
    - Verify by retrieving the object and checking the values:
      ```python
      p = Product.objects.first()
      print(p.price) # Output will be -55
      print(p.stock_count) # Output will be -2
      ```
    - Exit the shell: `exit()`

2.  **Define Database Constraints in Model:**

    - Edit your model definition (e.g., `Product` model).
    - Add an inner `Meta` class if you don't have one.
    - Add a `constraints` list or tuple within the `Meta` class.
    - Add `CheckConstraint` instances for the desired fields, using `Q` objects for conditions and providing a unique `name` for each. Remember to import `Q` and `CheckConstraint` from `django.db.models`.

      ```python
      # In your_app/models.py
      from django.db import models
      from django.db.models import CheckConstraint, Q # Import Q and CheckConstraint

      class Product(models.Model):
          name = models.CharField(max_length=200)
          price = models.DecimalField(max_digits=10, decimal_places=2)
          stock_count = models.IntegerField()
          # ... other fields

          class Meta:
              constraints = [
                  # Ensure price is greater than 0
                  CheckConstraint(check=Q(price__gt=0), name='price_greater_than_zero'),
                  # Ensure stock_count is greater than 0
                  CheckConstraint(check=Q(stock_count__gt=0), name='stock_count_greater_than_zero'),
              ]
      ```

      _Note: For stock_count allowing zero, change `__gt=0` to `__gte=0`_.

3.  **Generate and Apply Migrations:**

    - Run `makemigrations` to create a migration file for the constraint changes:
      ```bash
      python manage.py makemigrations
      ```
    - **Important:** If you have existing data that violates the new constraints (like the negative price saved in step 1), the `migrate` command will fail. You must **remove or update the invalid data** first.
      - Go back to the shell: `python manage.py shell`
      - Import model: `from your_app.models import Product`
      - Find and delete the invalid object(s):
        ```python
        invalid_product = Product.objects.first() # Or filter to find specific objects
        invalid_product.delete()
        ```
      - Exit shell: `exit()`
    - Run `migrate` to apply the constraints to the database:
      ```bash
      python manage.py migrate
      ```

4.  **Write Tests for Constraints:**

    - Edit your test file (e.g., `your_app/tests/test_models.py`).
    - Import `IntegrityError` from `django.db`.
      ```python
      from django.test import TestCase
      from django.db import IntegrityError # Import IntegrityError
      from your_app.models import Product
      ```
    - Define test methods within your `TestCase` class to test each constraint.
    - Use the `assertRaises` context manager, expecting `IntegrityError`, around the code that attempts to save invalid data.

      ```python
      # In your_app/tests/test_models.py

      class ProductModelTests(TestCase):
          # ... (existing test methods like test_clean_method, etc.)

          def test_negative_price_constraint(self):
              """Ensure a product with a negative price cannot be saved."""
              # Create a product instance that violates the price constraint
              product = Product(name="Invalid Price Product", price=-1.00, stock_count=10)

              # Expect an IntegrityError when attempting to save
              with self.assertRaises(IntegrityError):
                  product.save() # This should fail due to the constraint

          def test_negative_stock_count_constraint(self):
              """Ensure a product with a negative stock count cannot be saved."""
              # Create a product instance that violates the stock count constraint
              product = Product(name="Invalid Stock Product", price=5.00, stock_count=-5)

              # Expect an IntegrityError when attempting to save
              with self.assertRaises(IntegrityError):
                  product.save() # This should fail due to the constraint
      ```

5.  **Run Tests:**
    - Execute the tests from the terminal:
      ```bash
      python manage.py test
      ```
    - Verify that the new tests pass, confirming the database constraints are correctly enforcing the rules.
    - Consider adding tests for **edge cases**, such as the boundary value (e.g., `price=0` or `stock_count=0`), depending on whether your constraint uses `__gt` or `__gte`.

These steps establish both Python-level validation (`clean` method, useful with forms) and database-level constraints (`CheckConstraint`s) for robust data integrity. Testing ensures that these constraints function as expected.
