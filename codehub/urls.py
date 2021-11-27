from django.urls import path
from .views import ArticlesListView, ArticlesDetailView, ArticlesCreateView, ArticlesUpdateView, ArticlesDeleteView


urlpatterns = [
    path('', ArticlesListView.as_view(), name='Home'),
    path('article/<int:pk>/', ArticlesDetailView.as_view(), name='Detail'),
    path('article/<int:pk>/update', ArticlesUpdateView.as_view(), name='Update'),
    path('article/<int:pk>/delete/', ArticlesDeleteView.as_view(), name="Delete"),
    path('article/create/', ArticlesCreateView.as_view(), name="Create")
]