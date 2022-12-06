from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Category, GameCategory, Game, PlayerReview, Player, PlayerRating

class GameRatingView(ViewSet):
  """handles all requests for ratings"""
  
  def create(self, request):
    """handles POST requests for game ratings"""
    
    game = Game.objects.get(pk=request.data["game"])
    player = Player.objects.get(uid=request.data["player"])
    
    review = PlayerRating.objects.create(
      game = game,
      player = player,
      rating = request.data["rating"]
    )
    serializer = RatingSerializer(review)
    return Response(serializer.data)
  
class RatingSerializer(serializers.ModelSerializer):
  """JSON serializer for Player Ratings"""
  
  class Meta:
    model = PlayerRating
    fields = ('id', 'player', 'game', 'rating')
