from django.contrib import admin
from django.db import models

from mezzanine.core.forms import TinyMceWidget
from sorl.thumbnail.admin import AdminImageMixin
from .models import ProductType, Product, ServiceType, Service


admin.site.register(ProductType)

class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("title", "product_type",)
    formfield_overrides = {
        models.TextField: {"widget": TinyMceWidget},
    }
admin.site.register(Product, ProductAdmin)


admin.site.register(ServiceType)

class ServiceAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("title", "service_type",)
    formfield_overrides = {
        models.TextField: {"widget": TinyMceWidget},
    }
admin.site.register(Service, ServiceAdmin)
