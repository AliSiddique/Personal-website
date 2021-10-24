import django_filters

from .models import job

class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = job
        fields = '__all__'
        exclude = ['date_posted', 'pay', 'content', 'Contact', 'Website', 'author']
