from django.contrib.auth.models import AbstractUser
from django.db import models


class Accounts(AbstractUser):
    birthdate = models.DateField()
    bio = models.TextField(null=True)
    is_critic = models.BooleanField(null=True, default=False)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name", "birthdate"]
