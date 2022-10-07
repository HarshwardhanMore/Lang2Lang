
from django.contrib import admin
from django.urls import path
from app import urls
from . import views

urlpatterns = [
    path('', views.home)
]