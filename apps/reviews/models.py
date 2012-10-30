# -*- coding: utf-8 -*-
from django.db import models

from projects.models import Project


class Review(models.Model):
    is_published = models.BooleanField(verbose_name=u'показывать ли на сайте',
                                       default=False,)
    date = models.DateField(verbose_name=u'дата отзыва',
                            help_text=u'Используется для сортировки.')
    short_text = models.CharField(verbose_name=u'краткое описание',
                                  max_length=200,)
    text = models.TextField(verbose_name=u'текст отзыва',)
    project = models.ForeignKey(Project,
                                help_text=u'Проект, с которым связан отзыв.',)
    
    class Meta:
        ordering = ('-date',)
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'
    
    def __unicode__(self):
        return self.short_text
    
    @staticmethod
    def get_published():
        return Review.objects.filter(is_published=True)
