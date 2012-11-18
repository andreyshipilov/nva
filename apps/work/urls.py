from django.conf.urls.defaults import patterns, url

from .views import Index, Product


urlpatterns = patterns("",
    url(r"^$", Index.as_view(), name="products_index"),
    url(r"^(?P<pk>\d+)/$", Product.as_view(), name="products_item"),
)
