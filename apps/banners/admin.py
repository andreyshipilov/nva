from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin

from .models import Banner


class BannerAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("__unicode__", "is_published")
admin.site.register(Banner, BannerAdmin)
