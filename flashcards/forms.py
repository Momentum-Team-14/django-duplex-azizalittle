from django import forms
from .models import Card, Deck

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('prompt', 'answer')


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ('title',)

