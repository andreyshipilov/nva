from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render

from .models import NewsItem


class Index(ListView):
    queryset = NewsItem.objects.published()

class Item(DetailView):
    model = NewsItem
    slug_field = "pk"
