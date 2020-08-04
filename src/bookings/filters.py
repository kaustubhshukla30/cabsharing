from django.contrib.auth.models import User
import django_filters
from django_filters import DateRangeFilter,DateFilter
from .models import createbooking, Member



class BookingFilter(django_filters.FilterSet):
    destination = django_filters.CharFilter(lookup_expr='iexact')
    pickup = django_filters.CharFilter(lookup_expr='iexact')
    date = DateFilter(field_name='date',lookup_expr='iexact', label='Date (mm/dd/yyyy)')
    time = django_filters.TimeFilter(lookup_expr='lt')

    class Meta:
        model = createbooking
        fields = ['destination', 'pickup', 'date' , 'time' ]
