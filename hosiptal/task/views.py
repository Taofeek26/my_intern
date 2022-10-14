# core/views.py
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import Blog


class HomeView(ListView):
    template_name = 'home.html'
    queryset = Blog.objects.all()
    context_object_name = 'Blogs'
    paginate_by = 30


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content', 'category', 'summary', 'image', 'draft']
    template_name = 'add-blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CreateBlog, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class BlogView(ListView):
    template_name = 'blog.html'
    queryset = Blog.objects.all()
    context_object_name = 'Blogs'
    paginate_by = 30