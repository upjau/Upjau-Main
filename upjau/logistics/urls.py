from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'log_profilePage/', views.logistics_profilePage, name='LogProfilePage'),
]
