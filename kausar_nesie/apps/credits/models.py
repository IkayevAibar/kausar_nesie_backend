from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Credit(models.Model):
    """Кредиты"""
    credit_type = models.ForeignKey("catalog.CreditType", verbose_name="Идентификатор типов кредитов",
                                    on_delete=models.CASCADE, blank=False,
                                    null=False)
    emp = models.ForeignKey(User, verbose_name="Сотрудник ответственный за кредит",
                            on_delete=models.SET_NULL, blank=True, null=True)

    request = models.IntegerField(verbose_name="Идентификатор заявки",
                                  blank=True, null=True)
    client = models.ForeignKey("clients.Client", verbose_name="Идентификатор заемщика", on_delete=models.CASCADE,
                               blank=False,
                               null=False)
    amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Сумма кредита", null=False,
                                 blank=False)

    status = models.ForeignKey("catalog.Status", default=1, verbose_name="Идентификатор статусов", on_delete=models.CASCADE,
                               blank=False,
                               null=False)#TODO: Убрать default правила платежа
    rule = models.ForeignKey("catalog.PaymentRule", default=1, verbose_name="Идентификатор правила платежа",
                             on_delete=models.CASCADE, blank=False,
                             null=False) #TODO: Убрать default правила платежа
    curr = models.ForeignKey('catalog.Currencies', verbose_name="Идентификатор валюты кредита",
                             on_delete=models.CASCADE,
                             blank=True, null=True)
    ex_rate = models.DecimalField(max_digits=16, decimal_places=4, verbose_name="Значение курса при выдаче", null=True,
                                  blank=True)
    date_begin = models.DateField(verbose_name="Дата начала", null=False, blank=False)
    date_end = models.DateField(verbose_name="Дата окончания", null=False, blank=False)
    date_close = models.DateField(verbose_name="Дата закрытия", null=True, blank=True)
    date_sign = models.DateField(verbose_name="Дата подписания договора", null=True, blank=True)
    depart = models.ForeignKey("catalog.Departament", verbose_name="Реквизиты для выдачи. Отдел",
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    notes = models.TextField(verbose_name="Комментарий", null=True, blank=True)
    project_type = models.ForeignKey("catalog.ProjectType", verbose_name="Тип проекта",
                                     on_delete=models.CASCADE,
                                     blank=True, null=True)
    credit_source = models.ForeignKey("catalog.CreditSource", verbose_name="Источник кредитования",
                                      on_delete=models.CASCADE,
                                      blank=True, null=True)
    credit_target = models.ForeignKey("catalog.CreditTarget", verbose_name="Цель кредитования",
                                      on_delete=models.CASCADE,
                                      blank=True, null=True)
    num_dog = models.CharField(max_length=20, verbose_name="Номер договора", blank=True, null=True)

    is_line = models.BooleanField(verbose_name="Признак линии",
                                  null=True, default=True)
    period_type = models.ForeignKey("catalog.PeriodType", on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name="Тип периода - Срок")
    period_count = models.IntegerField(verbose_name="Срок", null=True, blank=True)
    reason = models.TextField(verbose_name="Основание выдачи кредита", null=True, blank=True)
    effective_rate = models.DecimalField(max_digits=16, default=0, decimal_places=2, verbose_name="Эффективная ставка", null=False,
                                         blank=False)
    is_affiliated = models.BooleanField(verbose_name="Аффилированное лицо",
                                        null=True, default=True)
    is_rate_fixed = models.BooleanField(verbose_name="Фиксировать курсовую разницу",
                                        null=True, default=True)
    insurance_amt = models.DecimalField( max_digits=16, decimal_places=2, verbose_name="Страховая премия", null=False,
                                        blank=False)
    agency_cost = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Агентская премия", null=False,
                                      blank=False)

    coborrowers = models.ManyToManyField("clients.IndividualClient", verbose_name="Созаемщики", related_name="coborrowers", blank=True)
    
    class Meta:
        verbose_name = "Кредит"
        verbose_name_plural = "Кредиты"

class CreditTreatments(models.Model):
    credit = models.ForeignKey(Credit, verbose_name="Кредит", on_delete=models.CASCADE, related_name='treatments')
    document = models.FileField(upload_to='credit/docs/', verbose_name="Сканированная копия документа Договора Кредита", null=False, blank=False)

    class Meta:
        verbose_name = "Файл Договора Кредита"
        verbose_name_plural = "Файлы Договора Кредита"