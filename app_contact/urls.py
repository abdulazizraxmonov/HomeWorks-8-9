# Ваш файл urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InquiryViewSet

router = DefaultRouter()
router.register(r'contact', InquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
