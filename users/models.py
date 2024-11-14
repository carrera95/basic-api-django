from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True, auto_now_add=True)
    uncripted_pswd = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username