from favourite.models import Favourite
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class FavouriteListCreateAPISerializer(ModelSerializer):
  class Meta:
    model =  Favourite
    fields = '__all__'
    
  def validate(self, attrs):
    
    queryset = Favourite.objects.filter(user=attrs['user'], post=attrs['post'])
    if queryset.exists():
      raise serializers.ValidationError("This is an existing favourite")
    return attrs    
    
class FavouriteAPISerializer(ModelSerializer):
  class Meta:
    model =  Favourite
    fields = '__all__'