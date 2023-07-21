from django.contrib import admin
from .models import Credit ,CreditTreatments, Requisite

class CreditAdmin(admin.ModelAdmin):
    list_display = ('num_dog', 'request', 'credit_type', 'client', 'emp', 'amount', 'status', 'rule', 'curr', 'ex_rate', 'date_begin', 'date_end', 'date_close', 'date_sign', 'depart', 'notes', 'project_type', 'credit_source', 'credit_target', 'is_line', 'period_type', 'period_count', 'reason', 'effective_rate', 'is_affiliated', 'is_rate_fixed', 'insurance_amt', 'agency_cost')
    list_filter = ('is_line', 'is_affiliated', 'status', 'credit_type', 'project_type', 'credit_source', 'credit_target', 'curr')
    search_fields = ('request', 'num_dog')

class RequisiteAdmin(admin.ModelAdmin):
    list_display = ('client', 'req_acc', 'req_bank', 'req_name', 'req_kbe')
    list_filter = ('req_bank', 'to_cash')
    search_fields = ('req_name', 'req_kbe', 'req_acc')

admin.site.register(Credit, CreditAdmin)
admin.site.register(CreditTreatments)
admin.site.register(Requisite, RequisiteAdmin)

# Register your models here.
