from django.db import models
from .player import Player
from .game import Game

class PlayerPictures(models.Model):
  
  game = models.ForeignKey(Game, on_delete=models.CASCADE)
  player = models.ForeignKey(Player, on_delete=models.CASCADE)
  picture = models.CharField(max_length=50)
  