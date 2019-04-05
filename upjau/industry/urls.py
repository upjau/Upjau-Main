from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'industryProfile/', views.industry_profile, name='industryProfilePage'),

    url(r'availableProduce/', views.industry_produceAvailable, name='industryPorduceAvailable'),

    url(r'buyLand/', views.industry_buyLand, name='buyLand'),

    url(r'produce/', views.industry_produce, name='produceRecord'),
]
