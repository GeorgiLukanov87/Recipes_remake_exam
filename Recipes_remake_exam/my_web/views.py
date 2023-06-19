from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def create_recipe(request):
    return render(request, 'create.html')


def edit_recipe(request, id):
    return render(request, 'edit.html')


def delete_recipe(request, id):
    return render(request, 'delete.html')


def details_recipe(request, id):
    return render(request, 'details.html')
