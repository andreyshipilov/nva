from django.contrib import admin
from django.db import models

from mezzanine.core.forms import TinyMceWidget
from .models import ProductType, Product


admin.site.register(ProductType)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "product_type", "is_published",)
admin.site.register(Product, ProductAdmin)