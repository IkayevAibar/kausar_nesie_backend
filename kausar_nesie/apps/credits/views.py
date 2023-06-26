from django.http import JsonResponse

from rest_framework import viewsets, permissions, status, filters

from django_filters.rest_framework import DjangoFilterBackend, IsoDateTimeFilter, DateFilter, LookupChoiceFilter
from django_filters import FilterSet, DateTimeFromToRangeFilter
from .serializers import *

class CreditFilter(FilterSet):
    date_range = DateTimeFromToRangeFilter(field_name='date_begin', lookup_expr='range')

    class Meta:
        model = Credit
        fields = ['date_range', 'date_begin', 'date_end', 'date_close', 'date_sign', 'credit_type', 'curr', 'status', 'depart', 'project_type', 'credit_source'\
            , 'credit_target', 'is_line', 'period_type', 'is_affiliated', 'is_rate_fixed', 'emp']

class CreditViewSet(viewsets.ModelViewSet):
    """Регистрация, Получение, Удаление, Изменение, Частичное Изменение"""
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = CreditFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['notes', 'num_dog', 'period_count', 'reason', 'client__individual_client__name', 'client__individual_client__surname'] 

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CreditGetSerializer
        return self.serializer_class


class CreditTreatmentViewSet(viewsets.ModelViewSet):
    queryset = CreditTreatments.objects.all()
    serializer_class = CreditTreatmentsSerializer
    permission_classes = [permissions.AllowAny]