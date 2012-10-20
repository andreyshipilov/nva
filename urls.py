from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from mezzanine.core.views import direct_to_template

from news.models import NewsItem


admin.autodiscover()

urlpatterns = patterns("",
    url(r"^news/", include("news.urls")),
    ("^admin/", include(admin.site.urls)),
    url("^$", direct_to_template, {
        "template": "index.html",
        "extra_context": {
            "news": NewsItem.get_published()[:4],
        }
    }, name="home"),
    ("^", include("mezzanine.urls")),
)

handler500 = "mezzanine.core.views.server_error"
