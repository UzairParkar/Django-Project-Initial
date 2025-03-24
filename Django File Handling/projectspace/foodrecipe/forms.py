from django import forms
from .models import Recipe, Steps, Ingredients

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'image']

class StepForm(forms.ModelForm):
    class Meta:
        model = Steps
        fields = ['desc']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name', 'quantity']