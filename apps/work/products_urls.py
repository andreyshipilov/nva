from django.conf.urls.defaults import patterns, url

from .views import ProductsIndex, product


urlpatterns = patterns("",
    url(r"^$", ProductsIndex.as_view(), name="products_index"),
    url(r"^(?P<pk>\d+)/$", product, name="products_item"),
)
