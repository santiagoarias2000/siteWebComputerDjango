from django import forms
from products.models import Monitor_character, Monitor


class monitor_form(forms.ModelForm):
    class Meta:
        model = Monitor_character
        fields = ['monitors', 'size', 'hz', 'quality']


class monitors_form(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = [
            'products'
        ]
