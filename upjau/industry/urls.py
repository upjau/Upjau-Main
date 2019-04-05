from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'industryProfile/', views.industry_profile, name='industryProfilePage'),
]
