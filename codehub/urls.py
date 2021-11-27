from django.urls import path
from .views import ArticlesListView, ArticlesDetailView, ArticlesCreateView


urlpatterns = [
    path('', ArticlesListView.as_view(), name='Home'),
    path('article/<int:pk>/', ArticlesDetailView.as_view(), name='Detail'),
    path('article/create/', ArticlesCreateView.as_view(), name="Create")
]