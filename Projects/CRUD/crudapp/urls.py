# crudapp/urls.py

from django.urls import path
from .views import BlogPostListView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='post-list'),
    path('create/', BlogPostCreateView.as_view(), name='post-create'),
    path('update/<int:pk>/', BlogPostUpdateView.as_view(), name='post-update'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='post-delete'),
]
