from django.shortcuts import get_object_or_404, render

from news.models import NewsItem
from projects.models import Project


def index(request):
    context = {
        "news": NewsItem.objects.published()[:3],
        "projects": Project.get_published(),
    }
    return render(request, "index.html", context)