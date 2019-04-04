from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .constants import *

class Profile(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=18)
    pincode = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=40, choices=COUNTRY)
    category = models.CharField(max_length=20, choices=CATEGORY)

    def __str__(self):
        return self.username

