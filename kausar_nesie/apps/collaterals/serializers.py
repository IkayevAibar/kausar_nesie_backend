from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from django.utils import timezone

class CollateralSerializer(serializers.ModelSerializer):
    """Договора обеспечения"""

    def validate_date_begin(self, value):
        if value == None:
            raise serializers.ValidationError("Дата начала не может быть пустой")

        if value < timezone.now().date():
            raise serializers.ValidationError("Дата начала не может быть раньше текущей даты")
        
        return value
    
    def validate_date_end(self, value):
        if value == None:
            raise serializers.ValidationError("Дата окончания не может быть пустой")

        if value < self.validated_data.get("date_begin"):
            raise serializers.ValidationError("Дата окончания не может быть раньше даты начала")
        
        return value

    def validate_amount(self, value):
        if value == None:
            raise serializers.ValidationError("Сумма не может быть пустой")

        if value <= 0:
            raise serializers.ValidationError("Сумма должна быть больше 0")

        return value
    
    def validate_name(self, value):
        if value == None:
            raise serializers.ValidationError("Наименование не может быть пустым")

        return value

    class Meta:
        model = Collateral
        fields = "__all__"


class CollateralInsuranceSerializer(serializers.ModelSerializer):
    """Страхование залога"""

    class Meta:
        model = CollateralInsurance
        fields = "__all__"


class CollateralCoclientSerializer(serializers.ModelSerializer):
    """Со-залогодатели"""

    class Meta:
        model = CollateralInsurance
        fields = "__all__"


class CollateralAssesmentSerializer(serializers.ModelSerializer):
    """Оценка залога"""


    class Meta:
        model = CollateralAssesment
        fields = "__all__"
