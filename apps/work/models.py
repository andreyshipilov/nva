# -*- coding: utf-8 -*-
from os.path import splitext
from os import urandom

from django.db import models

from sorl.thumbnail import ImageField


class ProductType(models.Model):
    title = models.CharField(unique=True, max_length=100,
                             verbose_name=u"название типа ПО",)

    class Meta:
        ordering = ("title",)
        verbose_name = u"тип"
        verbose_name_plural = u"типы ПО"

    def __unicode__(self):
        return self.title


class Product(models.Model):
    is_published = models.BooleanField(default=False,
                                       verbose_name=u"показывать ли на сайте",)
    product_type = models.ForeignKey(ProductType,
                                     verbose_name=u"тип продукта")
    title = models.CharField(max_length=200,
                             verbose_name=u"название продукта",)
    text = models.TextField(verbose_name=u"описание продукта",)
    image = ImageField(blank=True,
                       upload_to=lambda i, f: "products/%s%s" % \
                           (urandom(16).encode("hex"), splitext(f)[1].lower()),
                       verbose_name=u"изображение",
                       help_text=u"Например, фотография упаковки или обложка.",)
    demo_file = models.FileField(blank=True,
                                 upload_to="product_demos",
                                 verbose_name=u"файл, демо-версия продукта",)

    class Meta:
        ordering = ("title",)
        verbose_name = u"продукт"
        verbose_name_plural = u"продукты"

    def __unicode__(self):
        return self.title

    @staticmethod
    def get_published():
        return Human.objects.filter(is_published=True)

    @models.permalink
    def get_absolute_url(self):
        return ('products_item', (), {'pk': self.pk})
