from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.views.generic.base import RedirectView

def login(request):
    
    context = []

    return render(request, 'registration/login.html', context) 

