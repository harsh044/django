from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.Register,name='users'),
    path('/login',views.Login,name='login'),
    ]