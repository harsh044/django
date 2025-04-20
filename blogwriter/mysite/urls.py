from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostView
from django.views.static import serve
from django.urls import re_path as url
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PostView.as_view(), name="home"),
    path('blog',include('blogs.urls')),
    path('users',include('django.contrib.auth.urls')),
    path('users',include('users.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

