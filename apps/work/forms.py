# -*- coding: utf-8 -*-
from django import forms



class ContactForm(forms.Form):
    message = forms.CharField(label=u"Вопрос", widget=forms.Textarea)
