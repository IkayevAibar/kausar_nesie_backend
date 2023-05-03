from rest_framework import viewsets, permissions

from django.http import JsonResponse

from .serializers import *

class CreditViewSet(viewsets.ModelViewSet):
    """Регистрация, Получение, Удаление, Изменение, Частичное Изменение"""
    queryset = Credit.objects.all()
    serializer_class = CreditListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]