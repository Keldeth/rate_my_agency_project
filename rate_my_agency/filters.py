import django_filters
from django_filters import CharFilter

from .models import *

class AgencyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label = "Name ", field_name='name', lookup_expr='icontains')
    
    class Meta:
        model = Agency
        fields = ['name',]

