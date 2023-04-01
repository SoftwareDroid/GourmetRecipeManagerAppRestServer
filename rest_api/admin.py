from django.contrib import admin
from .gourmet_model import Recipe,Ingredients,Keylookup,PluginInfo, Shopcats,Unitdict,Categories, Info

# Register your models here.
# Relaventa Tabellen sind Recipe, Ingredients, Info und Categories

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Info)
admin.site.register(Categories)
