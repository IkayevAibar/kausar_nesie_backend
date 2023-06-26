from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import *
from apps.catalog.serializers import *

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

class IndividualClientSerializer(serializers.ModelSerializer):
    """Физическое лицо"""
    class Meta:
        model = IndividualClient
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    """Юр лица"""

    class Meta:
        model = Company
        fields = "__all__"

class CompanyInClientRetrieveSerializer(serializers.ModelSerializer):
    """Юр лица"""
    sector = SectorEconSerializer(read_only=True)
    org_form = OrgFormSerializer(read_only=True)
    form_property = FormPropertySerializer(read_only=True)

    class Meta:
        model = Company
        exclude = ['owners']


class AccountSerializer(serializers.ModelSerializer):
    """Счета"""

    class Meta:
        model = Account
        fields = "__all__"


class DocsSerializer(serializers.ModelSerializer):
    """Документы"""

    class Meta:
        model = Docs
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    """Контакты"""

    class Meta:
        model = Contact
        fields = "__all__"


class ContactRetrieveSerializer(serializers.ModelSerializer):
    """Контакты"""
    contact_type = ContactTypeSerializer(read_only=True)
    class Meta:
        model = Contact
        fields = "__all__"

class IndividualClientRetrieveSerializer(serializers.ModelSerializer):
    """Физическое лицо"""
    country = CountrySerializer(read_only=True)
    client_category = ClientCategorySerializer(read_only=True)
    place_of_birth = AreasSerializer(read_only=True)

    class Meta:
        model = IndividualClient
        fields = "__all__"
    

class ClientRetrieveSerializer(serializers.ModelSerializer):
    """Клиенты"""
    individual_client = IndividualClientRetrieveSerializer(required=False)
    docs = DocsSerializer(many=True, read_only=True)
    addresses = AddressRetrieveSerializer(many=True, read_only=True)
    contacts = ContactRetrieveSerializer(many=True, read_only=True)
    companies = CompanyInClientRetrieveSerializer(many=True, read_only=True, source="company_owners")

    class Meta:
        model = Client
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):  
    individual_client = IndividualClientSerializer(required=False)
    class Meta:
        model = Client
        fields = "__all__"
    
    def create(self, validated_data):
        individual_client_data = validated_data.pop('individual_client', None)
        client = Client.objects.create(**validated_data)

        if individual_client_data:
            individual_client = IndividualClient.objects.create(**individual_client_data)
            client.individual_client = individual_client
            client.save()

        return client


class CompanyRetrieveSerializer(serializers.ModelSerializer):
    """Юр лица"""
    sector = SectorEconSerializer(read_only=True)
    org_form = OrgFormSerializer(read_only=True)
    form_property = FormPropertySerializer(read_only=True)
    owners = ClientSerializer(read_only=True, many=True)
    class Meta:
        model = Company
        fields = "__all__"

class RequisiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requisite
        fields = "__all__"