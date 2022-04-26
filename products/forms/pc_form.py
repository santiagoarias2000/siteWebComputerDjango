from django import forms
from products.models import Pc_character, Pc


class pc_form(forms.ModelForm):
    class Meta:
        model = Pc_character
        fields = [
            'pcs',
            'peripherals',
            'board',
            'monitors',
            'processor',
            'memory',
            'storage',
            'refrigeration',
        ]


class pcs_form(forms.ModelForm):
    class Meta:
        model = Pc
        fields = [
            'products'
        ]
