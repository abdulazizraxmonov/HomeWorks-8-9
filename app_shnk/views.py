from rest_framework import viewsets
from .models import Subsystem, Group, Document
from .serializers import SubsystemSerializer, GroupSerializer, DocumentSerializer

class SubsystemViewSet(viewsets.ModelViewSet):
    queryset = Subsystem.objects.all()
    serializer_class = SubsystemSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
