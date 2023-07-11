from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

from Oauth.serializers import UserSerializer
from apps.catalog.serializers import *
from apps.clients.serializers import ClientSerializer
class CreditSerializer(serializers.ModelSerializer):
    """Credit Create/Update"""
    request = serializers.IntegerField(read_only=True)
    date_close = serializers.DateField(read_only=True)
    date_sign = serializers.DateField(read_only=True)
    class Meta:
        model = Credit
        fields = "__all__"


class CreditGetSerializer(serializers.ModelSerializer):
    """Credit Retrieve/List"""
    client = ClientSerializer()
    emp = UserSerializer()
    credit_type = CreditTypeSerializer()
    curr = CurrenciesSerializer()
    depart = DepartamentSerializer()
    project_type = ProjectTypeSerializer()
    credit_source = CreditSourceSerializer()
    credit_target= CreditTargetSerializer()
    period_type = PeriodTypeSerializer()
    class Meta:
        model = Credit
        fields = "__all__"

class CreditTreatmentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CreditTreatments
        fields = "__all__"

class CreditPaymentScheduleSerializer(serializers.ModelSerializer):
    """CreditPaymentSchedule Create/Update"""
    class Meta:
        model = CreditPaymentSchedule
        fields = "__all__"