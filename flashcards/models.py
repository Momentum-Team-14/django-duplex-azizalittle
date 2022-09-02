from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    # could add custom user attributes here
    pass

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE, related_name='cards')
    prompt = models.CharField(max_length=200)
    answer = models.TextField()
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )

    def __str__(self):
        return self.prompt

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]
        if new_box in BOXES:
            self.box = new_box
            self.save()
        return self


class Deck(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'
