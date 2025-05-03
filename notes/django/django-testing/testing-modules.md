# Testing in Django Tutorial #5 - Testing Modules

## 1. Core Concepts

### Django Models

Django **model classes** map to database tables under the hood and often contain **business logic** and **validation rules**. Testing these custom additions to models is crucial within the application's context.

### Extending the Built-in User Model

The tutorial shows how to create a custom **User model** by overriding the built-in abstract user model. This involves importing **`AbstractUser`** and creating a subclass, allowing for the addition of properties and methods. The **`AUTH_USER_MODEL`** Django setting must be pointed to this new user model to tell Django which model to use as the user model in the application.

### Model Fields

Models are defined with **fields** like **`CharField`**, **`DecimalField`**, and **`IntegerField`** which map to database columns. These fields can have parameters like `max_length` for `CharField` or `max_digits` and `decimal_places` for `DecimalField`. Default values can also be set for fields.

### Model Validation (`clean` method)

The **`clean`** method can be defined on a model to perform **validation** on data before saving. Within this method, custom checks can be implemented, and a **`ValidationError`** can be raised if data fails validation. This method is where logic for checking constraints like negative price or stock count is placed. The `ValidationError` is imported from `django.core.exceptions`.

### Model Properties (`@property` decorator)

Custom logic that acts like an attribute can be defined using the **`@property`** decorator on a function within the model class. This decorated method takes `self` as a parameter and allows external code to access its result by accessing `.` followed by the property name, rather than calling it as a function. The tutorial uses this for an **`in_stock`** property based on the stock count.

### Model Methods

Models can have custom **methods** defined to encapsulate specific **business logic**. These methods can take arguments beyond `self`. The example demonstrates a **`get_discounted_price`** method that calculates a new price based on a discount percentage.

### Django's Test Case

Tests for models are written in files like `test_models.py`. Test classes are created as subclasses of **`django.test.TestCase`**. This class provides methods for writing various assertions and manages the test database lifecycle. `TestCase` extends Python's `unittest` package.

### Test Database Isolation

When running tests with `python manage.py test`, Django creates a separate **test database** at the start of the test run and destroys it at the end. This ensures **isolation** of tests, meaning tests do not affect the main development database or each other.

### Setting up Tests

Tests are typically placed in a **`tests`** directory within the app, often with an `__init__.py` file to treat it as a package. Specific test files like `test_models.py` are created to organize tests by component. Essential imports for model tests include the model itself, `TestCase`, and `ValidationError` (if testing validation).

### `setUp` Method

A **`setUp`** method can be defined within a test class to run code before each test method. This is useful for creating objects or setting up data that will be used across multiple test cases, allowing code to be shared.

### Assertion Methods

Django's `TestCase` (from `unittest`) provides various **assertion methods** to check if certain conditions are met. Examples include:

- **`assertTrue(condition)`**: Asserts that a condition is true.
- **`assertFalse(condition)`**: Asserts that a condition is false.
- **`assertEqual(a, b)`**: Asserts that `a` equals `b`.
- **`assertRaises(exception, callable, \*args, **kwargs)`**: Asserts that a specific `exception`is raised when`callable`is called with given arguments. This is used with a context manager in a`with` block.

### Running Tests

Tests are executed using the command **`python manage.py test`** from the terminal. The output indicates the number of tests run, whether they passed or failed, and provides details on failures.

### What to Test

When testing Django models, the focus should be on custom **business logic**, **validation rules**, model **properties**, and model **methods**. Built-in functionality of Django fields is already well-tested and doesn't need redundant testing. Testing includes checking expected return values, edge cases (like zero values), and ensuring correct exceptions are raised for invalid input.

## 2. Resources

- [Testing in Django Tutorial #5 - Testing Modules](https://youtu.be/duYxizXokZM?si=DyR3O_J-fqgXKxEJ)
- [Django Documentation](https://docs.djangoproject.com/en/5.1/internals/contributing/writing-code/unit-tests/)
- [Testing Project](./testing-project/)

## 3. Practical Steps: Hands-on Guide

1.  **Define Custom Django Models**:

    - Create a custom **`User`** model extending Django's built-in **`AbstractUser`** in your `models.py` file.
    - Define a **`Product`** model inheriting from `models.Model`.
    - Add fields to the `Product` model:
      - `name = models.CharField(max_length=128)`
      - `price = models.DecimalField(max_digits=10, decimal_places=2)`
      - `stock_count = models.IntegerField(default=0)`

    ```python
    # In your app's models.py
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    from django.core.exceptions import ValidationError

    class User(AbstractUser):
        # Add custom fields here if needed
        pass

    class Product(models.Model):
        name = models.CharField(max_length=128)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        stock_count = models.IntegerField(default=0)

        def clean(self):
            if self.price < 0:
                raise ValidationError("Price cannot be negative")
            if self.stock_count < 0:
                raise ValidationError("Stock count cannot be negative")

        @property
        def in_stock(self):
            return self.stock_count > 0

        def get_discounted_price(self, discount_percentage):
            return self.price * (1 - discount_percentage / 100)

    ```

    - Implement **validation logic** using the **`clean`** method to check that `price` and `stock_count` are not negative, raising a **`ValidationError`** if they are.
    - Define a **model property** (e.g., **`in_stock`**) using the **`@property`** decorator to return a boolean indicating if stock is greater than zero.
    - Define a **model method** (e.g., **`get_discounted_price`**) to calculate a price after a given discount percentage.

2.  **Configure AUTH_USER_MODEL**:

    - Go to your project's `settings.py` file.
    - Add or modify the **`AUTH_USER_MODEL`** setting to point to your custom User model (e.g., `'products.User'`).

    ```python
    # In your project's settings.py
    AUTH_USER_MODEL = 'products.User'
    ```

3.  **Run Migrations**:

    - Open your terminal or command prompt.
    - Navigate to your project's root directory.
    - Run **`python manage.py make migrations`** to create migration files for your new models.
    - Run **`python manage.py migrate`** to apply the migrations and create the database tables. This will also create the test database when tests are run.

    ```bash
    python manage.py make migrations
    python manage.py migrate
    ```

4.  **Set up the Test Directory**:

    - Within your Django app directory (e.g., `products`), create a new folder named **`tests`**.
    - Delete the default `tests.py` file in the app directory if it exists.
    - Inside the `tests` folder, create an empty file named **`__init__.py`**. This makes the `tests` directory a Python package.
    - Inside the `tests` folder, create a file named **`test_models.py`**. This is where you will write your model tests.

5.  **Write Model Tests**:

    - In `test_models.py`, import necessary classes: **`TestCase`** from `django.test`, **`ValidationError`** from `django.core.exceptions`, and your model (**`Product`**) from your app's models.
    - Create a test class that inherits from **`TestCase`** (e.g., **`ProductModelTest`**).
    - Define a **`setUp`** method within the class to create a **`Product`** instance that can be accessed by all test methods using `self.product`.

    ```python
    # In your app's tests/test_models.py
    from django.test import TestCase
    from django.core.exceptions import ValidationError
    from products.models import Product # Adjust import path if needed

    class ProductModelTest(TestCase):

        def setUp(self):
            self.product = Product.objects.create(
                name="Test Product",
                price=100.00,
                stock_count=10
            )
    ```

    - Write test methods (starting with `test_`) for each piece of functionality you want to verify.
    - **Test the `@property`**: Use **`assertTrue`** and **`assertFalse`** to check the **`in_stock`** property under different stock counts.

    ```python
        def test_in_stock_property(self):
            # Test when stock > 0
            self.assertTrue(self.product.in_stock) # stock_count is 10 in setUp

            # Test when stock == 0
            self.product.stock_count = 0
            self.assertFalse(self.product.in_stock)
    ```

    - **Test the model method**: Use **`assertEqual`** to check if **`get_discounted_price`** returns the correct value for different discount percentages, including edge cases like 0%.

    ```python
        def test_get_discounted_price(self):
            # Test 10% discount
            self.assertEqual(self.product.get_discounted_price(10), 90.00)

            # Test 50% discount
            self.assertEqual(self.product.get_discounted_price(50), 50.00)

            # Test 0% discount (edge case)
            self.assertEqual(self.product.get_discounted_price(0), 100.00)
    ```

    - **Test validation logic**: Use the **`assertRaises`** context manager to check that calling the **`clean`** method raises a **`ValidationError`** when `price` or `stock_count` is negative.

    ```python
        def test_negative_price_validation(self):
            self.product.price = -10.00
            with self.assertRaises(ValidationError):
                self.product.clean()

        def test_negative_stock_count_validation(self):
            self.product.stock_count = -10
            with self.assertRaises(ValidationError):
                self.product.clean()
    ```

6.  **Run Your Tests**:

    - Open your terminal or command prompt.
    - Navigate to your project's root directory.
    - Run the command **`python manage.py test`**.
    - Observe the output to see if tests pass (`OK`) or fail.

    ```bash
    python manage.py test
    ```
