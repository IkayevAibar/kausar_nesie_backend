from .serializers import *
from rest_framework import viewsets, permissions

class CollateralViewSet(viewsets.ModelViewSet):
    queryset = Collateral.objects.all()
    serializer_class = CollateralSerializer
    
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