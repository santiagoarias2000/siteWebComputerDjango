from django import forms
from products.models import Laptops_character, Laptop


class laptop_form(forms.ModelForm):
    class Meta:
        model = Laptops_character
        fields = [
            'laptops',
            'graphic_card',
            'keyboard',
            'display',
            'processor',
            'memory',
            'storage',
            'warranty',
        ]


class laptops_form(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = [
            'products'
        ]
