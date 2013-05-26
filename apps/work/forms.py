# -*- coding: utf-8 -*-
from django import forms
import supercaptcha


class ContactForm(forms.Form):
    message = forms.CharField(label=u"Вопрос", widget=forms.Textarea)
    name =  forms.CharField(label=u"Как вас зовут",)
    contact =  forms.CharField(label=u"Как с вами связаться",)
    captcha = supercaptcha.CaptchaField(label=u"Введите цифры")
