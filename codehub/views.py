from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articles


class ArticlesListView(ListView):
    model = Articles
    template_name = 'codehub/base.html'
    context_object_name = 'Articles'
    ordering = ['-date']


class ArticlesDetailView(DetailView):
    model = Articles
