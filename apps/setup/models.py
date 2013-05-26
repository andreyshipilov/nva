# -*- coding: utf-8 -*-
from os.path import splitext
from os import urandom

from django.db import models

from sorl.thumbnail import ImageField


class Setup(models.Model):
    site_short_title = models.CharField(max_length=100,
                                        verbose_name=u'короткое название сайта')
    site_full_title = models.CharField(max_length=100,
                                       verbose_name=u'полное название сайта')
    copyright = models.CharField(max_length=200, blank=True,
                                 verbose_name=u'текст после копирайта')
    phone = models.CharField(max_length=20, verbose_name=u'телефон')
    main_logo = ImageField(blank=True, upload_to=lambda i, f: "logos/%s%s" %
                      (urandom(16).encode("hex"), splitext(f)[1].lower()),
                      verbose_name=u"большой логотип в шапке",)
    small_logo = ImageField(blank=True, upload_to=lambda i, f: "logos/%s%s" %
                      (urandom(16).encode("hex"), splitext(f)[1].lower()),
                      verbose_name=u"маленький логотип в колонтитуле",)

    class Meta:
        verbose_name = u'настройки сайта'
        verbose_name_plural = u'настройки сайта'

    def __unicode__(self):
        return self._meta.verbose_name.capitalize()

    @staticmethod
    def get_available():
        if Setup.objects.exists():
            return Setup.objects.all()[0]
        return Setup.objects.none()
