# Testing in Django Tutorial #12 - Mocking External Services

## 1. Core Concepts

- **Mocking:** The process of replacing parts of your **system under test** with controlled objects (mocks) that simulate the behavior of the real dependencies. This allows tests to focus on the logic being tested without relying on external systems.
- **External Services:** Third-party systems or resources that your application interacts with, such as APIs (e.g., JSON Placeholder), email services, message queues, or databases.
- **Why Mock External Services?:**
  - **Speed:** Avoids slow operations like HTTP requests or database calls during tests.
  - **Reliability:** Prevents tests from failing due to external service downtime or network issues.
  - **Control:** Allows testers to simulate specific responses and conditions (success, failure, errors) from the external service, which can be difficult to trigger reliably with the actual service.
  - **Isolation:** Ensures tests are independent of external factors.
- **`unittest.mock`:** A library included in the Python standard library that provides tools for mocking.
- **`Mock` Class:** The core class in `unittest.mock` used to create mock objects. Mock objects can replace other objects in your system, and you can then make **assertions** about how they were used (which methods/attributes were accessed, with what arguments). You can also set **return values** for mock methods or define attributes.
- **`patch` Decorator:** A convenient way provided by `unittest.mock` to replace objects within the scope of a test function or class. It takes a **target** (e.g., a function or attribute to be replaced) and replaces it with a mock object (or a specified new object) during the test's execution.
- **MagicMock:** The default type of mock object used by `patch` when replacing synchronous functions or objects (unless a `new` object is explicitly provided).
- **Target for Patching:** When using `patch`, the target string should be the path to where the object is _used_, not where it is defined. For example, if `requests.get` is called in `products.views`, the target is `"products.views.requests.get"`.
- **`return_value`:** An attribute on a mock object or a mocked method that allows you to specify what the mock should return when it is called.
- **`side_effect`:** An attribute on a mock object or a mocked method that allows you to configure the mock to raise an exception or execute a sequence of actions when called. This is useful for simulating errors or specific behaviors.
- **Assertions on Mocks:** Mock objects have built-in assertion methods to check if they were called and how they were called. Examples include **`assert_called_once_with(...)`**, which verifies that the mock object was called exactly once with specific arguments.

## 2. Resources

- [Testing in Django Tutorial #12 - Mocking External Services](https://youtu.be/Za1EBzZ0CfQ?si=vXVGyliTTZ4y1_F8)
- [Unittest Documentation - Mock](https://docs.python.org/3/library/unittest.mock.html)
- [Unittest Documentation - The patchers](https://docs.python.org/3/library/unittest.mock.html#the-patchers)
- [Testing Project](./testing-project/)

## 3. Practical Steps: Hands-on Guide

1.  **Install the `requests` module:**
    Use pip to install the library needed to make HTTP requests.

    ```bash
    pip install requests
    ```

2.  **Create a Django View using `requests`:**
    Write a view function (e.g., `post`) that makes an external HTTP GET request using `requests.get` and returns a `JsonResponse` or an `HttpResponse` on failure.

    ```python
    # views.py
    import requests
    from django.http import JsonResponse, HttpResponse
    from requests.exceptions import RequestException

    # ... other imports

    def post(request):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        try:
            response = requests.get(url) # This is the call to be mocked
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            data = response.json() # Convert response data to Python dictionary
            return JsonResponse(data) # Return JSON response
        except RequestException as e: # Capture requests exceptions
            # Typically log error here
            return HttpResponse("Service unavailable", status=503) # Return 503 on error

    ```

3.  **Register the View in `urls.py`:**
    Add a URL pattern to route requests to the new view.

    ```python
    # urls.py
    from django.urls import path
    from . import views # Assuming views are in the same app

    urlpatterns = [
        # ... other urls
        path('post/', views.post, name='post'),
    ]
    ```

4.  **Create a Test File and Class:**
    Create or open a test file (e.g., `tests/test_views.py`) and define a test class inheriting from Django's `TestCase`.

    ```python
    # tests/test_views.py
    from django.test import TestCase, Client
    from unittest.mock import patch, MagicMock # Import patch and other mock tools
    # No need to import requests directly in test if mocking
    from django.urls import reverse # To get URL by name

    # Assuming the view is in 'products.views' for patch target
    # Adjust path if your app name is different

    class PostViewTest(TestCase): # Inherit from TestCase
        def setUp(self):
            self.client = Client() # Django test client

        # Test methods will go here
    ```

5.  **Write a Test for Success Condition:**
    Define a test method (e.g., `test_post_view_success`) decorated with **`@patch`** to mock `requests.get`.

    ```python
    # tests/test_views.py

    # ... imports and PostViewTest class

    class PostViewTest(TestCase):
        # ... setUp method

        @patch('products.views.requests.get') # Patch requests.get where it is used in views
        def test_post_view_success(self, mock_get): # The mock object is passed as an argument
            # Configure the mock to simulate a successful response
            mock_response = MagicMock() # Or just use the mock_get object directly
            mock_response.status_code = 200 # Set status code attribute
            # Define the data the mocked API should return
            return_data = {
                "userId": 1,
                "id": 1,
                "title": "mock title",
                "body": "mock body"
            }
            # Configure the mock's .json() method to return the desired data
            mock_response.json.return_value = return_data
            # Configure the mock_get object to return the mock_response when called
            mock_get.return_value = mock_response

            # Send a request to the Django view using the test client
            url = reverse('post') # Get URL for the 'post' view
            response = self.client.get(url)

            # Assert the response from the Django view
            self.assertEqual(response.status_code, 200) # Check HTTP status code
            self.assertJsonEqual(response.content, return_data) # Check JSON content

            # Assert that the mocked requests.get was called correctly
            expected_url = "https://jsonplaceholder.typicode.com/posts/1"
            mock_get.assert_called_once_with(expected_url) # Check it was called once with the correct URL
    ```

6.  **Write a Test for Failure Condition:**
    Define another test method (e.g., `test_post_view_fail`) using `@patch`. Configure the mock's **`side_effect`** to raise an exception.

    ```python
    # tests/test_views.py

    # ... imports, PostViewTest class, success test

    class PostViewTest(TestCase):
        # ... setUp and success test methods

        @patch('products.views.requests.get') # Patch requests.get again
        def test_post_view_fail(self, mock_get): # Mock object argument
            # Configure the mock to simulate an exception
            mock_get.side_effect = requests.exceptions.RequestException # Make the mock raise RequestException when called

            # Send a request to the Django view
            url = reverse('post')
            response = self.client.get(url)

            # Assert the response from the Django view (should return 503 from the except block)
            self.assertEqual(response.status_code, 503) # Check for 503 status code
            # Optionally, check the content: self.assertEqual(response.content.decode(), "Service unavailable")

            # Assert that the mocked requests.get was called correctly even on failure
            expected_url = "https://jsonplaceholder.typicode.com/posts/1"
            mock_get.assert_called_once_with(expected_url) # Check it was called once with the correct URL

    ```

7.  **Run the Tests:**
    Execute the Django tests from the terminal.

    ```bash
    python manage.py test
    ```

    Verify that all tests, including the new success and failure tests for the view, pass.
