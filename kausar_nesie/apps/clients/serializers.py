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

    def validate_name(self, value):
        """
        Валидация поля name: проверяем, что имя содержит только буквы и дефисы, если указано.
        """
        if not value:
            raise serializers.ValidationError("Поле 'Имя' обязательно.")
        if not re.match(r'^[A-Za-zА-Яа-я-]+$', value):
            raise serializers.ValidationError("Поле 'Имя' должно содержать только буквы и дефисы.")
        return value

    def validate_surname(self, value):
        """
        Валидация поля surname: проверяем, что фамилия содержит только буквы и дефисы, если указана.
        """
        if not value:
            raise serializers.ValidationError("Поле 'Фамилия' обязательно.")
        if not re.match(r'^[A-Za-zА-Яа-я-]+$', value):
            raise serializers.ValidationError("Поле 'Фамилия' должно содержать только буквы и дефисы.")
        return value

    def validate_middle_name(self, value):
        """
        Валидация поля middle_name: проверяем, что отчество содержит только буквы и дефисы, если указано.
        """
        if value is None:
            return value  # Разрешаем значение None (null=True)

        if not re.match(r'^[A-Za-zА-Яа-я-]+$', value):
            raise serializers.ValidationError("Поле 'Отчество' должно содержать только буквы и дефисы.")
        return value
    
    def validate_date_of_birth(self, value):
        # Валидация даты рождения, чтобы не была в будущем
        if value > timezone.now().date():
            raise serializers.ValidationError("Дата рождения не может быть в будущем.")
        return value

    def validate_rnn(self, value):
        # Валидация РНН (Регистрационный номер налогоплательщика)
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
        if not value.isdigit() or len(value) != 11:
            raise serializers.ValidationError("СИК должен состоять из 11 цифр.")
        return value

    # def validate_gender(self, value):
    #     """
    #     Валидация поля gender: проверяем, что выбран корректный вариант пола.
    #     """
    #     valid_genders = [choice[0] for choice in IndividualClient.GENDER_CHOICES]
    #     if value not in valid_genders:
    #         raise serializers.ValidationError("Выберите корректный пол.")
    #     return value

    class Meta:
        model = IndividualClient
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
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

    def validate_okpo(self, value):
        """
        Валидация поля okpo: проверяем, что ОКПО состоит из 8 или 10 цифр.
        """
        if not value.isdigit() or len(value) not in (8, 10):
            raise serializers.ValidationError("ОКПО должен состоять из 8 или 10 цифр.")
        return value

    def validate_reg_num(self, value):
        """
        Валидация поля reg_num: проверяем, что регистрационный номер не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Регистрационный номер не может быть пустым.")
        return value

    def validate_reg_date(self, value):
        """
        Валидация поля reg_date: проверяем, что дата регистрации не находится в будущем.
        """
        if value > timezone.now().date():
            raise serializers.ValidationError("Дата регистрации не может быть в будущем.")
        return value

    def validate_certify_ser(self, value):
        """
        Валидация поля certify_ser: проверяем, что серия рег. удостоверения не пустая.
        """
        if not value.strip():
            raise serializers.ValidationError("Серия рег. удостоверения не может быть пустой.")
        return value

    def validate_certify_num(self, value):
        """
        Валидация поля certify_num: проверяем, что номер рег. удостоверения не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Номер рег. удостоверения не может быть пустым.")
        return value
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
        return value

    def validate_series(self, value):
        """
        Валидация поля series: проверяем, что серия документа не пустая.
        """
        if not value.strip():
            raise serializers.ValidationError("Серия документа не может быть пустой.")
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
        Валидация поля issued_by: проверяем, что поле не пустое.
        """
        if not value.strip():
            raise serializers.ValidationError("Поле 'Кем выдан' не может быть пустым.")
        return re.sub(r'\D', '', value)
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

        # Проверка на электронную почту
        if re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            return value

        # Проверка на номер телефона
        if re.match(r'^\+?[0-9]+$', value):
            return value

        raise serializers.ValidationError("Некорректный формат 'Значения'. Пожалуйста, введите корректный адрес электронной почты или номер телефона.")

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
    individual_client = IndividualClientSerializer(required=True)
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


class CompanyRetrieveSerializer(serializers.ModelSerializer):
    """Юр лица"""
    sector = SectorEconSerializer(read_only=True)
    org_form = OrgFormSerializer(read_only=True)
    form_property = FormPropertySerializer(read_only=True)
    owners = ClientSerializer(read_only=True, many=True)
    class Meta:
        model = Company
        fields = "__all__"

