from django.shortcuts import render

# Create your views here.
from .gourmet_model import Recipe
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.generics import(
                                        ListCreateAPIView,
                                        RetrieveUpdateDestroyAPIView
       )


from .permissions import CustomDjangoModelPermissions


from .serializers import RecipeSerializer
from .models import Recipe2


#class HeroViewSet(viewsets.ModelViewSet):
#    queryset = Recipe2.objects.all().order_by('name')
#    serializer_class = RecipeSerializer

class RecipesView(viewsets.ModelViewSet):
    permission_classes = (CustomDjangoModelPermissions, )
    queryset = Recipe.objects.all().order_by('title')
    serializer_class = RecipeSerializer