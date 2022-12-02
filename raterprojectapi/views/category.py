from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Category

class CategoryView(ViewSet):
  """Handles requests for categories"""
  
  def list(self, request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

class CategorySerializer(serializers.ModelSerializer):
  """JSON serializer for categories"""
  
  class Meta:
    model: Category
    fields= ('id', 'label')
  