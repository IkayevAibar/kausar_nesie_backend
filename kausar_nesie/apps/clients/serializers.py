from rest_framework import serializers, status
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .models import *
from apps.catalog.serializers import *

import re
import datetime


class AddressSerializer(serializers.ModelSerializer):
    """Адреса клиента"""

    def validate_house(self, value):
        """
        Валидация поля house: проверяем, что номер дома не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Номер дома не может быть пустым.")
        return value
    
    def validate_flat(self, value):
        """
        Валидация поля flat: проверяем, что номер квартиры не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Номер квартиры не может быть пустым.")
        return value
    
    def validate_post_index(self, value):
        """
        Валидация поля post_index: проверяем, что индекс не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Индекс не может быть пустым.")
        return value

    class Meta:
        model = Address
        fields = "__all__"

class AddressRetrieveSerializer(serializers.ModelSerializer):
    """Адреса клиента"""
    addr_type = AddressTypeSerializer(read_only=True)
    cities = CitiesSerializer(read_only=True)
    areas = AreasSerializer(read_only=True)
    class Meta:
        model = Address
        fields = "__all__"

class IndividualClientSerializer(serializers.ModelSerializer):
    """Физическое лицо"""

    def validate_reg_number(self, value):
        """
        Валидация поля reg_number: проверяем, что номер регистрации не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Номер регистрации не может быть пустым.")
        return value

    def validate_full_name(self, value):
        """
        Валидация поля full_name: проверяем, что имя содержит только буквы и дефисы, если указано.
        """
        if not value:
            raise serializers.ValidationError("Поле 'full_name' обязательно.")
        if not re.match(r'^[A-Za-zА-Яа-я-\s]+$', value):
            raise serializers.ValidationError("Поле 'full_name' должно содержать только буквы и дефисы.")
        return value

    def validate_date_of_birth(self, value):
        # Валидация даты рождения, чтобы не была в будущем
        if value > timezone.now().date():
            raise serializers.ValidationError("Дата рождения не может быть в будущем.")
        
        if value.year < 1900:
            raise serializers.ValidationError("Дата рождения не может быть раньше 1900 года.")
        
        return value

    def validate_rnn(self, value):
        # Валидация РНН (Регистрационный номер налогоплательщика)
        if(value != None and value != ""):
            if not value.isdigit() or len(value) != 12:
                raise serializers.ValidationError("РНН должен состоять из 12 цифр.")
        
        return value

    def validate_iin(self, value):
        # Валидация ИИН (Идентификационный номер налогоплательщика)
        if not value.isdigit() or len(value) != 12:
            raise serializers.ValidationError("ИИН должен состоять из 12 цифр.")
        return value

    def validate_sic(self, value):
        # Валидация СИК (Страховой идентификационный номер)
        if(value != None and value != ""):
            if not value.isdigit() or len(value) != 11:
                raise serializers.ValidationError("СИК должен состоять из 11 цифр.")
        return value

    class Meta:
        model = IndividualClient
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    sector = SectorEconSerializer(read_only=True)
    org_form = OrgFormSerializer(read_only=True)
    form_property = FormPropertySerializer(read_only=True)
    okpo = serializers.CharField(read_only=True)
    reg_date = serializers.DateField(read_only=True)
    reg_org = serializers.CharField(read_only=True)
    certify_ser = serializers.CharField(read_only=True)
    certify_num = serializers.CharField(read_only=True)
    owners = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    """Юр лица"""
    def validate_short_name(self, value):
        """
        Валидация поля short_name: проверяем, что короткое наименование не пустое.
        """
        if not value.strip():
            raise serializers.ValidationError("Короткое наименование не может быть пустым.")
        return value

    def validate_full_name(self, value):
        """
        Валидация поля full_name: проверяем, что полное наименование не пустое.
        """
        if not value.strip():
            raise serializers.ValidationError("Полное наименование не может быть пустым.")
        return value

    # def validate_okpo(self, value):
    #     """
    #     Валидация поля okpo: проверяем, что ОКПО состоит из 8 или 10 цифр.
    #     """
    #     if not value.isdigit() or len(value) not in (8, 10):
    #         raise serializers.ValidationError("ОКПО должен состоять из 8 или 10 цифр.")
    #     return value

    def validate_reg_num(self, value):
        """
        Валидация поля reg_num: проверяем, что регистрационный номер не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Регистрационный номер не может быть пустым.")
        return value

    # def validate_reg_date(self, value):
    #     """
    #     Валидация поля reg_date: проверяем, что дата регистрации не находится в будущем.
    #     """
    #     if value > timezone.now().date():
    #         raise serializers.ValidationError("Дата регистрации не может быть в будущем.")
    #     return value

    # def validate_certify_ser(self, value):
    #     """
    #     Валидация поля certify_ser: проверяем, что серия рег. удостоверения не пустая.
    #     """
    #     if not value.strip():
    #         raise serializers.ValidationError("Серия рег. удостоверения не может быть пустой.")
    #     return value

    # def validate_certify_num(self, value):
    #     """
    #     Валидация поля certify_num: проверяем, что номер рег. удостоверения не пустой.
    #     """
    #     if not value.strip():
    #         raise serializers.ValidationError("Номер рег. удостоверения не может быть пустым.")
    #     return value
    class Meta:
        model = Company
        fields = "__all__"

class CompanyInClientRetrieveSerializer(serializers.ModelSerializer):
    """Юр лица"""
    sector = SectorEconSerializer(read_only=True)
    org_form = OrgFormSerializer(read_only=True)
    form_property = FormPropertySerializer(read_only=True)

    class Meta:
        model = Company
        exclude = ['owners']


class AccountSerializer(serializers.ModelSerializer):
    """Счета"""

    def validate_amount(self, value):
        """
        Валидация поля amount: проверяем, что остаток на счете неотрицательный.
        """
        if value < 0:
            raise serializers.ValidationError("Остаток на счете не может быть отрицательным.")
        return value

    def validate_acc_num(self, value):
        """
        Валидация поля acc_num: проверяем, что номер счета не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Номер счета не может быть пустым.")
        return value

    def validate_date_open(self, value):
        """
        Валидация поля date_open: проверяем, что дата открытия счета не находится в будущем.
        """
        if value and value > timezone.now().date():
            raise serializers.ValidationError("Дата открытия счета не может быть в будущем.")
        return value

    def validate_date_close(self, value):
        """
        Валидация поля date_close: проверяем, что дата закрытия счета не меньше даты открытия.
        """
        date_open_str = self.initial_data.get('date_open')
        date_open = datetime.datetime.strptime(date_open_str, "%Y-%m-%d").date()

        if value and date_open and value < date_open:
            raise serializers.ValidationError("Дата закрытия счета не может быть меньше даты открытия.")
        return value
    
    class Meta:
        model = Account
        fields = "__all__"


class DocsSerializer(serializers.ModelSerializer):
    """Документы"""
    
    def validate_number(self, value):
        """
        Валидация поля number: проверяем, что номер документа не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Номер документа не может быть пустым.")
        
        if not re.match(r'^[0-9]+$', value):
            raise serializers.ValidationError("Номер документа может содержать только цифры.")
        
        return value

    def validate_series(self, value):
        """
        Валидация поля series: проверяем, что серия документа не пустая.
        """
        if not value.strip():
            raise serializers.ValidationError("Серия документа не может быть пустой.") 
        
        if not re.match(r'^[a-zA-Z0-9]+$', value):
            raise serializers.ValidationError("Серия документа может содержать только латинские буквы и цифры.")
        
        return value

    def validate_start_date(self, value):
        """
        Валидация поля start_date: проверяем, что дата начала не находится в будущем.
        """
        if value > timezone.now().date():
            raise serializers.ValidationError("Дата начала не может быть в будущем.")
        
        if value.year < 1900:
            raise serializers.ValidationError("Дата не может быть раньше 1900 года.")
        
        return value

    def validate_end_date(self, value):
        """
        Валидация поля end_date: проверяем, что дата окончания не меньше даты начала.
        """
        start_date_str = self.initial_data.get('start_date', value)
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        
        if value < start_date:
            raise serializers.ValidationError("Дата окончания не может быть меньше даты начала.")
        return value

    def validate_issued_by(self, value):
        """
        Валидация поля issued_by: проверяем, что поле не пустое и содержит только
        буквы английского, русского и казахского алфавитов, а также пробелы.
        """
        if not value.strip():
            raise serializers.ValidationError("Поле 'Кем выдан' не может быть пустым.")

        # Проверяем, что в поле issued_by нет лишних символов, кроме букв и пробелов
        if not re.match(r'^[a-zA-Zа-яА-Яғқңәіһүұққ\s]+$', value):
            raise serializers.ValidationError("Поле 'Кем выдан' может содержать только буквы английского, русского и казахского алфавитов, а также пробелы.")

        return value

    class Meta:
        model = Docs
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    """Контакты"""

    def validate_value(self, value):
        """
        Валидация поля value: проверяем, что поле не пустое,
        а также что содержимое является либо электронной почтой, либо номером телефона.
        """
        if not value.strip():
            raise serializers.ValidationError("Поле 'Значение' не может быть пустым.")

        # Получаем значение типа контакта из данных сериализации
        contact_type = self.initial_data.get('contact_type')

        # Проверка на электронную почту
        if contact_type == "3" or contact_type == "5":
            if not re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
                raise serializers.ValidationError("Некорректный формат электронной почты.")

        # Проверка на номер телефона
        if contact_type == "1" or contact_type == "2" or contact_type == "4":
            if not re.match(r'^\+?[0-9]+$', value):
                raise serializers.ValidationError("Некорректный формат номера телефона.")

        return value
    
    class Meta:
        model = Contact
        fields = "__all__"


class ContactRetrieveSerializer(serializers.ModelSerializer):
    """Контакты"""
    contact_type = ContactTypeSerializer(read_only=True)
    class Meta:
        model = Contact
        fields = "__all__"

class IndividualClientRetrieveSerializer(serializers.ModelSerializer):
    """Физическое лицо"""
    country = CountrySerializer(read_only=True)
    client_category = ClientCategorySerializer(read_only=True)
    place_of_birth = AreasSerializer(read_only=True)

    class Meta:
        model = IndividualClient
        fields = "__all__"
    
class ClientAddBalanceToAccountSerializer(serializers.Serializer):
    """Пополнение счета клиента"""
    amount = serializers.CharField(required=True)


class ClientRetrieveSerializer(serializers.ModelSerializer):
    """Клиенты"""
    individual_client = IndividualClientRetrieveSerializer(required=False)
    docs = DocsSerializer(many=True, read_only=True)
    addresses = AddressRetrieveSerializer(many=True, read_only=True)
    contacts = ContactRetrieveSerializer(many=True, read_only=True)
    companies = CompanyInClientRetrieveSerializer(many=True, read_only=True, source="company_owners")

    class Meta:
        model = Client
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):  
    # id = serializers.UUIDField(read_only=True)
    individual_client = IndividualClientSerializer(required=True)
    category_type = CategoryTypeSerializer(read_only=True)
    class Meta:
        model = Client
        fields = "__all__"
    
    def create(self, validated_data):
        individual_client_data = validated_data.pop('individual_client', None)

        if individual_client_data:
            try:
                individual_client = IndividualClient.objects.create(**individual_client_data)
                validated_data['individual_client'] = individual_client
            except Exception as e:
                raise serializers.ValidationError({"error":"Данные для физ лица некорректны", "error_message": e})  
        else:
            raise serializers.ValidationError({"error":"Данные для физ лица не предоставлены"})

        client = Client.objects.create(**validated_data)

        return client
    
    def update(self, instance, validated_data):
        individual_client_data = validated_data.pop('individual_client', None)

        reg_number = individual_client_data.get('reg_number', instance.individual_client.reg_number)

        if reg_number != instance.individual_client.reg_number:
            instance.individual_client.reg_number = reg_number
        

        instance.individual_client.full_name = individual_client_data.get('full_name', instance.individual_client.full_name)
        instance.individual_client.gender = individual_client_data.get('gender', instance.individual_client.gender)
        instance.individual_client.iin = individual_client_data.get('iin', instance.individual_client.iin)
        instance.individual_client.rnn = individual_client_data.get('rnn', instance.individual_client.iin)
        instance.individual_client.sic = individual_client_data.get('sic', instance.individual_client.iin)
        instance.individual_client.date_of_birth = individual_client_data.get('date_of_birth', instance.individual_client.date_of_birth)
        instance.individual_client.place_of_birth = individual_client_data.get('place_of_birth', instance.individual_client.place_of_birth)
        instance.individual_client.country = individual_client_data.get('country', instance.individual_client.country)
        instance.individual_client.client_category = individual_client_data.get('client_category', instance.individual_client.client_category)
        try:
            instance.individual_client.save()
        except Exception as e:
            raise serializers.ValidationError({"error":"Данные для физ лица некорректны", "error_message": e})
        return instance


class CompanyRetrieveSerializer(serializers.ModelSerializer):
    """Юр лица"""
    sector = SectorEconSerializer(read_only=True)
    org_form = OrgFormSerializer(read_only=True)
    form_property = FormPropertySerializer(read_only=True)
    owners = ClientSerializer(read_only=True, many=True)
    class Meta:
        model = Company
        fields = "__all__"


class CompanyAddOwnerSerializer(serializers.Serializer):
    """Добавление владельца"""
    owner_id = serializers.CharField(required=True)