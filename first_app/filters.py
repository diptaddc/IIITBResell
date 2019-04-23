import django_filters

from .models import Product_Details

class UserFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product_Details
        fields = ['Category']
