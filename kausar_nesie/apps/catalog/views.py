from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import *
from rest_framework import viewsets

class AreasViewSet(viewsets.ModelViewSet):
    """Справочник. Области"""
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer


class AddressTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы адресов"""
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeSerializer


class CitiesViewSet(viewsets.ModelViewSet):
    """Справочник. Населенные пункты"""
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """Контакты"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ClientCategoryViewSet(viewsets.ModelViewSet):
    """Справочник. Категории клиентов"""
    queryset = ClientCategory.objects.all()
    serializer_class = ClientCategorySerializer


class CategoryTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Виды категорий качества"""
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer


class WorkTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Тип занятости"""
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer


class TransactionTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы транзакций"""
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer


class StatusViewSet(viewsets.ModelViewSet):
    """Справочник. Статусы"""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class SectorEconViewSet(viewsets.ModelViewSet):
    """Справочник. Сектора экономики"""
    queryset = SectorEcon.objects.all()
    serializer_class = SectorEconSerializer


class ProjectTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы проектов"""
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


class PositionTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Тип должности"""
    queryset = PositionType.objects.all()
    serializer_class = PositionTypeSerializer


class PeriodTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы периодов"""
    queryset = PeriodType.objects.all()
    serializer_class = PeriodTypeSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """Справочник. КНП"""
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class OrgFormViewSet(viewsets.ModelViewSet):
    """Справочник. Форма предприятия"""
    queryset = OrgForm.objects.all()
    serializer_class = OrgFormSerializer


class LinkTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы связи договоров"""
    queryset = LinkType.objects.all()
    serializer_class = LinkTypeSerializer


class LineTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы связи линий"""
    queryset = LineType.objects.all()
    serializer_class = LineTypeSerializer

class IdCardViewSet(viewsets.ModelViewSet):
    """Документы удостоверющие данные клиента"""
    queryset = IdcardType.objects.all()
    serializer_class = IdcardTypeSerializer


class FormPropertyViewSet(viewsets.ModelViewSet):
    """Справочник. Форма собственности"""
    queryset = FormProperty.objects.all()
    serializer_class = FormPropertySerializer


class CurrenciesViewSet(viewsets.ModelViewSet):
    """Справочник. Валюты"""
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer

class CreditTargetViewSet(viewsets.ModelViewSet):
    """Справочник. Цели кредитования"""
    queryset = CreditTarget.objects.all()
    serializer_class = CreditTargetSerializer


class CreditSourceViewSet(viewsets.ModelViewSet):
    """Справочник. Источник кредитования"""
    queryset = CreditSource.objects.all()
    serializer_class = CreditSourceSerializer


class CountryViewSet(viewsets.ModelViewSet):
    """Справочник. Государства"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountersViewSet(viewsets.ModelViewSet):
    """Справочник. Счетчики"""
    queryset = Counters.objects.all()
    serializer_class = CountersSerializer


class ContactTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы контактов"""
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer


class CollateralTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы залога"""
    queryset = CollateralType.objects.all()
    serializer_class = CollateralTypeSerializer


class BankViewSet(viewsets.ModelViewSet):
    """Справочник. Банки"""
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class CalculateViewSet(viewsets.ModelViewSet):
    """Справочник. Тип расчета"""
    queryset = Calculate.objects.all()
    serializer_class = CalculateSerializer


class BaseAccountViewSet(viewsets.ModelViewSet):
    """План счетов"""
    queryset = BaseAccount.objects.all()
    serializer_class = BaseAccountSerializer