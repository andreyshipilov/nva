from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from reviews.views import Index as ReviewsIndex
from legal.views import Index as LegalIndex


admin.autodiscover()
urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),
    
    url(r"^news/", include("news.urls")),
    url(r"^reviews/$", ReviewsIndex.as_view(), name="reviews",),
    url(r"^licenses_patents/$", LegalIndex.as_view(), name="licenses_patents",),
    
    url("^$", "views.index", name="home"),
    ("^", include("mezzanine.urls")),
)

handler500 = "mezzanine.core.views.server_error"
