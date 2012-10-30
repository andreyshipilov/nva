from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin
from .models import Project


class ProjectAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('project_title', 'client_title',)
admin.site.register(Project, ProjectAdmin)