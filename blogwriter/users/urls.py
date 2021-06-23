from django.urls import path
from . import views

#from .views import UsersRegisterView,authenticate
urlpatterns = [
    path('',views.Register,name='users'),
    path('/login',views.Login,name='login'),
    ]