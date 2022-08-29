from django.shortcuts import render, get_list_or_404
from . models import Card
from flashcards.forms import CardForm
from django.shortcuts import redirect

# Create your views here.
def list_decks(request):
    decks = Card.objects.all()
    return render(request, 'flashcards/list_decks.html', {'decks': decks})

# I think I need to create an empty list called deck so all the added cards can be added to it. But what does that mean for the Card model?
def create_deck(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save()
            return redirect('list_decks')
    form = CardForm()
    return render(request, 'deck/create_deck.html', {'form': form})

# this is where i think that list will be useful since each deck is a list of cards
def deck_detail(request, pk):
    deck = get_list_or_404(Card, pk=pk)
    return render(request, 'decks/deck_detail.html', {'deck': deck})
