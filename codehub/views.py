from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Articles


class ArticlesListView(ListView):
    model = Articles
    template_name = 'codehub/base.html'
    context_object_name = 'Articles'
    ordering = ['-date']


class ArticlesDetailView(DetailView):
    model = Articles


class ArticlesCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



