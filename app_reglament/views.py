from rest_framework import viewsets
from .models import Reglament
from .serializers import ReglamentSerializer

class ReglamentViewSet(viewsets.ModelViewSet):
    queryset = Reglament.objects.all()
    serializer_class = ReglamentSerializer