from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    supervisor = models.BooleanField(blank=True, default=False)
