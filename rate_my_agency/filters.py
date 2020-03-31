import django_filters
from django_filters import CharFilter

from .models import *

class AgencyFilter(django_filters.FilterSet):
    agencyName = django_filters.CharFilter(label = "Name ", field_name='agencyName', lookup_expr='icontains')
    
    class Meta:
        model = Agency
        fields = ['agencyName',]

