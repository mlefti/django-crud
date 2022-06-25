from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from .models import Post
# from django.contrib.auth import reverse_lazy

# Create your views here.


class PostListView():
    model=Post
class PostCreateView():
    model=Post
    fields="__all__"
    success_url=reverse_lazy("blog:all")
class PostDetailView():
    model = Post
class PostUpdateView():
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
class PostDeleteView():
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
