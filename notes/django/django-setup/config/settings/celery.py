from config.env import env

CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://localhost:6379/0")  # type: ignore
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="django-db")  # type: ignore
CELERY_RESULT_EXTENDED = env("CELERY_RESULT_EXTENDED", default=True)  # type: ignore
