from django.shortcuts import render
from . import models

def industry_profile(request):
    user = request.user
    context = {
        'user': user,
    }

    return render(request, 'dashboard/indprofile.html', context)

def industry_produceAvailable(request):
    user = request.user
    context = {
        'user': user,
    }

    return render(request, 'dashboard/available.html', context)

def industry_buyLand(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'dashboard/buyLand.html', context)

def industry_produce(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'dashboard/produce.html', context)
