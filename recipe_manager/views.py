from django.shortcuts import render
from .forms import RecipeForm

# create view
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
