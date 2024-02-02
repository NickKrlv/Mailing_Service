from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

app_name = 'blog'

urlpatterns = [
    path('blogpost_list/', BlogPostListView.as_view(), name='blogpost_list'),
    path('create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('edit/<slug:slug>', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('delete/<slug:slug>', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]
