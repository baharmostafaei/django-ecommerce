from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'last_login', 'is_active',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(models.Account, AccountAdmin)