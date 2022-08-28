from django.shortcuts import render, get_list_or_404

import flashcards
from . models import Card

# Create your views here.
def list_deck(request):
    decks = Card.deck.title
    return render(request, 'flashcards/list_decks.html', {'decks':decks})