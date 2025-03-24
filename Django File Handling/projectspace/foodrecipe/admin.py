from django.contrib import admin
from foodrecipe.models import Recipe, Ingredients, Steps
# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    
    list_display = ['name','image']

@admin.register(Steps)
class StepsAdmin(admin.ModelAdmin):
    list_display = ['recipe','desc']

@admin.register(Ingredients)
class Ingredient(admin.ModelAdmin):
    list_display = ['recipe','name','quantity']