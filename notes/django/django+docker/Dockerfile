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
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use the custom entrypoint script
ENTRYPOINT ["./entrypoint.sh"]