import django_filters
from .models import Bike

class BikeFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    brand = django_filters.CharFilter(field_name="brand", lookup_expr='icontains')
    rating = django_filters.NumberFilter(field_name="rating", lookup_expr='gte')

    class Meta:
        model = Bike
        fields = ['brand', 'rating', 'release_date']
