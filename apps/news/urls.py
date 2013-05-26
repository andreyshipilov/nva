from django.conf.urls.defaults import patterns, url

from .views import Index, Item


urlpatterns = patterns("",
    url(r"^$", Index.as_view(), name="news_index"),
    url(r"^(?P<pk>\d+)/$", Item.as_view(), name="news_item"),
)
