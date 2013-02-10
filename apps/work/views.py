# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.template import loader, Context
from django.views.generic import ListView

from mezzanine.utils.views import render

from .models import ProductType, Product, ServiceType, Service
from .forms import ContactForm


"""
Products
"""
class ProductsIndex(ListView):
    queryset = ProductType.objects.annotate(count=Count("product")).filter(count__gt=0)

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form_is_ok = False

    context = {
        'product': product,
        'form_is_ok': form_is_ok,
    }

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            template = loader.get_template("email_feedback.html")
            email_context = Context({
                "form": contact_form,
                "obj": product,
            })
            send_mail("Получен новый вопрос", template.render(email_context),
                      "from@example.com", ["to@example.com"], fail_silently=True)
            form_is_ok = True
    else:
        contact_form = ContactForm()

    context.update({
        'contact_form': contact_form,
        'form_is_ok': form_is_ok,
    })

    return render(request, "work/product_detail.html", context)

"""
Services
"""
class ServicesIndex(ListView):
    queryset = ServiceType.objects.annotate(count=Count("service")).filter(count__gt=0)

def service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    form_is_ok = False

    context = {
        'service': service,
        'form_is_ok': form_is_ok,
    }

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            template = loader.get_template("email_feedback.html")
            email_context = Context({
                "form": contact_form,
                "obj": service,
            })
            send_mail("Получен новый вопрос", template.render(email_context),
                      "from@example.com", ["to@example.com"], fail_silently=True)
            form_is_ok = True
    else:
        contact_form = ContactForm()

    context.update({
        'contact_form': contact_form,
        'form_is_ok': form_is_ok,
    })

    return render(request, "work/service_detail.html", context)