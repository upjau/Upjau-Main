from django.shortcuts import render
from .forms import *

def farm_land(request):
    form = FarmLandForm(request.POST)

    context = {
        'form': form,
    }

    if request.method=="POST":
        form = FarmLandForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FarmLandForm()

    return render(request, 'farm_land_form.html', context)

def farmer_dashboard(request):
    return render(request, 'dashboard/index.html')


# Dashboard elements:
def farmer_profilePage(request):
    user = request.user

    context = {
        'user': user,
    }

    return render(request, 'dashboard/profile.html', context)

def farmer_landPage(request):
    return render(request, 'dashboard/land.html')

def farmer_sellHarvestPage(request):
    return render(request, 'dashboard/sellHarvest.html')

