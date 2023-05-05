from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from apps.catalog.serializers import ContactRetrieveSerializer, CountrySerializer, ClientCategorySerializer, CitiesSerializer, AreasSerializer, AddressTypeSerializer


class AddressSerializer(serializers.ModelSerializer):
    """Адреса клиента"""

    class Meta:
        model = Address
        fields = "__all__"

class AddressRetrieveSerializer(serializers.ModelSerializer):
    """Адреса клиента"""
    addr_type = AddressTypeSerializer(read_only=True)
    cities = CitiesSerializer(read_only=True)
    areas = AreasSerializer(read_only=True)
    class Meta:
        model = Address
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    """Клиенты"""

    class Meta:
        model = Client
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    """Юр лица"""

    class Meta:
        model = Company
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    """Счета"""

    class Meta:
        model = Account
        fields = "__all__"



class IdCardSerializer(serializers.ModelSerializer):
    """Документы удостоверющие данные клиента"""


    class Meta:
        model = IdCard
        fields = "__all__"

class DocsSerializer(serializers.ModelSerializer):
    """Документы"""

    class Meta:
        model = Docs
        fields = "__all__"



class IndividualClientSerializer(serializers.ModelSerializer):
    """Физическое лицо"""
    class Meta:
        model = IndividualClient
        fields = "__all__"

class IndividualClientRetrieveSerializer(serializers.ModelSerializer):
    """Физическое лицо"""
    docs = DocsSerializer(many=True, read_only=True)
    addresses = AddressRetrieveSerializer(many=True, read_only=True)
    contacts = ContactRetrieveSerializer(many=True, read_only=True)
    country = CountrySerializer(read_only=True)
    client_category = ClientCategorySerializer(read_only=True)

    class Meta:
        model = IndividualClient
        fields = "__all__"
    
