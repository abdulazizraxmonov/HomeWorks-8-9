from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, pagination
from .models import elstandardsFound, elstandardsFoundPhoto
from .serializers import ElStandardFoundSerializer, elstandartsFoundPhotoSerializer
from .filters import elstandartsFoundFilter

# Custom pagination class for navigation
class CustomPagination(pagination.PageNumberPagination):
    page_size = 10  # Set the number of items per page
    page_query_param = 'page'  # Customize the page query parameter name
    page_size_query_param = 'page_size'  # Customize the page size query parameter name
    max_page_size = 1000  # Set the maximum page size

class StandardListView(generics.ListCreateAPIView):
    queryset = elstandardsFound.objects.all()
    serializer_class = ElStandardFoundSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = elstandartsFoundFilter
    pagination_class = CustomPagination  # Use custom pagination class

class StandardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = elstandardsFound.objects.all()
    serializer_class = ElStandardFoundSerializer

class elstandartsFoundPhotoListView(generics.ListCreateAPIView):
    queryset = elstandardsFoundPhoto.objects.all()
    serializer_class = elstandartsFoundPhotoSerializer
    pagination_class = CustomPagination  # Use custom pagination class

class elstandartsFoundPhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = elstandardsFoundPhoto.objects.all()
    serializer_class = elstandartsFoundPhotoSerializer
