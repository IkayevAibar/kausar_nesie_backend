from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()




class AddressType(models.Model):
    """Справочник. Типы адресов"""

    name = models.CharField(max_length=255, verbose_name="Название", blank=True)
    code = models.CharField(max_length=255, verbose_name="Населенный пункт", blank=True)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип адресов"
        verbose_name_plural = "Справочник. Типы адресов"


class Areas(models.Model):
    """Справочник. Области"""

    name = models.CharField(max_length=255, verbose_name="Название", blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Справочник. Область"
        verbose_name_plural = "Справочник. Области"

class Cities(models.Model):
    """Справочник. Населенные пункты"""

    area = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name="Область", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Название", blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Справочник. Населенный пункт"
        verbose_name_plural = "Справочник. Населенные пункты"

class District(models.Model):
    """Справочник. Районы"""

    city = models.ForeignKey(Cities, on_delete=models.CASCADE, verbose_name="Населенный пункт", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Название", blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Справочник. Район"
        verbose_name_plural = "Справочник. Районы"


class Street(models.Model):
    """Справочник. Улицы"""

    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name="Район", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Название", blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Справочник. Улица"
        verbose_name_plural = "Справочник. Улицы"

class ClientCategory(models.Model):
    """Справочник. Категории клиентов"""

    name = models.CharField(max_length=255, verbose_name="Название", blank=True)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Категория клиентов"
        verbose_name_plural = "Категории клиентов"


class CategoryType(models.Model):
    """Справочник. Виды категорий качества"""

    name = models.CharField(max_length=255, verbose_name="Название", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)
    provision_prc = models.FloatField(verbose_name="provision_prc", blank=True, null=True)
    provision_from = models.FloatField(
        verbose_name="Минимальный размер провизии по стандарту национального банка",
        blank=True, null=True)
    provision_to = models.FloatField(
        verbose_name="Максимальный размер провизии по стандарту национального банка",
        blank=True, null=True)
    delay_days_to = models.IntegerField(verbose_name="delay_days_to",
                                        blank=True, null=True)
    delay_days_from = models.IntegerField(verbose_name="delay_days_from",
                                          blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Вид категории качества"
        verbose_name_plural = "Справочник. Виды категорий качества"


class WorkType(models.Model):
    """Справочник. Тип занятости"""

    name = models.CharField(max_length=255, verbose_name="Название", blank=True)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип занятости"
        verbose_name_plural = "Справочник. Типы занятости"


class TransactionType(models.Model):
    """Справочник. Типы транзакций"""

    name = models.CharField(max_length=255, verbose_name="Название", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)
    num_pattern = models.CharField(max_length=255, verbose_name="Шаблон номера документа", blank=True)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип транзакций"
        verbose_name_plural = "Справочник. Типы транзакций"


class Status(models.Model):
    """Справочник. Статусы"""

    name = models.CharField(max_length=255, verbose_name="Наименование статуса", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код статуса", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Статус"
        verbose_name_plural = "Справочник. Статусы"


class SectorEcon(models.Model):
    """Справочник. Сектора экономики"""

    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)
    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Сектор экономики"
        verbose_name_plural = "Справочник. Сектора экономики"


class ProjectType(models.Model):
    """Справочник. Типы проектов"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип проектов"
        verbose_name_plural = "Справочник. Типы проектов"


class PositionType(models.Model):
    """Справочник. Тип должности"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип должности"
        verbose_name_plural = "Справочник. Типы должности"


class PeriodType(models.Model):
    """Справчоник. Типы периодов"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип периодов"
        verbose_name_plural = "Справочник. Типы периодов"


class PaymentType(models.Model):
    """Справочник. КНП"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник КНП"
        verbose_name_plural = "Справочник КНП"


class OrgForm(models.Model):
    """Справочник. Форма предприятия"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Форма предприятия"
        verbose_name_plural = "Справочник. Форма предприятия"


class LinkType(models.Model):
    """Справочник. Типы связи договоров"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип связи договоров"
        verbose_name_plural = "Справочник. Типы связи договоров"


class LineType(models.Model):
    """Справочник. Типы кредитных линий"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип кредитных линий"
        verbose_name_plural = "Справочник. Типы кредитных линий"


class IdcardType(models.Model):
    """Справочник. Типы документов"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник.Тип документов"
        verbose_name_plural = "Справочник. Типы документов"


class FormProperty(models.Model):
    """Справочник. Форма собственности"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Форма собственности"
        verbose_name_plural = "Справочник. Формы собственности"


class Currencies(models.Model):
    """Справочник. Валюты"""
    HB = 1
    CKB = 2
    DBB = 3
    TYPE_CHOICES = (
        (HB, 'НВ'),
        (CKB, 'СКВ'),
        (DBB, 'ДВВ'),
    )

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    alpha_code = models.CharField(max_length=3, verbose_name="Буквенный код валюты", blank=True, null=False)
    num_code = models.CharField(max_length=3, verbose_name="Цифровой код валюты", blank=True, null=False)
    curr_type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICES, null=True, blank=True, verbose_name=("Тип валюты")
    )

    def __str__(self):
        return f"{self.name} {self.alpha_code} {self.num_code}"

    class Meta:
        verbose_name = "Справочник. Валюта"
        verbose_name_plural = "Справочник. Валюты"


class CreditTarget(models.Model):
    """Справочник. Цели кредитования"""

    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)
    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Цель кредитования"
        verbose_name_plural = "Справочник. Цели кредитования"


class CreditSource(models.Model):
    """Справочник. Источник кредитования"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Источник кредитования"
        verbose_name_plural = "Справочник. Источники кредитования"


class Country(models.Model):
    """Справочник. Государства"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=3, verbose_name="Код", blank=True, null=False)
    alfa_3 = models.CharField(max_length=3, verbose_name="Код алфа - 3", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Государство"
        verbose_name_plural = "Справочник. Государства"


class Counters(models.Model):
    """Справочник. Счетчики"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=255, verbose_name="Код", blank=True, null=False)
    value = models.IntegerField(verbose_name="Значение", blank=True, null=False)
    max_value = models.IntegerField(verbose_name="максимальное значение", blank=True, null=True)
    auto_reset = models.BooleanField(verbose_name="Автосброс при достижении максимального значения", \
                                     null=True, default=False)
    period_type = models.ForeignKey(PeriodType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Счетчик"
        verbose_name_plural = "Справочник. Счетчики"


class ContactType(models.Model):
    """Справочник. Типы контактов"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=3, verbose_name="Код", blank=True, null=False)

    has_child = models.BooleanField(verbose_name="Может иметь потомков", \
                                    null=False, default=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип контактов"
        verbose_name_plural = "Справочник. Типы контактов"


class CollateralType(models.Model):
    """Справочник. Типы залога"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=4, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип залога"
        verbose_name_plural = "Справочник. Типы залога"


class DeptType(models.Model):
    """Справочник. Виды задолженностей"""
    TYPE_CHOICES = (
        ("S", 'системная'),

    )
    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=50, verbose_name="Код", blank=True, null=False)
    category = models.CharField(max_length=1, choices=TYPE_CHOICES,
                                verbose_name="Категория задолженности (S - системная)", blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Виды задолженностей"
        verbose_name_plural = "Справочник. Виды задолженностей"


class Bank(models.Model):
    """Справочник. Банки"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    bic = models.CharField(max_length=3, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.bic}"

    class Meta:
        verbose_name = "Справочник. Банк"
        verbose_name_plural = "Справочник. Банки"


class Calculate(models.Model):
    """Справочник. Тип расчета"""

    first = 0
    second = 1
    three = 2
    four = 3
    TYPE_CHOICES = (
        (first, '360/30'),
        (second, '365/30'),
        (three, '360/ВВ'),
        (four, '365/DD'),
    )
    name = models.CharField(max_length=2000, verbose_name="Наименование типа расчета", blank=True, null=False)
    code = models.CharField(max_length=100, verbose_name="Код типа расчета", blank=True, null=False)
    calc_type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES,
                                                 null=True, blank=True, verbose_name=(
            "Тип начисления (0 - 360/30 1 - 365/30 2- 360/ВВ, 3 - 365/DD)")
                                                 )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Справочник. Тип расчета"
        verbose_name_plural = "Справочник. Тип расчета"


class BaseAccount(models.Model):
    """План счетов"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=10, verbose_name="Код", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "План счета"
        verbose_name_plural = "План счетов"


class AccountPattern(models.Model):
    """Шаблоны номеров счетов"""

    O = "o"
    V = "v"
    R = "r"

    TYPE_CHOICES = (
        (O, 'владелец организация'),
        (V, 'владелец клиент'),
        (R, 'владелец организация, клиент для расчетов'),
    )

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=20, verbose_name="Код", blank=True, null=False)
    patt_num = models.CharField(max_length=255, verbose_name="шаблон номера счета", blank=True, null=False)
    patt_name = models.CharField(max_length=2000, verbose_name="шаблон наименования счета", blank=True, null=True)
    subject_type = models.CharField(
        verbose_name="Тип субъекта для открытия счета (o/v/r - владелец организация/владелец клиент/владелец организация,клиент для расчетов )",
        max_length=2, choices=TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"


class AccountType(models.Model):
    """Справочник. Типы счетов"""
    A = "A"
    P = "P"
    T = "T"
    N = "N"
    n_open = "n"
    o_open = "o"
    od_open = "od"
    oc_open = "oc"
    op_open = "op"
    TYPE_CHOICES = (
        (A, 'Active'),
        (P, 'Passive'),
        (T, 'Technical'),
        (N, 'Any'),
    )

    CURRENCY_TYPE_CHOICES = (
        (0, 'не указано'),
        (1, 'нац'),
        (2, 'валюта продукта'),
        (3, "в указанной валюте"),
    )
    OPEN_TYPE_CHOICES = (
        (n_open, 'не открывать'),
        (o_open, 'открыть'),
        (od_open, 'открыть на подразделение'),
        (oc_open, "открыть на клиента"),
        (op_open, "открыть на продукт"),
    )
    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=100, verbose_name="Код", blank=True, null=False)
    acc_type = models.CharField(max_length=1,
                                verbose_name="Тип счета (A - Active, P - Passive, T - Technical, N - Any )",
                                choices=TYPE_CHOICES)
    acc_pattern = models.ForeignKey(AccountPattern, on_delete=models.SET_NULL, null=True, blank=True)
    open_type = models.CharField(max_length=5,
                                 verbose_name="Тип открытия (n - не открывать, o - открыть, od/oc/op - открыть на подразделение/клиента/продукт(договор)",
                                 choices=OPEN_TYPE_CHOICES, null=True, blank=True)
    def_currency = models.PositiveSmallIntegerField(
        choices=CURRENCY_TYPE_CHOICES, null=True, blank=True, verbose_name=(
            "Настройка валюты для открытия (0 - не указано, 1- нац, 2 - валюта продукта, 3 - в указанной валютеы")
    )
    currency = models.ForeignKey(Currencies, verbose_name="Идентификатор валюты", on_delete=models.SET_NULL, blank=True,
                                 null=True)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Тип счетов"
        verbose_name_plural = "Справочник. Типы счетов"


class Departament(models.Model):
    """Справочник. Отделы"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    code = models.CharField(max_length=10, verbose_name="Код", blank=True, null=False)
    company = models.ForeignKey("clients.Company", verbose_name="Идентификатор юр.лица", on_delete=models.SET_NULL,
                                blank=True,
                                null=True)
    liferay_id = models.IntegerField(verbose_name="Сообщество в портале", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Отдел"
        verbose_name_plural = "Справочник. Отделы"


class PaymentRule(models.Model):
    """Правила гашения"""
    name = models.TextField(verbose_name="Наименование правила гашения", blank=True, null=False)
    code = models.CharField(max_length=100, verbose_name="Код правила гашения", blank=True, null=False)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Правило гашения"
        verbose_name_plural = "Правила гашения"


class CreditType(models.Model):
    """Справочник. Типы кредитов"""

    CURRENCY_TYPE_CHOICES = (
        (1, 'проценты по факту'),
        (2, 'проценты за весь период')
    )
    name = models.TextField(verbose_name="Наименование типа кредита", blank=True, null=False)
    code = models.CharField(max_length=100, verbose_name="Код типа кредита", blank=True, null=False)
    min_period = models.IntegerField(verbose_name="Минимальный срок кредитования", blank=True, null=False)
    max_period = models.IntegerField(verbose_name="Максимальный срок кредитования", blank=True, null=False)
    min_amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Минимальная сумма кредита")
    max_amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Максимальный сумма кредита")
    need_collateral = models.BooleanField(verbose_name="Требуется залог", blank=True, null=False, default=False)
    need_guarantor = models.IntegerField(verbose_name="Количетво гарантов", blank=True, null=False)
    need_coclient = models.IntegerField(verbose_name="Количество необходимых созаемщиков", blank=True, null=False)
    penalty_period = models.IntegerField(verbose_name="Мораторий на досрочное погашение", blank=True, null=False)
    rule = models.ForeignKey(PaymentRule, verbose_name="Идентификатор правила платежа",
                             on_delete=models.CASCADE,
                             blank=True, null=False)
    currency = models.ForeignKey(Currencies, verbose_name="Идентификатор валюты", on_delete=models.CASCADE,
                                 blank=True, null=False)
    line_type = models.ForeignKey(LineType, verbose_name="Типы кредитных линий", on_delete=models.CASCADE,
                                  blank=True, null=True)
    plan_type = models.IntegerField(verbose_name="Тип плана (Аннуитет, равными долями, ...)", blank=True, null=True)
    num_pattern = models.CharField(max_length=30, verbose_name="Шаблон номера договора", blank=True, null=True)
    project_type = models.ForeignKey(ProjectType, verbose_name="Программа кредитования",
                                     on_delete=models.CASCADE,
                                     blank=True, null=False)
    credit_source = models.ForeignKey(CreditSource, verbose_name="Источник кредитования",
                                      on_delete=models.CASCADE,
                                      blank=True, null=False)
    early_prc_mode = models.PositiveSmallIntegerField(
        choices=CURRENCY_TYPE_CHOICES, null=True, blank=True, verbose_name=(
            "Условия досрочки (1 - проценты по факту, 2 - проценты за весь период)")
    )

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        verbose_name = "Справочник. Типы кредитов"
        verbose_name_plural = "Справочник. Типы кредитов"


class InterestScheme(models.Model):
    """Справочник. Схемы начисления процентов"""

    name = models.CharField(max_length=255, verbose_name="Наименование", blank=True, null=False)
    individual = models.BooleanField(verbose_name="индивидуальная",
                                     null=False, default=False)
    calculate = models.ForeignKey(Calculate, verbose_name="тип расчета", blank=True, null=True,
                                  on_delete=models.SET_NULL)
    period_type = models.ForeignKey(PeriodType, verbose_name="period_type_id", blank=True, null=True,
                                    on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Справочник. Схемы начисления процентов"
        verbose_name_plural = "Справочник. Схемы начисления процентов"


class InterestRate(models.Model):
    """Ставки. Схемы начисления процентов"""
    interest_scheme = models.ForeignKey(InterestScheme, verbose_name="Процентная схема", blank=True, null=True,
                                        on_delete=models.SET_NULL)
    date_begin = models.DateField(verbose_name="дата начала действия", null=False, blank=False)
    date_end = models.DateField(verbose_name="дата окончания действия", null=True, blank=True)
    rate = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="ставка процента / сумма", null=True,
                               blank=True)
    is_rate = models.BooleanField(verbose_name="признак процента",
                                  null=True, default=False)
    forumula = models.TextField(verbose_name="Выражение для расчета суммы тарифа", blank=True, null=True)

    class Meta:
        verbose_name = "Ставки. Схемы начисления процентов"
        verbose_name_plural = "Ставки. Схемы начисления процентов"


class InterestJournal(models.Model):
    """Журнал начисленных процентов"""
    date_begin = models.DateField(verbose_name="Дата начала расчета", null=False, blank=False)
    date_end = models.DateField(verbose_name="Дата окончания расчета", null=False, blank=False)
    days = models.IntegerField(verbose_name="Количество дней", blank=False, null=False)
    amount_for_calc = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Сумма для начисления",
                                          null=True,
                                          blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Сумма процентов (округленная)",
                                 null=True,
                                 blank=True)
    interest_scheme = models.ForeignKey(InterestScheme, verbose_name="Процентная схема", blank=True, null=True,
                                        on_delete=models.SET_NULL)

    rate = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Ставка процента", null=False,
                               blank=False)
    amount_interest = models.DecimalField(max_digits=16, decimal_places=8, verbose_name="Сумма процентов (точная)",
                                          null=False,
                                          blank=False)
    credit = models.ForeignKey("credits.Credit", on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name="Идентификатор Credit")

    debt_type = models.ForeignKey(DeptType, verbose_name="Вид задолженности", blank=True, null=True,
                                  on_delete=models.CASCADE)

    is_fixed = models.BooleanField(
        null=True, default=False)
    description = models.TextField(verbose_name="Выражение для расчета суммы тарифа", blank=True, null=True)

    class Meta:
        verbose_name = "Журнал начисленных процентов"
        verbose_name_plural = "Журнал начисленных процентов"


class Insurance(models.Model):
    """Договора страхования"""
    client = models.ForeignKey("clients.Client", verbose_name="Клиент", on_delete=models.CASCADE,
                               blank=False,
                               null=False)
    num_dog = models.CharField(max_length=20, verbose_name="Номер договора", blank=False, null=False)

    date_begin = models.DateField(verbose_name="дата начала", null=False, blank=False)
    date_end = models.DateField(verbose_name="дата окончания", null=False, blank=False)
    amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Сумма")
    premia = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Страховая премия", null=True)
    ins_company = models.CharField(max_length=20, verbose_name="Страховая компания", blank=False, null=False)
    currency = models.ForeignKey(Currencies, verbose_name="Валюта", on_delete=models.CASCADE, blank=False,
                                 null=False)
    notes = models.TextField(verbose_name="Примечания", blank=True, null=True)
    status = models.ForeignKey(Status, verbose_name="Статус", on_delete=models.CASCADE, blank=False,
                               null=False)
    departament = models.ForeignKey(Departament, verbose_name="Подразделение", on_delete=models.CASCADE, blank=False,
                                    null=False)
    emp = models.ForeignKey(User, verbose_name="ответственный сотрудник",
                            on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Договор страхования"
        verbose_name_plural = "Договора страхования"


class InsuranceLink(models.Model):
    """Связь с договорами страхования"""

    insurance = models.ForeignKey(Departament, verbose_name="Договор страхования", on_delete=models.CASCADE,
                                  blank=False,
                                  null=False)
    credit = models.ForeignKey("credits.Credit", on_delete=models.CASCADE, null=False, blank=False,
                               verbose_name="Кредит")

    class Meta:
        verbose_name = "Связь с договорами страхования"
        verbose_name_plural = "Связь с договорами страхования"
