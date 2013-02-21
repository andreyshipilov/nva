from django.shortcuts import get_object_or_404, render

from news.models import NewsItem
from people.models import Human
from projects.models import Project
from banners.models import Banner


def index(request):
    context = {
        "news": NewsItem.objects.published()[:3],
        "projects": Project.get_published(),
        "banners": Banner.get_random(),
        "human": Human.get_one_for_index(),
    }
    return render(request, "index.html", context)
