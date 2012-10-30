from django.contrib import admin
from django.db import models

from .models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    list_filter = ('publish_date', 'expiry_date', 'status',)
    list_display = ('title', 'publish_date', 'status')
    exclude = ('slug', 'short_url', 'description', 'keywords',)
admin.site.register(NewsItem, NewsItemAdmin)