from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signuuser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password', 'password1']

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        #     'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email'}),
        #     'password': forms.TextInput(attrs={'type': 'pas', 'class': 'form-control', 'placeholder': 'password'}),
        #     'password1': forms.TextInput(attrs={'type': 'pas', 'class': 'form-control', 'placeholder': 'password Again'}),
        # }
