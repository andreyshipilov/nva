from django.contrib import admin
from django.db import models
from sorl.thumbnail.admin import AdminImageMixin
from mezzanine.core.forms import TinyMceWidget

from .models import Project, Client, Field


class FieldAdmin(admin.ModelAdmin):
    list_display = ("title",)
admin.site.register(Field, FieldAdmin)

class ClientAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("title",)
admin.site.register(Client, ClientAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "is_published")
    formfield_overrides = {
        models.TextField: {"widget": TinyMceWidget},
    }
admin.site.register(Project, ProjectAdmin)
