from django.http import JsonResponse

from rest_framework import viewsets, permissions, status, filters

from django_filters.rest_framework import DjangoFilterBackend, IsoDateTimeFilter, DateFilter, LookupChoiceFilter, CharFilter
from django_filters import FilterSet, DateTimeFromToRangeFilter
from .serializers import *

class CreditFilter(FilterSet):
    num_dog = CharFilter()
    client__individual_client__rnn = CharFilter()
    client__individual_client__iin = CharFilter()
    client = CharFilter()
    # period_count = CharFilter()
    # reason = CharFilter()
    # client__individual_client__name = CharFilter()
    # client__individual_client__surname = CharFilter()
    class Meta:
        model = Credit
        fields = ['num_dog', 'client__individual_client__rnn','client__individual_client__iin', 'status', 'client', 'credit_type']

class CreditViewSet(viewsets.ModelViewSet):
    """Регистрация, Получение, Удаление, Изменение, Частичное Изменение"""
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = CreditFilter
    filter_backends = [DjangoFilterBackend,] #filters.SearchFilter]
    # search_fields = ['notes', 'num_dog', 'period_count', 'reason', 'client__individual_client__name', 'client__individual_client__surname'] 

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CreditGetSerializer
        return self.serializer_class


class CreditTreatmentViewSet(viewsets.ModelViewSet):
    queryset = CreditTreatments.objects.all()
    serializer_class = CreditTreatmentsSerializer
    permission_classes = [permissions.AllowAny]