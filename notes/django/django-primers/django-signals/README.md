# Django Signals

This tutorial introduces **Django Signals**, a built-in part of the Django framework that allows different parts of an application to communicate and respond to events. Signals enable **senders** to notify a set of **receivers** that a specific event has occurred, acting as a **signal dispatcher** that helps decoupled apps get notified when actions happen elsewhere in the framework. They are particularly useful when multiple pieces of code might be interested in the same event, although it's noted that they can sometimes lead to code that is harder to understand, adjust, and debug if misused.

## 1. Core Concepts

- **Django Signals**: A mechanism within the Django framework for allowing decoupled applications or parts of applications to be notified when certain actions occur. They connect **events** to **actions**.
- **Sender**: The component that dispatches or "sends" a signal when an event takes place.
- **Receiver**: A function or piece of code that "listens" for a specific signal from a specific sender and executes predefined actions when the signal is received.
- **Signal Dispatcher**: The core mechanism in Django that manages the connections between senders and receivers, ensuring that receivers are notified when their corresponding signals are sent.
- **Connecting Receivers**: To receive a signal, you register a **receiver function**. This can be done using the `signal.connect()` method, which takes the receiver function, an optional sender, and an optional `dispatch_uid` as arguments.
- **`@receiver` Decorator**: An alternative, often more convenient, way to connect a receiver function to a signal. You place the `@receiver` decorator from `django.dispatch` directly above the receiver function, passing the signal and optional sender and `dispatch_uid` as arguments to the decorator.
- **`dispatch_uid`**: A unique ID for a signal receiver, used in cases where duplicate signals might otherwise be sent.
- **Built-in Signals**: Django provides several signals out-of-the-box for common events, such as:
  - **Model Signals**: Sent before or after model operations like saving (`pre_save`, `post_save`) or deleting (`pre_delete`, `post_delete`).
  - **Management Signals**: Related to management commands like migrations (`pre_migrate`, `post_migrate`).
  - **Request Signals**: Hooked into Django's request processing (`request_started`, `request_finished`).
  - **`setting_changed`**: Sent when Django settings are changed.
- **Receiver Function Arguments**: Receiver functions connected to built-in signals receive specific arguments depending on the signal. For example, `post_save` and `post_delete` model signals send the **sender** (the model class), the **instance** (the actual model instance being saved or deleted), and for `post_save`, a **created flag** (a boolean indicating if a new record was created).
- **Caveats of Using Signals**: While useful for decoupling, especially in reusable apps or third-party packages, signals can make code harder to follow and debug compared to direct function calls. It is often recommended to opt for directly calling handling code if you have control over both parts of the application.

## 2. Resources

- [Django Signals - Introduction!](https://youtu.be/8p4M-7VXhAU?si=JsGA8VTQlMNjvGCX)
- [Django Signals Documentation](https://docs.djangoproject.com/en/5.1/topics/signals/)
- [Django Built-in Signals Documentation](https://docs.djangoproject.com/en/5.1/ref/signals/)

## 3. Practical Steps: Hands-on Guide

This section outlines practical examples demonstrated in the tutorial, showing how to implement Django signals for specific tasks.

**Example 1: Sending a Welcome Email on User Creation**

This example uses the `post_save` signal to send a welcome email after a new user is saved to the database.

1.  **Set up Custom User Model:** Ensure you have a custom user model defined and specified in `settings.py` using the `AUTH_USER_MODEL` setting. Run `makemigrations` and `migrate` if necessary.
2.  **Create `signals.py`:** In your application's directory (e.g., `core`), create a file named `signals.py`.
3.  **Import necessary modules:**
    ```python
    # core/signals.py
    from django.db.models.signals import post_save # Import the post_save signal
    from django.dispatch import receiver # Import the receiver decorator
    from django.core.mail import send_mail # Import Django's send_mail function
    # Assuming your custom user model is in models.py in the same app:
    from .models import User # Import your custom User model
    ```
4.  **Define the receiver function:** Use the `@receiver` decorator to connect the function to the `post_save` signal, specifying the User model as the sender and providing a unique `dispatch_uid`. The function accepts `sender`, `instance`, and `created` arguments.

    ```python
    # core/signals.py

    @receiver(post_save, sender=User, dispatch_uid="send_welcome_email") # Connects to post_save signal for the User model
    def send_welcome_email(sender, instance, created, **kwargs): # Accepts standard arguments
        """
        Sends a welcome email to a user after they are created.
        """
        print("Signal fired") # Print statement for testing
        if created: # Check if a new user instance was created
            subject = "Welcome"
            message = "Thank you for signing up"
            from_email = "admin@django.com" # Use a real email in production
            recipient_list = [instance.email] # Get email from the saved user instance

            send_mail(subject, message, from_email, recipient_list) # Call Django's send_mail function
            print(f"Welcome email sent to {instance.email}") # Optional: confirmation print
    ```

5.  **Configure Email Backend (for development):** In `settings.py`, set the `EMAIL_BACKEND` to the console backend to see emails printed to the console during development instead of being sent.
    ```python
    # settings.py
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # Emails printed to console
    ```
6.  **Register Signals:** In your app's `apps.py` file, create a `ready` method within the `AppConfig` subclass and import the `signals` module to ensure the receivers are registered when the app is ready.

    ```python
    # core/apps.py
    from django.apps import AppConfig

    class CoreConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'core'

        def ready(self):
            import core.signals # Import the signals module to register receivers
    ```

7.  **Test:** Start the Django development server (`python manage.py runserver`). Register a new user through your application's registration page (or the admin interface). Check your console output for the "Signal fired" message and the printed email content.

**Example 2: Deleting Associated File on User Deletion**

This example uses the `post_delete` signal to clean up files associated with a model instance (like a user's CV) when the instance is deleted from the database.

1.  **Add FileField to Model:** Add a `FileField` to your model (e.g., a `CV` field to the User model). Configure `upload_to`, and set `null=True` and `blank=True` if the field is optional.

    ```python
    # core/models.py
    from django.db import models
    from django.contrib.auth.models import AbstractUser # Assuming you inherit AbstractUser

    class User(AbstractUser):
        # ... other fields ...
        cv = models.FileField(upload_to='cvs/', null=True, blank=True) # Add the FileField

        # ... other methods ...
    ```

2.  **Run Migrations:** Stop the server and run `python manage.py makemigrations` and `python manage.py migrate` to apply the model changes to the database.
3.  **Configure Media Settings:** In `settings.py`, set `MEDIA_ROOT` and `MEDIA_URL` to define where uploaded files will be stored and accessed.

    ```python
    # settings.py
    import os # Import os module

    BASE_DIR = Path(__file__).resolve().parent.parent # Assuming BASE_DIR is defined

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Define the root directory for media files
    MEDIA_URL = '/media/' # Define the URL path for media files
    ```

4.  **Create Media Directory:** Manually create the `media` directory at the root of your project if it doesn't exist. The `upload_to` path (`cvs/` in this case) will be created automatically under `MEDIA_ROOT` when a file is uploaded.
5.  **Import necessary modules:** In `signals.py`, import the `post_delete` signal and the `os` module.
    ```python
    # core/signals.py
    from django.db.models.signals import post_save, post_delete # Import post_delete signal
    from django.dispatch import receiver
    from django.core.mail import send_mail
    from .models import User
    import os # Import the os module
    ```
6.  **Define the receiver function:** Use the `@receiver` decorator for the `post_delete` signal and the User model sender. The function accepts `sender`, `instance`, and `**kwargs`. Implement logic to check if the instance has a file in the CV field and if that file exists on the filesystem, then remove it using `os.remove()`.

    ```python
    # core/signals.py

    # ... (previous post_save signal) ...

    @receiver(post_delete, sender=User) # Connects to post_delete signal for the User model
    def delete_associated_file(sender, instance, **kwargs): # Accepts standard arguments, including instance
        """
        Deletes the associated file from the filesystem when a User instance is deleted.
        """
        # Delete file from filesystem if it exists
        if instance.cv: # Check if the user instance has a file in the 'cv' field
            if os.path.isfile(instance.cv.path): # Check if the path points to an existing file
                os.remove(instance.cv.path) # Remove the file using os.remove()
                print(f"Deleted file: {instance.cv.path}") # Optional: confirmation print
    ```

7.  **Test:** Start the server. Go to the Django admin, add a user, upload a file to the CV field for that user, and save. Verify the file appears in your `media/cvs/` directory. Then, delete that user from the admin. Check the `media/cvs/` directory again; the file associated with the deleted user should now be gone.

This pattern can be applied to any model with `FileField` or `ImageField` to clean up corresponding files upon record deletion. Note that a third-party package called **`django-cleanup`** exists to automate this process for all models with file fields.
