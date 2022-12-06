from django.db import models
from .player import Player
from .game import Game

class PlayerRating(models.Model):
  
  game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="ratings")
  player = models.ForeignKey(Player, on_delete=models.CASCADE)
  rating = models.FloatField()
  
  
  