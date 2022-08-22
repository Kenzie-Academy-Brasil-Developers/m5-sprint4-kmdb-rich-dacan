from django.contrib.auth.models import AbstractUser
from django.db import models


class Accounts(AbstractUser):
    birthdate = models.DateField()
    bio = models.TextField()
    is_critic = models.BooleanField(default=False)
    updated_at = models.DateTimeField()
