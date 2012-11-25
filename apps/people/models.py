# -*- coding: utf-8 -*-
from os.path import splitext
from os import urandom

from django.db import models

from sorl.thumbnail import ImageField


class Human(models.Model):
    full_name = models.CharField(max_length=100,
                                 verbose_name=u"полное имя",)
    quote = models.CharField(max_length=200,
                             verbose_name=u"цитата",)
    position = models.CharField(max_length=100,
                                verbose_name=u"должность",)
    email = models.EmailField(blank=True,
                              verbose_name=u"электронная почта",)
    image = ImageField(upload_to=lambda i, f: "human_banners/%s%s" % \
                           (urandom(16).encode("hex"), splitext(f)[1].lower()),
                       blank=True,
                       verbose_name=u"изображение",
                       help_text=u"PNG файл с прозрачным фоном.",)

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
    full_name = models.CharField(max_length=100,
                                 verbose_name=u"полное имя",)
    email = models.EmailField(verbose_name=u"электронная почта",)
    phone = models.CharField(max_length=30, blank=True,
                             verbose_name=u"телефон",)

    class Meta:
        ordering = ("full_name",)
        verbose_name = u"объект"
        verbose_name_plural = u"менеджеры"

    def __unicode__(self):
        return self.full_name