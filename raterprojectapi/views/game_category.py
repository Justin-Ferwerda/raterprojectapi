from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Category, GameCategory, Game

class GameCategoryView(ViewSet):
  """handles requests for GameCategory entity"""
  
  def list(self, request):
    """handles GET requests for game categories"""
    game_categories = GameCategory.objects.all()
    serializer = GameCategorySerializer(game_categories, many=True)
    return Response(serializer.data)
    
  def create(self, request):
    """handle POST operations for game categories"""
    
    game = Game.objects.get(pk=request.data["game"])
    category = Category.objects.get(pk=request.data["category"])
    
    game_category = GameCategory.objects.create(
      game = game,
      category = category
    )
    
    serializer = GameCategorySerializer(game_category)
    return Response(serializer.data)
    
class GameCategorySerializer(serializers.ModelSerializer):
  """JSON serializer for game categories"""
  
  class Meta:
    model = GameCategory
    fields= ('id', 'game', 'category')
    depth = 1
