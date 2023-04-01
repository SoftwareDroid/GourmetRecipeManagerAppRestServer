from rest_framework import serializers
from .gourmet_model import Recipe

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title',"last_modified")