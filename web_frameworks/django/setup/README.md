# Django Setup and Project Structure

## 1. Django Installation

**Theory:**

- Django is a Python web framework, so you'll need Python installed.
- We'll use `pip` (Python's package installer) to install Django.
- It's highly recommended to use a virtual environment to isolate your project's dependencies.

**Steps:**

a. **Create a Virtual Environment:**

- `python3 -m venv myenv` (creates a virtual environment named `myenv`)
- `source myenv/bin/activate` (activates the virtual environment)

b. **Install Django:**

- `pip install Django` (installs the latest version of Django)
- `pip install "django~=4.2.0"` (installs a specific version of Django, for example 4.2.0)

c. **Verify Installation:**

- `python -m django --version` (checks the installed Django version)

## 2. Creating a Django Project

**Theory:**

- A Django project is a collection of settings for an instance of Django.
- It includes configuration for databases, middleware, and applications.

**Steps:**

**a. Create a Project:**

- `django-admin startproject myproject` (creates a Django project named `myproject`)

**b. Project Structure:**

- `myproject/`: The project directory.
  - `manage.py`: A command-line utility for administrative tasks.
  - `myproject/`: The inner project directory.
    - `__init__`.py: An empty file that tells Python that this directory should be considered a Python package.
    - `asgi.py`: An entry-point for ASGI-compatible web servers to serve your project.
    - `settings.py`: Project settings and configurations.
    - `urls.py`: URL declarations for the project.
    - `wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project.

## 3. Running the Development Server

**Theory:**

- Django includes a lightweight development server for testing.
- It automatically reloads code changes, making development faster.

**Steps:**

**a. Navigate to the Project Directory:**

- `cd myproject`

**b. Run the Server:**

- `python manage.py runserver`

**c. Access the Server:**

- Open your web browser and go to `http://127.0.0.1:8000/`. You should see the default Django welcome page.

## 4. Creating a Django App:

**Theory:**

- A Django app is a reusable component of a Django project.
- Each app is responsible for a specific functionality (e.g., blog, users, products).

**Steps:**

**a. Create an App:**

- `python manage.py startapp myapp` (creates an app named `myapp`)

**b. App Structure:**

- `myapp/`: The app directory.
  - `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
  - `admin.py`: Configuration for the Django admin interface.
  - `apps.py`: App configuration.
  - `models.py`: Data models (database tables).
  - `tests.py`: Unit tests for the app.
  - `views.py`: Request handlers (logic for handling HTTP requests).

## 5. Registering the App:

**Theory:**

- You need to register your app in the `settings.py` file for Django to recognize it.

**Steps:**

- Open `myproject/settings.py`.
- Add your app to the `INSTALLED_APPS `list:

```python
INSTALLED_APPS = [
    'myapp', #Add this line
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
