# -*- coding: utf-8 -*-
from django.db import models

from mezzanine.core.fields import RichTextField
from mezzanine.core.models import Displayable
from mezzanine.core.managers import PublishedManager
from projects.models import Project
from work.models import Product


class NewsItem(Displayable):
    full_text = RichTextField(verbose_name=u'текст новости')
    product = models.ForeignKey(Product, blank=True, null=True,
                                verbose_name=u'продукт, с которым связана новость',)
    project = models.ForeignKey(Project, blank=True, null=True,
                                verbose_name=u'проект, с которым связана новость',)

    objects = PublishedManager()

    class Meta:
        ordering = ('-publish_date',)
        verbose_name = u'новость'
        verbose_name_plural = u'новости'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('news_item', (), {'pk': self.pk})
