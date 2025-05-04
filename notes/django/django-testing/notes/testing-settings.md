# Test Settings

## 1. Core Concepts

- **Django Settings**: Configuration values that control the behavior of your Django application. Examples include enabling **maintenance mode** or defining **authentication backends**. Application behavior often depends on these settings.
- **Dynamically Changing Settings for Tests**: The ability to alter setting values specifically for the duration of a test to test different scenarios. This prevents global setting changes in `settings.py` from breaking unrelated tests.
- **Django Middleware**: A framework providing hooks into Django's request and response processing pipeline. It acts as a light, low-level plugin system to globally alter Django's input and output. Middleware is processed sequentially from top to bottom in the `MIDDLEWARE` list. It can perform actions before or after the view function is called, or even return a response early.
- **`override_settings` Decorator**: A decorator from `django.test` used to **dynamically change a specific setting** for the duration of a test method or an entire test class. It takes the setting name and the desired value as arguments, for example, `@override_settings(SETTING_NAME=Value)`. This is a very handy decorator when the functionality being tested depends on a setting.
- **Dedicated Test Settings File**: A common practice is to create a separate Python file (e.g., **`test_settings.py`**) that imports the default settings (`from your_project.settings import *`) and then overrides specific settings suitable for testing, such as setting `MAINTENANCE_MODE` to `False`. This allows running the test suite with a consistent baseline configuration.

## 2. Resources

- [Testing in Django Tutorial #14 - Test Settings](https://youtu.be/3tHHTnLqZfA?si=PPYURSKgAr59TaL7)
- [Django Documentation - Middleware](https://docs.djangoproject.com/en/5.1/topics/http/middleware/)
- [Project Tests](../testing-project/products/tests/test_middleware.py)

## 3. Practical Steps: Hands-on Guide

1.  **Create Middleware**:

    - In your Django application (e.g., `products`), create a new file named `middleware.py`.
    - Define a class `MaintenanceModeMiddleware` that checks a **`MAINTENANCE_MODE`** setting.
    - Implement the `__init__` method to store the `get_response` callable.
    - Implement the `__call__` method to get the `MAINTENANCE_MODE` setting value (defaulting to `False` if not defined).
    - If **`MAINTENANCE_MODE`** is `True`, return an `HttpResponse` with "site under maintenance" and a status code of 503.
    - If **`MAINTENANCE_MODE`** is `False`, call `self.get_response(request)` to continue processing the request.

    ```python
    # products/middleware.py (example logic based on description)
    from django.conf import settings
    from django.http import HttpResponse

    class MaintenanceModeMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            # Get MAINTENANCE_MODE setting, default to False
            maintenance_mode = getattr(settings, 'MAINTENANCE_MODE', False)

            if maintenance_mode:
                return HttpResponse('site under maintenance', status=503)
            else:
                return self.get_response(request)
    ```

2.  **Add Middleware to Settings**:

    - Open your project's `settings.py` file.
    - Add the fully qualified path to your new middleware class to the `MIDDLEWARE` list.
    - Place it near the top of the list so it can return a response early when maintenance mode is on.

    ```python
    # your_project/settings.py
    MIDDLEWARE = [
        # ... other middleware ...
        'products.middleware.MaintenanceModeMiddleware', # Add your middleware here
        # ... rest of middleware ...
    ]
    ```

3.  **Define the Maintenance Mode Setting**:

    - In your project's `settings.py`, add a setting for **`MAINTENANCE_MODE`**.
    - Initially set it to `True` for manual testing.

    ```python
    # your_project/settings.py
    # ...
    MAINTENANCE_MODE = True # Or False
    ```

4.  **Manual Testing**:

    - Run the development server:
      ```bash
      python manage.py runserver
      ```
    - Visit the application's homepage in a browser. If **`MAINTENANCE_MODE`** is `True` in `settings.py`, you should see the "site under maintenance" message. If `False`, you should see the normal homepage content.

5.  **Prepare for Test Writing**:

    - Ensure your homepage URL pattern has a `name` defined (e.g., `name='home'`) in `urls.py` for use with `reverse`.

    ```python
    # your_project/urls.py (example)
    from django.urls import path
    from . import views # Assuming a view for the homepage

    urlpatterns = [
        path('', views.home, name='home'), # Add name='home'
        # ... other urls ...
    ]
    ```

    - In your application's `tests` directory, create a file named `test_middleware.py`.
    - Import necessary testing tools:

    ```python
    # products/tests/test_middleware.py
    from django.test import TestCase, override_settings
    from django.urls import reverse
    # No need to import middleware directly for this test
    ```

    - Define a test class inheriting from **`TestCase`**.

    ```python
    # products/tests/test_middleware.py
    from django.test import TestCase, Client, override_settings
    from django.urls import reverse

    class MaintenanceModeTests(TestCase):
        # Tests will go here
        pass
    ```

6.  **Write Test for Maintenance Mode Off**:

    - Define a test method `test_maintenance_mode_off` within the test class.
    - Use the **`@override_settings(MAINTENANCE_MODE=False)`** decorator above this method to ensure **`MAINTENANCE_MODE`** is `False` for this specific test, regardless of the value in `settings.py`.
    - Use the Django test client (`self.client`) to simulate a GET request to the homepage using `reverse('home')`.
    - Assert that the response contains the expected normal homepage content ("welcome to the store") and has a status code of 200. The `assertContains` method can check content and status code.

    ```python
    # products/tests/test_middleware.py
    # ... imports and MaintenanceModeTests class definition ...

    class MaintenanceModeTests(TestCase):
        @override_settings(MAINTENANCE_MODE=False) # Override for this test
        def test_maintenance_mode_off(self):
            # Simulate a request
            response = self.client.get(reverse('home'))

            # Check the response is successful and normal content is returned
            self.assertContains(response, "welcome to the store", status_code=200)
    ```

7.  **Run the Test File (Initial)**:

    - Run the test command targeting only this specific file:
      ```bash
      python manage.py test products.tests.test_middleware
      ```
    - This test should pass because you used the `@override_settings` decorator to force **`MAINTENANCE_MODE`** to `False` for this test. If you commented out the decorator and ran the test while `MAINTENANCE_MODE = True` in `settings.py`, the test would fail.

8.  **Write Test for Maintenance Mode On**:

    - Define another test method, `test_maintenance_mode_on`, within the test class.
    - Use the **`@override_settings(MAINTENANCE_MODE=True)`** decorator above this method.
    - Simulate the same GET request to the homepage.
    - Assert that the response contains the maintenance message ("site is under maintenance") and has a status code of 503.

    ```python
    # products/tests/test_middleware.py
    # ... previous test method ...

    class MaintenanceModeTests(TestCase):
        # ... test_maintenance_mode_off method ...

        @override_settings(MAINTENANCE_MODE=True) # Override for this test
        def test_maintenance_mode_on(self):
            # Simulate the same request
            response = self.client.get(reverse('home'))

            # Check the response is the maintenance message and status 503
            self.assertContains(response, "site is under maintenance", status_code=503)
    ```

9.  **Run the Test File (Both Tests)**:

    - Rerun the test command targeting the file:
      ```bash
      python manage.py test products.tests.test_middleware
      ```
    - Both tests should now pass, demonstrating how `@override_settings` allows testing different scenarios controlled by settings.

10. **Address Full Test Suite Failures**:

    - If you set **`MAINTENANCE_MODE = True`** in `settings.py` and run the full test suite (`python manage.py test`), many tests will likely fail because the middleware will return a 503 response instead of allowing views to process.

11. **Option 1 (Less Preferred) - Apply Decorator to Class**:

    - The **`@override_settings`** decorator can be applied to an entire test class. This would set the specified setting for every test method within that class.
    - While possible, this approach would require decorating many test classes if the global setting impacts multiple parts of the application being tested.

12. **Option 2 (Preferred) - Create Dedicated Test Settings**:

    - In your project's root directory, create a new file named **`test_settings.py`**.
    - Import all default settings from your main `settings.py` file.
    - Override the **`MAINTENANCE_MODE`** setting in **`test_settings.py`** to `False`. You can override other settings here too (e.g., email backend).

    ```python
    # your_project/test_settings.py
    from your_project.settings import * # Import all default settings

    # Override settings specifically for testing
    MAINTENANCE_MODE = False
    # EMAIL_BACKEND = '...' # Example of another override
    ```

13. **Run Tests with Dedicated Settings File**:

    - Run the full test suite using the **`--settings`** flag to specify the dedicated test settings file.

    ```bash
    python manage.py test --settings your_project.test_settings
    ```

    - This approach ensures that for all tests, the **`MAINTENANCE_MODE`** setting defaults to `False` (as defined in **`test_settings.py`**), fixing the widespread failures. You can still use `@override_settings` on individual test methods or classes if you need to test scenarios where a setting is temporarily changed (like testing the middleware itself in steps 6 & 8).
