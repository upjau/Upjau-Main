from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .constants import *

class Profile(AbstractUser):
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100, choices=GENDER_CHOICE)
    state = models.CharField(max_length=18)
    pincode = models.IntegerField()
    country = models.CharField(max_length=40)
    category = models.CharField(max_length=20)

