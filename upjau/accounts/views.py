from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.views.generic.base import RedirectView

from .models import *
from .forms import *

def login(request):
    return render(request, 'authentication/login.html') 

def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('/register')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html', context)

def mainPage(request):
    return render(request, 'index.html')
