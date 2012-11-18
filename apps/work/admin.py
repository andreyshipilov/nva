from django.contrib import admin
from django.db import models

from mezzanine.core.forms import TinyMceWidget
from sorl.thumbnail.admin import AdminImageMixin
from .models import ProductType, Product, Service


admin.site.register(ProductType)

class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("title", "product_type", "is_published",)
    formfield_overrides = {
        models.TextField: {"widget": TinyMceWidget},
    }
admin.site.register(Product, ProductAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published",)
admin.site.register(Service, ServiceAdmin)