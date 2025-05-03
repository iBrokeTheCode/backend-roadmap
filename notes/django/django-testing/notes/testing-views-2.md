# Testing in Django Tutorial #9 - Testing Views (part 2)

## 1. Core Concepts

- **Django Views**: Python functions (or classes) that handle incoming web requests and return HTTP responses, often rendering data using templates.
- **Templates**: HTML files that use Django's template language to render dynamic data provided by the view.
- **Context**: A dictionary containing data passed from a Django view to a template, allowing the template to render dynamic information.
- **Django Models and ORM**: Python classes defining the structure of database tables (**models**) and Django's Object-Relational Mapper (**ORM**) for interacting with the database using Python code (e.g., `Product.objects.all()`).
- **`TestCase` vs `SimpleTestCase`**: `SimpleTestCase` is suitable for testing views that do _not_ interact with the database. `TestCase` is the appropriate base class for tests that require database access, as it sets up a test database environment.
- **`setUp` Method**: A special method within a `TestCase` class that is automatically run before _each_ individual test method in that class. It's commonly used to create necessary test data in the database.
- **Test Client**: A utility provided by Django's testing framework (`self.client`) used to simulate sending HTTP requests (like GET or POST) to Django views and get the response.
- **`reverse` Function**: A Django utility function used in tests (and elsewhere) to dynamically generate a URL path based on the **name** given to a URL pattern in `urls.py`. This makes tests less fragile if URL paths change but names remain constant.
- **Assertion Methods**: Methods provided by Django's test classes (`self.assert...`) used to check if expected conditions are met during a test. Examples include:
  - `assertTemplateUsed`: Checks if a specific template was used to render the response.
  - `assertEqual`: Checks if two values are equal, often used to verify the length or specific values within the response **context**.
  - `assertContains`: Checks if a specific piece of content (string) is present in the response's HTML content.
  - `assertNotContains`: Checks if a specific piece of content (string) is _not_ present in the response's HTML content.
- **Testing Context Data**: Examining the `response.context` attribute to ensure that the correct data (e.g., a list of products) was passed to the template as expected.
- **Testing Rendered Content**: Verifying that dynamic data from the **context** is correctly rendered in the final HTML output by checking for the presence or absence of specific strings.
- **Testing Scenarios Without Data**: Writing tests that specifically check the view's behavior and output when the database contains no relevant objects. This often involves deleting data created in the `setUp` method or running tests that don't rely on `setUp`'s data.

## 2. Resources

- [Testing in Django Tutorial #9 - Testing Views (part 2)](https://youtu.be/GOxdQLrEX5U?si=R6YF8lbqchuBI96v)
- [Testing Project](./testing-project/)

## 3. Practical Steps: Hands-on Guide

1.  **Create the Products View**: Define a new view function `products` in your `views.py`.

    ```python
    # views.py
    from .models import Product # Import your Product model
    from django.shortcuts import render

    def products(request):
        # Fetch all products from the database
        products = Product.objects.all()
        # Create a context dictionary
        context = {'products': products}
        # Render the products.html template with the context
        return render(request, 'products.html', context)
    ```

    This view fetches all objects from the `Product` model, puts them into a **context** dictionary with the key `'products'`, and passes this context to the `products.html` template for rendering.

2.  **Create the Products Template**: Create a `products.html` file in your templates directory.

    ```html
    {% extends 'base.html' %} {% block content %}
    <h1>Products</h1>
    {% for product in products %}
    <p>{{ product.name }}</p>
    {% empty %}
    <p>no products available</p>
    {% endfor %} {% endblock content %}
    ```

    This template extends a base template, iterates over the list of `products` provided in the **context**, and displays each product's name. It also includes an `{% empty %}` block to show a message if no products are found.

3.  **Add the Products URL Pattern**: Define a URL pattern for the `products` view in your project's `urls.py` or app's `urls.py`.

    ```python
    # urls.py
    from django.urls import path
    from . import views # Import your views

    urlpatterns = [
        # ... other urls
        path('products/', views.products, name='products'), # Map /products to the view and name it 'products'
    ]
    ```

    This maps the `/products/` URL path to the `products` view and gives it the name `'products'`, which is useful for reversing URLs in tests.

4.  **Create the Test Class for Products View**: In your `test_views.py`, create a test class that inherits from `django.test.TestCase` because this view interacts with the database.

    ```python
    # test_views.py
    from django.test import TestCase, SimpleTestCase # SimpleTestCase if needed for other tests
    from django.urls import reverse # Import reverse function
    from .models import Product # Import your Product model

    class TestProductsPage(TestCase): # Inherit from TestCase for database access
        # setup method runs before each test method
        def setUp(self):
            # Create test data in the database
            Product.objects.create(name='Laptop', price=1000, stock=5) # Add stock as needed based on model constraints
            Product.objects.create(name='Phone', price=800, stock=10)
    ```

    The `setUp` method creates two `Product` objects before every test in this class, providing data for testing.

5.  **Write Test for Correct Template Usage**: Add a test method to check if the correct template is used for the products page.

    ```python
    # Inside TestProductsPage class
    def test_products_uses_correct_template(self):
        # Use reverse to get the URL for the 'products' name
        url = reverse('products')
        # Send a GET request using the test client
        response = self.client.get(url)
        # Assert that 'products.html' was used to render the response
        self.assertTemplateUsed(response, 'products.html')
    ```

6.  **Write Test for Context Data and Content (with products)**: Add a test method to verify the data in the **context** and the rendered content when products are present.

    ```python
    # Inside TestProductsPage class
    def test_products_context(self):
        # The setup method created two products before this test runs

        # Send a GET request to the products URL
        url = reverse('products')
        response = self.client.get(url)

        # Assert that the 'products' key exists in the context and its length is 2
        self.assertEqual(len(response.context['products']), 2)

        # Assert that the names of the products are present in the response content
        self.assertContains(response, 'Laptop')
        self.assertContains(response, 'Phone')

        # Assert that the "no products available" message is NOT present
        self.assertNotContains(response, 'no products available')
    ```

7.  **Write Test for Context Data and Content (no products)**: Add a test method to check the view's behavior when no products are in the database.

    ```python
    # Inside TestProductsPage class
    def test_products_view_no_products(self):
        # Delete all products created by the setup method (or any others)
        Product.objects.all().delete()

        # Send a GET request to the products URL
        url = reverse('products')
        response = self.client.get(url)

        # Assert that the 'products' list in the context is empty
        self.assertEqual(len(response.context['products']), 0)

        # Assert that the "no products available" message IS present in the response content
        self.assertContains(response, 'no products available')
    ```

8.  **Run the Tests**: Execute the tests from your terminal.
    ```bash
    python manage.py test
    ```
    This command runs all tests in your Django project. You should see output indicating how many tests ran and if they passed or failed.
