from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    cv = models.FileField(upload_to="cvs/", blank=True, null=True)
