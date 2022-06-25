# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import User

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Donar,Ngo


class DonarSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_donar = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        donar = Donar.objects.create(user=user)
        donar.phone_number=self.cleaned_data.get('phone_number')
        donar.save()
        return user

class NgoSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    ngo_name = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_ngo = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        ngo = Ngo.objects.create(user=user)
        ngo.phone_number=self.cleaned_data.get('phone_number')
        ngo.save()
        return user

# class LoginForm(forms.Form):
#     username =forms.CharField()

#     password =forms.CharField()

# class RegisterForm(UserCreationForm):
#     email =forms.CharField()

#     username =forms.CharField()

#     password1 =forms.CharField()

#     password2 =forms.CharField()

#     class Meta:
#         model = User
#         fields=('email','username','password1','password2','is_donar','is_ngo')
