from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from reviews.views import Index as ReviewsIndex
from legal.views import Index as LegalIndex


admin.autodiscover()

#from copy import deepcopy
#from mezzanine.pages.admin import PageAdmin
#from mezzanine.pages.models import Page
#from sorl.thumbnail.admin import AdminImageMixin
#
#pages_fieldsets = deepcopy(PageAdmin.fieldsets)
#pages_fieldsets[0][1]['fields'].insert(-2, 'image')
#
#class MyPageAdmin(PageAdmin):
#    fieldsets = pages_fieldsets
#
#admin.site.unregister(Page)
#admin.site.register(Page, MyPageAdmin)

urlpatterns = patterns('',
    ('^admin/', include(admin.site.urls)),
    url(r'^captcha/(?P<code>[\da-f]{32})/$', 'supercaptcha.draw'),

    url(r'^news/', include('news.urls')),
    url(r'^products/', include('work.products_urls')),
    url(r'^services/', include('work.services_urls')),
    url(r'^reviews/$', ReviewsIndex.as_view(), name='reviews',),
    url(r'^licenses_patents/$', LegalIndex.as_view(), name='licenses_patents',),

    url('^$', 'views.index', name='home'),
    ('^', include('mezzanine.urls')),
)

handler500 = 'mezzanine.core.views.server_error'
