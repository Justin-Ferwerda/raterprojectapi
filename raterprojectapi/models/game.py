from django.db import models

class Game(models.Model):
  
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=50)
  designer = models.CharField(max_length=50)
  year_released = models.IntegerField()
  no_of_players = models.IntegerField()
  time_to_play = models.CharField(max_length=50)
  age_recommendation = models.IntegerField()
