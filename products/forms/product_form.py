from django import forms
from products.models import Products


class product_form(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['name', 'description_general', 'image', 'price']
