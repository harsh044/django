from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import DonarSignUpForm,NgoSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def register(request):
    return render(request, '../templates/register.html')

class donar_register(CreateView):
    model = User
    form_class = DonarSignUpForm
    template_name = 'donar_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class ngo_register(CreateView):
    model = User
    form_class = NgoSignUpForm
    template_name = 'ngo_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_donar :
                login(request,user)
                return redirect('donar')
            elif user is not None and user.is_ngo:
                login(request,user)
                return redirect('ngo')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('index')