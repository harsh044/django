from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, '../templates/index.html')

def home(request):
    html = "<html><body>Home Page</body></html>" 
    return HttpResponse(html)

def about(request):
    html = "<html><body>About US Page</body></html>"
    return HttpResponse(html)

def contact(request):
    html = "<html><body>Contact Page</body></html>"
    return HttpResponse(html)

@login_required
def donar(request):
    return render(request, '../templates/donar.html')

@login_required
def ngo(request):
    return render(request, '../templates/ngo.html')
