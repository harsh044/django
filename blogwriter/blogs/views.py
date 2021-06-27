from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm,UpdateForm
from django import forms
from django.shortcuts import redirect, render
from django.db.models import Q


# Create your views here.

class PostView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']


class PostDetail(DetailView):
    model = Post
    template_name = 'PostDetail.html'


class AddPostview(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    redirect = "index.html"


class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('Post')


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('Post')


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('S')
        object_list = Post.objects.filter(Q(category=query))
        return object_list
