from importlib.resources import path
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_decks, name='list_decks'),
]