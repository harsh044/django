from django.shortcuts import render, redirect
from .forms import signuuser
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# registration
def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = signuuser()
        if request.method == "POST":
            form = signuuser(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account Has Been created-" + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'signup.html', context)

# login
def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Account does not exist")

        context = {}
        return render(request, 'login.html', context)
