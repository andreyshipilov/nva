# -*- coding: utf-8 -*-
from os.path import splitext
from os import urandom

from django.db import models

from sorl.thumbnail import ImageField


class Human(models.Model):
    full_name = models.CharField(verbose_name=u"полное имя", max_length=100,)
    quote = models.CharField(verbose_name=u"цитата", max_length=200,)
    position = models.CharField(verbose_name=u"должность", max_length=100,)
    email = models.EmailField(verbose_name=u"электронная почта", blank=True,)
    image = ImageField(verbose_name=u"изображение",
                       help_text=u"PNG файл с прозрачным фоном.",
                       upload_to=lambda i, f: "human_banners/%s%s" % \
                           (urandom(16).encode("hex"), splitext(f)[1].lower()),
                       blank=True,)
    
    class Meta:
        ordering = ("full_name",)
        verbose_name = u"объект"
        verbose_name_plural = u"баннеры"
    
    def __unicode__(self):
        return self.full_name
    
    @staticmethod
    def get_random():
        humans = Human.objects.order_by("?")
        
        if humans.exists():
            return humans[0]
        else:
            return Human.objects.none()

class Manager(models.Model):
    full_name = models.CharField(verbose_name=u"полное имя", max_length=100,)
    email = models.EmailField(verbose_name=u"электронная почта",)
    
    class Meta:
        ordering = ("full_name",)
        verbose_name = u"объект"
        verbose_name_plural = u"менеджеры"
    
    def __unicode__(self):
        return self.full_name