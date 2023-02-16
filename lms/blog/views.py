from django.shortcuts import render
from django.views import generic
from .models import Post , Book
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=0).order_by('-created_on')
    template_name = 'blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BookList(generic.ListView):
    queryset = Book.objects.filter(status=0).order_by('-created_on')
    template_name = 'book/index.html'