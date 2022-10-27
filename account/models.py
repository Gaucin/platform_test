from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "email",
    ]

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
