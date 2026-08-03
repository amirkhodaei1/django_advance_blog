from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionManager,
)


class User(AbstractBaseUser, PermissionManager):
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_veirfied=models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    USERNANE_FIELD='email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


# Create your models here.
