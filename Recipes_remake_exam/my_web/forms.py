from django import forms

from Recipes_remake_exam.my_web.models import Recipe


class BaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class CreateRecipeForm(BaseForm):
    pass