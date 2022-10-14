# core/urls.py
from django.urls import path, include

from .views import HomeView, CreateBlog, BlogView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-blog', CreateBlog.as_view(), name='add-blog'),
    path('Blog', BlogView.as_view(), name='Blog'),
]