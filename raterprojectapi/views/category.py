from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Category, GameCategory, Game

class CategoryView(ViewSet):
  """Handles requests for categories"""
  
  def list(self, request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
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

class CategorySerializer(serializers.ModelSerializer):
  """JSON serializer for categories"""
  
  class Meta:
    model = Category
    fields= ('id', 'label')
    
class GameCategorySerializer(serializers.ModelSerializer):
  """JSON serializer for game categories"""
  
  class Meta:
    model = GameCategory
    fields= ('id', 'game', 'category')
  