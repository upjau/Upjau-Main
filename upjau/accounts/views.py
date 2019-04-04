from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.views.generic.base import RedirectView

from .models import *
from .forms import *

def login(request):
    
    context = [
    
    ]

    return render(request, 'authentication/login.html') 

def register(request):
    if request.method == 'POST':
        print("test1")
        form = ProfileForm(request.POST)
        print("test2")
        if form.is_valid():
            print("Save pre")
            form.save()
            print("Save Post")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('/register')
    else:
        print("Why here?")
        form = ProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/register.html', context)
