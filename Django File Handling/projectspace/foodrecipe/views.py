from django.shortcuts import render, redirect
from .models import Recipe, Steps, Ingredients
from .forms import RecipeForm, StepForm, IngredientForm
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

def create_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe = recipe_form.save()
            return redirect('add_steps', recipe_id=recipe.id)
    else:
        recipe_form = RecipeForm()

    recipes = Recipe.objects.all()
    return render(request, 'create_recipe.html', {'recipe_form': recipe_form, 'recipes': recipes})


def add_steps(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        step_form = StepForm(request.POST)
        if step_form.is_valid():
            step = step_form.save(commit=False)
            step.recipe = recipe
            step.save()
            return redirect('add_steps', recipe_id=recipe.id)
    else:
        step_form = StepForm()


    steps = recipe.steps.all()
    return render(request, 'add_steps.html', {
        'recipe': recipe,
        'step_form': step_form,
        'steps': steps,
    })

def add_ingredients(request, recipe_id):
  
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
            ingredient = ingredient_form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('add_ingredients', recipe_id=recipe.id)
    else:
        ingredient_form = IngredientForm()


    ingredients = recipe.ingredients.all()
    return render(request, 'add_ingredients.html', {
        'recipe': recipe,
        'ingredient_form': ingredient_form,
        'ingredients': ingredients,
    })
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    
    return redirect(reverse('create_recipe'))


def read_recipe(request, recipe_id):

    recipe = get_object_or_404(Recipe, id=recipe_id)

    steps = recipe.steps.all()
    ingredients = recipe.ingredients.all()

    return render(request, 'read_recipe.html', {
        'recipe': recipe,
        'steps': steps,
        'ingredients': ingredients,
    })