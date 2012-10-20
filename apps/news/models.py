# -*- coding: utf-8 -*-

from django.db import models

from mezzanine.core.models import Displayable


class NewsItem(Displayable):
    full_text = models.TextField(verbose_name=u'текст новости')
    
    class Meta:
        ordering = ('-publish_date',)
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
    
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('news_item', (), {'pk': self.pk})
    
    @staticmethod
    def get_published():
        return NewsItem.objects.all()