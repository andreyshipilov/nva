# -*- coding: utf-8 -*-
from os.path import splitext
from os import urandom

from django.db import models

from sorl.thumbnail import ImageField


class License(models.Model):
    title = models.CharField(max_length=400,
                             verbose_name=u"название лицензии",)
    image = ImageField(upload_to=lambda i, f: "licenses/%s%s" % \
                           (urandom(16).encode("hex"), splitext(f)[1].lower()),
                       verbose_name=u"изображение",)

    class Meta:
        verbose_name = u"объект"
        verbose_name_plural = u"лицензии"

    def __unicode__(self):
        return self.title


class Patent(models.Model):
    title = models.CharField(max_length=400,
                             verbose_name=u"название патента",)
    image = ImageField(upload_to=lambda i, f: "patents/%s%s" % \
                           (urandom(16).encode("hex"), splitext(f)[1].lower()),
                       verbose_name=u"изображение",)

    class Meta:
        verbose_name = u"объект"
        verbose_name_plural = u"патенты"

    def __unicode__(self):
        return self.title