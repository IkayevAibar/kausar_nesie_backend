from .serializers import *

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend, IsoDateTimeFilter, DateFilter, LookupChoiceFilter
from django_filters import FilterSet

class CollateralFilter(FilterSet):

    class Meta:
        model = Collateral
        fields = ['num_dog', 'client', 'type', 'status',]

class CollateralViewSet(viewsets.ModelViewSet):
    queryset = Collateral.objects.all()
    serializer_class = CollateralSerializer
    filterset_class = CollateralFilter
    filter_backends = [DjangoFilterBackend,]

    @action(detail=False, methods=['get'])
    def get_last_num_reg(self, request):
        last_object = Collateral.objects.last()
        if last_object:
            value = last_object.id
        else: value = 0

        return Response({'last_num_reg': value})
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class CollateralInsuranceViewSet(viewsets.ModelViewSet):
    queryset = CollateralInsurance.objects.all()
    serializer_class = CollateralInsuranceSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class CollateralCoclientViewSet(viewsets.ModelViewSet):
    queryset = CollateralCoclient.objects.all()
    serializer_class = CollateralCoclientSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class CollateralAssesmentViewSet(viewsets.ModelViewSet):
    queryset = CollateralAssesment.objects.all()
    serializer_class = CollateralAssesmentSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]