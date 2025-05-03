# Django Testing Basics

## 1. Core Concepts

- **Django Testing Functionality**: Django provides built-in tools and structure to facilitate testing applications, leveraging the Python standard library's `unit test` module.
- **Out-of-the-Box Features**: When creating a Django application, a **`tests.py`** file is automatically included, serving as a default location for writing tests. This file typically imports the **`TestCase`** class from **`django.test`**.
- **Django Test Case vs. unit test.TestCase**: Django's **`TestCase`** is a **subclass** of Python's **`unit test.TestCase`**, inheriting methods like `setUp` and assertion methods (`self.assertEqual`, etc.). A key augmentation is that Django's **`TestCase`** automatically runs each test method within a **database transaction**, providing crucial isolation.
- **Test Discovery**: Django's test runner automatically discovers tests in files that start with `test_` (e.g., `test_models.py`, `test_views.py`) within your project. By default, it discovers tests throughout the project.
- **Running Tests**: Tests in a Django project are executed using the command **`python manage.py test`**. This command initiates the Django test runner.
- **Running a Subset of Tests**: You can run tests for specific applications by passing the application name to the test command, e.g., `python manage.py test products`.
- **Structuring Tests**: For larger applications, it's beneficial to organize tests into a **`test` directory** within the application, splitting tests into files like `test_models.py`, `test_views.py`, etc., instead of keeping all tests in a single `tests.py` file. This improves organization and readability.
- **Test Database Management**: When running tests, Django creates a **dedicated test database** instead of using the real production database. This ensures tests do not affect live user data. Regardless of test outcomes, the test database is **destroyed** after the tests complete. The default name for the test database is created by prepending **`test_`** to the database name defined in the `DATABASES` setting (e.g., `test_default`).
- **In-Memory SQLite Database**: If you are using SQLite, the test database will use an **in-memory database** by default, bypassing the file system for improved speed and performance.
- **Configuring the Test Database**: The `DATABASES` setting in `settings.py` includes a `test` dictionary where you can specify settings (like a different name) specifically for the test database.

## 2. Resources

- [Testing in Django Tutorial #4 - Django Testing Basics](https://youtu.be/QklKI2etw30?si=pygEJ2-MgmTkwfPN)
- [Django Documentation](https://docs.djangoproject.com/en/5.1/topics/testing/overview/)
- [Testing Project](./testing-project/)

## 3. Practical Steps: Hands-on Guide

1.  **Create a Python Virtual Environment**:

    ```bash
    python3 -m venv venv_testing
    ```

    This command uses the `venv` module to create a virtual environment named `venv_testing`.

2.  **Activate the Virtual Environment**:

    - On Mac/Linux:
      ```bash
      source venv_testing/bin/activate
      ```
    - On Windows (not shown in source, common practice):
      ```bash
      .\venv_testing\Scripts\activate
      ```

    Activating the environment ensures that packages installed are specific to this environment.

3.  **Install Django**:

    ```bash
    pip install django
    ```

    This command installs Django into the activated virtual environment.

4.  **Start a New Django Project**:

    ```bash
    django-admin startproject testing_project
    ```

    This command creates a new Django project directory named `testing_project`.

5.  **Change Directory into the Project**:

    ```bash
    cd testing_project
    ```

    Navigate into the newly created project directory to access the `manage.py` file.

6.  **Create a New Django Application**:

    ```bash
    python manage.py startapp products
    ```

    This command creates a new Django application directory named `products` within the project. This app directory contains the default `tests.py` file.

7.  **Add the New Application to `INSTALLED_APPS`**:
    Edit the `settings.py` file located inside the `testing_project` directory. Find the `INSTALLED_APPS` list and add the name of your new app (`'products'`) to it.

    ```python
    # settings.py
    INSTALLED_APPS = [
        # ... other apps
        'products',
    ]
    ```

    This registers the `products` application with your Django project.

8.  **Run Tests (Initial Run)**:

    ```bash
    python manage.py test
    ```

    Execute this command from the project root directory (where `manage.py` is located). Initially, it will report that no tests were found because no tests have been written yet, but it demonstrates the command for running tests.

9.  **Run Tests for a Specific Application**:
    ```bash
    python manage.py test products
    ```
    Use this command to run only the tests located within the `products` application.
