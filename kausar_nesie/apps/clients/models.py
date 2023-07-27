from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class IndividualClient(models.Model):
    """Физическое лицо"""
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
    )

    reg_number = models.CharField(max_length=255, unique=True, verbose_name="Номер peг.", blank=True, null=False)
    full_name = models.CharField(max_length=255, verbose_name="Полное имя", blank=True, null=False)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=False, blank=False, verbose_name=("Пол"))
    date_of_birth = models.DateField(verbose_name="Дата рождения", null=False, blank=True, default=timezone.now)
    place_of_birth = models.ForeignKey('catalog.Areas', verbose_name="Место рождения", null=False, blank=False, on_delete=models.CASCADE)
    rnn = models.CharField(max_length=255, verbose_name="РНН", blank=True)
    iin = models.CharField(max_length=255, verbose_name="ИИН", blank=True)
    sic = models.CharField(max_length=255, verbose_name="СИК", blank=True)
    is_resident = models.BooleanField(default=True, verbose_name="Резидент", blank=True)
    country = models.ForeignKey('catalog.Country', verbose_name="Страна", null=True, blank=True,on_delete=models.SET_NULL)
    client_category = models.ForeignKey('catalog.ClientCategory', verbose_name="Категория клиента", null=True, blank=True,
                                      on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Физическое лицо"
        verbose_name_plural = "Физические лица"

class Company(models.Model):
    """Юридические лица"""

    short_name = models.CharField(max_length=2000, verbose_name="Короткое наименование", blank=True)
    full_name = models.CharField(max_length=2000, verbose_name="Полное наименование", blank=True)
    sector = models.ForeignKey('catalog.SectorEcon', verbose_name="Сектор Экономики", null=True, blank=True,
                               on_delete=models.CASCADE)
    org_form = models.ForeignKey('catalog.OrgForm', verbose_name="Форма предприятия", null=True, blank=True,
                                 on_delete=models.CASCADE)
    form_property = models.ForeignKey('catalog.FormProperty', verbose_name="Форма собс.", null=True, blank=True,
                                      on_delete=models.CASCADE)
    okpo = models.CharField(max_length=255, verbose_name="ОКПО", blank=True)
    reg_num = models.CharField(max_length=255, verbose_name="Регистрационный номер", blank=True)
    reg_date = models.DateField(verbose_name="Дата регистрации", blank=True, default=timezone.now)
    reg_org = models.CharField(max_length=255, verbose_name="Регистрирующий орган", blank=True)
    certify_ser = models.CharField(max_length=20, verbose_name="Серия рег. удостоверения", blank=True)
    certify_num = models.CharField(max_length=20, verbose_name="Номер рег. удостоврения", blank=True)

    owners = models.ManyToManyField('Client', related_name='company_owners', blank=True)
    def __str__(self):
        return f"{self.short_name}"

    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"

class Client(models.Model):
    """Клиенты"""
    emp = models.ForeignKey(User, related_name="manager", verbose_name="Идентификатор пользователя создавшего запись",
                            on_delete=models.SET_NULL, blank=True, null=True)
    insert_date = models.DateField(auto_now_add=True, verbose_name='Дата ввода записи', editable=False)
    individual_client = models.OneToOneField(IndividualClient, on_delete=models.CASCADE, null=True, blank=True)
    category_type = models.ForeignKey('catalog.ClientCategory', verbose_name="Категория клиента", null=True, blank=True,
                                     on_delete=models.CASCADE)
    def __str__(self):
        if(self.individual_client):
            return f"{self.individual_client.full_name}"
        return f"{self.id}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class Docs(models.Model):
    """Документы"""
    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name='docs')
    identity_card_type = models.ForeignKey('catalog.IdcardType', verbose_name="Идентификатор типа документа",
                             on_delete=models.CASCADE,
                             blank=True, null=True)
    number = models.CharField(max_length=255, verbose_name="Номер", blank=True)
    start_date = models.DateField(verbose_name="Дата начала", blank=True, default=timezone.now)
    end_date = models.DateField(verbose_name="Дата окончания", blank=True, default=timezone.now)
    issued_by = models.CharField(max_length=255, verbose_name="Кем выдан", blank=True)
    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"


class Address(models.Model):
    """Адреса клиента"""
    client = models.ForeignKey(Client, verbose_name="Адрес физицеского лица", on_delete=models.CASCADE, related_name='addresses')
    post_index = models.CharField(max_length=10, verbose_name="Почтовый индекс", null=True, blank=True)
    country = models.ForeignKey('catalog.Country', verbose_name="Страна", null=True, blank=True, on_delete=models.CASCADE)
    cities = models.ForeignKey('catalog.Cities', verbose_name="Город", null=True, blank=True, on_delete=models.CASCADE)
    areas = models.ForeignKey('catalog.Areas', verbose_name="Область", null=True, blank=True, on_delete=models.CASCADE)
    district = models.ForeignKey('catalog.District', verbose_name="Район города", blank=True, null=False, on_delete=models.CASCADE)
    street = models.ForeignKey('catalog.Street', verbose_name="Улица", blank=True, null=True, on_delete=models.CASCADE)
    housing = models.CharField(max_length=255, verbose_name="Корпус", blank=True, null=True)
    house = models.CharField(max_length=255, verbose_name="Дом", blank=True, null=False)
    flat = models.CharField(max_length=255, verbose_name="Квартира", blank=True, null=True)
    addr_type = models.ForeignKey('catalog.AddressType', verbose_name="Тип адреса", on_delete=models.CASCADE,
                                  blank=True, null=False)

    def __str__(self):
        return f"{self.street} {self.house}"

    class Meta:
        verbose_name = "Адрес клиента"
        verbose_name_plural = "Адреса клиента"



class Account(models.Model):
    """Счета"""

    client = models.ForeignKey(Client, verbose_name="Идентификатор клиента", on_delete=models.CASCADE,
                               blank=False, null=False, related_name='client')
    account_type_id = models.ForeignKey('catalog.AccountType', verbose_name="Идентификатор типа счета",
                                        on_delete=models.CASCADE,
                                        blank=False, null=False)

    currency = models.ForeignKey('catalog.Currencies', verbose_name="Идентификатор валюты", on_delete=models.CASCADE,
                                 blank=True, null=False, default=1)
    amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Остаток на счете", null=False,
                                 blank=False)
    acc_num = models.CharField(max_length=255, verbose_name="Номер счета", blank=True, null=False)
    base_account = models.ForeignKey('catalog.BaseAccount', verbose_name="Идентификатор базового счета",
                                     on_delete=models.CASCADE,
                                     blank=False, null=False, default=1)
    date_open = models.DateField(verbose_name="Дата открытия счета", null=True, blank=True)
    date_close = models.DateField(verbose_name="Дата закрытия счета", null=True, blank=True)

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    departament = models.ForeignKey('catalog.Departament', verbose_name="Идентификатор департамента",
                                    on_delete=models.CASCADE,
                                    blank=True, null=True)
    client_r = models.ForeignKey(Client, verbose_name="Доверенный клиент", on_delete=models.CASCADE,
                                 blank=True, null=True, related_name='client_r')
    amount_nat = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Остаток в нац.покрытии", null=False,
                                     blank=False)

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"

class Contact(models.Model):
    """Контакты"""

    client = models.ForeignKey("Client", verbose_name="Контакт физического лица", on_delete=models.CASCADE, related_name='contacts')
    contact_type = models.ForeignKey("catalog.ContactType", verbose_name="Тип контакта", on_delete=models.CASCADE, related_name='contact_type', blank=True)
    value = models.CharField(max_length=255, verbose_name="Значение", blank=True)

    def __str__(self):
        return f"{self.contact_type} {self.value}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"



# class IdCard(models.Model):
#     """Документы удостоверющие данные клиента"""
#     id_card_type = models.ForeignKey('catalog.IdcardType', verbose_name="Идентификатор типа документа",
#                              on_delete=models.CASCADE,
#                              blank=True, null=True)
#     date_begin = models.DateField(verbose_name="Дата начала действия", null=False, blank=False)
#     date_end = models.DateField(verbose_name="дата окончания действия", null=True, blank=True)
#     who = models.TextField(verbose_name="Кем выдан", blank=True, null=True)
#     num_passport = models.TextField(verbose_name="Номер документа", blank=False, null=False)
#     serial_passport = models.TextField(verbose_name="Серия документа", blank=True, null=True)
#     client = models.ForeignKey(Client, verbose_name="Идентификатор клиента", on_delete=models.CASCADE,
#                                blank=True, null=True)
#     scan = models.FileField(upload_to='docs/', verbose_name="Сканированная копия документа", null=False, blank=False)

#     def __str__(self):
#         return f"{self.client}"

#     class Meta:
#         verbose_name = "Документ удостоверяющое данные клиента"
#         verbose_name_plural = "Документы удостоверяющие данные клиента"
