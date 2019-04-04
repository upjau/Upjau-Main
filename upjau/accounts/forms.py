from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class ProfileForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Profile
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile', 'address', 'city', 'state', 'pincode', 'country', 'password1', 'password2']

