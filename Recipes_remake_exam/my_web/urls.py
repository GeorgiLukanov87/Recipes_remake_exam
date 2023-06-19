from django.urls import path, include

from Recipes_remake_exam.my_web.views import index, create_recipe, edit_recipe, delete_recipe, details_recipe

urlpatterns = (
    path('', index, name='index'),
    path('create/', create_recipe, name='create-recipe'),
    path('edit/<int:id>/', edit_recipe, name='edit-recipe'),
    path('delete/<int:id>/', delete_recipe, name='delete-recipe'),
    path('details/<int:id>/', details_recipe, name='details_recipe'),
)
"""
/' - home page
/create' - create recipe page
/edit/:id' - edit recipe page
/delete/:id' - delete recipe page
/details/:id' - recipe details page
"""
