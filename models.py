from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class MyUser(AbstractUser):
    mobile = models.CharField(unique=True, max_length=11)

    REQUIRED_FIELDS = ['email', 'mobile']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



