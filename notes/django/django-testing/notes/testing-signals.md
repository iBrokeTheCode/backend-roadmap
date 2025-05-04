# Testing Signals

## 1. Core Concepts

- **Django Signals:** A mechanism in Django that allows certain **senders** to notify a set of **receivers** that an action has occurred. It helps **decoupled applications** react to events.
- **Signal Senders and Receivers:** A **sender** is the source of the signal (e.g., a model instance being saved), and **receivers** are functions that are invoked when the signal is sent.
- **`receiver` Decorator:** A decorator used to register a function as a signal receiver. It takes the specific signal (e.g., `post_save`) and optionally the sender (e.g., the User model) as arguments.
- **`post_save` Signal:** A built-in Django signal that is sent _after_ a model instance's `save()` method is called.
- **`instance` and `created` Arguments:** When a `post_save` signal is received, the receiver function gets the `instance` of the model that was saved and a boolean `created` flag which is `True` if the instance was created for the first time, and `False` if it was updated.
- **Wiring Signals:** For signals to be recognized and connected, they must be imported in the `ready()` method of the application's **AppConfig** subclass, typically located in `apps.py`.
- **Email Backend:** Django uses an email backend to handle sending emails. For development and testing, it's common practice to change the default backend to avoid sending real emails. The **`console` backend** is useful for testing as it writes emails to standard output instead of sending them. This is configured in `settings.py`.
- **Testing Signals:** Requires simulating the conditions that trigger the signal and verifying that the receiver function behaves as expected.
- **`unittest.mock.patch`:** A decorator or context manager from Python's `unittest.mock` library used to replace parts of the system under test with mock objects. This is essential for testing components that interact with external services, like sending emails, by **mocking** the external call (`send_mail`).
- **Mock Objects:** Objects that replace real objects during testing, allowing assertions about how they were called (e.g., if they were called, how many times, and with what arguments).
- **`assert_called_once_with()`:** A method on a mock object that asserts it was called exactly once and with the specified arguments.
- **`assert_not_called()`:** A method on a mock object that asserts it was never called.
- **`reset_mock()`:** A method on a mock object used to reset its call count and call history to zero.

## 2. Resources

- [Testing in Django Tutorial #13 - Testing Signals](https://youtu.be/DWMM0IJ2uNw?si=DzqDyo0mKx4_KzSn)
- [Django Documentation - Signals](https://docs.djangoproject.com/en/5.1/topics/signals/)
- [Project Tests](../testing-project/products/tests/test_signals.py)

## 3. Practical Steps: Hands-on Guide

1.  **Create a Signal Function:**

    - In your Django application (e.g., `products`), create a file named `signals.py`.
    - Define a function decorated with `@receiver(post_save, sender=User)`.
    - This function should accept `sender`, `instance`, and `created` arguments.
    - Implement logic inside the function, for example, checking `if created:` to send a welcome email only on user creation.
    - Example function structure:

      ```python
      # products/signals.py
      from django.db.models.signals import post_save
      from django.dispatch import receiver
      from django.contrib.auth.models import User
      from django.core.mail import send_mail

      @receiver(post_save, sender=User)
      def send_welcome_email(sender, instance, created, **kwargs):
          if created:
              print("Signal fired!") # Optional print statement for debugging
              subject = "Thank you for signing up!"
              message = "Welcome to the app." # Example message
              from_email = "admin@django.com"
              recipient_list = [instance.email]
              send_mail(subject, message, from_email, recipient_list, fail_silently=False)
      ```

2.  **Wire Up the Signal:**

    - Go to your application's `apps.py` file.
    - Inside the `ready()` method of your AppConfig subclass, import your `signals` module.
    - Example:

      ```python
      # products/apps.py
      from django.apps import AppConfig

      class ProductsConfig(AppConfig):
          default_auto_field = 'django.db.models.BigAutoField'
          name = 'products'

          def ready(self):
              import products.signals # Import your signals module here

              signals.send_welcome_email
              # _ = signals
      ```

3.  **Configure Email Backend for Testing:**

    - Open your project's `settings.py` file.
    - Add the following setting at the bottom to use the console email backend:
      ```python
      # settings.py
      EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
      ```

4.  **Test the Signal in Django Shell (Optional Manual Test):**

    - Open your terminal and navigate to your project directory.
    - Run the Django shell:
      ```bash
      python manage.py shell
      ```
    - Inside the shell, import the User model and create a new user:
      ```python
      from django.contrib.auth.models import User
      User.objects.create_user(username='testuser', password='password123', email='test@example.com')
      ```
    - Observe the output; you should see the "Signal fired!" print statement and the email content printed to the console.
    - Exit the shell: `exit()`.

5.  **Create a Test File for Signals:**

    - In your application's `tests` directory, create a file named `test_signals.py`.

6.  **Add Imports:**

    - Add necessary imports at the top of `test_signals.py`:
      ```python
      # products/tests/test_signals.py
      from django.test import TestCase
      from unittest.mock import patch # For mocking
      from products.models import User # The sender model
      ```

7.  **Write a Test Case Class:**

    - Create a class inheriting from `TestCase`:
      ```python
      # products/tests/test_signals.py
      class UserSignalsTest(TestCase):
          pass # Tests will go inside this class
      ```

8.  **Test Email Sent on User Creation:**

    - Add a test method inside `UserSignalsTest` to check if the email signal fires when a user is created.
    - Use the `@patch` decorator to mock the `send_mail` function.
    - Create a user, which triggers the signal.
    - Use `mock_send_mail.assert_called_once_with()` to verify the mock was called with the correct arguments.
    - Example:

      ```python
      # products/tests/test_signals.py
      # ... imports and UserSignalsTest class ...

          @patch('products.signals.send_mail') # Patch the send_mail function in the signals module
          def test_welcome_email_sent_on_user_creation(self, mock_send_mail):
              """
              Tests that the welcome email signal sends an email when a new user is created.
              """
              email = 'john@example.com'
              User.objects.create_user(username='john', password='password', email=email)

              # Assert that send_mail was called exactly once with the expected arguments
              expected_subject = "Thank you for signing up!"
              expected_message = "Welcome to the app." # Ensure this matches your signal logic
              expected_from_email = "admin@django.com"
              expected_recipient_list = [email] # Recipient should be the user's email

              mock_send_mail.assert_called_once_with(
                  expected_subject,
                  expected_message,
                  expected_from_email,
                  expected_recipient_list,
                  fail_silently=False # Match argument in signal
              )
      ```

9.  **Test No Email Sent on User Update:**

    - Add a second test method to ensure the email signal _doesn't_ fire when a user is updated, but not created.
    - Again, use `@patch` to mock `send_mail`.
    - Create a user first (this will trigger the signal, but we'll handle that).
    - Use `mock_send_mail.reset_mock()` to clear the call count from the creation step.
    - Update the user (e.g., change email) and call `.save()`.
    - Use `mock_send_mail.assert_not_called()` to confirm the mock wasn't called after the update.
    - Example:

      ```python
      # products/tests/test_signals.py
      # ... imports and UserSignalsTest class ...

          @patch('products.signals.send_mail') # Patch the send_mail function
          def test_no_email_sent_on_user_update(self, mock_send_mail):
              """
              Tests that the welcome email signal does not send an email when an existing user is updated.
              """
              # Create a user first - this *will* trigger the signal initially
              user = User.objects.create_user(username='jane', password='password', email='jane@example.com')

              # Reset the mock to clear the call from the creation step
              mock_send_mail.reset_mock()

              # Update the user and save - this triggers the signal again but 'created' will be False
              user.email = 'jane.new@example.com'
              user.save()

              # Assert that send_mail was *not* called after the update
              mock_send_mail.assert_not_called()
      ```

10. **Run the Tests:**
    - Open your terminal and navigate to your project directory.
    - Run the test command:
      ```bash
      python manage.py test
      ```
    - The tests should run and pass, confirming that your signal logic works as expected for both creation and update scenarios.
