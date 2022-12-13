from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game, Category, GameCategory


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
    
    game = Game()
      
    game.title=request.data["title"]
    game.description=request.data["description"]
    game.designer=request.data["designer"]
    game.year_released=request.data["year_released"]
    game.no_of_players=request.data["no_of_players"]
    game.time_to_play=request.data["time_to_play"]
    game.age_recommendation=request.data["age_recommendation"]
    
    category_ids= request.data["category_ids"]
    
    categories = [Category.objects.get(pk=category_id) for category_id in category_ids]
    
    game.save()
    
    for category in categories:
      game_category = GameCategory(game=game, category=category)
      game_category.save()
      
    serializer = GameSerializer(game)
    return Response(serializer.data)
    
class GameSerializer(serializers.ModelSerializer):
  """JSON serializer for games"""
  
  class Meta:
    model = Game
    fields = ('id', 'title','description', 'designer', 'year_released', 'no_of_players', 'time_to_play', 'age_recommendation', 'average_rating')
    depth = 1
    