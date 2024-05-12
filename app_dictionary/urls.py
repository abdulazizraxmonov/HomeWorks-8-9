from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DictionaryLanguagesViewSet, DictionaryViewSet, DictionaryListAPIView

router = DefaultRouter()
router.register(r'dictionarylanguages', DictionaryLanguagesViewSet)
router.register(r'dictionary', DictionaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', DictionaryListAPIView.as_view(), name='dictionary_list'),
]
