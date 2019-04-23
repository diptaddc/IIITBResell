# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile_no=models.CharField(max_length=120,default='7033574516')

    def __str__(self):
        return self.username
