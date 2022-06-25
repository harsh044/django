from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    return render(request,"home.html")

# registration function
def signup(request):
    if request.method== 'POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        email =request.POST['email']
        username =request.POST['username']
        password1 =request.POST['password1']
        password2 =request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exists')
                # print("Username Exists")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                #print("email Exists")
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.success(request, 'User created Successfully')
                #print('user Created')
                return redirect('signin')
        else:
            messages.info(request, 'Password and Confirm password are Not Macthed')
            #print("Password Not Matched")

        return redirect('signup')
    else:
        return render(request,"signup.html")

# login function
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("Successfull login")
            return redirect(request,'signin')
        else:
            print("Invalid")
            messages.info(request,"Invalid crentials")
            return redirect(request,'signin')
    else:
        return render(request,'signin.html')


def logout(request):
    auth.logout(request)
    return redirect('home')