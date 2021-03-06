# -*- coding: utf-8 -*-
from django.db import models

from projects.models import Project


class Review(models.Model):
    is_published = models.BooleanField(default=False,
                                       verbose_name=u"показывать ли на сайте",)
    date = models.DateField(verbose_name=u"дата отзыва",
                            help_text=u"Используется для сортировки.")
    short_text = models.CharField(max_length=200,
                                  verbose_name=u"краткое описание",)
    text = models.TextField(verbose_name=u"текст отзыва",)
    project = models.ForeignKey(Project,
                                verbose_name=u"проект, с которым связан отзыв",)

    class Meta:
        ordering = ("-date",)
        verbose_name = u"отзыв"
        verbose_name_plural = u"отзывы"

    def __unicode__(self):
        return self.short_text

    @staticmethod
    def get_published():
        return Review.objects.filter(is_published=True)
