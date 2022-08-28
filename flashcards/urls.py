from django.contrib import main
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_decks, name='list_decks'),
]