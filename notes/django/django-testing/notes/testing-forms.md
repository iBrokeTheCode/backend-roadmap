# Testing in Django Tutorial #10 - Testing Forms

## 1. Core Concepts

- **Django Model Form**: A class that builds a form directly from a Django model. It simplifies the process of creating forms that interact with model instances.
- **Nested `Meta` Class**: An inner class within a `ModelForm` that defines configuration options, such as specifying the **model** the form is tied to and the specific **fields** to include on the form.
- **Field-level Validation**: Custom validation logic applied to individual fields within a form. This is implemented using methods prefixed with `clean_` followed by the field name (e.g., `clean_price`). These methods retrieve data using `self.cleaned_data` and can raise a `ValidationError` if the data is invalid.
- **Request Handling (GET vs. POST)**: Django views can check the HTTP method of an incoming request using `request.method`. **GET requests** are typically used to display a page or an empty form, while **POST requests** are used to submit data, often from a form.
- **Form Instantiation and Validation**: When a POST request containing form data is received, the form class is **instantiated** with the posted data (`ProductForm(request.POST)`). Calling `form.is_valid()` runs the validation logic defined in the form; it returns `True` if all data is valid and `False` otherwise.
- **Saving Model Forms**: For valid **Model Forms**, calling `form.save()` automatically takes the cleaned data and saves it to the associated database model.
- **Django Redirect**: After successfully processing a form submission (e.g., saving data), a **redirect** is often used to send the user to another page, preventing form resubmission issues. This is done using the `redirect` helper function. A redirect response typically has a **status code** of **302**.
- **Form in Context**: If a form submission is invalid, the view typically adds the **populated form instance** (containing submitted data and error messages) to the template context. This allows the template to re-render the form with the user's input and display the validation errors.
- **Rendering Forms in Templates**: In Django templates, a form object passed in the context can be easily rendered. Using `{{ form.as_div }}` (or similar `as_p`, `as_ul`) renders the form fields wrapped in HTML tags (e.g., `div`).
- **CSRF Token**: For security, POST requests in Django forms require a **Cross-Site Request Forgery (CSRF)** token (`{% csrf_token %}`) to be included in the form.
- **Django Test Case**: Tests for Django applications are often written as methods within a class that inherits from `django.test.TestCase`. This provides utility methods for testing web applications and ensures tests run in isolated database transactions.
- **Django Test Client**: `self.client` in a test case provides a way to simulate HTTP requests (GET, POST, etc.) to your Django application programmatically.
- **Testing POST Requests**: `self.client.post(url, data)` simulates submitting data via a POST request to a specified URL.
- **Assertions in Tests**: Test methods use assertion functions (e.g., `self.assertEqual`, `self.assertTrue`, `self.assertFalse`, `self.assertFormError`) to check if the actual outcome matches the expected outcome.
- **`self.assertFormError`**: A specific Django test assertion used to verify that a particular field on a form object has a specific validation error message.
- **Test Isolation**: Each test method within a `TestCase` typically runs in isolation, often within its own database transaction that is rolled back at the end of the test, ensuring tests don't interfere with each other.

## 2. Resources

- [Testing in Django Tutorial #10 - Testing Forms](https://youtu.be/RR7wANxu5gk?si=MYDJxoS2kA1fMEOI)
- [Testing Project](./testing-project/)

## 3. Practical Steps: Hands-on Guide

1.  **Create the Product Form (`forms.py`)**:

    - Import necessary modules: `forms` from `django`, your `Product` model.
    - Create a class `ProductForm` inheriting from `forms.ModelForm`.
    - Define a nested `Meta` class specifying the `model = Product` and `fields = ('name', 'price', 'stock_count')`.
    - Add custom field-level validation methods:
      - `clean_price(self)`: Get price from `self.cleaned_data`. If price is less than 0, raise `ValidationError("Price cannot be negative")`. Otherwise, return the price.
      - `clean_stock_count(self)`: Get stock count from `self.cleaned_data`. If stock count is less than 0, raise `ValidationError("Stock count cannot be negative")`. Otherwise, return the stock count.

    ```python
    from django import forms
    from .models import Product # Assuming Product is in a models.py in the same app
    from django.core.exceptions import ValidationError

    class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = ('name', 'price', 'stock_count')

        def clean_price(self):
            price = self.cleaned_data['price']
            if price < 0:
                raise ValidationError("Price cannot be negative")
            return price

        def clean_stock_count(self):
            stock_count = self.cleaned_data['stock_count']
            if stock_count < 0:
                raise ValidationError("Stock count cannot be negative")
            return stock_count
    ```

2.  **Update the View to Handle Form Submission (`views.py`)**:

    - Import `ProductForm` and `redirect`.
    - In your view function (e.g., `products` view):
      - Check `if request.method == 'POST'`:
        - Instantiate the form with POST data: `form = ProductForm(request.POST)`.
        - Check if the form is valid: `if form.is_valid():`.
          - Save the form data: `form.save()`.
          - Redirect: `return redirect('products')` (assuming 'products' is the URL name).
        - If `form.is_valid()` is `False` (the `else` block):
          - Prepare context including products and the populated form: `context = {'products': Product.objects.all(), 'form': form}`.
          - Render the template with the context: `return render(request, 'products/products.html', context)`.
      - If `request.method == 'GET'` (or any other method):
        - Instantiate an empty form: `form = ProductForm()`.
        - Prepare context including products and the empty form: `context = {'products': Product.objects.all(), 'form': form}`.
        - Render the template with the context: `return render(request, 'products/products.html', context)`.

    ```python
    from django.shortcuts import render, redirect
    from .models import Product # Assuming Product is in a models.py in the same app
    from .forms import ProductForm # Import the form

    def products_view(request): # Adjust function name as needed
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('products') # Replace 'products' with your actual URL name
            else:
                # Form is invalid, render page with errors
                products = Product.objects.all()
                context = {'products': products, 'form': form}
                return render(request, 'products/products.html', context)
        else: # GET request
            form = ProductForm()
            products = Product.objects.all()
            context = {'products': products, 'form': form}
            return render(request, 'products/products.html', context)
    ```

3.  **Update the Template to Display the Form (`products.html`)**:

    - Add a `<form>` tag with `method="post"`.
    - Include the CSRF token: `{% csrf_token %}`.
    - Render the form fields (e.g., as divs): `{{ form.as_div }}`.
    - Add a submit button: `<button type="submit">Submit</button>`.

    ```html+django
    <h1>Products</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_div }} {# Renders form fields within div tags #}
        <button type="submit">Add Product</button>
    </form>

    <hr> {# Optional separator #}

    {# Loop through and display products as before #}
    {% for product in products %}
        <p>{{ product.name }}</p>
    {% endfor %}
    ```

4.  **Refactor Model Validation (Optional but shown)**:

    - If you had validation logic (like price < 0 check) in your `Product` model's `clean` method, remove it after moving it to the form.

5.  **Update Model Tests (if applicable)**:

    - If you had tests specifically for the model's `clean` method validation, remove or update them as the validation is now handled by the form.

6.  **Create Form Tests (`test_forms.py`)**:

    - Create a new file `test_forms.py` in your app's `tests` directory.
    - Import `TestCase` from `django.test`, `reverse` from `django.urls`, and your `Product` model.
    - Create a test class `ProductFormTest` inheriting from `TestCase`.

    ```python
    from django.test import TestCase, Client
    from django.urls import reverse
    from .models import Product # Assuming Product model is defined

    class ProductFormTest(TestCase):
        pass # Test methods will go here
    ```

7.  **Write Test for Valid Form Submission**:

    - Add a method (e.g., `test_create_product_when_valid`) to `ProductFormTest`.
    - Define a dictionary `form_data` with valid data (e.g., `{'name': 'Tablet', 'price': 299.99, 'stock_count': 50}`).
    - Simulate a POST request using `self.client.post()` to the products URL, passing the `form_data` using the `data` keyword argument. Get the `response` object.
    - Assert that the response status code is 302 (redirect) using `self.assertEqual(response.status_code, 302)`.
    - Assert that a product with the submitted name exists in the database using `self.assertTrue(Product.objects.filter(name='Tablet').exists())`.

    ```python
    # Inside ProductFormTest class
    def test_create_product_when_valid(self):
        form_data = {'name': 'Tablet', 'price': 299.99, 'stock_count': 50}
        # Assuming your products view is mapped to a URL name 'products'
        response = self.client.post(reverse('products'), data=form_data)

        # Assert redirect status code
        self.assertEqual(response.status_code, 302)

        # Assert that the product was created in the database
        self.assertTrue(Product.objects.filter(name='Tablet').exists())
    ```

8.  **Write Test for Invalid Form Submission**:

    - Add a method (e.g., `test_don't_create_product_when_invalid`) to `ProductFormTest`.
    - Define a dictionary `form_data` with invalid data (e.g., missing name, negative price, negative stock count).
    - Simulate a POST request using `self.client.post()` to the products URL, passing the `form_data`. Get the `response` object.
    - Assert that the response status code is 200 (staying on the page to show errors) using `self.assertEqual(response.status_code, 200)`.
    - Assert that the form is present in the response context using `self.assertTrue('form' in response.context)`.
    - Get the form instance from the context: `form = response.context['form']`.
    - Use `self.assertFormError` to check for specific errors on specific fields:
      - `self.assertFormError(form, 'name', 'This field is required.')` (or similar required error message)
      - `self.assertFormError(form, 'price', 'Price cannot be negative')`
      - `self.assertFormError(form, 'stock_count', 'Stock count cannot be negative')`
    - Assert that no new product was created in the database using `self.assertFalse(Product.objects.exists())`. This relies on test isolation ensuring no products exist before this test runs.

    ```python
    # Inside ProductFormTest class
    def test_dont_create_product_when_invalid(self):
        # Invalid data: missing name, negative price, negative stock
        form_data = {'name': '', 'price': -10.00, 'stock_count': -5}
         # Assuming your products view is mapped to a URL name 'products'
        response = self.client.post(reverse('products'), data=form_data)

        # Assert status code 200 (stay on page)
        self.assertEqual(response.status_code, 200)

        # Assert that the form is in the context
        self.assertTrue('form' in response.context)

        # Get the form from the context
        form = response.context['form']

        # Assert specific form errors
        self.assertFormError(form, 'name', 'This field is required.') # Check error for required field
        self.assertFormError(form, 'price', 'Price cannot be negative') # Check custom price error
        self.assertFormError(form, 'stock_count', 'Stock count cannot be negative') # Check custom stock error

        # Assert that no product was created in the database
        self.assertFalse(Product.objects.exists())
    ```

9.  **Run the Tests**:
    - Open your terminal in the project root.
    - Run all tests: `python manage.py test`.
    - Run tests for a specific app: `python manage.py test your_app_name`.
    - Run tests for a specific module (like your forms tests): `python manage.py test your_app_name.tests.test_forms`.
    - Verify that all tests pass.
