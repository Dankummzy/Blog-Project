from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class ArticlesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        articles = self.get_object()
        if self.request.user == articles.author:
            return True
        return False


class ArticlesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    success_url = '/'

    def test_func(self):
        articles = self.get_object()
        if self.request.user == articles.author:
            return True
        return False



