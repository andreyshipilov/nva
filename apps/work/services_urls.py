from django.conf.urls.defaults import patterns, url

from .views import ServicesIndex, service


urlpatterns = patterns("",
    url(r"^$", ServicesIndex.as_view(), name="services_index"),
    url(r"^(?P<pk>\d+)/$", service, name="services_item"),
)
