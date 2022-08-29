from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_decks, name='list_decks'),
    path('decks/new', views.create_deck, name='create_deck'),
    path('decks/<int:pk>/', views.deck_detail, name='deck_detail'),
]