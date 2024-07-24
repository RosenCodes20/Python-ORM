from django.db import models
from django import forms

from FruitiPedia.fruits.models import Category, Fruit


class CreateCategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter category name'})}


class CategoryOriginalForm(CreateCategoryBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ""


class CreateFruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter the name of the fruit"}),
            "image_url": forms.TextInput(attrs={"placeholder": "Enter the url photo of the fruit"}),
            "description": forms.TextInput(attrs={"placeholder": "Enter the fruit description"}),
            "nutrition": forms.TextInput(attrs={"placeholder": "Enter the nutrition of the food"}),
        }


class CreateFruitOriginalForm(CreateFruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ""
            self.fields[field].error_messages["required"] = ""


class EditFruitForm(CreateFruitOriginalForm):
    pass


class DeleteFruitForm(CreateFruitOriginalForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
