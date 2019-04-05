from django.shortcuts import render
from . import models

def industry_profile(request):
    user = request.user
    context = {
        'user': user,
    }

    return render(request, 'dashboard/indprofile.html', context)

