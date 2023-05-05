from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from apps.catalog.serializers import ContactSerializer


class AddressSerializer(serializers.ModelSerializer):
    """Адреса клиента"""

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
    docs = DocsSerializer(many=True)
    addresses = AddressSerializer(many=True)
    contacts = ContactSerializer(many=True)

    class Meta:
        model = IndividualClient
        fields = "__all__"
