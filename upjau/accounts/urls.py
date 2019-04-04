from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register/', views.register, name='registration'),
    url(r'$/', views.mainPage, name=''),
]
