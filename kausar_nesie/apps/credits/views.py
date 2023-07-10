from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend, IsoDateTimeFilter, DateFilter, LookupChoiceFilter, CharFilter
from django_filters import FilterSet, DateTimeFromToRangeFilter
from .serializers import *

from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
import calendar
from num2words import num2words

from apps.clients.models import *
from apps.collaterals.models import *
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
    
    def fill_field(self, paragraph, field_name, field_value):
        if field_name in paragraph.text:
            run = paragraph.runs[0]  # Получаем первый Run в параграфе
            font_size = run.font.size  # Получаем размер шрифта
            paragraph.text = paragraph.text.replace(field_name, field_value)
            new_run = paragraph.runs[0]  # Получаем новый Run
            new_run.font.size = font_size  # Устанавливаем размер шрифта
            new_run.font.name = 'Times New Roman'  # Устанавливаем шрифт Times New Roman


    @action(detail=True, methods=['get'])
    def generate_credit_treatment(self, request, pk=None):
        try:
            credit = self.get_object()
        except:
            raise Response(status=status.HTTP_404_NOT_FOUND)

        # try:
        kausar_company = Company.objects.get(reg_num=123123123)
        kausar_company_director = IndividualClient.objects.filter(reg_number="0001").first()
        
        try:
            percent_rate = float(credit.effective_rate)
            loan_term = credit.period_count
            loan_amount = float(credit.amount)
            commission_rate = 2
            days_in_first_payment = 30
            days_in_last_payment = 30
            monthly_commission_in = 0
            data = self.calculate_payment(percent_rate, loan_term, loan_amount, commission_rate, days_in_first_payment, monthly_commission_in)
        except:
            return Response({"error_message":"Ошибка при расчете платежей"},status=status.HTTP_404_NOT_FOUND)        
        credit_client = credit.client
        
        try:
            client_docs = Docs.objects.filter(client=credit_client, identity_card_type=1).last()
        except:
            return Response({"error_message":"У клиента нет документа удостоверяющего личность"},status=status.HTTP_404_NOT_FOUND)
        
        try:
            client_address_fact = Address.objects.filter(client=credit_client, addr_type=1).last()
            client_address_reg = Address.objects.filter(client=credit_client, addr_type=2).last()
        except:
            return Response({"error_message":"У клиента нет адресов"},status=status.HTTP_404_NOT_FOUND)
        
        try:
            client_contact_home = Contact.objects.filter(client=credit_client, contact_type=1).last()
            client_contact_phone = Contact.objects.filter(client=credit_client, contact_type=2).last()
        except:
            return Response({"error_message":"У клиента нет контактов"},status=status.HTTP_404_NOT_FOUND)
        
        try:
            document = Document('apps/credits/utils/template.docx')
        except:
            try:
                document = Document('kausar_nesie/apps/credits/utils/template.docx')
            except:
                return Response({"error_message":"Шаблон Документа не найден"},status=status.HTTP_404_NOT_FOUND)

        field_name_00 = "_director_full_name_"
        field_value_00 = "Директор Каусар Компани"

        field_name_01 = "_credit_protocol_number_"
        field_value_01 = credit.num_dog

        field_name_02 = "_credit_day_number_"
        field_value_02 = credit.date_begin.strftime("%d")
        
        date_begin_month_number = credit.date_begin.strftime("%m")
        date_begin_month_name = calendar.month_name[int(date_begin_month_number)]

        field_name_03 = "_credit_month_string_"
        field_value_03 = date_begin_month_name.capitalize()

        field_name_04 = "_credit_year_last_two_"
        field_value_04 = credit.date_begin.strftime("%y")

        field_name_05 = "_credit_year_last_one_"
        field_value_05 = credit.date_begin.strftime("%y")[1]

        field_name_06 = "_credit_amount_"
        field_value_06 = str(credit.amount).rstrip("0").rstrip(".")

        field_name_07 = "_credit_string_amount_"
        field_value_07 = num2words(str(credit.amount).rstrip("0").rstrip("."), lang='ru')

        field_name_1 = "_credit_end_day_"
        field_value_1 = credit.date_end.strftime("%d")

        date_end_month_number = credit.date_end.strftime("%m")
        date_end_month_name = calendar.month_name[int(date_end_month_number)]

        field_name_2 = "_credit_end_month_string_"
        field_value_2 = date_end_month_name.capitalize()

        field_name_3 = "_credit_end_year_last_two_"
        field_value_3 = credit.date_end.strftime("%y")

        field_name_3_1 = "_credit_payment_persent_"
        field_value_3_1 = str(credit.effective_rate).rstrip("0").rstrip(".")

        field_name_4 = "_credit_payment_persent_string_"
        field_value_4 = num2words(str(credit.effective_rate).rstrip("0").rstrip("."), lang='ru')

        field_name_5 = "_credit_payment_method_"
        field_value_5 = "Аннуитетный"

        field_name_6 = "_credit_aim_"
        field_value_6 = credit.credit_target.name

        field_name_7 = "_year_effect_rate_persent_"
        field_value_7 = str(data["gesv"])

        field_name_8 = "_year_effect_rate_persent_string_"
        field_value_8 = num2words(str(commission_rate).rstrip("0").rstrip("."), lang='ru')

        try:
            collateral = Collateral.objects.filter(client=credit.client).last()
        except:
            return Response({"error_message":"У клиента нет залога"},status=status.HTTP_404_NOT_FOUND)
        
        field_name_08 = "_collateral_type_"
        field_value_08 = collateral.type.name

        field_name_09 = "_collateral_name_"
        field_value_09 = collateral.name

        field_name_9 = "_collateral_date_begin_day_"
        field_value_9 = collateral.date_begin.strftime("%d")

        collateral_date_begin_month_number = collateral.date_begin.strftime("%m")
        collateral_date_begin_month_name = calendar.month_name[int(date_begin_month_number)]

        field_name_10 = "_collateral_date_begin_month_string_"
        field_value_10 = collateral_date_begin_month_name.capitalize()

        field_name_11 = "_collateral_date_begin_year_last_one_"
        field_value_11 = collateral.date_begin.strftime("%y")[1]

        field_name_12 = "_collateral_market_rated_company_"
        field_value_12 = "___________"

        field_name_13 = "_collateral_reg_num_"
        field_value_13 = collateral.num_dog

        field_name_14 = "_collateral_num_dog_"
        field_value_14 = collateral.num_dog

        field_name_15 = "_commission_rate_"
        field_value_15 = "2"

        field_name_16 = "_commission_string_rate_"
        field_value_16 = "Два"

        field_name_17 = "_bank_company_address_"
        field_value_17 = "г. Алматы"

        field_name_18 = "_bank_fact_address_"
        field_value_18 = "г. Алматы"

        field_name_19 = "_bank_iik_"
        field_value_19 = "123123123123123"

        field_name_20 = "_bank_kbe_"
        field_value_20 = "125121221323112"

        field_name_21 = "_country_"
        field_value_21 = "Республика Казахстан"

        field_name_22 = "_client_full_name_"
        field_value_22 = f"{credit.client.individual_client.name} {credit.client.individual_client.surname} {credit.client.individual_client.middle_name}"

        field_name_23 = "_passport_number_"
        field_value_23 = f"{client_docs.number}"

        field_name_24 = "_passport_given_place_"
        field_value_24 = f"{client_docs.issued_by}"

        field_name_25 = "_client_country_"
        field_value_25 = credit.client.individual_client.country.name

        field_name_26 = "_client_iin_"
        field_value_26 = credit.client.individual_client.iin

        field_name_27 = "_client_address_registered_"
        field_value_27 = f"{client_address_reg.areas.name}, {client_address_reg.cities.name}, {client_address_reg.street.name}, {client_address_reg.district.name}, Дом {client_address_reg.house}, Квартира {client_address_reg.flat}"

        field_name_28 = "_client_address_actual_"
        field_value_28 = f"{client_address_fact.areas.name}, {client_address_fact.cities.name}, {client_address_fact.street.name}, {client_address_fact.district.name}, Дом {client_address_fact.house}, Квартира {client_address_fact.flat}"

        field_name_29 = "_client_phone_private_"
        field_value_29 = f"{client_contact_phone.value}"

        field_name_30 = "_client_phone_home_"
        field_value_30 = f"{client_contact_home.value}"



        for paragraph in document.paragraphs:
            self.fill_field(paragraph, field_name_00, field_value_00)
            self.fill_field(paragraph, field_name_01, field_value_01)
            self.fill_field(paragraph, field_name_02, field_value_02)
            self.fill_field(paragraph, field_name_03, field_value_03)
            self.fill_field(paragraph, field_name_04, field_value_04)
            self.fill_field(paragraph, field_name_05, field_value_05)
            self.fill_field(paragraph, field_name_06, field_value_06)
            self.fill_field(paragraph, field_name_07, field_value_07)
            self.fill_field(paragraph, field_name_08, field_value_08)
            self.fill_field(paragraph, field_name_09, field_value_09)
            self.fill_field(paragraph, field_name_1, field_value_1)
            self.fill_field(paragraph, field_name_2, field_value_2)
            self.fill_field(paragraph, field_name_3, field_value_3)
            self.fill_field(paragraph, field_name_4, field_value_4)
            self.fill_field(paragraph, field_name_3_1, field_value_3_1)
            self.fill_field(paragraph, field_name_5, field_value_5)
            self.fill_field(paragraph, field_name_6, field_value_6)
            self.fill_field(paragraph, field_name_8, field_value_8)
            self.fill_field(paragraph, field_name_7, field_value_7)
            self.fill_field(paragraph, field_name_9, field_value_9)
            self.fill_field(paragraph, field_name_10, field_value_10)
            self.fill_field(paragraph, field_name_11, field_value_11)
            self.fill_field(paragraph, field_name_12, field_value_12)
            self.fill_field(paragraph, field_name_13, field_value_13)
            self.fill_field(paragraph, field_name_14, field_value_14)
            self.fill_field(paragraph, field_name_15, field_value_15)
            self.fill_field(paragraph, field_name_16, field_value_16)
            self.fill_field(paragraph, field_name_17, field_value_17)
            self.fill_field(paragraph, field_name_18, field_value_18)
            self.fill_field(paragraph, field_name_19, field_value_19)
            self.fill_field(paragraph, field_name_20, field_value_20)
            self.fill_field(paragraph, field_name_21, field_value_21)
            self.fill_field(paragraph, field_name_22, field_value_22)
            self.fill_field(paragraph, field_name_23, field_value_23)
            self.fill_field(paragraph, field_name_24, field_value_24)
            self.fill_field(paragraph, field_name_25, field_value_25)
            self.fill_field(paragraph, field_name_26, field_value_26)
            self.fill_field(paragraph, field_name_27, field_value_27)
            self.fill_field(paragraph, field_name_28, field_value_28)
            self.fill_field(paragraph, field_name_29, field_value_29)
            self.fill_field(paragraph, field_name_30, field_value_30)

        path = f'/credit/contracts/{field_value_01}_credit_contract.docx'

        try:
            document.save(f'kausar_nesie/media{path}')
        except:
            try:
                document.save(f'media{path}')
            except:
                return Response({"error_message":"Не удалось сохранить договор"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        ct = CreditTreatments.objects.get_or_create(credit=credit, name=f'{field_value_01}_credit_contract.docx' , document=path)
        if(ct[0] == False):
            index = 1
        else:
            index = 0

        url = request.build_absolute_uri(ct[index].document.url)
        return Response({'status': 'ok', 'url': url}, status=status.HTTP_200_OK)

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