from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class CollateralSerializer(serializers.ModelSerializer):
    """Договора обеспечения"""

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
