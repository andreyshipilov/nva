from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from reviews.views import Index as ReviewsIndex
from legal.views import Index as LegalIndex
from projects.views import Index as ProjectsIndex


admin.autodiscover()






urlpatterns = patterns('',
    ('^admin/', include(admin.site.urls)),
    url(r'^captcha/(?P<code>[\da-f]{32})/$', 'supercaptcha.draw'),

    url(r'^news/', include('news.urls')),
    url(r'^products/', include('work.products_urls')),
    url(r'^services/', include('work.services_urls')),
    url(r'^reviews/$', ReviewsIndex.as_view(), name='reviews',),
    url(r'^licenses_patents/$', LegalIndex.as_view(), name='licenses_patents',),
    url(r'^projects/$', ProjectsIndex.as_view(), name='projects'),

    url('^$', 'views.index', name='home'),
    ('^', include('mezzanine.urls')),
)

handler500 = 'mezzanine.core.views.server_error'


from copy import deepcopy

#from mezzanine.forms.admin import FormAdmin
#from mezzanine.forms.models import Form
#from mezzanine.galleries.admin import GalleryAdmin
#from mezzanine.galleries.models import Gallery
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import RichTextPage


#from mezzanine.pages.admin import PageAdmin
#from mezzanine.pages.models import Page
from sorl.thumbnail.admin import AdminImageMixin
#
pages_fieldsets = deepcopy(PageAdmin.fieldsets)
pages_fieldsets[0][1]['fields'] += ('image',)
#PageAdmin.fieldsets = pages_fieldsets

#
class MyRichTextPageAdmin(AdminImageMixin, PageAdmin):
    fieldsets = pages_fieldsets
#
#admin.site.unregister(Page)
#admin.site.register(Page, MyPageAdmin)

#admin.site.unregister(Form)
#admin.site.register(Form, FormAdmin)
#admin.site.unregister(Gallery)
#admin.site.register(Gallery, GalleryAdmin)
admin.site.unregister(RichTextPage)
#admin.site.register(RichTextPage, MyRichTextPageAdmin)
