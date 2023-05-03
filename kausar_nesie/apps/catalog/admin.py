from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Contact)
admin.site.register(AddressType)
admin.site.register(Areas)
admin.site.register(Cities)
admin.site.register(ClientCategory)