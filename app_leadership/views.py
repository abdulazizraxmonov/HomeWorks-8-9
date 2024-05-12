from rest_framework import viewsets
from .models import Rahbariyat
from .serializers import RahbariyatSerializer

class RahbariyatViewSet(viewsets.ModelViewSet):
    queryset = Rahbariyat.objects.all()
    serializer_class = RahbariyatSerializer