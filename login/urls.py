from django.contrib import admin
from django.urls import path, re_path, include

from login import views

urlpatterns = [
    path('', include('artistas.urls')),
    path('registrarse', views.registerUser, name = 'register'),
    path('', views.loginPage, name = 'login'),
]