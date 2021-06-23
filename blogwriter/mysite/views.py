from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Post
from django.views.generic import ListView


class PostView(ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.order_by('-id')[:4]