from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReglamentViewSet

router = DefaultRouter()
router.register(r'reglaments', ReglamentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]