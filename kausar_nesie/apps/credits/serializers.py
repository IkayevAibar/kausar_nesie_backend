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

class CreditRecalculatePaymentScheduleStandardSerializer(serializers.Serializer):
    payment_amount = serializers.DecimalField(max_digits=20, decimal_places=2, required=True)
    payment_number = serializers.IntegerField(required=True)
    new_month_number = serializers.IntegerField(required=False)

class CreditPaymentScheduleStandardSerializer(serializers.Serializer):
    payment_number = serializers.IntegerField(required=True)
    payment_date = serializers.DateField(required=False)


class CreditTreatmentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CreditTreatments
        fields = "__all__"

class CreditPaymentScheduleSerializer(serializers.ModelSerializer):
    """CreditPaymentSchedule Create/Update"""
    class Meta:
        model = CreditPaymentSchedule
        fields = "__all__"

class CreditLineSerializer(serializers.ModelSerializer):
    """CreditLine Create/Update"""
    credits = CreditSerializer(many=True, read_only=True)
    class Meta:
        model = CreditLine
        fields = "__all__"

class RequisiteSerializer(serializers.ModelSerializer):
    """Requisite Create/Update"""

    def validate_req_acc(self, value):
        if value == None:
            raise serializers.ValidationError("IBAN не может быть пустым")
        
        value = value.replace(" ", "")

        if len(value) != 20:
            raise serializers.ValidationError("IBAN должен состоять из 20 символов")
        return value

    def validate_req_name(self, value):
        if value == None:
            raise serializers.ValidationError("ФИО не может быть пустым")
        
        return value.strip().upper()

    def validate_req_kbe(self, value):
        if value == None:
            raise serializers.ValidationError("КБЕ не может быть пустым")
        
        value = value.replace(" ", "")

        if len(value) != 2:
            raise serializers.ValidationError("КБЕ должен состоять из 2 символов")
        return value
    
    def validate_req_perioud(self, value):
        if value == None:
            raise serializers.ValidationError("Период не может быть пустым")
        return value
    
    class Meta:
        model = Requisite
        fields = "__all__"