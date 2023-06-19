from django.shortcuts import render

from Recipes_remake_exam.my_web.models import Recipe


def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    return render(request, 'create.html')


def edit_recipe(request, id):
    return render(request, 'edit.html')


def delete_recipe(request, id):
    return render(request, 'delete.html')


def details_recipe(request, id):
    return render(request, 'details.html')
