from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('country/', views.country, name = 'country'),
    path('countries/', views.countries, name = 'countries'),




]
