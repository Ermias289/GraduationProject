# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_USER = "USER"
    ROLE_ADMIN = "ADMIN"
    ROLE_CHOICES = [
        (ROLE_USER, "User"),
        (ROLE_ADMIN, "Admin"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ROLE_USER)
    # you can add extra profile fields here (phone, address, etc.)

    def is_admin(self):
        return self.role == self.ROLE_ADMIN or self.is_staff or self.is_superuser
