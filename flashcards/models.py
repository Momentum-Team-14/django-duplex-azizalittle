from importlib import machinery
from django.contrib.auth.models import User as BaseUser
from django.db import models


# Create your models here.
class User(BaseUser):
    # could add custom user attributes here
    pass

class Card(models.Model):
    deck = models.CharField(max_length=200)
    prompt = models.CharField(max_length=200)
    answer = models.TextField

    def __str__(self):
        return f'{self.deck}'