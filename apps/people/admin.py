from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin
from .models import Human, Manager


class HumanAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("full_name", "quote", "email")
admin.site.register(Human, HumanAdmin)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email")
admin.site.register(Manager, ManagerAdmin)