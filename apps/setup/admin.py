from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import Setup


class SetupAdmin(AdminImageMixin, admin.ModelAdmin):
    pass
admin.site.register(Setup, SetupAdmin)
