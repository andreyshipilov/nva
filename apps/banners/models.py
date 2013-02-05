# -*- coding: utf-8 -*-
from os.path import splitext
from os import urandom

from django.db import models
from sorl.thumbnail import ImageField

from work.models import Product


class Banner(models.Model):
    is_published = models.BooleanField(default=False,
                                       verbose_name=u"показывать ли на сайте",)
    big_title = models.CharField(max_length=100,
                                 verbose_name=u"большой заголовок",)
    medium_title = models.CharField(max_length=100,
                                    verbose_name=u"средний заголовок",)
    small_text = models.CharField(max_length=100,
                                  verbose_name=u"текст-описание",)
    bg_image = ImageField(upload_to=lambda i, f: "banners/%s%s" % \
                          (urandom(16).encode("hex"), splitext(f)[1].lower()),
                          verbose_name=u"фоновое изображение",)
    illustration = ImageField(blank=True, upload_to=lambda i, f: "banners/%s%s" % \
                           (urandom(16).encode("hex"), splitext(f)[1].lower()),
                              verbose_name=u"иллюстрация продукта",)
    file_attached = models.FileField(blank=True, upload_to="banners/demos",
                                 verbose_name=u"файл для скачивания",)

    product = models.ForeignKey(Product, blank=True, null=True,
                                verbose_name=u"Продукт, связанный с баннером",
                                help_text=u"Если указан продукт, то будет \
                                использована его иллюстрация и файл",)

    class Meta:
        verbose_name = u"баннер"
        verbose_name_plural = u"баннеры на главной"

    def __unicode__(self):
        return self.big_title

    @staticmethod
    def get_published():
        return Banner.objects.filter(is_published=True)

    @staticmethod
    def get_random():
        return Banner.get_published().order_by('?')

    def get_image(self):
        if self.product:
            return self.product.image
        return self.illustration

    def get_file(self):
        if self.product:
            return self.product.demo_file
        return self.file_attached
