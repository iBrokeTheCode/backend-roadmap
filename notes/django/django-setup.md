# Django Environment-Based Settings Setup

## 1. Core Concepts

- **Environment-Specific Settings** Django projects need different settings for different environments (e.g., local development, production, testing). Settings like `DEBUG`, database configurations, secret keys, and allowed hosts should vary.
- **Hacksoft Style Guide** The lesson follows setting recommendations from the Hacksoft style guide for Django. This guide suggests a specific folder structure for organizing settings.
- **Settings Structure** The recommended structure involves a `config` directory at the project root. Inside `config`, there are two subdirectories: `django` for Django-specific settings per environment (`base.py`, `local.py`, `production.py`, `test.py`) and `settings` for third-party application configurations (e.g., `celery.py`, `file_storage.py`). There is also an `env.py` file within the `config` directory.
- **`base.py` File** This file contains all the base, default settings for the project that are common across environments.
- **Environment Files (`local.py`, `production.py`, `test.py`)** These files import all settings from `base.py` and then overwrite or define environment-specific values.
- **`django-environ` Package** This package is used to read environment variables from a `.env` file.
- **`.env` File** A file at the project root that stores environment-specific configuration values (like `SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_SETTINGS_MODULE`, third-party service URLs, API keys, etc.). This file should **not** be committed to version control due to sensitive information.
- **`env.py` File** A single location where the `django-environ` `Env` object is instantiated and configured to read the `.env` file. This object is then imported and used in other settings files to access environment variables. The project's base directory (`BASE_DIR`) is also often defined here using `pathlib`.
- **`DJANGO_SETTINGS_MODULE`** An environment variable that tells Django which settings file (`.py` module) to load for the current environment. This variable is typically set in the `.env` file but can also be set in the terminal or server configuration.
- **Third-Party Settings** Configurations for external services (like Celery, Sentry, AWS, email providers) are separated into their own files within the `config/settings` directory. These files are then imported into `base.py`.
- **`.env.example` File** A non-sensitive file committed to version control that shows developers the expected environment variables required by the project, often with dummy values.

## 2. Practical Steps

### 2.1. Restructuring Settings

- [x] Start with the default Django project structure containing `settings.py` in the project folder.
- [x] Following the Hacksoft style guide, rename the main project folder to `config`.
- [x] Create two new directories inside the `config` folder: `django` and `settings`.
- [x] Update references to the old project name (e.g., `old_project_name`) in `urls.py`, `wsgi.py`, `asgi.py` and `settings.py` to point to the new `config` folder.
- [x] Move the `settings.py` file from the `config` directory into the `config/django` directory and rename it to `base.py`. This file now holds the base settings.
- [x] Create empty `__init__.py` files in both `config/django` and `config/settings` to make them Python packages.
- [x] Create environment-specific settings files inside `config/django`: `local.py`, `production.py`, and `test.py`.
- [x] In `local.py`, `production.py`, and `test.py`, import all settings from `base.py`.

  ```python
  from config.django.base import *
  ```

### 2.2. .env File and Django-environ

- [x] Create a `.env` file at the project root. Define environment variables, including `DJANGO_SETTINGS_MODULE`.

  ```env
  DJANGO_SETTINGS_MODULE='config.django.local'
  DJANGO_DEBUG = True
  SECRET_KEY=secret
  # Add other settings like database URL, API keys, etc.
  ```

- [x] Install the `django-environ` package.

  ```shell
  pip install django-environ

  # uv or poetry
  uv add django-environ
  poetry add django-environ
  ```

- [x] Create an `env.py` file inside the `config` directory.
- [x] Add code to `config/env.py` to instantiate `django-environ`'s `Env` object and define `BASE_DIR`.

  ```python
  # In config/env.py
    from pathlib import Path

    import environ

    BASE_DIR = Path(__file__).resolve().parent.parent
    env = environ.Env()
  ```

- [x] In `config/django/base.py`, import the `env` object and `BASE_DIR` from `config.env`. Also, import the `os` module. Then, use the `env.read_env()` method to load values from a `.env` file.

  ```python
  # In config/django/base.py
  import os
  from config.env import env, BASE_DIR

  # Read the .env file
  env.read_env(os.path.join(BASE_DIR, '.env'))
  # env.read_env(BASE_DIR / ".env") # MODERN WAY
  ```

- [x] Modify settings in `base.py` to read values from environment variables using the `env` object. Provide appropriate casting and default values.

  ```python
  # In config/django/base.py

  SECRET_KEY = env("SECRET_KEY") # Read SECRET_KEY from environment
  DEBUG = env.bool("DJANGO_DEBUG", default=True)  # type:  ignore
  ALLOWED_HOSTS = ["*"]
  ```

- [x] Define environment-specific settings in their respective files, often overriding or setting defaults differently than `base.py`.

  ```python
  # In config/django/production.py
  from config.django.base import *
  from config.env import env

  # Override settings for production
  # DEBUG = env.bool("DJANGO_DEBUG", default=False)  # type: ignore
  DEBUG = False
  # Read ALLOWED_HOSTS from environment, defaulting to an empty list if not set
  ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
  ```

- [x] Update the `DJANGO_SETTINGS_MODULE` environment variable setting in `manage.py`, `wsgi.py`, and `asgi.py` to point to the desired default environment settings file (e.g., `config.django.local`).

  ```python
  # In manage.py, config/wsgi.py, config/asgi.py

  # ...
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.local')
  # ...
  ```

- [x] Verify settings are loaded correctly by running `python manage.py shell` and inspecting `django.conf.settings`.

  ```bash
  python manage.py shell
  ```

  ```python
  # In the Django shell
  from django.conf import settings
  print(settings.SECRET_KEY)
  print(settings.DEBUG)
  print(settings.ALLOWED_HOSTS)
  ```

- [x] Demonstrate switching environments by changing the `DJANGO_SETTINGS_MODULE` environment variable in the terminal before running Django commands.
  ```bash
  # On Linux/macOS
  export DJANGO_SETTINGS_MODULE=config.django.production
  python manage.py shell
  ```
  ```powershell
  # On Windows PowerShell
  $env:DJANGO_SETTINGS_MODULE="config.django.production"
  python manage.py shell
  ```

---

**(16:44)**

### 2.3. Third-Party Configuration

- Create files for third-party settings inside the `config/settings` directory (e.g., `celery.py`, `file_storage.py`).
- In these third-party settings files, import the `env` object from `config.env` and define settings, reading values from the environment using `env`.

  ```python
  # In config/settings/celery.py
  from config.env import env

  CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='redis://localhost:6379/0')
  CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', default='django-db')
  CELERY_RESULT_EXTENDED = env('CELERY_RESULT_EXTENDED', default=True)
  ```

  ```python
  # In config/settings/file_storage.py (example for Django Storages with S3)
  from config.env import env

  # Django 4.2+ STORAGES setting
  STORAGES = {
      "default": {
          "BACKEND": "storages.backends.s3.S3Storage",
          "OPTIONS": {
              # Add options here if needed
          },
      },
      "staticfiles": {
          "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
      },
  }

  AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
  AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
  AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
  AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
  # Add other S3 related settings if necessary
  ```

- In `config/django/base.py`, import all settings from the third-party settings files created in the previous step.

  ```python
  # In config/django/base.py (at the bottom)
  # ... other base settings ...

  # Import third-party settings
  from .settings.celery import * # Assumes celery.py exists in config/settings
  from .settings.file_storage import * # Assumes file_storage.py exists in config/settings
  # Import other third-party settings files here
  ```

- Create an `.env.example` file at the project root. Copy the structure of your `.env` file but replace sensitive values with dummy or placeholder values. Commit this file to version control.

  ```dotenv
  # In .env.example at the project root
  # Example environment variables required for this project

  DJANGO_SETTINGS_MODULE=config.django.local
  DJANGO_DEBUG=True
  SECRET_KEY=replace_with_a_real_secret_key

  # Database
  DATABASE_URL=postgres://user:password@host:port/dbname

  # Celery
  CELERY_BROKER_URL=redis://localhost:6379/0
  CELERY_RESULT_BACKEND=django-db

  # AWS S3 Storage (using django-storages)
  AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY_ID
  AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY
  AWS_STORAGE_BUCKET_NAME=your-s3-bucket-name
  AWS_S3_REGION_NAME=your-aws-region
  ```

- Add the `.env` file to your project's `.gitignore` file to prevent it from being committed to version control.
