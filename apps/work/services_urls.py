from django.conf.urls.defaults import patterns, url

from .views import ServicesIndex, Service


urlpatterns = patterns("",
    url(r"^$", ServicesIndex.as_view(), name="services_index"),
    url(r"^(?P<pk>\d+)/$", Service.as_view(), name="services_item"),
)
