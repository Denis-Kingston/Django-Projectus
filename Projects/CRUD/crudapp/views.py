# crudapp/views.py

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'crudapp/list.html'
    context_object_name = 'posts'

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'crudapp/create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'crudapp/update.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'crudapp/delete.html'
    success_url = reverse_lazy('post-list')
