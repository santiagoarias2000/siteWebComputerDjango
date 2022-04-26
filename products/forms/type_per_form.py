from django import forms
from products.models import Type_peripheral


class type_per_form(forms.ModelForm):
    class Meta:
        model = Type_peripheral
        fields = [
            'name',
        ]
