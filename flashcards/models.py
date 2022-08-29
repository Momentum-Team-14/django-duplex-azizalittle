from django.contrib.auth.models import User as BaseUser
from django.db import models


# Create your models here.
class User(BaseUser):
    # could add custom user attributes here
    pass

class Card(models.Model):
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE, related_name='cards')
    prompt = models.CharField(max_length=200)
    answer = models.TextField()
    

    def __str__(self):
        return f'{self.prompt}: {self.answer}'

class Deck(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'
