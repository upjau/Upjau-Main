from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'farm-land/', views.farm_land, name='farm_land'),

    # HomePage
    url(r'homepage/', views.farmer_dashboard, name='FDashboard'),

    # Dasboard
    url(r'profile/', views.farmer_profilePage, name='ProfilePage'),
    url(r'land/', views.farmer_landPage, name='LandPage'),
    url(r'sell/', views.farmer_sellHarvestPage, name='SellHarvestPage'),

    # SepDB
    url(r'add/', views.farmer_addland, name='AddLand'),
]

