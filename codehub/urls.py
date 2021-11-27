from django.urls import path
from .views import ArticlesListView, ArticlesDetailView


urlpatterns = [
    path('', ArticlesListView.as_view(), name='Home'),
    path('article/<int:pk>/', ArticlesDetailView.as_view(), name='Detail'),
]