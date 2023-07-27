from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *

class AreasViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Области"""
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class AddressTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Типы адресов"""
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class CitiesViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Населенные пункты"""
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['area']
    pagination_class = None

class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Районы"""
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']
    pagination_class = None

class StreetViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Улицы"""
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['district']
    pagination_class = None

class ClientCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Категории клиентов"""
    queryset = ClientCategory.objects.all()
    serializer_class = ClientCategorySerializer
    permission_classes = [AllowAny]
    pagination_class = None


class CategoryTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Виды категорий качества"""
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class WorkTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Тип занятости"""
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class TransactionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Типы транзакций"""
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Статусы"""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class SectorEconViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Сектора экономики"""
    queryset = SectorEcon.objects.all()
    serializer_class = SectorEconSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class ProjectTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Типы проектов"""
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class PositionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Тип должности"""
    queryset = PositionType.objects.all()
    serializer_class = PositionTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class PeriodTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Типы периодов"""
    queryset = PeriodType.objects.all()
    serializer_class = PeriodTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class PaymentTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. КНП"""
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class OrgFormViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Форма предприятия"""
    queryset = OrgForm.objects.all()
    serializer_class = OrgFormSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class LinkTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Типы связи договоров"""
    queryset = LinkType.objects.all()
    serializer_class = LinkTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class LineTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Типы связи линий"""
    queryset = LineType.objects.all()
    serializer_class = LineTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class IdCardViewSet(viewsets.ReadOnlyModelViewSet):
    """Документы удостоверющие данные клиента"""
    queryset = IdcardType.objects.all()
    serializer_class = IdcardTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class FormPropertyViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Форма собственности"""
    queryset = FormProperty.objects.all()
    serializer_class = FormPropertySerializer
    permission_classes = [AllowAny]
    pagination_class = None


class CurrenciesViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Валюты"""
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class CreditTargetViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Цели кредитования"""
    queryset = CreditTarget.objects.all()
    serializer_class = CreditTargetSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class CreditSourceViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Источник кредитования"""
    queryset = CreditSource.objects.all()
    serializer_class = CreditSourceSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Государства"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [AllowAny]
    pagination_class = None


class CountersViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Счетчики"""
    queryset = Counters.objects.all()
    serializer_class = CountersSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class ContactTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Типы контактов"""
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class CollateralTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Типы залога"""
    queryset = CollateralType.objects.all()
    serializer_class = CollateralTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class DeptTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Виды задолженностей"""
    queryset = DeptType.objects.all()
    serializer_class = DeptTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class BankViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Банки"""
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class CalculateViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Тип расчета"""
    queryset = Calculate.objects.all()
    serializer_class = CalculateSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class BaseAccountViewSet(viewsets.ReadOnlyModelViewSet):
    """План счетов"""
    queryset = BaseAccount.objects.all()
    serializer_class = BaseAccountSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class AccountPatternViewSet(viewsets.ReadOnlyModelViewSet):
    """Шаблоны номеров счетов"""
    queryset = AccountPattern.objects.all()
    serializer_class = AccountPatternSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class AccountTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Типы счетов"""
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class DepartamentViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Отделы"""
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class PaymentRuleViewSet(viewsets.ReadOnlyModelViewSet):
    """Правила гашения"""
    queryset = PaymentRule.objects.all()
    serializer_class = PaymentRuleSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class CreditTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Типы кредитов"""
    queryset = CreditType.objects.all()
    serializer_class = CreditTypeSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class InterestSchemeViewSet(viewsets.ReadOnlyModelViewSet):
    """Справочник. Схемы начисления процентов"""
    queryset = InterestScheme.objects.all()
    serializer_class = InterestSchemeSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class InterestRateViewSet(viewsets.ReadOnlyModelViewSet):
    """Ставки. Схемы начисления процентов"""
    queryset = InterestRate.objects.all()
    serializer_class = InterestRateSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class InterestJournalViewSet(viewsets.ReadOnlyModelViewSet):
    """Журнал начисленных процентов"""
    queryset = InterestJournal.objects.all()
    serializer_class = InterestJournalSerializer
    permission_classes = [AllowAny]
    pagination_class = None


class InsuranceViewSet(viewsets.ReadOnlyModelViewSet):
    """Договора страхования"""
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [AllowAny]
    pagination_class = None

class InsuranceLinkViewSet(viewsets.ReadOnlyModelViewSet):
    """Связь с договорами страхования"""
    queryset = InsuranceLink.objects.all()
    serializer_class = InsuranceLinkSerializer
    permission_classes = [AllowAny]
    pagination_class = None

