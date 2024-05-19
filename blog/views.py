from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView # новое
from django.urls import reverse_lazy # импортируем новые методы
from .models import Post, Category

from math import pi
import datetime

class HomePageView(ListView):
    model = Post
    template_name = 'charts.html'

class ChartsListView(ListView):
    model = Post
    template_name = 'charts.html'

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView): # новое
    model = Post
    template_name = 'post_detail.html'

class CategoryListView(ListView):
    model = Category
    template_name = "base.html"


class PostByCategoryView(ListView):
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Post.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category
        return context
def upload(request):
    
    if request.method == 'POST':
        image = request.FILES.get('image_upload')
        title = request.POST['title']

        return redirect('/')
    else:
        return redirect('/')