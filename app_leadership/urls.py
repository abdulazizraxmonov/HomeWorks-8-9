from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RahbariyatViewSet

router = DefaultRouter()
router.register(r'rahbariyat', RahbariyatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]