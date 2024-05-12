import django_filters
from .models import elstandardsFound

class elstandartsFoundFilter(django_filters.FilterSet):
    hujjat_raqami__contains = django_filters.CharFilter(field_name='document_number', lookup_expr='icontains', label='Hujjat raqami')
    kalit_soz__contains = django_filters.CharFilter(field_name='keyword', lookup_expr='icontains', label='Kalit so’z')
    hujjat_toifasi = django_filters.CharFilter(field_name='document_type', lookup_expr='exact', label='Hujjat toifasini tanlang')
    shartli_beligisi = django_filters.CharFilter(field_name='status', lookup_expr='exact', label='Shartli belgisi')
    hujjat_tasdiqlangan_yili = django_filters.NumberFilter(field_name='approved_year', lookup_expr='exact', label='Hujjat tasdiqlangan yili')

    class Meta:
        model = elstandardsFound
        fields = ['hujjat_raqami__contains', 'kalit_soz__contains', 'hujjat_toifasi', 'shartli_beligisi', 'hujjat_tasdiqlangan_yili']
