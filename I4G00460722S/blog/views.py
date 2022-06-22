from django.shortcuts import render
from msilib.schema import ListView
from django.urls import reverse_lazy

from blog.models import Post
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
class PostListView(ListView):
    model = Post
    
class PostCtreateView(CreateView):
    model: Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
    
class PostDetailView(DetailView):
    model = Post
    
class PostUpdateView(UpdateView):
    model: Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
    
class PostDeleteView(DeleteView):
    model: Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
    