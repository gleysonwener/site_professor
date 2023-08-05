from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'principal'

urlpatterns = [
    path('', views.home, name='home'),
    path('home_adm/', views.home_adm, name='home_adm'),    
]
