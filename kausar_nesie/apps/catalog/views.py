from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .serializers import *

class AreasViewSet(viewsets.ModelViewSet):
    """Справочник. Области"""
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer
    permission_classes = [AllowAny]


class AddressTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы адресов"""
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeSerializer
    permission_classes = [AllowAny]


class CitiesViewSet(viewsets.ModelViewSet):
    """Справочник. Населенные пункты"""
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = [AllowAny]


class ContactViewSet(viewsets.ModelViewSet):
    """Контакты"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ContactRetrieveSerializer
        return self.serializer_class


class ClientCategoryViewSet(viewsets.ModelViewSet):
    """Справочник. Категории клиентов"""
    queryset = ClientCategory.objects.all()
    serializer_class = ClientCategorySerializer
    permission_classes = [AllowAny]


class CategoryTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Виды категорий качества"""
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer
    permission_classes = [AllowAny]


class WorkTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Тип занятости"""
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer
    permission_classes = [AllowAny]


class TransactionTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы транзакций"""
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    permission_classes = [AllowAny]


class StatusViewSet(viewsets.ModelViewSet):
    """Справочник. Статусы"""
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [AllowAny]


class SectorEconViewSet(viewsets.ModelViewSet):
    """Справочник. Сектора экономики"""
    queryset = SectorEcon.objects.all()
    serializer_class = SectorEconSerializer
    permission_classes = [AllowAny]


class ProjectTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы проектов"""
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer
    permission_classes = [AllowAny]


class PositionTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Тип должности"""
    queryset = PositionType.objects.all()
    serializer_class = PositionTypeSerializer
    permission_classes = [AllowAny]


class PeriodTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы периодов"""
    queryset = PeriodType.objects.all()
    serializer_class = PeriodTypeSerializer
    permission_classes = [AllowAny]


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """Справочник. КНП"""
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
    permission_classes = [AllowAny]


class OrgFormViewSet(viewsets.ModelViewSet):
    """Справочник. Форма предприятия"""
    queryset = OrgForm.objects.all()
    serializer_class = OrgFormSerializer
    permission_classes = [AllowAny]


class LinkTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы связи договоров"""
    queryset = LinkType.objects.all()
    serializer_class = LinkTypeSerializer
    permission_classes = [AllowAny]


class LineTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы связи линий"""
    queryset = LineType.objects.all()
    serializer_class = LineTypeSerializer
    permission_classes = [AllowAny]

class IdCardViewSet(viewsets.ModelViewSet):
    """Документы удостоверющие данные клиента"""
    queryset = IdcardType.objects.all()
    serializer_class = IdcardTypeSerializer
    permission_classes = [AllowAny]


class FormPropertyViewSet(viewsets.ModelViewSet):
    """Справочник. Форма собственности"""
    queryset = FormProperty.objects.all()
    serializer_class = FormPropertySerializer
    permission_classes = [AllowAny]


class CurrenciesViewSet(viewsets.ModelViewSet):
    """Справочник. Валюты"""
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer
    permission_classes = [AllowAny]

class CreditTargetViewSet(viewsets.ModelViewSet):
    """Справочник. Цели кредитования"""
    queryset = CreditTarget.objects.all()
    serializer_class = CreditTargetSerializer
    permission_classes = [AllowAny]


class CreditSourceViewSet(viewsets.ModelViewSet):
    """Справочник. Источник кредитования"""
    queryset = CreditSource.objects.all()
    serializer_class = CreditSourceSerializer
    permission_classes = [AllowAny]


class CountryViewSet(viewsets.ModelViewSet):
    """Справочник. Государства"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [AllowAny]


class CountersViewSet(viewsets.ModelViewSet):
    """Справочник. Счетчики"""
    queryset = Counters.objects.all()
    serializer_class = CountersSerializer
    permission_classes = [AllowAny]


class ContactTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы контактов"""
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer
    permission_classes = [AllowAny]


class CollateralTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы залога"""
    queryset = CollateralType.objects.all()
    serializer_class = CollateralTypeSerializer
    permission_classes = [AllowAny]

class DeptTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Виды задолженностей"""
    queryset = DeptType.objects.all()
    serializer_class = DeptTypeSerializer
    permission_classes = [AllowAny]


class BankViewSet(viewsets.ModelViewSet):
    """Справочник. Банки"""
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [AllowAny]


class CalculateViewSet(viewsets.ModelViewSet):
    """Справочник. Тип расчета"""
    queryset = Calculate.objects.all()
    serializer_class = CalculateSerializer
    permission_classes = [AllowAny]


class BaseAccountViewSet(viewsets.ModelViewSet):
    """План счетов"""
    queryset = BaseAccount.objects.all()
    serializer_class = BaseAccountSerializer
    permission_classes = [AllowAny]

class AccountPatternViewSet(viewsets.ModelViewSet):
    """Шаблоны номеров счетов"""
    queryset = AccountPattern.objects.all()
    serializer_class = AccountPatternSerializer
    permission_classes = [AllowAny]

class AccountTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы счетов"""
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer
    permission_classes = [AllowAny]

class DepartamentViewSet(viewsets.ModelViewSet):
    """Справочник. Отделы"""
    queryset = Departament.objects.all()
    serializer_class = DepartamentSerializer
    permission_classes = [AllowAny]

class PaymentRuleViewSet(viewsets.ModelViewSet):
    """Правила гашения"""
    queryset = PaymentRule.objects.all()
    serializer_class = PaymentRuleSerializer
    permission_classes = [AllowAny]

class CreditTypeViewSet(viewsets.ModelViewSet):
    """Справочник. Типы кредитов"""
    queryset = CreditType.objects.all()
    serializer_class = CreditTypeSerializer
    permission_classes = [AllowAny]

class InterestSchemeViewSet(viewsets.ModelViewSet):
    """Справочник. Схемы начисления процентов"""
    queryset = InterestScheme.objects.all()
    serializer_class = InterestSchemeSerializer
    permission_classes = [AllowAny]

class InterestRateViewSet(viewsets.ModelViewSet):
    """Ставки. Схемы начисления процентов"""
    queryset = InterestRate.objects.all()
    serializer_class = InterestRateSerializer
    permission_classes = [AllowAny]


class InterestJournalViewSet(viewsets.ModelViewSet):
    """Журнал начисленных процентов"""
    queryset = InterestJournal.objects.all()
    serializer_class = InterestJournalSerializer
    permission_classes = [AllowAny]


class InsuranceViewSet(viewsets.ModelViewSet):
    """Договора страхования"""
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [AllowAny]

class InsuranceLinkViewSet(viewsets.ModelViewSet):
    """Связь с договорами страхования"""
    queryset = InsuranceLink.objects.all()
    serializer_class = InsuranceLinkSerializer
    permission_classes = [AllowAny]

