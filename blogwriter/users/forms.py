from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signuuser(UserCreationForm):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control mt-3','placeholder':'Enter Your name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mt-3','placeholder':'Enter Your Emai-ID'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    def __init__(self,*args, **kwargs):
        super(signuuser,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] ='form-control my-3'
        self.fields['username'].widget.attrs['placeholder'] ='Username'
        self.fields['password1'].widget.attrs['class'] ='form-control my-3'
        self.fields['password1'].widget.attrs['placeholder'] ='Password'
        self.fields['password2'].widget.attrs['class'] ='form-control my-3'
        self.fields['password2'].widget.attrs['placeholder'] ='Password Again'


