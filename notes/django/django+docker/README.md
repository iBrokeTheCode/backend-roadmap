# Docker - Django and PostgreSQL setup (with uv) from scratch!

This tutorial provides a deep dive into dockerizing a basic Django application alongside a PostgreSQL database container. It covers the fundamental concepts of using Docker images (Python and Postgres) and creating containers from them to run a Django application that connects to a PostgreSQL database. The learning objectives include setting up a Django project, creating a Dockerfile for the Django app, using Docker Compose to orchestrate the web and database services, configuring the Django application to connect to the database using environment variables and volumes, and interacting with the running containers.

## 1. Core Concepts

### Docker Basics

- **Docker Images**: A **blueprint** or **snapshot** that contains all the necessary components (code, libraries, dependencies, configuration) to run an application.
- **Docker Containers**: An **isolated environment** created from a Docker image, where an application can run. Each container is independent.
- **Dockerfile**: A text document containing **commands** that Docker uses to **assemble an image**.

### Dockerfile Instructions

- **`FROM`**: Specifies the **base image** to build upon (e.g., a Python image).
- **`ENV`**: Sets **environment variables** inside the container (e.g., `PYTHONUNBUFFERED`).
- **`WORKDIR`**: Sets the **working directory** for subsequent instructions (like `RUN`, `COPY`, `ADD`).
- **`COPY`**: Copies files or directories from the host machine into the container's file system.
- **`RUN`**: Executes **commands** during the image build process (e.g., installing packages).
- **`EXPOSE`**: Informs Docker that the container listens on the specified **network ports** at runtime (a declaration, not a binding).
- **`CMD`**: Sets the default **executable** and parameters for a container when it starts.
- **`ENTRYPOINT`**: Configures a container that will run as an executable. Often used with a custom script to perform setup tasks before running the main command.

### Dependency Management

- System dependencies: Installed using the base image's package manager (e.g., **`apt-get`** on Debian-based images).
- Python dependencies: Installed using a Python package manager like **`uv`** or `pip`, typically listed in a **`requirements.txt`** file. The `--system` flag with `uv pip install` uses the system Python inside the container without creating a virtual environment.
- **`psycopg2-binary`**: A **driver** for Python applications to communicate with a PostgreSQL database. The `-binary` version is pre-compiled, useful for development but not recommended for production where `libpq-dev` might be needed.

### Docker Layer Caching

- Docker builds images in **layers**. Copying and installing dependencies in a separate layer _before_ copying the rest of the application code is a **best practice** for **performance optimization** during rebuilds. If only the application code changes, Docker can reuse the cached dependency layers.

### Docker Compose

- A tool for defining and running **multi-container Docker applications**. Uses a **`docker-compose.yaml`** file.
- **Services**: Individual containers defined in the `docker-compose.yaml` file (e.g., `web` for Django, `db` for Postgres).
- **`build` vs. `image`**: `build` specifies a path to a directory containing a Dockerfile to build an image. `image` specifies an existing image name from Docker Hub or a registry.
- **Volumes**: Used for **persisting data** (e.g., database files) or **sharing code** between the host and container (e.g., development workflow). **Named volumes** are managed by Docker and persist data beyond container lifetime.
- **Ports**: **Mapping ports** between the host machine and containers, allowing access to container services from the host. Format: `HOST_PORT:CONTAINER_PORT`.
- **Environment Variables**: Pass configuration to services. Can be defined directly in the `docker-compose.yaml` or read from a **`.env` file** using the `env_file` key. **Interpolation** can be used to read values from the `.env` file.
- **Networking**: Docker Compose creates a default network. Services can communicate with each other using their **service names** as hostnames (e.g., the Django app can connect to the database using `host: db`).
- **Service Coordination**:
  - **`depends_on`**: Specifies that one service depends on another. By default, only ensures the dependency container is running.
  - **`condition: service_healthy`**: A condition used with `depends_on` to ensure a dependency service is **healthy** before starting the dependent service.
  - **`healthcheck`**: Defines how to check the health of a service. Uses a command that returns a status (e.g., **`pg_isready`** for Postgres). Configurable with interval, timeout, start period, and retries.
  - **`restart: true`**: Configures the service to automatically restart if the Docker daemon restarts or the container manually restarts.

### Container Interaction

- **`docker exec`**: Command used to **run commands inside a running container**. Useful for executing management commands (like Django migrations) or accessing command-line utilities (like `psql`). The `-ti` flag is often used to get an interactive terminal session.

## 2. Resources

- [Source Video Tutorial](https://youtu.be/37aNpE-9dD4?si=GeSCEjHTaWe1BOhr)
- [Docker Documentation](https://docs.docker.com/)
- [Python DockerHub](https://hub.docker.com/_/python)
- [Postgres DockerHub](https://hub.docker.com/_/postgres)
- [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/)
- [psycopg](https://www.psycopg.org/)
- [Project Sample](../django+docker/)

## 3. Practical Steps: Hands-on Guide

1.  **Set up Initial Django Project**

    - Create a project directory (e.g., `django_docker_demo`).
    - Inside the project directory, create a source directory (e.g., `src`).
    - Navigate into the `src` directory.
    - Run Django commands:
      ```bash
      django-admin startproject project .
      python manage.py startapp core
      ```
    - Open `src/django_docker_demo/settings.py` and add `'core'` to `INSTALLED_APPS`.

2.  **Create Dockerfile for Django App**

    - Navigate back to the project root directory (outside `src`).
    - Create a file named `Dockerfile`. Optionally, you can use **Docker extension for VSCode** and the tool `Docker: Add Docker Files to Workspace` (Press `Ctrl + Shift + P`). This will create Started Files, you can use as guide and keep `.dockerignore` or overwrite them.

    - The Dockerfile look like this:

      ```dockerfile
      FROM python:3.13.3-slim-bookworm

      # Keeps Python from generating .pyc files in the container
      ENV PYTHONDONTWRITEBYTECODE=1

      # Turns off buffering for easier container logging
      ENV PYTHONUNBUFFERED=1

      # Set Working Directory
      WORKDIR /app

      # Install curl
      RUN apt-get update && apt-get install -y curl

      # Install uv
      COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

      # Install pip requirements
      COPY src/requirements.txt .
      RUN uv pip install -r requirements.txt --system

      # Copy project files
      COPY src/ .

      # Expose port
      EXPOSE 8000

      # Creates a non-root user with an explicit UID and adds permission to access the /app folder
      # RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
      # USER appuser

      # Execute Django server
      CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
      ```

    - You have to create `src/requirements.txt` and put the packages of your project:

      ```txt
      django
      psycopg[binary]

      ---

      django==5.2.1
      psycopg==3.2.7
      psycopg-binary==3.2.7
      ```

3.  **Set up Docker Compose File**

    - In the project root directory, create a file named `docker-compose.yml`.
    - Add the basic structure and define the services:

      ```yaml
      services:
        web:
          # build: .
          build: # Build from the Dockerfile in the current directory
            context: .
            dockerfile: ./Dockerfile
          container_name: django_app # Optional, provides a friendly name
          ports: # Map host port 8000 to container port 8000
            - 8000:8000
          volumes: # Mount the source directory for live updates during development
            - ./src:/app
          depends_on:
            db:
              condition: service_healthy # Wait for the database to be healthy
              # command: python manage.py runserver 0.0.0.0:8000 # CMD from Dockerfile is default
              restart: true # Restart if the service fails
          env_file:
            - .env
        db:
          # Configuration for the Postgres database service goes here
          image: postgres:17 # Use a specific Postgres image from Docker Hub
          container_name: postgres_db # Optional, friendly name
          volumes:
            - postgres_data:/var/lib/postgresql/data/ # Named volume for data persistence
          environment: # Set required Postgres environment variables
            # Values will be read from the .env file via interpolation
            POSTGRES_DB: ${POSTGRES_DB}
            POSTGRES_USER: ${POSTGRES_USER}
            POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
          healthcheck: # Define a health check for the database
            test: [
                "CMD-SHELL",
                "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}",
              ] # Check if Postgres is ready
            interval: 10s # Check every 10 seconds
            retries: 5 # Retry 5 times
            start_period: 30s # Allow 30 seconds for the container to start
            timeout: 10s # Wait 5 seconds for a response

      # Define named volumes
      volumes:
        postgres_data:
      ```

4.  **Create `.env` File**

    - In the project root directory, create a file named `.env`.
    - Add environment variables needed by the services:

      ```ini
      # Database Configuration
      POSTGRES_DB=dev_database
      POSTGRES_USER=bug_bytes # Or your desired user
      POSTGRES_PASSWORD=changeme # Change to a secure password

      # Django Database Host/Port (Used in settings.py)
      DB_HOST=db # Use the service name 'db' for the host
      DB_PORT=5432 # Default Postgres port
      ```

5.  **Configure Django Settings for Postgres**

    - Open `src/django_docker_demo/settings.py`.
    - Import the `os` module.
    - Modify the `DATABASES` setting to use environment variables:

      ```python
      import os # Add this at the top

      # ... other settings

      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': os.environ.get('POSTGRES_DB'), # os.environ['POSTGRES_DB']
              'USER': os.environ.get('POSTGRES_USER'),
              'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
              'HOST': os.environ.get('DB_HOST'), # Use the service name 'db'
              'PORT': os.environ.get('DB_PORT'),
          }
      }
      ```

6.  **Build and Run with Docker Compose**

    - Ensure Docker Desktop (or your Docker engine) is running.
    - Open a terminal in the project root directory (where `docker-compose.yml` is).
    - Run the command to build images and start containers:

      ```bash
      docker compose up
      # docker compose up --build
      ```

    - Docker will build the web image, pull the Postgres image, start the Postgres container, wait for its health check to pass, and then start the web container.

7.  **Verify Django App**

    - Once the `docker compose up` command shows the Django development server running, open a web browser and go to `http://localhost:8000`.
    - You should see the default Django landing page.

8.  **Add Django Model**

    - Open `src/core/models.py`.
    - Define a simple model, e.g.:

      ```python
      from django.db import models

      class Actor(models.Model):
          name = models.CharField(max_length=100)
          nationality = models.CharField(max_length=100)
          added_at = models.DateTimeField(auto_now_add=True)

          def __str__(self):
              return self.name
      ```

9.  **Run Migrations via Docker Exec**

    - Open a _new_ terminal (leave the `docker compose up` process running).
    - Run `makemigrations` inside the Django container:

      ```bash
      docker exec django_app python manage.py makemigrations
      ```

    - Run `migrate` inside the Django container to apply migrations to the database:
      ```bash
      docker exec django_app python manage.py migrate
      ```

10. **Interact with Postgres Container via Docker Exec**

    - Use `docker exec` to access the `psql` command-line utility inside the database container:
      ```bash
      docker exec -ti postgres_db psql -U bug_bytes -d dev_database
      ```
    - Inside the `psql` prompt, you can list tables:
      ```sql
      \dt
      ```
      You should see your `core_actor` table along with Django's built-in tables.
    - Exit `psql` by typing `\q` and pressing Enter.

11. **Interact with Django Shell via Docker Exec**

    - Use `docker exec` to access the Django shell inside the web container:

      ```bash
      docker exec -ti django_app python manage.py shell
      ```

    - Inside the Django shell, you can create objects:

      ```python
      from core.models import Actor # (Or use auto-imported models if Django 5.2+)
      Actor.objects.create(name='Joe Pesci', nationality='American')
      Actor.objects.create(name='Michael Caine', nationality='British')
      ```

    - Verify the data by connecting back to the Postgres container (step 12) and running a SQL query:
      ```sql
      SELECT * FROM core_actor;
      ```
      You should see the added rows.
    - Exit the Django shell by typing `exit()` and pressing Enter.

12. **(Optional) Implement Entrypoint Script for Migrations**

    - Create a file named `entrypoint.sh` in the project root directory.
    - Add commands to run migrations and then start the server:

      ```bash
      #!/bin/sh

      # Apply database migrations
      echo "Applying database migrations..."
      python manage.py migrate

      # Start the Django development server
      echo "Starting server..."
      python manage.py runserver 0.0.0.0:8000
      ```

    - Make the script executable (on Linux/Mac hosts):

      ```bash
      chmod +x entrypoint.sh
      ```

    - Modify the `Dockerfile` to use this script instead of `CMD`:

      ```dockerfile
      # ... previous Dockerfile content

      # Use the custom entrypoint script
      ENTRYPOINT ["./entrypoint.sh"] # Note: /app is the WORKDIR
      ```

      *(Make sure `COPY ./src/ /app/` is *before* this line)*

    - Stop the currently running Docker Compose process (`Ctrl+C`).
    - Simulate a code change (e.g., add a field to the `Actor` model in `src/core/models.py`).
    - Run `makemigrations` on your host machine (or via `docker exec` if preferred) to generate the new migration file (`docker exec django_app python manage.py makemigrations` if containers were already running).
    - Run `docker compose up --build` again. Observe that the entrypoint script automatically runs the `migrate` command during container startup.

This completes the basic setup and interaction with the dockerized Django and PostgreSQL application.
