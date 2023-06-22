from django import forms
from .models import Category, Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['category_id', 'title', 'ingredients',
                  'directions']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

