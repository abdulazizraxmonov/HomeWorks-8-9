import django_filters
from .models import Dictionary

class DictionaryFilter(django_filters.FilterSet):
    language = django_filters.CharFilter(field_name='language__language_name', lookup_expr='icontains')
    code = django_filters.CharFilter(field_name='code', lookup_expr='icontains')

    class Meta:
        model = Dictionary
        fields = ['language', 'code', 'word']