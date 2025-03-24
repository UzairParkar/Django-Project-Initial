from django.urls import path
from foodrecipe import views


urlpatterns = [
    path('', views.create_recipe, name='create_recipe'),
    path('add-steps/<int:recipe_id>/', views.add_steps, name='add_steps'),
    path('add-ingredients/<int:recipe_id>/', views.add_ingredients, name='add_ingredients'),
    path('delete-recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('read-recipe/<int:recipe_id>/', views.read_recipe, name='read_recipe')]