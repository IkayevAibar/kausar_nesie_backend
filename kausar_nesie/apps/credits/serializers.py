from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class CreditListSerializer(serializers.ModelSerializer):
    """Credit"""

    class Meta:
        model = Credit
        fields = "__all__"

