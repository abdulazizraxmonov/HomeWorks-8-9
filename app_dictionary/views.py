from rest_framework import viewsets, pagination, generics
from .models import DictionaryLanguages, Dictionary
from .serializers import DictionaryLanguagesSerializer, DictionarySerializer
from .filters import DictionaryFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import DictionaryFilter

class DictionaryLanguagesViewSet(viewsets.ModelViewSet):
    queryset = DictionaryLanguages.objects.all()
    serializer_class = DictionaryLanguagesSerializer
    pagination_class = pagination.PageNumberPagination

class DictionaryViewSet(viewsets.ModelViewSet):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    pagination_class = pagination.PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = DictionaryFilter


class DictionaryListAPIView(generics.ListAPIView):
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DictionaryFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', None)
        if search_term:
            queryset = queryset.filter(word__icontains=search_term)
        return queryset
