from django.contrib import admin
from .models import *
# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')
    list_filter = ('area',)
    search_fields = ('name', 'area')

class NameCodeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

class AreasAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name',  'city')
    list_filter = ('city',)

class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'district')
    search_fields = ('name',  'district')
    list_filter = ('district',)

class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'provision_prc', 'provision_to', 'provision_from', 'delay_days_to', 'delay_days_from')
    search_fields = ('name',  'code', 'provision_prc', 'provision_to', 'provision_from', 'delay_days_to', 'delay_days_from')

class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'num_pattern')
    search_fields = ('name', 'code', 'num_pattern')

class CurrenciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'alpha_code', 'num_code', 'curr_type')
    search_fields = ('name', 'alpha_code', 'num_code', 'curr_type')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'alfa_3')
    search_fields = ('name', 'code', 'alfa_3')

class CountersAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'value', 'max_value', 'auto_reset', 'period_type')
    search_fields = ('name', 'code', 'value', 'max_value', 'auto_reset', 'period_type')

class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'has_child')
    search_fields = ('name', 'code', 'has_child')

class DeptTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category')
    search_fields = ('name', 'code', 'category')

class BankTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'bic')
    search_fields = ('name', 'bic')

class CalculateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'calc_type')
    search_fields = ('name', 'code', 'calc_type')

class AccountPatternAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'patt_num', 'patt_name', 'subject_type')
    search_fields = ('name', 'code', 'patt_num', 'patt_name', 'subject_type')

class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'acc_type', 'acc_pattern', 'open_type', 'def_currency', 'currency')
    search_fields = ('name', 'code', 'acc_type', 'acc_pattern', 'open_type', 'def_currency', 'currency')

class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'company', 'liferay_id')
    search_fields = ('name', 'code', 'company', 'liferay_id')

class CreditTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'min_period', 'max_period', 'min_amount', 'max_amount', 'need_collateral', 'need_guarantor', 'need_coclient', 'penalty_period', 'rule', 'currency', 'line_type', 'plan_type', 'num_pattern', 'project_type', 'credit_source', 'early_prc_mode')
    search_fields = ('name', 'code', 'min_period', 'max_period', 'min_amount', 'max_amount', 'need_collateral', 'need_guarantor', 'need_coclient', 'penalty_period', 'rule', 'currency', 'line_type', 'plan_type', 'num_pattern', 'project_type', 'credit_source', 'early_prc_mode')

class InterestSchemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'individual', 'calculate', 'period_type')
    search_fields = ('name', 'individual', 'calculate', 'period_type')

class InterestRateAdmin(admin.ModelAdmin):
    list_display = ('interest_scheme', 'rate', 'is_rate', 'forumula', 'date_begin', 'date_end')
    search_fields = ('interest_scheme', 'rate', 'is_rate', 'forumula', 'date_begin', 'date_end')

class InterestJournalAdmin(admin.ModelAdmin):
    list_display = ('days', 'amount_for_calc', 'amount', 'interest_scheme', 'rate', 'amount_interest', 'credit', 'debt_type', 'is_fixed', 'description', 'date_begin', 'date_end')
    search_fields = ('days', 'amount_for_calc', 'amount', 'interest_scheme', 'rate', 'amount_interest', 'credit', 'debt_type', 'is_fixed', 'description', 'date_begin', 'date_end')

class InsuranceAdmin(admin.ModelAdmin):
    list_display = ('num_dog', 'client', 'amount', 'premia', 'ins_company', 'currency', 'status', 'notes', 'departament', 'emp', 'date_begin', 'date_end')

class InsuranceLinkAdmin(admin.ModelAdmin):
    list_display = ('insurance', 'credit')

admin.site.register(Cities, CityAdmin)
admin.site.register(AddressType, NameCodeTypeAdmin)
admin.site.register(Areas, AreasAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Street, StreetAdmin)
admin.site.register(ClientCategory, NameCodeTypeAdmin)
admin.site.register(CategoryType, CategoryTypeAdmin)
admin.site.register(WorkType, NameCodeTypeAdmin)
admin.site.register(TransactionType, TransactionTypeAdmin)
admin.site.register(Status, NameCodeTypeAdmin)
admin.site.register(PaymentStatus, NameCodeTypeAdmin)
admin.site.register(SectorEcon, NameCodeTypeAdmin)
admin.site.register(ProjectType, NameCodeTypeAdmin)
admin.site.register(PositionType, NameCodeTypeAdmin)
admin.site.register(PeriodType, NameCodeTypeAdmin)
admin.site.register(PaymentType, NameCodeTypeAdmin)
admin.site.register(OrgForm, NameCodeTypeAdmin)
admin.site.register(LinkType, NameCodeTypeAdmin)
admin.site.register(LineType, NameCodeTypeAdmin)
admin.site.register(IdcardType, NameCodeTypeAdmin)
admin.site.register(FormProperty, NameCodeTypeAdmin)
admin.site.register(Currencies, CurrenciesAdmin)
admin.site.register(CreditTarget, NameCodeTypeAdmin)
admin.site.register(CreditSource, NameCodeTypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Counters, CountersAdmin)
admin.site.register(ContactType, ContactTypeAdmin)
admin.site.register(CollateralType, NameCodeTypeAdmin)
admin.site.register(DeptType, DeptTypeAdmin)
admin.site.register(Bank, BankTypeAdmin)
admin.site.register(Calculate, CalculateAdmin)
admin.site.register(BaseAccount, NameCodeTypeAdmin)
admin.site.register(AccountPattern, AccountPatternAdmin)
admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Departament, DepartamentAdmin)
admin.site.register(PaymentRule, NameCodeTypeAdmin)
admin.site.register(CreditType, CreditTypeAdmin)
admin.site.register(InterestScheme, InterestSchemeAdmin)
admin.site.register(InterestRate, InterestRateAdmin)
admin.site.register(InterestJournal, InterestJournalAdmin)
admin.site.register(Insurance, InsuranceAdmin)
admin.site.register(InsuranceLink, InsuranceLinkAdmin)
