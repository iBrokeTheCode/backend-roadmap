from config.django.base import *
from config.env import env

# DEBUG = env.bool("DJANGO_DEBUG", default=False)  # type: ignore
DEBUG = False
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])  # type: ignore
