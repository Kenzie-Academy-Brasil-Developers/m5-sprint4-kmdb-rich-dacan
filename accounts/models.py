from django.contrib.auth.models import AbstractUser
from django.db import models


class Accounts(AbstractUser):
    birthdate = models.DateField()
    bio = models.TextField(null=False)
    is_critic = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name", "birthdate"]
