# Optimizing Test Performance

## 1. Core Concepts

### The Need for Speed

Large Django projects can have thousands of tests that hit the database, perform computationally intensive logic, or use many objects, leading to **slow execution times**. Optimizing test performance is vital for efficient development and rapid feedback loops, especially in continuous integration/continuous deployment (CI/CD) workflows.

### Mocking External Services

Tests that interact with external services like APIs or caches can be slow due to network connections, latency, or potential errors. A performance improvement is to **mock** these services, replacing them with **mock objects** that simulate their behavior without the overhead of actual external calls.

### Efficient Test Setup: `setup_test_data`

The `setup_test_data` is a **class method** available on the **`TestCase`** class. Unlike a standard `setup` function (which runs before _every_ test method in a class), `setup_test_data` runs only **once** for the entire test case class. This allows for consolidating test setup and is a good performance optimization for classes with complex setup logic and many test methods, as data creation happens only once.

### Database Handling: `TestCase` vs `TransactionTestCase`

Django provides different base classes for tests that interact with the database. The **`TestCase`** class is generally **more performant** than **`TransactionTestCase`**.

- **`TestCase`**: Encloses test code within a **database transaction**. To reset the database state after each test, it simply **rolls back the transaction**. Rolling back a transaction is a quick operation.
- **`TransactionTestCase`**: Resets the database by **truncating all tables**. Truncating tables involves looking at all tables and calling the `TRUNCATE` SQL command for each one, which is slower than rolling back a transaction.
  You should typically subclass **`TestCase`** unless you specifically need to test transaction-specific behavior (e.g., using `select_for_update`).

### Parallel Execution

Running tests in **parallel** can significantly speed up the test suite, especially on **multi-core hardware** and when you have a large number of tests. Django's test runner can execute tests concurrently. When run in parallel, Django creates a separate **test database** for each process or core being used.

### Faster Authentication: Overriding Password Hashers

If your test suite involves authenticating users, the default Django password hasher can be slow by design. For tests, you can override the `PASSWORD_HASHERS` setting in a custom settings file (like one specifically for tests) and use a **faster algorithm** such as **MD5**. This is **not recommended for production** as MD5 is easily cracked, but it's safe for a test suite.

### Reusing the Test Database

By default, Django's test runner creates a new test database before running tests and destroys it afterward. The **`--keepdb`** option allows you to **preserve the test database** between test runs. This skips the time-consuming create and destroy actions, which can significantly decrease the time to run tests, especially if you have many tests hitting the database. Whether you can use this depends on whether your tests require a fresh database state for each run.

### Identifying Slow Tests: `--durations` flag

New in Django 5, the **`--durations N`** flag can be used with `manage.py test` (requires Python 3.12 or later). This flag shows the **N slowest test cases**, which is helpful for identifying performance bottlenecks within your test suite.

### Selective Testing

Instead of running the entire test suite, you can **selectively run a subset of tests**. This is useful when focusing on testing a specific feature or part of the application. You can run tests from a specific file by providing the path to `manage.py test`.

### Tagging Tests

Tests can be assigned **tags** using the **`@tag` decorator** from the `django.test` package. Tags are strings or sets of strings applied to test methods. This allows you to group related tests (e.g., all tests involving authentication can be tagged with 'auth'). You can then use the **`--tag <tag_name>`** option with `manage.py test` to run only the tests that have a specific tag.

### Other Considerations

Disabling logging in tests can also potentially offer performance improvements.

## 2. Resources

- [Testing in Django Tutorial #15 - Optmizing Test Performance](https://youtu.be/f4ndAxG54Pg?si=YFDwrUjAD1qRI2Es)
- [Speeding up the tests](https://docs.djangoproject.com/en/5.1/topics/testing/overview/#speeding-up-the-tests)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [TestCase](https://docs.djangoproject.com/en/5.1/topics/testing/tools/#testcase)
- [TransactionTestCase](https://docs.djangoproject.com/en/5.1/topics/testing/tools/#transactiontestcase)
- [Testing Project](./testing-project/)

## 3. Practical Steps: Hands-on Guide

1.  **Run Tests in Parallel**
    To run your test suite concurrently on multiple CPU cores, use the `--parallel` flag with the `manage.py test` command.

    ```bash
    python manage.py test --parallel
    ```

    You can optionally specify the number of cores to use:

    ```bash
    python manage.py test --parallel N  # Replace N with the desired number of cores
    ```

    Note that running in parallel involves creating multiple test databases.

2.  **Override Password Hashers for Tests (Conceptual)**
    To speed up tests involving user authentication, configure your test settings to use a faster password hashing algorithm like MD5. This involves creating or modifying a settings file used for tests (e.g., `settings_test.py`) and changing the `PASSWORD_HASHERS` setting.

    ```python
    # Example in settings_test.py
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ]
    ```

    Remember this is **not recommended for production**.

3.  **Preserve the Test Database**
    To avoid recreating and destroying the test database for each test run, use the `--keepdb` flag.

    ```bash
    python manage.py test --keepdb
    ```

    Use this only if your tests do not require a completely fresh database state on every run.

4.  **Run Tests by File Path**
    To run only the tests contained within a specific file, provide the path to the file as an argument to `manage.py test`.

    ```bash
    python manage.py test <app_name>/tests/<file_name>.py
    # Example:
    # python manage.py test users/tests/test_views.py
    ```

    This allows you to focus on testing a particular part of your application.

5.  **Tag a Test Method**
    To tag a specific test method (or class) with a string tag, import the `tag` decorator and apply it to the method.

    ```python
    # In your test file (e.g., tests/test_views.py)
    from django.test import TestCase, tag # Make sure to import tag

    class ProfilePageTests(TestCase):
        # ... other methods ...

        @tag('auth') # Apply the 'auth' tag
        def test_authenticated_user_can_access_profile_page(self):
            # ... test logic involving authentication ...
            pass

        @tag('auth', 'integration') # Apply multiple tags
        def test_another_auth_related_feature(self):
             # ... test logic ...
             pass
    ```

    You can apply one or more tags as strings to the decorator.

6.  **Run Tests by Tag**
    To run only the tests that have been tagged with a specific string, use the `--tag` option followed by the tag name.
    ```bash
    python manage.py test --tag auth
    ```
    This will execute all tests that have the 'auth' tag. You can specify multiple `--tag` arguments to run tests with any of the given tags.
