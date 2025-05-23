# Testing in Django

## References

> [!IMPORTANT]  
> Notes taken from the [Testing in Django](https://youtube.com/playlist?list=PL4cUxeGkcC9ic9O6xDW2d1qMp3rMOb0Nu&si=9ZWgnUf-k8YjPICY) tutorial.

## Table of Contents

1. [Overview in Testing](./notes/testing-overview.md) - An introduction and overview of testing, specifically focusing on its application in web development and within the Django framework.
2. [The Python unittest Module](./notes/unittest-module.md) - **`unittest`** package in Python, which is part of the standard library and **Django's testing utilities are built on top of it**
3. [Django Testing Basics](./notes/django-testing-basics.md) - An introduction to the structure of test files and the utility of the **Django Test Case** class.
4. [Testing Modules](./notes/testing-modules.md) - Demonstrates how to test model **properties**, **methods**, and **validation logic** within the context of a Django application using the testing framework.
5. [Testing Database Constraints](./notes/database-constraints.md) - Enhances data integrity in Django applications by implementing and testing **database constraints**.
6. [TestCase](./notes/test-case.md) - Focus is on understanding how `TestCase` uses atomic transactions and how to leverage the **`setUpTestData`** class method as a performance enhancement compared to the standard `setUp` method
7. [Testing Views (part 1)](./notes/testing-views-1.md) - Understand how to write and test simple views that serve static HTML content without requiring database access, utilizing Django's testing tools like `SimpleTestCase` and the test client.
8. [Testing Views (part 2)](./notes/testing-views-2.md) - Write tests for views that retrieve data from models, add it to the template **context**, and display it.
9. [Testing Forms](./notes/testing-forms.md) - Covers creating a **Model Form** tied to a database model, adding **field-level validation** to the form, and integrating this form into a Django view to handle both GET and POST requests.
10. [Testing Authentication](./notes/testing-authentication.md) - Write tests to verify that protected pages are only accessible to authenticated users and that unauthenticated users attempting to access them are correctly redirected
11. [Mocking External Services](./notes/mocking-external-services.md) - Demonstrates how to use Python's built-in **`unittest.mock`** library, specifically the **`patch`** decorator, to mock external HTTP requests made using the **`requests`** module in a Django view.
12. [Testing Signals](./notes/testing-signals.md) - Write tests for a signal that sends a welcome email when a new user is created, specifically focusing on using **mocking** to test the email sending logic without actually sending emails
13. [Test Settings](./notes/testing-settings.md) - Demonstrates how to alter settings for the duration of a specific test function or apply a completely new settings file for testing purposes. This is achieved by building and testing a simple Django middleware class and utilizing the `override_settings` decorator and a dedicated test settings module.
14. [Optimizing Test Performance](./notes/optimizing-perfomance.md) - Covers several methods, including leveraging built-in Django test features, optimizing database interactions, using command-line flags for parallel execution and database management, and selectively running subsets of tests using tags.
15. [Test Coverage](./notes/test-coverage.md) - Introduces **coverage.py**, a powerful tool for measuring code coverage in Python programs. Code coverage measurement is primarily used to evaluate the effectiveness of your test suite by monitoring which parts of your code are executed when tests are run.
