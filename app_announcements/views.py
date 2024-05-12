from rest_framework import generics
from .models import AllAnnouncements
from .serializers import AllAnnouncementsSerializer

class AllAnnouncementsListCreate(generics.ListCreateAPIView):
    queryset = AllAnnouncements.objects.all()
    serializer_class = AllAnnouncementsSerializer

class AllAnnouncementsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AllAnnouncements.objects.all()
    serializer_class = AllAnnouncementsSerializer