from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls), #username=admin, password=admin
    path('', include("signup_signin.urls")),
]
