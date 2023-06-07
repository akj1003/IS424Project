from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_supplier = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
