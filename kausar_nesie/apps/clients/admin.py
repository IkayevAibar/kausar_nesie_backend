from django.contrib import admin
from django import forms
from .models import *
# Register your models here.

class IndividualClientAdmin(admin.ModelAdmin):
    list_display = ('reg_number', 'full_name', 'gender', 'date_of_birth', 'place_of_birth', 'rnn', 'iin', 'sic', 'is_resident', 'country', 'client_category')
    list_filter = ('client_category', 'country', 'is_resident', 'place_of_birth', 'gender')
    search_fields = ('full_name', 'rnn', 'iin', 'sic')

class DocsAdmin(admin.ModelAdmin):
    list_display = ('client', 'identity_card_type', 'number', 'series', 'start_date', 'end_date', 'issued_by')
    list_filter = ('identity_card_type', )
    search_fields = ('number', 'series', 'series', 'client')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'full_name', 'sector', 'org_form', 'form_property', 'okpo', 'reg_num', 'reg_date', 'reg_org', 'certify_ser', 'certify_num')
    list_filter = ('sector', 'org_form', 'form_property')
    search_fields = ('short_name', 'full_name', 'reg_num', 'certify_num')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('client', 'post_index', 'cities', 'areas', 'district', 'street', 'house', 'flat', 'addr_type')
    list_filter = ('addr_type', 'areas')
    search_fields = ('house', 'flat')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('client', 'account_type_id', 'currency', 'amount', 'acc_num', 'base_account', 'date_open', 'date_close', 'name', 'departament', 'client_r', 'amount_nat')
    list_filter = ('account_type_id', 'currency', 'base_account', 'departament')
    search_fields = ('acc_num', 'flat')

class CompanyInline(admin.TabularInline):
    model = Company.owners.through
    extra = 0
    verbose_name = "Компания Клиента"
    verbose_name_plural = "Компании Клиента"

class ClientAdmin(admin.ModelAdmin):
    list_display = ('individual_client', 'insert_date', 'emp')
    search_fields = ('individual_client__name', 'individual_client__surname', 'individual_client__middle_name', 'individual_client__reg_num')
    inlines = [CompanyInline]
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('client', 'contact_type', 'value')
    list_filter = ('contact_type', )
    search_fields = ('value', )


admin.site.register(IndividualClient, IndividualClientAdmin)
admin.site.register(Docs, DocsAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contact, ContactAdmin)


