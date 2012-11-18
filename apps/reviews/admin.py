from django.contrib import admin
from django.db import models

from mezzanine.core.forms import TinyMceWidget
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("short_text", "project", "date",)
    formfield_overrides = {
        models.TextField: {"widget": TinyMceWidget},
    }
admin.site.register(Review, ReviewAdmin)