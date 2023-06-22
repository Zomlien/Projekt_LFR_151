from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Category
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def category_list(request):
    categories = Category.objects.all()
    return render(request, "category_list.html", {'categories': categories})


def recipe_list(request):
    query = request.GET.get('search', None)
    category_id = request.GET.get('category', None)
    recipes = Recipe.objects.all()
    if query:
        recipes = recipes.filter(title__icontains=query)
    if category_id:
        recipes = recipes.filter(category_id=category_id)
    recipes = recipes.prefetch_related('category_id')
    categories = Category.objects.all()
    return render(request, "recipe_list.html", {'recipes': recipes, 'categories': categories})



def recipe_detail(request, pk):
    recipe_obj = Recipe.objects.get(pk=pk)
    context = {
        "recipe": recipe_obj,
    }
    return render(request, "recipe_detail.html", context)


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.creator = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_create.html', {'form': form})


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if not request.user.is_superuser and request.user != recipe.creator:
        raise Http404
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_edit.html', {'form': form})


@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if not request.user.is_superuser and request.user != recipe.creator:
        raise Http404
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return redirect('recipe_detail', pk=recipe.pk)


def home(request):
    return render(request, 'home.html')
