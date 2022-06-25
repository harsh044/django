from django.contrib import admin
from django.urls import path,include
from . import views 

# from Multiple_Users.multipleUser.accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('home', views.home,name="home"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('donar', views.donar,name="donar"),
    path('ngo', views.ngo,name="ngo"),
    path('accounts/', include('accounts.urls')),
]
