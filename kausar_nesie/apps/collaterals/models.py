from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Collateral(models.Model):
    """Договора обеспечения"""

    
    num_dog = models.CharField(max_length=20, verbose_name="Номер договора", blank=True, null=True)
    is_evaluated = models.BooleanField(verbose_name="Оценка", default= False, blank=True, null=True)
    is_insured = models.BooleanField(verbose_name="Страховка", default= False, blank=True, null=True)
    date_begin = models.DateField(verbose_name="Дата открытия счета", null=False, blank=False)
    date_end = models.DateField(verbose_name="Дата окончания действия", null=False, blank=False)
    date_sign = models.DateField(verbose_name="Дата подписания", null=True, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Сумма обеспечения")
    currency = models.ForeignKey('catalog.Currencies', verbose_name="Валюта", on_delete=models.CASCADE,
                                 blank=True, null=False)
    type = models.ForeignKey('catalog.CollateralType', verbose_name="Идентификатор типа залога",
                             on_delete=models.CASCADE,
                             blank=True, null=False)
    client = models.ForeignKey('clients.Client', verbose_name="Идентификатор залогодателя", on_delete=models.CASCADE,
                               blank=True, null=False)
    
    coborrowers = models.ManyToManyField("clients.IndividualClient", verbose_name="Созаемщики", related_name="collateral_coborrowers", blank=True)
    documents = models.ManyToManyField("CollateralDocuments", verbose_name="Документы", related_name="documents", blank=True)

    description = models.TextField(verbose_name="Описание залоговой ценности", null=True, blank=True)
    location = models.TextField(verbose_name="Расположение ценностии", null=True, blank=True)
    
    status = models.ForeignKey('catalog.Status', verbose_name="Статус",
                               on_delete=models.SET_NULL,
                               blank=True, null=True)
    departament = models.ForeignKey('catalog.Departament', verbose_name="Отдел",
                                    on_delete=models.SET_NULL,
                                    blank=True, null=True)
    emp = models.ForeignKey(User, verbose_name="Ответственный сотрудник",
                            on_delete=models.SET_NULL, blank=True, null=True)
    date_close = models.DateField(verbose_name="Дата подписания", null=True, blank=True)
    
    # name = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Наименование залоговой ценности")
    # market_value = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Рыночная стоимость")
    # market_date = models.DateField(verbose_name="Дата оценки рыночной стоимости", null=True, blank=True)
    # market_currency = models.PositiveIntegerField(null=True, blank=True, verbose_name="market_currency")
    # account = models.ForeignKey('clients.Account', verbose_name="Счет учета залога",
    #                             on_delete=models.SET_NULL,
    #                             blank=True, null=True)
    # legal_docs = models.TextField(verbose_name="Правоустанавливающие документы", null=True, blank=True)
    
    

    # encumbrance = models.BooleanField(verbose_name="Признак обременения", blank=True, null=True)
    # comments = models.TextField(verbose_name="Комментарии к обременению", null=True, blank=True)

    class Meta:
        verbose_name = "Договор обеспечения"
        verbose_name_plural = "Договора обеспечения"

class CollateralDocuments(models.Model):
    collateral = models.ForeignKey(Collateral, verbose_name="Договор залога", on_delete=models.SET_NULL,
                                   blank=True, null=True)
    document = models.FileField(upload_to='collateral/docs/', verbose_name="Сканированная копия документа Обеспечения", null=False, blank=False)



class CollateralInsurance(models.Model):
    """Страхование залога"""

    collateral = models.ForeignKey(Collateral, verbose_name="Договор залога", on_delete=models.SET_NULL,
                                   blank=True, null=True)
    date_begin = models.DateField(verbose_name="Дата начала", null=False, blank=False)
    date_end = models.DateField(verbose_name="Дата окончения", null=False, blank=False)

    ins_num = models.CharField(max_length=20, verbose_name="Номер страховки", blank=False, null=False)
    ins_company = models.CharField(max_length=200, verbose_name="Страховая компания", blank=False, null=False)
    ins_amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Сумма страховки", blank=False,
                                     null=False)
    ins_premia = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Страховая премия", blank=True,
                                     null=True)
    currency = models.ForeignKey('catalog.Currencies', verbose_name="Валюта", on_delete=models.CASCADE,
                                 blank=True, null=True)
    notes = models.TextField(verbose_name="Комментарий", null=True, blank=True)

    class Meta:
        verbose_name = "Страхование залога"
        verbose_name_plural = "Страхование залога"


class CollateralCoclient(models.Model):
    """Со-залогодатели"""

    collateral = models.ForeignKey(Collateral, verbose_name="collaterals", on_delete=models.SET_NULL,
                                   blank=True, null=True)

    client = models.ForeignKey('clients.Client', verbose_name="clients", on_delete=models.CASCADE,
                               blank=True, null=True)

    class Meta:
        verbose_name = "Со-залогодатель"
        verbose_name_plural = "Со-залогодатели"


class CollateralAssesment(models.Model):
    """Оценка залога"""

    collateral = models.ForeignKey(Collateral, verbose_name="Договор залога", on_delete=models.SET_NULL,
                                   blank=True, null=True)
    report_date = models.DateField(verbose_name="Дата отчета", null=False, blank=False)
    amount = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Сумма оценки в валюте", null=False,
                                 blank=False)
    currency = models.ForeignKey('catalog.Currencies', verbose_name="Валюта", on_delete=models.CASCADE,
                                 blank=True, null=True)
    agent = models.CharField(max_length=200, verbose_name="Оценщик", blank=False, null=False)
    license_num = models.CharField(max_length=50, verbose_name="Номер гоц. лицензии", blank=False, null=False)
    license_date = models.DateField(verbose_name="Дата лицензии", null=False, blank=False)
    report_num = models.CharField(max_length=50, verbose_name="Номер отчета", blank=False, null=False)
    amount_nat = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Сумма оценки в нац. покрытии",
                                     null=True, blank=True, default=None)
    rate_currency = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="Курс валюты при оценке",
                                        null=True, blank=True)
    rate_date = models.DateField(verbose_name="Дата курса (для валюты оценки)", null=True, blank=True)

    class Meta:
        verbose_name = "Оценка залога"
        verbose_name_plural = "Оценка залога"
