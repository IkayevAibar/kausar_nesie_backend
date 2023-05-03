from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

class AddressTypeSerializer(serializers.ModelSerializer):
    """Справочник. Типы адресов"""

    class Meta:
        model = AddressType
        fields = "__all__"


class CitiesSerializer(serializers.ModelSerializer):
    """Справочник. Населенные пункты"""

    class Meta:
        model = Cities
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    """Контакты"""

    class Meta:
        model = Contact
        fields = "__all__"


class AreasSerializer(serializers.ModelSerializer):
    """Справочник. Области"""

    class Meta:
        model = Areas
        fields = "__all__"


class ClientCategorySerializer(serializers.ModelSerializer):
    """Справочник. Категории клиентов"""

    class Meta:
        model = ClientCategory
        fields = "__all__"


class CategoryTypeSerializer(serializers.ModelSerializer):
    """Справочник. Виды категорий качества"""

    class Meta:
        model = CategoryType
        fields = "__all__"


class WorkTypeSerializer(serializers.ModelSerializer):
    """Справочник. Тип занятости"""

    class Meta:
        model = WorkType
        fields = "__all__"


class TransactionTypeSerializer(serializers.ModelSerializer):
    """Справочник. Типы транзакций"""

    class Meta:
        model = TransactionType
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    """Справочник. Статусы"""

    class Meta:
        model = Status
        fields = "__all__"


class SectorEconSerializer(serializers.ModelSerializer):
    """Справочник.Сектора экономики"""

    class Meta:
        model = SectorEcon
        fields = "__all__"


class ProjectTypeSerializer(serializers.ModelSerializer):
    """Справочник. Типы проектов"""

    class Meta:
        model = ProjectType
        fields = "__all__"


class PositionTypeSerializer(serializers.ModelSerializer):
    """Справочник. Тип должности"""

    class Meta:
        model = PositionType
        fields = "__all__"


class PeriodTypeSerializer(serializers.ModelSerializer):
    """Справочник. Типы периодов"""

    class Meta:
        model = PeriodType
        fields = "__all__"


class PaymentTypeSerializer(serializers.ModelSerializer):
    """Справочник. КНП"""

    class Meta:
        model = PaymentType
        fields = "__all__"


class OrgFormSerializer(serializers.ModelSerializer):
    """Справочник. Форма предприятия"""

    class Meta:
        model = OrgForm
        fields = "__all__"


class LinkTypeSerializer(serializers.ModelSerializer):
    """Справочник. Типы связи договоров"""

    class Meta:
        model = LinkType
        fields = "__all__"


class LineTypeSerializer(serializers.ModelSerializer):
    """Справочник.Типы кредитных линий"""

    class Meta:
        model = LineType
        fields = "__all__"


class IdcardTypeSerializer(serializers.ModelSerializer):
    """Справочник.Типы документов"""

    class Meta:
        model = IdcardType
        fields = "__all__"


class FormPropertySerializer(serializers.ModelSerializer):
    """Справочник. Форма собственности"""

    class Meta:
        model = FormProperty
        fields = "__all__"


class CurrenciesSerializer(serializers.ModelSerializer):
    """Справочник. Валюты"""

    class Meta:
        model = Currencies
        fields = "__all__"


class CreditTargetSerializer(serializers.ModelSerializer):
    """Справочник. Цели кредитования"""

    class Meta:
        model = CreditTarget
        fields = "__all__"


class CreditSourceSerializer(serializers.ModelSerializer):
    """Справочник. Источник кредитования"""

    class Meta:
        model = CreditSource
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    """Справочник. Государства"""

    class Meta:
        model = Country
        fields = "__all__"


class CountersSerializer(serializers.ModelSerializer):
    """Справочник. Счетчики"""

    class Meta:
        model = Counters
        fields = "__all__"


class ContactTypeSerializer(serializers.ModelSerializer):
    """Справочник. Типы контактов"""

    class Meta:
        model = ContactType
        fields = "__all__"


class CollateralTypeSerializer(serializers.ModelSerializer):
    """Справочник. Типы залога"""

    class Meta:
        model = CollateralType
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    """Справочник. Банки"""

    class Meta:
        model = Bank
        fields = "__all__"


class CalculateSerializer(serializers.ModelSerializer):
    """Справочник. Тип расчета"""

    class Meta:
        model = Calculate
        fields = "__all__"


class BaseAccountSerializer(serializers.ModelSerializer):
    """План счетов"""

    class Meta:
        model = BaseAccount
        fields = "__all__"
