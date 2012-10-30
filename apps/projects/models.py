# -*- coding: utf-8 -*-
from os.path import splitext

from django.db import models

from sorl.thumbnail import ImageField


class Project(models.Model):
    project_title = models.CharField(verbose_name=u'название проекта',
                                     max_length=100,)
    project_description = models.CharField(verbose_name=u'краткое описание',
                                           max_length=100,)
    client_title = models.CharField(verbose_name=u'название клиента',
                                    max_length=200,)
    image = ImageField(verbose_name=u'изображение',
                       help_text=u'PNG файл с прозрачным фоном.',
                       upload_to=lambda i, f: 'project/image%s' % splitext(f)[1],
                       blank=True,)
    
    class Meta:
        ordering = ('project_title',)
        verbose_name = u'проект'
        verbose_name_plural = u'проекты'
    
    def __unicode__(self):
        return self.project_title
