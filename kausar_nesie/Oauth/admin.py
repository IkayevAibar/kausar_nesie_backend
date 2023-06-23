from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _

from .models import User

# Register your models here.
class OUserAdmin(UserAdmin):
    change_password_form = AdminPasswordChangeForm
    change_user_password_template = None

    list_display = ("username", "email", "is_staff")
    fieldsets = (
        (None, {'fields': ('email','username', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', )}),
    )

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser and not request.user.is_staff:
            return False
        return super().has_change_permission(request, obj)


admin.site.register(User, OUserAdmin)