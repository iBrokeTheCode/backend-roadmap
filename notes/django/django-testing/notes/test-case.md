# TestCase

## 1. Core Concepts

- **`TestCase` Class**: The most frequently used class for writing tests in Django applications. It inherits from `TransactionTestCase`. A key feature is that it wraps tests in **two nested atomic blocks**. There's an outer atomic transaction for the **entire class**, and an inner atomic transaction for **each test method**. This means each test method runs within its own transaction that is rolled back at the end, but there's also a transaction encompassing all tests in the class.
- **Atomic Transactions**: `TestCase` uses these to ensure test isolation. Changes made within a test method are typically rolled back at the end of that test method's transaction. The class-level transaction enables features like `setup_test_data`.
- **`setUp` Method**: A standard method in `unittest.TestCase` (which Django's `TestCase` builds upon) that is run **at the start of each individual test method** within a test class. If you create data here, it will be created repeatedly for every single test.
- **`setUpTestData` Method**: A specialized **class method** available on Django's `TestCase`. It is decorated with `@classmethod`. This method is run **only once** for the entire test case class, before any test methods are executed. It leverages the class-level atomic block. It's designed for creating initial data that can be shared across all test methods in the class without being modified by them.
- **Performance Optimization**: Using `setUpTestData` to create test data that doesn't change across tests provides a significant performance benefit, especially when creating numerous database objects. Instead of creating, saving, and rolling back objects hundreds or thousands of times (once per test method using `setUp`), they are created only once per class.

## 2. Resources

- [Testing in Django Tutorial #7 - TestCase](https://youtu.be/hKjJmvksaJ8?si=TSDFJQfcRdaXeiCb)
- [Django Documentation - TestCase](https://docs.djangoproject.com/en/5.1/topics/testing/tools/#testcase)
- [Project Tests](../testing-project/products/tests/)

## 3. Practical Steps: Hands-on Guide

Here's how to move database object setup from the `setUp` method to the performance-optimized `setUpTestData` method in a Django `TestCase`:

1.  **Identify Setup Code**: Locate the code within your `TestCase`'s `setUp` method that creates objects (especially database objects) needed for your tests. For example, creating a `Product` instance.
2.  **Create `setUpTestData` Method**: Add a new method named `setUpTestData` to your `TestCase` class.
3.  **Add `@classmethod` Decorator**: Immediately above the `setUpTestData` method definition, add the `@classmethod` decorator.
    ```python
    @classmethod
    def setUpTestData(cls):
        # ... setup code here ...
    ```
    The decorator signifies that it's a class method, taking the class itself (conventionally named `cls` or `class`) as the first argument instead of the instance (`self`).
4.  **Move Setup Logic**: Copy the relevant object creation code from the original `setUp` method into the new `setUpTestData` method.
5.  **Update Object References**: Inside `setup_test_data`, change any references to instance attributes (which would typically use `self.`) to use the class argument (`cls.`) instead. For example, `self.product = ...` becomes `cls.product = ...`.

    ```python
    @classmethod
    def setUpTestData(cls):
        print("setting up test data once for the class")
        # Example: Create a product and attach it to the class
        cls.product = Product.objects.create(
            name="A Product",
            price=100.00,
            in_stock=True
        )
    ```

6.  **Keep or Adjust `setUp`**: You might keep the original `setUp` method if it performs other instance-specific setup, but the data creation part is now handled by `setUpTestData`. If `setup` is only used for data creation, you might remove or empty it.
7.  **Run Tests**: Execute your tests using the Django test command.
    ```bash
    python manage.py test
    ```
8.  **Verify**: Confirm that all tests still pass. You can optionally add print statements (like the example above) to observe that `setUpTestData` runs only once per class, while `setUp` runs before each test method.

This refactoring ensures that the test data object (`cls.product` in the example) is created only once per test class, providing performance gains, especially in large test suites. Remember that this is suitable for data that is _not_ modified by the test methods.
