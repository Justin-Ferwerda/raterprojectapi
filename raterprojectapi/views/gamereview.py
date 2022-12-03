from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Category, GameCategory, Game, PlayerReview, Player

class GameReviewView(ViewSet):
  """Handles requests for Game Reviews"""
  
  def list(self, request):
    """handles GET requests for reviews"""
    reviews = PlayerReview.objects.all()
    serializer = ReviewCategorySerializer(reviews)
    return Response(serializer.data)
  
  def create(self, request):
    """handles POST requests for reviews"""
    
    game = Game.objects.get(pk=request.data["game"])
    player = Player.objects.get(uid=request.data["uid"])
    
    review = PlayerReview.objects.create(
      game = game,
      player = player,
      review = request.data["review"]
    )
    serializer = ReviewCategorySerializer(review)
    return Response(serializer.data)
  
class ReviewCategorySerializer(serializers.ModelSerializer):
  """review serializer"""
  
  class Meta:
    model = PlayerReview
    fields = ('game', 'player', 'review')
