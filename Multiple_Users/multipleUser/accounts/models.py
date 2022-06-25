from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_donar = models.BooleanField(default=False)
    is_ngo = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Donar(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)

class Ngo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    Ngo_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

