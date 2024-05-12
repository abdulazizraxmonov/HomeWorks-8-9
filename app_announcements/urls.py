from django.urls import path
from .views import AllAnnouncementsListCreate, AllAnnouncementsRetrieveUpdateDestroy

urlpatterns = [
    path('announcements/', AllAnnouncementsListCreate.as_view(), name='announcements-list'),
    path('announcements/<int:pk>/', AllAnnouncementsRetrieveUpdateDestroy.as_view(), name='announcements-detail'),
]