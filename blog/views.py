from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Post, Author

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        return Post.objects.order_by('-created_date')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'