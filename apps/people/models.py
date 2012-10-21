# -*- coding: utf-8 -*-

from os.path import splitext

from django.db import models

from sorl.thumbnail import ImageField


class Human(models.Model):
    full_name = models.CharField(verbose_name=u'полное имя', max_length=100,)
    quote = models.CharField(verbose_name=u'цитата', max_length=200,)
    position = models.CharField(verbose_name=u'должность', max_length=100,)
    email = models.EmailField(verbose_name=u'электронная почта')
    image = ImageField(verbose_name=u'изображение',
                       help_text=u'PNG файл с прозрачным фоном.',
                       upload_to=lambda i, f: 'people/human%s' % splitext(f)[1],
                       blank=True,)
    
    class Meta:
        ordering = ('full_name',)
        verbose_name = u'объект'
        verbose_name_plural = u'объекты'
    
    def __unicode__(self):
        return self.full_name
    
    @staticmethod
    def get_random():
        return Human.objects.order_by('?')[0]
