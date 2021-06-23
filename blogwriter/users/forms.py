from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signuuser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password', 'password1']