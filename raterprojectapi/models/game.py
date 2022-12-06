from django.db import models

class Game(models.Model):
  
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=50)
  designer = models.CharField(max_length=50)
  year_released = models.IntegerField()
  no_of_players = models.IntegerField()
  time_to_play = models.CharField(max_length=50)
  age_recommendation = models.IntegerField()

  @property 
  def average_rating(self):
    """average rating for each game"""
    ratings = self.ratings.all()
    
    total_rating = 0
    for rating in ratings:
      total_rating += rating.rating
      
    if len(ratings):
      average_rating = total_rating/len(ratings)
      return average_rating
    
