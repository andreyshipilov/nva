from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import License, Patent


class LicenseAdmin(AdminImageMixin, admin.ModelAdmin):
    pass
admin.site.register(License, LicenseAdmin)

class PatentAdmin(AdminImageMixin, admin.ModelAdmin):
    pass
admin.site.register(Patent, PatentAdmin)