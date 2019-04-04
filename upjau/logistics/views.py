from django.shortcuts import render


def logistics_profilePage(request):
    user = request.user

    context = {
        'user': user,
    }

    return render(request, 'dashboard/logprofile.html', context)

