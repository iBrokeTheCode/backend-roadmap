# Testing in Django Tutorial #11 - Testing Authentication

## 1. Core Concepts

- **Authentication in Django:** The process of verifying the identity of a user accessing an application.
- **Protected Resources:** Pages or data within a Django application that should only be accessible to users who are logged in (authenticated). Testing ensures these resources are secure.
- **`login_required` Decorator:** A decorator applied to a view function or class method in Django that restricts access to authenticated users only. If an unauthenticated user tries to access a view protected by `login_required`, Django redirects them.
- **`LOGIN_URL` Setting:** A setting in Django's `settings.py` file that specifies the URL users should be redirected to when they attempt to access a view protected by `login_required` without being authenticated.
- **Django Test Client:** A utility provided by Django for simulating requests (GET, POST, etc.) to your application views within tests. It also offers methods, like `login`, to simulate user authentication for testing purposes.
- **User Model:** Django's built-in model for representing users. It's used in tests to create test user instances.
- **`reverse` Function:** A Django utility used to dynamically get the URL for a given URL pattern name. This is preferred over hardcoding URLs in tests.
- **`assertContains`:** A method available on Django test client responses or test cases that asserts whether the response content contains a specific string. Useful for checking if expected content is present after accessing a page.
- **`assertRedirects`:** A method available on Django test cases that asserts whether a response is a redirect. It can optionally check if the redirect is to a specific expected URL.
- **`next` Query Parameter:** When Django redirects an unauthenticated user from a protected page to the login page, it often adds a `?next=/path/to/protected/page/` query parameter to the login URL. This parameter tells Django where to redirect the user _after_ they successfully log in.

## 2. Resources

- [Testing in Django Tutorial #11 - Testing Authentication](https://youtu.be/LBuyGv3R0IY?si=iqHAFVDzOjnUXnfn)
- [Testing Project](./testing-project/)

## 3. Practical Steps: Hands-on Guide

Follow these steps to write authentication tests for a protected profile page and an unprotected login page in Django:

1.  **Ensure Setup:** Have views, URL patterns, and templates configured, including a view protected by `@login_required` (e.g., `profile_view`), an unprotected login view (`login_view`), and the `LOGIN_URL` setting configured in `settings.py`.
2.  **Navigate to Tests:** Go to your application's `tests` directory and open or create `test_views.py`.
3.  **Import Necessary Modules:** Import `TestCase` from `django.test` and your `User` model (e.g., from `product.models`).

    ```python
    from django.test import TestCase, Client
    from django.urls import reverse
    from django.contrib.auth import get_user_model # Or import your specific User model path
    # Assuming your User model is the default or accessible
    User = get_user_model()
    ```

4.  **Create a Test Class:** Define a new test class that subclasses `TestCase`, for example, `TestProfilePage`.

    ```python
    class TestProfilePage(TestCase):
        # Test methods will go here
        pass
    ```

5.  **Write Test for Authenticated Access:** Add a method to test that an authenticated user can access the protected view.

    - Create a test user using `User.objects.create_user()`.
    - Log in the created user using `self.client.login(username='...', password='...')`.
    - Send a GET request to the protected page using `self.client.get(reverse('profile'))`.
    - Assert that the response contains content expected on the profile page (e.g., the user's username) using `self.assertContains(response, 'testuser')`.

    ```python
    class TestProfilePage(TestCase):
        def test_profile_view_accessible_for_authenticated_users(self):
            # Create a test user
            test_user = User.objects.create_user(username='testuser', password='testpassword')

            # Log in the user using the test client
            self.client.login(username='testuser', password='testpassword')

            # Send a GET request to the profile page
            response = self.client.get(reverse('profile')) # Assuming 'profile' is the URL name

            # Assert that the response contains the username (indicating successful access)
            self.assertContains(response, 'testuser')
    ```

6.  **Write Test for Unauthenticated Redirection:** Add a method to test that an unauthenticated user is redirected from the protected view.

    - Send a GET request to the protected page _without_ logging in a user.
    - Assert that the response is a redirect using `self.assertRedirects(response, expected_url)`.
    - The `expected_url` should be the `LOGIN_URL` with the `next` query parameter pointing back to the protected page. Use `reverse` for the login URL and construct the `next` parameter.

    ```python
    class TestProfilePage(TestCase):
        # ... (previous method) ...

        def test_profile_view_redirects_for_anonymous_users(self):
            # Send a GET request to the profile page without logging in
            response = self.client.get(reverse('profile')) # Assuming 'profile' is the URL name

            # Construct the expected redirect URL (LOGIN_URL with 'next' parameter)
            # Assuming 'login' is the URL name for the login page and LOGIN_URL is set accordingly
            expected_url = f"{reverse('login')}?next={reverse('profile')}"

            # Assert that the response is a redirect to the expected login URL
            self.assertRedirects(response, expected_url)
    ```

7.  **Run the Tests:** Execute the tests from your terminal.

    ```bash
    python manage.py test
    ```

8.  **Optional: Run Specific Tests:** To run only the tests in the `TestProfilePage` class, specify the app, file, and class path.

    ```bash
    python manage.py test <app_name>.tests.test_views.TestProfilePage
    ```

These tests help ensure that protected pages are not accidentally exposed to unauthenticated users, verifying the application's security behavior.
