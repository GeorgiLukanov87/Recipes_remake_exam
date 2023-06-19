from django.shortcuts import render, redirect

from Recipes_remake_exam.my_web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from Recipes_remake_exam.my_web.models import Recipe


def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {
        'form': form,

    }

    return render(request, 'create.html', context, )


def edit_recipe(request, id):
    recipe = Recipe.objects.filter(pk=id).get()

    if request.method == 'GET':
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'edit.html', context, )


def delete_recipe(request, id):
    recipe = Recipe.objects.filter(pk=id).get()

    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'delete.html', context, )


def details_recipe(request, id):
    return render(request, 'details.html')
