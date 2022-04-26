from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class customer_form(UserCreationForm):
    username = forms.CharField(label="Username", required=True, max_length=25,
                               widget=forms.TextInput(attrs={'placeholder': 'Username:'}))
    first_name = forms.CharField(label="first name", required=True, max_length=25,
                                 widget=forms.TextInput(attrs={'placeholder': 'First name:'}))
    last_name = forms.CharField(label="last name", required=True, max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': 'Last name:'}))
    email = forms.CharField(label="Email", required=True, max_length=25,
                            widget=forms.TextInput(attrs={'placeholder': 'Email:'}))
    password1 = forms.CharField(label="password1", required=True, max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': 'Password:', 'type': 'password'}))
    password2 = forms.CharField(label="password2", required=True, max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': 'Password confirm:', 'type': 'password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k: "" for k in fields}


class superuser_form(UserCreationForm):
    username = forms.CharField(label="Username", required=True, max_length=25,
                               widget=forms.TextInput(attrs={'placeholder': 'Username:'}))
    first_name = forms.CharField(label="first name", required=True, max_length=25,
                                 widget=forms.TextInput(attrs={'placeholder': 'First name:'}))
    last_name = forms.CharField(label="last name", required=True, max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': 'Last name:'}))
    email = forms.CharField(label="Email", required=True, max_length=25,
                            widget=forms.TextInput(attrs={'placeholder': 'Email:'}))
    password1 = forms.CharField(label="password1", required=True, max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': 'Password:', 'type': 'password'}))
    password2 = forms.CharField(label="password2", required=True, max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': 'Password confirm:', 'type': 'password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'is_superuser',
            'is_staff',
        ]
        help_texts = {k: "" for k in fields}
