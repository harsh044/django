from django.shortcuts import render
from django.http import HttpResponse
from Blogs.models import Post
from django.views.generic import ListView
# from Blogs.views import 

# Create your views here.
# def home(request):
#     post=Post.objects.all()[:5]
#     return render(request,"index.html", {data:"post"})

class PostView(ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.order_by('-id')[:4]