from django.conf.urls.defaults import patterns, url

from .views import ProductsIndex, Product


urlpatterns = patterns("",
    url(r"^$", ProductsIndex.as_view(), name="products_index"),
    url(r"^(?P<pk>\d+)/$", Product.as_view(), name="products_item"),
)
