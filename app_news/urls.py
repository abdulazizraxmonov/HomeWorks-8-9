from django.urls import path
from .views import NewsListCreate, NewsRetrieveUpdateDestroy

urlpatterns = [
    path('news/', NewsListCreate.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsRetrieveUpdateDestroy.as_view(), name='news-detail'),
]