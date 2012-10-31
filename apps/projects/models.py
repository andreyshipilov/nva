# -*- coding: utf-8 -*-
from os.path import splitext
from os import urandom

from django.db import models

from sorl.thumbnail import ImageField
    

class Client(models.Model):
    title = models.CharField(verbose_name=u"название клиента", max_length=200,
                             unique=True,)
    image = ImageField(verbose_name=u"изображение",
                       upload_to=lambda i, f: "projects/clients/%s%s" % \
                           (urandom(16).encode("hex"), splitext(f)[1].lower()),
                       blank=True,)
    
    class Meta:
        ordering = ("title",)
        verbose_name = u"клиент"
        verbose_name_plural = u"клиенты"
    
    def __unicode__(self):
        return self.title

class Field(models.Model):
    title = models.CharField(verbose_name=u"название отрасли", max_length=200,
                             unique=True,)
    
    class Meta:
        ordering = ("title",)
        verbose_name = u"отрасль"
        verbose_name_plural = u"отрасли"
    
    def __unicode__(self):
        return self.title

class Project(models.Model):
    is_published = models.BooleanField(verbose_name=u"показывать ли на сайте",
                                       default=False,)
    date = models.DateField(verbose_name=u"дата",
                            help_text=u"Используется для сортировки.")
    title = models.CharField(verbose_name=u"название проекта",
                             max_length=100,)
    description = models.CharField(verbose_name=u"краткое описание",
                                   max_length=100,)
    client = models.ForeignKey(Client, blank=True, null=True,
                               verbose_name=u"клиент, для которого выполнен проект",)
    field = models.ManyToManyField(Field, related_name="fields", blank=True,
                                   verbose_name=u"отрасль проекта",)
    
    class Meta:
        ordering = ("-date",)
        verbose_name = u"проект"
        verbose_name_plural = u"проекты"
    
    def __unicode__(self):
        return self.title
    
    @staticmethod
    def get_published():
        return Project.objects.filter(is_published=True)