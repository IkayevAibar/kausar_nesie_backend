from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import *
from .models import *


class IndividualClientViewSet(viewsets.ModelViewSet):
    """Физические лица"""
    queryset = IndividualClient.objects.all()
    serializer_class = IndividualClientSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        # Используем IndividualClientReadOnlySerializer для чтения
        if self.action == 'list' or self.action == 'retrieve':
            return IndividualClientRetrieveSerializer
        return self.serializer_class


class AddressViewSet(viewsets.ModelViewSet):
    """Адреса клиента"""
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AddressRetrieveSerializer
        return self.serializer_class



class ClientViewSet(viewsets.ModelViewSet):
    """Клиент"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ClientRetrieveSerializer
        return self.serializer_class




class CompanyViewSet(viewsets.ModelViewSet):
    """Юр лица"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CompanyRetrieveSerializer
        return self.serializer_class


class AccountViewSet(viewsets.ModelViewSet):
    """Счета"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]



class DocsViewSet(viewsets.ModelViewSet):
    """Документы"""
    queryset = Docs.objects.all()
    serializer_class = DocsSerializer
    permission_classes = [AllowAny]

class ContactViewSet(viewsets.ModelViewSet):
    """Контакты"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ContactRetrieveSerializer
        return self.serializer_class

