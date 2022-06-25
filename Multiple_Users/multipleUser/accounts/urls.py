from django.urls import path
from . import views


urlpatterns = [
    path('register',views.register, name='register'),
     path('donar_register/',views.donar_register.as_view(), name='donar_register'),
     path('ngo_register/',views.ngo_register.as_view(), name='ngo_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]