from django.views.generic import ListView

from .models import Review


class Index(ListView):
    queryset = Review.get_published()
