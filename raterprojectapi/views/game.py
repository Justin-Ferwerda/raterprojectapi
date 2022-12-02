from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game


class GameView(ViewSet):
  """Game Rater Games View"""
  
  def retrieve(self, request, pk):
    """Handles GET requests for single game"""
    game = Game.objects.get(pk=pk)
    serializer = GameSerializer(game)
    return Response(serializer.data)
  
  def list(self, request):
    """Handles GET requests for all games"""
    
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)
    
  def create(self, request):
    """Handles POST requests for game"""
    
    game = Game.objects.create(
      title=request.data["title"],
      description=request.data["description"],
      designer=request.data["designer"],
      year_released=request.data["year_released"],
      no_of_players=request.data["no_of_players"],
      time_to_play=request.data["time_to_play"],
      age_recommendation=request.data["age_recommendation"]
    )
    serializer = GameSerializer(game)
    return Response(serializer.data)
    
class GameSerializer(serializers.ModelSerializer):
  """JSON serializer for games"""
  
  class Meta:
    model = Game
    fields = ('id', 'title','description', 'designer', 'year_released', 'no_of_players', 'time_to_play', 'age_recommendation')
    depth = 1
    