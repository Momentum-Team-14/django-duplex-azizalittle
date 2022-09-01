from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_decks, name='list_decks'),
    # deck paths
    path('decks/new', views.new_deck, name='new_deck'),
    path('decks/<int:pk>/', views.deck_detail, name='deck_detail'),
    path('decks/<int:pk>/edit/', views.edit_deck, name='edit_deck'),
    path('decks/<int:pk>/delete/', views.delete_deck, name='delete_deck'),
    # card paths
    path('decks/<int:pk>/add/', views.add_card, name='add_card'),
    path('decks/<int:deck_pk>/card/<int:card_pk>/edit/', views.edit_card, name='edit_card'),
    path('decks/<int:deck_pk>/card/<int:card_pk>/delete/', views.delete_card, name='delete_card'),
]