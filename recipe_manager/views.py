from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe

# display form and save new recipes
def add_recipe(request):
    if request.method == 'POST':        # check whether form submitted
        form = RecipeForm(request.POST) # create form containing submitted info

        if form.is_valid():     # validate input 
            form.save()         # save form to database
            return redirect('recipe_list')  # redirect user
    else:
        form = RecipeForm()     # create empty form 
    
    # display HTML template containing form
    return render(request, 'recipe_manager/add_recipe.html', {'form': form})

# display all saved recipes
def recipe_list(request):
    recipes = Recipe.objects.all()

    return render(request, 'recipe_manager/recipe_list.html', {'recipes': recipes})

# 
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    return render(request, 'recipe_manager/recipe_detail.html', {'recipe': recipe})

