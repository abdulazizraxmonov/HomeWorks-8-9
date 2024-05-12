from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StandardViewSet, PhotoViewSet

router = DefaultRouter()
router.register(r'standards', StandardViewSet)
router.register(r'standarts/photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]