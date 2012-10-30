from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin
from .models import Project, Client, Field


class FieldAdmin(admin.ModelAdmin):
    list_display = ("title",)
admin.site.register(Field, FieldAdmin)

class ClientAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ("title",)
admin.site.register(Client, ClientAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "is_published")
admin.site.register(Project, ProjectAdmin)
