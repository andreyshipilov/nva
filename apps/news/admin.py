from django.contrib import admin
from django.db import models

from mezzanine.core.forms import TinyMceWidget

from .models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    list_filter = ('publish_date', 'expiry_date')
    list_display = ('title', 'publish_date', 'status')
    exclude = ('slug', 'short_url', 'description', 'keywords',)
    formfield_overrides = {
        models.TextField: {
            'widget': TinyMceWidget
        }
    }
admin.site.register(NewsItem, NewsItemAdmin)