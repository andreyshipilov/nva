from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render

#from mezzanine.utils.views import render

from .models import NewsItem


class Index(ListView):
    model = NewsItem
    
class Item(DetailView):
    model = NewsItem
    slug_field = 'pk'