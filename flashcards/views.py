from django.shortcuts import render, get_object_or_404
from . models import Card, Deck
from flashcards.forms import CardForm, DeckForm
from django.shortcuts import redirect

# show list of deck names
def list_decks(request):
    decks = Deck.objects.all()
    return render(request, 'flashcards/list_decks.html', {'decks': decks})

# create a new deck
def new_deck(request):
    if request.method == 'POST':
        deck_form = DeckForm(request.POST)
        if deck_form.is_valid():
            deck = deck_form.save()
            return redirect('deck_detail', pk=deck.pk)
    deck_form = DeckForm()
    return render(request, 'flashcards/new_deck.html', {'deck_form': deck_form})

# should show all the cards in the selected deck
def deck_detail(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    cards = deck.cards.all()
    return render(request, 'flashcards/deck_detail.html', {'deck': deck, 'cards': deck.cards.all()})

# edit deck (name)
def edit_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        deck_form = DeckForm(request.POST, instance=deck)
        if deck_form.is_valid():
            deck = deck_form.save()
            return redirect('deck_detail', pk=deck.pk)
    else:
        deck_form = DeckForm(instance=deck)
    return render(request, 'flashcards/edit_deck.html', {'deck_form': deck_form})

# delete deck
def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        deck.delete()
        return redirect('list_decks')
    return render(request, 'flashcards/delete_deck.html', {'deck':deck})


# add a new card to the selected deck
def add_card(request, pk=None):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        card_form = CardForm(request.POST)
        if card_form.is_valid():
            card = card_form.save(commit=False)
            card.deck = deck
            card.save()
            return redirect('deck_detail', pk=pk)
    else:
        card_form = CardForm()
    return render(request, 'flashcards/add_card.html', {'card_form': card_form})

