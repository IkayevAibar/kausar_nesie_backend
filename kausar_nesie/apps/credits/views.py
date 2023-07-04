from django.http import JsonResponse

from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend, IsoDateTimeFilter, DateFilter, LookupChoiceFilter, CharFilter
from django_filters import FilterSet, DateTimeFromToRangeFilter
from .serializers import *

class CreditFilter(FilterSet):
    num_dog = CharFilter()
    client__individual_client__rnn = CharFilter()
    client__individual_client__iin = CharFilter()
    client = CharFilter()
    # period_count = CharFilter()
    # reason = CharFilter()
    # client__individual_client__name = CharFilter()
    # client__individual_client__surname = CharFilter()
    class Meta:
        model = Credit
        fields = ['num_dog', 'client__individual_client__rnn','client__individual_client__iin', 'status', 'client', 'credit_type']

class CreditViewSet(viewsets.ModelViewSet):
    """Регистрация, Получение, Удаление, Изменение, Частичное Изменение"""
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = CreditFilter
    filter_backends = [DjangoFilterBackend,] #filters.SearchFilter]
    # search_fields = ['notes', 'num_dog', 'period_count', 'reason', 'client__individual_client__name', 'client__individual_client__surname'] 

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CreditGetSerializer
        return self.serializer_class
    
    @action(detail=True, methods=['get'])
    def get_graphic_of_payment(self, request, pk=None):
        try:
            credit = Credit.objects.get(id=pk)
        except:
            raise Exception("Кредит не найден")
        
        percent_rate = float(credit.effective_rate)
        loan_term = credit.period_count
        loan_amount = float(credit.amount)
        commission_rate = 2
        days_in_first_payment = 30
        days_in_last_payment = 30
        monthly_commission_in = 0

        data = self.calculate_payment(percent_rate, loan_term, loan_amount, commission_rate, days_in_first_payment, monthly_commission_in)
        
        return JsonResponse(data)

    def calculate_payment(self, percent_rate, loan_term, loan_amount, commission_rate, days_in_first_payment, monthly_commission_in):
        # Расчетные данные
        
        #Ежемесячный платеж
        monthly_payment = round(loan_amount * ((percent_rate*0.01/12)/(1-(1+percent_rate*0.01/12)**-loan_term)),0)
        #Сумма ком.
        commission_amount = loan_amount*commission_rate/100
        #Остаток ОД
        principal_remaining = loan_amount 
        #Изначальные данные по Сумма %,  Сумма ежемес. ком., Сумма ежемес. ком.
        sum_income = 0 #Сумма %
        sum_of_principal_remaining = principal_remaining #Сумма ост. ОД
        sum_of_monthly_commission = 0 #Сумма ежемес. ком.
        #Доход
        total_income = 0

        result = {
            "table": [],
            "gesv": 0,
            "sum_income": sum_income,
            "commission_amount": commission_amount,
            "sum_of_principal_remaining": sum_of_principal_remaining,
            "commission_rate": commission_rate,
            "total_income": total_income,
            "monthly_commission_in": monthly_commission_in,
            "sum_of_monthly_commission": sum_of_monthly_commission
        }

        result["table"].append({
            "number": 0,
            "principal_payment": 0,
            "commission_payment": 0,
            "total_payment": 0,
            "principal_remaining": principal_remaining,
            "monthly_commission": 0.0
        })

        for month in range(1, loan_term + 1):
            if month <= loan_term:
                monthly_commission = round(loan_amount * monthly_commission_in, 0)
            else:
                monthly_commission = 0
            # Высчитываем Погашение ОД
            if month < loan_term:
                principal_payment= round(monthly_payment - (principal_remaining*percent_rate/100/12),0)
            else:
                if month == loan_term:
                    principal_payment = round(principal_remaining,0)
                else:
                    principal_payment = 0
            # Высчитываем Погашение возн.
            commission_payment  = round((principal_remaining*percent_rate/100/12)/30*days_in_first_payment,0)
            # Высчитываем Сумма %
            sum_income+=commission_payment
            # Высчитываем Общая сумма ОД+%+ком
            total_payment = principal_payment + commission_payment + monthly_commission
            # Высчитываем Остаток ОД
            principal_remaining -= principal_payment
            # Высчитываем Сумма ост. ОД
            sum_of_principal_remaining+=principal_remaining
            # Высчитываем Сумма ежемес. ком.
            sum_of_monthly_commission+=monthly_commission

            result["table"].append({
                "number": month,
                "principal_payment": principal_payment,
                "commission_payment": commission_payment,
                "total_payment": total_payment,
                "principal_remaining": principal_remaining,
                "monthly_commission": monthly_commission
            })
        total_income = sum_income + commission_amount + sum_of_monthly_commission
        result["total_income"] = total_income
        result["gesv"] = round((total_income/(sum_of_principal_remaining/loan_term))/loan_term*12*100, 1)
        result["sum_income"] = sum_income
        result["sum_of_principal_remaining"] = sum_of_principal_remaining
        return result

class CreditTreatmentViewSet(viewsets.ModelViewSet):
    queryset = CreditTreatments.objects.all()
    serializer_class = CreditTreatmentsSerializer
    permission_classes = [permissions.AllowAny]