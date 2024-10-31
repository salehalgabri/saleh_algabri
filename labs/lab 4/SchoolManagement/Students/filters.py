import django_filters as filters
from .models import Students


class StudentsFilter(filters.FilterSet):
    class Meta:
        model = Students
        fields = '__all__'
        exclude=['status','reporet']