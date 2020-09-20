from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('example/', views.example, name = 'example'),
    path('countries/', views.countries, name = 'countries'),
    path('examples/', views.example2, name = 'examples'),




]
