from django.contrib import admin
from .models import *

class CollateralAdmin(admin.ModelAdmin):
    list_display = ('num_dog', 'is_evaluated', 'is_insured', 'date_begin', 'date_end', 'date_sign', 'amount', 'currency', 'type', 'client', 'description', 'location', 'status', 'departament', 'emp', 'date_close')
    list_filter = ('status', 'type', 'departament', 'currency')
    search_fields = ('num_dog', )


admin.site.register(Collateral, CollateralAdmin)
admin.site.register(CollateralAssesment)
admin.site.register(CollateralInsurance)
admin.site.register(CollateralCoclient)
# Register your models here.
