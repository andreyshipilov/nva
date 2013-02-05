from django.db.models import Count
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render

from .models import ProductType, Product, ServiceType, Service
from .forms import ContactForm


class ProductsIndex(ListView):
    queryset = ProductType.objects.annotate(count=Count("product")).filter(count__gt=0)

class Product(DetailView):
    model = Product
    slug_field = "pk"

    def get_context_data(self, **kwargs):
        context = super(Product, self).get_context_data(**kwargs)
        context['form'] = ContactForm()

        return context


class ServicesIndex(ListView):
    queryset = ServiceType.objects.annotate(count=Count("service")).filter(count__gt=0)

class Service(DetailView):
    model = Service
    slug_field = "pk"
