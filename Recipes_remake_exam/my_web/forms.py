from django import forms

from Recipes_remake_exam.my_web.models import Recipe


class BaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        labels = {
            'title': 'Title',
            'image_url': 'Image URL',
            'description': 'Description',
            'ingredients': 'Ingredients',
            'time': 'Time(Minutes)',
        }


class CreateRecipeForm(BaseForm):
    pass


class EditRecipeForm(BaseForm):
    pass


class DeleteRecipeForm(BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False
