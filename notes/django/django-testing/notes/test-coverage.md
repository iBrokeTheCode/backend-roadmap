# Testing in Django Tutorial #16 - Test Coverage

## 1. Core Concepts

### Code Coverage

**Code coverage** is a metric used to gauge the effectiveness of tests. It shows which parts of your code are being exercised by tests and which are not. Identifying code with **no coverage** helps developers determine where new tests might be needed.

### Coverage.py

**Coverage.py** is a third-party tool specifically designed for measuring the code coverage of Python programs. It monitors your program during execution, notes which lines of code are executed, and then analyzes the source to identify code that could have been run but wasn't.

### Phases of Coverage.py

Coverage.py operates in three distinct phases:

- **Execution Phase**: Coverage runs your code and monitors it to record which lines are executed. This phase is typically initiated using the `coverage run` command.
- **Analysis Phase**: After execution, coverage examines your code to determine all lines that _could_ have been run.
- **Reporting Phase**: This phase combines the results from the execution and analysis phases to produce a **coverage number** (percentage) and indicate **missing** lines. Reporting is handled by commands like `coverage report` or `coverage HTML`.

## 2. Resources

- [Testing in Django Tutorial #16 - Test Coverage](https://youtu.be/yLhV1qCDFeU?si=8rCfn2yqKkWVHc3U)
- [Coverage.py](https://coverage.readthedocs.io/en/7.8.0/)
- [Testing Project](./testing-project/)

## 3. Practical Steps: Hands-on Guide

Here's a step-by-step guide to using coverage.py based on the tutorial:

1.  **Install coverage.py**: Since it's a third-party tool, you need to install it into your virtual environment.

    ```bash
    pip install coverage
    ```

2.  **Run Tests with Coverage**: Replace the initial `python` in your test command with `coverage run` to execute your tests while coverage.py monitors code execution.

    ```bash
    coverage run manage.py test --settings=your_project.settings.testing
    ```

    _(Note: The `--settings` part might vary based on your project setup)_
    Running this command will look similar to a normal test run, but it creates a new file, `.coverage`, which stores the execution data.

3.  **View the Coverage Report (Terminal)**: After running tests with `coverage run`, use the `coverage report` command to see a summary in your terminal.

    ```bash
    coverage report
    ```

    This report shows files, statements, missed lines, and coverage percentage for each. It helps identify areas with less than 100% coverage, like a `views.py` file with 94% coverage and two missed statements in the example.

4.  **View the Coverage Report (HTML)**: For a more interactive view, generate an HTML report.

    ```bash
    coverage html
    ```

    This command writes an HTML report to an `index.html` file within an `htmlcov` directory.

5.  **Explore the HTML Report**: Open the generated `htmlcov/index.html` file in your browser to view the report interactively.

    ```bash
    # Navigate to the htmlcov directory and open index.html
    # For example, using a live server extension or just opening the file
    ```

    In the HTML report, you can click through files (e.g., `products/views.py`) to see the specific lines of code highlighted that were not covered (missed) during the test execution. This visual representation makes it easier to pinpoint where new tests are needed.
