from django import forms
from products.models import Peripheral


class peripheral_form(forms.ModelForm):
    class Meta:
        model = Peripheral
        fields = ['products',
                  'type_peripherals',
                  'description',
                  'link_website',
                  ]
